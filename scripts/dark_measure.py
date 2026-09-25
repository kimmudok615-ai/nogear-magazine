#!/usr/bin/env python3
"""다크사이드 계정 측정 → 학습.

게시 48시간 뒤 Graph API 인사이트(무료)로 도달·저장·공유를 읽어 원장에 measured 로 남기고,
축(axis)별 «저장률 = 저장/도달» 로 다음 소재 고르기에 가중치를 준다.
표본이 3편 미만인 축은 1.0 (모르는 것은 모른다 — 0 으로 벌주지 않는다).

사용: python3 scripts/dark_measure.py
"""
import datetime as dt
import os
import statistics
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import dark_ledger  # noqa: E402
import dark_publish  # noqa: E402

METRICS = "reach,saved,shares,total_interactions"
MIN_AGE_H = 48
MIN_SAMPLES = 3


def due(ledger=dark_ledger.LEDGER, now=None):
    now = now or dt.datetime.now()
    last = dark_ledger.latest(ledger)
    out = []
    for r in last.values():
        if r["state"] == "posted" and r.get("media_id"):
            age = now - dt.datetime.fromisoformat(r["at"])
            if age >= dt.timedelta(hours=MIN_AGE_H):
                out.append(r)
    return out


def read_insights(media_id, token, call=dark_publish.http):
    data = call("GET", f"{dark_publish.GRAPH}/{media_id}/insights",
                {"metric": METRICS, "access_token": token}).get("data", [])
    return {m["name"]: (m.get("values") or [{}])[0].get("value") for m in data}


def run(ledger=dark_ledger.LEDGER, call=dark_publish.http, now=None):
    token = os.getenv("DARK_IG_TOKEN", "").strip()
    items = due(ledger, now)
    if not items:
        return ["측정할 게시물 없음"]
    if not token:
        return ["측정 안 함 — DARK_IG_TOKEN 없음"]
    rep = []
    for r in items:
        try:
            m = read_insights(r["media_id"], token, call)
        except dark_publish.PublishError as e:
            rep.append(f"✗ {r['id']}: {e}")
            continue
        dark_ledger.append(r["id"], "measured", ledger, metrics=m, media_id=r["media_id"])
        rep.append(f"✓ {r['id']} 도달 {m.get('reach')} · 저장 {m.get('saved')} · 공유 {m.get('shares')}")
    return rep


def axis_weights(ledger=dark_ledger.LEDGER):
    """축 → 가중치(0.5~2.0). 전체 평균 저장률 대비 그 축의 저장률."""
    rates, axis_of = {}, {}
    for r in dark_ledger.rows(ledger):
        if r["state"] == "picked":
            axis_of[r["id"]] = r.get("axis")
        if r["state"] == "measured":
            m = r.get("metrics") or {}
            reach, saved = m.get("reach") or 0, m.get("saved") or 0
            if reach and axis_of.get(r["id"]):
                rates.setdefault(axis_of[r["id"]], []).append(saved / reach)
    every = [x for v in rates.values() for x in v]
    if not every or statistics.mean(every) == 0:
        return {}
    base = statistics.mean(every)
    return {a: max(0.5, min(2.0, statistics.mean(v) / base))
            for a, v in rates.items() if len(v) >= MIN_SAMPLES}


if __name__ == "__main__":
    print("\n".join(run()))
    print("축 가중치:", axis_weights() or "표본 부족")
