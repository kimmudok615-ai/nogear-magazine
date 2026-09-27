#!/usr/bin/env python3
"""직접 게시용 키트 — 2026-09-27 Andy: «게시는 직접 할게».

그날 만든 편마다 [올릴 순서 · 카드 이미지 링크 · 복사해 붙일 캡션 · 릴스 파일 · 추천 시간]을
cardnews/<날짜>_dark_auto/POST_TODAY.md 한 장에 모은다. 텔레그램 보고에도 요약이 붙는다.
"""
import json
import os
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

ROOT = Path(__file__).resolve().parent.parent
BEST_TIMES = ["12:30", "20:30"]  # 점심·저녁 피크 — 한 편씩 나눠 올리기
BASE = os.getenv("DARK_PUBLIC_BASE", "https://nogear-magazine.vercel.app").rstrip("/")


def build(date, root=ROOT, base=BASE, suffix="dark_auto", times=None):
    times = times or BEST_TIMES
    day = root / "cardnews" / f"{date}_{suffix}"
    items = sorted(p for p in day.glob("*/series.json")) if day.exists() else []
    if not items:
        return None, "오늘 만든 편 없음"
    out = [f"# {date} 올릴 것 ({len(items)}편)", "",
           "순서대로 카드 이미지를 받아 캐러셀로 올리고, 캡션은 아래 상자를 그대로 복사한다.", ""]
    summary = []
    for i, sj in enumerate(items):
        d = sj.parent
        s = json.loads(sj.read_text(encoding="utf-8"))
        rel = d.relative_to(root)
        cards = sorted(p.name for p in d.glob("[0-9][0-9]_*.png"))
        cap = (d / "caption.txt").read_text(encoding="utf-8").strip() if (d / "caption.txt").exists() else ""
        when = times[i % len(times)]
        hook = cap.splitlines()[0] if cap else d.name
        out += [f"## {i + 1}. {hook}", f"- 추천 시간: **{when}** · 바이럴 점수: {s.get('viral_score', '—')}",
                f"- 카드 {len(cards)}장: " + " · ".join(f"[{n[:2]}]({base}/{rel}/{n})" for n in cards)]
        if (d / "reel.mp4").exists():
            out.append(f"- 릴스(선택, 8초): [{rel}/reel.mp4]({base}/{rel}/reel.mp4) — 인기 음원은 앱에서 붙인다")
        out += ["", "```", cap, "```", ""]
        summary.append(f"{i + 1}) {when} {hook[:40]} — 카드 {len(cards)}장")
    kit = day / "POST_TODAY.md"
    kit.write_text("\n".join(out), encoding="utf-8")
    return kit, "\n".join(summary)


if __name__ == "__main__":
    import datetime as dt
    import dark_accounts
    args = [x for x in sys.argv[1:] if not x.startswith("--account=")]
    acc = dark_accounts.get(next((x.split("=", 1)[1] for x in sys.argv[1:] if x.startswith("--account=")),
                                 dark_accounts.DEFAULT))
    date = args[0] if args else dt.date.today().strftime("%Y%m%d")
    kit, summary = build(date, suffix=acc.get("out_suffix", "dark_auto"), times=acc.get("post_times"))
    print(f"📦 오늘 올릴 것 → {kit.relative_to(ROOT) if kit else '없음'}\n{summary}")
