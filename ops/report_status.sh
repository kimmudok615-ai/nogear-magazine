#!/usr/bin/env bash
# 맥 상태를 저장소에 올린다 → 원격 Claude 가 git 으로 읽는다(복사·붙여넣기 불필요).
# 비밀값은 싣지 않는다: --check 는 ✅/❌ 만, 시험 실행은 소재 제목·판정만 찍는다.
# 사용: bash ~/nogear-magazine/ops/report_status.sh
set -uo pipefail
cd "$(dirname "$0")/.."
OUT=ops/status/mac_status.txt; mkdir -p ops/status
{
  echo "# $(date '+%Y-%m-%d %H:%M:%S') $(hostname -s)"
  echo; bash ops/install_mac.sh --check 2>&1
  echo; echo "── 시험 실행 (임시 원장, 게시 없음)"
  python3 scripts/dark_daily.py --count 1 --test --no-reels 2>&1 | tail -8
  echo; echo "── 최근 하루치 로그"
  tail -20 data/dark_daily.log 2>/dev/null || echo "(아직 없음)"
} > "$OUT"
# 토큰처럼 보이는 긴 문자열은 가린다 (혹시 모를 유출 방지)
sed -i '' -E 's/[A-Za-z0-9_-]{40,}/[가림]/g' "$OUT" 2>/dev/null || sed -i -E 's/[A-Za-z0-9_-]{40,}/[가림]/g' "$OUT"
cat "$OUT"
git add -- "$OUT" && git commit -q -m "상태: 맥 점검 $(date +%m%d-%H%M)" -- "$OUT" && git push -q origin HEAD:main && echo "✅ 올림 — Claude 에게 «올렸어» 라고 하면 됩니다"
