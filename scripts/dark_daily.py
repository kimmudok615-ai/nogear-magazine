#!/usr/bin/env python3
"""다크사이드 계정 하루치 — 캐러셀 2편을 고르고·쓰고·가드하고·렌더해서 게시 대기열에 올린다.

2026-09-24 결정: 매일 2편 · 카피는 로컬 GPT 우선 · 승인 없이 자동 게시.
→ 사람 승인 대신 dark_guard 가 유일한 문이다. HOLD 된 편은 고치지 않고 다음 후보로 넘어간다.
게시 자체(인스타 업로드)는 아직 없다: 대기열(data/dark_publish_queue.jsonl)까지만.

사용: python3 scripts/dark_daily.py [--count 2] [--date 20260925] [--account ngr] [--brand neutral] [--no-png]
종료코드: 0 = 목표 편수 채움 · 1 = 일부만 · 2 = 0편
"""
import argparse
import datetime as dt
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import dark_copywriter  # noqa: E402
import dark_guard  # noqa: E402
import dark_jev  # noqa: E402
import dark_ledger  # noqa: E402
import dark_picker  # noqa: E402
import dark_reel  # noqa: E402
import dark_viral  # noqa: E402
import generate_dark_cardnews as gen  # noqa: E402

ROOT = gen.ROOT
QUEUE = ROOT / "data" / "dark_publish_queue.jsonl"
MAX_TRIES = 6  # 하루에 카피를 쓰는 최대 횟수 — 가드가 계속 막으면 멈추고 보고


def step(msg):
    """진행 상황을 바로 찍는다 — 카피 작성이 몇 분 걸려 «멈춘 것처럼» 보였다(9/25 맥)."""
    print(f"  · {dt.datetime.now():%H:%M:%S} {msg}", flush=True)


# 축별 해시태그 — 과하지 않게 5개. 숫자 없음(가드의 숫자 규칙과 부딪히지 않게).
HASHTAGS = {
    "tactics": "#내추럴 #가짜내추럴 #헬스 #STAYNATURAL #NGR",
    "body_cost": "#스테로이드부작용 #심장건강 #보디빌딩 #STAYNATURAL #NGR",
    "hidden": "#보충제 #성분표 #헬스 #STAYNATURAL #NGR",
    "drugs": "#스테로이드 #약물 #보디빌딩 #STAYNATURAL #NGR",
    "sport": "#도핑 #스포츠 #헬스 #STAYNATURAL #NGR",
    "law": "#스테로이드 #약물의이면 #보디빌딩 #STAYNATURAL #NGR",
}


HEDGE = r"단정할 수 없|단정하지 않|연구 한계|한계가 있|확정할 수 없|일반화할 수 없|인과관계.{0,6}(아니|없)"


def hook_score(h):
    """표지 훅 점수 — dark_viral 의 실측 공식 점수 + 길이 + 면책 감점."""
    h = re.sub(r"\*", "", str(h))
    pts, _ = dark_viral.hook_points(h)
    pts += 5 if 10 <= len(h) <= 32 else -10
    pts -= 30 if re.search(HEDGE, h) else 0
    return pts


def best_hook(obj):
    """모델이 준 훅 후보와 원래 표지 중 점수가 가장 높은 것."""
    cover = next((x for x in obj.get("slides", []) if x.get("kind") == "cover"), None)
    options = [str(h) for h in obj.get("hooks") or [] if str(h).strip()]
    if cover and cover.get("text"):
        options.append(cover["text"])
    listed = [o for o in options if dark_viral.has_list_hook(o)]  # 목록형(TOP N·N가지) 후보가 있으면 그중에서
    return max(listed or options, key=hook_score) if options else None


def assemble(obj, pick):
    f = pick["fact"]
    slides = [dict(x) for x in obj["slides"]]
    hook = best_hook(obj)
    if hook and slides and slides[0].get("kind") == "cover":
        if "*" not in hook:  # 강조어가 없으면 가장 센 낱말에 붉은 강조
            m = re.search(r"아무도|절대|숨기는|속고|진짜|마지막|\d+\s*가지", hook)
            hook = hook.replace(m.group(0), f"*{m.group(0)}*", 1) if m else hook
        slides[0]["text"] = hook
    # 면책·변명 문장은 슬라이드에서 빼고 캡션 끝으로 (본문 흐름을 끊지 않게)
    moved = [x for x in slides[1:-1] if re.search(HEDGE, " ".join(str(v) for v in x.values()))]
    slides = [x for x in slides if x not in moved]
    caption = list(obj.get("caption") or [])
    if hook:
        caption = [re.sub(r"\*", "", hook)] + [c for c in caption[1:]]
    if obj.get("comment_prompt"):
        caption += ["", str(obj["comment_prompt"]).strip()]
    for x in moved:
        caption.append("※ " + re.sub(r"\*", "", str(x.get("text") or x.get("label") or "")).replace("\n", " "))
    caption.append("저장해두고, 속고 있는 친구에게 보내라.")
    if f.get("source"):
        caption.append(f"원문: {f['source']}")
    caption += ["", HASHTAGS.get(pick["axis"], "#다크사이드")]
    return {
        "id": f"{pick['axis']}_{pick['fact_id']}",
        "tag": str(obj.get("tag") or pick["axis"].upper())[:24],
        "bg": pick["bg"],
        "slides": slides,
        "caption": caption,
        "fact_ids": [pick["fact_id"]],
        "facts": [f"{f['title']} — factchecks: {f.get('accuracy')}"],
        **({"thread": obj["thread"]} if isinstance(obj.get("thread"), dict) else {}),
    }


def run(count=2, date=None, brand="neutral", png=True, facts=None, ledger=dark_ledger.LEDGER,
        queue=QUEUE, writer=None, reels=True, suffix="dark_auto", axes_allowed=None, trends=None,
        reviewer=None):
    writer = writer or dark_copywriter.write
    date = date or dt.date.today().strftime("%Y%m%d")
    gen.set_brand(brand)
    facts = dark_guard.load_facts() if facts is None else facts
    out = gen.CARDNEWS / f"{date}_{suffix}"
    used = dark_ledger.used_fact_ids(path=ledger)
    try:
        import dark_measure
        weights = dark_measure.axis_weights(ledger)
    except Exception:  # noqa: BLE001 — 학습이 없어도 하루치는 돈다
        weights = {}
    pool = dark_picker.candidates(facts, used, weights)
    dark_copywriter.TREND_HINT = ""
    if trends:  # 커뮤니티·뉴스 화제(dark_trends) — 뜨거운 축·낱말 팩트를 앞으로. 사실 근거는 아니다
        import dark_trends
        pool = sorted(((sc * dark_trends.boost(f, trends), fid, ax, f) for sc, fid, ax, f in pool),
                      key=lambda c: (-c[0], c[1]))
        dark_copywriter.TREND_HINT = dark_trends.hint(trends)
        step("화제 반영: " + ", ".join(list(trends.get("terms", {}))[:5]))
    if axes_allowed:  # 계정마다 다루는 축이 다를 수 있다(config/accounts.json)
        pool = [c for c in pool if c[2] in axes_allowed]
    made, tries, axes, report = [], 0, set(), []

    for _, fid, axis, fact in pool:
        if len(made) == count or tries >= MAX_TRIES:
            break
        if axis in axes:
            continue
        tries += 1
        pick = {"fact_id": fid, "axis": axis, "fact": fact, "bg": dark_picker.BG[axis]}
        item = f"{date}_{axis}_{fid}"
        dark_ledger.append(item, "picked", ledger, fact_ids=[fid], axis=axis)

        step(f"[{axis}] 카피 작성 중 (GPT Luna → 로컬 LLM, 최대 몇 분) — {fact['title'][:40]}")
        obj, model, errs = writer(fact)
        if not obj:
            dark_ledger.append(item, "copy_failed", ledger, errors=errs)
            report.append(f"✗ {axis} 카피 실패: {'; '.join(errs)[:200]}")
            if all("JSON 없음" not in e for e in errs):
                report.append("■ 카피 모델이 모두 꺼져 있어 오늘은 멈춘다")
                break
            continue
        series = assemble(obj, pick)
        dark_ledger.append(item, "drafted", ledger, model=model)

        step(f"[{axis}] 카피 받음({model}) → 가드 검사" + (f" · 앞 모델 실패: {'; '.join(errs)[:160]}" if errs else ""))
        ok, why = dark_guard.check(series, facts)
        if ok:
            vs, vok, vnotes = dark_viral.score(series)
            if not vok:  # 바이럴 구조 미달 → 사유를 붙여 한 번 다시 쓰게 한다
                step(f"[{axis}] 바이럴 {vs}점 — 다시 쓰기: {'; '.join(vnotes)[:120]}")
                try:
                    obj2, model2, _ = writer(fact, feedback=vnotes)
                except TypeError:
                    obj2 = None
                if obj2:
                    s2 = assemble(obj2, pick)
                    ok2, why2 = dark_guard.check(s2, facts)
                    vs2, vok2, vnotes2 = dark_viral.score(s2)
                    if ok2 and vs2 >= vs:
                        series, vs, vok, vnotes, model = s2, vs2, vok2, vnotes2, model2
            if not vok and not dark_viral.has_list_hook(series["slides"][0].get("text")):
                s3 = dark_viral.force_list_hook(series)  # 두 번 다 목록형 표지가 없으면 코드가 붙인다
                ok3, _ = dark_guard.check(s3, facts)
                vs3, vok3, vnotes3 = dark_viral.score(s3)
                if ok3:
                    series, vs, vok, vnotes = s3, vs3, vok3, vnotes3
                    step(f"[{axis}] 표지 목록형 자동 보정 → {series['slides'][0]['text'].splitlines()[0]}")
            if not vok:
                ok, why = False, [f"바이럴 구조 {vs}점 < {dark_viral.PASS_SCORE}"] + vnotes
            else:
                series["viral_score"] = vs
        jev_log = None
        if ok and reviewer:  # JEV 심사위원 — 코드 ∥ JEV ∥ 로컬 LLM (섀도우: 위험 합의만 막는다)
            step(f"[{axis}] JEV 심사 (코드 ∥ JEV ∥ 로컬 LLM)")
            rv = reviewer(series)
            block, jlines, jrank = dark_jev.advice(rv)
            series["jev"] = {"notes": jlines, "rank": jrank}
            jev_log = {q: [v.get("answer"), v.get("status")] for q, v in (rv.get("questions") or {}).items()}
            jev_log["_code"] = dark_jev.code_answers(series)
            if block:
                ok, why = False, ["JEV·로컬 LLM 합의: 위험(too_risky)"] + jlines
        if not ok:
            dark_ledger.append(item, "held", ledger, hold_reason=why, **({"jev": jev_log} if jev_log else {}))
            report.append(f"✗ {axis} HOLD: {'; '.join(why)[:200]}")
            continue
        dark_ledger.append(item, "guarded", ledger, **({"jev": jev_log} if jev_log else {}))

        d = out / series["id"]
        d.mkdir(parents=True, exist_ok=True)
        (d / "series.json").write_text(json.dumps(series, ensure_ascii=False, indent=2), encoding="utf-8")
        try:
            step(f"[{axis}] 가드 통과 → 카드 렌더")
            pairs = gen.build_series(series, d, f"../../assets/{series['bg']}", manual=False)
            reel = None
            if png:
                gen.render(pairs)
                if reels:
                    reel = dark_reel.build(series, d, gen.ACCOUNT, gen.render)
        except Exception as e:  # noqa: BLE001
            dark_ledger.append(item, "render_failed", ledger, error=str(e)[:200])
            report.append(f"✗ {axis} 렌더 실패: {e}")
            continue
        dark_ledger.append(item, "rendered", ledger, dir=str(d.relative_to(gen.ROOT)))

        queue.parent.mkdir(parents=True, exist_ok=True)
        with queue.open("a", encoding="utf-8") as q:
            q.write(json.dumps({"id": item, "dir": str(d.relative_to(gen.ROOT)), "account": "@" + gen.ACCOUNT["handle"],
                                "auto_publish": True,
                                "reel": str(reel.relative_to(gen.ROOT)) if reel else None, "queued_at": dt.datetime.now().isoformat(timespec="seconds")},
                               ensure_ascii=False) + "\n")
        dark_ledger.append(item, "queued", ledger)
        made.append(item)
        axes.add(axis)
        report.append(f"✓ {axis} {fact['title'][:40]} ({model})")

    return made, report


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--count", type=int, default=2)
    ap.add_argument("--date")
    ap.add_argument("--account", default=None, help="config/accounts.json 의 id (주면 브랜드·축·원장·폴더를 거기서)")
    ap.add_argument("--brand", choices=sorted(gen.BRANDS), default="neutral")
    ap.add_argument("--no-png", action="store_true")
    ap.add_argument("--no-reels", action="store_true")
    ap.add_argument("--no-jev", action="store_true", help="JEV 심사 끄기(판정 사슬 없이)")
    ap.add_argument("--test", action="store_true", help="임시 원장·대기열·출력 — 진짜 기록을 건드리지 않는다")
    a = ap.parse_args()
    kw = {}
    if a.account:
        import dark_accounts
        acc = dark_accounts.get(a.account)
        a.brand = acc.get("brand", a.brand)
        led, que = dark_accounts.paths(acc, ROOT)
        kw = {"ledger": led, "queue": que, "suffix": acc.get("out_suffix", "dark_auto"),
              "axes_allowed": acc.get("axes")}
    if a.test:
        import tempfile
        t = Path(tempfile.mkdtemp(prefix="dark_test_"))
        gen.CARDNEWS = t / "cardnews"
        gen.ROOT = t  # 경로 기록(relative_to)도 임시 폴더 기준으로 — 9/25 맥 시험 실행에서 여기서 죽었다
        kw.update({"ledger": t / "ledger.jsonl", "queue": t / "queue.jsonl"})
        print(f"시험 모드 — 출력: {t}")
    import dark_trends
    made, report = run(a.count, a.date, a.brand, not a.no_png, reels=not a.no_reels,
                       trends=dark_trends.load(), reviewer=None if a.no_jev else dark_jev.review, **kw)
    print("\n".join(report) or "후보 없음")
    print(f"완료 {len(made)}/{a.count}")
    sys.exit(0 if len(made) == a.count else (1 if made else 2))


if __name__ == "__main__":
    main()
