#!/usr/bin/env python3
"""다크사이드 에셋 자동 정리 — 매일 러너 끝에 돈다. 사람이 폴더를 뒤질 필요가 없게.

cardnews/*_dark_auto/<편>/ 을 훑어 한 장짜리 색인을 만든다:
  content/dark/assets_index.json  (기계용)
  cardnews/DARK_INDEX.md          (사람용 — 날짜·축·표지 훅·상태·카드 수·릴스 유무·원문 링크)
상태는 원장(data/dark_ledger.jsonl)의 마지막 값: posted / queued / held …
"""
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import dark_ledger  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
INDEX_JSON = ROOT / "content" / "dark" / "assets_index.json"
INDEX_MD = ROOT / "cardnews" / "DARK_INDEX.md"


def scan(root=ROOT, ledger=dark_ledger.LEDGER):
    last = dark_ledger.latest(ledger)
    rows = []
    for d in sorted((root / "cardnews").glob("*_dark_auto/*/"), reverse=True):
        sj = d / "series.json"
        if not sj.exists():
            continue
        s = json.loads(sj.read_text(encoding="utf-8"))
        date = d.parent.name.split("_")[0]
        item = f"{date}_{d.name}"
        cover = next((x.get("text", "") for x in s.get("slides", []) if x.get("kind") == "cover"), "")
        src = next((c[4:].strip() for c in s.get("caption", []) if str(c).startswith("원문:")), "")
        rows.append({
            "date": date, "id": item, "axis": d.name.rsplit("_", 1)[0],
            "hook": re.sub(r"\s+", " ", re.sub(r"\*", "", cover)).strip(),
            "status": last.get(item, {}).get("state", "—"),
            "media_id": last.get(item, {}).get("media_id"),
            "cards": len(list(d.glob("[0-9][0-9]_*.png"))),
            "reel": (d / "reel.mp4").exists(),
            "dir": str(d.relative_to(root)), "source": src,
        })
    return rows


def write(rows, root=ROOT):
    j, m = root / "content" / "dark" / "assets_index.json", root / "cardnews" / "DARK_INDEX.md"
    j.parent.mkdir(parents=True, exist_ok=True)
    j.write_text(json.dumps(rows, ensure_ascii=False, indent=1), encoding="utf-8")
    lines = ["# 다크사이드 에셋 색인 (자동 생성 — 손으로 고치지 않는다)", "",
             f"총 {len(rows)}편 · 게시 {sum(r['status'] == 'posted' or r['status'] == 'measured' for r in rows)} · "
             f"대기 {sum(r['status'] == 'queued' for r in rows)}", "",
             "| 날짜 | 축 | 표지 훅 | 상태 | 카드 | 릴스 | 폴더 |", "|---|---|---|---|---|---|---|"]
    for r in rows:
        lines.append(f"| {r['date']} | {r['axis']} | {r['hook'][:40]} | {r['status']} | {r['cards']} | "
                     f"{'✓' if r['reel'] else ''} | [{r['id']}]({Path(r['dir']).relative_to('cardnews')}/) |")
    m.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return j, m


if __name__ == "__main__":
    rows = scan()
    write(rows)
    print(f"에셋 색인 {len(rows)}편 → cardnews/DARK_INDEX.md")
