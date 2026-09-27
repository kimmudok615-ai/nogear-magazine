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

# 모드: daily(기본, 08:30) = 소재 보충 → 2편 생성 → 게시 / publish = 대기열 게시만(수동 실행용)
MODE="${1:-daily}"
if [ "$MODE" = "daily" ]; then
python3 scripts/dark_research.py --days 60 --per 8 >> "$REPORT" 2>&1 || echo "연구 소재 보충 실패 — 기존 원장으로 진행" >> "$REPORT"
python3 scripts/dark_trends.py >> "$REPORT" 2>&1 || echo "화제 수집 실패 — 화제 없이 진행" >> "$REPORT"
for RDATA in content/dark/research.json content/dark/trends.json; do
  if [ -f "$RDATA" ] && [ -n "$(git status --porcelain -- "$RDATA")" ]; then
    git add -- "$RDATA" && git commit -q -m "다크사이드: 소재·화제 ${TODAY}" -- "$RDATA"
  fi
done
# 계정마다(config/accounts.json 의 enabled) — 2026-09-27 계정 여러 개
for ACC in $(python3 scripts/dark_accounts.py --enabled); do
  SUFFIX=$(python3 -c "import sys;sys.path.insert(0,'scripts');import dark_accounts as a;print(a.get('$ACC').get('out_suffix','dark_auto'))")
  COUNT=$(python3 -c "import sys;sys.path.insert(0,'scripts');import dark_accounts as a;print(a.get('$ACC').get('count',2))")
  echo "── @$ACC" >> "$REPORT"
  python3 scripts/dark_daily.py --account "$ACC" --count "$COUNT" >> "$REPORT" 2>&1
  python3 scripts/dark_kit.py "$TODAY" --account="$ACC" >> "$REPORT" 2>&1   # 직접 게시용 키트(POST_TODAY.md)

  DIR="cardnews/${TODAY}_${SUFFIX}"
  if [ -d "$DIR" ] && [ -n "$(git status --porcelain -- "$DIR")" ]; then
    git add -- "$DIR"                      # 그날 폴더만 — git add -A 금지
    git commit -q -m "다크사이드 @$ACC: ${TODAY} 캐러셀" -- "$DIR" \
      && git push -q origin HEAD:main >> "$REPORT" 2>&1 \
      && echo "카드 push 완료 → Vercel 배포 대기" >> "$REPORT"
  fi
done

fi  # MODE=daily

# 게시는 사람이 직접(2026-09-27). 자동 게시는 DARK_AUTO_PUBLISH=1 일 때만.
if [ "${DARK_AUTO_PUBLISH:-0}" = "1" ]; then
  python3 scripts/dark_publish.py --max 2 >> "$REPORT" 2>&1
else
  echo "자동 게시 꺼짐 — POST_TODAY.md 보고 직접 올리기" >> "$REPORT"
fi
python3 scripts/dark_measure.py >> "$REPORT" 2>&1   # 직접 게시 매칭 → 48시간 측정
python3 scripts/dark_jev_audit.py >> "$REPORT" 2>&1 # JEV 심사 ↔ 실제 저장률 검증
python3 scripts/dark_assets.py >> "$REPORT" 2>&1   # 에셋 색인 자동 정리
python3 scripts/tower.py >> "$REPORT" 2>&1         # 컨트롤타워 tower/index.html
python3 scripts/dark_notify.py < "$REPORT"
{ date; cat "$REPORT"; echo; } >> "$LOG"
# 원격에서도 결과를 볼 수 있게 하루 보고를 저장소에 남긴다(비밀값 없음, 긴 문자열 가림)
mkdir -p ops/status
{ date; echo "mode=$MODE"; sed -E 's/[A-Za-z0-9_-]{40,}/[가림]/g' "$REPORT"; } > "ops/status/last_run_${MODE}.txt"
python3 scripts/tower.py >/dev/null 2>&1          # 방금 쓴 상태 파일까지 반영
git add -- "ops/status/last_run_${MODE}.txt" cardnews/DARK_INDEX.md content/dark/assets_index.json content/dark/jev_audit.json tower/index.html tower/status.json 2>/dev/null
git commit -q -m "상태: ${MODE} ${TODAY}" -- "ops/status/last_run_${MODE}.txt" cardnews/DARK_INDEX.md content/dark/assets_index.json content/dark/jev_audit.json tower/index.html tower/status.json \
  && git push -q origin HEAD:main
rm -f "$REPORT"
