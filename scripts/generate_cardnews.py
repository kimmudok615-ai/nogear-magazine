#!/usr/bin/env python3
"""
NOGEAR Magazine — 카드뉴스 자동 생성기
TOP 기사 → 인스타 카드뉴스 HTML 템플릿 생성
@nogear.magazine 계정용

출력: cardnews/ 폴더에 HTML 파일 + 캡션 텍스트
"""

import json
from datetime import datetime, timezone, timedelta
from pathlib import Path

KST = timezone(timedelta(hours=9))
BASE = Path(__file__).parent.parent
CONTENT_FILE = BASE / "content" / "articles.json"
FEATURED_FILE = BASE / "content" / "featured.json"
CARDNEWS_DIR = BASE / "cardnews"

# 카드 수 설정
CARDS_PER_POST = 5  # 인스타 캐러셀 슬라이드 수 (커버 + 4장)


def load_articles():
    with open(CONTENT_FILE, encoding="utf-8") as f:
        return json.load(f)


def generate_card_html(article: dict, card_num: int, total: int) -> str:
    """개별 카드 HTML 생성 (1080x1350 인스타 세로)"""
    title = article.get("title", "")
    summary = article.get("summary", "")
    detail = article.get("summary_detail", "")
    score = article.get("viral_score", 0)
    emoji = article.get("viral_emoji", "⚪")
    category_ko = article.get("category_ko", article.get("category", ""))
    source = article.get("source", "")
    tags = article.get("tags", [])

    score_color = "#FF2D20" if score >= 90 else "#F59E0B" if score >= 75 else "#3B82F6"

    # 본문 텍스트 결정 (detail이 있으면 detail, 없으면 summary)
    body_text = detail if detail else summary
    # 너무 길면 자르기
    if len(body_text) > 280:
        body_text = body_text[:277] + "..."

    return f"""<!DOCTYPE html>
<html><head><meta charset="utf-8">
<style>
@import url('https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@400;700;900&display=swap');
* {{ margin:0; padding:0; box-sizing:border-box; }}
body {{
  width:1080px; height:1350px;
  background:#030306;
  font-family:'Noto Sans KR',sans-serif;
  color:#F4F4F6;
  display:flex; flex-direction:column;
  overflow:hidden;
}}
.top-bar {{
  display:flex; align-items:center; justify-content:space-between;
  padding:40px 56px 0;
}}
.logo {{
  font-size:20px; font-weight:900; letter-spacing:3px;
}}
.logo .n {{ color:#FF2D20; }}
.logo .mag {{ font-size:10px; color:#555; letter-spacing:5px; margin-left:4px; }}
.page-num {{
  font-size:14px; font-weight:700; color:#333; letter-spacing:2px;
}}
.category-bar {{
  margin:28px 56px 0;
  display:flex; align-items:center; gap:12px;
}}
.cat-tag {{
  padding:6px 16px; border-radius:4px;
  font-size:12px; font-weight:800; letter-spacing:1px;
  background:rgba(255,45,32,.1); border:1px solid rgba(255,45,32,.2); color:#FF2D20;
}}
.viral-tag {{
  padding:6px 16px; border-radius:4px;
  font-size:14px; font-weight:900;
  background:rgba(255,255,255,.03); border:1px solid rgba(255,255,255,.06);
  color:{score_color};
}}
.title-area {{
  padding:36px 56px 0;
  flex-shrink:0;
}}
.title {{
  font-size:42px; font-weight:900; line-height:1.25;
  letter-spacing:-1px;
  max-height:210px; overflow:hidden;
}}
.body-area {{
  padding:32px 56px 0;
  flex:1;
  overflow:hidden;
}}
.body-text {{
  font-size:22px; font-weight:400; line-height:1.75;
  color:#AAA;
}}
.bottom-bar {{
  padding:32px 56px 40px;
  display:flex; align-items:center; justify-content:space-between;
  border-top:1px solid rgba(255,255,255,.06);
  margin-top:auto;
}}
.source {{
  font-size:13px; color:#444; font-weight:700; letter-spacing:.5px;
}}
.swipe {{
  font-size:13px; color:#333; font-weight:700;
  display:flex; align-items:center; gap:6px;
}}
.red-line {{
  position:absolute; top:0; left:0; right:0; height:4px;
  background:linear-gradient(90deg, #FF2D20, transparent);
}}
</style></head>
<body>
  <div class="red-line"></div>
  <div class="top-bar">
    <div class="logo"><span class="n">NO</span>GEAR<span class="mag">MAGAZINE</span></div>
    <div class="page-num">{card_num}/{total}</div>
  </div>
  <div class="category-bar">
    <div class="cat-tag">{category_ko}</div>
    <div class="viral-tag">{emoji} {score}</div>
  </div>
  <div class="title-area">
    <div class="title">{title}</div>
  </div>
  <div class="body-area">
    <div class="body-text">{body_text}</div>
  </div>
  <div class="bottom-bar">
    <div class="source">📄 {source}</div>
    <div class="swipe">{'밀어서 다음 →' if card_num < total else 'FXXK FAKES. STAY NATURAL.'}</div>
  </div>
</body></html>"""


def generate_cover_html(articles: list) -> str:
    """커버 카드 (첫 슬라이드)"""
    now = datetime.now(KST)
    date_str = now.strftime("%Y.%m.%d")
    day_ko = ["월","화","수","목","금","토","일"][now.weekday()]

    titles_preview = ""
    for i, a in enumerate(articles[:4]):
        titles_preview += f"""
        <div style="display:flex;align-items:flex-start;gap:12px;margin-bottom:16px;">
          <div style="font-size:28px;font-weight:900;color:#FF2D20;min-width:36px;">{i+1:02d}</div>
          <div style="font-size:20px;font-weight:700;line-height:1.35;color:#888;">{a.get('title','')[:35]}...</div>
        </div>"""

    return f"""<!DOCTYPE html>
<html><head><meta charset="utf-8">
<style>
@import url('https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@400;700;900&display=swap');
* {{ margin:0; padding:0; box-sizing:border-box; }}
body {{
  width:1080px; height:1350px;
  background:#030306;
  font-family:'Noto Sans KR',sans-serif;
  color:#F4F4F6;
  display:flex; flex-direction:column;
  justify-content:center;
  overflow:hidden;
  position:relative;
}}
.red-line {{ position:absolute; top:0; left:0; right:0; height:4px; background:#FF2D20; }}
.glow {{ position:absolute; top:-100px; left:50%; transform:translateX(-50%); width:600px; height:400px; background:radial-gradient(ellipse,rgba(255,45,32,.08),transparent 70%); pointer-events:none; }}
</style></head>
<body>
  <div class="red-line"></div>
  <div class="glow"></div>

  <div style="padding:0 56px;">
    <div style="font-size:20px;font-weight:900;letter-spacing:3px;margin-bottom:8px;">
      <span style="color:#FF2D20;">NO</span>GEAR
      <span style="font-size:10px;color:#555;letter-spacing:5px;margin-left:4px;">MAGAZINE</span>
    </div>
    <div style="font-size:13px;color:#333;letter-spacing:2px;font-weight:700;margin-bottom:48px;">
      {date_str} ({day_ko}) · DAILY DIGEST
    </div>

    <div style="font-size:64px;font-weight:900;line-height:1.05;letter-spacing:-2px;margin-bottom:48px;">
      오늘의<br>
      <span style="color:#FF2D20;">핵심 뉴스</span>
    </div>

    <div style="margin-bottom:40px;">
      {titles_preview}
    </div>

    <div style="font-size:14px;color:#333;font-weight:700;letter-spacing:1px;">
      밀어서 읽기 →
    </div>
  </div>

  <div style="position:absolute;bottom:40px;left:56px;right:56px;display:flex;justify-content:space-between;align-items:center;">
    <div style="font-size:12px;color:#222;letter-spacing:2px;font-weight:800;">FXXK FAKES. STAY NATURAL.</div>
    <div style="font-size:12px;color:#222;">@nogear.magazine</div>
  </div>
</body></html>"""


def generate_caption(articles: list) -> str:
    """인스타 캡션 자동 생성"""
    now = datetime.now(KST)
    date_str = now.strftime("%m/%d")
    day_ko = ["월","화","수","목","금","토","일"][now.weekday()]

    lines = [
        f"📡 NOGEAR MAGAZINE [{date_str}({day_ko})]",
        f"오늘의 핵심 뉴스 {len(articles)}선",
        "",
    ]

    for i, a in enumerate(articles):
        emoji = a.get("viral_emoji", "⚪")
        title = a.get("title", "")
        lines.append(f"{emoji} {i+1}. {title}")

    lines.extend([
        "",
        "👉 밀어서 자세히 보기",
        "🔗 전체 매거진: nogear-magazine.vercel.app",
        "",
        "—",
        "FXXK FAKES. STAY NATURAL.",
        "@nogear.magazine",
        "",
        "#NOGEAR #노기어 #스테로이드 #약물부작용 #네추럴보디빌딩",
        "#피트니스과학 #운동과학 #헬스정보 #카드뉴스 #약물위험성",
        "#보디빌딩 #자연근육 #StayNatural #FxxkFakes",
        "#펩타이드 #SARMs #DNP #스테로이드부작용 #논문기반",
    ])

    return "\n".join(lines)


def main():
    now = datetime.now(KST)
    now_str = now.strftime("%Y-%m-%d %H:%M KST")
    date_slug = now.strftime("%Y%m%d")

    print(f"🎨 NOGEAR Magazine 카드뉴스 생성기")
    print(f"⏰ {now_str}")

    data = load_articles()
    news = data.get("news", [])

    # TOP 4 기사 선택 (커버 + 4장 = 5장 캐러셀)
    top = news[:4]
    print(f"📰 TOP {len(top)} 기사 선택")

    # 출력 폴더
    output_dir = CARDNEWS_DIR / date_slug
    output_dir.mkdir(parents=True, exist_ok=True)

    # 1. 커버 생성
    cover_html = generate_cover_html(top)
    cover_path = output_dir / "00_cover.html"
    with open(cover_path, "w", encoding="utf-8") as f:
        f.write(cover_html)
    print(f"✅ 커버 → {cover_path.name}")

    # 2. 개별 카드 생성
    for i, article in enumerate(top):
        card_html = generate_card_html(article, i + 1, len(top))
        card_path = output_dir / f"{i+1:02d}_card.html"
        with open(card_path, "w", encoding="utf-8") as f:
            f.write(card_html)
        print(f"✅ 카드 {i+1} → {card_path.name} | [{article.get('viral_score',0)}] {article.get('title','')[:30]}")

    # 3. 캡션 생성
    caption = generate_caption(top)
    caption_path = output_dir / "caption.txt"
    with open(caption_path, "w", encoding="utf-8") as f:
        f.write(caption)
    print(f"✅ 캡션 → {caption_path.name}")

    # 4. HTML → PNG 변환 (Playwright)
    png_paths = []
    print(f"\n🖼️  이미지 생성 중...")
    try:
        from playwright.sync_api import sync_playwright
        with sync_playwright() as p:
            browser = p.chromium.launch()
            page = browser.new_page(viewport={"width": 1080, "height": 1350})

            # 커버
            page.goto(f"file://{cover_path.resolve()}")
            page.wait_for_timeout(500)
            png_cover = output_dir / "00_cover.png"
            page.screenshot(path=str(png_cover))
            png_paths.append(png_cover)
            print(f"   🖼️  00_cover.png ✅")

            # 개별 카드
            for i in range(len(top)):
                html_path = output_dir / f"{i+1:02d}_card.html"
                page.goto(f"file://{html_path.resolve()}")
                page.wait_for_timeout(300)
                png_path = output_dir / f"{i+1:02d}_card.png"
                page.screenshot(path=str(png_path))
                png_paths.append(png_path)
                print(f"   🖼️  {i+1:02d}_card.png ✅")

            browser.close()
        print(f"   총 {len(png_paths)}장 PNG 생성 완료!")
    except Exception as e:
        print(f"   ⚠️ 이미지 생성 실패: {e}")
        print(f"   HTML 파일은 정상 생성됨 — 수동 스크린샷 가능")

    # 5. 메타 저장
    meta = {
        "generated_at": now_str,
        "articles": [{"title": a.get("title",""), "viral_score": a.get("viral_score",0)} for a in top],
        "card_count": len(top) + 1,
        "caption_file": "caption.txt",
        "png_files": [p.name for p in png_paths],
    }
    meta_path = output_dir / "meta.json"
    with open(meta_path, "w", encoding="utf-8") as f:
        json.dump(meta, f, ensure_ascii=False, indent=2)

    print(f"\n{'='*40}")
    print(f"📊 카드뉴스 생성 완료")
    print(f"   위치: cardnews/{date_slug}/")
    print(f"   슬라이드: {len(top)+1}장 (커버 + {len(top)})")
    print(f"   PNG: {len(png_paths)}장")
    print(f"   캡션: caption.txt")
    print(f"{'='*40}")


if __name__ == "__main__":
    main()
