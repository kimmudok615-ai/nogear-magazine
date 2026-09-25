#!/usr/bin/env bash
# 다크사이드 계정 — 맥 설치 한 번에. 맥에서:  bash ~/nogear-magazine/ops/install_mac.sh
#   --check   무엇이 준비됐고 무엇이 빠졌는지만 본다 (아무것도 바꾸지 않음)
# 하는 일: 파이썬 패키지 · 키체인에 인스타 토큰 저장(입력 받음) · launchd 등록(매일 08:30) · 시험 실행(임시 원장, 게시·push 없음)
set -uo pipefail
REPO="$HOME/nogear-magazine"; cd "$REPO" || { echo "✗ $REPO 없음 — git clone 먼저"; exit 1; }
PLIST="$HOME/Library/LaunchAgents/com.darkside.daily.plist"
ok(){ echo "  ✅ $1"; }; no(){ echo "  ❌ $1"; MISSING=1; }
MISSING=0

check() {
  echo "── 준비 상태"
  [ "$(git rev-parse --abbrev-ref HEAD)" = "main" ] && ok "main 브랜치" || no "main 브랜치 아님 (git checkout main)"
  python3 -c "import playwright" 2>/dev/null && ok "playwright" || no "playwright (pip)"
  python3 -c "import imageio_ffmpeg" 2>/dev/null && ok "imageio-ffmpeg (릴스)" || no "imageio-ffmpeg (pip)"
  [ -x "$HOME/.local/bin/aside" ] && ok "aside (GPT Luna 카피)" || no "aside 없음 — 로컬 LLM 만 사용"
  curl -s -m 3 http://localhost:11434/api/tags >/dev/null && ok "ollama 로컬 LLM" || no "ollama 꺼짐"
  for K in DARK_IG_TOKEN DARK_IG_USER_ID; do
    security find-generic-password -s darkside -a "$K" -w >/dev/null 2>&1 && ok "키체인 $K" || no "키체인 $K (게시 안 됨)"
  done
  [ -f "$PLIST" ] && launchctl list | grep -q com.darkside.daily && ok "launchd 등록" || no "launchd 미등록"
}

if [ "${1:-}" = "--check" ]; then check; exit $MISSING; fi

echo "── 1/4 파이썬 패키지"
# 맥 파이썬이 --user 설치를 막으면(PEP 668) --break-system-packages 로 한 번 더 (2026-09-25 실측)
python3 -m pip install -q --user playwright imageio-ffmpeg 2>/dev/null \
  || python3 -m pip install -q --break-system-packages playwright imageio-ffmpeg \
  || echo "  ❌ pip 설치 실패 — 위 에러를 확인"
python3 -m playwright install chromium >/dev/null 2>&1 || echo "  ❌ 크로미움 설치 실패"
echo "── 2/4 인스타 자격증명 → 키체인 (비우고 엔터 = 건너뜀, 나중에 다시 실행)"
for K in DARK_IG_TOKEN DARK_IG_USER_ID; do
  read -r -s -p "  $K: " V; echo
  [ -n "$V" ] && security add-generic-password -U -s darkside -a "$K" -w "$V" && echo "  저장됨"
done
echo "── 3/4 launchd 등록 (매일 08:30)"
git checkout -q main && git pull -q --ff-only origin main
chmod +x ops/dark_daily.sh
cp ops/com.darkside.daily.plist "$PLIST"
launchctl unload "$PLIST" 2>/dev/null; launchctl load "$PLIST"
echo "── 4/4 시험 실행 (카드 1편 생성만, 게시·push 없음)"
python3 scripts/dark_daily.py --count 1 --test && echo "  ✅ 생성 OK (카드·릴스 경로는 위 «시험 모드» 폴더)" || echo "  ⚠️ 생성 실패 — 위 사유 확인"
check
