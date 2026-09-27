#!/usr/bin/env python3
"""컨트롤타워 — 계정 여러 개를 한 화면에서 본다(2026-09-27 Andy «추후에 컨트롤타워도»).

config/accounts.json 의 계정마다:
  오늘 만든 편·올릴 키트 · 원장 상태(대기/게시/보류) · 남은 소재 · 팔로워 추이 · 마지막 실행 · 경보
→ tower/index.html (사람용, Vercel 에 그대로 뜬다) + tower/status.json (기계용)
읽기만 한다. 게시·자격증명·스케줄은 건드리지 않는다.
측정 못 한 값은 0 이 아니라 «—»(None) 으로 둔다.

사용: python3 scripts/tower.py [--date 20260927]
"""
import argparse
import datetime as dt
import html
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import dark_accounts  # noqa: E402
import dark_ledger  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
STALE_H = 26          # 하루 한 번 도는 러너 — 26시간 넘게 소식 없으면 멈춘 것
LOW_FACTS = 6         # 남은 소재가 사흘치(하루 2편) 아래면 경보
POST_STATES = ("posted", "measured")


def _facts_left(ledger, axes):
    try:
        import dark_guard
        import dark_picker
        pool = dark_picker.candidates(dark_guard.load_facts(), dark_ledger.used_fact_ids(path=ledger))
        return sum(1 for c in pool if not axes or c[2] in axes)
    except Exception:  # noqa: BLE001 — 소재를 못 읽으면 UNKNOWN
        return None


def _followers(acc, root):
    p = root / acc.get("account_log", "data/dark_account.jsonl")
    if not p.exists():
        return None, None
    rows = [json.loads(x) for x in p.read_text(encoding="utf-8").splitlines() if x.strip()]
    rows = [r for r in rows if isinstance(r.get("followers"), int)]
    if not rows:
        return None, None
    week = [r for r in rows if r["at"][:10] >= (dt.date.today() - dt.timedelta(days=7)).isoformat()]
    return rows[-1]["followers"], (rows[-1]["followers"] - week[0]["followers"]) if week else None


def _last_run(root, now):
    st = root / "ops" / "status"
    p = next((x for x in (st / "last_run_daily.txt", st / "last_run.txt") if x.exists()), None)
    if p is None:
        return None, None
    first = p.read_text(encoding="utf-8").splitlines()[:1]
    age_h = (now.timestamp() - p.stat().st_mtime) / 3600
    return (first[0] if first else "?"), round(age_h, 1)


def account_status(acc, date, root=ROOT, now=None):
    now = now or dt.datetime.now()
    ledger, _ = dark_accounts.paths(acc, root)
    last = dark_ledger.latest(ledger)
    states = [r["state"] for r in last.values()]
    day = root / "cardnews" / f"{date}_{acc.get('out_suffix', 'dark_auto')}"
    today = []
    for sj in sorted(day.glob("*/series.json")) if day.exists() else []:
        s = json.loads(sj.read_text(encoding="utf-8"))
        cover = next((x.get("text", "") for x in s.get("slides", []) if x.get("kind") == "cover"), "")
        item = f"{date}_{sj.parent.name}"
        today.append({"dir": str(sj.parent.relative_to(root)), "hook": " ".join(cover.replace("*", "").split()),
                      "viral": s.get("viral_score"), "state": last.get(item, {}).get("state", "—"),
                      "cards": len(list(sj.parent.glob("[0-9][0-9]_*.png"))),
                      "cover": next(iter(sorted(sj.parent.glob("[0-9][0-9]_*.png"))), None)})
        today[-1]["cover"] = today[-1]["cover"].name if today[-1]["cover"] else None
    followers, week_delta = _followers(acc, root)
    run_line, run_age = _last_run(root, now)
    st = {
        "id": acc["id"], "handle": acc.get("handle"), "name": acc.get("name", acc["id"]),
        "enabled": bool(acc.get("enabled")), "target": acc.get("count", 2),
        "today": today, "kit": str((day / "POST_TODAY.md").relative_to(root)) if (day / "POST_TODAY.md").exists() else None,
        "queued": states.count("queued"), "posted": sum(s in POST_STATES for s in states),
        "held": states.count("held"), "failed": sum(s.endswith("_failed") for s in states),
        "facts_left": _facts_left(ledger, acc.get("axes")),
        "followers": followers, "followers_7d": week_delta,
        "last_run": run_line, "last_run_age_h": run_age, "canva": acc.get("canva"),
    }
    alerts = []
    if not st["enabled"]:
        alerts.append("꺼짐")
    else:
        if run_age is None or run_age > STALE_H:
            alerts.append(f"러너 소식 없음 ({run_age if run_age is not None else '기록 없음'}h) — 맥 launchd 확인")
        if len(today) < st["target"]:
            alerts.append(f"오늘 {len(today)}/{st['target']}편 — 보류·소재 부족 사유는 ops/status 보고")
        if st["facts_left"] is not None and st["facts_left"] < LOW_FACTS:
            alerts.append(f"남은 소재 {st['facts_left']}건 — 연구 보충 필요")
        if st["queued"] > 2 * st["target"]:
            alerts.append(f"안 올린 편 {st['queued']}개 쌓임 — POST_TODAY.md 보고 게시")
    st["alerts"] = alerts
    return st


def _v(x):
    return "—" if x is None else html.escape(str(x))


def render(statuses, date, now):
    tok = json.loads((ROOT / "design" / "tokens.json").read_text(encoding="utf-8"))["color"]
    try:
        import dark_trends
        tr = dark_trends.load()
    except Exception:  # noqa: BLE001
        tr = None
    trend_html = ("<p class=m>🔥 이번 주 헬스 커뮤니티 화제: " + " · ".join(
        f"{html.escape(k)} {v}" for k, v in list(tr["terms"].items())[:8]) + "</p>") if tr and tr.get("terms") \
        else "<p class=m>🔥 화제 수집 없음(3일 이내)</p>"
    cards = []
    for s in statuses:
        rows = "".join(
            f"<li><b>{_v(t['viral'])}</b> {_v(t['hook'][:48])} <span class=m>· {t['cards']}장 · {_v(t['state'])}</span>"
            + (f" <a href='../{html.escape(t['dir'])}/{t['cover']}'>표지</a>" if t['cover'] else "") + "</li>" for t in s["today"]) or "<li class=m>없음</li>"
        alerts = "".join(f"<li>{html.escape(a)}</li>" for a in s["alerts"])
        fd = s["followers_7d"]
        cards.append(f"""<section class="card{' warn' if s['alerts'] else ''}">
<header><h2>@{_v(s['handle'])}</h2><span class=m>{_v(s['name'])}</span></header>
<div class=kpis>
 <div><i>팔로워</i><b>{_v(s['followers'])}</b><small>{'' if fd is None else f'{fd:+d} / 7일'}</small></div>
 <div><i>오늘</i><b>{len(s['today'])}/{s['target']}</b><small>편</small></div>
 <div><i>대기</i><b>{s['queued']}</b><small>안 올림</small></div>
 <div><i>게시</i><b>{s['posted']}</b><small>누적</small></div>
 <div><i>보류</i><b>{s['held']}</b><small>가드·바이럴</small></div>
 <div><i>소재</i><b>{_v(s['facts_left'])}</b><small>남음</small></div>
</div>
{f'<ul class=alerts>{alerts}</ul>' if alerts else '<p class=ok>이상 없음</p>'}
<h3>오늘 편 (바이럴 점수)</h3><ul class=today>{rows}</ul>
<p class=links>{f"<a href='../{html.escape(s['kit'])}'>📦 POST_TODAY.md</a>" if s['kit'] else '키트 없음'}
{f" · <a href='{html.escape(s['canva'])}'>Canva 템플릿</a>" if s['canva'] else ''}
 · 마지막 실행 {_v(s['last_run'])} ({_v(s['last_run_age_h'])}h 전)</p>
</section>""")
    return f"""<!doctype html><html lang=ko><head><meta charset=utf-8>
<meta name=viewport content="width=device-width,initial-scale=1"><title>NGR 컨트롤타워</title>
<style>
:root{{--bg:{tok['bg']};--ink:{tok['ink']};--accent:{tok['accent']};--muted:{tok['muted']};--faint:{tok['faint']}}}
*{{box-sizing:border-box}}body{{margin:0;background:var(--bg);color:var(--ink);font:15px/1.5 -apple-system,"Noto Sans KR",sans-serif;padding:24px 16px}}
h1{{font-size:20px;letter-spacing:.08em;margin:0 0 4px}}h1 em{{color:var(--accent);font-style:normal}}
.m,small,i{{color:var(--muted);font-style:normal}}.grid{{display:grid;gap:16px;grid-template-columns:repeat(auto-fit,minmax(320px,1fr));margin-top:20px}}
.card{{border:1px solid var(--faint);padding:16px}}.card.warn{{border-color:var(--accent)}}
header{{display:flex;gap:8px;align-items:baseline;flex-wrap:wrap}}h2{{margin:0;font-size:17px}}h3{{font-size:13px;color:var(--muted);margin:14px 0 4px}}
.kpis{{display:grid;grid-template-columns:repeat(3,1fr);gap:8px;margin-top:12px}}.kpis div{{background:#111;padding:8px}}
.kpis i{{display:block;font-size:11px}}.kpis b{{font-size:20px}}.kpis small{{display:block;font-size:11px}}
.alerts{{color:var(--accent);padding-left:18px}}.ok{{color:var(--muted)}}ul{{margin:4px 0;padding-left:18px}}
a{{color:var(--ink)}}.today b{{color:var(--accent)}}
</style></head><body>
<h1>NGR <em>CONTROL TOWER</em></h1>
<div class=m>{date} · 생성 {now:%Y-%m-%d %H:%M} (90분 넘게 지난 화면은 낡은 값) · 계정 {len(statuses)}개 · FXXK FAKES · STAY NATURAL</div>
{trend_html}
<div class=grid>{''.join(cards)}</div>
</body></html>"""


def build(date=None, root=ROOT, now=None):
    now = now or dt.datetime.now()
    date = date or now.strftime("%Y%m%d")
    statuses = [account_status(a, date, root, now) for a in dark_accounts.load()]
    out = root / "tower"
    out.mkdir(exist_ok=True)
    (out / "status.json").write_text(json.dumps({"generated": now.isoformat(timespec="seconds"), "date": date,
                                                 "accounts": statuses}, ensure_ascii=False, indent=1), encoding="utf-8")
    (out / "index.html").write_text(render(statuses, date, now), encoding="utf-8")
    return statuses


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--date")
    a = ap.parse_args()
    for s in build(a.date):
        print(f"🗼 @{s['handle']} 오늘 {len(s['today'])}/{s['target']} · 대기 {s['queued']} · 게시 {s['posted']} · "
              f"소재 {s['facts_left'] if s['facts_left'] is not None else '—'}"
              + (f" · ⚠ {'; '.join(s['alerts'])}" if s["alerts"] else ""))
