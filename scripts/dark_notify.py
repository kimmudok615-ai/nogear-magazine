#!/usr/bin/env python3
"""다크사이드 계정 하루 보고 → 노기어 텔레그램 봇(이미 있는 것).

TELEGRAM_BOT_TOKEN / TELEGRAM_CHAT_ID 를 쓰고, 없으면 ~/nogear/.env.cafe24 에서 읽는다
(노기어 telegram_dashboard_summary.py 와 같은 방식). 없으면 조용히 건너뛴다.
사용: python3 scripts/dark_notify.py < 보고.txt
"""
import json
import os
import sys
import urllib.request
from pathlib import Path


def creds():
    bot = os.getenv("TELEGRAM_BOT_TOKEN") or os.getenv("TELEGRAM_BOT", "")
    chat = os.getenv("TELEGRAM_CHAT_ID") or os.getenv("TELEGRAM_CHAT", "")
    env_f = Path(os.getenv("NOGEAR_ROOT", Path.home() / "nogear")) / ".env.cafe24"
    if (not bot or not chat) and env_f.exists():
        for line in env_f.read_text(encoding="utf-8").splitlines():
            k, _, v = line.partition("=")
            v = v.strip().strip('"').strip("'")
            if k.strip() in ("TELEGRAM_BOT_TOKEN", "TELEGRAM_BOT") and not bot:
                bot = v
            if k.strip() in ("TELEGRAM_CHAT_ID", "TELEGRAM_CHAT") and not chat:
                chat = v
    return bot, chat


def send(text):
    if os.getenv("PYTEST_CURRENT_TEST") or os.getenv("NOGEAR_NO_TELEGRAM"):
        return False
    bot, chat = creds()
    if not bot or not chat:
        print("텔레그램 자격증명 없음 — 보고 생략")
        return False
    body = json.dumps({"chat_id": chat, "text": text[:3900], "disable_web_page_preview": True}).encode()
    req = urllib.request.Request(f"https://api.telegram.org/bot{bot}/sendMessage", data=body,
                                 headers={"Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=15) as r:  # noqa: S310 — api.telegram.org 고정
            return r.status == 200
    except Exception as e:  # noqa: BLE001
        print(f"텔레그램 발송 오류: {type(e).__name__}")
        return False


if __name__ == "__main__":
    send("🌑 다크사이드 하루치\n" + sys.stdin.read())
