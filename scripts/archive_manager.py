#!/usr/bin/env python3
"""
NOGEAR Magazine — 아카이브 매니저
매일 크롤 후 자동 실행
- 바이럴 85+ → featured.json (명예의 전당, 영구 보관)
- 7일 지난 + 바이럴 75 미만 → archive/YYYY-MM.json
- 활성 피드(articles.json)는 최신 50개만 유지
"""

import json
from datetime import datetime, timezone, timedelta
from pathlib import Path

KST = timezone(timedelta(hours=9))
BASE = Path(__file__).parent.parent / "content"
ARTICLES_FILE = BASE / "articles.json"
FEATURED_FILE = BASE / "featured.json"
ARCHIVE_DIR = BASE / "archive"

# 설정
MAX_ACTIVE = 50          # 활성 피드 최대 기사 수
FEATURED_THRESHOLD = 85  # 이 점수 이상은 명예의 전당
ARCHIVE_AGE_DAYS = 7     # 이 일수 지나면 아카이브 대상
ARCHIVE_SCORE_BELOW = 75 # 이 점수 미만이면 아카이브


def load_json(path: Path) -> dict:
    if path.exists():
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}


def save_json(path: Path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def parse_date(date_str: str) -> datetime:
    """다양한 날짜 포맷 파싱"""
    for fmt in ["%Y.%m.%d", "%Y-%m-%d", "%Y/%m/%d"]:
        try:
            return datetime.strptime(date_str, fmt).replace(tzinfo=KST)
        except ValueError:
            continue
    return datetime.now(KST)  # 파싱 실패 시 오늘 날짜


def main():
    now = datetime.now(KST)
    now_str = now.strftime("%Y-%m-%d %H:%M KST")
    print(f"📦 NOGEAR Magazine 아카이브 매니저")
    print(f"⏰ {now_str}")

    # 1. 현재 데이터 로드
    data = load_json(ARTICLES_FILE)
    news = data.get("news", [])
    meta = data.get("meta", {})
    print(f"📚 현재 활성 기사: {len(news)}건")

    # 2. featured.json 로드 (기존 명예의 전당)
    featured_data = load_json(FEATURED_FILE)
    featured_list = featured_data.get("articles", [])
    featured_titles = {a.get("title", "")[:40].lower() for a in featured_list}
    print(f"🏆 기존 명예의 전당: {len(featured_list)}건")

    # 3. 분류 시작
    keep_active = []       # 활성 피드에 남길 기사
    new_featured = []      # 명예의 전당에 추가할 기사
    to_archive = []        # 아카이브로 보낼 기사

    cutoff = now - timedelta(days=ARCHIVE_AGE_DAYS)

    for article in news:
        score = article.get("viral_score", 0)
        date = parse_date(article.get("date", ""))
        title_key = article.get("title", "")[:40].lower()

        # 바이럴 85+ → 명예의 전당 (중복 체크)
        if score >= FEATURED_THRESHOLD and title_key not in featured_titles:
            new_featured.append(article)
            featured_titles.add(title_key)

        # 7일 지남 + 75 미만 → 아카이브
        if date < cutoff and score < ARCHIVE_SCORE_BELOW:
            to_archive.append(article)
        else:
            keep_active.append(article)

    # 4. 활성 피드가 MAX_ACTIVE 초과 시 추가 아카이브
    if len(keep_active) > MAX_ACTIVE:
        # 바이럴 점수 낮은 순으로 초과분 아카이브
        keep_active.sort(key=lambda x: x.get("viral_score", 0), reverse=True)
        overflow = keep_active[MAX_ACTIVE:]
        keep_active = keep_active[:MAX_ACTIVE]
        to_archive.extend(overflow)
        print(f"📤 활성 피드 초과분 {len(overflow)}건 → 아카이브")

    # 5. 명예의 전당 저장
    if new_featured:
        featured_list.extend(new_featured)
        featured_list.sort(key=lambda x: x.get("viral_score", 0), reverse=True)
        featured_data = {
            "meta": {
                "last_updated": datetime.now(timezone.utc).isoformat(),
                "total": len(featured_list),
                "threshold": FEATURED_THRESHOLD,
                "description": "바이럴 85점 이상 핵심 기사 — 영구 보관"
            },
            "articles": featured_list
        }
        save_json(FEATURED_FILE, featured_data)
        print(f"🏆 명예의 전당 +{len(new_featured)}건 → 총 {len(featured_list)}건")

    # 6. 월별 아카이브 저장
    if to_archive:
        # 월별로 분류
        monthly = {}
        for article in to_archive:
            date = parse_date(article.get("date", ""))
            month_key = date.strftime("%Y-%m")
            if month_key not in monthly:
                monthly[month_key] = []
            monthly[month_key].append(article)

        for month_key, articles in monthly.items():
            archive_file = ARCHIVE_DIR / f"{month_key}.json"
            existing = load_json(archive_file)
            existing_list = existing.get("articles", [])
            existing_titles = {a.get("title", "")[:40].lower() for a in existing_list}

            # 중복 제거 후 추가
            new_items = [a for a in articles if a.get("title", "")[:40].lower() not in existing_titles]
            existing_list.extend(new_items)
            existing_list.sort(key=lambda x: x.get("viral_score", 0), reverse=True)

            archive_data = {
                "meta": {
                    "month": month_key,
                    "total": len(existing_list),
                    "last_updated": datetime.now(timezone.utc).isoformat()
                },
                "articles": existing_list
            }
            save_json(archive_file, archive_data)
            print(f"📂 아카이브 {month_key}: +{len(new_items)}건 → 총 {len(existing_list)}건")

    # 7. 활성 피드 업데이트
    keep_active.sort(key=lambda x: x.get("viral_score", 0), reverse=True)
    data["news"] = keep_active
    data["meta"]["news_count"] = len(keep_active)
    data["meta"]["last_archive"] = datetime.now(timezone.utc).isoformat()
    data["meta"]["featured_count"] = len(featured_list)
    data["meta"]["archived_count"] = len(to_archive)
    save_json(ARTICLES_FILE, data)

    # 8. 리포트
    print(f"\n{'='*40}")
    print(f"📊 아카이브 결과:")
    print(f"   활성 피드: {len(keep_active)}건 (최대 {MAX_ACTIVE})")
    print(f"   명예의 전당: {len(featured_list)}건 (바이럴 {FEATURED_THRESHOLD}+)")
    print(f"   이번 아카이브: {len(to_archive)}건")
    print(f"{'='*40}")


if __name__ == "__main__":
    main()
