#!/usr/bin/env python3
"""
NOGEAR Magazine — Auto Crawl Agent v2 (Haiku)
매일 08:00 / 20:00 KST 자동 실행
30-50개 아티클 수집 → 바이럴 점수 calibration → 정렬 → content/articles.json 업데이트
"""

import os
import json
import re
from datetime import datetime, timezone, timedelta
from pathlib import Path

import anthropic

# ── CONFIG ──────────────────────────────────────────────────────────────────
CONTENT_FILE = Path(__file__).parent.parent / "content" / "articles.json"
MAX_NEWS_ITEMS = 200       # 최대 보관 뉴스 수
NEW_ITEMS_PER_CRAWL = 40   # 크롤당 신규 기사 수 (30-50)
MODEL = "claude-haiku-4-5-20251001"
KST = timezone(timedelta(hours=9))

# ── CONTENT PILLARS (전체 확장) ─────────────────────────────────────────────
CONTENT_PILLARS = {
    "steroids": [
        "anabolic steroids health effects research 2026",
        "AAS cardiovascular liver testosterone study",
        "HPTA suppression recovery steroid cycle",
        "steroid users long-term health outcomes",
        "bodybuilder steroid death heart failure",
    ],
    "drugs": [
        "SARMs clinical trial results dangers",
        "DNP dinitrophenol death overdose 2026",
        "performance enhancing drugs caught athletes",
        "clenbuterol peptides hormone abuse fitness",
        "drug testing positive results sports",
    ],
    "exercise": [
        "hypertrophy muscle growth science breakthrough 2026",
        "training frequency volume research study",
        "natural bodybuilding science evidence",
        "recovery sleep adaptation muscle protein",
        "exercise inflammation fatigue mechanisms",
    ],
    "nutrition": [
        "protein synthesis optimal intake research",
        "supplement efficacy creatine evidence 2026",
        "nutrition myths debunked science study",
        "intermittent fasting muscle loss reality",
        "post-workout nutrition timing evidence",
    ],
    "viral": [
        "fitness influencer steroids exposed confession",
        "bodybuilding supplement fraud scam exposed",
        "doping scandal sports viral 2026",
        "before after transformation fake natty",
        "gym culture controversy viral moment",
    ],
    "science": [
        "exercise science review meta-analysis 2026",
        "strength training longevity lifespan study",
        "testosterone aging muscle preservation",
        "metabolic health fitness intervention study",
        "sports medicine breakthrough research",
    ],
    "industry": [
        "fitness industry fraud supplement false claims",
        "personal trainer steroid use epidemic",
        "natty or not influencer investigation",
        "gym culture toxic masculinity drugs",
        "professional bodybuilder health consequences",
    ],
    "mental": [
        "exercise mental health depression anxiety study",
        "steroid psychological effects aggression",
        "body dysmorphia muscle dysmorphia research",
        "fitness motivation psychology science",
        "overtraining syndrome mental burnout",
    ],
}

# ── SYSTEM PROMPT ────────────────────────────────────────────────────────────
SYSTEM_PROMPT = """You are NOGEAR Magazine's elite research agent. Brand: "FXXK FAKES. STAY NATURAL."

Your mission: Curate 30-50 high-impact articles/news items across fitness, steroids, drugs, exercise science, and industry culture.

For each article output a JSON object with these fields:
- "title": Punchy headline in English (max 90 chars)
- "title_ko": Korean translation/adaptation (임팩트있게)
- "summary": 3-4 sentence detailed summary with KEY MECHANISM if science (English)
- "category": one of [steroids, drugs, exercise, nutrition, viral, science, industry, mental]
- "source": Publication name (e.g., "PubMed / J Strength Cond Res", "Instagram", "New York Times")
- "source_type": one of [journal, news, social, study, documentary]
- "viral_score": INTEGER 0-100 (see scoring below)
- "viral_signals": object with sub-scores (see below)
- "tags": array of 3-5 keyword strings
- "date": "YYYY.MM.DD" format (approximate if unknown)
- "url": URL string if real and confident (omit if uncertain)

VIRAL SCORE FORMULA (0-100):
Calculate "viral_signals" object first, then sum for "viral_score":

{
  "shock_factor": 0-25,        // 충격도: surprising/disturbing/counter-intuitive
  "scientific_credibility": 0-20,  // 논문 신뢰도: peer-reviewed backing
  "relatability": 0-20,        // 공감도: affects most fitness people
  "recency": 0-15,             // 최신성: how recent/trending
  "controversy": 0-10,         // 논쟁성: generates debate
  "visual_potential": 0-10     // 시각화: shareable image/infographic potential
}

"viral_score" = sum of all signal values.

SIGNAL TIER based on score:
- 90-100: 🔴 VIRAL BOMB
- 75-89:  🟠 HOT
- 60-74:  🟡 TRENDING
- 45-59:  ⚪ RELEVANT
- 0-44:   🔵 INFO

Prioritize HIGH viral_score articles. Include:
- 5-8 science/research items (high scientific_credibility)
- 8-12 shocking/dramatic items (high shock_factor)
- 8-12 relatable fitness items (high relatability)
- 5-8 industry/viral items (high controversy)
- 3-5 mental/lifestyle items

Output ONLY a valid JSON array. No markdown, no explanation, no code blocks."""

def load_existing() -> dict:
    if CONTENT_FILE.exists():
        with open(CONTENT_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return {"meta": {}, "featured": [], "news": [], "research": []}

def save_content(data: dict):
    CONTENT_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(CONTENT_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def fetch_articles_batch(client: anthropic.Anthropic, pillars: list[str], now_kst: str) -> list[dict]:
    """Fetch a batch of articles for given content pillars"""

    topics_str = "\n".join(
        f"- [{pillar.upper()}] {topic}"
        for pillar in pillars
        for topic in CONTENT_PILLARS.get(pillar, [])[:3]  # 3 topics per pillar
    )

    prompt = f"""Current time: {now_kst}

Find {NEW_ITEMS_PER_CRAWL} recent, high-impact news items and research across these areas:
{topics_str}

Use your knowledge of recent events, published research, fitness culture, and viral moments.

IMPORTANT: Prioritize items with HIGH viral_score (70+). Think about:
- What would make a natural lifter say "WTF?!"
- What exposes industry BS or drug use?
- What scientific findings overturn common beliefs?
- What scandals/exposés are circulating?

Output exactly {NEW_ITEMS_PER_CRAWL} items as a JSON array."""

    response = client.messages.create(
        model=MODEL,
        max_tokens=8192,
        system=SYSTEM_PROMPT,
        messages=[{"role": "user", "content": prompt}]
    )

    text = response.content[0].text.strip()

    # Extract JSON array
    json_match = re.search(r'\[[\s\S]*\]', text)
    if json_match:
        text = json_match.group(0)

    articles = json.loads(text)
    return articles

def normalize_article(article: dict, now_str: str) -> dict:
    """Ensure article has all required fields"""

    # Calculate viral_score from signals if not set
    signals = article.get("viral_signals", {})
    if signals and not article.get("viral_score"):
        article["viral_score"] = sum(signals.values())

    viral_score = int(article.get("viral_score", 50))
    viral_score = max(0, min(100, viral_score))
    article["viral_score"] = viral_score

    # Assign tier
    if viral_score >= 90:
        article["viral_tier"] = "VIRAL_BOMB"
        article["viral_emoji"] = "🔴"
    elif viral_score >= 75:
        article["viral_tier"] = "HOT"
        article["viral_emoji"] = "🟠"
    elif viral_score >= 60:
        article["viral_tier"] = "TRENDING"
        article["viral_emoji"] = "🟡"
    elif viral_score >= 45:
        article["viral_tier"] = "RELEVANT"
        article["viral_emoji"] = "⚪"
    else:
        article["viral_tier"] = "INFO"
        article["viral_emoji"] = "🔵"

    article.setdefault("date", now_str)
    article.setdefault("crawled_at", datetime.now(timezone.utc).isoformat())
    article.setdefault("source_type", "news")
    article.setdefault("tags", [])

    return article

def deduplicate(existing: list, new_items: list) -> list:
    existing_titles = {n["title"].lower()[:50] for n in existing}
    filtered = []
    for a in new_items:
        key = a["title"].lower()[:50]
        if key not in existing_titles:
            filtered.append(a)
            existing_titles.add(key)
    return filtered

def main():
    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        print("ERROR: ANTHROPIC_API_KEY not set")
        exit(1)

    now_kst = datetime.now(KST)
    now_str = now_kst.strftime("%Y.%m.%d")
    now_iso = now_kst.strftime("%Y-%m-%d %H:%M KST")

    print(f"🔍 NOGEAR Magazine Crawl Agent v2")
    print(f"⏰ {now_iso} | Target: {NEW_ITEMS_PER_CRAWL} articles | Model: {MODEL}")

    client = anthropic.Anthropic(api_key=api_key)

    # Select pillar mix based on time of day
    if now_kst.hour < 12:
        # Morning: heavy on steroids/drugs/viral
        pillars = ["steroids", "drugs", "viral", "industry", "science"]
    else:
        # Evening: exercise/nutrition/mental/science
        pillars = ["exercise", "nutrition", "mental", "viral", "science"]

    print(f"📂 Pillars: {', '.join(pillars)}")

    # Load existing
    data = load_existing()
    existing_news = data.get("news", [])
    print(f"📚 Existing: {len(existing_news)} articles")

    # Fetch new articles
    print("🤖 Fetching articles via Haiku...")
    try:
        raw_articles = fetch_articles_batch(client, pillars, now_iso)
        print(f"✅ Fetched: {len(raw_articles)} articles")
    except json.JSONDecodeError as e:
        print(f"❌ JSON parse error: {e}")
        exit(1)
    except Exception as e:
        print(f"❌ API error: {e}")
        exit(1)

    # Normalize and score
    articles = [normalize_article(a, now_str) for a in raw_articles]

    # Deduplicate
    unique_new = deduplicate(existing_news, articles)
    print(f"🔄 New unique: {len(unique_new)}")

    # Log viral score distribution
    scores = [a["viral_score"] for a in unique_new]
    if scores:
        bombs = sum(1 for s in scores if s >= 90)
        hot = sum(1 for s in scores if 75 <= s < 90)
        trend = sum(1 for s in scores if 60 <= s < 75)
        print(f"📊 Scores — 🔴 VIRAL: {bombs} | 🟠 HOT: {hot} | 🟡 TRENDING: {trend}")
        print(f"📊 Avg score: {sum(scores)/len(scores):.1f} | Max: {max(scores)} | Min: {min(scores)}")

    # Merge and sort by viral_score (DESC)
    all_news = unique_new + existing_news
    all_news.sort(key=lambda x: x.get("viral_score", 0), reverse=True)
    all_news = all_news[:MAX_NEWS_ITEMS]

    # Update data
    data["news"] = all_news
    data["meta"] = {
        "last_updated": datetime.now(timezone.utc).isoformat(),
        "last_updated_kst": now_iso,
        "total_articles": 12 + len(all_news),
        "studies_cited": 47 + sum(1 for a in all_news if a.get("source_type") == "journal"),
        "crawl_count": data.get("meta", {}).get("crawl_count", 0) + 1,
        "news_count": len(all_news),
        "model": MODEL,
        "top_viral_score": all_news[0]["viral_score"] if all_news else 0,
        "avg_viral_score": round(sum(a.get("viral_score",0) for a in all_news[:20]) / min(20, len(all_news)), 1) if all_news else 0,
    }

    save_content(data)
    crawl_n = data["meta"]["crawl_count"]
    print(f"💾 Saved {len(all_news)} articles (sorted by viral score)")
    print(f"🏆 Top article: [{all_news[0]['viral_score']}] {all_news[0]['title'][:60]}..." if all_news else "")
    print(f"✅ Crawl #{crawl_n} complete")

if __name__ == "__main__":
    main()
