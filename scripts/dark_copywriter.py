#!/usr/bin/env python3
"""다크사이드 계정 카피 작성 — 팩트 하나 → 캐러셀 JSON.

모델 순서 (2026-09-24 결정: «최대한 GPT 로컬로»)
  1. aside → openai-codex/gpt-5.6-luna  (ChatGPT 구독 지갑, 맥에서만)
  2. 맥미니 로컬 LLM (ollama qwen3:8b, 0원)
  3. 둘 다 실패 → None (유료 모델로 자동 대체하지 않는다)
강제로 고르기: DARK_LLM=aside|local
팩트는 공개 논문·보도 요약이라 aside 경계(공개 정보만)를 지킨다.
"""
import json
import os
import re
import sys
import urllib.request
from pathlib import Path

NOGEAR_ROOT = Path(os.getenv("NOGEAR_ROOT", Path.home() / "nogear"))
LOCAL_URL = os.getenv("NOGEAR_LOCAL_LLM_URL", "http://localhost:11434/api/generate")
LOCAL_MODEL = os.getenv("NOGEAR_LOCAL_LLM_MODEL", "qwen3:8b")

SPEC = """너는 인스타그램 '다크사이콜로지' 스타일 캐러셀 카피라이터다.
주제: 몸·운동 산업의 어두운 면(가짜 몸, 약물, 숨은 성분, 되돌릴 수 없는 대가).
형식: 검은 배경, 한 장에 한두 문장, 붉은 강조어는 *별표*로 한 장에 하나만.

반드시 지킬 것
- 숫자는 아래 FACT 에 있는 숫자만 쓴다. 새 숫자를 만들지 않는다.
- 용량·사이클·복용법·구매 경로·제품 추천 금지.
- 특정 인물 실명 금지. 사람이 아니라 산업·약물·알고리즘을 비판한다.
- 사망을 특정 약 탓으로 단정하지 않는다.
- 조롱·체형 비하 금지. 마지막 장은 방어법이나 출구로 끝낸다.
- 6~8장. 첫 장 kind=cover, 마지막 장 kind=end(cta 필수).

slide kind
- cover: {"kind":"cover","kicker":"영문 대문자 2~3단어","text":"훅 한두 줄"}
- line:  {"kind":"line","text":"문장","sub":"보조 문장(선택)"}
- item:  {"kind":"item","no":"01","title":"짧은 제목","text":"문장"}
- stat:  {"kind":"stat","num":"FACT 속 숫자","label":"설명","src":"출처 이름"}
- end:   {"kind":"end","text":"마무리 문장","cta":"저장 유도 한 줄"}
줄바꿈은 \\n.

JSON 하나만 출력한다:
{"tag":"영문 대문자 태그","slides":[...],"caption":["첫 줄 훅","", "핵심 3줄", "", "출처: ..."]}
"""


def prompt_for(fact):
    return (SPEC + "\nFACT 제목: " + fact["title"] + "\nFACT 검증 노트: " + fact.get("notes", "")[:1500]
            + "\n\nJSON:")


def extract_json(text):
    """모델 답에서 가장 바깥 JSON 오브젝트를 꺼낸다. 실패 시 None."""
    if not text:
        return None
    text = re.sub(r"<think>.*?</think>", "", text, flags=re.S)
    start = text.find("{")
    while start != -1:
        depth = 0
        for i in range(start, len(text)):
            if text[i] == "{":
                depth += 1
            elif text[i] == "}":
                depth -= 1
                if depth == 0:
                    try:
                        obj = json.loads(text[start:i + 1])
                        if isinstance(obj, dict) and obj.get("slides"):
                            return obj
                    except json.JSONDecodeError:
                        pass
                    break
        start = text.find("{", start + 1)
    return None


def via_aside(prompt):
    sys.path.insert(0, str(NOGEAR_ROOT / "scripts"))
    import aside_ask  # noqa: E402 — 맥의 노기어 저장소에 있다
    if not aside_ask.available():
        return None
    return aside_ask.ask(prompt, who="dark_copywriter", kind="dark_carousel_copy",
                         timeout=180, until=r'"caption"\s*:\s*\[[^\]]*\]\s*\}')


def via_local(prompt):
    body = json.dumps({"model": LOCAL_MODEL, "prompt": prompt, "stream": False, "think": False,
                       "format": "json", "options": {"temperature": 0.6, "num_predict": 2000}}).encode()
    req = urllib.request.Request(LOCAL_URL, data=body, headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=180) as r:  # noqa: S310 — 로컬 고정 주소
        return json.loads(r.read().decode()).get("response", "")


PROVIDERS = {"aside": via_aside, "local": via_local}


def write(fact, order=None):
    """→ (series dict | None, 쓴 모델 이름, 실패 사유 목록)"""
    forced = os.getenv("DARK_LLM")
    order = order or ([forced] if forced else ["aside", "local"])
    errors = []
    p = prompt_for(fact)
    for name in order:
        try:
            obj = extract_json(PROVIDERS[name](p))
        except Exception as e:  # noqa: BLE001 — 한 모델이 죽어도 다음으로
            errors.append(f"{name}: {type(e).__name__}: {str(e)[:120]}")
            continue
        if obj:
            return obj, name, errors
        errors.append(f"{name}: JSON 없음")
    return None, None, errors
