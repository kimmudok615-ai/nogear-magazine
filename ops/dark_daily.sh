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

# 인스타 자격증명은 맥 키체인에서 (파일·plist 에 평문으로 두지 않는다). 설치: ops/install_mac.sh
for K in DARK_IG_TOKEN DARK_IG_USER_ID; do
  if [ -z "${!K:-}" ] && command -v security >/dev/null; then
    V=$(security find-generic-password -s darkside -a "$K" -w 2>/dev/null) && export "$K=$V"
  fi
done

if [ "$(git rev-parse --abbrev-ref HEAD)" != "main" ]; then
  echo "main 브랜치가 아니라 중단 (다른 작업 브랜치를 main 으로 밀지 않는다)" | python3 scripts/dark_notify.py
  exit 1
fi
git pull -q --ff-only origin main || echo "pull 실패 — 로컬 그대로 진행" >> "$REPORT"

# 모드: 기본(아침) = 소재 보충 → 2편 생성 → 1편 게시 / publish(저녁) = 남은 1편 게시만
# 하루 2편을 한꺼번에 올리지 않고 시간을 나눈다(아침·저녁 두 번 노출).
MODE="${1:-$([ "$(date +%H)" -ge 12 ] && echo publish || echo daily)}"  # 인자 없으면 시각으로
if [ "$MODE" = "daily" ]; then
python3 scripts/dark_research.py --days 60 --per 8 >> "$REPORT" 2>&1 || echo "연구 소재 보충 실패 — 기존 원장으로 진행" >> "$REPORT"
RDATA=content/dark/research.json
if [ -f "$RDATA" ] && [ -n "$(git status --porcelain -- "$RDATA")" ]; then
  git add -- "$RDATA" && git commit -q -m "다크사이드: 연구 소재 ${TODAY}" -- "$RDATA"
fi
python3 scripts/dark_daily.py --count 2 >> "$REPORT" 2>&1

DIR="cardnews/${TODAY}_dark_auto"
if [ -d "$DIR" ] && [ -n "$(git status --porcelain -- "$DIR")" ]; then
  git add -- "$DIR"                      # 그날 폴더만 — git add -A 금지
  git commit -q -m "다크사이드: ${TODAY} 캐러셀" -- "$DIR" \
    && git push -q origin HEAD:main >> "$REPORT" 2>&1 \
    && echo "카드 push 완료 → Vercel 배포 대기" >> "$REPORT"
fi

fi  # MODE=daily

python3 scripts/dark_publish.py --max 1 >> "$REPORT" 2>&1
python3 scripts/dark_measure.py >> "$REPORT" 2>&1
python3 scripts/dark_notify.py < "$REPORT"
{ date; cat "$REPORT"; echo; } >> "$LOG"
# 원격에서도 결과를 볼 수 있게 하루 보고를 저장소에 남긴다(비밀값 없음, 긴 문자열 가림)
mkdir -p ops/status
{ date; echo "mode=$MODE"; sed -E 's/[A-Za-z0-9_-]{40,}/[가림]/g' "$REPORT"; } > "ops/status/last_run_${MODE}.txt"
git add -- "ops/status/last_run_${MODE}.txt" && git commit -q -m "상태: ${MODE} ${TODAY}" -- "ops/status/last_run_${MODE}.txt" \
  && git push -q origin HEAD:main
rm -f "$REPORT"
