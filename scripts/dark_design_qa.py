#!/usr/bin/env python3
"""디자인 자동 검사 — design/DESIGN_RULES.md «자동 검사» 4항목을 렌더된 페이지에서 잰다(AI 판단 아님, 측정).

1) 글자가 여백 상자(64~1016 × 56~1294) 밖으로 나감  2) 글자 요소끼리 겹침
3) 글자 16px 미만                                   4) 붉은 글자 요소 3개 이상(판정은 드물게)
generate_dark_cardnews.render(..., on_page=Collector()) 로 렌더 직후 같은 페이지에서 잰다.
"""
from pathlib import Path

BOX = (64, 56, 1016, 1294)
JS = """() => {
  const RED = 'rgb(200, 20, 30)';
  const els = [...document.querySelectorAll('body *')].filter(e => {
    if (['SCRIPT','STYLE','SVG','PATH','I','B'].includes(e.tagName.toUpperCase())) return false;
    const own = [...e.childNodes].some(n => n.nodeType === 3 && n.textContent.trim());
    const cs = getComputedStyle(e);
    if (cs.display === 'inline' && e.parentElement && e.parentElement !== document.body) return false; // 문장 안 강조는 부모가 대표
    return own && cs.visibility !== 'hidden' && cs.color !== 'rgba(0, 0, 0, 0)' && !e.closest('.bigno');
  });
  return els.map(e => { const r = e.getBoundingClientRect(); const cs = getComputedStyle(e);
    return {t: e.textContent.trim().slice(0, 24), x0: r.left, y0: r.top, x1: r.right, y1: r.bottom,
            fs: parseFloat(cs.fontSize), red: cs.color === RED, cls: e.className, parent: e.parentElement === null ? '' : e.parentElement.className}; });
}"""


def check(boxes, box=BOX):
    bad = []
    for b in boxes:
        if b["x0"] < box[0] - 1 or b["y0"] < box[1] - 1 or b["x1"] > box[2] + 1 or b["y1"] > box[3] + 1:
            bad.append(f"넘침: «{b['t']}»")
        if b["fs"] < 16:
            bad.append(f"글자 작음 {b['fs']:.0f}px: «{b['t']}»")
    for i, a in enumerate(boxes):
        for c in boxes[i + 1:]:
            ix = min(a["x1"], c["x1"]) - max(a["x0"], c["x0"])
            iy = min(a["y1"], c["y1"]) - max(a["y0"], c["y0"])
            nested = (a["x0"] <= c["x0"] and a["x1"] >= c["x1"] and a["y0"] <= c["y0"] and a["y1"] >= c["y1"]) or \
                     (c["x0"] <= a["x0"] and c["x1"] >= a["x1"] and c["y0"] <= a["y0"] and c["y1"] >= a["y1"])
            if ix > 2 and iy > 2 and not nested:
                bad.append(f"겹침: «{a['t']}» × «{c['t']}»")
    if sum(1 for b in boxes if b["red"]) >= 3:
        bad.append("붉은 글자 3곳 이상")
    return bad


class Collector:
    """render(on_page=...) 에 넘기는 수집기. .report = {파일명: [문제...]}"""

    def __init__(self):
        self.report = {}

    def __call__(self, page, src):
        try:
            self.report[Path(src).name] = check(page.evaluate(JS))
        except Exception as e:  # noqa: BLE001 — 검사 실패는 문제로 기록
            self.report[Path(src).name] = [f"검사 실패 {type(e).__name__}"]

    def problems(self, prefix=""):
        return {k: v for k, v in self.report.items() if v and k.startswith(prefix)}
