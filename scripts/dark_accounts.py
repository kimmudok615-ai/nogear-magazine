#!/usr/bin/env python3
"""계정 목록 — config/accounts.json. 같은 공장으로 계정 여러 개를 돌린다(2026-09-27 Andy).

계정마다 따로: 브랜드(카드 이름·핸들), 쓰는 축, 출력 폴더 꼬리(<날짜>_<out_suffix>), 원장, 대기열.
같이 쓰는 것: 팩트 원장·연구 소재·가드·바이럴 검사·렌더러.

사용: python3 scripts/dark_accounts.py --enabled   → 켜진 계정 id 를 한 줄씩
"""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CONFIG = ROOT / "config" / "accounts.json"
DEFAULT = "ngr"


def load(path=CONFIG):
    if not path.exists():
        return [{"id": DEFAULT, "handle": "ngr_magazine", "brand": "neutral", "enabled": True, "count": 2,
                 "out_suffix": "dark_auto", "ledger": "data/dark_ledger.jsonl",
                 "queue": "data/dark_publish_queue.jsonl"}]
    return json.loads(path.read_text(encoding="utf-8"))["accounts"]


def get(acc_id=DEFAULT, path=CONFIG):
    for a in load(path):
        if a["id"] == acc_id:
            return a
    raise KeyError(f"계정 없음: {acc_id} (config/accounts.json)")


def paths(acc, root=ROOT):
    """계정 → (원장, 대기열) 절대경로."""
    return root / acc["ledger"], root / acc["queue"]


if __name__ == "__main__":
    if "--enabled" in sys.argv:
        print("\n".join(a["id"] for a in load() if a.get("enabled")))
    else:
        print(json.dumps(load(), ensure_ascii=False, indent=1))
