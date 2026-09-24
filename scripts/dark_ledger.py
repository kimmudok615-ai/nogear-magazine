#!/usr/bin/env python3
"""다크사이드 계정 원장 — 한 줄 = 한 콘텐츠의 상태 변화 (append-only).

상태: picked → drafted → guarded → rendered → queued → posted → measured
      실패 갈래: copy_failed · held (가드 HOLD) · render_failed
"""
import datetime as dt
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LEDGER = ROOT / "data" / "dark_ledger.jsonl"
STATES = ("picked", "drafted", "guarded", "rendered", "queued", "posted", "measured",
          "copy_failed", "held", "render_failed")
RETRYABLE = ("copy_failed", "render_failed")


def append(item_id, state, path=LEDGER, **extra):
    if state not in STATES:
        raise ValueError(f"모르는 상태 {state}")
    path.parent.mkdir(parents=True, exist_ok=True)
    row = {"id": item_id, "state": state, "at": dt.datetime.now().isoformat(timespec="seconds"), **extra}
    with path.open("a", encoding="utf-8") as f:
        f.write(json.dumps(row, ensure_ascii=False) + "\n")
    return row


def rows(path=LEDGER):
    if not path.exists():
        return []
    out = []
    for line in path.read_text(encoding="utf-8").splitlines():
        try:
            out.append(json.loads(line))
        except json.JSONDecodeError:
            continue  # 깨진 줄은 건너뛴다 — 원장 전체를 버리지 않는다
    return out


def latest(path=LEDGER):
    """id → 마지막 행."""
    last = {}
    for r in rows(path):
        last[r["id"]] = r
    return last


def used_fact_ids(days=30, path=LEDGER, today=None):
    """최근 days 일 안에 picked 된 팩트. 재사용 방지.
    우리 쪽 사정(카피 모델 꺼짐·렌더 실패)으로 끝난 건은 팩트를 태우지 않는다."""
    today = today or dt.date.today()
    cut = today - dt.timedelta(days=days)
    last = latest(path)
    used = set()
    for r in rows(path):
        if (r["state"] == "picked" and dt.date.fromisoformat(r["at"][:10]) >= cut
                and last[r["id"]]["state"] not in RETRYABLE):
            used |= set(r.get("fact_ids", []))
    return used
