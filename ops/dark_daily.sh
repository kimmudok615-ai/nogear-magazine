#!/usr/bin/env bash
# 다크사이드 계정 하루치 — 맥 launchd(ops/com.darkside.daily.plist)가 매일 부른다.
#   1) 캐러셀 2편 생성(dark_daily)  2) 그날 카드만 커밋·push → Vercel 이 공개 URL 로 배포
#   3) 인스타 게시 — 캐러셀 + 8초 릴스(dark_publish, 자격증명 있을 때만)
#   4) 48시간 지난 게시물 측정 → 다음 소재 가중치(dark_measure)  5) 텔레그램 보고(dark_notify)
# 2026-09-24 Andy 결정: 승인 없이 자동. 가드(dark_guard)가 유일한 문.
set -uo pipefail
cd "$(dirname "$0")/.."
TODAY=$(date +%Y%m%d)
LOG=data/dark_daily.log; mkdir -p data
REPORT=$(mktemp)

if [ "$(git rev-parse --abbrev-ref HEAD)" != "main" ]; then
  echo "main 브랜치가 아니라 중단 (다른 작업 브랜치를 main 으로 밀지 않는다)" | python3 scripts/dark_notify.py
  exit 1
fi
git pull -q --ff-only origin main || echo "pull 실패 — 로컬 그대로 진행" >> "$REPORT"
python3 scripts/dark_daily.py --count 2 >> "$REPORT" 2>&1

DIR="cardnews/${TODAY}_dark_auto"
if [ -d "$DIR" ] && [ -n "$(git status --porcelain -- "$DIR")" ]; then
  git add -- "$DIR"                      # 그날 폴더만 — git add -A 금지
  git commit -q -m "다크사이드: ${TODAY} 캐러셀" -- "$DIR" \
    && git push -q origin HEAD:main >> "$REPORT" 2>&1 \
    && echo "카드 push 완료 → Vercel 배포 대기" >> "$REPORT"
fi

python3 scripts/dark_publish.py --max 2 >> "$REPORT" 2>&1
python3 scripts/dark_measure.py >> "$REPORT" 2>&1
python3 scripts/dark_notify.py < "$REPORT"
{ date; cat "$REPORT"; echo; } >> "$LOG"
rm -f "$REPORT"
