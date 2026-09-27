#!/usr/bin/env python3
"""디자인 토큰 적용 — design/tokens.json 의 색·폰트를 카드 CSS 에 반영한다.

CSS 에 박힌 기본값(아래 DEFAULTS)을 토큰 값으로 바꾸는 방식이라, 토큰 파일이 없거나
키가 빠져도 지금 모습 그대로 나온다. Figma 등 디자인 도구에서 정한 값을 이 파일에만 옮기면 된다.
"""
import json
import re
from pathlib import Path

TOKENS = Path(__file__).resolve().parent.parent / "design" / "tokens.json"
DEFAULTS = {
    ("color", "bg"): ["#050505"],
    ("color", "ink"): ["#EDEAE4"],
    ("color", "accent"): ["#C8141E"],
    ("color", "accent_dim"): ["#B3121B"],
    ("color", "muted"): ["#8A857C"],
    ("color", "faint"): ["#5C5850"],
    ("color", "source"): ["#6F6A62"],
}
FONTS = {"serif": "Noto Serif KR", "sans": "Noto Sans KR", "display": "Cormorant Garamond"}


def load(path=TOKENS):
    try:
        return json.loads(Path(path).read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return {}


def apply(css, tokens=None):
    t = load() if tokens is None else tokens
    for (grp, key), olds in DEFAULTS.items():
        new = (t.get(grp) or {}).get(key)
        if new and re.fullmatch(r"#[0-9A-Fa-f]{6}", new):
            for old in olds:
                css = re.sub(re.escape(old), new, css, flags=re.I)
    for key, old in FONTS.items():
        new = (t.get("font") or {}).get(key)
        if new and new != old and re.fullmatch(r"[A-Za-z0-9 ]{2,40}", new):
            css = css.replace(f"'{old}'", f"'{new}'").replace(old.replace(" ", "+"), new.replace(" ", "+"))
    return css
