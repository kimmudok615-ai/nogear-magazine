#!/usr/bin/env python3
"""
NOGEAR Magazine — Digest Sender
Telegram + Gmail 자동 발송
크롤 후 자동 호출되어 TOP 아티클 다이제스트 전송
"""

import os
import json
import smtplib
import urllib.request
import urllib.parse
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime, timezone, timedelta
from pathlib import Path

KST = timezone(timedelta(hours=9))
CONTENT_FILE = Path(__file__).parent.parent / "content" / "articles.json"

# ── TELEGRAM CONFIG ──
TELEGRAM_BOT = os.environ.get("TELEGRAM_BOT", "8660683197:AAG")  # fallback prefix
TELEGRAM_CHAT = os.environ.get("TELEGRAM_CHAT", "8536675465")

# ── GMAIL CONFIG ──
GMAIL_USER = os.environ.get("GMAIL_USER", "")
GMAIL_APP_PASSWORD = os.environ.get("GMAIL_APP_PASSWORD", "")
GMAIL_TO = os.environ.get("GMAIL_TO", "")


def load_articles():
    with open(CONTENT_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def build_digest(data: dict, top_n: int = 7) -> dict:
    """Build digest from articles data"""
    news = data.get("news", [])
    meta = data.get("meta", {})

    # Top articles by viral_score
    top = sorted(news, key=lambda x: x.get("viral_score", 0), reverse=True)[:top_n]

    # Stats
    total = len(news)
    avg_score = sum(a.get("viral_score", 0) for a in news[:20]) / min(20, len(news)) if news else 0
    verified = sum(1 for a in news if a.get("credibility", {}).get("cross_checked"))
    crawl_n = meta.get("crawl_count", 0)

    return {
        "top": top,
        "total": total,
        "avg_score": round(avg_score, 1),
        "verified": verified,
        "crawl_count": crawl_n,
        "timestamp": datetime.now(KST).strftime("%Y-%m-%d %H:%M KST"),
    }


def format_telegram(digest: dict) -> str:
    """Format digest for Telegram"""
    lines = [
        "📡 *NOGEAR MAGAZINE DIGEST*",
        f"🕐 {digest['timestamp']}",
        f"📊 총 {digest['total']}개 | 평균 바이럴 {digest['avg_score']} | ✅ 검증 {digest['verified']}개",
        "",
        "🏆 *TOP ARTICLES:*",
    ]

    for i, a in enumerate(digest["top"]):
        emoji = a.get("viral_emoji", "⚪")
        score = a.get("viral_score", 0)
        title_ko = a.get("title_ko", a.get("title", ""))
        cat = a.get("category", "")
        badge = ""
        cred = a.get("credibility", {})
        if cred.get("confidence") == "high":
            badge = " ✅"
        elif cred.get("confidence") == "medium":
            badge = " 🔍"

        lines.append(f"{i+1}. {emoji} *[{score}]* {title_ko}{badge}")
        lines.append(f"   _{cat} · {a.get('source', '')}_")

    lines.append("")
    lines.append(f"🔗 https://nogear-magazine.vercel.app")
    lines.append(f"_Crawl #{digest['crawl_count']}_")

    return "\n".join(lines)


def format_gmail_html(digest: dict) -> str:
    """Format digest as HTML email"""
    rows = ""
    for i, a in enumerate(digest["top"]):
        emoji = a.get("viral_emoji", "⚪")
        score = a.get("viral_score", 0)
        title = a.get("title", "")
        title_ko = a.get("title_ko", "")
        summary = a.get("summary", "")[:150]
        cat = a.get("category", "")
        source = a.get("source", "")
        url = a.get("source_url", "#")

        cred = a.get("credibility", {})
        badge = ""
        if cred.get("confidence") == "high":
            badge = '<span style="color:#10B981;">✅ VERIFIED</span>'
        elif cred.get("confidence") == "medium":
            badge = '<span style="color:#F59E0B;">🔍 CHECKED</span>'
        else:
            badge = '<span style="color:#666;">⚠️ UNVERIFIED</span>'

        score_color = "#FF2D20" if score >= 90 else "#F59E0B" if score >= 75 else "#3B82F6"

        rows += f"""
        <tr style="border-bottom:1px solid #1a1a2e;">
          <td style="padding:12px 8px;text-align:center;font-size:24px;">{emoji}</td>
          <td style="padding:12px 8px;">
            <div style="font-size:11px;color:{score_color};font-weight:800;margin-bottom:4px;">
              VIRAL {score} · {cat.upper()} {badge}
            </div>
            <div style="font-size:15px;font-weight:700;color:#F4F4F6;margin-bottom:4px;">
              {title_ko}
            </div>
            <div style="font-size:12px;color:#888;margin-bottom:4px;">
              {title}
            </div>
            <div style="font-size:11px;color:#666;line-height:1.5;">
              {summary}...
            </div>
            <div style="font-size:10px;color:#555;margin-top:6px;">
              📄 {source}
              {f' · <a href="{url}" style="color:#3B82F6;">LINK</a>' if url != '#' else ''}
            </div>
          </td>
        </tr>"""

    return f"""
    <html>
    <body style="margin:0;padding:0;background:#030306;font-family:'Helvetica Neue',Arial,sans-serif;">
      <div style="max-width:640px;margin:0 auto;background:#030306;padding:24px;">
        <!-- HEADER -->
        <div style="text-align:center;padding:20px 0;border-bottom:1px solid #1a1a2e;">
          <div style="font-size:18px;font-weight:900;color:#F4F4F6;letter-spacing:3px;">
            <span style="color:#FF2D20;">NO</span>GEAR
            <span style="font-size:9px;color:#555;letter-spacing:4px;margin-left:4px;">MAGAZINE</span>
          </div>
          <div style="font-size:10px;color:#555;margin-top:8px;letter-spacing:1px;">
            DAILY DIGEST · {digest['timestamp']}
          </div>
        </div>

        <!-- STATS -->
        <div style="display:flex;justify-content:center;gap:32px;padding:16px 0;text-align:center;">
          <div>
            <div style="font-size:20px;font-weight:800;color:#F4F4F6;">{digest['total']}</div>
            <div style="font-size:9px;color:#555;letter-spacing:1px;">ARTICLES</div>
          </div>
          <div>
            <div style="font-size:20px;font-weight:800;color:#FF2D20;">{digest['avg_score']}</div>
            <div style="font-size:9px;color:#555;letter-spacing:1px;">AVG VIRAL</div>
          </div>
          <div>
            <div style="font-size:20px;font-weight:800;color:#10B981;">{digest['verified']}</div>
            <div style="font-size:9px;color:#555;letter-spacing:1px;">VERIFIED</div>
          </div>
        </div>

        <!-- TOP ARTICLES -->
        <div style="padding:8px 0;">
          <div style="font-size:10px;font-weight:800;color:#FF2D20;letter-spacing:2px;margin-bottom:12px;">
            TOP {len(digest['top'])} ARTICLES
          </div>
          <table style="width:100%;border-collapse:collapse;">
            {rows}
          </table>
        </div>

        <!-- CTA -->
        <div style="text-align:center;padding:24px 0;">
          <a href="https://nogear-magazine.vercel.app" style="display:inline-block;padding:10px 28px;background:#FF2D20;color:#fff;font-size:12px;font-weight:800;letter-spacing:1px;text-decoration:none;border-radius:6px;">
            VIEW FULL MAGAZINE →
          </a>
        </div>

        <!-- FOOTER -->
        <div style="text-align:center;padding:16px 0;border-top:1px solid #1a1a2e;">
          <div style="font-size:9px;color:#333;letter-spacing:1px;">
            FXXK FAKES. STAY NATURAL. · Crawl #{digest['crawl_count']}
          </div>
        </div>
      </div>
    </body>
    </html>"""


def send_telegram(text: str):
    """Send via Telegram Bot API"""
    if not TELEGRAM_BOT or len(TELEGRAM_BOT) < 20:
        print("⚠️ Telegram bot token not configured, skipping")
        return False

    url = f"https://api.telegram.org/bot{TELEGRAM_BOT}/sendMessage"
    data = urllib.parse.urlencode({
        "chat_id": TELEGRAM_CHAT,
        "text": text,
        "parse_mode": "Markdown",
        "disable_web_page_preview": "true",
    }).encode()

    try:
        req = urllib.request.Request(url, data=data)
        with urllib.request.urlopen(req, timeout=10) as resp:
            result = json.loads(resp.read())
            if result.get("ok"):
                print("✅ Telegram sent")
                return True
            else:
                print(f"❌ Telegram error: {result}")
                return False
    except Exception as e:
        print(f"❌ Telegram error: {e}")
        return False


def send_gmail(subject: str, html: str):
    """Send via Gmail SMTP"""
    if not GMAIL_USER or not GMAIL_APP_PASSWORD or not GMAIL_TO:
        print("⚠️ Gmail not configured (GMAIL_USER, GMAIL_APP_PASSWORD, GMAIL_TO needed)")
        return False

    msg = MIMEMultipart("alternative")
    msg["Subject"] = subject
    msg["From"] = f"NOGEAR Magazine <{GMAIL_USER}>"
    msg["To"] = GMAIL_TO
    msg.attach(MIMEText(html, "html", "utf-8"))

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(GMAIL_USER, GMAIL_APP_PASSWORD)
            server.send_message(msg)
        print("✅ Gmail sent")
        return True
    except Exception as e:
        print(f"❌ Gmail error: {e}")
        return False


def main():
    print("📡 NOGEAR Magazine Digest Sender")

    data = load_articles()
    digest = build_digest(data)

    print(f"📊 {digest['total']} articles | avg viral {digest['avg_score']} | {digest['verified']} verified")

    # Telegram
    tg_text = format_telegram(digest)
    send_telegram(tg_text)

    # Gmail
    now_kst = datetime.now(KST).strftime("%m/%d")
    subject = f"📡 NOGEAR Magazine [{now_kst}] TOP {len(digest['top'])} · Viral {digest['top'][0].get('viral_score', 0)}"
    html = format_gmail_html(digest)
    send_gmail(subject, html)

    print("✅ Digest complete")


if __name__ == "__main__":
    main()
