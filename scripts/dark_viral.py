#!/usr/bin/env python3
"""바이럴 구조 검사 — 가드(안전)를 통과한 편이 «터지는 모양»인지 점수로 본다.

근거: vidIQ 실측 (2026-09-25·27, 한국 심리·자기계발·피트니스 아웃라이어)
  · "목에 칼이 들어와도 절대 말하면 안 되는 5가지"      100만 (채널 중앙값의 226배)
  · "IQ 높은 사람 특징 TOP 7"                           310만 (94배)
  · "일찍 철든 사람 특징"                               150만
  · "인간이 빠지는 쾌락 TOP 7, 1위는 충격입니다"          (68배)
  · "심리학 사실들" 검은 배경 정지 목록 + 잔잔한 음악     110만 (@update.yourmind, 책 판매)
  · @dark.psychologyyyy 스레드 캡처형 8초 정지 릴스       6.8만~11.4만
  · 영어권 "3 reasons I'll never use steroids"          250만 (122배)
공통 구조: [극단 조건/정체성/금지] + [숫자 목록] + [순위·마지막 반전] · 한 장 한 생각 · 저장형.

점수는 100점 만점. PASS_SCORE 미만이면 그 편은 내보내지 않는다(다음 후보로).
«무조건 터진다»를 보장하는 도구는 아니다 — 터진 게시물들과 같은 뼈대인지만 확인한다.
"""
import re

PASS_SCORE = 70

# 표지 훅 공식 — (이름, 정규식, 점수)
HOOK_FORMULAS = [
    ("숫자 목록", r"\d+\s*(가지|개|유형|단계|번째|TOP|위)|TOP\s*\d+", 25),
    ("정체성 특징", r"(사람|몸|헬스인|초보|내추럴)\S{0,4}\s*특징|유형", 15),
    ("금지·경고", r"절대|하면 안 되는|하지 마|목에 칼|위험한|피해야", 15),
    ("숨은 진실", r"아무도|숨기|말 안 하는|모르는|몰랐|진짜 이유|진실|속고", 15),
    ("순위 반전", r"1위|마지막(이|은)?|충격", 10),
    ("2인칭", r"당신|너(는|의|가)|네가", 5),
]
HEDGE = r"단정할 수 없|단정하지 않|연구 한계|한계가 있|확정할 수 없|일반화할 수 없"
MAX_LINE = 28  # 한 줄 글자 수 — 휴대폰에서 한눈에 읽히는 한계


def _plain(t):
    return re.sub(r"\*", "", str(t or ""))


def hook_points(hook):
    h = _plain(hook)
    got = [(n, p) for n, pat, p in HOOK_FORMULAS if re.search(pat, h)]
    return min(45, sum(p for _, p in got)), [n for n, _ in got]


def score(series):
    """→ (점수, 통과?, 사유 목록)"""
    slides = series.get("slides", [])
    notes, pts = [], 0
    cover = slides[0] if slides else {}
    hp, forms = hook_points(cover.get("text", ""))
    pts += hp
    notes.append(f"표지 공식 {'+'.join(forms) or '없음'} ({hp}/45)")

    if len(slides) > 1 and slides[1].get("kind") in ("stat", "item"):
        pts += 15
    else:
        notes.append("2장이 숫자·목록이 아님 (-15)")

    body = slides[1:-1]
    dense = sum(1 for x in body if x.get("kind") in ("stat", "item"))
    pts += min(10, dense * 4)
    if dense < 2:
        notes.append(f"숫자·목록 장이 {dense}장 (2장 이상 권장)")

    long_lines = [ln for x in slides for k in ("text", "label", "title") for ln in _plain(x.get(k)).split("\n")
                  if len(ln) > MAX_LINE + 12]
    if long_lines:
        notes.append(f"긴 줄 {len(long_lines)}개 (> {MAX_LINE + 12}자)")
    else:
        pts += 10

    if any(re.search(HEDGE, " ".join(_plain(v) for v in x.values())) for x in slides):
        notes.append("본문에 면책 문장 (-10)")
    else:
        pts += 10

    end = slides[-1] if slides else {}
    if re.search(r"저장|공유|보내|태그", _plain(end.get("cta"))):
        pts += 5
    else:
        notes.append("마지막 장 CTA 에 저장/공유 없음")

    cap = " ".join(map(str, series.get("caption", [])))
    pts += 5 if "?" in cap else 0
    if "?" not in cap:
        notes.append("캡션에 댓글 질문 없음")

    th = series.get("thread") or {}
    if th and 3 <= len(th.get("items", [])) <= 7:
        pts += 0  # 릴스 글은 있으면 좋다 — 감점만 한다
    elif th:
        notes.append("릴스 목록 길이 이상")
    ok = pts >= PASS_SCORE
    return pts, ok, notes
