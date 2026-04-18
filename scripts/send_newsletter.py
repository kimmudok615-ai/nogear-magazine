#!/usr/bin/env python3
"""
NOGEAR Newsletter — 뉴스레터 발송기
newsletter.html에서 생성한 payload JSON을 읽고 Gmail SMTP로 발송.

사용법:
  python3 scripts/send_newsletter.py <payload.json>
  python3 scripts/send_newsletter.py ~/Downloads/newsletter_2026-04-18_payload.json

payload 구조:
{
  "subject": "📡 NOGEAR WEEKLY INTEL · 2026-04-18",
  "to": ["email1@example.com", "email2@example.com"],
  "html": "<!DOCTYPE html>...",
  "generated_at": "ISO timestamp"
}
"""

import smtplib, json, sys
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from pathlib import Path
from datetime import datetime, timezone, timedelta

KST = timezone(timedelta(hours=9))

# Gmail 인증 (기존 send_daily_email.py와 동일)
GMAIL_USER = "kimmudok615@gmail.com"
GMAIL_PASS = "vzos qvhz jjqb jbql"


def send(payload_path: str):
    path = Path(payload_path).expanduser()
    if not path.exists():
        print(f"❌ payload 파일 없음: {path}")
        sys.exit(1)

    with open(path, encoding='utf-8') as f:
        payload = json.load(f)

    subject = payload.get('subject', 'NOGEAR Newsletter')
    recipients = payload.get('to', [])
    html = payload.get('html', '')

    if not recipients:
        print("❌ 수신자 없음")
        sys.exit(1)

    print(f"📧 NOGEAR Newsletter 발송")
    print(f"   제목: {subject}")
    print(f"   수신자: {len(recipients)}명 — {', '.join(recipients[:3])}{'...' if len(recipients)>3 else ''}")
    print(f"   HTML: {len(html):,}자")

    success = []
    failed = []

    for recipient in recipients:
        recipient = recipient.strip()
        if not recipient or '@' not in recipient:
            continue
        try:
            msg = MIMEMultipart('alternative')
            msg['Subject'] = subject
            msg['From'] = f'NOGEAR Magazine <{GMAIL_USER}>'
            msg['To'] = recipient
            msg.attach(MIMEText(html, 'html', 'utf-8'))

            with smtplib.SMTP_SSL('smtp.gmail.com', 465, timeout=15) as server:
                server.login(GMAIL_USER, GMAIL_PASS)
                server.send_message(msg)
            success.append(recipient)
            print(f"   ✅ {recipient}")
        except Exception as e:
            failed.append(recipient)
            print(f"   ❌ {recipient} — {e}")

    # 리포트
    print()
    print(f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print(f"✅ 성공: {len(success)}")
    print(f"❌ 실패: {len(failed)}")
    if failed:
        print(f"   실패 리스트: {', '.join(failed)}")
    print(f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━")

    # 로그 저장
    log_path = Path(__file__).parent.parent / "content" / "editorial" / "newsletter_log.json"
    log_path.parent.mkdir(parents=True, exist_ok=True)

    logs = []
    if log_path.exists():
        try:
            with open(log_path, encoding='utf-8') as f:
                logs = json.load(f).get('logs', [])
        except: pass

    logs.append({
        "sent_at": datetime.now(timezone.utc).isoformat(),
        "sent_at_kst": datetime.now(KST).strftime('%Y-%m-%d %H:%M KST'),
        "subject": subject,
        "recipients_count": len(recipients),
        "success": success,
        "failed": failed,
    })
    # 최근 50건만 유지
    logs = logs[-50:]

    with open(log_path, 'w', encoding='utf-8') as f:
        json.dump({"logs": logs}, f, ensure_ascii=False, indent=2)
    print(f"📝 로그: {log_path}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("사용법: python3 scripts/send_newsletter.py <payload.json>")
        print("예시: python3 scripts/send_newsletter.py ~/Downloads/newsletter_2026-04-18_payload.json")
        sys.exit(1)
    send(sys.argv[1])
