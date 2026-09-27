#!/usr/bin/env python3
"""여러 편을 한 번에 — 손으로(또는 다른 모델이) 쓴 캐러셀 묶음을 하루치와 같은 문으로 통과시켜 렌더한다.

입력: content/dark/examples/<날짜>.json  {"series": [ {id, tag, bg, fact_ids, slides, caption, thread?}, ... ]}
처리: 가드(dark_guard) → 바이럴 게이트(dark_viral, 목록형 표지 없으면 코드 보정) → [JEV 심사] → 렌더(스레드 캡처형)
출력: cardnews/<날짜>_<suffix>/<id>/  카드 PNG · caption.txt · series.json (+ 대안 표지)
      cardnews/<날짜>_<suffix>/EXAMPLES.md  편마다 표지·점수·보류 사유
      cardnews/<날짜>_<suffix>/contact_sheet.png  표지 한눈에
원장·게시 대기열은 건드리지 않는다(예시·기획용). 게시는 사람이 고른다.

사용: python3 scripts/dark_batch.py content/dark/examples/20260927.json [--suffix dark_examples] [--no-png] [--jev]
"""
import argparse
import html
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import dark_guard  # noqa: E402
import dark_viral  # noqa: E402
import generate_dark_cardnews as gen  # noqa: E402


def run(path, suffix="dark_examples", png=True, facts=None, reviewer=None, brand="neutral"):
    data = json.loads(Path(path).read_text(encoding="utf-8"))
    date = data.get("date") or Path(path).stem
    gen.set_brand(brand)
    facts = dark_guard.load_facts() if facts is None else facts
    out = gen.CARDNEWS / f"{date}_{suffix}"
    rows, pairs = [], []
    import dark_characters
    import dark_picker
    for s in data["series"]:
        axis = next((a for a in dark_picker.AXES if s["id"].startswith(a + "_")), None)
        s["bg"] = (dark_characters.pick(axis, s["id"]) if axis else None) or s.get("bg")  # 캐릭터 표지 우선
        ok, why = dark_guard.check(s, facts)
        vs, vok, vnotes = dark_viral.score(s)
        if ok and not vok and not dark_viral.has_list_hook(s["slides"][0].get("text")):
            s = dark_viral.force_list_hook(s)
            vs, vok, vnotes = dark_viral.score(s)
        row = {"id": s["id"], "guard": ok, "why": why, "viral": vs, "viral_ok": vok, "notes": vnotes,
               "hook": s["slides"][0]["text"].replace("*", "").replace("\n", " ")}
        if ok and vok and reviewer:
            import dark_jev
            block, lines, rank = dark_jev.advice(reviewer(s))
            s["jev"] = {"notes": lines, "rank": rank}
            row["jev"] = lines
            if block:
                ok, row["why"] = False, ["JEV·로컬 LLM 합의: 위험"]
        if ok and vok:
            s["viral_score"] = vs
            d = out / s["id"]
            d.mkdir(parents=True, exist_ok=True)
            pairs += gen.build_series(s, d, f"../../assets/{s['bg']}", manual=False)
            (d / "series.json").write_text(json.dumps(s, ensure_ascii=False, indent=2), encoding="utf-8")
            row["dir"] = str(d.relative_to(gen.ROOT))
        rows.append(row)
    qa = None
    if png and pairs:
        import dark_design_qa
        qa = dark_design_qa.Collector()  # 렌더 직후 측정 검사(넘침·겹침·글자 크기·붉은색 개수)
        gen.render(pairs, on_page=qa)
        for r in rows:
            if r.get("dir"):
                probs = {k: v for k, v in qa.report.items() if v and (gen.ROOT / r["dir"] / k).exists()}
                r["design"] = sum(len(v) for v in probs.values())
                sj = gen.ROOT / r["dir"] / "series.json"  # 보드가 읽도록 편 파일에도 남긴다
                sd = json.loads(sj.read_text(encoding="utf-8"))
                sd["design_qa"] = probs
                sj.write_text(json.dumps(sd, ensure_ascii=False, indent=2), encoding="utf-8")
    out.mkdir(parents=True, exist_ok=True)
    made = [r for r in rows if r.get("dir")]
    if png and made:
        sheet = out / "contact_sheet.html"
        tiles = "".join(f'<div class="t"><img src="{Path(r["dir"]).name}/00_cover.png"><b>{r["viral"]}</b></div>'
                        for r in made)
        sheet.write_text(f"""<!DOCTYPE html><html><head><meta charset="utf-8"><style>
body{{margin:0;width:2160px;background:#111;display:flex;flex-wrap:wrap;gap:12px;padding:12px}}
.t{{position:relative;width:420px}}.t img{{width:420px;display:block}}
.t b{{position:absolute;top:8px;right:10px;color:#C8141E;font:700 28px sans-serif}}</style></head>
<body>{tiles}</body></html>""", encoding="utf-8")
        gen.render([(sheet, out / "contact_sheet.png")], viewport_h=1350, full_page=True)
    lines = [f"# {date} 예시 {len(made)}/{len(rows)}편 — 가드·바이럴 게이트 통과분만 렌더", "",
             "| # | 표지 훅 | 바이럴 | 디자인 검사 | 결과 |", "|---|---|---|---|---|"]
    for i, r in enumerate(rows, 1):
        res = f"[카드]({Path(r['dir']).name}/00_cover.png)" if r.get("dir") else "보류: " + "; ".join(r["why"] or r["notes"])[:80]
        dq = "—" if "design" not in r else ("통과" if not r["design"] else f"문제 {r['design']}")
        lines.append(f"| {i} | {html.escape(r['hook'][:44])} | {r['viral']} | {dq} | {res} |")
    (out / "EXAMPLES.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    return rows, out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("path")
    ap.add_argument("--suffix", default="dark_examples")
    ap.add_argument("--no-png", action="store_true")
    ap.add_argument("--jev", action="store_true", help="노기어 판정 사슬로 심사(맥에서)")
    a = ap.parse_args()
    reviewer = None
    if a.jev:
        import dark_jev
        reviewer = dark_jev.review
    rows, out = run(a.path, a.suffix, not a.no_png, reviewer=reviewer)
    for r in rows:
        print(("✓" if r.get("dir") else "✗"), r["viral"], r["hook"][:50], "" if r.get("dir") else r["why"] or r["notes"])
    print(f"→ {out}")


if __name__ == "__main__":
    main()
