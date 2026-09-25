#!/usr/bin/env bash
# Higgsfield 결과물을 이 폴더로 받는다(맥에서 실행). 받은 뒤:
#   python3 scripts/generate_dark_cardnews.py  → 커버가 Higgsfield 이미지로 교체된다.
set -euo pipefail
cd "$(dirname "$0")"
python3 - <<'PY'
import json, urllib.request
m = json.load(open("manifest.json"))
for name, v in {**m["images"], **m["videos"]}.items():
    f = v.get("file")
    if not f:
        print(f"skip {name} (URL 미기록)"); continue
    urllib.request.urlretrieve(m["cdn"] + f, name); print("ok", name)
PY
