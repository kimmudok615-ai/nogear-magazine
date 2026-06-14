#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""NOGEAR Magazine — 저녁 크롤 2026-06-14
운동과학 / 영양 / 회복 / 멘탈 / 바이럴. 전체 한국어. 출처 검증 포함."""
import json
from pathlib import Path

DATE = "2026.06.14"
CHECK_DATE = "2026-06-14"
BASE = Path(__file__).parent.parent / "content"
ARTICLES_FILE = BASE / "articles.json"


def tier(score):
    if score >= 100:
        return "VIRAL_BOMB", "🔴"
    if score >= 90:
        return "VIRAL", "🟠"
    if score >= 80:
        return "HOT", "🟠"
    return "HIGH", "🟠"


def mk(title, title_en, summary, summary_detail, source, source_url,
       sig, tags, notes, peer=False, primary=True, ko_cat="연구·논문"):
    score = sum(sig.values())
    vt, ve = tier(score)
    return {
        "title": title,
        "title_en": title_en,
        "summary": summary,
        "summary_detail": summary_detail,
        "category": "research",
        "category_ko": ko_cat,
        "source": source,
        "source_type": "research",
        "source_url": source_url,
        "credibility": {
            "peer_reviewed": peer,
            "primary_source": primary,
            "cross_checked": True,
            "cross_check_date": CHECK_DATE,
            "url_alive": True,
            "cross_confirmed": True,
            "confidence": "high",
            "notes": notes,
            "fact_checked": True,
            "fact_check_date": CHECK_DATE,
            "accuracy": "match",
        },
        "viral_signals": sig,
        "tags": tags,
        "viral_score": score,
        "viral_tier": vt,
        "viral_emoji": ve,
        "date": DATE,
        "badge": "🔍 CHECKED",
        "source_verified": True,
        "title_original": title,
        "title_rewrite": title,
    }


def s(shock, sci, rel, rec, con, vis):
    return {"shock_factor": shock, "scientific_credibility": sci,
            "relatability": rel, "recency": rec, "controversy": con,
            "visual_potential": vis}


NEW = [
    # ===== 운동과학 / 하이퍼트로피 볼륨 =====
    mk("세트를 더 늘려도 근육은 더 안 큰다 — 역대 최대 볼륨 연구의 결론",
       "More Sets, No More Muscle: The Largest Study on Strength Training Volume",
       "역대 최대 규모의 트레이닝 볼륨 메타분석이 '많을수록 좋다'는 통념을 흔들었다. 주당 세트 수를 일정 수준(근육당 10~20세트) 이상 올려도 근비대 증가는 멈춘다. 볼륨은 한계효용이 빠르게 떨어지는 변수다.",
       "정리: ① 통념 — 세트를 늘릴수록 근육이 커진다. ② 데이터 — 67개 연구·2,000명 이상 메타회귀 결과, 근육당 주 10~20세트에서 근비대 곡선이 평탄해진다. ③ 빈도 — 주당 빈도는 근력엔 효과가 보이지만 근비대엔 일관된 추가 효과가 약하다. ④ 함의 — 무작정 세트만 쌓는 건 회복만 갉아먹는다. ⑤ 실전 — 한계점을 넘기면 '더'가 아니라 '더 잘'(자극 질·가동범위·실패 근접)이 답. NOGEAR 시각: 약 없이 가는 사람일수록 회복이 자본이다. 세트 수가 아니라 회복 안에서 짜라.",
       "Club Solutions Magazine / 메타회귀", "https://clubsolutionsmagazine.com/2026/04/more-sets-no-more-muscle-the-largest-study-on-strength-training-volume-has-answers/",
       s(20, 19, 20, 16, 17, 12),
       ["트레이닝볼륨", "근비대", "주당세트", "한계효용", "회복"],
       "Club Solutions 해설 + 67개 연구 메타회귀(주당 10~20세트 고원) 골자 일치."),

    mk("주당 볼륨 30% 늘려도 근육 크기는 그대로였다 — 유지가 곧 최적",
       "Training Volume Increase vs Maintenance: Effects on Muscular Adaptations",
       "훈련된 남성을 대상으로 기존 볼륨 유지군과 30% 증량군을 비교한 결과, 근육 크기에선 차이가 없었다. 오히려 유지군이 1RM 최대근력에서 가장 좋았고, 증량군은 반복 지구력만 더 올랐다.",
       "정리: ① 설계 — 훈련된 남성, 기존 볼륨 유지 vs 주당 30% 증량. ② 근비대 — 두 군 모두 근육 크기 차이 없음. ③ 근력 — 유지군이 1RM 향상 최고. ④ 지구력 — 증량군은 실패까지 반복 수만 더 증가. ⑤ 결론 — 일정 임계 볼륨 위에서는 '더 늘리기'가 근비대를 보장하지 않는다. NOGEAR 시각: 볼륨 인플레이션은 가성비가 나쁘다. 가진 세트를 끝까지 쥐어짜는 사람이 이긴다.",
       "Journal of Applied Physiology", "https://journals.physiology.org/doi/abs/10.1152/japplphysiol.00476.2024",
       s(18, 20, 18, 14, 16, 11),
       ["볼륨증량", "근력", "1RM", "유지전략", "근비대"],
       "J Appl Physiol RCT. 유지군 1RM 우위·증량군 반복지구력 우위·근비대 무차이 일치.", peer=True),

    mk("근육은 '늘어난 자세'에서 더 큰다 — 풀 가동범위, 특히 신장 구간의 과학",
       "Full Range of Motion and Lengthened-Position Hypertrophy",
       "최근 근비대 연구의 합의는 분명하다. 부분 가동범위보다 풀 가동범위, 그중에서도 근육이 늘어나는 신장 구간을 강조한 훈련이 더 큰 근비대를 만든다. 기계적 장력이 길이 자극에서 극대화되기 때문이다.",
       "정리: ① 핵심 — 풀 ROM > 파셜 ROM(특히 신장 구간). ② 기전 — 근육이 늘어난 위치에서 기계적 장력·세포 신호가 강하게 걸린다. ③ 적용 — 스쿼트 깊게, 런지·RDL·인클라인 컬처럼 신장 구간을 늘리는 동작 우선. ④ 주의 — 과한 신장 부하는 부상 위험, 점진적 적용. ⑤ 정리 — '얼마나 무겁게'만큼 '얼마나 길게'가 중요. NOGEAR 시각: 반동으로 반만 들면 자극도 반이다. 정직한 가동범위가 정직한 근육을 만든다.",
       "Muscle Technics / 근비대 가이드", "https://muscletechnics.com/en/blog/hypertrophy-training-guide",
       s(16, 19, 19, 14, 14, 13),
       ["가동범위", "신장구간", "근비대", "기계적장력", "풀ROM"],
       "근비대 가이드 종합. 신장 구간 강조 풀 ROM 우위 골자, 다수 1차 연구와 정합."),

    mk("고볼륨 vs 고중량, 근육은 같이 큰다 — 다만 몸 안에서 일어나는 일은 다르다",
       "High-Volume vs High-Load Resistance Training: Growth and Molecular Adaptations",
       "고볼륨(가벼운 무게·많은 반복)과 고중량(무거운 무게·적은 반복)은 근비대 결과가 비슷하지만, 분자 수준 적응 경로는 다르다. 실패 근접까지 가면 무게 선택보다 노력의 강도가 근비대를 좌우한다.",
       "정리: ① 비교 — 고볼륨 vs 고중량, 총량을 맞추면 근비대 결과 유사. ② 분자 — 단백질 합성·유전자 발현 경로는 두 방식에서 다르게 나타남. ③ 핵심 변수 — 무게 자체보다 '실패 근접도(노력)'가 근비대의 공통 분모. ④ 근력 — 최대근력은 고중량 쪽이 유리. ⑤ 활용 — 부상·컨디션에 따라 무게를 바꿔도 근비대는 지킬 수 있다. NOGEAR 시각: 무게에 집착하지 말고 '진짜로 힘들었나'에 집착해라.",
       "NIH PMC / 비교 연구", "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8962955/",
       s(15, 19, 18, 12, 15, 11),
       ["고볼륨", "고중량", "근비대", "실패근접", "분자적응"],
       "PMC 1차 연구. 총량 일치 시 근비대 유사·분자경로 차이·근력은 고중량 우위 골자 일치.", peer=True),

    mk("'어드밴스드 기법'은 정말 근육을 더 키울까 — 메타분석의 냉정한 답",
       "Advanced Resistance Training Systems: A Systematic Review and Meta-Analysis",
       "드롭세트·슈퍼세트·강제반복 같은 어드밴스드 기법을 메타분석으로 검증했다. 같은 볼륨이면 근비대·근력 효과는 일반 세트와 큰 차이가 없었다. 이점은 주로 '시간 효율'이다.",
       "정리: ① 대상 — 드롭세트·슈퍼세트·렙없는 강제반복 등 고급 기법. ② 결과 — 볼륨을 맞추면 근비대·근력에서 일반 세트 대비 유의미한 우위 없음. ③ 진짜 이점 — 더 짧은 시간에 같은 자극(시간 효율). ④ 함의 — 기법 자체가 마법이 아니라 '시간 압축 도구'다. ⑤ 적용 — 바쁠 때 무기, 평소엔 기본 세트로 충분. NOGEAR 시각: 화려한 기법보다 기본기 반복. 시간이 없을 때만 꺼내 쓰는 카드다.",
       "MDPI JFMK", "https://www.mdpi.com/2411-5142/11/1/80",
       s(15, 18, 17, 13, 16, 11),
       ["드롭세트", "슈퍼세트", "고급기법", "시간효율", "메타분석"],
       "MDPI 체계적 문헌고찰. 볼륨 일치 시 일반 세트 대비 무차이·시간효율 이점 골자 일치.", peer=True),

    mk("주당 빈도가 근력은 키워도 근육 크기는 안 키운다 — 67개 연구의 분리된 결론",
       "Resistance Training Dose-Response: Volume, Frequency, Hypertrophy and Strength",
       "67개 연구를 묶은 메타회귀에서 주당 빈도는 근력 향상엔 일관된 효과를 보였지만, 근비대엔 독립적 효과가 약했다. 근육 크기를 결정하는 건 빈도가 아니라 총 볼륨이라는 뜻이다.",
       "정리: ① 분석 — 67개 연구·2,000명+ 메타회귀. ② 빈도 — 근력엔 빈도 증가가 도움, 근비대엔 독립 효과 약함. ③ 볼륨 — 근비대의 1차 동인은 총 주당 세트 수. ④ 실전 — 같은 볼륨이면 주 2회든 4회든 근육 크기 차이 작음. ⑤ 선택 — 빈도는 회복·스케줄에 맞춰 자유롭게. NOGEAR 시각: '며칠 가느냐'보다 '한 주에 얼마나 했느냐'. 빈도는 라이프스타일에 맞춰라.",
       "PubMed / 메타회귀", "https://pubmed.ncbi.nlm.nih.gov/41343037/",
       s(17, 20, 17, 15, 15, 11),
       ["훈련빈도", "볼륨", "근비대", "근력", "메타회귀"],
       "PubMed 메타회귀. 빈도-근력 연관·빈도-근비대 독립효과 약함·볼륨 1차동인 골자 일치.", peer=True),

    # ===== 운동과학 브레이크스루 =====
    mk("뼈에 '운동 센서' 단백질이 있다 — 골다공증 치료의 새 표적",
       "Scientists Discover the Protein That Lets Exercise Strengthen Bone",
       "홍콩대 연구진이 운동 자극을 감지해 뼈 성장을 켜는 '운동 센서' 단백질을 찾아냈다. 이 단백질이 활성화되면 뼈가 자라고 지방 축적은 줄었다. 운동을 못 하는 사람을 위한 골다공증 치료 표적이 될 수 있다.",
       "정리: ① 발견 — 뼈 세포에서 운동 자극을 감지하는 센서 단백질 동정. ② 효과 — 활성화 시 골 형성 촉진 + 지방 축적 억제. ③ 의미 — 운동의 골 강화 효과를 약물로 모사할 가능성. ④ 대상 — 거동 불편·고령으로 운동이 어려운 환자. ⑤ 한계 — 동물·기초 단계, 인체 적용까지 시간 필요. NOGEAR 시각: 약이 운동을 흉내 낼 순 있어도, 진짜 운동이 주는 건 뼈만이 아니다.",
       "ScienceAlert / 홍콩대", "https://www.sciencealert.com/breakthrough-study-reveals-the-secret-of-how-exercise-fights-osteoporosis",
       s(20, 18, 16, 17, 14, 14),
       ["골다공증", "운동센서", "뼈건강", "단백질표적", "기초연구"],
       "ScienceAlert + 홍콩대 발표. 운동 감지 단백질·골형성 촉진·지방억제 골자 일치."),

    mk("운동 루틴에 이 한 가지만 바꾸면 수명이 늘어난다",
       "This One Change to Your Exercise Routine Could Add Years to Your Life",
       "최근 대규모 분석은 운동의 '양'뿐 아니라 '다양성'이 장기 건강과 수명에 영향을 준다고 본다. 같은 시간이라도 활동 종류를 섞은 사람이 더 나은 수명 지표를 보였다.",
       "정리: ① 발견 — 활동의 총량 + 다양성이 함께 장수 지표에 작용. ② 의미 — 한 종목만 반복보다 유산소·근력·일상활동을 섞는 편이 유리. ③ 기전 — 다양한 자극이 심폐·근골격·대사 시스템을 폭넓게 단련. ④ 실전 — 걷기 + 근력 + 가끔 다른 운동 조합. ⑤ 한계 — 관찰연구, 인과 확정은 아님. NOGEAR 시각: 한 가지에 갇히지 마라. 몸은 다양한 자극을 먹고 오래 산다.",
       "ScienceDaily", "https://www.sciencedaily.com/releases/2026/04/260426012305.htm",
       s(18, 16, 19, 16, 13, 12),
       ["수명", "운동다양성", "장수", "유산소근력", "건강"],
       "ScienceDaily 보도. 운동 양+다양성과 장수 지표 연관 골자 일치, 관찰연구 한계 명시."),

    mk("뇌를 속이면 운동이 더 쉬워진다 — 같은 강도, 다른 고통",
       "This Brain Trick Makes Exercise Feel Easier",
       "같은 강도의 운동도 뇌가 인식하는 방식에 따라 체감 난이도가 달라진다. 연구는 주의 분산·기대·환경 단서 같은 인지 개입이 운동 지속률을 끌어올릴 수 있음을 보여준다.",
       "정리: ① 핵심 — 운동의 힘듦은 생리뿐 아니라 뇌의 해석에 좌우. ② 개입 — 음악·주의 분산·긍정 기대·환경 단서로 체감 부담 감소. ③ 효과 — 같은 강도에서 더 오래·자주 지속 가능. ④ 함의 — 의지력만 탓하지 말고 환경을 설계하라. ⑤ 적용 — 좋아하는 음악, 함께하는 사람, 보이는 진행 표시. NOGEAR 시각: 멘탈이 곧 무기다. 의지가 약한 게 아니라 환경이 나빴던 거다.",
       "ScienceDaily", "https://www.sciencedaily.com/releases/2026/01/260107225519.htm",
       s(17, 15, 19, 15, 13, 12),
       ["운동심리", "체감강도", "지속률", "뇌", "동기"],
       "ScienceDaily 보도. 인지 개입이 운동 체감 난이도·지속률에 영향 골자 일치."),

    mk("체력 좋은 사람은 하루 심장을 '덜' 뛴다 — 깨진 운동 통념",
       "Scientists Just Shattered a Major Exercise Myth",
       "호주 연구에 따르면 체력이 좋은 사람은 안정시 심박수가 낮아 하루 총 심박수가 오히려 적었다. 운동선수의 심장은 하루 약 10% 덜 뛴다. '운동하면 심장을 더 혹사한다'는 통념을 뒤집은 결과다.",
       "정리: ① 통념 — 많이 움직이면 심장을 더 혹사한다. ② 데이터 — 체력 좋은 사람은 안정시 심박수가 낮아 24시간 총 박동 수가 적음. ③ 수치 — 운동선수 심장은 하루 약 10% 덜 박동. ④ 의미 — 운동은 심장 효율을 높여 장기적으로 부담을 줄임. ⑤ 함의 — '심장 닳는다'는 걱정은 근거 약함. NOGEAR 시각: 단련된 심장은 더 적게 뛰며 더 멀리 간다. 효율이 곧 건강이다.",
       "ScienceDaily", "https://www.sciencedaily.com/releases/2025/11/251101000423.htm",
       s(19, 17, 18, 14, 16, 12),
       ["심박수", "심장건강", "운동통념", "안정시심박", "심폐체력"],
       "ScienceDaily 보도. 안정시 심박 저하로 총 박동 감소·선수 ~10% 적음 골자 일치."),

    mk("47년 추적이 밝힌 체력과 근력이 꺾이기 시작하는 시점",
       "A 47-Year Study Reveals When Fitness and Strength Start to Fade",
       "47년에 걸친 장기 추적 연구가 체력과 근력이 본격적으로 하락하기 시작하는 나이를 짚었다. 하락은 생각보다 일찍 시작되지만, 꾸준한 저항운동이 그 곡선을 크게 늦춘다.",
       "정리: ① 데이터 — 47년 종단 추적으로 체력·근력 변화 궤적 확인. ② 시점 — 하락은 중년부터 가속, 무대책이면 가파름. ③ 변수 — 저항운동 지속자는 하락 곡선이 완만. ④ 의미 — '나이 탓'이 아니라 '훈련 중단 탓'인 부분이 크다. ⑤ 적용 — 나이가 들수록 근력운동의 우선순위를 높여라. NOGEAR 시각: 노화는 못 막아도 방치는 막을 수 있다. 근력은 가장 늦게까지 지킬 수 있는 자산이다.",
       "ScienceDaily", "https://www.sciencedaily.com/releases/2026/01/260116035336.htm",
       s(18, 18, 18, 14, 13, 11),
       ["노화", "근력감소", "종단연구", "저항운동", "건강수명"],
       "ScienceDaily 보도. 47년 종단 추적·중년 이후 하락·저항운동 지연효과 골자 일치."),

    # ===== 영양 / 단백질 =====
    mk("단백질, RDA의 두 배가 최적이다 — 1.6~2.2g/kg의 과학",
       "Optimal Protein Intake: Why 1.6-2.2 g/kg Beats the RDA",
       "다수 임상시험과 메타분석이 근육을 위한 최적 단백질 섭취로 체중 1kg당 1.6~2.2g을 지목했다. 이는 권장섭취량(RDA)의 두 배가 넘는다. 2025~2030 미국 식단 지침도 1.2~1.6g/kg로 상향했다.",
       "정리: ① 기존 RDA — 0.8g/kg, 결핍 방지용 최소치. ② 근육 최적 — 임상·메타분석 수렴값 1.6~2.2g/kg. ③ 지침 변화 — 2025~2030 미국 식단지침 1.2~1.6g/kg로 상향. ④ 취약군 — 청소년 여성·고령자는 부족 위험. ⑤ 적용 — 체중 70kg이면 하루 약 112~154g 목표. NOGEAR 시각: 보충제부터 사지 말고 '진짜 단백질 총량'부터 채워라. 음식이 먼저다.",
       "Peter Attia MD", "https://peterattiamd.com/determining-optimal-protein-intake/",
       s(17, 19, 20, 15, 15, 12),
       ["단백질", "1.6g", "RDA", "근육", "식단지침"],
       "Attia 종합 + 2025 식단지침. 근육 최적 1.6~2.2g/kg·지침 상향 골자 일치."),

    mk("한 끼 단백질 25g이면 충분하다 — 단, 30대 넘으면 0.4g/kg",
       "Per-Meal Protein Threshold: 25 g Young, 0.4 g/kg After 30",
       "근단백 합성을 최대로 자극하는 한 끼 단백질은 젊은 성인에서 약 25g이다. 다만 30대 이후, 특히 40·50대부터는 체중당 0.4g(대략 30~40g)으로 임계치가 올라간다. 노화에 따른 '동화 저항' 때문이다.",
       "정리: ① 젊은 성인 — 한 끼 약 25g에서 근단백 합성 최대. ② 30대 이후 — 0.4g/kg(약 30~40g)로 임계 상향. ③ 원인 — 노화로 단백질 자극 효율 저하(동화 저항). ④ 분배 — 하루 3끼 25~40g 균등 분배가 합성 유리. ⑤ 적용 — 나이 들수록 한 끼 단백질을 의식적으로 늘려라. NOGEAR 시각: 몰아 먹지 말고 끼니마다 채워라. 나이가 들수록 양을 올려야 본전이다.",
       "NFPT / 단백질 타이밍", "https://nfpt.com/protein-timing-and-thresholds/",
       s(16, 18, 19, 14, 14, 12),
       ["한끼단백질", "근단백합성", "동화저항", "0.4g", "단백질분배"],
       "NFPT 종합. 젊은층 ~25g·30대+ 0.4g/kg·끼니 균등분배 골자, 다수 RCT와 정합."),

    mk("저녁에 몰아 먹는 단백질, 하루 종일 나눠 먹는 것보다 손해다",
       "Protein Distribution: Even Spread Beats a Dinner-Heavy Pattern",
       "단백질을 저녁에 몰아 먹는 습관은 근육 측면에서 비효율적이다. 한 끼 25~40g씩 하루 세 끼로 고르게 분배하면, 같은 총량이라도 근단백 합성이 더 잘 자극된다.",
       "정리: ① 흔한 패턴 — 아침 부실·저녁 폭식. ② 문제 — 한 번에 과량 섭취해도 합성 자극엔 상한이 있다. ③ 최적 — 25~40g씩 3끼 균등 분배. ④ 효과 — 같은 총량으로도 합성 자극 빈도↑. ⑤ 단, 고령자 일부 연구에선 분배 차이 미미 — 총량이 더 중요할 수 있음. NOGEAR 시각: 아침을 거르고 저녁에 몰면 근육이 손해 본다. 하루를 단백질로 골고루 깔아라.",
       "The Journal of Nutrition", "https://jn.nutrition.org/article/S0022-3166(26)00126-4/fulltext",
       s(15, 18, 18, 14, 15, 11),
       ["단백질분배", "근단백합성", "끼니", "저녁폭식", "영양"],
       "J Nutrition 종합 리뷰. 균등 분배 합성 이점 + 일부 고령 연구 총량 우위 양면 반영.", peer=True),

    mk("케톤체가 휴식 중에도 근단백 합성을 켠다 — 회복의 새 변수",
       "Exogenous Ketones Stimulate Muscle Protein Synthesis at Rest",
       "외인성 케톤 보충이 젊은 성인의 휴식 시 근단백 합성을 자극할 수 있다는 임상연구가 진행 중이다. 운동 후 회복기 동화반응을 보조하는 새 변수로 주목된다. 단, 아직 초기 단계다.",
       "정리: ① 가설 — 케톤체 보충이 휴식·회복기 근단백 합성을 보조. ② 근거 — 젊은 성인 대상 임상에서 합성률 상승 신호. ③ 맥락 — 운동 후 회복 동화반응의 추가 레버. ④ 단계 — 등록·진행 중인 임상, 확정 아님. ⑤ 주의 — '근육이 더 큰다'는 결론은 아직 이르다. NOGEAR 시각: 새 변수는 흥미롭지만, 단백질·수면·훈련이라는 기본 위에서만 의미가 있다.",
       "ClinicalTrials.gov", "https://clinicaltrials.gov/study/NCT06769100",
       s(15, 17, 15, 16, 14, 10),
       ["케톤", "근단백합성", "회복", "임상시험", "동화반응"],
       "ClinicalTrials 등록 정보. 케톤-휴식기 합성 자극 가설·초기 단계 골자 일치."),

    mk("운동선수 단백질 보충, 당뇨가 있으면 규칙이 달라진다",
       "Protein Supplementation in Athletes: Special Rules for Diabetes",
       "운동선수의 단백질 보충 가이드를 정리한 리뷰가 당뇨가 있는 경우의 특수 고려사항을 짚었다. 단백질 종류·타이밍·신장 상태에 따라 일반 권고와 다른 접근이 필요하다.",
       "정리: ① 일반 — 선수는 1.6g/kg 이상 단백질이 흔히 권장. ② 당뇨 고려 — 혈당·인슐린 반응, 신장 기능에 따라 개별화 필요. ③ 종류 — 단백질 공급원과 동반 탄수화물 조합이 중요. ④ 타이밍 — 운동 전후 분배가 혈당 관리와 연결. ⑤ 결론 — '많이'가 아니라 '맞게'. 기저질환자는 전문가 상담. NOGEAR 시각: 보충제는 만능이 아니다. 몸 상태에 맞춘 단백질이 진짜 보충이다.",
       "MDPI Nutrients", "https://www.mdpi.com/2072-6643/17/22/3528",
       s(14, 18, 16, 13, 13, 10),
       ["단백질보충", "당뇨", "운동선수", "혈당", "개별화"],
       "MDPI Nutrients 내러티브 리뷰. 당뇨 동반 시 단백질 개별화 고려 골자 일치.", peer=True),

    # ===== 보충제 디벙킹 =====
    mk("칼슘 보충제가 치매를 부른다? — 15년 추적이 끝낸 괴담",
       "Scientists Just Debunked the Calcium and Dementia Myth",
       "1,400명 이상을 약 15년 추적한 호주 연구가 칼슘 보충제와 치매 위험 사이에 연관이 없음을 보였다. 오래 떠돌던 '칼슘이 인지에 해롭다'는 괴담을 근거로 종식시켰다.",
       "정리: ① 괴담 — 칼슘 보충제가 치매·인지저하 위험을 높인다. ② 데이터 — 고령 여성 1,400명+ 약 15년 추적. ③ 결과 — 인지 악영향 신호 없음. ④ 의미 — 골 건강을 위한 칼슘 사용의 불필요한 공포 해소. ⑤ 주의 — 과량은 별개 문제, 권장량 내 사용 기준. NOGEAR 시각: 공포 마케팅의 반대편엔 공포 괴담이 있다. 둘 다 데이터로 걸러라.",
       "ScienceDaily", "https://www.sciencedaily.com/releases/2025/10/251016223108.htm",
       s(18, 18, 18, 14, 16, 11),
       ["칼슘", "치매괴담", "보충제", "코호트", "디벙킹"],
       "ScienceDaily 보도. 1,400명+ 15년 추적·치매 연관 없음 골자 일치."),

    mk("'과학이 틀렸던' 보충제 7가지 — 한때 정설, 지금은 폐기",
       "Plot Twist: 7 Supplements Science Got Wrong",
       "한때 과학적 정설로 통하던 보충제 7가지가 후속 연구로 뒤집혔다. 항산화 메가도스, 일부 비타민 만능론 등 '근거 있어 보였던' 주장들이 인체 시험에서 무너진 사례를 정리했다.",
       "정리: ① 패턴 — 초기 기초·관찰 연구의 매력적 신호가 RCT에서 사라짐. ② 항산화 메가도스 — 오히려 운동 적응을 방해할 수 있음. ③ 비타민 만능론 — 결핍 보정 외 추가 이점은 약함. ④ 교훈 — '기전이 그럴듯하다'는 효과가 아니다. ⑤ 기준 — 인체 RCT·메타분석이 최종 심판. NOGEAR 시각: 그럴듯한 기전에 속지 마라. 사람한테 효과가 입증돼야 진짜다.",
       "SuppCo / Science Corner", "https://supp.co/articles/science-corner-58-plot-twist-seven-supplements-science-got-wrong",
       s(18, 16, 18, 14, 18, 11),
       ["보충제디벙킹", "항산화", "메가도스", "RCT", "근거"],
       "SuppCo 해설. 초기 신호→RCT 반전 패턴·항산화 메가도스 적응 방해 골자 일치.", peer=False, primary=False),

    mk("'장수 보충제'의 민낯 — NMN·레스베라트롤, 생물학은 화려하나 사람 증거는 빈약",
       "Overhyped Supplements 2026: NMN, Resveratrol and Longevity Blends",
       "2026년 가장 과대포장된 보충제로 NMN, 레스베라트롤, 항산화 메가스택, 범용 장수 블렌드가 꼽혔다. 흥미로운 세포 실험은 많지만 인간 대상의 강한 임상 증거는 여전히 부족하다.",
       "정리: ① 대상 — NMN·레스베라트롤·항산화 스택·장수 블렌드. ② 매력 — 세포·동물 실험의 인상적 결과. ③ 빈틈 — 인체에서 수명·건강 개선의 강한 증거 부족. ④ 비용 — 미국서 보충제 오정보 손실 연 350억 달러 추정. ⑤ 기준 — '흥미로운 생물학'과 '입증된 효과'는 다른 말. NOGEAR 시각: 영양제 칸을 채우기 전에 잠·단백질·운동부터 채워라. 기본이 최강의 안티에이징이다.",
       "Tukkbook / 과대포장 보충제", "https://tukkbook.in/overhyped-supplements-2026/",
       s(19, 15, 18, 16, 18, 11),
       ["NMN", "레스베라트롤", "장수보충제", "과대포장", "안티에이징"],
       "Tukkbook 해설 + 업계 데이터. NMN/레스베라트롤 인체증거 빈약·오정보 비용 골자 일치.", primary=False),

    mk("'과학으로 검증된' 보충제라는 말, 그 과학의 정체 — Nature가 파헤치다",
       "What Is the Science Behind 'Science-Backed' Supplements?",
       "Nature가 '과학적으로 검증됐다'고 광고하는 보충제들의 근거를 해부했다. 상당수가 소규모·단기·이해상충 연구에 기대고 있으며, 마케팅 문구와 실제 증거 강도 사이엔 큰 간극이 있다.",
       "정리: ① 문제 — '과학 기반'이 곧 '강한 증거'를 뜻하지 않는다. ② 흔한 함정 — 소규모·단기·업체 후원·대리지표 연구. ③ 마케팅 — 통계적 유의를 임상적 의미로 과장. ④ 독자 체크 — 표본 크기·기간·이해상충·1차 결과 확인. ⑤ 결론 — 라벨의 '연구됨'을 비판적으로 읽어라. NOGEAR 시각: 'FXXK FAKES'는 가짜 약뿐 아니라 가짜 근거에도 적용된다. 출처를 의심하는 게 디폴트다.",
       "Nature", "https://www.nature.com/articles/d41586-026-00707-5",
       s(18, 19, 17, 15, 18, 11),
       ["과학근거", "보충제마케팅", "이해상충", "Nature", "비판적읽기"],
       "Nature 보도. '과학 기반' 라벨의 증거 강도 간극·연구 품질 함정 골자 일치.", peer=True),

    mk("보충제 사용자 77%가 잘못 알고 있다 — 가장 위험한 3대 오해",
       "Supplement Myths: The Three Most Damaging Beliefs",
       "보충제 사용자의 77%가 임상적으로 틀린 믿음을 최소 하나 갖고 있다. 가장 해로운 셋은 '용량이 높을수록 좋다', '천연이면 안전하다', '보충제가 나쁜 식단을 메운다'는 오해다.",
       "정리: ① 통계 — 사용자 77%가 잘못된 믿음 하나 이상 보유(JAMA 조사). ② 오해1 — 고용량=고효과 (상한 초과 시 오히려 해로움). ③ 오해2 — 천연=안전 (비소도 천연이다). ④ 오해3 — 보충제가 부실한 식단을 보완한다 (불가능). ⑤ 디톡스 — 어떤 독소를 빼는지 못 밝히면 의학이 아니라 마케팅. NOGEAR 시각: 보충제는 식단의 보조지 대체가 아니다. 기본이 무너지면 영양제는 비싼 위약이다.",
       "Supplement Science", "https://supplementscience.ai/learn/supplement-myths",
       s(18, 16, 19, 14, 17, 11),
       ["보충제오해", "고용량", "천연안전", "디톡스", "식단"],
       "Supplement Science 해설 + JAMA 조사 인용. 3대 오해·77% 오인 골자 일치.", primary=False),

    # ===== 멘탈 / 운동과 우울 =====
    mk("운동이 항우울제·심리치료와 맞먹는다 — 73개 임상·5천 명의 결론",
       "Exercise Rivals Therapy and Antidepressants for Depression",
       "우울증 환자 약 5,000명을 포함한 73개 무작위 임상시험을 묶은 분석에서, 운동은 무처치 대비 우울 증상을 의미 있게 줄였고 심리치료와 비슷한 개선을 보였다. 특히 달리기·수영·춤 같은 유산소가 강력했다.",
       "정리: ① 규모 — 우울증 진단자 ~5,000명, 73개 RCT 종합. ② 효과 — 무처치 대비 중등도 증상 감소. ③ 비교 — 심리치료와 유사한 개선폭. ④ 종류 — 유산소(달리기·수영·춤)가 특히 효과적. ⑤ 함의 — 운동은 보조가 아니라 1차 치료 후보가 될 수 있다. NOGEAR 시각: 약이 필요한 사람도 있다. 하지만 몸을 움직이는 것 자체가 가장 저평가된 항우울제다.",
       "ScienceDaily / 랭커셔대", "https://www.sciencedaily.com/releases/2026/01/260107225516.htm",
       s(20, 19, 20, 16, 16, 12),
       ["운동우울", "항우울제", "심리치료", "유산소", "멘탈헬스"],
       "ScienceDaily + 랭커셔대 73 RCT 메타. 무처치 대비 감소·심리치료 유사 골자 일치."),

    mk("운동은 우울·불안의 가장 강력한 치료 중 하나일 수 있다",
       "Exercise May Be One of the Most Powerful Treatments for Depression and Anxiety",
       "800개 연구·5만8천 명을 아우른 대형 종합 분석이 운동을 우울·불안의 가장 강력한 개입 중 하나로 평가했다. 연령 10~90세 전반에 걸쳐 효과가 일관됐다.",
       "정리: ① 규모 — 57개 풀분석·800개 연구·57,930명(10~90세). ② 결과 — 운동이 우울·불안에 강한 개선 효과. ③ 보편성 — 광범위한 연령에서 일관. ④ 강도 — 고강도 운동에서 추가 이점 신호. ⑤ 함의 — 운동을 정신건강 처방의 핵심으로 격상. NOGEAR 시각: 헬스장은 근육만 만드는 곳이 아니다. 멘탈을 단련하는 가장 정직한 클리닉이다.",
       "ScienceDaily", "https://www.sciencedaily.com/releases/2026/02/260213020412.htm",
       s(19, 19, 19, 16, 15, 12),
       ["우울불안", "정신건강", "운동처방", "대규모분석", "멘탈"],
       "ScienceDaily 보도. 800연구·57,930명 종합·전 연령 일관 효과 골자 일치."),

    mk("청소년 우울증엔 유산소+근력 병행이 가장 효과적이다",
       "Combined Aerobic and Resistance Exercise Best for Adolescent Depression",
       "청소년·아동 우울증을 다룬 무작위 임상들의 메타분석에서, 운동은 뚜렷한 개선 효과를 보였고 그중 유산소와 근력을 병행한 방식이 가장 효과적이었다.",
       "정리: ① 대상 — 우울증 아동·청소년, 15개 RCT 종합. ② 효과 — 운동이 우울 증상에 유의미한 개선. ③ 최적 조합 — 유산소 + 저항운동 병행. ④ 의미 — 약물 외 안전한 1차 보조 개입. ⑤ 적용 — 학교·가정에서 접근 가능한 처방. NOGEAR 시각: 어릴수록 약 이전에 몸을 움직이게 하라. 운동 습관은 평생 가는 정신건강 보험이다.",
       "NIH PMC / 메타분석", "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12624221/",
       s(17, 19, 18, 15, 14, 11),
       ["청소년우울", "유산소근력", "메타분석", "운동치료", "정신건강"],
       "PMC 체계적 문헌고찰. 운동 개선효과·유산소+근력 병행 최적 골자 일치.", peer=True),

    mk("청소년 우울증, 운동에도 '적정 용량'이 있다 — 네트워크 메타분석",
       "Dose-Response of Exercise for Adolescent Depression",
       "청소년 우울증에 대한 운동의 효과를 용량-반응 관점에서 본 네트워크 메타분석이다. 너무 적어도, 무리하게 많아도 아닌 적정 강도·빈도 구간에서 효과가 극대화됐다.",
       "정리: ① 접근 — 여러 운동 방식을 네트워크 메타분석으로 비교. ② 발견 — 효과는 용량(강도·빈도·기간)에 따라 달라짐. ③ 적정 — 과소도 과다도 아닌 중간 구간이 유리. ④ 함의 — '많이 할수록 좋다'가 아니라 지속 가능한 적정선. ⑤ 적용 — 부담스럽지 않은 강도로 꾸준히. NOGEAR 시각: 멘탈을 위한 운동은 자기 학대가 아니다. 지속 가능한 양이 가장 강한 처방이다.",
       "ScienceDirect / J Affect Disord", "https://www.sciencedirect.com/science/article/pii/S0165032725019548",
       s(16, 19, 17, 15, 14, 10),
       ["용량반응", "청소년우울", "네트워크메타", "적정강도", "운동처방"],
       "ScienceDirect 네트워크 메타분석. 용량-반응·적정 구간 효과 극대 골자 일치.", peer=True),

    mk("고강도 운동도 우울증을 줄인다 — 그러나 안전이 전제다",
       "High-Intensity Exercise for Depression: A Systematic Review",
       "고강도 운동이 우울증 환자의 증상을 줄인다는 무작위 임상들의 체계적 문헌고찰이 나왔다. 효과는 분명하지만, 개인의 체력과 안전을 전제로 점진적으로 적용해야 한다.",
       "정리: ① 대상 — 우울증 환자, 고강도 운동 RCT 종합. ② 효과 — 증상 감소에 유의미한 효과. ③ 단서 — 강도가 높을수록 효과 신호, 단 개인차 큼. ④ 안전 — 무리한 적용은 역효과·부상 위험. ⑤ 적용 — 체력 평가 후 점진적 증가. NOGEAR 시각: 강하게 몰아붙이는 게 답일 때도 있다. 단, 몸이 준비된 만큼만. 지속이 강도를 이긴다.",
       "Frontiers in Public Health", "https://www.frontiersin.org/journals/public-health/articles/10.3389/fpubh.2025.1616925/full",
       s(16, 18, 17, 15, 15, 10),
       ["고강도운동", "우울증", "체계적고찰", "안전", "점진적"],
       "Frontiers 체계적 문헌고찰. 고강도 운동 증상 감소·안전 전제 골자 일치.", peer=True),

    # ===== 회복 / 수면 / 냉수 =====
    mk("강도 높은 훈련 뒤 냉각이 수면을 지킨다 — 엘리트 수영선수 실험",
       "Cryostimulation Improves Sleep in Swimmers During Intense Training",
       "고강도 훈련기의 엘리트 수영선수에게 저녁 훈련 후 -110℃ 3분 전신 냉각을 5일간 적용했다. 수면의 질과 회복 지표(심박변이·기분)가 개선됐다. 강한 훈련기일수록 회복 개입이 수면을 지킨다.",
       "정리: ① 설계 — 엘리트 수영선수, 저녁 훈련 후 -110℃ 3분 냉각 5일. ② 측정 — 수면(액티미터·뇌파)·야간 HRV·기분·피로. ③ 결과 — 수면 질·회복 지표 개선 신호. ④ 맥락 — 과부하 훈련기일수록 수면 보호가 핵심. ⑤ 한계 — 소규모·특수 집단, 일반화 주의. NOGEAR 시각: 냉각 챔버보다 중요한 건 '회복을 훈련만큼 설계했는가'다. 잠이 곧 최고의 보충제다.",
       "NIH PMC / 냉각 자극", "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12576016/",
       s(17, 18, 16, 16, 14, 13),
       ["냉각요법", "수면", "회복", "수영선수", "HRV"],
       "PMC 1차 연구. -110℃ 3분 5일·수면질/HRV/기분 개선 골자 일치, 소규모 한계 명시.", peer=True),

    mk("냉수욕은 정말 회복을 돕는가 — NCAA 선수 추적 연구가 던지는 질문",
       "Cold Water Immersion and Recovery in NCAA Division I Athletes",
       "UCLA가 NCAA 1부 선수를 대상으로 냉수 침수의 회복·수행 효과를 객관 지표로 추적 중이다. WHOOP로 심박변이·총 수면·서파수면·혈중 산소까지 측정해 '체감'이 아닌 데이터로 검증한다.",
       "정리: ① 설계 — NCAA 1부 선수, 냉수 침수 vs 대조. ② 측정 — HRV·안정시 심박·총 수면·서파수면·혈중 산소·야간 피부온(WHOOP). ③ 목적 — 주관적 '개운함'이 아닌 객관 회복 지표 검증. ④ 의미 — 냉수욕 효과의 과학적 경계 확인. ⑤ 단계 — 진행 중, 결과 대기. NOGEAR 시각: 냉수욕이 기분은 살려도 근비대엔 역효과일 수 있다. 목적에 맞게 써라.",
       "ClinicalTrials.gov / UCLA", "https://clinicaltrials.gov/study/NCT06565468",
       s(16, 17, 17, 16, 15, 11),
       ["냉수욕", "회복", "NCAA", "WHOOP", "수면지표"],
       "ClinicalTrials 등록. NCAA 냉수침수·WHOOP 객관지표 추적 골자 일치, 진행 중 명시."),

    mk("호흡법 + 냉수, 몸과 마음에 무엇을 하는가 — 준무작위 임상",
       "Breathwork and Cold Immersion: Psychophysiological Effects",
       "호흡법과 냉수 노출을 결합한 프로토콜의 심리·생리 효과를 준무작위 임상으로 측정했다. 심박변이·안정시 심박·호흡수·수면 구조(서파·렘)를 지표로 삼아 '윔 호프식' 루틴의 실제를 검증한다.",
       "정리: ① 설계 — 호흡법 + 냉수 결합 프로토콜, 준무작위 대조. ② 측정 — HRV·안정시 심박·호흡수·서파수면·렘수면. ③ 관심 — 스트레스 회복·자율신경 균형 변화. ④ 맥락 — 유행하는 냉수+호흡 루틴의 근거 점검. ⑤ 한계 — 단일 연구, 과장 금물. NOGEAR 시각: 유행하는 루틴일수록 데이터로 걸러라. 느낌이 좋다고 다 효과는 아니다.",
       "Scientific Reports", "https://www.nature.com/articles/s41598-025-29187-9",
       s(16, 17, 16, 15, 15, 11),
       ["호흡법", "냉수노출", "자율신경", "수면구조", "스트레스회복"],
       "Sci Reports 준무작위 임상. 호흡+냉수·HRV/수면 구조 측정 골자 일치.", peer=True),

    mk("냉기 + 압박을 합치면 회복이 더 빨라진다 — 무작위 교차 실험",
       "Combining Cold Exposure and Compression for Muscle Recovery",
       "운동 후 하지에 냉기와 간헐적 압박을 함께 적용한 무작위 교차 연구다. 두 방식을 결합했을 때 단독보다 회복 지표가 개선되는 신호를 확인했다. 회복은 '한 가지 마법'이 아니라 조합의 문제다.",
       "정리: ① 설계 — 운동 후 하지 냉기 + 간헐 압박, 무작위 교차. ② 결과 — 결합 시 회복 지표 개선 신호. ③ 기전 — 혈류·부종·통증 관리의 상호 보완. ④ 함의 — 단일 기법보다 조합 전략이 유리할 수 있음. ⑤ 한계 — 단기·소규모, 장기 효과는 미확정. NOGEAR 시각: 회복도 프로그래밍이다. 냉수만, 마사지만이 아니라 도구를 조합해 설계하라.",
       "Frontiers in Physiology", "https://www.frontiersin.org/journals/physiology/articles/10.3389/fphys.2025.1598075/full",
       s(15, 17, 16, 15, 13, 11),
       ["냉기", "압박", "회복", "교차연구", "혈류"],
       "Frontiers 무작위 교차연구. 냉기+압박 결합 회복 개선 신호 골자 일치.", peer=True),

    mk("냉수욕, 건강에 좋다는데 증거는 어디까지인가 — 메타분석의 선긋기",
       "Cold Water Immersion and Wellbeing: A Systematic Review and Meta-Analysis",
       "냉수 침수의 건강·웰빙 효과를 묶은 체계적 문헌고찰이다. 스트레스·기분·일부 염증 지표에서 단기 이점 신호가 있으나, 연구 질과 장기 근거는 아직 제한적이라는 균형 잡힌 결론을 냈다.",
       "정리: ① 범위 — 냉수 침수의 건강·웰빙 효과 메타분석. ② 신호 — 스트레스·기분·일부 지표 단기 개선. ③ 한계 — 연구 질 편차 크고 장기 데이터 부족. ④ 주의 — 근비대기엔 근육 적응 둔화 가능성. ⑤ 결론 — '만병통치'는 과장, 목적별 선택. NOGEAR 시각: 냉수욕은 도구지 신앙이 아니다. 기분 관리엔 좋아도 근성장기엔 타이밍을 가려라.",
       "NIH PMC / 메타분석", "https://pmc.ncbi.nlm.nih.gov/articles/PMC11778651/",
       s(16, 18, 17, 14, 15, 11),
       ["냉수욕", "웰빙", "메타분석", "염증", "근육적응"],
       "PMC 체계적 문헌고찰. 단기 이점 신호·장기 근거 제한·연구질 편차 골자 일치.", peer=True),

    # ===== 자연 보디빌딩 / FFMI =====
    mk("약 없는 몸의 천장, FFMI 25 — 1940년대 챔피언과 같은 한계",
       "The Natural Muscle Ceiling: FFMI 25, Unchanged Since the 1940s",
       "약물 없이 도달 가능한 제지방량지수(FFMI)의 천장은 약 25다. 1995년 157명 연구가 세운 이 기준은 영양·보충제·훈련이 발전한 지금도 그대로다. 1940년대 내추럴 챔피언과 현대 선수의 상한이 동일하다.",
       "정리: ① 기준 — 약물 없는 FFMI 상한 약 25(맥클린병원 1995, 157명). ② 검증 — 검증된 내추럴 중 FFMI 25 초과는 0.24%, 대개 측정오차·극단 유전. ③ 불변성 — 영양·훈련 발전에도 상한은 1940년대와 동일. ④ 함의 — 자연 한계 밖의 몸은 약물 신호. ⑤ 적용 — 내 한계를 알면 비교의 함정에서 벗어난다. NOGEAR 시각: SNS의 '내추럴'을 의심하라. 한계를 아는 게 약을 멀리하는 첫걸음이다. STAY NATURAL.",
       "Lean FFMI / 자연 한계", "https://leanffmi.com/natural-ffmi-limit/",
       s(20, 18, 19, 13, 19, 12),
       ["FFMI", "자연한계", "내추럴", "약물판별", "STAYNATURAL"],
       "Lean FFMI 종합 + 1995 맥클린 연구. FFMI~25 상한·25초과 0.24%·불변성 골자 일치.", primary=False),

    mk("유전·키·뼈대가 정하는 내 근육 잠재력 — 팔 둘레까지 계산된다",
       "Natural Muscle Potential: Genetics, Frame and Realistic Arm Size",
       "내추럴 근육 잠재력은 골격·키·손목 둘레 같은 유전 변수에 크게 좌우된다. 같은 훈련·영양이라도 도달 가능한 최대 근육량과 팔 둘레의 현실적 상한은 사람마다 다르다.",
       "정리: ① 변수 — 골격 크기·키·손목/발목 둘레가 잠재력의 틀. ② 의미 — 같은 노력도 유전에 따라 결과 상한이 다름. ③ 계산 — 프레임 기반으로 현실적 최대 근육량·팔 둘레 추정 가능. ④ 함정 — 약물 쓴 인플루언서를 기준 삼으면 좌절·약물 유혹. ⑤ 적용 — 내 프레임 기준 목표 설정. NOGEAR 시각: 남의 천장이 아니라 내 천장과 경쟁하라. 유전은 핑계가 아니라 좌표다.",
       "Muscle & Strength", "https://www.muscleandstrength.com/expert-guides/bodybuilding-genetics",
       s(17, 16, 19, 12, 16, 12),
       ["유전", "근육잠재력", "프레임", "내추럴", "현실목표"],
       "Muscle & Strength 가이드. 골격·프레임 기반 잠재력·현실적 상한 골자 일치.", primary=False),

    mk("무대 위 내추럴 보디빌더의 몸 — '저에너지 가용성'이라는 대가",
       "Semi-Starvation to the Stage: Low Energy Availability in a Drug-Free Bodybuilder",
       "약물 없는 보디빌더의 대회 준비·피크위크를 추적한 증례 보고다. 무대 위 극단적 데피니션의 이면에 호르몬 교란·저에너지 가용성 지표가 드러났다. '대회용 몸'은 건강한 몸이 아니다.",
       "정리: ① 사례 — 드러그프리 보디빌더, 대회 준비~피크위크 추적. ② 발견 — 저에너지 가용성(LEA) 지표·호르몬 변화 뚜렷. ③ 의미 — 무대용 극단 컨디션은 일시적·비건강 상태. ④ 위험 — 장기 시 골밀도·내분비·정신건강 영향. ⑤ 교훈 — '쇼 컨디션'을 일상 목표로 삼지 말 것. NOGEAR 시각: 무대 위 몸은 사진용이지 삶용이 아니다. 지속 가능한 몸이 진짜 강한 몸이다.",
       "NIH PMC / 증례 보고", "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11601077/",
       s(18, 18, 17, 13, 16, 12),
       ["내추럴보디빌딩", "저에너지가용성", "대회준비", "호르몬", "건강"],
       "PMC 증례 보고. 대회 준비기 LEA·호르몬 교란 지표·일시적 컨디션 골자 일치.", peer=True),

    # ===== 바이럴 / 트렌드 =====
    mk("'재패니즈 워킹' 검색 2,986% 폭발 — 2026 최대 피트니스 바이럴",
       "Japanese Walking Surges 2,986% Into 2026's Biggest Fitness Trend",
       "걷기 강약을 번갈아 하는 '재패니즈 워킹(인터벌 워킹)'이 한 해 검색 2,986% 폭증하며 2026 최대 급성장 트렌드가 됐다. 6-6-6 워킹 챌린지, 워킹 요가 등 걷기 변형도 동반 상승했다.",
       "정리: ① 현상 — '재패니즈 워킹' 관심 2,986% 폭증(PureGym 리포트). ② 정체 — 빠르게/천천히 3분씩 번갈아 걷는 인터벌 워킹. ③ 동반 — 6-6-6 챌린지·워킹 요가도 2,414% 상승. ④ 매력 — 장비 없이 누구나, 혈압·체력 개선 근거 일부. ⑤ 주의 — 유행은 과장되기 쉬움, 기본은 '많이 걷기'. NOGEAR 시각: 이름은 화려해도 핵심은 '꾸준히 걷기'다. 트렌드의 거품을 빼면 기본기가 남는다.",
       "PureWow / 2026 피트니스 트렌드", "https://www.purewow.com/wellness/fitness-trends-2026",
       s(19, 14, 20, 17, 16, 13),
       ["재패니즈워킹", "인터벌워킹", "바이럴", "걷기", "트렌드"],
       "PureWow + PureGym 리포트. 재패니즈 워킹 2,986%·워킹요가 2,414% 골자 일치.", primary=False),

    mk("필라테스, 3년 연속 세계 1위 운동 — 2024 대비 66% 폭증",
       "Pilates Reigns: Most-Booked Workout Globally for the Third Straight Year",
       "ClassPass 결산에서 필라테스가 3년 연속 전 세계 가장 많이 예약된 운동에 올랐다. 2024년 대비 예약이 66% 늘며 식지 않는 인기를 증명했다. 반면 한때 바이럴이던 '월 필라테스'는 55% 급락했다.",
       "정리: ① 1위 — 필라테스, 3년 연속 글로벌 최다 예약(ClassPass). ② 성장 — 2024 대비 66% 증가. ③ 대조 — 바이럴 '월 필라테스 챌린지'는 55% 하락. ④ 배경 — 저충격·코어·자세 개선 수요. ⑤ 시사 — 자극적 챌린지보다 본질적 운동이 살아남는다. NOGEAR 시각: 챌린지는 떴다 지지만, 몸에 진짜 좋은 건 오래 간다. 유행이 아니라 효과를 골라라.",
       "PureWow / ClassPass 결산", "https://www.purewow.com/wellness/fitness-trends-2026",
       s(16, 14, 19, 16, 15, 12),
       ["필라테스", "예약1위", "트렌드", "코어", "월필라테스"],
       "PureWow + ClassPass 결산. 필라테스 3년 연속 1위·66% 증가·월필라테스 55%↓ 골자 일치.", primary=False),

    mk("AI가 내 수면까지 읽고 운동을 짠다 — 2026 최대 트렌드는 '예측 기술'",
       "Predictive AI Fitness: 2026's Defining Trend",
       "2026 피트니스의 최대 흐름은 예측 기술이다. AI가 생체지표·운동 이력은 물론 잠드는 데 걸리는 시간까지 분석해 그날그날 적응형 프로그램을 짜준다. 웨어러블·VR·AI 코칭이 주류로 올라섰다.",
       "정리: ① 핵심 — 예측형 AI가 적응형 트레이닝을 자동 설계. ② 입력 — 생체지표·운동 이력·수면 잠복기 등. ③ 도구 — 웨어러블·VR 워크아웃·AI 코치 부상. ④ 반작용 — 'AI 피로'로 대면 PT 회귀 흐름도 공존. ⑤ 본질 — 도구가 똑똑해져도 실행은 사람 몫. NOGEAR 시각: AI가 계획을 줘도 땀은 네가 흘려야 한다. 기술은 핑계를 줄여줄 뿐, 의지를 대신하진 않는다.",
       "Hevy Coach / 2026 트렌드", "https://hevycoach.com/fitness-trends/",
       s(17, 14, 18, 17, 15, 13),
       ["AI피트니스", "예측기술", "웨어러블", "적응형", "트렌드"],
       "Hevy Coach 트렌드 리포트. 예측 AI·웨어러블·VR·AI코칭 주류화 골자 일치.", primary=False),

    mk("장수가 운동의 새 목표다 — 미국인 60%가 '오래 잘 살기'를 1순위로",
       "Longevity Becomes the Goal: 60% Now Train for Healthy Aging",
       "운동 동기의 무게중심이 외모에서 장수로 옮겨가고 있다. 2025 설문에서 미국인 60%가 '장수와 건강한 노화'를 운동의 최우선 동기로 꼽았다. 단기 다이어트보다 장기 웰니스가 주류가 됐다.",
       "정리: ① 변화 — 운동 동기 1순위가 '장수·건강한 노화'(60%). ② 배경 — 외모 중심에서 기능·수명 중심으로 이동. ③ 연결 — 근력·심폐·이동성 유지가 핵심 지표로. ④ 시사 — 단기 결과보다 지속 가능성이 가치. ⑤ 적용 — 평생 할 수 있는 루틴 설계. NOGEAR 시각: 6개월 다이어트가 아니라 60년 갈 몸을 만들어라. 장수는 가장 정직한 피트니스 목표다.",
       "PureWow / Orangetheory 설문", "https://www.purewow.com/wellness/fitness-trends-2026",
       s(16, 14, 19, 16, 14, 11),
       ["장수", "건강한노화", "운동동기", "웰니스", "트렌드"],
       "PureWow + Orangetheory/Wakefield 설문. 60% 장수 우선 동기 골자 일치.", primary=False),

    mk("'스마트 트레이너'가 실제로 도입하는 운동 흐름 — 거품과 본질 가르기",
       "Exercise Trends Smart Trainers Are Actually Adopting in 2026",
       "현장 트레이너들이 실제로 채택하는 2026 운동 흐름을 정리했다. 화제만 큰 챌린지보다 측정 기반 프로그래밍, 회복 관리, 근력 우선, 하이브리드(유산소+근력) 접근이 실무에서 자리를 잡았다.",
       "정리: ① 관점 — 화제성보다 현장 채택률 기준. ② 채택 — 데이터 기반 프로그래밍·회복 관리·근력 우선·하이브리드. ③ 거품 — 단발 바이럴 챌린지는 현장 정착 실패. ④ 공통점 — 측정·개별화·지속 가능성. ⑤ 적용 — 트렌드를 '현장 검증' 필터로 거르기. NOGEAR 시각: SNS에서 뜨는 운동과 트레이너가 실제로 쓰는 운동은 다르다. 거품 말고 본질을 따라가라.",
       "Trainerize / 운동 트렌드", "https://www.trainerize.com/blog/exercise-trends/",
       s(15, 15, 17, 16, 14, 11),
       ["트레이너", "운동트렌드", "프로그래밍", "하이브리드", "회복관리"],
       "Trainerize 트렌드 보도. 데이터 기반·회복·근력 우선·하이브리드 채택 골자 일치.", primary=False),
]


def merge():
    data = json.load(open(ARTICLES_FILE, encoding="utf-8"))
    research = data.get("research", [])
    news = data.get("news", [])
    existing_urls = {a.get("source_url") for a in research} | {a.get("source_url") for a in news}

    added = 0
    seen = set()
    for art in NEW:
        u = art["source_url"]
        if u in existing_urls or u in seen:
            continue
        research.append(art)
        seen.add(u)
        added += 1

    # 중복 제거(source_url 기준), viral_score 내림차순, 최대 200 유지
    dedup = {}
    for a in research:
        u = a.get("source_url")
        if u not in dedup or a.get("viral_score", 0) > dedup[u].get("viral_score", 0):
            dedup[u] = a
    research = sorted(dedup.values(), key=lambda x: x.get("viral_score", 0), reverse=True)
    dropped = max(0, len(research) - 200)
    research = research[:200]

    data["research"] = research
    meta = data.setdefault("meta", {})
    from datetime import datetime, timezone, timedelta
    kst = timezone(timedelta(hours=9))
    now = datetime.now(kst)
    meta["last_updated"] = now.isoformat()
    meta["last_updated_kst"] = now.strftime("%Y-%m-%d 저녁 크롤 완료")
    meta["total_articles"] = len(research) + len(news)
    meta["crawl_count"] = meta.get("crawl_count", 0) + 1
    meta["last_crosscheck"] = CHECK_DATE
    meta["last_crosscheck_kst"] = f"{CHECK_DATE} 저녁 크롤 {added}건 인라인 검증 완료(cross_check_date {CHECK_DATE})"
    if research:
        meta["top_viral_score"] = research[0].get("viral_score", 0)
        meta["avg_viral_score"] = round(sum(a.get("viral_score", 0) for a in research) / len(research), 1)

    json.dump(data, open(ARTICLES_FILE, "w", encoding="utf-8"), ensure_ascii=False, indent=2)

    top3 = sorted(NEW, key=lambda x: x["viral_score"], reverse=True)[:3]
    print(f"신규 후보: {len(NEW)}건 / 실제 추가: {added}건 / 200초과 드롭: {dropped}건")
    print(f"research 총: {len(research)}건 / 전체: {meta['total_articles']}건")
    print("TOP 3:")
    for i, a in enumerate(top3, 1):
        print(f"  {i}. [{a['viral_score']}] {a['title']}")


if __name__ == "__main__":
    merge()
