#!/usr/bin/env python3
"""
NOGEAR Magazine — Auto Crawl Agent (Haiku)
매일 08:00 / 20:00 KST 자동 실행
운동/약물/스테로이드/바이럴 뉴스 수집 → content/articles.json 업데이트
"""

import os
import json
import re
from datetime import datetime, timezone, timedelta
from pathlib import Path

import anthropic

# ── CONFIG ──────────────────────────────────────────────────────────────────
CONTENT_FILE = Path(__file__).parent.parent / "content" / "articles.json"
MAX_NEWS_ITEMS = 60       # 최대 보관 뉴스 수
NEW_ITEMS_PER_CRAWL = 12  # 크롤당 신규 기사 수
MODEL = "claude-haiku-4-5-20251001"

KST = timezone(timedelta(hours=9))

SEARCH_TOPICS = [
    # 스테로이드 & AAS
    "anabolic steroids bodybuilding research 2026",
    "steroid use health effects study",
    "HPTA testosterone suppression",
    "AAS cardiovascular effects new research",
    # 약물 & PED
    "SARMs clinical trial results",
    "performance enhancing drugs athletes caught",
    "DNP dangerous diet drug death",
    "peptide hormones bodybuilding abuse",
    # 운동 과학 (바이럴)
    "exercise science viral study 2026",
    "fitness training research breakthrough",
    "natural bodybuilding science hypertrophy",
    "muscle growth protein synthesis study",
    # 바이럴 / 뉴스
    "fitness influencer steroids exposed",
    "doping scandal sports 2026",
    "bodybuilding health documentary",
    "drug testing sports news",
]

SYSTEM_PROMPT = """You are NOGEAR Magazine's research agent. Brand: "FXXK FAKES. STAY NATURAL."

Your job: Find real, viral-worthy news and research about:
- Steroids, SARMs, PEDs and their health effects
- Exercise science breakthroughs
- Fitness/bodybuilding industry scandals or viral moments
- Drug use consequences in sports/fitness

For each article, provide:
- title: Punchy, Korean-friendly headline (English OK, max 80 chars)
- title_ko: Korean translation/adaptation
- summary: 2-3 sentence summary (English)
- category: one of [steroids, drugs, exercise, viral, science, news]
- source: Publication/source name
- url: URL if real (omit if uncertain)
- relevance: Why this matters to natural fitness community (1 sentence)
- tags: list of 2-4 keyword tags

Prioritize:
1. Paper-backed science with mechanisms explained
2. Viral news about PED consequences
3. Bodybuilding industry exposés
4. Practical exercise science

Output ONLY valid JSON array. No markdown, no explanation."""

def load_existing() -> dict:
    """Load existing content.json"""
    if CONTENT_FILE.exists():
        with open(CONTENT_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return {"meta": {}, "featured": [], "news": [], "research": []}

def save_content(data: dict):
    """Save updated content.json"""
    with open(CONTENT_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def fetch_new_articles(client: anthropic.Anthropic, run_topics: list[str]) -> list[dict]:
    """Use Haiku to find and curate news articles"""

    topics_str = "\n".join(f"- {t}" for t in run_topics)
    now_kst = datetime.now(KST).strftime("%Y-%m-%d %H:%M KST")

    prompt = f"""Current time: {now_kst}

Search for {NEW_ITEMS_PER_CRAWL} recent, high-quality news items on these topics:
{topics_str}

Use your knowledge of recent events, research publications, and fitness/sports news.
Focus on content from the last few weeks/months that would interest the NOGEAR audience.

Include a mix of:
- 3-4 science/research items (PubMed-level quality)
- 3-4 viral/news items (shocking, shareable)
- 2-3 exercise science items
- 2-3 industry/doping news items

Output a JSON array of exactly {NEW_ITEMS_PER_CRAWL} items."""

    response = client.messages.create(
        model=MODEL,
        max_tokens=4096,
        system=SYSTEM_PROMPT,
        messages=[{"role": "user", "content": prompt}]
    )

    text = response.content[0].text.strip()

    # Extract JSON from response
    # Try to find JSON array
    json_match = re.search(r'\[[\s\S]*\]', text)
    if json_match:
        text = json_match.group(0)

    articles = json.loads(text)

    # Add metadata to each article
    now_str = datetime.now(KST).strftime("%Y.%m.%d")
    for article in articles:
        article["date"] = article.get("date", now_str)
        article["crawled_at"] = datetime.now(timezone.utc).isoformat()

    return articles

def deduplicate(existing_news: list, new_articles: list) -> list:
    """Remove duplicate titles"""
    existing_titles = {n["title"].lower()[:40] for n in existing_news}
    filtered = []
    for a in new_articles:
        key = a["title"].lower()[:40]
        if key not in existing_titles:
            filtered.append(a)
            existing_titles.add(key)
    return filtered

def main():
    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        print("ERROR: ANTHROPIC_API_KEY not set")
        exit(1)

    topic_filter = os.environ.get("CRAWL_TOPIC", "all")

    # Select topics for this run
    if topic_filter == "all":
        # Rotate through topics: use time-based selection for variety
        hour = datetime.now(KST).hour
        if hour < 12:
            run_topics = SEARCH_TOPICS[:8]   # Morning: steroids/AAS focus
        else:
            run_topics = SEARCH_TOPICS[8:]   # Evening: viral/exercise focus
    else:
        run_topics = [t for t in SEARCH_TOPICS if topic_filter.lower() in t.lower()]
        if not run_topics:
            run_topics = SEARCH_TOPICS[:8]

    print(f"🔍 Starting crawl — {len(run_topics)} topics | Model: {MODEL}")
    print(f"⏰ Time: {datetime.now(KST).strftime('%Y-%m-%d %H:%M KST')}")

    client = anthropic.Anthropic(api_key=api_key)

    # Load existing content
    data = load_existing()
    existing_news = data.get("news", [])
    print(f"📚 Existing articles: {len(existing_news)}")

    # Fetch new articles
    print("🤖 Fetching new articles via Haiku...")
    new_articles = fetch_new_articles(client, run_topics)
    print(f"✅ Fetched: {len(new_articles)} articles")

    # Deduplicate
    unique_new = deduplicate(existing_news, new_articles)
    print(f"🔄 New unique articles: {len(unique_new)}")

    # Prepend new articles, trim to max
    updated_news = unique_new + existing_news
    updated_news = updated_news[:MAX_NEWS_ITEMS]

    # Update metadata
    data["news"] = updated_news
    data["meta"] = {
        "last_updated": datetime.now(timezone.utc).isoformat(),
        "last_updated_kst": datetime.now(KST).strftime("%Y-%m-%d %H:%M KST"),
        "total_articles": 12 + len(updated_news),  # static articles + news
        "studies_cited": 47,
        "crawl_count": data.get("meta", {}).get("crawl_count", 0) + 1,
        "news_count": len(updated_news),
        "model": MODEL,
    }

    # Save
    save_content(data)
    print(f"💾 Saved {len(updated_news)} news items")
    print(f"📊 Crawl #{data['meta']['crawl_count']} complete")

if __name__ == "__main__":
    main()
