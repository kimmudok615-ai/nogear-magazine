#!/usr/bin/env python3
"""캐릭터 표지 이미지 — design/characters.json (2026-09-27 Andy «사람이나 캐릭터가 있어서 그에 맞는 이미지도»).

축(axis)마다 캐릭터 이미지를 고른다. 파일이 아직 없으면 None → 기존 스톡 배경으로 돌아간다(안 멈춘다).
  python3 scripts/dark_characters.py --fetch   맥에서 CDN 원본을 cardnews/assets/characters/ 로 받는다
                                               (클라우드 세션은 CDN 이 막혀 있다 — 받는 건 맥 러너 몫)
새 이미지는 Higgsfield 로 만들고 manifest 에 job·url 을 적는다. 크레딧 소비라 사람이 요청할 때만.
"""
import json
import sys
import urllib.request
import zlib
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MANIFEST = ROOT / "design" / "characters.json"
DIR = ROOT / "cardnews" / "assets" / "characters"


def manifest(path=MANIFEST):
    try:
        return json.loads(path.read_text(encoding="utf-8")).get("images", {})
    except Exception:  # noqa: BLE001
        return {}


def pick(axis, key, d=DIR, path=MANIFEST):
    """→ assets 기준 상대경로('characters/drugs_01.png') 또는 None. 같은 key 는 늘 같은 그림."""
    have = sorted(n for n, v in manifest(path).items() if v.get("axis") == axis and (d / f"{n}.png").exists())
    if not have:
        return None
    return f"characters/{have[zlib.crc32(str(key).encode()) % len(have)]}.png"


def fetch(d=DIR, path=MANIFEST, get=None):
    get = get or (lambda u: urllib.request.urlopen(urllib.request.Request(u, headers={"User-Agent": "ngr"}), timeout=60).read())  # noqa: S310
    d.mkdir(parents=True, exist_ok=True)
    got, fail = [], []
    for n, v in manifest(path).items():
        f = d / f"{n}.png"
        if f.exists():
            continue
        try:
            f.write_bytes(get(v["url"]))
            got.append(n)
        except Exception as e:  # noqa: BLE001
            fail.append(f"{n}: {type(e).__name__}")
    return got, fail


if __name__ == "__main__":
    if "--fetch" in sys.argv:
        got, fail = fetch()
        print(f"🎭 캐릭터 이미지 새로 받음 {len(got)}장" + (f" · 실패 {len(fail)}: {', '.join(fail)}" if fail else ""))
    else:
        print(json.dumps(manifest(), ensure_ascii=False, indent=1))
