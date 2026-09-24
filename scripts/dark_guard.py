#!/usr/bin/env python3
"""다크사이드 계정 가드 — 게시 전 마지막 문. LLM 없이 규칙만 본다.

승인 단계 없이 자동 게시하므로(2026-09-24 결정) 이 문이 유일한 안전장치다.
하나라도 걸리면 HOLD — 고쳐서 통과시키지 않고 그 편은 버린다.

규칙
  1. 숫자      슬라이드·캡션의 숫자는 연결된 팩트(제목+노트)에 있어야 한다. 12 이하 정수는 예외.
  2. 팩트 등급  연결 팩트가 원장에 있고 accuracy=match. (수동 검수 시리즈만 partial 허용)
  3. 금지어    용량·사이클·구매 경로·제품 추천
  4. 실명      원장에 나오는 인물 중 허용 목록 밖이면 HOLD
  5. 끝맺음    마지막 장은 end, 출구 문장(cta) 있음
  6. 정신건강  자살·자해 언급 시 109(자살예방상담) 안내 필수
  7. 인과 단정 «약 때문에 죽었다» 류
"""
import hashlib
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
FACTCHECKS = ROOT / "content" / "editorial" / "factchecks.json"

BANNED = [
    r"\d+\s*(mg|ml|㎎|㎖|iu|IU|mcg|μg)\b", r"주당\s*\d", r"하루\s*\d+\s*(알|정|캡슐)",
    r"사이클\s*(방법|짜|구성|추천)", r"\bPCT\b", r"스택\s*(추천|구성)",
    r"구매|구입|직구|판매처|파는\s*곳|어디서\s*(사|구)", r"(추천|강추)\s*(제품|브랜드)",
    r"복용법|투여법|주사\s*(법|방법)",
]
# 공개적으로 본인이 인정했고 주요 매체가 보도한 사람만.
NAME_ALLOW = ["리버 킹", "Liver King"]
# 원장에 나오는 실존 인물 — 허용 목록 밖이면 쓰지 않는다.
NAME_WATCH = ["잭슨 티펫", "재키슨 티펫", "Jaxon Tippet", "칼리 머슬", "마이크 오헌", "Larry Wheels",
              "래리 휠스", "브라이언 존슨", "투트베리제", "발리예바", "RFK", "케네디",
              "가브리엘 갠리", "Gabriel Ganley"]
MENTAL = r"자살|자해|극단적\s*선택"
CAUSAL = (r"(스테로이드|약물|약|SARMs?|AAS|트렌볼론|DNP)\S{0,3}\s*(때문에|탓에|로\s*인해|으로\s*인해)"
          r"[^.]{0,20}(사망|죽)")
NUM = re.compile(r"\d[\d,]*(?:\.\d+)?")
ALWAYS_OK = {"109"}  # 자살예방상담전화 — 안내 문구용


def fact_id(title):
    return hashlib.sha1(title.encode("utf-8")).hexdigest()[:10]


def load_facts(path=FACTCHECKS):
    data = json.loads(Path(path).read_text(encoding="utf-8"))
    return {fact_id(f["title"]): f for f in data.get("factchecks", [])}


def _norm(n):
    n = n.replace(",", "")
    return n.rstrip("0").rstrip(".") if "." in n else n


def is_small(n):
    """12 이하 정수 — 장 번호·기간(8주) 같은 일상 숫자는 출처 대조에서 뺀다."""
    return "." not in n and "," not in n and int(n) <= 12


def _texts(series):
    for s in series.get("slides", []):
        for k in ("text", "sub", "title", "label", "num", "cta", "kicker"):
            if s.get(k):
                yield k, str(s[k])
    for line in series.get("caption", []):
        yield "caption", str(line)


def check(series, facts=None):
    """→ (ok, [사유]). ok=False 면 게시하지 않는다."""
    facts = load_facts() if facts is None else facts
    why = []
    manual = bool(series.get("manual_review"))

    linked = [facts.get(i) for i in series.get("fact_ids", [])]
    if not linked:
        why.append("팩트 연결 없음")
    for i, f in zip(series.get("fact_ids", []), linked):
        if f is None:
            why.append(f"원장에 없는 팩트 {i}")
        elif f.get("accuracy") != "match" and not (manual and f.get("accuracy") == "partial"):
            why.append(f"팩트 등급 {f.get('accuracy')}: {f['title'][:30]}")

    allowed = set()
    for f in filter(None, linked):
        allowed |= {_norm(n) for n in NUM.findall(f.get("title", "") + " " + f.get("notes", ""))}
    for k, t in _texts(series):
        if k == "kicker":
            continue
        for n in NUM.findall(t):
            v = _norm(n)
            if v not in allowed and v not in ALWAYS_OK and not is_small(n):
                why.append(f"출처 없는 숫자 {n} ({k})")

    blob = "\n".join(t for _, t in _texts(series))
    for pat in BANNED:
        if re.search(pat, blob):
            why.append(f"금지 표현 /{pat}/")
    for name in NAME_WATCH:
        if name in blob and name not in NAME_ALLOW:
            why.append(f"허용 밖 실명 {name}")
    if re.search(CAUSAL, blob):
        why.append("사망 인과 단정")
    if re.search(MENTAL, blob) and "109" not in blob:
        why.append("정신건강 언급에 109 안내 없음")

    slides = series.get("slides", [])
    if not slides or slides[0].get("kind") != "cover":
        why.append("첫 장이 cover 아님")
    if not slides or slides[-1].get("kind") != "end" or not slides[-1].get("cta"):
        why.append("마지막 장이 end+cta 아님")
    if not 5 <= len(slides) <= 10:
        why.append(f"장수 {len(slides)} (5~10)")
    return (not why, sorted(set(why)))


if __name__ == "__main__":
    import sys
    for p in sys.argv[1:]:
        ok, why = check(json.loads(Path(p).read_text(encoding="utf-8")))
        print(("PASS " if ok else "HOLD ") + p + ("" if ok else " — " + "; ".join(why)))
