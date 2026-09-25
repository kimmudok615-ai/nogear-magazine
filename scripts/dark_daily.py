#!/usr/bin/env python3
"""다크사이드 계정 하루치 — 캐러셀 2편을 고르고·쓰고·가드하고·렌더해서 게시 대기열에 올린다.

2026-09-24 결정: 매일 2편 · 카피는 로컬 GPT 우선 · 승인 없이 자동 게시.
→ 사람 승인 대신 dark_guard 가 유일한 문이다. HOLD 된 편은 고치지 않고 다음 후보로 넘어간다.
게시 자체(인스타 업로드)는 아직 없다: 대기열(data/dark_publish_queue.jsonl)까지만.

사용: python3 scripts/dark_daily.py [--count 2] [--date 20260925] [--brand neutral] [--no-png]
종료코드: 0 = 목표 편수 채움 · 1 = 일부만 · 2 = 0편
"""
import argparse
import datetime as dt
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import dark_copywriter  # noqa: E402
import dark_guard  # noqa: E402
import dark_ledger  # noqa: E402
import dark_picker  # noqa: E402
import dark_reel  # noqa: E402
import generate_dark_cardnews as gen  # noqa: E402

ROOT = gen.ROOT
QUEUE = ROOT / "data" / "dark_publish_queue.jsonl"
MAX_TRIES = 6  # 하루에 카피를 쓰는 최대 횟수 — 가드가 계속 막으면 멈추고 보고


def assemble(obj, pick):
    f = pick["fact"]
    return {
        "id": f"{pick['axis']}_{pick['fact_id']}",
        "tag": str(obj.get("tag") or pick["axis"].upper())[:24],
        "bg": pick["bg"],
        "slides": obj["slides"],
        "caption": obj.get("caption") or [],
        "fact_ids": [pick["fact_id"]],
        "facts": [f"{f['title']} — factchecks: {f.get('accuracy')}"],
        **({"thread": obj["thread"]} if isinstance(obj.get("thread"), dict) else {}),
    }


def run(count=2, date=None, brand="neutral", png=True, facts=None, ledger=dark_ledger.LEDGER,
        queue=QUEUE, writer=None, reels=True):
    writer = writer or dark_copywriter.write
    date = date or dt.date.today().strftime("%Y%m%d")
    gen.set_brand(brand)
    facts = dark_guard.load_facts() if facts is None else facts
    out = gen.CARDNEWS / f"{date}_dark_auto"
    used = dark_ledger.used_fact_ids(path=ledger)
    try:
        import dark_measure
        weights = dark_measure.axis_weights(ledger)
    except Exception:  # noqa: BLE001 — 학습이 없어도 하루치는 돈다
        weights = {}
    pool = dark_picker.candidates(facts, used, weights)
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

        ok, why = dark_guard.check(series, facts)
        if not ok:
            dark_ledger.append(item, "held", ledger, hold_reason=why)
            report.append(f"✗ {axis} HOLD: {'; '.join(why)[:200]}")
            continue
        dark_ledger.append(item, "guarded", ledger)

        d = out / series["id"]
        d.mkdir(parents=True, exist_ok=True)
        (d / "series.json").write_text(json.dumps(series, ensure_ascii=False, indent=2), encoding="utf-8")
        try:
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
    ap.add_argument("--brand", choices=sorted(gen.BRANDS), default="neutral")
    ap.add_argument("--no-png", action="store_true")
    ap.add_argument("--no-reels", action="store_true")
    ap.add_argument("--test", action="store_true", help="임시 원장·대기열·출력 — 진짜 기록을 건드리지 않는다")
    a = ap.parse_args()
    kw = {}
    if a.test:
        import tempfile
        t = Path(tempfile.mkdtemp(prefix="dark_test_"))
        gen.CARDNEWS = t / "cardnews"
        gen.ROOT = t  # 경로 기록(relative_to)도 임시 폴더 기준으로 — 9/25 맥 시험 실행에서 여기서 죽었다
        kw = {"ledger": t / "ledger.jsonl", "queue": t / "queue.jsonl"}
        print(f"시험 모드 — 출력: {t}")
    made, report = run(a.count, a.date, a.brand, not a.no_png, reels=not a.no_reels, **kw)
    print("\n".join(report) or "후보 없음")
    print(f"완료 {len(made)}/{a.count}")
    sys.exit(0 if len(made) == a.count else (1 if made else 2))


if __name__ == "__main__":
    main()
