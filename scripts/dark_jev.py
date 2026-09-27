#!/usr/bin/env python3
"""JEV 심사위원 — 가드·바이럴 게이트를 통과한 캐러셀을 판정 사슬로 한 번 더 본다.
(2026-09-27 Andy «JEV 맥스활용해서 무조건 바이럴 갈 수 밖에 없고, 체크하고»)

한 편을 네 눈이 동시에 본다 — 노기어 판정 사슬(scripts/judgment_chain.py, 맥 ~/nogear):
  코드(dark_viral 규칙) ∥ JEV(TypeSafe, 1건 약 $0.00004) ∥ 맥미니 로컬 LLM(qwen3:8b, 0원) ∥ JEV 규칙 기준선
  둘 이상 같은 답이면 «확정», 갈리면 «의견 갈림»(유료 LLM 대기열), 표가 모자라면 «보류».
레인: dark_carousel_review (nogear config — 섀도우). 문항 7개:
  목록형 훅 · 약속 지킴 · 훅 세기 · 공유 이유 · 저장 가치 · 위험도 · 말투

🔴 섀도우 규칙(노기어 CLAUDE.md): 새 레인은 JEV 가 경로를 정하지 않는다.
   · 확정된 «too_risky» 만 막는다 — 더 조심하는 쪽으로만 쓴다.
   · 나머지는 게시 키트의 «심사 의견»과 올릴 순서 제안에만 쓴다.
   · 게시 48시간 뒤 저장률과 맞춰 본다(dark_jev_audit) — 그게 승격 근거(real_evidence)가 된다.
보내는 것: 게시할 카드 문구(공개)뿐. 팩트 원문·계정 정보·토큰 없음.
판정 사슬을 못 부르면(노기어 저장소 없음·JEV 막힘) 조용히 «심사 없음» — 하루치는 계속 돈다.
"""
import os
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import dark_viral  # noqa: E402

LANE = "dark_carousel_review"
NOGEAR_ROOT = Path(os.getenv("NOGEAR_ROOT", Path.home() / "nogear"))
QUESTIONS = ["list_hook_present", "promise_kept", "hook_strength", "share_trigger", "save_value",
             "risk_level", "tone_fit"]
KO = {"list_hook_present": "목록형 훅", "promise_kept": "약속 지킴", "hook_strength": "훅 세기",
      "share_trigger": "공유 이유", "save_value": "저장 가치", "risk_level": "위험도", "tone_fit": "말투"}
ANSWER_KO = {"true": "예", "false": "아니오", "strong": "강함", "average": "보통", "weak": "약함",
             "identity_mirror": "나도 해당?(정체성)", "warning": "경고", "hidden_truth": "숨은 진실",
             "ranking_reveal": "순위 반전", "none": "없음", "high": "높음", "medium": "보통", "low": "낮음",
             "safe": "안전", "edgy_ok": "세지만 괜찮음", "too_risky": "위험", "street_direct": "헬창 말투",
             "academic": "논문조", "preachy": "훈계조"}


def _p(t):
    return re.sub(r"\s+", " ", re.sub(r"\*", "", str(t or ""))).strip()


def state_of(series):
    """JEV·로컬 LLM 에 보내는 것 — 카드 문구(공개 예정)와 개수만."""
    slides = series.get("slides", [])
    cover = _p(slides[0].get("text")) if slides else ""
    body = []
    for x in slides[1:-1]:
        k = x.get("kind")
        t = (f"{x.get('no', '')} {x.get('title', '')} — {x.get('text', '')}" if k == "item"
             else f"{x.get('num', '')} {x.get('label', '')}" if k == "stat" else x.get("text", ""))
        if _p(t):
            body.append(_p(t)[:90])
    m = re.search(dark_viral.LIST_HOOK, cover, re.I)
    n = int(re.search(r"\d+", m.group(0)).group(0)) if m else 0
    cap = next((_p(c) for c in series.get("caption", []) if _p(c)), "")
    return {"cover": cover[:120], "body": body[:8], "promised_n": n, "item_count": dark_viral.list_count(series),
            "caption_first": cap[:120], "axis": str(series.get("id", "")).split("_")[0]}


def code_answers(series):
    """코드가 낼 수 있는 표 — 입력마다 달라지는 답만(상수 답은 일치율을 속인다)."""
    st = state_of(series)
    pts, forms = dark_viral.hook_points(st["cover"])
    body = series.get("slides", [])[1:-1]
    dense = sum(1 for x in body if x.get("kind") in ("stat", "item"))
    share = ("ranking_reveal" if "순위 반전" in forms else "identity_mirror" if "정체성 특징" in forms
             else "hidden_truth" if "숨은 진실" in forms else "warning" if "금지·경고" in forms else "none")
    return {
        "list_hook_present": "true" if st["promised_n"] else "false",
        "promise_kept": "true" if st["promised_n"] and max(st["item_count"], dense) >= st["promised_n"] else "false",
        "hook_strength": "strong" if pts >= 40 else "average" if pts >= 25 else "weak",
        "save_value": "high" if dense >= 3 else "medium" if dense >= 1 else "low",
        "share_trigger": share,
    }


def _chain():
    sys.path.insert(0, str(NOGEAR_ROOT / "scripts"))
    import judgment_chain  # noqa: E402 — 맥의 노기어 저장소
    return judgment_chain.judge


def review(series, judge=None):
    """→ {"questions": {q: {"answer","status","votes"}}, "jevCalled": bool} 또는 {"unavailable": 사유}"""
    try:
        judge = judge or _chain()
        out = judge(LANE, state_of(series), source="nogear-magazine.dark_daily", questions=QUESTIONS,
                    code_answer=code_answers(series), data_class="public")
    except Exception as e:  # noqa: BLE001 — 심사가 죽어도 하루치는 돈다
        return {"unavailable": f"{type(e).__name__}: {str(e)[:120]}"}
    qs = {q: {"answer": r.get("answer"), "status": r.get("status"),
              "votes": {k: v for k, v in (r.get("votes") or {}).items() if v}}
          for q, r in (out.get("questions") or {}).items()}
    return {"questions": qs, "jevCalled": bool(out.get("jevCalled")), "jevMode": out.get("jevMode")}


RANK = {"strong": 3, "average": 2, "weak": 0, "high": 3, "medium": 2, "low": 0}


def advice(rv):
    """→ (막을까?, 사람이 읽을 한 줄들, 순위 점수). 확정된 답만 믿는다."""
    if not rv or "unavailable" in rv:
        return False, [f"JEV 심사 없음 ({(rv or {}).get('unavailable', '미실행')})"], None
    q = rv["questions"]
    got = {k: v["answer"] for k, v in q.items() if v.get("status") == "decided" and v.get("answer")}
    split = [KO[k] for k, v in q.items() if v.get("status") == "escalated"]
    block = got.get("risk_level") == "too_risky"
    lines = ["JEV 심사(합의): " + (" · ".join(f"{KO[k]} {ANSWER_KO.get(a, a)}" for k, a in got.items()) or "합의 없음")]
    if split:
        lines.append("의견 갈림: " + ", ".join(split))
    if got.get("promise_kept") == "false":
        lines.append("⚠ 표지 개수 약속과 본문 장 수가 안 맞는다는 판정")
    if got.get("tone_fit") in ("academic", "preachy"):
        lines.append(f"⚠ 말투 {ANSWER_KO[got['tone_fit']]} — 올리기 전 표지 한 줄만 다듬기")
    score = RANK.get(got.get("hook_strength"), 1) + RANK.get(got.get("save_value"), 1) \
        + (1 if got.get("share_trigger") not in (None, "none") else 0)
    return block, lines, score
