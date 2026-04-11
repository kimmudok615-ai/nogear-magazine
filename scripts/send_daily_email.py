#!/usr/bin/env python3
"""
NOGEAR Magazine — 일일 이메일 다이제스트
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

CAT_KO = {
    "steroids": "스테로이드",
    "drugs": "약물/PED",
    "exercise": "운동과학",
    "nutrition": "영양",
    "viral": "바이럴",
    "science": "과학연구",
    "industry": "업계동향",
    "mental": "멘탈/심리",
    "other": "기타",
}

TIER_KO = {
    "VIRAL_BOMB": "폭발",
    "HOT": "핫",
    "TRENDING": "트렌딩",
    "RELEVANT": "관련",
    "INFO": "정보",
}


def main():
    now = datetime.now(KST).strftime('%Y년 %m월 %d일 %H:%M')
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

    # HTML 아티클 행 생성
    rows = ""
    for i, a in enumerate(top10):
        score = a.get('viral_score', 0)
        emoji = a.get('viral_emoji', '⚪')
        tier = a.get('viral_tier', '')
        tier_ko = TIER_KO.get(tier, tier)
        title_ko = a.get('title_ko', a.get('title', ''))
        summary = a.get('summary', '')
        source = a.get('source', '')
        cat = a.get('category', '')
        cat_ko = CAT_KO.get(cat, cat)
        signals = a.get('viral_signals', {})
        sc = "#FF2D20" if score >= 90 else "#F59E0B" if score >= 75 else "#3B82F6" if score >= 60 else "#666"

        signal_parts = []
        if signals.get('shock_factor'): signal_parts.append(f"충격도 {signals['shock_factor']}")
        if signals.get('scientific_credibility'): signal_parts.append(f"신뢰도 {signals['scientific_credibility']}")
        if signals.get('relatability'): signal_parts.append(f"공감도 {signals['relatability']}")
        if signals.get('recency'): signal_parts.append(f"최신성 {signals['recency']}")
        if signals.get('controversy'): signal_parts.append(f"논쟁성 {signals['controversy']}")
        signal_str = " &middot; ".join(signal_parts)

        url = a.get('source_url', a.get('url', ''))
        url_link = f' &middot; <a href="{url}" style="color:#3B82F6;font-size:10px;font-weight:700;text-decoration:none;">원문 보기 →</a>' if url else ''

        cred = a.get('credibility', {})
        badge = ''
        if cred.get('confidence') == 'high':
            badge = ' <span style="color:#10B981;">✅ 검증됨</span>'
        elif cred.get('confidence') == 'medium':
            badge = ' <span style="color:#F59E0B;">🔍 확인중</span>'

        rows += f"""
        <tr style="border-bottom:1px solid #1a1a2e;">
          <td style="padding:18px 10px;vertical-align:top;text-align:center;width:55px;">
            <div style="font-size:26px;">{emoji}</div>
            <div style="font-size:20px;font-weight:900;color:{sc};margin-top:3px;">{score}</div>
            <div style="font-size:8px;font-weight:700;color:{sc};letter-spacing:1px;margin-top:2px;">{tier_ko}</div>
          </td>
          <td style="padding:18px 14px;vertical-align:top;">
            <div style="font-size:9px;font-weight:800;letter-spacing:1px;color:{sc};margin-bottom:6px;">{cat_ko}{badge}</div>
            <div style="font-size:17px;font-weight:800;color:#F4F4F6;line-height:1.35;margin-bottom:10px;">{title_ko}</div>
            <div style="font-size:12.5px;color:#999;line-height:1.75;margin-bottom:12px;">{summary}</div>
            <div style="font-size:10px;color:#555;">📄 {source}{url_link}</div>
            <div style="font-size:9px;color:#444;margin-top:5px;">{signal_str}</div>
          </td>
        </tr>"""

    # 카테고리 한글 표시
    cat_html = ""
    for c, n in sorted(cats.items(), key=lambda x: -x[1]):
        cat_html += f'<span style="display:inline-block;padding:4px 12px;margin:3px;border-radius:4px;font-size:10px;font-weight:700;background:rgba(255,255,255,.04);border:1px solid rgba(255,255,255,.06);color:#888;">{CAT_KO.get(c,c)} {n}건</span> '

    # 신뢰도 통계
    verified = sum(1 for a in news if a.get('credibility', {}).get('confidence') == 'high')
    checked = sum(1 for a in news if a.get('credibility', {}).get('confidence') == 'medium')

    html = f"""<!DOCTYPE html>
<html><head><meta charset="utf-8"></head>
<body style="margin:0;padding:0;background:#030306;font-family:-apple-system,'Helvetica Neue',Arial,sans-serif;">
  <div style="max-width:680px;margin:0 auto;background:#030306;">

    <!-- 헤더 -->
    <div style="padding:32px 28px 20px;border-bottom:2px solid #FF2D20;">
      <div style="font-size:22px;font-weight:900;color:#F4F4F6;letter-spacing:2px;">
        <span style="color:#FF2D20;">NO</span>GEAR
        <span style="font-size:10px;color:#444;letter-spacing:4px;margin-left:4px;">MAGAZINE</span>
      </div>
      <div style="font-size:12px;color:#777;margin-top:10px;">일일 인텔리전스 다이제스트 &middot; {now}</div>
    </div>

    <!-- 통계 -->
    <table style="width:100%;border-collapse:collapse;background:#07070e;">
      <tr>
        <td style="padding:22px 12px;text-align:center;width:20%;border-right:1px solid #111;">
          <div style="font-size:30px;font-weight:900;color:#F4F4F6;">{total}</div>
          <div style="font-size:9px;font-weight:800;color:#555;letter-spacing:1px;">총 기사</div>
        </td>
        <td style="padding:22px 12px;text-align:center;width:20%;border-right:1px solid #111;">
          <div style="font-size:30px;font-weight:900;color:#FF2D20;">{meta.get('top_viral_score',0)}</div>
          <div style="font-size:9px;font-weight:800;color:#555;letter-spacing:1px;">최고 바이럴</div>
        </td>
        <td style="padding:22px 12px;text-align:center;width:20%;border-right:1px solid #111;">
          <div style="font-size:30px;font-weight:900;color:#F59E0B;">{meta.get('avg_viral_score',0)}</div>
          <div style="font-size:9px;font-weight:800;color:#555;letter-spacing:1px;">평균 점수</div>
        </td>
        <td style="padding:22px 12px;text-align:center;width:20%;border-right:1px solid #111;">
          <div style="font-size:30px;font-weight:900;color:#10B981;">{verified}</div>
          <div style="font-size:9px;font-weight:800;color:#555;letter-spacing:1px;">검증완료</div>
        </td>
        <td style="padding:22px 12px;text-align:center;width:20%;">
          <div style="font-size:30px;font-weight:900;color:#A855F7;">#{meta.get('crawl_count',0)}</div>
          <div style="font-size:9px;font-weight:800;color:#555;letter-spacing:1px;">크롤 회차</div>
        </td>
      </tr>
    </table>

    <!-- 카테고리 분포 -->
    <div style="padding:16px 28px;background:#07070e;border-bottom:1px solid #111;">
      <div style="font-size:9px;font-weight:800;color:#FF2D20;letter-spacing:2px;margin-bottom:10px;">카테고리별 분포</div>
      {cat_html}
    </div>

    <!-- TOP 10 기사 -->
    <div style="padding:24px 28px;">
      <div style="font-size:11px;font-weight:800;color:#FF2D20;letter-spacing:1.5px;margin-bottom:18px;">
        TOP 10 기사 — 바이럴 점수 순
      </div>
      <table style="width:100%;border-collapse:collapse;">{rows}</table>
    </div>

    <!-- 매거진 링크 -->
    <div style="text-align:center;padding:28px;">
      <a href="https://nogear-magazine.vercel.app" style="display:inline-block;padding:14px 40px;background:#FF2D20;color:#fff;font-size:13px;font-weight:800;letter-spacing:1px;text-decoration:none;border-radius:6px;">전체 매거진 보기 →</a>
    </div>

    <!-- 푸터 -->
    <div style="padding:20px 28px;border-top:1px solid #111;text-align:center;">
      <div style="font-size:10px;color:#333;letter-spacing:1px;">FXXK FAKES. STAY NATURAL.</div>
      <div style="font-size:9px;color:#222;margin-top:4px;">NOGEAR Magazine 자동 다이제스트 &middot; {now}</div>
    </div>
  </div>
</body></html>"""

    # 텍스트 버전
    plain = f"NOGEAR MAGAZINE 일일 다이제스트\n{now}\n\n총 {total}건 | 최고 바이럴 {meta.get('top_viral_score',0)} | 평균 {meta.get('avg_viral_score',0)}\n\n"
    for i, a in enumerate(top10):
        plain += f"{i+1}. [{a.get('viral_score',0)}점] {a.get('title_ko', a.get('title',''))}\n   {a.get('summary','')[:150]}...\n   출처: {a.get('source','')}\n\n"
    plain += f"전체 매거진: https://nogear-magazine.vercel.app\n\nFXXK FAKES. STAY NATURAL."

    subject = f"📡 NOGEAR 매거진 [{date_short}] TOP 10 | 바이럴 {top10[0].get('viral_score',0)}점 | 총 {total}건"

    msg = MIMEMultipart('alternative')
    msg['Subject'] = subject
    msg['From'] = f'NOGEAR Magazine <{GMAIL_USER}>'
    msg['To'] = TO
    msg.attach(MIMEText(plain, 'plain', 'utf-8'))
    msg.attach(MIMEText(html, 'html', 'utf-8'))

    with smtplib.SMTP_SSL('smtp.gmail.com', 465, timeout=15) as server:
        server.login(GMAIL_USER, GMAIL_PASS)
        server.send_message(msg)

    print(f"✅ 이메일 전송 완료 → {TO}")
    print(f"📊 총 {total}건 | 최고 바이럴 {meta.get('top_viral_score',0)} | 평균 {meta.get('avg_viral_score',0)}")
    print(f"🏆 TOP 3:")
    for a in top10[:3]:
        print(f"   [{a.get('viral_score',0)}] {a.get('title_ko', a.get('title',''))[:50]}")


if __name__ == "__main__":
    main()
