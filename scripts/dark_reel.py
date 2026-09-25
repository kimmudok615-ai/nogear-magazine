#!/usr/bin/env python3
"""다크사이드 계정 릴스 — 스레드 글 캡처형 8초 정지 릴스.

벤치마크(2026-09-25, vidIQ): @dark.psychologyyyy 의 상위 릴스는 캐러셀이 아니라
«검은 배경 + 스레드 글 캡처 + 번호 목록 5~7줄» 8초 정지 영상이었다(6.8만~11.4만 회).
같은 시리즈 JSON 에서 뽑으므로 LLM 추가 호출이 없다. 가드도 같은 글을 본다.

series["thread"] = {"title": "...", "items": ["...", ...], "outro": "..."} 가 있으면 그걸 쓰고,
없으면 슬라이드에서 뽑는다.
ffmpeg 는 imageio-ffmpeg 에 들어 있는 것을 쓴다(pip 하나, 맥·리눅스 공통, 0원).
음악은 API 로 못 붙인다(인스타 라이선스 음원은 앱에서만) — DARK_REEL_AUDIO 에 저작권 없는 파일이 있으면 붙인다.
"""
import html
import os
import re
import subprocess
from pathlib import Path

REEL_SECONDS = 8


def _plain(t):
    return re.sub(r"\*(.+?)\*", r"\1", str(t)).replace("\n", " ").strip()


def thread_of(series):
    """→ {"title", "items", "outro"}"""
    if series.get("thread"):
        return series["thread"]
    slides = series["slides"]
    items = []
    for s in slides[1:-1]:
        if s["kind"] == "stat":
            items.append(f"{s['num']} — {_plain(str(s['label']).split(chr(10))[0])}")
        elif s["kind"] == "item":
            items.append(f"{_plain(s['title'])}: {_plain(s['text'])}")
        else:
            items.append(_plain(s["text"]))
    return {"title": _plain(slides[0]["text"]), "items": items[:7], "outro": _plain(slides[-1]["text"])}


CSS = """
@import url('https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@400;700&display=swap');
*{margin:0;padding:0;box-sizing:border-box}
body{width:1080px;height:1920px;background:#000;color:#f3f3f3;font-family:'Noto Sans KR',sans-serif;
     display:flex;align-items:center;justify-content:center;word-break:keep-all}
.post{width:920px}
.head{display:flex;align-items:center;gap:24px;margin-bottom:40px}
.av{width:84px;height:84px;border-radius:50%;background:#111;border:2px solid #333;display:flex;
    align-items:center;justify-content:center;font-size:30px;font-weight:700;color:#c8141e}
.who{font-size:34px;font-weight:700}.ago{font-size:30px;color:#777;margin-left:12px;font-weight:400}
.title{font-size:44px;font-weight:700;line-height:1.5;margin-bottom:36px}
ol{list-style:none;counter-reset:n}
li{counter-increment:n;font-size:38px;line-height:1.6;margin-bottom:22px;padding-left:64px;position:relative}
li::before{content:counter(n) ".";position:absolute;left:0;color:#c8141e;font-weight:700}
.outro{margin-top:40px;font-size:40px;font-weight:700;line-height:1.5;color:#fff}
"""


def card_html(series, account):
    t = thread_of(series)
    av = "".join(account.get("avatar", ("D", "S")))
    lis = "".join(f"<li>{html.escape(i)}</li>" for i in t["items"])
    return f"""<!DOCTYPE html><html><head><meta charset="utf-8"><style>{CSS}</style></head><body>
<div class="post"><div class="head"><div class="av">{html.escape(av)}</div>
<div class="who">{html.escape(account['handle'])}<span class="ago">2시간</span></div></div>
<div class="title">{html.escape(t['title'])}</div><ol>{lis}</ol>
<div class="outro">{html.escape(t.get('outro', ''))}</div></div></body></html>"""


def ffmpeg():
    import imageio_ffmpeg
    return imageio_ffmpeg.get_ffmpeg_exe()


def to_mp4(png, mp4, seconds=REEL_SECONDS, audio=None):
    audio = audio or os.getenv("DARK_REEL_AUDIO")
    cmd = [ffmpeg(), "-y", "-loglevel", "error", "-loop", "1", "-framerate", "30", "-i", str(png)]
    if audio and Path(audio).exists():
        cmd += ["-i", audio, "-c:a", "aac", "-b:a", "128k", "-shortest"]
    cmd += ["-t", str(seconds), "-vf", "scale=1080:1920,format=yuv420p", "-c:v", "libx264",
            "-preset", "veryfast", "-crf", "20", "-movflags", "+faststart", str(mp4)]
    subprocess.run(cmd, check=True, timeout=120)
    return mp4


def build(series, d, account, render):
    """폴더 d 에 reel_card.html/png, reel.mp4 를 만든다. render = generate_dark_cardnews.render"""
    card = d / "reel_card.html"
    card.write_text(card_html(series, account), encoding="utf-8")
    png = d / "reel_card.png"
    render([(card, png)], viewport_h=1920)
    return to_mp4(png, d / "reel.mp4")
