#!/usr/bin/env python3
"""다크사이콜로지 포맷 그대로 — @dark.psychologyyyy 상위 게시물(vidIQ 9/25·9/27 재확인) 형식을 규칙으로 옮겼다.

벤치마크 형식: 순수 검정 화면 · 스레드 글 캡처 한 장 · 작은 원형 프로필 + 아이디(굵게) + «2시간»(회색)
             · 굵은 제목 한 줄 · 번호 목록(1. 2. 3. …) · 흰 글씨만, 장식 없음 · 글 덩어리는 화면 세로 가운데.
캐러셀로 옮기는 법: 1장 = 제목 + 전체 번호 목록(벤치마크 한 장 그대로) → 2장부터 = 번호 하나씩 «답글»로 풀기
                  → 마지막 = 맺음 글 + 저장 유도. 모든 장이 같은 캡처 틀이라 «진짜 스레드 글»처럼 보인다.
AI 에게 레이아웃을 맡기지 않는다 — 크기·간격은 아래 숫자(벤치마크를 1080 폭으로 잰 값)에서 나온다.
"""
import html
import re

INK, TEXT, GRAY, BORDER = "#000000", "#F3F3F3", "#8E8E8E", "#2B2B2B"
W = 936          # 글 덩어리 폭 (좌우 72)

CSS = f"""
@import url('https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@400;500;700&display=swap');
*{{margin:0;padding:0;box-sizing:border-box}}
body{{width:1080px;height:1350px;background:{INK};color:{TEXT};font-family:'Noto Sans KR',sans-serif;
     display:flex;align-items:center;justify-content:center;word-break:keep-all;overflow:hidden}}
.post{{width:{W}px;max-height:1206px;overflow:hidden}}
.head{{display:flex;align-items:center;gap:20px;margin-bottom:36px}}
.av{{width:68px;height:68px;border-radius:50%;border:1.5px solid {BORDER};background:#0d0d0d;display:flex;
    align-items:center;justify-content:center;font-size:22px;font-weight:700;letter-spacing:1px;color:{TEXT};overflow:hidden}}
.av img{{width:100%;height:100%;object-fit:cover;filter:grayscale(1) contrast(1.2)}}
.who{{font-size:30px;font-weight:700;letter-spacing:-.2px}}
.ago{{font-size:28px;color:{GRAY};font-weight:400;margin-left:12px}}
.title{{font-size:42px;font-weight:700;line-height:1.5;letter-spacing:-.6px;margin-bottom:30px;white-space:pre-line}}
.list{{list-style:none}}
.list li{{font-size:36px;font-weight:400;line-height:1.55;margin-bottom:18px;letter-spacing:-.4px}}
.t{{font-size:40px;font-weight:400;line-height:1.6;letter-spacing:-.5px;white-space:pre-line}}
.t b,.title b,.list b{{font-weight:700}}
.num{{font-size:40px;font-weight:700;line-height:1.6;margin-bottom:6px}}
.src{{margin-top:26px;font-size:28px;color:{GRAY};line-height:1.5}}
.outro{{margin-top:30px;font-size:38px;font-weight:700;line-height:1.55;white-space:pre-line}}
"""

FIT_JS = """<script>
document.fonts.ready.then(()=>{ const p=document.querySelector('.post'); let k=1;
  while(p.scrollHeight > p.clientHeight + 1 && k > 0.72){ k -= 0.04; p.style.zoom = k; }
  document.body.dataset.fit='1'; });
</script>"""


def _t(x):
    """*강조* → 굵게 (벤치마크는 색 강조가 없다 — 흰 글씨, 굵기로만)."""
    return re.sub(r"\*(.+?)\*", r"<b>\1</b>", html.escape(str(x)))


def _p(x):
    return re.sub(r"\*", "", str(x)).replace("\n", " ").strip()


def points(series):
    """본문 장 → 목록 한 줄씩 (1장 전체 목록용)."""
    out = []
    for s in series["slides"][1:-1]:
        if s["kind"] == "stat":
            out.append(f"{s['num']} — {_p(s['label'])}")
        elif s["kind"] == "item":
            out.append(f"{_p(s['title'])}: {_p(s['text'])}")
        else:
            out.append(_p(s["text"]))
    return out


def _head(account, avatar=None):
    av = f'<img src="{html.escape(avatar)}">' if avatar else html.escape("".join(account.get("avatar", ("N", "G"))))
    return (f'<div class="head"><div class="av">{av}</div><div class="who">{html.escape(account["handle"])}'
            f'<span class="ago">2시간</span></div></div>')


def slide_html(series, s, idx, total, account, avatar=None):
    kind = s["kind"]
    if kind == "cover":
        lis = "".join(f"<li><b>{i}.</b> {html.escape(p)}</li>" for i, p in enumerate(points(series), 1))
        body = f'<div class="title">{_t(s["text"])}</div><ol class="list">{lis}</ol>'
    elif kind == "stat":
        body = (f'<div class="num">{idx}. {html.escape(s["num"])}</div><div class="t">{_t(s["label"])}</div>'
                f'<div class="src">출처: {html.escape(s["src"])}</div>')
    elif kind == "item":
        body = f'<div class="num">{idx}. {html.escape(s["title"])}</div><div class="t">{_t(s["text"])}</div>'
    elif kind == "line":
        body = f'<div class="t">{_t(s["text"])}</div>' + (f'<div class="src">{_t(s["sub"])}</div>' if s.get("sub") else "")
    else:
        body = (f'<div class="t"><b>{_t(s["text"])}</b></div><div class="outro">{html.escape(s["cta"])}</div>'
                f'<div class="src">{html.escape(account.get("motto", ""))}</div>')
    return (f'<!DOCTYPE html><html><head><meta charset="utf-8"><style>{CSS}</style></head>'
            f'<body class="k-{kind}"><div class="post">{_head(account, avatar)}{body}</div>{FIT_JS}</body></html>')
