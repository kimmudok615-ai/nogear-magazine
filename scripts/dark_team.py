#!/usr/bin/env python3
"""계정 하나 = 회사 하나 — 역할별 오늘 상태판 (config/team.json).

역할은 따로 도는 봇이 아니라 매일 러너(ops/dark_daily.sh) 안의 단계다. 주인은 편집장 하나.
이 모듈은 이미 남은 흔적(원장·화제·검증 파일·오늘 폴더)만 읽어 «누가 오늘 일을 했나/막혔나»를 판정한다.
측정 못 한 건 «—». 상태: ok(했다) · warn(막힘·주의) · idle(오늘 할 일 없음/못 잼)
"""
import datetime as dt
import json
import statistics
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import dark_ledger  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
TEAM = ROOT / "config" / "team.json"


def roles(path=TEAM):
    return json.loads(path.read_text(encoding="utf-8"))["roles"]


def _today_rows(ledger, date):
    return [r for r in dark_ledger.rows(ledger) if str(r.get("id", "")).startswith(f"{date}_")]


def board(st, date, ledger, root=ROOT, trends=None, audit=None):
    """st = tower.account_status 결과. → [{id, name, state, detail}]"""
    rows = _today_rows(ledger, date)
    states = [r["state"] for r in rows]
    tried = len({r["id"] for r in rows if r["state"] == "picked"})
    held = [r for r in rows if r["state"] == "held"]
    viral_held = sum(1 for r in held if any("바이럴" in str(w) for w in r.get("hold_reason", [])))
    jev_held = sum(1 for r in held if any("JEV" in str(w) for w in r.get("hold_reason", [])))
    today = st.get("today", [])
    vs = [t["viral"] for t in today if isinstance(t.get("viral"), (int, float))]
    judged = sum(1 for r in rows if r["state"] == "guarded" and r.get("jev"))
    jev_decided = sum(1 for r in rows if r["state"] == "guarded"
                      for q, v in (r.get("jev") or {}).items() if not q.startswith("_") and v and v[1] == "decided")
    live = [k for k, v in ((trends or {}).get("sources") or {}).items() if str(v).endswith("건") and not str(v).startswith("0")]
    ready = [q for q, v in ((audit or {}).get("questions") or {}).items() if v.get("evidenceVerdict") == "real_evidence"]
    target, made = st.get("target", 2), len(today)

    def s(ok, warn=False):
        return "warn" if warn else ("ok" if ok else "idle")

    info = {
        "editor": (s(made >= target, made < target and bool(rows)), f"{made}/{target}편 · 시도 {tried}"),
        "trend": (s(bool(trends), not trends), f"소스 {len(live)}곳 살아 있음" if trends else "화제 없음(3일 이내)"),
        "fact": (s(st.get("facts_left") is not None, (st.get("facts_left") or 99) < 6),
                 f"남은 소재 {st.get('facts_left') if st.get('facts_left') is not None else '—'}"),
        "planner": (s(tried > 0), f"후보 {tried}건 배정"),
        "copy": (s(states.count("drafted") > 0, states.count("copy_failed") > 0),
                 f"작성 {states.count('drafted')} · 실패 {states.count('copy_failed')}"),
        "safety": (s(bool(rows)), f"보류 {len(held) - viral_held - jev_held}"),
        "viral": (s(bool(vs), viral_held > 0 and not vs),
                  f"평균 {round(statistics.mean(vs)) if vs else '—'}점 · 탈락 {viral_held}"),
        "jev": (s(judged > 0, bool(rows) and judged == 0 and states.count("guarded") > 0),
                f"심사 {judged}편 · 합의 {jev_decided}문항 · 위험 보류 {jev_held}"),
        "design": (s(any(t.get("cards") for t in today)),
                   f"카드 {sum(t.get('cards', 0) for t in today)}장"),
        "publish": (s(bool(st.get("kit")), st.get("queued", 0) > 2 * target),
                    f"키트 {'있음' if st.get('kit') else '없음'} · 안 올린 편 {st.get('queued', 0)}"),
        "analyst": (s((audit or {}).get("measured", 0) > 0),
                    f"측정 {(audit or {}).get('measured', 0)}편 · 근거 문항 {', '.join(ready) or '없음'}"),
    }
    out = []
    for r in roles():
        state, detail = info.get(r["id"], ("idle", "—"))
        out.append({"id": r["id"], "name": r["name"], "tier": r["tier"], "state": state, "detail": detail})
    return out


def load_audit(root=ROOT):
    p = root / "content" / "dark" / "jev_audit.json"
    try:
        return json.loads(p.read_text(encoding="utf-8"))
    except Exception:  # noqa: BLE001
        return None


if __name__ == "__main__":
    import tower
    import dark_accounts
    import dark_trends
    date = sys.argv[1] if len(sys.argv) > 1 else dt.date.today().strftime("%Y%m%d")
    for acc in dark_accounts.load():
        st = tower.account_status(acc, date)
        led, _ = dark_accounts.paths(acc)
        print(f"@{acc['handle']}")
        for b in board(st, date, led, trends=dark_trends.load(), audit=load_audit()):
            mark = {"ok": "✓", "warn": "⚠", "idle": "·"}[b["state"]]
            print(f"  {mark} {b['name']:<8} {b['detail']}")
