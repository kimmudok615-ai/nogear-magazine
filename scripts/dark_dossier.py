#!/usr/bin/env python3
"""Evidence Noir(증거 누아르) 카드 — design/PHILOSOPHY.md · design/DESIGN_RULES.md 를 코드로.

AI 에게 레이아웃을 시키지 않는다. 모든 위치·크기·색은 DESIGN_RULES 의 숫자에서 나온다.
글자가 상자를 넘치면 브라우저 안에서 규칙이 정한 만큼만 줄인다(fit) — 그래도 넘치면 QA 가 잡는다.
"""
import html
import re
import zlib
from pathlib import Path

FONTS = (Path(__file__).resolve().parent.parent / "design" / "fonts").as_uri()
INK, PAPER, DUST, LINE, RED = "#0B0B0A", "#E9E4DA", "#8C867B", "#3A3833", "#C8141E"

CSS = f"""
@import url('https://fonts.googleapis.com/css2?family=Noto+Serif+KR:wght@400;700;900&display=swap');
@font-face{{font-family:'Plex';src:url('{FONTS}/IBMPlexMono-Regular.ttf')}}
@font-face{{font-family:'Plex';font-weight:700;src:url('{FONTS}/IBMPlexMono-Bold.ttf')}}
@font-face{{font-family:'Gloock';src:url('{FONTS}/Gloock-Regular.ttf')}}
*{{margin:0;padding:0;box-sizing:border-box}}
body{{width:1080px;height:1350px;background:{INK};color:{PAPER};font-family:'Noto Serif KR',serif;
     position:relative;overflow:hidden;word-break:keep-all;font-variant-numeric:lining-nums}}
.mono{{font-family:'Plex',monospace;font-size:19px;letter-spacing:4px;color:{DUST};text-transform:uppercase}}
.rail{{position:absolute;left:72px;right:72px;display:flex;justify-content:space-between}}
.rail.top{{top:64px}} .rail.bot{{top:1266px}}
.hair{{position:absolute;left:72px;right:72px;height:1px;background:{LINE}}}
.reg{{position:absolute;width:14px;height:14px}}
.reg:before,.reg:after{{content:'';position:absolute;background:{LINE}}}
.reg:before{{left:6px;top:0;width:1px;height:14px}} .reg:after{{top:6px;left:0;height:1px;width:14px}}
em{{font-style:normal;color:{RED}}}
.red{{color:{RED}}}
/* 표지 */
.photo{{position:absolute;left:540px;top:152px;width:468px;height:600px;border:1px solid {LINE};overflow:hidden;background:#141412}}
.photo .img{{position:absolute;inset:0;background-size:cover;background-position:62% 30%;
            filter:grayscale(1) contrast(1.35) brightness(.78)}}
.photo .dots{{position:absolute;inset:0;background-image:radial-gradient({INK} 1.1px,transparent 1.3px);background-size:5px 5px;opacity:.55;mix-blend-mode:multiply}}
.photo.char .img{{filter:contrast(1.12) brightness(.92)}}
.photo.char .dots{{opacity:.25}}
.cap{{position:absolute;left:540px;top:764px;width:468px;display:flex;justify-content:space-between}}
.stamp{{position:absolute;left:500px;top:128px;transform:rotate(-7deg);border:2px solid {RED};color:{RED};
        padding:8px 14px 6px;font-family:'Plex';font-weight:700;font-size:20px;letter-spacing:6px;background:{INK}}}
.meta{{position:absolute;left:72px;top:152px;width:420px}}
.meta div{{margin-bottom:14px}}
.meta .k{{color:{LINE}}}
.hookbox{{position:absolute;left:72px;right:72px;top:824px;height:300px;display:flex;flex-direction:column;justify-content:flex-end}}
.hook{{font-weight:900;font-size:92px;line-height:1.18;letter-spacing:-2.5px;white-space:pre-line}}
.bars{{position:absolute;left:72px;top:1160px;display:flex;gap:12px}}
.bars i{{display:block;height:22px;background:{PAPER};opacity:.92}}
/* 수치 */
.tag{{position:absolute;left:72px;top:176px}}
.numbox{{position:absolute;left:72px;right:72px;top:236px;height:340px;display:flex;align-items:flex-end}}
.num{{font-family:'Gloock','Noto Serif KR',serif;font-size:300px;line-height:.9;letter-spacing:-6px;white-space:nowrap;color:{PAPER}}}
.ruler{{position:absolute;left:72px;right:72px;top:616px;height:28px}}
.ruler i{{position:absolute;bottom:0;width:1px;background:{LINE}}}
.ruler b{{position:absolute;bottom:-6px;width:3px;height:40px;background:{RED}}}
.scale{{position:absolute;left:72px;right:72px;top:652px;display:flex;justify-content:space-between}}
.lab{{position:absolute;left:72px;right:72px;top:740px;font-weight:700;font-size:62px;line-height:1.32;letter-spacing:-1.2px;white-space:pre-line}}
.foot{{position:absolute;left:72px;right:72px;top:1196px}}
/* 목록 */
.bigno{{position:absolute;right:56px;top:96px;font-family:'Gloock';font-size:420px;line-height:1;color:transparent;
        -webkit-text-stroke:1.5px {LINE}}}
.ititle{{position:absolute;left:72px;top:520px;font-family:'Plex';font-weight:700;font-size:22px;letter-spacing:6px;color:{RED}}}
.body{{position:absolute;left:72px;right:72px;top:580px;font-weight:700;font-size:62px;line-height:1.36;letter-spacing:-1.2px;white-space:pre-line}}
.sub{{position:absolute;left:72px;right:144px;font-size:30px;line-height:1.6;color:{DUST};white-space:pre-line}}
/* 끝 */
.endt{{position:absolute;left:72px;right:72px;top:420px;font-weight:900;font-size:80px;line-height:1.26;letter-spacing:-2px;white-space:pre-line}}
.cta{{position:absolute;left:72px;top:860px;display:flex;align-items:center;gap:18px;font-family:'Noto Serif KR';font-weight:700;font-size:34px}}
.cta svg{{width:34px;height:34px}}
.eof{{position:absolute;left:72px;top:1196px}}
"""

FIT_JS = """<script>
function fit(sel, min, box){ for(const el of document.querySelectorAll(sel)){
  const b = box ? el.closest(box) : el.parentElement; let s = parseFloat(getComputedStyle(el).fontSize);
  while((el.scrollWidth > b.clientWidth + 1 || el.scrollHeight > b.clientHeight + 1) && s > min){ s -= 4; el.style.fontSize = s + 'px'; } } }
document.fonts.ready.then(()=>{ fit('.hook',60,'.hookbox'); fit('.num',140,'.numbox'); document.body.dataset.fit='1'; });
</script>"""


def fmt(t):
    return re.sub(r"\*(.+?)\*", r"<em>\1</em>", html.escape(str(t)))


def _plain(t):
    return re.sub(r"\*", "", str(t))


def case_no(series):
    return f"{zlib.crc32(str(series.get('id') or series.get('tag', '')).encode()) % 10000:04d}"


def _frame(series, idx, total, account, left, right):
    regs = "".join(f'<i class="reg" style="{p}"></i>' for p in
                   ("left:28px;top:28px", "right:28px;top:28px", "left:28px;bottom:28px", "right:28px;bottom:28px"))
    return (f'{regs}<div class="rail top mono"><span>CASE N°{case_no(series)} — {html.escape(account["tag"])}</span>'
            f'<span>{left}</span></div><div class="hair" style="top:104px"></div>'
            f'<div class="hair" style="top:1246px"></div>'
            f'<div class="rail bot mono"><span>@{html.escape(account["handle"])}</span><span>{right}</span></div>')


def _bars(text):
    """가림 막대 — 폭은 주장 길이에서 잰다(무작위 장식 아님)."""
    n = len(_plain(text).replace("\n", ""))
    w = [min(360, 96 + n * 7), min(180, 48 + n * 3), min(300, 80 + n * 5)]
    return '<div class="bars">' + "".join(f'<i style="width:{x}px"></i>' for x in w) + "</div>"


def _ruler(num):
    ticks = "".join(f'<i style="left:{i * 936 / 24:.1f}px;height:{28 if i % 6 == 0 else 16 if i % 2 == 0 else 8}px"></i>'
                    for i in range(25))
    m = re.fullmatch(r"\s*([\d.]+)\s*%\s*", _plain(num))
    mark = f'<b style="left:{min(100.0, float(m.group(1))) * 9.36 - 1:.1f}px"></b>' if m else ""
    scale = '<div class="scale mono"><span>0</span><span>25</span><span>50</span><span>75</span><span>100</span></div>' if m else ""
    return f'<div class="ruler">{ticks}{mark}</div>{scale}'


def slide_html(series, s, idx, total, img_rel, account):
    kind = s["kind"]
    sheet = f"SHEET {idx + 1:02d} / {total:02d}"
    if kind == "cover":
        char = "characters/" in str(img_rel)
        body = (f'<div class="meta mono"><div><span class="k">FILE</span> N°{case_no(series)}</div>'
                f'<div><span class="k">CLASS</span> EYES ONLY</div><div><span class="k">SUBJECT</span> {html.escape(s.get("kicker") or "UNKNOWN")}</div></div>'
                f'<div class="photo{" char" if char else ""}"><div class="img" style="background-image:url(\'{img_rel}\')"></div><div class="dots"></div></div>'
                f'<div class="stamp">기밀 · CLASSIFIED</div>'
                f'<div class="cap mono"><span>EXHIBIT A</span><span>FIG. 1</span></div>'
                f'<div class="hookbox"><div class="hook">{fmt(s["text"])}</div></div>{_bars(s["text"])}')
        frame = _frame(series, idx, total, account, sheet, "SWIPE ——→")
    elif kind == "stat":
        body = (f'<div class="tag mono red">DECLASSIFIED · 기밀 해제 수치</div>'
                f'<div class="numbox"><div class="num">{html.escape(s["num"])}</div></div>{_ruler(s["num"])}'
                f'<div class="lab">{fmt(s["label"])}</div>'
                f'<div class="foot mono">[{idx}] 출처 — {html.escape(s["src"])}</div>')
        frame = _frame(series, idx, total, account, sheet, "CONTINUED ——→")
    elif kind == "item":
        no = str(s.get("no", idx)).lstrip("0") or str(idx)
        body = (f'<div class="bigno">{html.escape(no)}</div><div class="ititle">{html.escape(no.zfill(2))} — {html.escape(s["title"])}</div>'
                f'<div class="body">{fmt(s["text"])}</div>')
        frame = _frame(series, idx, total, account, sheet, "CONTINUED ——→")
    elif kind == "line":
        body = (f'<div class="body" style="top:460px">{fmt(s["text"])}</div>'
                + (f'<div class="sub" style="top:820px">{fmt(s["sub"])}</div>' if s.get("sub") else ""))
        frame = _frame(series, idx, total, account, sheet, "CONTINUED ——→")
    else:
        save = f'<svg viewBox="0 0 24 24" fill="none" stroke="{RED}" stroke-width="2"><path d="M6 3h12v18l-6-4-6 4z"/></svg>'
        body = (f'<div class="endt">{fmt(s["text"])}</div><div class="cta">{save}<span>{html.escape(s["cta"])}</span></div>'
                f'<div class="eof mono">END OF FILE — CASE N°{case_no(series)} · {html.escape(account.get("motto", ""))}</div>')
        frame = _frame(series, idx, total, account, sheet, "")
    return (f'<!DOCTYPE html><html><head><meta charset="utf-8"><style>{CSS}</style></head>'
            f'<body class="k-{kind}">{frame}{body}{FIT_JS}</body></html>')
