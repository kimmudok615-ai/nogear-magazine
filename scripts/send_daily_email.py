#!/usr/bin/env python3
"""
NOGEAR Magazine — Daily Email Digest
kimmudok615@gmail.com → nowornever20031206@gmail.com
매일 08:00 KST 자동 발송
"""

import smtplib, json
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime, timezone, timedelta
from pathlib import Path

KST = timezone(timedelta(hours=9))
CONTENT_FILE = Path(__file__).parent.parent / "content" / "articles.json"

GMAIL_USER = "kimmudok615@gmail.com"
GMAIL_PASS = "vzos qvhz jjqb jbql"
TO = "nowornever20031206@gmail.com"


def main():
    now = datetime.now(KST).strftime('%Y-%m-%d %H:%M KST')
    date_short = datetime.now(KST).strftime('%m/%d')

    with open(CONTENT_FILE, encoding='utf-8') as f:
        data = json.load(f)

    news = data.get('news', [])
    meta = data.get('meta', {})
    total = len(news)
    top10 = news[:10]

    cats = {}
    for a in news:
        c = a.get('category', 'other')
        cats[c] = cats.get(c, 0) + 1

    # Build HTML rows
    rows = ""
    for i, a in enumerate(top10):
        score = a.get('viral_score', 0)
        emoji = a.get('viral_emoji', '⚪')
        tier = a.get('viral_tier', '')
        title_ko = a.get('title_ko', a.get('title', ''))
        title_en = a.get('title', '')
        summary = a.get('summary', '')
        source = a.get('source', '')
        cat = a.get('category', '').upper()
        signals = a.get('viral_signals', {})
        sc = "#FF2D20" if score >= 90 else "#F59E0B" if score >= 75 else "#3B82F6" if score >= 60 else "#666"

        signal_parts = []
        if signals.get('shock_factor'): signal_parts.append(f"충격 {signals['shock_factor']}")
        if signals.get('scientific_credibility'): signal_parts.append(f"논문 {signals['scientific_credibility']}")
        if signals.get('relatability'): signal_parts.append(f"공감 {signals['relatability']}")
        if signals.get('recency'): signal_parts.append(f"최신 {signals['recency']}")
        if signals.get('controversy'): signal_parts.append(f"논쟁 {signals['controversy']}")
        signal_str = " &middot; ".join(signal_parts)

        url = a.get('source_url', a.get('url', ''))
        url_link = f' &middot; <a href="{url}" style="color:#3B82F6;font-size:10px;font-weight:700;text-decoration:none;">SOURCE →</a>' if url else ''

        cred = a.get('credibility', {})
        badge = ''
        if cred.get('confidence') == 'high':
            badge = ' <span style="color:#10B981;">✅</span>'
        elif cred.get('confidence') == 'medium':
            badge = ' <span style="color:#F59E0B;">🔍</span>'

        rows += f"""
        <tr style="border-bottom:1px solid #1a1a2e;">
          <td style="padding:16px 8px;vertical-align:top;text-align:center;width:50px;">
            <div style="font-size:24px;">{emoji}</div>
            <div style="font-size:18px;font-weight:900;color:{sc};margin-top:2px;">{score}</div>
          </td>
          <td style="padding:16px 12px;vertical-align:top;">
            <div style="font-size:9px;font-weight:800;letter-spacing:1.5px;color:{sc};margin-bottom:6px;">{tier} &middot; {cat}{badge}</div>
            <div style="font-size:16px;font-weight:800;color:#F4F4F6;line-height:1.3;margin-bottom:6px;">{title_ko}</div>
            <div style="font-size:11px;color:#555;margin-bottom:8px;">{title_en}</div>
            <div style="font-size:12px;color:#999;line-height:1.7;margin-bottom:10px;">{summary}</div>
            <div style="font-size:10px;color:#555;">📄 {source}{url_link}</div>
            <div style="font-size:9px;color:#333;margin-top:4px;">{signal_str}</div>
          </td>
        </tr>"""

    cat_html = ""
    for c, n in sorted(cats.items(), key=lambda x: -x[1]):
        cat_html += f'<span style="display:inline-block;padding:4px 12px;margin:2px;border-radius:4px;font-size:10px;font-weight:700;background:rgba(255,255,255,.04);border:1px solid rgba(255,255,255,.06);color:#888;">{c.upper()} {n}</span> '

    # Credibility stats
    verified = sum(1 for a in news if a.get('credibility', {}).get('confidence') == 'high')
    checked = sum(1 for a in news if a.get('credibility', {}).get('confidence') == 'medium')
    unverified = total - verified - checked

    html = f"""<!DOCTYPE html>
<html><head><meta charset="utf-8"></head>
<body style="margin:0;padding:0;background:#030306;font-family:-apple-system,'Helvetica Neue',Arial,sans-serif;">
  <div style="max-width:680px;margin:0 auto;background:#030306;">
    <div style="padding:32px 28px 20px;border-bottom:2px solid #FF2D20;">
      <div style="font-size:22px;font-weight:900;color:#F4F4F6;letter-spacing:2px;">
        <span style="color:#FF2D20;">NO</span>GEAR
        <span style="font-size:10px;color:#444;letter-spacing:4px;margin-left:4px;">MAGAZINE</span>
      </div>
      <div style="font-size:11px;color:#555;margin-top:8px;">DAILY INTELLIGENCE DIGEST &middot; {now}</div>
    </div>
    <table style="width:100%;border-collapse:collapse;background:#07070e;">
      <tr>
        <td style="padding:20px;text-align:center;width:20%;border-right:1px solid #111;">
          <div style="font-size:28px;font-weight:900;color:#F4F4F6;">{total}</div>
          <div style="font-size:8px;font-weight:800;color:#444;letter-spacing:2px;">ARTICLES</div>
        </td>
        <td style="padding:20px;text-align:center;width:20%;border-right:1px solid #111;">
          <div style="font-size:28px;font-weight:900;color:#FF2D20;">{meta.get('top_viral_score',0)}</div>
          <div style="font-size:8px;font-weight:800;color:#444;letter-spacing:2px;">TOP VIRAL</div>
        </td>
        <td style="padding:20px;text-align:center;width:20%;border-right:1px solid #111;">
          <div style="font-size:28px;font-weight:900;color:#F59E0B;">{meta.get('avg_viral_score',0)}</div>
          <div style="font-size:8px;font-weight:800;color:#444;letter-spacing:2px;">AVG SCORE</div>
        </td>
        <td style="padding:20px;text-align:center;width:20%;border-right:1px solid #111;">
          <div style="font-size:28px;font-weight:900;color:#10B981;">{verified}</div>
          <div style="font-size:8px;font-weight:800;color:#444;letter-spacing:2px;">VERIFIED</div>
        </td>
        <td style="padding:20px;text-align:center;width:20%;">
          <div style="font-size:28px;font-weight:900;color:#A855F7;">#{meta.get('crawl_count',0)}</div>
          <div style="font-size:8px;font-weight:800;color:#444;letter-spacing:2px;">CRAWL</div>
        </td>
      </tr>
    </table>
    <div style="padding:16px 28px;background:#07070e;border-bottom:1px solid #111;">
      <div style="font-size:9px;font-weight:800;color:#FF2D20;letter-spacing:2px;margin-bottom:8px;">CATEGORY BREAKDOWN</div>
      {cat_html}
    </div>
    <div style="padding:20px 28px;">
      <div style="font-size:10px;font-weight:800;color:#FF2D20;letter-spacing:2px;margin-bottom:16px;">TOP 10 ARTICLES — RANKED BY VIRAL SCORE</div>
      <table style="width:100%;border-collapse:collapse;">{rows}</table>
    </div>
    <div style="text-align:center;padding:28px;">
      <a href="https://nogear-magazine.vercel.app" style="display:inline-block;padding:12px 36px;background:#FF2D20;color:#fff;font-size:13px;font-weight:800;letter-spacing:1px;text-decoration:none;border-radius:6px;">FULL MAGAZINE →</a>
    </div>
    <div style="padding:20px 28px;border-top:1px solid #111;text-align:center;">
      <div style="font-size:10px;color:#333;letter-spacing:1px;">FXXK FAKES. STAY NATURAL.</div>
      <div style="font-size:9px;color:#222;margin-top:4px;">NOGEAR Magazine Auto-Digest &middot; {now}</div>
    </div>
  </div>
</body></html>"""

    # Plain text
    plain = f"NOGEAR MAGAZINE DAILY DIGEST\n{now}\n\n총 {total}개 | Top {meta.get('top_viral_score',0)} | Avg {meta.get('avg_viral_score',0)}\n\n"
    for i, a in enumerate(top10):
        plain += f"{i+1}. [{a.get('viral_score',0)}] {a.get('title_ko', a.get('title',''))}\n   {a.get('summary','')[:120]}...\n   Source: {a.get('source','')}\n\n"
    plain += f"🔗 https://nogear-magazine.vercel.app\n\nFXXK FAKES. STAY NATURAL."

    subject = f"📡 NOGEAR Magazine [{date_short}] TOP 10 · Viral {top10[0].get('viral_score',0)} | {total} Articles"

    msg = MIMEMultipart('alternative')
    msg['Subject'] = subject
    msg['From'] = f'NOGEAR Magazine <{GMAIL_USER}>'
    msg['To'] = TO
    msg.attach(MIMEText(plain, 'plain', 'utf-8'))
    msg.attach(MIMEText(html, 'html', 'utf-8'))

    with smtplib.SMTP_SSL('smtp.gmail.com', 465, timeout=15) as server:
        server.login(GMAIL_USER, GMAIL_PASS)
        server.send_message(msg)

    print(f"✅ Email sent → {TO}")
    print(f"📊 {total} articles | Top viral {meta.get('top_viral_score',0)} | Avg {meta.get('avg_viral_score',0)}")
    print(f"🏆 Top 3:")
    for a in top10[:3]:
        print(f"   [{a.get('viral_score',0)}] {a.get('title_ko', a.get('title',''))[:50]}")


if __name__ == "__main__":
    main()
