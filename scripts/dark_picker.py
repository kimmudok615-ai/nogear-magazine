#!/usr/bin/env python3
"""다크사이드 계정 소재 고르기 — 코드만. 하루 2편, 축이 겹치지 않게.

고르는 기준
  · accuracy=match 인 팩트만
  · 최근 30일 안에 고른 팩트는 제외(원장)
  · 허용 밖 실명이 제목에 있으면 제외
  · 같은 숫자를 wrong/unclear 판정 팩트가 쓰고 있으면 제외(원장끼리 다투는 숫자)
  · 개인 사망 기사(집단 수치 없이 한 사람의 죽음)는 제외 — 가장 논란이 큰 소재
  · 축(AXES) 5개 중 서로 다른 축에서, viral_score 높은 순
"""
import re

import dark_guard
import dark_ledger

AXES = {
    "tactics": r"인플루언서|내추럴|소셜|SNS|알고리즘|가짜|리버 킹|Liver King|비고렉시아|근이형",
    "body_cost": r"심장|급사|급성심장사|혈압|간|불임|정자|사망|조기사망|심근",
    "hidden": r"보충제|FDA|멀티비타민|NMN|레스베라트롤|항산화|성분",
    "drugs": r"SARM|DNP|트렌볼론|펩타이드|AAS|스테로이드|오젬픽|HGH",
    "sport": r"Enhanced|도핑|WADA|올림픽|USADA",
}
DEATH = r"사망|돌연사|숨진|숨져|죽음|멈췄다"
COHORT = r"\d[\d,]*\s*명|%|배|HR|메타|코호트|연구|분석|저널|Journal"


def individual_death(title):
    return bool(re.search(DEATH, title)) and not re.search(COHORT, title)


BG = {"tactics": "body.jpg", "body_cost": "heart.jpg", "hidden": "pills.jpg",
      "drugs": "syringe.jpg", "sport": "gym.jpg"}


def axis_of(title):
    for axis, pat in AXES.items():
        if re.search(pat, title):
            return axis
    return None


def _contested_numbers(all_facts):
    bad = set()
    for f in all_facts:
        if f.get("accuracy") in ("wrong", "unclear"):
            bad |= {dark_guard._norm(n) for n in dark_guard.NUM.findall(f.get("title", ""))
                    if not dark_guard.is_small(n)}
    return bad


def candidates(facts, used=frozenset()):
    contested = _contested_numbers(facts.values())
    out = []
    for fid, f in facts.items():
        title = f.get("title", "")
        if f.get("accuracy") != "match" or fid in used:
            continue
        if any(n in title for n in dark_guard.NAME_WATCH if n not in dark_guard.NAME_ALLOW):
            continue
        if individual_death(title):
            continue
        nums = {dark_guard._norm(n) for n in dark_guard.NUM.findall(title)}
        if nums & contested:
            continue
        axis = axis_of(title)
        if axis:
            out.append((f.get("viral_score") or 0, fid, axis, f))
    out.sort(key=lambda x: (-x[0], x[1]))
    return out


def pick(count=2, facts=None, ledger=dark_ledger.LEDGER, today=None):
    """→ [{fact_id, axis, fact, bg}] 최대 count 개, 축 중복 없이."""
    facts = dark_guard.load_facts() if facts is None else facts
    used = dark_ledger.used_fact_ids(path=ledger, today=today)
    chosen, axes = [], set()
    for _, fid, axis, f in candidates(facts, used):
        if axis in axes:
            continue
        chosen.append({"fact_id": fid, "axis": axis, "fact": f, "bg": BG[axis]})
        axes.add(axis)
        if len(chosen) == count:
            break
    return chosen


if __name__ == "__main__":
    for c in pick():
        print(c["axis"], c["fact_id"], c["fact"]["title"])
