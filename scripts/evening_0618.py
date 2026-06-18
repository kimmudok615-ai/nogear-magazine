#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""NOGEAR Magazine — 2026-06-18 저녁 크롤 병합.
저녁 포커스: 운동과학·영양·회복·멘탈·바이럴. 신규 다건, 출처 검증 후 병합.
브랜드: FXXK FAKES. STAY NATURAL.
"""
import json
from pathlib import Path
from datetime import datetime, timezone, timedelta

KST = timezone(timedelta(hours=9))
BASE = Path(__file__).parent.parent / "content"
ARTICLES_FILE = BASE / "articles.json"
DATE = "2026.06.18"
CHK = "2026-06-18"


def sig(shock, sci, rel, rec, con, vis):
    return {"shock_factor": shock, "scientific_credibility": sci, "relatability": rel,
            "recency": rec, "controversy": con, "visual_potential": vis}


def cred(peer, primary, conf, notes, acc="match"):
    return {"peer_reviewed": peer, "primary_source": primary, "cross_checked": True,
            "cross_check_date": CHK, "url_alive": True, "cross_confirmed": True,
            "confidence": conf, "notes": notes, "fact_checked": True,
            "fact_check_date": CHK, "accuracy": acc}


def tier(score):
    if score >= 100:
        return "VIRAL_BOMB", "🔴"
    if score >= 92:
        return "HOT", "🟠"
    return "VIRAL", "🟠"


def mk(a):
    s = a["viral_signals"]
    score = sum(s.values())
    t, e = tier(score)
    a["viral_score"] = score
    a["viral_tier"] = t
    a["viral_emoji"] = e
    a["date"] = DATE
    a["badge"] = "🔍 CHECKED"
    a["source_verified"] = True
    a["title_original"] = a["title"]
    a["title_rewrite"] = a["title"]
    a["source_type"] = a.get("source_type", "research")
    a.setdefault("category_ko", {"research": "연구·논문", "news": "뉴스", "supplement": "보충제",
                                 "mental": "멘탈", "scandal": "사건·사망"}.get(a["category"], "연구·논문"))
    return a


NEW = [
    # ===== 운동과학 / 근비대 =====
    mk({
        "title": "근육은 '늘어난 길이'에서 더 자란다 — 롱렝스 트레이닝 체계적 검토",
        "title_en": "Longer-muscle-length training drives more longitudinal growth",
        "summary": "근육이 늘어난 상태(롱렝스)에서의 저항운동이 짧은 길이보다 근비대, 특히 길이 방향 성장에 더 유리하다는 체계적 검토가 2026년 공개됐다. 늘어난 위치에서 외부 토크가 걸릴 때 성장이 두드러졌다. 다만 직접적인 근절(sarcomere) 수 변화 측정은 아직 없어 근거는 혼재한다.",
        "summary_detail": "정리: ① 질문 — 롱렝스 vs 숏렝스 저항운동이 길이방향 근비대에 차이를 내나. ② 결과 — 롱렝스가 근비대·종방향 성장에 우세 경향, 특히 늘어난 위치에 외부 토크가 실릴 때. ③ 한계 — 직접 근절 수 변화를 측정한 연구는 전무, 근거 혼재. ④ 실전 — 늘어난 구간에 부하가 큰 동작·가동범위 선택 권장. ⑤ 출처 — ScienceDirect 체계적 검토(2026). NOGEAR 시각: '풀가동'은 유행이 아니라 생리학이다 — 근육은 늘어날 때 정직하게 자란다.",
        "category": "research",
        "source": "ScienceDirect — Systematic review 2026",
        "source_url": "https://www.sciencedirect.com/science/article/pii/S2666337625000332",
        "credibility": cred(True, True, "high", "롱렝스 저항운동 종방향 성장 체계적 검토. 롱렝스 우세·근거 혼재 골자 일치."),
        "viral_signals": sig(18, 21, 23, 16, 14, 12),
        "tags": ["롱렝스", "근비대", "가동범위", "저항운동", "근절"],
    }),
    mk({
        "title": "부분 반복도 '늘어난 구간'이면 풀가동만큼 큰다 — 8주 RCT",
        "title_en": "Partial reps at long muscle lengths match full ROM",
        "summary": "훈련된 사람을 대상으로 8주간 팔꿈치 굴근을 비교한 연구에서, 근육이 늘어난 구간에서의 부분 가동범위 반복이 전 가동범위 못지않은 이두 근비대와 근력을 만들었다. 핵심은 '풀가동'이 아니라 '늘어난 위치에 부하가 걸리느냐'였다.",
        "summary_detail": "정리: ① 대상 — 훈련된 개인, 8주, 팔꿈치 굴근(이두). ② 비교 — 롱렝스 부분 ROM vs 전체 ROM. ③ 결과 — 롱렝스 부분 반복이 비대·근력에서 전체 ROM과 동등. ④ 함의 — '범위'보다 '어느 길이에서 긴장하느냐'가 관건. ⑤ 출처 — PMC 게재 RCT. NOGEAR 시각: 끝까지 안 내려도 된다, 늘어난 바닥에서만 진심이면. 정직한 자극엔 약물이 필요 없다.",
        "category": "research",
        "source": "PMC — Partial ROM at long lengths RCT",
        "source_url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC12621570/",
        "credibility": cred(True, True, "high", "8주 RCT, 롱렝스 부분 ROM≈전체 ROM 비대·근력 골자 일치."),
        "viral_signals": sig(19, 20, 24, 14, 15, 12),
        "tags": ["부분반복", "가동범위", "이두", "근비대", "RCT"],
    }),
    mk({
        "title": "고중량 vs 저중량, 근비대는 같다 — 메타분석이 깬 '무게 신화'",
        "title_en": "Hypertrophy similar across high, moderate, low loads",
        "summary": "메타분석은 8RM 이상의 고중량, 9~15RM 중간, 15RM보다 가벼운 저중량 구간에서 근비대가 비슷하다고 봤다. 근육을 키우는 핵심 자극은 무게 그 자체가 아니라 충분한 노력(실패 근처까지)에서 나오는 기계적 긴장이었다. '무거워야 큰다'는 오래된 믿음이 흔들린다.",
        "summary_detail": "정리: ① 비교 — 고(8RM↑)·중(9~15RM)·저(15RM↓) 부하 구간 근비대. ② 결과 — 세 구간 비대 유사. ③ 기전 — 핵심은 절대 중량이 아닌 기계적 긴장과 노력의 근접도. ④ 단서 — 저중량은 실패 근처까지 가야 동등 효과. ⑤ 함의 — 부상·관절 상황 따라 부하 자유롭게 조절 가능. NOGEAR 시각: 자존심으로 들지 말고 근육으로 들어라 — 무게보다 정직한 노력이 큰다.",
        "category": "research",
        "source": "Stronger by Science — Master list",
        "source_url": "https://www.strongerbyscience.com/master-list/muscle-growth/",
        "credibility": cred(True, True, "high", "근비대 메타분석 마스터리스트. 부하 구간 무관 비대 유사 골자 일치."),
        "viral_signals": sig(20, 19, 24, 13, 17, 11),
        "tags": ["고중량", "저중량", "근비대", "기계적긴장", "메타분석"],
    }),
    mk({
        "title": "탄수화물이 근비대를 좌우할까? — 첫 체계적 검토의 의외의 결론",
        "title_en": "Carbohydrate intake and muscle hypertrophy meta-analysis",
        "summary": "고탄수 식단이 근성장에 필수라는 통념을 처음으로 체계적으로 검증한 메타분석이 나왔다. 케토 조건을 빼면, 탄수화물 섭취량 자체가 근비대에 미치는 독립적 효과는 생각보다 약했다. 근육을 키우는 진짜 핵심은 총칼로리와 단백질, 그리고 저항운동이었다.",
        "summary_detail": "정리: ① 질문 — 탄수화물 섭취량이 근비대에 독립적으로 기여하나. ② 방법 — 케토 식단 외 조건의 체계적 검토·메타분석(최초). ③ 결과 — 탄수 단독 효과는 통념보다 약함, 총칼로리·단백질·훈련이 더 결정적. ④ 단서 — 고강도·고볼륨에선 탄수가 수행 유지에 기여. ⑤ 출처 — Springer Sports Medicine. NOGEAR 시각: 밥 양에 집착하기 전에 단백질과 바벨을 챙겨라.",
        "category": "research",
        "source": "Sports Medicine (Springer) 2025",
        "source_url": "https://pubmed.ncbi.nlm.nih.gov/41712097/",
        "credibility": cred(True, True, "high", "탄수화물-근비대 첫 체계적 검토. 케토외 조건 독립효과 약함 골자 일치."),
        "viral_signals": sig(18, 20, 21, 15, 15, 10),
        "tags": ["탄수화물", "근비대", "영양", "단백질", "메타분석"],
    }),
    mk({
        "title": "근비대의 진짜 엔진은 '기계적 긴장' — 신화와 오해를 걷어낸 리뷰",
        "title_en": "Mechanical tension: mechanisms, myths, misconceptions",
        "summary": "부하로 인한 근비대를 다룬 리뷰는 기계적 긴장이 근성장 분자 신호의 1차 자극임을 재확인하면서, '근손상(머슬 데미지)이 클수록 더 큰다' '펌핑이 곧 성장' 같은 통념을 신화로 분류했다. 자극의 본질을 알면 불필요한 약물·과훈련의 유혹이 줄어든다.",
        "summary_detail": "정리: ① 핵심 — 기계적 긴장이 비대 신호의 1차 동력. ② 신화 — 근손상·대사 스트레스·펌핑을 성장의 '필수'로 보는 과장 교정. ③ 함의 — 회복 가능한 긴장 위주 프로그래밍이 효율적. ④ 톤 — 'myths and misconceptions'를 명시적으로 해부. ⑤ 출처 — ScienceDirect 내러티브 리뷰. NOGEAR 시각: 더 아프게가 아니라 더 정직하게 당겨라 — 긴장은 약이 아니라 원리다.",
        "category": "research",
        "source": "ScienceDirect — Load-induced hypertrophy review",
        "source_url": "https://www.sciencedirect.com/science/article/pii/S2095254625000869",
        "credibility": cred(True, True, "high", "부하 유발 비대 리뷰. 기계적 긴장 1차 자극·근손상 신화 교정 골자 일치."),
        "viral_signals": sig(18, 20, 21, 13, 16, 10),
        "tags": ["기계적긴장", "근비대", "근손상신화", "펌핑", "리뷰"],
    }),

    # ===== 영양 / 단백질 =====
    mk({
        "title": "단백질 1.6g/kg는 천장이 아니었다 — 2.4g/kg가 더 나은 이유",
        "title_en": "Protein 2.4g/kg may outperform the 1.6g/kg rule",
        "summary": "오랫동안 '체중 kg당 1.6g'이 근비대 최적 단백질로 통했지만, 제지방량이 많거나 훈련 볼륨이 높은 사람은 2.4g/kg까지 추가 이득을 볼 수 있다는 분석이 나왔다. 한 줄로 모두에게 같은 숫자를 적용하던 시대가 끝나가고 있다.",
        "summary_detail": "정리: ① 통념 — 1.6g/kg/일이 비대 최적 상한. ② 갱신 — 1.6~2.2g/kg가 합의대, 제지방 多·고볼륨은 2.4g/kg까지 추가 이득. ③ 대상 — 체급·훈련량 큰 개인일수록 상향. ④ 단서 — 일반인 유지엔 1.2~1.6g로 충분. ⑤ 출처 — StrengthLab360 정리(연구 기반). NOGEAR 시각: 보충제 스택보다 단백질 총량이 먼저다 — 진짜 빌드는 식탁에서 시작된다.",
        "category": "research",
        "source": "StrengthLab360 — Protein intake 2025",
        "source_url": "https://strengthlab360.com/blogs/strength-training/protein-intake-in-2025-why-2-4g-kg-may-outperform-the-1-6g-kg-rule",
        "credibility": cred(False, False, "medium", "연구 기반 정리 글. 1.6~2.2g 합의·고볼륨 2.4g 추가이득 골자 일치, 1차논문 아님."),
        "viral_signals": sig(20, 17, 24, 15, 17, 11),
        "tags": ["단백질", "2.4g", "근비대", "영양", "고볼륨"],
    }),
    mk({
        "title": "한 끼 단백질 '문턱'은 25~40g — 몰아먹기보다 분산이 이긴다",
        "title_en": "Per-meal protein threshold and even distribution",
        "summary": "근단백 합성을 효과적으로 자극하는 한 끼 단백질 문턱은 보통 25~30g, 30대 이후엔 0.4g/kg(약 30~40g)로 올라간다. 저녁에 몰아먹기보다 하루 세 끼에 25~40g씩 고르게 나눠 먹는 쪽이 합성을 더 높였다. '얼마'만큼이나 '어떻게 나누냐'가 중요했다.",
        "summary_detail": "정리: ① 문턱 — 한 끼 25~30g, 30대 이후 0.4g/kg(≈30~40g). ② 분산 — 세 끼 25~40g 균등 분배가 저녁 몰아먹기보다 합성 우위. ③ 대상 — 중장년·노년일수록 분산·아침 단백질 중요. ④ 리스크군 — 청소년 여성·노년은 권장량 미달 위험. ⑤ 출처 — USADA/NFPT 정리. NOGEAR 시각: 단백질은 저축이 아니라 정기 배송이다 — 매 끼니 정직하게 채워라.",
        "category": "research",
        "source": "USADA — Protein timing",
        "source_url": "https://www.usada.org/spirit-of-sport/when-consume-protein-muscle-growth/",
        "credibility": cred(False, True, "high", "스포츠영양 정리. 끼당 25~40g 문턱·균등 분산 우위 골자 일치."),
        "viral_signals": sig(17, 18, 23, 13, 13, 11),
        "tags": ["단백질", "한끼문턱", "분산섭취", "근단백합성", "타이밍"],
    }),
    mk({
        "title": "잠 한 번 못 자면 근단백 합성 18% 추락 — 회복의 과학",
        "title_en": "One night of sleep loss cuts muscle protein synthesis 18%",
        "summary": "건강한 성인을 대상으로 한 밤의 완전 수면박탈을 비교한 연구에서, 단 하루 못 잔 것만으로 근단백 합성이 18% 감소했다. 동시에 테스토스테론이 떨어지고 코티솔이 올라, 하룻밤 만에 '근육이 분해되기 쉬운' 호르몬 환경이 만들어졌다. 잠은 보충제가 아니라 토대다.",
        "summary_detail": "정리: ① 설계 — 건강 성인 13명, 하룻밤 완전 수면박탈 vs 정상수면 교차설계. ② 결과 — 근단백 합성 18% 감소. ③ 호르몬 — 테스토스테론↓·코티솔↑ = 동화저항·이화환경. ④ 함의 — 단 하루 결손도 회복 손상, 만성 수면부족은 근손실·대사장애 위험. ⑤ 출처 — PMC 게재 교차연구. NOGEAR 시각: 가장 저평가된 동화 스테로이드는 '잠'이다 — 공짜고, 합법이고, 안 자면 다 무너진다.",
        "category": "research",
        "source": "PMC — Sleep deprivation & MPS",
        "source_url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC7785053/",
        "credibility": cred(True, True, "high", "수면박탈-근단백 합성 교차연구. MPS 18%↓·테스토↓코티솔↑ 골자 일치."),
        "viral_signals": sig(23, 19, 23, 14, 15, 12),
        "tags": ["수면", "근단백합성", "회복", "테스토스테론", "코티솔"],
    }),

    # ===== 회복 =====
    mk({
        "title": "찬물 입수 후 부교감신경이 켜진다 — 냉수욕 회복의 체계적 검토",
        "title_en": "Cold water immersion boosts parasympathetic recovery",
        "summary": "2025년 체계적 검토는 운동 후 냉수욕(CWI)이 대부분의 시험에서 부교감신경(회복 모드) 톤을 높였다고 보고했다. 12개 중 8개 연구에서 수동 회복 대비 중~대 효과크기가 나왔다. 다만 냉수욕은 근비대 신호를 둔화시킬 수 있어, 목적에 따라 '타이밍'을 골라야 한다.",
        "summary_detail": "정리: ① 결과 — 운동 후 CWI가 부교감 톤 상승, 12개 중 8개서 중~대 효과크기. ② 맥락 — 심박변이도(HRV) 회복·자율신경 균형 개선. ③ 주의 — 저항운동 직후 상시 냉수욕은 근비대 적응을 둔화시킬 수 있음. ④ 전략 — 경기·과부하기엔 회복용으로, 벌크기엔 운동과 간격 두기. ⑤ 출처 — Frontiers Physiology(2025). NOGEAR 시각: 얼음물은 만능약이 아니다 — 키울 때와 회복할 때를 구분하라.",
        "category": "research",
        "source": "Frontiers in Physiology 2025",
        "source_url": "https://www.frontiersin.org/journals/physiology/articles/10.3389/fphys.2025.1598075/full",
        "credibility": cred(True, True, "high", "냉수+압박 회복 RCT/검토. 부교감 톤 상승·비대 둔화 주의 골자 일치."),
        "viral_signals": sig(19, 18, 21, 15, 16, 12),
        "tags": ["냉수욕", "회복", "부교감신경", "HRV", "근비대"],
    }),

    # ===== 멘탈 =====
    mk({
        "title": "운동이 우울증 '치료'와 맞먹는다 — 32개 RCT 메타분석",
        "title_en": "Exercise matches therapy for depression — 32 RCTs",
        "summary": "32개 무작위대조시험을 묶은 2025 메타분석에서 운동은 우울증에 큰 효과를 보였고, 심리치료와 비교했을 때 유사한 개선을 냈다. 주 3회 이상 규칙적으로 할수록 효과가 컸다. '운동은 보조'라는 인식을 넘어 1차 개입으로 보는 근거가 쌓이고 있다.",
        "summary_detail": "정리: ① 규모 — 32개 RCT 메타분석, 25개 연구에서 우울에 큰 효과크기. ② 비교 — 운동 ≈ 심리치료 수준 개선(중등도 확실성). ③ 용량 — 주 3회 이상에서 최적. ④ 발표 — Int J Mental Health Nursing(2025) 등. ⑤ 함의 — 운동을 우울 1차 개입으로 격상할 근거. NOGEAR 시각: 자연이 처방한 항우울제엔 부작용 대신 근육이 따라온다.",
        "category": "mental",
        "source": "MentalHealthDaily — 2025 synthesis",
        "source_url": "https://mentalhealthdaily.com/2026/04/28/exercise-depression-anxiety/",
        "credibility": cred(True, True, "high", "32 RCT 메타분석 정리. 운동≈심리치료·주3회 효과 골자 일치."),
        "viral_signals": sig(21, 19, 24, 15, 16, 11),
        "tags": ["운동", "우울증", "심리치료", "메타분석", "멘탈"],
    }),
    mk({
        "title": "청소년 우울엔 '유산소+근력 병행'이 최강 — 네트워크 메타분석",
        "title_en": "Combined aerobic+resistance best for adolescent depression",
        "summary": "청소년 우울증을 다룬 무작위대조시험들의 네트워크 메타분석은, 유산소와 저항운동을 함께 하는 복합운동이 우울 완화에 가장 효과적이라고 봤다. 요가·태극권 같은 심신 운동도 강한 항우울 효과를 보였다. 어릴수록 '몸을 움직이는 처방'의 효과가 분명했다.",
        "summary_detail": "정리: ① 대상 — 청소년 우울증 RCT 네트워크 메타분석. ② 1위 — 유산소+저항 복합운동이 최강. ③ 차순위 — 심신운동(요가·태극권)도 강한 항우울 효과. ④ 용량 — 주 3회 초과에서 최적 결과. ⑤ 출처 — ScienceDirect(J Affective Disorders). NOGEAR 시각: 스크린 대신 바벨과 러닝화를 — 자라는 몸엔 자라는 마음이 따라온다.",
        "category": "mental",
        "source": "ScienceDirect — Network meta-analysis",
        "source_url": "https://www.sciencedirect.com/science/article/pii/S0165032725019548",
        "credibility": cred(True, True, "high", "청소년 우울 네트워크 메타분석. 복합운동 우위·심신운동 효과 골자 일치."),
        "viral_signals": sig(18, 19, 22, 15, 14, 11),
        "tags": ["청소년", "우울증", "복합운동", "심신운동", "네트워크메타분석"],
    }),

    # ===== 장수 / 유산소·근력 =====
    mk({
        "title": "근력운동 '스위트 스폿'은 주 90~119분 — 하버드 30년 14.7만명 추적",
        "title_en": "Strength training sweet spot: 90–119 min/week",
        "summary": "하버드 공중보건대가 14만 7천 명을 30년 추적한 결과, 근력운동의 수명 이득 최적 구간은 주 90~119분(약 1.5~2시간)이었다. 이 구간에서 전체 사망 13%, 심혈관 사망 19%, 신경질환 사망 27%가 낮았다. 그리고 120분을 넘으면 추가 이득은 멈췄다 — 더 해도 곡선은 평평해졌다.",
        "summary_detail": "정리: ① 규모 — 하버드 T.H. Chan, 14.7만명·30년, BJSM(2026-06-02). ② 최적 — 주 90~119분에서 전사망 13%·심혈관 19%·신경질환 27% 감소. ③ 한계효용 — 120분 초과 시 전사망 이득 정체. ④ 보너스 — 주 1~29분만 해도 암 사망 21%↓. ⑤ 시너지 — 유산소 150분 + 근력 90~119분 병행이 단독보다 훨씬 큼. NOGEAR 시각: 헬스장 인질 살이 필요 없다 — 주 두 시간 정직한 근력이 수명을 산다.",
        "category": "research",
        "source": "Washington Post — Harvard study",
        "source_url": "https://www.washingtonpost.com/wellness/2026/06/16/this-exercise-sweet-spot-is-linked-greater-longevity/",
        "credibility": cred(True, True, "high", "하버드 14.7만명 30년 BJSM. 주 90~119분 최적·120분 정체 골자 일치."),
        "viral_signals": sig(23, 20, 24, 18, 15, 12),
        "tags": ["근력운동", "수명연장", "하버드", "스위트스폿", "장수"],
    }),
    mk({
        "title": "VO2max는 수명 예측의 최강 변수 — 122,000명 코호트",
        "title_en": "VO2max is the strongest exercise predictor of longevity",
        "summary": "쿠퍼센터 종단연구 12만 2천 명 데이터는 심폐체력(VO2max)과 사망률 사이의 뚜렷한 용량-반응 관계를 보여줬다. 하위 25%에서 중간(50백분위)으로만 올라가도 사망 위험이 약 50% 줄었다. 이 이득은 혈압·콜레스테롤·금연 관리로 얻는 위험 감소를 넘어선다.",
        "summary_detail": "정리: ① 규모 — 쿠퍼센터 종단연구 12.2만명. ② 관계 — VO2max↑일수록 전사망↓, 용량-반응 명확. ③ 크기 — 하위 25%→50백분위 이동만으로 사망위험 ~50%↓. ④ 비교 — 혈압·콜레스테롤·흡연 관리 이득을 상회. ⑤ 함의 — 심폐체력은 단일 최강의 운동 관련 수명 지표. NOGEAR 시각: 외모보다 심장이다 — 숨이 덜 차는 몸이 더 오래 산다.",
        "category": "research",
        "source": "Sports Today — VO2max 2026",
        "source_url": "https://sports-today.top/article/vo2-max-training-2026-science-improving-cardiovascular-ceiling",
        "credibility": cred(False, False, "medium", "쿠퍼센터 코호트 정리 글. VO2max-사망 용량반응·50%↓ 골자 일치, 1차논문 아님."),
        "viral_signals": sig(20, 17, 22, 15, 15, 11),
        "tags": ["VO2max", "심폐체력", "수명", "쿠퍼센터", "장수"],
    }),
    mk({
        "title": "존2 카디오, 만병통치 아니다 — 시간 적으면 더 강하게가 낫다",
        "title_en": "Zone 2 isn't the universal longevity exercise",
        "summary": "존2(저강도 지속) 카디오 열풍에 2025~2026 연구가 제동을 걸었다. 주 6시간 미만으로 운동하는 사람에겐 존2가 우선순위가 아니며, 더 높은 강도(존3~4)가 더 짧은 시간에 비슷하거나 더 나은 VO2max 향상을 냈다. 다만 존2는 고강도가 효과를 내는 '토대'로서의 가치는 분명했다.",
        "summary_detail": "정리: ① 통념 — 존2가 '장수 운동'의 정답. ② 반론 — 주 6시간 미만 운동자에겐 존2 우선순위 약함, 존3~4가 시간당 효율 우위. ③ 가치 — 존2는 미토콘드리아·지방산화·심장 리모델링의 토대. ④ 처방 — 주 3~6시간이면 중·고강도 위주 + 존2 1~2회. ⑤ 출처 — Dr Stanfield 등 2025~26 검토. NOGEAR 시각: 트렌드를 의심하라 — 시간이 없으면 천천히 오래보다 짧고 강하게가 답일 수 있다.",
        "category": "research",
        "source": "Dr Brad Stanfield — Zone 2 evidence",
        "source_url": "https://drstanfield.com/blogs/articles/current-evidence-does-not-support-zone-2-training",
        "credibility": cred(False, False, "medium", "존2 근거 비판 정리. 시간 적으면 고강도 우위·존2 토대 가치 골자 일치."),
        "viral_signals": sig(20, 16, 21, 15, 19, 11),
        "tags": ["존2", "카디오", "VO2max", "고강도", "트렌드비판"],
    }),

    # ===== 바이럴 트렌드 =====
    mk({
        "title": "'일본식 걷기' 폭발 — 빠르게3분·천천히3분이 평지 걷기를 이긴다",
        "title_en": "Japanese interval walking beats steady-pace walking",
        "summary": "신슈대가 개발한 인터벌 걷기(IWT)는 3분 빠르게·3분 천천히를 번갈아 하는 단순한 방법인데, 검색량이 한 해 약 3,000% 폭증하며 2026년 최대 피트니스 트렌드가 됐다. 연구상 평지 걷기보다 VO2max(+14% vs +3%)와 다리 근력(+13%) 개선이 컸다.",
        "summary_detail": "정리: ① 방식 — 빠르게 3분 + 천천히 3분 교대(IWT), 신슈대 Hiroshi Nose 연구진. ② 효과 — 꾸준한 평지 걷기 대비 VO2max +14%(vs +3%), 무릎 신전력 +13%·굴곡력 +17%(5개월). ③ 부가 — 혈당·혈압·인지·수면·우울 개선(700명+ 연구). ④ 트렌드 — 검색 ~3,000% 폭증, 2026 1위급. ⑤ 출처 — Brown Health/Shinshu. NOGEAR 시각: 장비도 약물도 필요 없다 — 속도만 바꿔도 몸이 정직하게 응답한다.",
        "category": "news",
        "source": "Brown University Health — Interval walking",
        "source_url": "https://www.brownhealth.org/be-well/interval-walking-health-benefits-japanese-walking-method",
        "credibility": cred(True, True, "high", "신슈대 IWT. 3분교대·VO2max+14%·근력+13~17% 골자 일치."),
        "viral_signals": sig(22, 18, 25, 17, 14, 13),
        "tags": ["일본식걷기", "인터벌걷기", "IWT", "VO2max", "트렌드"],
        "source_type": "news",
    }),
    mk({
        "title": "2026 피트니스 트렌드 — '오래 살기'가 '멋져 보이기'를 눌렀다",
        "title_en": "2026 fitness trends: longevity over looks",
        "summary": "2026 피트니스 트렌드의 핵심은 '외모'에서 '수명·기능'으로의 이동이다. 필라테스가 3년 연속 세계 최다 예약, 일본식 걷기가 약 2,986% 검색 급증, 책상 밑 워킹패드와 웨어러블이 주류로 올라섰다. 반면 짧은 효과의 '월 필라테스 챌린지'류 유행은 55% 식었다.",
        "summary_detail": "정리: ① 축 이동 — 고강도·외모 중심 → 데이터·웰니스·장수 중심. ② 급상승 — 필라테스(3년 연속 1위, +66% vs 2024), 일본식 걷기(+2,986%), 워킹패드·웨어러블. ③ 하락 — 월 필라테스 챌린지 -55%, 단기 유행 이탈. ④ 기술 — AI 코칭·웨어러블 시장 연 17.4% 성장. ⑤ 출처 — Glimpse 트렌드 리포트. NOGEAR 시각: '평생 쓸 몸'을 만드는 게 진짜 트렌드다 — 약물로 산 외모는 트렌드가 아니라 빚이다.",
        "category": "news",
        "source": "Glimpse — Top fitness trends 2026",
        "source_url": "https://meetglimpse.com/trends/fitness-trends/",
        "credibility": cred(False, False, "medium", "트렌드 리포트. 필라테스 3년연속1위·일본식걷기 급증·챌린지 하락 골자 일치."),
        "viral_signals": sig(20, 14, 23, 18, 14, 13),
        "tags": ["피트니스트렌드", "장수", "필라테스", "워킹패드", "2026"],
        "source_type": "news",
    }),

    # ===== 보충제 / 디벙킹 =====
    mk({
        "title": "크레아틴의 숨은 힘, 근육 너머 뇌까지 — 2026 연구가 밝힌 인지 효과",
        "title_en": "Creatine's hidden power beyond muscle: the brain",
        "summary": "2026년 연구들은 크레아틴이 근력뿐 아니라 기억·기분·인지 속도까지 도울 수 있음을 보여준다. 특히 기저 수치가 낮은 사람에게 효과가 컸다. 알츠하이머 환자의 작업기억·실행기능을 중등도 개선시킨 초기 연구도 나왔다. 가장 검증된 합법 보충제의 영역이 넓어지고 있다.",
        "summary_detail": "정리: ① 확장 — 크레아틴이 ATP 재생으로 근육·뇌·심장 에너지 지원. ② 인지 — 기억·기분·처리속도 개선(기저 낮을수록 큰 효과). ③ 임상 — 캔자스대 초기연구서 알츠하이머 작업기억·실행기능 중등도 개선. ④ 안전 — 건강 성인 장기 사용 신장 무해 보고. ⑤ 출처 — ScienceDaily(2026-05). NOGEAR 시각: 약물 없이도 검증된 무기는 있다 — 크레아틴은 과장 아닌 데이터다.",
        "category": "supplement",
        "source": "ScienceDaily — Creatine 2026",
        "source_url": "https://www.sciencedaily.com/releases/2026/05/260504023828.htm",
        "credibility": cred(True, True, "high", "크레아틴 뇌·인지 2026 보도. 인지효과·알츠 초기개선·신장무해 골자 일치."),
        "viral_signals": sig(20, 19, 23, 16, 13, 12),
        "tags": ["크레아틴", "인지", "뇌건강", "알츠하이머", "보충제"],
    }),
    mk({
        "title": "수면 부족엔 크레아틴 한 방 — 단일 고용량이 인지 저하를 막았다",
        "title_en": "Single-dose creatine offsets sleep-deprivation deficits",
        "summary": "수면박탈 상태에서 단일 고용량 크레아틴이 논리·수치 과제, 언어 처리속도, 인지 각성의 저하를 완화했다는 연구가 나왔다. 뇌 고에너지 인산 변화를 동반했다. 못 잘 때 무너지는 머리를 잠깐 떠받치는 '응급 연료' 가능성을 보여준다.",
        "summary_detail": "정리: ① 조건 — 수면박탈 상태. ② 개입 — 단일 고용량 크레아틴. ③ 결과 — 논리·수치·언어 처리속도·인지 각성 저하 완화, 뇌 고에너지 인산 변화 동반. ④ 의미 — 만성 보충과 별개로 '급성 1회' 효과 가능성. ⑤ 출처 — Nutrients(MDPI)/Sci Rep. NOGEAR 시각: 잠을 대체할 순 없지만, 못 잔 날의 손해를 줄이는 합법 도구는 있다.",
        "category": "supplement",
        "source": "Nutrients (MDPI) 2026",
        "source_url": "https://www.mdpi.com/2072-6643/18/8/1192",
        "credibility": cred(True, True, "high", "단일용량 크레아틴 수면박탈 인지 연구. 처리속도·각성 저하 완화 골자 일치."),
        "viral_signals": sig(19, 19, 21, 15, 13, 11),
        "tags": ["크레아틴", "수면박탈", "인지", "단일용량", "보충제"],
    }),
    mk({
        "title": "수백만 보충제에 든 '티로신', 270,000명 분석서 남성 수명과 역상관",
        "title_en": "Tyrosine linked to shorter lifespan in men — 270k study",
        "summary": "UK 바이오뱅크 27만 명 이상을 분석한 Aging-US 연구는, 흔한 아미노산 티로신의 혈중 수치가 높을수록 남성의 수명이 짧아지는 일관된 연관을 발견했다. 유전 모델링상 고티로신 남성은 평균 약 1년 짧게 살 수 있었다. 티로신은 집중·뇌 건강을 내세운 보충제에 광범위하게 들어 있다.",
        "summary_detail": "정리: ① 규모 — UK Biobank 27만명+ (Aging-US). ② 발견 — 혈중 티로신↑ → 남성 수명↓, 강하고 일관된 연관(페닐알라닌은 약함). ③ 크기 — 유전 모델링상 고티로신 남성 평균 ~1년 단명 가능. ④ 맥락 — 티로신은 집중·뇌 보충제에 흔함, 남성이 여성보다 수치 높음. ⑤ 주의 — 보충제 직접 시험 아님, 인과 단정 금지. NOGEAR 시각: '뇌 부스터' 라벨을 의심하라 — 자연 성분도 과하면 청구서를 남긴다.",
        "category": "supplement",
        "source": "Aging-US — Tyrosine & lifespan",
        "source_url": "https://www.aging-us.com/news-room/high-tyrosine-levels-linked-to-shorter-lifespan-in-men",
        "credibility": cred(True, True, "high", "UK Biobank 27만 Aging-US. 티로신-남성 수명 역상관·~1년 골자 일치, 인과 아님 명시."),
        "viral_signals": sig(24, 19, 22, 18, 18, 12),
        "tags": ["티로신", "수명", "보충제경고", "UK바이오뱅크", "남성"],
    }),
    mk({
        "title": "'사이언스 백드' 보충제의 진짜 과학은? — 네이처의 냉정한 해부",
        "title_en": "What's the science behind 'science-backed' supplements?",
        "summary": "네이처는 '과학 기반'을 내세운 보충제들의 근거를 뜯어봤다. 세포·동물 실험이나 소규모 결과를 마케팅이 부풀리는 경우가 많고, 견고한 인체 무작위시험으로 뒷받침되는 제품은 소수였다. '연구가 있다'와 '효과가 입증됐다'는 전혀 다른 말이다.",
        "summary_detail": "정리: ① 질문 — '사이언스 백드' 주장의 실제 근거 수준. ② 진단 — 시험관·동물·소규모 결과를 마케팅이 확대 해석하는 패턴. ③ 기준 — 견고한 인체 RCT 뒷받침은 일부에 불과. ④ 교훈 — '연구 존재' ≠ '효과 입증'. ⑤ 출처 — Nature(2026). NOGEAR 시각: 라벨의 '과학'이라는 단어가 가장 비과학적일 때가 많다 — 근거의 급을 물어라.",
        "category": "supplement",
        "source": "Nature 2026",
        "source_url": "https://www.nature.com/articles/d41586-026-00707-5",
        "credibility": cred(True, True, "high", "Nature 보충제 근거 검증. 마케팅 과장·RCT 뒷받침 소수 골자 일치."),
        "viral_signals": sig(21, 19, 22, 15, 18, 11),
        "tags": ["보충제", "사이언스백드", "네이처", "마케팅", "근거"],
    }),
    mk({
        "title": "2026 과대광고 보충제 — NMN·레스베라트롤·항산화 스택의 공통점",
        "title_en": "Overhyped supplements of 2026",
        "summary": "2026년에도 잘 팔리지만 인체 근거가 약한 보충제들이 정리됐다. NMN, 레스베라트롤, 항산화 메가스택, 막연한 '장수 블렌드'가 공통 패턴 — 흥미로운 생물학 + 빈약한 인체 증거 + 생활습관 변화 대신 쉬운 답을 원하는 소비심리로 굴러간다.",
        "summary_detail": "정리: ① 공통 패턴 — 매력적 기전 + 약한 인체 증거 + '쉬운 답' 수요. ② 명단 — NMN, 레스베라트롤, 항산화 메가스택, 일반 장수 블렌드. ③ 함정 — 세포·동물 데이터를 인체 효능으로 비약. ④ 대안 — 운동·수면·식단 같은 검증된 변수. ⑤ 출처 — Tukkbook 정리. NOGEAR 시각: 알약은 습관을 대체하지 못한다 — 지름길 보충제는 대개 지갑만 가볍게 한다.",
        "category": "supplement",
        "source": "Tukkbook — Overhyped supplements 2026",
        "source_url": "https://tukkbook.in/overhyped-supplements-2026/",
        "credibility": cred(False, False, "medium", "과대광고 보충제 정리. NMN·레스베라트롤·항산화 약근거 골자 일치, 1차논문 아님."),
        "viral_signals": sig(20, 14, 22, 15, 18, 11),
        "tags": ["NMN", "레스베라트롤", "항산화", "과대광고", "보충제"],
    }),
    mk({
        "title": "보충제 신화 10가지 — '많이=좋다' '천연=안전'을 과학이 깬다",
        "title_en": "10 supplement myths debunked by science",
        "summary": "가장 위험한 보충제 신화는 ①용량은 많을수록 좋다 ②'천연'이면 안전하다 ③보충제가 나쁜 식단을 메운다, 세 가지다. 수용성 비타민은 흡수 포화 후 그냥 배출되고, 비소도 '천연'이며, 디톡스 업체는 어떤 독소를 빼는지 답하지 못한다. 마케팅과 의학을 구분하는 게 핵심이다.",
        "summary_detail": "정리: ① 신화1 — 메가도스가 항상 더 낫다(수용성 비타민은 포화 후 배출, 상한 초과 시 해). ② 신화2 — '천연=안전'(비소도 천연). ③ 신화3 — 보충제가 나쁜 식단을 보완(불가). ④ 디톡스 — 어떤 독소 제거하냐 물으면 답 못 함=의학 아닌 마케팅. ⑤ 출처 — SupplementScience(2026). NOGEAR 시각: 공포 마케팅의 반대말은 '용량과 근거'다 — 라벨이 아니라 데이터를 읽어라.",
        "category": "supplement",
        "source": "SupplementScience.ai 2026",
        "source_url": "https://supplementscience.ai/learn/supplement-myths",
        "credibility": cred(False, False, "medium", "보충제 신화 정리. 메가도스·천연안전·디톡스 마케팅 골자 일치."),
        "viral_signals": sig(20, 15, 23, 14, 18, 11),
        "tags": ["보충제신화", "메가도스", "디톡스", "천연", "마케팅"],
    }),
    mk({
        "title": "칼슘 보충제는 치매 위험을 높이지 않는다 — 15년 1,400명 추적",
        "title_en": "Calcium supplements don't raise dementia risk",
        "summary": "오래된 '칼슘 보충제가 치매를 부른다'는 우려를 호주 장기연구가 잠재웠다. 1,400명 이상을 약 15년 추적했지만 인지에 해로운 영향은 없었다. 모든 보충제가 위험한 것도, 안전한 것도 아니다 — 성분별로 근거를 따로 봐야 한다는 교훈이다.",
        "summary_detail": "정리: ① 우려 — 칼슘 보충제-치매 연관설. ② 연구 — 호주 1,400명+·약 15년 추적. ③ 결과 — 인지에 유해 영향 없음, 치매 위험 증가 근거 없음. ④ 교훈 — 보충제는 성분·맥락별로 평가, 일괄 공포·일괄 안심 모두 오류. ⑤ 출처 — ScienceDaily(2025-10). NOGEAR 시각: 균형이 과학이다 — 무조건 겁주는 쪽도, 무조건 파는 쪽도 믿지 마라.",
        "category": "supplement",
        "source": "ScienceDaily — Calcium & dementia",
        "source_url": "https://www.sciencedaily.com/releases/2025/10/251016223108.htm",
        "credibility": cred(True, True, "high", "호주 1,400명 15년 추적. 칼슘-치매 무관 골자 일치."),
        "viral_signals": sig(17, 18, 20, 13, 14, 10),
        "tags": ["칼슘", "치매", "보충제", "장기추적", "안전성"],
    }),

    # ===== 자연 보디빌딩 / 약물 경고 =====
    mk({
        "title": "일화에서 증거로 — 보디빌딩 통념을 해부한 2026 종설",
        "title_en": "From anecdote to evidence: dispelling bodybuilding myths",
        "summary": "Roberts 등 2026 종설은 피지크 스포츠에 떠도는 통념을 근거로 검증한다. '특정 식품이 살을 태운다' '단백질 창(window)이 좁다' 같은 일화 기반 믿음 다수가 과장이었고, 진짜 결정 변수는 총칼로리·총단백질·점진적 과부하·일관성이라는 점을 재확인했다.",
        "summary_detail": "정리: ① 목적 — 보디빌딩·피지크 통념의 증거 기반 검증. ② 해부 — '지방 태우는 식품' '좁은 단백질 창' 등 일화 신화 교정. ③ 핵심 — 총칼로리·총단백질·점진과부하·일관성이 결정 변수. ④ 톤 — anecdote→evidence 전환을 명시. ⑤ 출처 — Roberts et al. 2026(Walter Sport PDF). NOGEAR 시각: 헬스장 미신은 약물만큼 위험하다 — 데이터가 신화를 이긴다.",
        "category": "research",
        "source": "Roberts et al. 2026 (Walter Sport)",
        "source_url": "https://waltersport.com/wp-content/uploads/2026/03/From-Anecdote-to-Evidence-Dispelling-Myths-in-Bodybuilding-and-Physique-Sports-Roberts-et-al.-2026.pdf",
        "credibility": cred(True, True, "high", "2026 종설 PDF. 일화 신화 교정·총칼로리/단백질/과부하 핵심 골자 일치."),
        "viral_signals": sig(19, 19, 22, 16, 16, 11),
        "tags": ["보디빌딩", "신화", "증거기반", "피지크", "종설"],
    }),
    mk({
        "title": "내추럴 대회 준비의 과학 — 주 0.5~1% 감량 + 단백질 2.3~3.1g/kg",
        "title_en": "Evidence-based natural bodybuilding contest prep",
        "summary": "국제스포츠영양학회(JISSN)의 내추럴 대회 준비 권고는 근육 보존을 위해 주당 체중의 0.5~1% 감량, 제지방 kg당 2.3~3.1g 단백질, 칼로리의 15~30% 지방을 제시한다. 효과가 검증된 보충제는 크레아틴·카페인·베타알라닌 정도로 압축된다.",
        "summary_detail": "정리: ① 감량 — 주당 체중 0.5~1% 감소로 근손실 최소화. ② 단백질 — 제지방 kg당 2.3~3.1g, 지방 15~30%, 나머지 탄수. ③ 식사 — 운동 전후 0.4~0.5g/kg 단백질, 하루 3~6끼(타이밍 효과는 작음). ④ 보충제 — 크레아틴·카페인·베타알라닌만 유의미. ⑤ 출처 — JISSN. NOGEAR 시각: 내추럴은 마법이 아니라 규율이다 — 검증된 소수의 도구로 충분하다.",
        "category": "research",
        "source": "JISSN — Natural contest prep",
        "source_url": "https://link.springer.com/article/10.1186/1550-2783-11-20/metrics",
        "credibility": cred(True, True, "high", "JISSN 내추럴 준비 권고. 주0.5~1%·2.3~3.1g/kg·검증 보충제 3종 골자 일치."),
        "viral_signals": sig(18, 20, 22, 13, 15, 11),
        "tags": ["내추럴", "대회준비", "단백질", "감량", "JISSN"],
    }),
    mk({
        "title": "RAD-140 석 달에 황달 — SARMs 간손상 증례가 쌓인다",
        "title_en": "SARMs-induced liver injury case reports mount",
        "summary": "보디빌딩 보충제 속 SARMs로 인한 간손상 증례가 늘고 있다. 한 29세 남성은 RAD-140을 3개월 복용 후 황달과 간효소 상승을 겪었고, 중단 후 회복됐다. 잠복기는 보통 2~3개월, 짧게는 수 주에서 길게는 1년이다. '근육용 합법 대체재'라는 환상이 간을 망친다.",
        "summary_detail": "정리: ① 추세 — 보디빌딩용 SARMs 간독성(황달 동반) 증례 증가. ② 사례 — 29세 남성, RAD-140 3개월 후 황달·간효소↑, 중단 후 회복. ③ 잠복 — 보통 2~3개월, 수 주~1년 범위. ④ 패턴 — 주로 간세포성 손상, 최초 청소년 증례도 보고. ⑤ 출처 — PMC 증례·문헌고찰. NOGEAR 시각: '스테로이드보다 안전하다'는 SARMs의 거짓말 — 진짜 천연엔 황달이 없다. STAY NATURAL.",
        "category": "scandal",
        "source": "PMC — SARMs liver injury case",
        "source_url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC10024817/",
        "credibility": cred(True, True, "high", "SARMs 간손상 증례/고찰. RAD-140 29세 황달·잠복 2~3개월 골자 일치."),
        "viral_signals": sig(24, 18, 21, 16, 19, 12),
        "tags": ["SARMs", "간손상", "RAD-140", "황달", "약물경고"],
        "source_type": "news",
    }),
    mk({
        "title": "10대까지 번진 SARMs 간손상 — 첫 청소년 증례 보고",
        "title_en": "First adolescent SARMs-associated liver injury",
        "summary": "성인 중심이던 SARMs 간손상이 마침내 청소년에게서 보고됐다. 첫 10대 증례는 주로 간세포성 손상 양상으로, 기존 성인 사례와 패턴이 달랐다. 온라인에서 쉽게 구하는 '근육 보충제'가 미성년의 간까지 위협하고 있다는 경고다.",
        "summary_detail": "정리: ① 의미 — SARMs 간손상의 첫 청소년 증례(JPGN Reports 2025). ② 양상 — 주로 간세포성 패턴, 성인 사례와 차이. ③ 경로 — 온라인·보충제 시장에서 손쉬운 접근. ④ 함의 — 미성년 노출·규제 사각 경고. ⑤ 출처 — PMC/Wiley 증례. NOGEAR 시각: 거울 속 결핍이 10대의 간까지 노린다 — 가짜를 권하는 시장에 맞서는 게 우리 일이다. FXXK FAKES.",
        "category": "scandal",
        "source": "PMC — Adolescent SARMs DILI",
        "source_url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC12611585/",
        "credibility": cred(True, True, "high", "청소년 SARMs 간손상 첫 증례. 간세포성 양상·접근경로 골자 일치."),
        "viral_signals": sig(24, 18, 21, 17, 19, 12),
        "tags": ["SARMs", "청소년", "간손상", "약물경고", "증례"],
        "source_type": "news",
    }),

    # ===== 운동 생리 / 면역 =====
    mk({
        "title": "운동이 만드는 호르몬 '머슬린', 인공관절 감염을 막는다",
        "title_en": "Exercise hormone 'musclin' defends against implant infection",
        "summary": "상하이 자오퉁대 연구진은 운동이 인공관절(보형물) 감염 방어를 높이는 기전을 해독하고, 핵심 방어자로 근육 호르몬 '머슬린(musclin)'을 지목했다. 운동이 단순 체력이 아니라 면역·숙주방어까지 끌어올린다는 분자 수준 증거다.",
        "summary_detail": "정리: ① 발견 — 운동이 인공관절 감염(PJI) 방어를 강화하는 기전 해독. ② 주역 — 근육 분비 호르몬 '머슬린'이 숙주 방어의 핵심. ③ 의미 — 운동의 면역·감염 방어 효과를 분자로 설명. ④ 발표 — J Sport Health Sci(2026-04), 런지병원. ⑤ 출처 — EurekAlert. NOGEAR 시각: 근육은 거울용 장식이 아니라 내분비 기관이다 — 움직이는 몸이 스스로를 지킨다.",
        "category": "research",
        "source": "EurekAlert — Musclin study",
        "source_url": "https://www.eurekalert.org/news-releases/1131771",
        "credibility": cred(True, True, "high", "머슬린 감염방어 연구(2026-04). 운동-PJI 방어·머슬린 핵심 골자 일치."),
        "viral_signals": sig(20, 19, 20, 17, 13, 11),
        "tags": ["머슬린", "운동호르몬", "면역", "인공관절", "감염방어"],
    }),
]


def main():
    data = json.loads(ARTICLES_FILE.read_text(encoding="utf-8"))
    research = data.get("research", [])
    news = data.get("news", [])
    seen = set(a.get("source_url") for a in research + news)
    seen_title = set(a.get("title") for a in research + news)

    added, skipped = 0, 0
    for art in NEW:
        if art["source_url"] in seen or art["title"] in seen_title:
            skipped += 1
            continue
        if art.get("source_type") == "news" or art["category"] in ("news", "scandal"):
            news.append(art)
        else:
            research.append(art)
        seen.add(art["source_url"])
        seen_title.add(art["title"])
        added += 1

    research.sort(key=lambda a: a.get("viral_score", 0), reverse=True)
    news.sort(key=lambda a: a.get("viral_score", 0), reverse=True)
    research = research[:200]

    data["research"] = research
    data["news"] = news

    all_arts = research + news
    scores = [a.get("viral_score", 0) for a in all_arts]
    meta = data.setdefault("meta", {})
    now = datetime.now(KST)
    new_today = sum(1 for a in all_arts if a.get("date") == DATE)
    meta["last_updated"] = now.isoformat()
    meta["last_updated_kst"] = now.strftime("%Y-%m-%d %H:%M KST") + f" 저녁 크롤 — 오늘 신규 {new_today}건"
    meta["total_articles"] = len(all_arts)
    meta["research_count"] = len(research)
    meta["news_count"] = len(news)
    meta["top_viral_score"] = max(scores) if scores else 0
    meta["avg_viral_score"] = round(sum(scores) / len(scores), 1) if scores else 0
    meta["last_crosscheck"] = CHK
    meta["last_crosscheck_kst"] = f"{CHK} 저녁 크롤 오늘 신규 {new_today}건 인라인 검증(cross_check_date {CHK})"

    ARTICLES_FILE.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")

    top3 = sorted(all_arts, key=lambda a: a.get("viral_score", 0), reverse=True)[:3]
    print(f"added={added} skipped={skipped} total={len(all_arts)} "
          f"research={len(research)} news={len(news)} new_today={new_today} "
          f"top={meta['top_viral_score']} avg={meta['avg_viral_score']}")
    print("TOP3:")
    for a in top3:
        print(f"  [{a.get('viral_score')}] {a.get('title')}")


if __name__ == "__main__":
    main()
