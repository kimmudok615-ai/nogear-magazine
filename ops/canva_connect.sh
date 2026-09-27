#!/usr/bin/env bash
# Canva 에셋 축적 연결 — 맥에서 한 번:  bash ~/nogear-magazine/ops/canva_connect.sh
# 준비: canva.com/developers → «통합 만들기» → 권한 asset:write · folder:read · folder:write
#       리디렉트 URL http://127.0.0.1:8765/callback 추가 → Client ID / Client secret 복사
set -uo pipefail
cd "$HOME/nogear-magazine" || exit 1
for K in CANVA_CLIENT_ID CANVA_CLIENT_SECRET; do
  read -r -s -p "  $K: " V; echo
  [ -n "$V" ] && security add-generic-password -U -s darkside -a "$K" -w "$V" && echo "  저장됨"
done
export CANVA_CLIENT_ID=$(security find-generic-password -s darkside -a CANVA_CLIENT_ID -w)
export CANVA_CLIENT_SECRET=$(security find-generic-password -s darkside -a CANVA_CLIENT_SECRET -w)
python3 scripts/dark_canva_sync.py --auth && python3 scripts/dark_canva_sync.py --max 200
