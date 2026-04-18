#!/usr/bin/env python3
"""
NOGEAR Magazine — VIRAL Cardnews Generator v2
바이럴 마케팅 기반 고퀄리티 카드뉴스

원칙:
1. 첫 0.3초 스크롤 스톱 (거대 숫자, 강한 대비)
2. 본문 최소화 — 하나의 충격적 팩트만
3. 디자이너 레벨 타이포그래피
4. 브루탈리즘 + 디지털 미디어 스타일
5. 캐러셀 스토리텔링 (훅→증거→전환→CTA)

포맷:
- carousel: 1080x1350 (인스타 피드 메인)
- story: 1080x1920 (스토리)
- square: 1080x1080 (피드 그리드 뷰)
"""

import json
import re
from datetime import datetime, timezone, timedelta
from pathlib import Path

KST = timezone(timedelta(hours=9))
BASE = Path(__file__).parent.parent
CONTENT_FILE = BASE / "content" / "articles.json"
COPY_FILE = BASE / "content" / "editorial" / "copy-rewrites.json"
BRIEF_FILE = BASE / "content" / "editorial" / "daily-brief.json"
CARDNEWS_DIR = BASE / "cardnews"

# 바이럴 디자인 토큰
DESIGN = {
    "bg": "#030306",
    "bg_alt": "#0A0A12",
    "red": "#FF2D20",
    "red_soft": "rgba(255,45,32,0.15)",
    "white": "#F4F4F6",
    "grey": "#888",
    "dark_grey": "#333",
    "accent_amber": "#F59E0B",
    "accent_green": "#10B981",
}


def extract_hero_number(text: str) -> dict:
    """제목에서 핵심 숫자 추출 (가장 임팩트 있는 것)"""
    # 패턴: 93%, 9배, 40%, $11,000, 2,986% 등
    patterns = [
        (r'(\d+(?:,\d+)*)%', '%', 1),        # 93%
        (r'(\d+)배', '배', 2),                # 9배
        (r'\$(\d+(?:,\d+)*)', '$', 0),       # $11,000
        (r'(\d+(?:,\d+)*)\s*(?:원|만원)', '원', 0),
        (r'(\d+(?:,\d+)*)명', '명', 3),       # 1,189명
        (r'(\d+)주', '주', 4),                # 12주
        (r'(\d+)년', '년', 4),
        (r'(\d+)', '', 5),                   # 기타 숫자
    ]
    for pattern, unit, priority in patterns:
        m = re.search(pattern, text)
        if m:
            return {
                "number": m.group(1),
                "unit": unit,
                "priority": priority,
                "full": m.group(0),
            }
    return None


def viral_hook(title: str, score: int) -> str:
    """제목에서 가장 충격적인 부분 추출 (짧게)"""
    # 핵심 문구만 추출
    # "X한 Y가 Z하다" → "Z하다"에 초점
    hooks = []
    if '파괴' in title or '무너진' in title or '죽' in title or '사망' in title:
        hooks.append('DESTROY')
    if '거짓' in title or '페이크' in title or '속' in title or '가짜' in title:
        hooks.append('LIE')
    if '숨겨' in title or '몰랐던' in title or '실체' in title:
        hooks.append('HIDDEN')
    if '폭발' in title or '급증' in title or '폭주' in title:
        hooks.append('SURGE')
    if '경고' in title or '위험' in title:
        hooks.append('WARNING')
    return hooks[0] if hooks else 'VIRAL'


# ── SVG ICONS ──
HEART_ICON = """<svg viewBox="0 0 64 64" style="width:100%;height:100%;">
<path d="M32 56 C32 56 8 40 8 24 C8 16 14 10 22 10 C27 10 32 14 32 20 C32 14 37 10 42 10 C50 10 56 16 56 24 C56 40 32 56 32 56 Z" fill="none" stroke="#FF2D20" stroke-width="3"/>
<path d="M20 28 L26 22 L30 32 L36 18 L40 28 L44 24" fill="none" stroke="#FF2D20" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/>
</svg>"""

WARNING_ICON = """<svg viewBox="0 0 64 64" style="width:100%;height:100%;">
<polygon points="32,6 60,56 4,56" fill="none" stroke="#FF2D20" stroke-width="3" stroke-linejoin="round"/>
<line x1="32" y1="24" x2="32" y2="40" stroke="#FF2D20" stroke-width="4" stroke-linecap="round"/>
<circle cx="32" cy="48" r="2.5" fill="#FF2D20"/>
</svg>"""

SKULL_ICON = """<svg viewBox="0 0 64 64" style="width:100%;height:100%;">
<path d="M32 8 C18 8 10 18 10 30 L10 42 L18 42 L18 52 L22 52 L22 48 L28 48 L28 52 L36 52 L36 48 L42 48 L42 52 L46 52 L46 42 L54 42 L54 30 C54 18 46 8 32 8 Z" fill="none" stroke="#FF2D20" stroke-width="3"/>
<circle cx="22" cy="30" r="4" fill="#FF2D20"/>
<circle cx="42" cy="30" r="4" fill="#FF2D20"/>
<path d="M30 38 L34 38 L32 42 Z" fill="#FF2D20"/>
</svg>"""

PILL_ICON = """<svg viewBox="0 0 64 64" style="width:100%;height:100%;">
<rect x="8" y="24" width="48" height="16" rx="8" fill="none" stroke="#FF2D20" stroke-width="3"/>
<line x1="32" y1="24" x2="32" y2="40" stroke="#FF2D20" stroke-width="3"/>
<circle cx="20" cy="32" r="2" fill="#FF2D20"/>
<circle cx="44" cy="32" r="2" fill="#FF2D20"/>
</svg>"""

LAB_ICON = """<svg viewBox="0 0 64 64" style="width:100%;height:100%;">
<path d="M24 8 L24 24 L14 48 C13 52 16 56 20 56 L44 56 C48 56 51 52 50 48 L40 24 L40 8 Z" fill="none" stroke="#FF2D20" stroke-width="3"/>
<line x1="20" y1="8" x2="44" y2="8" stroke="#FF2D20" stroke-width="3" stroke-linecap="round"/>
<path d="M18 40 L46 40" stroke="#FF2D20" stroke-width="2" stroke-dasharray="3,3"/>
<circle cx="24" cy="44" r="2" fill="#FF2D20"/>
<circle cx="36" cy="48" r="2.5" fill="#FF2D20"/>
<circle cx="30" cy="52" r="1.5" fill="#FF2D20"/>
</svg>"""

CHART_BAR_SVG = """<svg viewBox="0 0 400 120" style="width:100%;height:100%;">
<line x1="40" y1="100" x2="380" y2="100" stroke="rgba(255,255,255,.2)" stroke-width="1"/>
<rect x="60" y="60" width="40" height="40" fill="rgba(255,45,32,.3)"/>
<rect x="120" y="40" width="40" height="60" fill="rgba(255,45,32,.5)"/>
<rect x="180" y="20" width="40" height="80" fill="rgba(255,45,32,.7)"/>
<rect x="240" y="10" width="40" height="90" fill="#FF2D20"/>
<rect x="300" y="5" width="40" height="95" fill="#FF2D20"/>
<text x="80" y="115" fill="rgba(255,255,255,.4)" font-size="11" font-family="Space Grotesk" text-anchor="middle">2021</text>
<text x="140" y="115" fill="rgba(255,255,255,.4)" font-size="11" font-family="Space Grotesk" text-anchor="middle">2022</text>
<text x="200" y="115" fill="rgba(255,255,255,.4)" font-size="11" font-family="Space Grotesk" text-anchor="middle">2023</text>
<text x="260" y="115" fill="rgba(255,255,255,.4)" font-size="11" font-family="Space Grotesk" text-anchor="middle">2024</text>
<text x="320" y="115" fill="#FF2D20" font-size="11" font-weight="900" font-family="Space Grotesk" text-anchor="middle">2025</text>
</svg>"""


def pick_icon(article: dict) -> str:
    """기사 카테고리/주제에 맞는 아이콘 선택"""
    title = (article.get('title', '') + article.get('summary', '')).lower()
    if any(k in title for k in ['심장', '심근', '심혈관']):
        return HEART_ICON
    if any(k in title for k in ['사망', '사망자', '죽', '치명']):
        return SKULL_ICON
    if any(k in title for k in ['dnp', '스테로이드', 'sarm', '약물', '펩타이드']):
        return PILL_ICON
    if any(k in title for k in ['연구', '논문', '실험', '분석']):
        return LAB_ICON
    return WARNING_ICON


# ── CARD 1: COVER — VIRAL HOOK ──
def cover_card(top_articles: list, date_str: str) -> str:
    """커버: 거대 숫자 + 충격 헤드라인 + 심장/경고 아이콘"""
    top = top_articles[0]
    title = top.get('title_rewrite', top.get('title', ''))
    score = top.get('viral_score', 0)
    hero = extract_hero_number(title)
    icon = pick_icon(top)

    hero_display = hero['full'] if hero else f"VIRAL {score}"

    day_ko = ["월","화","수","목","금","토","일"][datetime.now(KST).weekday()]

    return f"""<!DOCTYPE html>
<html><head><meta charset="utf-8">
<style>
@import url('https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@400;700;900&family=Space+Grotesk:wght@700;900&display=swap');
*{{margin:0;padding:0;box-sizing:border-box;}}
body{{width:1080px;height:1350px;background:{DESIGN['bg']};font-family:'Noto Sans KR',sans-serif;color:{DESIGN['white']};overflow:hidden;position:relative;}}
.grain{{position:absolute;inset:0;background-image:radial-gradient(rgba(255,255,255,.02) 1px,transparent 1px);background-size:3px 3px;pointer-events:none;}}
.noise-lines{{position:absolute;top:0;left:0;right:0;height:100%;background:linear-gradient(90deg,transparent 98%,rgba(255,45,32,.04) 100%);background-size:60px 100%;pointer-events:none;}}
.top-strip{{position:absolute;top:0;left:0;right:0;height:60px;background:{DESIGN['red']};display:flex;align-items:center;justify-content:space-between;padding:0 56px;}}
.top-strip .ticker{{font-family:'Space Grotesk';font-size:13px;font-weight:900;letter-spacing:4px;color:#000;}}
.top-strip .date{{font-family:'Space Grotesk';font-size:13px;font-weight:700;letter-spacing:2px;color:#000;}}
.icon-wrap{{position:absolute;top:100px;left:56px;width:80px;height:80px;}}
.icon-label{{position:absolute;top:110px;left:156px;font-family:'Space Grotesk';font-size:12px;font-weight:900;letter-spacing:4px;color:{DESIGN['red']};}}
.icon-subtext{{position:absolute;top:140px;left:156px;font-size:16px;color:{DESIGN['grey']};font-weight:400;}}
.hero-num{{position:absolute;top:220px;left:0;right:0;text-align:center;font-family:'Space Grotesk';font-weight:900;font-size:280px;line-height:1;letter-spacing:-10px;color:{DESIGN['red']};text-shadow:0 0 80px rgba(255,45,32,.4);}}
.hero-label{{position:absolute;top:520px;left:0;right:0;text-align:center;font-family:'Space Grotesk';font-size:14px;font-weight:900;letter-spacing:6px;color:{DESIGN['white']};}}
.pulse-ring{{position:absolute;top:240px;left:50%;width:500px;height:500px;border:2px solid rgba(255,45,32,.1);border-radius:50%;transform:translateX(-50%);pointer-events:none;}}
.pulse-ring-2{{position:absolute;top:290px;left:50%;width:400px;height:400px;border:1px solid rgba(255,45,32,.05);border-radius:50%;transform:translateX(-50%);pointer-events:none;}}
.main-hook{{position:absolute;top:620px;left:56px;right:56px;font-size:62px;font-weight:900;line-height:1.1;letter-spacing:-2px;color:{DESIGN['white']};}}
.main-hook .accent{{color:{DESIGN['red']};}}
.meta-line{{position:absolute;bottom:120px;left:56px;right:56px;display:flex;align-items:center;justify-content:space-between;border-top:1px solid rgba(255,255,255,.1);padding-top:16px;}}
.meta-left{{font-size:13px;color:{DESIGN['grey']};letter-spacing:1px;font-weight:700;}}
.meta-right{{font-family:'Space Grotesk';font-size:11px;color:{DESIGN['dark_grey']};letter-spacing:3px;}}
.swipe-cta{{position:absolute;bottom:40px;left:56px;right:56px;display:flex;align-items:center;justify-content:space-between;}}
.swipe-cta .logo{{font-family:'Space Grotesk';font-size:18px;font-weight:900;letter-spacing:2px;}}
.swipe-cta .logo .n{{color:{DESIGN['red']};}}
.swipe-cta .logo .mag{{font-size:9px;color:{DESIGN['dark_grey']};letter-spacing:4px;margin-left:4px;}}
.swipe-cta .arrow{{font-family:'Space Grotesk';font-size:14px;font-weight:800;color:{DESIGN['red']};letter-spacing:3px;animation:pulse 1.5s infinite;}}
@keyframes pulse{{0%,100%{{opacity:1}}50%{{opacity:.4}}}}
.vertical-label{{position:absolute;left:20px;top:50%;transform:rotate(-90deg) translateY(-50%);transform-origin:left center;font-family:'Space Grotesk';font-size:10px;font-weight:800;color:{DESIGN['dark_grey']};letter-spacing:5px;}}
</style></head>
<body>
  <div class="grain"></div>
  <div class="noise-lines"></div>
  <div class="top-strip">
    <div class="ticker">■ NOGEAR INTEL</div>
    <div class="date">{date_str} ({day_ko}) · EDITION</div>
  </div>
  <div class="vertical-label">ISSUE / DAILY</div>

  <div class="icon-wrap">{icon}</div>
  <div class="icon-label">HEALTH ALERT</div>
  <div class="icon-subtext">오늘의 경고 리포트</div>

  <div class="pulse-ring"></div>
  <div class="pulse-ring-2"></div>
  <div class="hero-num">{hero_display}</div>
  <div class="hero-label">— SHOCKING STAT OF THE DAY —</div>

  <div class="main-hook">{title[:55]}...</div>

  <div class="meta-line">
    <div class="meta-left">오늘의 바이럴 #{score}점 · NO FILTER</div>
    <div class="meta-right">VIRAL / WARNING / FACT</div>
  </div>

  <div class="swipe-cta">
    <div class="logo"><span class="n">NO</span>GEAR<span class="mag">MAGAZINE</span></div>
    <div class="arrow">SWIPE →</div>
  </div>
</body></html>"""


# ── CARD 2: PROBLEM — 문제 제시 ──
def problem_card(article: dict, idx: int, total: int) -> str:
    title = article.get('title_rewrite', article.get('title', ''))
    summary = article.get('summary', '')[:180]
    score = article.get('viral_score', 0)
    category_ko = article.get('category_ko', article.get('category', ''))
    source = article.get('source', '')
    hero = extract_hero_number(title + ' ' + summary)
    icon = pick_icon(article)

    hero_html = ""
    if hero and hero['priority'] <= 3:
        hero_html = f'<div style="position:absolute;top:760px;right:56px;font-family:\'Space Grotesk\';font-size:280px;font-weight:900;color:{DESIGN["red"]};opacity:.08;line-height:1;letter-spacing:-10px;pointer-events:none;">{hero["full"]}</div>'

    icon_html = f'<div style="position:absolute;top:870px;left:56px;width:64px;height:64px;opacity:.8;">{icon}</div>'

    return f"""<!DOCTYPE html>
<html><head><meta charset="utf-8">
<style>
@import url('https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@400;700;900&family=Space+Grotesk:wght@700;900&display=swap');
*{{margin:0;padding:0;box-sizing:border-box;}}
body{{width:1080px;height:1350px;background:{DESIGN['bg']};font-family:'Noto Sans KR',sans-serif;color:{DESIGN['white']};overflow:hidden;position:relative;}}
.grain{{position:absolute;inset:0;background-image:radial-gradient(rgba(255,255,255,.02) 1px,transparent 1px);background-size:3px 3px;pointer-events:none;}}
.top-bar{{position:absolute;top:0;left:0;right:0;height:50px;display:flex;align-items:center;justify-content:space-between;padding:0 56px;border-bottom:1px solid rgba(255,255,255,.06);}}
.top-bar .logo{{font-family:'Space Grotesk';font-size:16px;font-weight:900;letter-spacing:2px;}}
.top-bar .logo .n{{color:{DESIGN['red']};}}
.top-bar .page{{font-family:'Space Grotesk';font-size:12px;font-weight:800;color:{DESIGN['grey']};letter-spacing:3px;}}
.cat-chip{{position:absolute;top:90px;left:56px;display:inline-block;padding:8px 18px;background:{DESIGN['red']};color:#000;font-family:'Space Grotesk';font-size:12px;font-weight:900;letter-spacing:2px;}}
.score-corner{{position:absolute;top:90px;right:56px;display:flex;align-items:center;gap:8px;}}
.score-corner .dot{{width:10px;height:10px;border-radius:50%;background:{DESIGN['red']};box-shadow:0 0 16px {DESIGN['red']};}}
.score-corner .num{{font-family:'Space Grotesk';font-size:22px;font-weight:900;color:{DESIGN['red']};}}
.title-block{{position:absolute;top:180px;left:56px;right:56px;z-index:10;}}
.title-block .main{{font-size:56px;font-weight:900;line-height:1.12;letter-spacing:-1.5px;color:{DESIGN['white']};margin-bottom:32px;}}
.title-block .main .hl{{background:linear-gradient(180deg,transparent 60%,{DESIGN['red']} 60%);padding:0 4px;color:{DESIGN['white']};}}
.divider{{position:absolute;top:640px;left:56px;right:56px;height:2px;background:linear-gradient(90deg,{DESIGN['red']} 30%,transparent 100%);}}
.summary{{position:absolute;top:680px;left:56px;right:56px;font-size:21px;font-weight:400;line-height:1.7;color:{DESIGN['grey']};letter-spacing:-.3px;}}
.summary strong{{color:{DESIGN['white']};font-weight:700;}}
.footer{{position:absolute;bottom:50px;left:56px;right:56px;display:flex;align-items:center;justify-content:space-between;font-family:'Space Grotesk';font-size:11px;letter-spacing:2px;}}
.footer .src{{color:{DESIGN['dark_grey']};}}
.footer .arrow{{color:{DESIGN['red']};font-weight:800;}}
.corner-mark{{position:absolute;bottom:50px;left:56px;width:24px;height:24px;border-left:2px solid {DESIGN['red']};border-bottom:2px solid {DESIGN['red']};}}
</style></head>
<body>
  <div class="grain"></div>
  {hero_html}
  {icon_html}
  <div class="top-bar">
    <div class="logo"><span class="n">NO</span>GEAR MAGAZINE</div>
    <div class="page">{idx:02d} / {total:02d}</div>
  </div>
  <div class="cat-chip">{category_ko}</div>
  <div class="score-corner"><div class="dot"></div><div class="num">{score}</div></div>

  <div class="title-block">
    <div class="main">{title}</div>
  </div>

  <div class="divider"></div>
  <div class="summary">{summary}...</div>

  <div class="footer">
    <div class="src">SOURCE · {source[:30]}</div>
    <div class="arrow">CONTINUE →</div>
  </div>
</body></html>"""


# ── CARD 3: EVIDENCE — 수치/증거 ──
def evidence_card(articles: list, idx: int, total: int) -> str:
    """여러 기사의 핵심 수치 종합"""
    stats = []
    for a in articles[:4]:
        title = a.get('title_rewrite', a.get('title', ''))
        hero = extract_hero_number(title)
        if hero:
            stats.append({
                "num": hero['full'],
                "context": title[:40] + '...'
            })

    # 최소 3개 stat 보장
    while len(stats) < 3:
        stats.append({"num": "-", "context": "-"})

    stats_html = ""
    for i, s in enumerate(stats[:3]):
        stats_html += f"""
        <div style="padding:28px 0;border-bottom:1px solid rgba(255,255,255,.08);">
          <div style="display:flex;align-items:baseline;gap:24px;">
            <div style="font-family:'Space Grotesk';font-size:84px;font-weight:900;color:{DESIGN['red']};line-height:1;letter-spacing:-3px;min-width:240px;">{s['num']}</div>
            <div style="font-size:17px;color:{DESIGN['grey']};line-height:1.5;font-weight:500;">{s['context']}</div>
          </div>
        </div>"""

    return f"""<!DOCTYPE html>
<html><head><meta charset="utf-8">
<style>
@import url('https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@400;700;900&family=Space+Grotesk:wght@700;900&display=swap');
*{{margin:0;padding:0;box-sizing:border-box;}}
body{{width:1080px;height:1350px;background:{DESIGN['bg']};font-family:'Noto Sans KR',sans-serif;color:{DESIGN['white']};overflow:hidden;position:relative;}}
.top-bar{{position:absolute;top:0;left:0;right:0;height:50px;display:flex;align-items:center;justify-content:space-between;padding:0 56px;border-bottom:1px solid rgba(255,255,255,.06);}}
.top-bar .logo{{font-family:'Space Grotesk';font-size:16px;font-weight:900;letter-spacing:2px;}}
.top-bar .logo .n{{color:{DESIGN['red']};}}
.top-bar .page{{font-family:'Space Grotesk';font-size:12px;font-weight:800;color:{DESIGN['grey']};letter-spacing:3px;}}
.header{{position:absolute;top:120px;left:56px;right:56px;}}
.header .label{{display:inline-block;padding:6px 14px;background:{DESIGN['white']};color:#000;font-family:'Space Grotesk';font-size:11px;font-weight:900;letter-spacing:3px;margin-bottom:18px;}}
.header .title{{font-size:58px;font-weight:900;line-height:1.05;letter-spacing:-2px;}}
.header .title .red{{color:{DESIGN['red']};}}
.chart-wrap{{position:absolute;top:300px;left:56px;right:56px;height:130px;padding:10px 0;}}
.stats-wrap{{position:absolute;top:460px;left:56px;right:56px;}}
.footer{{position:absolute;bottom:50px;left:56px;right:56px;display:flex;align-items:center;justify-content:space-between;font-family:'Space Grotesk';font-size:11px;letter-spacing:2px;}}
.footer .src{{color:{DESIGN['dark_grey']};}}
.footer .arrow{{color:{DESIGN['red']};font-weight:800;}}
</style></head>
<body>
  <div class="top-bar">
    <div class="logo"><span class="n">NO</span>GEAR MAGAZINE</div>
    <div class="page">{idx:02d} / {total:02d}</div>
  </div>
  <div class="header">
    <div class="label">DATA · 팩트</div>
    <div class="title">숫자가 <span class="red">증명한다</span></div>
  </div>
  <div class="chart-wrap">{CHART_BAR_SVG}</div>
  <div class="stats-wrap">{stats_html}</div>
  <div class="footer">
    <div class="src">VERIFIED · PubMed · Journals</div>
    <div class="arrow">NEXT →</div>
  </div>
</body></html>"""


# ── CARD 4: CTA — 행동 촉구 ──
def cta_card(idx: int, total: int) -> str:
    return f"""<!DOCTYPE html>
<html><head><meta charset="utf-8">
<style>
@import url('https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@400;700;900&family=Space+Grotesk:wght@700;900&display=swap');
*{{margin:0;padding:0;box-sizing:border-box;}}
body{{width:1080px;height:1350px;background:{DESIGN['red']};font-family:'Noto Sans KR',sans-serif;color:#000;overflow:hidden;position:relative;}}
.grid-pattern{{position:absolute;inset:0;background-image:linear-gradient(rgba(0,0,0,.05) 1px,transparent 1px),linear-gradient(90deg,rgba(0,0,0,.05) 1px,transparent 1px);background-size:40px 40px;pointer-events:none;}}
.top-bar{{position:absolute;top:0;left:0;right:0;height:50px;display:flex;align-items:center;justify-content:space-between;padding:0 56px;border-bottom:2px solid #000;}}
.top-bar .logo{{font-family:'Space Grotesk';font-size:16px;font-weight:900;letter-spacing:2px;color:#000;}}
.top-bar .page{{font-family:'Space Grotesk';font-size:12px;font-weight:800;letter-spacing:3px;color:#000;}}
.mark{{position:absolute;top:120px;left:56px;font-family:'Space Grotesk';font-size:14px;font-weight:900;letter-spacing:5px;color:#000;}}
.slogan{{position:absolute;top:200px;left:56px;right:56px;font-size:120px;font-weight:900;line-height:.95;letter-spacing:-5px;color:#000;}}
.slogan .white{{color:#fff;-webkit-text-stroke:3px #000;}}
.line-break{{position:absolute;top:760px;left:56px;right:56px;height:4px;background:#000;}}
.meaning{{position:absolute;top:800px;left:56px;right:56px;font-size:24px;font-weight:700;line-height:1.55;color:#000;}}
.cta-box{{position:absolute;bottom:180px;left:56px;right:56px;background:#000;color:{DESIGN['red']};padding:24px 32px;display:flex;align-items:center;justify-content:space-between;}}
.cta-box .text{{font-size:20px;font-weight:900;letter-spacing:1px;}}
.cta-box .handle{{font-family:'Space Grotesk';font-size:16px;font-weight:800;color:#fff;}}
.footer{{position:absolute;bottom:50px;left:56px;right:56px;display:flex;justify-content:space-between;font-family:'Space Grotesk';font-size:11px;letter-spacing:2px;color:#000;font-weight:800;}}
</style></head>
<body>
  <div class="grid-pattern"></div>
  <div class="top-bar">
    <div class="logo">NOGEAR · FINAL</div>
    <div class="page">{idx:02d} / {total:02d}</div>
  </div>
  <div class="mark">— NOGEAR MANIFESTO —</div>
  <div class="slogan">
    FXXK<br>
    FAKES.<br>
    STAY <span class="white">NATURAL.</span>
  </div>
  <div class="line-break"></div>
  <div class="meaning">
    진짜 몸은 진짜 노력으로만 만들어진다.<br>
    약물로 만든 몸은 약물이 없으면 존재하지 않는다.
  </div>
  <div class="cta-box">
    <div class="text">저장 · 공유 · 팔로우</div>
    <div class="handle">@nogear.magazine</div>
  </div>
  <div class="footer">
    <div>nogear-magazine.vercel.app</div>
    <div>DAILY · AUTO · FACT</div>
  </div>
</body></html>"""


# ── SAVE SLIDE ──
def feature_callout_card(feature: dict, idx: int, total: int) -> str:
    """주간 피처 예고 카드 (월요일 피처 있으면)"""
    title = feature.get('title', '주간 딥다이브 피처')
    subtitle = feature.get('subtitle', '')
    keyword = feature.get('keyword', '')
    citations = feature.get('citations', 0)

    return f"""<!DOCTYPE html>
<html><head><meta charset="utf-8">
<style>
@import url('https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@400;700;900&family=Space+Grotesk:wght@700;900&display=swap');
*{{margin:0;padding:0;box-sizing:border-box;}}
body{{width:1080px;height:1350px;background:{DESIGN['bg_alt']};font-family:'Noto Sans KR',sans-serif;color:{DESIGN['white']};overflow:hidden;position:relative;}}
.top-bar{{position:absolute;top:0;left:0;right:0;height:50px;display:flex;align-items:center;justify-content:space-between;padding:0 56px;border-bottom:1px solid rgba(255,255,255,.06);}}
.top-bar .logo{{font-family:'Space Grotesk';font-size:16px;font-weight:900;letter-spacing:2px;}}
.top-bar .logo .n{{color:{DESIGN['red']};}}
.top-bar .page{{font-family:'Space Grotesk';font-size:12px;font-weight:800;color:{DESIGN['grey']};letter-spacing:3px;}}
.badge{{position:absolute;top:140px;left:56px;display:inline-flex;gap:8px;align-items:center;}}
.badge .chip{{padding:8px 16px;background:{DESIGN['red']};color:#000;font-family:'Space Grotesk';font-size:11px;font-weight:900;letter-spacing:3px;}}
.badge .month{{font-family:'Space Grotesk';font-size:13px;font-weight:800;color:{DESIGN['grey']};letter-spacing:2px;}}
.title{{position:absolute;top:240px;left:56px;right:56px;font-size:58px;font-weight:900;line-height:1.1;letter-spacing:-1.5px;}}
.title .red{{color:{DESIGN['red']};}}
.subtitle{{position:absolute;top:560px;left:56px;right:56px;font-size:22px;font-weight:400;color:{DESIGN['grey']};line-height:1.6;}}
.stats{{position:absolute;bottom:200px;left:56px;right:56px;display:flex;justify-content:space-between;border-top:1px solid rgba(255,255,255,.1);padding-top:24px;}}
.stat .val{{font-family:'Space Grotesk';font-size:40px;font-weight:900;color:{DESIGN['red']};line-height:1;}}
.stat .label{{font-size:10px;color:{DESIGN['dark_grey']};letter-spacing:2px;margin-top:6px;font-weight:800;}}
.cta-row{{position:absolute;bottom:50px;left:56px;right:56px;display:flex;align-items:center;justify-content:space-between;}}
.cta-row .read{{padding:14px 32px;background:{DESIGN['red']};color:#000;font-size:15px;font-weight:900;letter-spacing:1px;}}
.cta-row .url{{font-family:'Space Grotesk';font-size:11px;color:{DESIGN['dark_grey']};letter-spacing:2px;}}
</style></head>
<body>
  <div class="top-bar">
    <div class="logo"><span class="n">NO</span>GEAR MAGAZINE</div>
    <div class="page">{idx:02d} / {total:02d}</div>
  </div>
  <div class="badge">
    <div class="chip">DEEP DIVE</div>
    <div class="month">이번 주 피처</div>
  </div>
  <div class="title">{title[:90]}</div>
  <div class="subtitle">{subtitle[:150]}</div>
  <div class="stats">
    <div class="stat"><div class="val">{citations}</div><div class="label">논문 인용</div></div>
    <div class="stat"><div class="val">3,200+</div><div class="label">자 분량</div></div>
    <div class="stat"><div class="val">{keyword[:8]}</div><div class="label">키워드</div></div>
  </div>
  <div class="cta-row">
    <div class="read">읽기 →</div>
    <div class="url">nogear-magazine.vercel.app</div>
  </div>
</body></html>"""


# ── VIRAL CAPTION ──
def viral_caption(top_articles: list, brief: dict = None) -> str:
    """바이럴 마케팅 기반 캡션"""
    now = datetime.now(KST)
    date_str = now.strftime("%m/%d")
    day_ko = ["월","화","수","목","금","토","일"][now.weekday()]

    top = top_articles[0]
    hero = extract_hero_number(top.get('title_rewrite', top.get('title', '')))
    hero_num = hero['full'] if hero else ''

    # 훅: 첫 2줄이 인스타 미리보기에서 가장 중요
    lines = [
        f"━━━━━━━━━━━━━━━━",
        f"⚠️ {hero_num} — 이 숫자를 보고도 계속 쓸 건가?",
        f"",
        f"🔥 {top.get('title', '')[:60]}",
        f"",
        "━━━━━━━━━━━━━━━━",
        "",
        "오늘의 핵심 인텔 (논문 기반)",
        "",
    ]

    for i, a in enumerate(top_articles[:4]):
        emoji = a.get('viral_emoji', '⚪')
        title = a.get('title_rewrite', a.get('title', ''))
        lines.append(f"{emoji} {i+1}. {title}")
        lines.append("")

    lines.extend([
        "━━━━━━━━━━━━━━━━",
        "",
        "📌 저장해두세요. 매일 업데이트됩니다.",
        "",
        "👉 더 많은 팩트 → @nogear.magazine",
        "🔗 링크 → nogear-magazine.vercel.app",
        "",
        "FXXK FAKES. STAY NATURAL.",
        "",
        "━━━━━━━━━━━━━━━━",
        "",
        # 해시태그 전략 (바이럴 최적화)
        "#헬스 #보디빌딩 #피트니스 #헬스타그램 #운동",
        "#스테로이드 #약물부작용 #네추럴보디빌딩 #논문기반 #건강정보",
        "#스테로이드부작용 #페이크내추럴 #헬스정보 #운동과학 #피트니스팁",
        "#헬스그램 #다이어트 #보충제 #운동루틴 #몸스타그램",
        "#fitnesskorea #healthylifestyle #natural #wellness",
        "#NOGEAR #FxxkFakes #StayNatural #카드뉴스 #운동뉴스",
    ])

    return "\n".join(lines)


def main():
    now = datetime.now(KST)
    date_slug = now.strftime("%Y%m%d")
    date_str = now.strftime("%Y.%m.%d")

    print(f"🔥 NOGEAR VIRAL Cardnews Generator v2")
    print(f"⏰ {now.strftime('%Y-%m-%d %H:%M KST')}")

    # 데이터 로드
    with open(CONTENT_FILE, encoding="utf-8") as f:
        data = json.load(f)
    news = data.get("news", [])

    # 카피라이터 리라이트 로드
    rewrites = {}
    if COPY_FILE.exists():
        with open(COPY_FILE, encoding="utf-8") as f:
            copy_data = json.load(f)
        # rewrites를 title 기준으로 매핑
        for r in copy_data.get("rewrites", []):
            orig = r.get("original", "")
            best = r.get("best", "")
            if orig and best:
                rewrites[orig] = best

    # 편집장 브리프 로드
    brief = {}
    if BRIEF_FILE.exists():
        with open(BRIEF_FILE, encoding="utf-8") as f:
            brief = json.load(f)

    # 피처 로드
    feature = None
    features_idx = BASE / "content" / "editorial" / "features" / "index.json"
    if features_idx.exists():
        with open(features_idx, encoding="utf-8") as f:
            features_data = json.load(f)
        if features_data.get("features"):
            feature = features_data["features"][0]

    # TOP 기사 선택 + 리라이트 제목 적용
    top = news[:4]
    for a in top:
        orig_title = a.get("title", "")
        if orig_title in rewrites:
            a["title_rewrite"] = rewrites[orig_title]
        else:
            a["title_rewrite"] = orig_title

    # 출력 폴더
    output_dir = CARDNEWS_DIR / (date_slug + "_viral")
    output_dir.mkdir(parents=True, exist_ok=True)

    # 카드 구성: Cover → 3개 Problem → Evidence → (Feature) → CTA = 6~7장
    cards = []
    total_cards = 5 + (1 if feature else 0)

    # 1. 커버
    cards.append(("00_cover.html", cover_card(top, date_str)))

    # 2-4. 문제 카드 3장 (TOP 3)
    for i, a in enumerate(top[:3]):
        cards.append((f"{i+1:02d}_problem.html", problem_card(a, i+2, total_cards)))

    # 5. 수치/증거 종합
    cards.append(("04_evidence.html", evidence_card(top, 5, total_cards)))

    # 6. 피처 예고 (있으면)
    if feature:
        cards.append(("05_feature.html", feature_callout_card(feature, 6, total_cards)))

    # 마지막. CTA
    cta_idx = len(cards) + 1
    cards.append((f"{cta_idx-1:02d}_cta.html", cta_card(cta_idx, total_cards)))

    # 저장
    for fname, html in cards:
        with open(output_dir / fname, "w", encoding="utf-8") as f:
            f.write(html)
        print(f"   ✅ {fname}")

    # 캡션
    caption = viral_caption(top, brief)
    with open(output_dir / "caption.txt", "w", encoding="utf-8") as f:
        f.write(caption)
    print(f"   ✅ caption.txt")

    # PNG 생성
    print(f"\n🖼️  PNG 변환 중...")
    try:
        from playwright.sync_api import sync_playwright
        with sync_playwright() as p:
            browser = p.chromium.launch()
            page = browser.new_page(viewport={"width": 1080, "height": 1350})
            for fname, _ in cards:
                html_path = output_dir / fname
                page.goto(f"file://{html_path.resolve()}")
                page.wait_for_timeout(500)
                png_name = fname.replace(".html", ".png")
                page.screenshot(path=str(output_dir / png_name), full_page=False)
                print(f"   🖼️  {png_name}")
            browser.close()
    except Exception as e:
        print(f"   ⚠️ 이미지 생성 실패: {e}")

    # 메타
    meta = {
        "generated_at": now.strftime("%Y-%m-%d %H:%M KST"),
        "version": "viral_v2",
        "card_count": len(cards),
        "caption_file": "caption.txt",
        "top_hook": top[0].get("title_rewrite", ""),
        "hero_number": extract_hero_number(top[0].get("title_rewrite", "")),
    }
    with open(output_dir / "meta.json", "w", encoding="utf-8") as f:
        json.dump(meta, f, ensure_ascii=False, indent=2)

    print(f"\n{'='*50}")
    print(f"🚀 VIRAL CARDNEWS READY")
    print(f"   {output_dir}")
    print(f"   카드 {len(cards)}장 + 캡션")
    print(f"   업로드: @nogear.magazine")
    print(f"{'='*50}")


if __name__ == "__main__":
    main()
