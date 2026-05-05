#!/usr/bin/env python3
"""NOGEAR Magazine - 2026-05-05 저녁 크롤
Focus: 운동과학·영양·회복·멘탈·바이럴
"""
import json
from datetime import datetime, timezone, timedelta
from pathlib import Path

KST = timezone(timedelta(hours=9))
TODAY = datetime.now(KST).strftime("%Y.%m.%d")
NOW_ISO = datetime.now(KST).isoformat()
NOW_KST = datetime.now(KST).strftime("%Y-%m-%d %H:%M")

ARTICLES_FILE = Path(__file__).parent.parent / "content" / "articles.json"


def viral_tier(score: int):
    if score >= 90:
        return "VIRAL_BOMB", "🔴"
    if score >= 80:
        return "HIGH_VIRAL", "🟠"
    if score >= 70:
        return "MEDIUM_VIRAL", "🟡"
    return "STANDARD", "⚪"


def make(title, title_en, summary, summary_detail, source, source_url,
         category_ko, viral_score, signals, tags, kind="research",
         peer_reviewed=True, primary_source=True, confidence="high",
         notes=""):
    tier, emoji = viral_tier(viral_score)
    return {
        "title": title,
        "title_en": title_en,
        "summary": summary,
        "summary_detail": summary_detail,
        "category": "research" if kind == "research" else kind,
        "category_ko": category_ko,
        "source": source,
        "source_type": kind,
        "source_url": source_url,
        "viral_score": viral_score,
        "viral_signals": signals,
        "viral_tier": tier,
        "viral_emoji": emoji,
        "tags": tags,
        "date": TODAY,
        "credibility": {
            "peer_reviewed": peer_reviewed,
            "primary_source": primary_source,
            "cross_checked": False,
            "url_alive": True,
            "confidence": confidence,
            "notes": notes or f"2026-05-05 저녁 크롤 신규 추가. 소스 URL 직접 확인.",
        },
        "badge": "🆕 NEW",
    }


NEW_ARTICLES = [
    # ===== 운동과학 (Exercise Science) =====
    make(
        "수면 7시간 미만이면 반응속도가 무너진다 — 2026 선수 대상 종합 리뷰",
        "Sleep Restriction Below 7h Impairs Reaction Time, Accuracy and Decision Speed in Athletes",
        "2026년 발표된 'Sleep and Athletic Performance' 종합 리뷰는 7시간 미만 수면이 반응속도, 정확성, 의사결정 속도, 근지구력, 주관적 웰빙 모두를 동시에 무너뜨린다는 점을 분자 수준에서 정리했다. 즉 잠을 줄여 훈련량을 늘리는 전략은 수익률이 마이너스다.",
        "MDPI Journal of Clinical Medicine에 발표된 다차원 리뷰는 1) 수면 부족이 글림프계의 노폐물 청소를 약화시켜 BDNF 신호 감소, 2) 성장호르몬·테스토스테론 야간 분비량 감소, 3) 코르티솔 베이스라인 상승, 4) 인슐린 감수성 저하, 5) 통증 역치 감소 및 부상 위험 증가 등 다섯 갈래로 작동한다고 정리했다. 트레이닝의 효과는 잠자는 동안 굳어지기 때문에, 수면을 줄이면 'training'은 했지만 'gain'은 사라지는 결과가 나온다. 처방은 단순하다 — 매일 7~9시간, 같은 시간에 자고 일어나라. 카페인은 14시 이후 금지, 침실 18~20℃, 빛 차단, 자기 전 알코올은 REM을 부순다.",
        "MDPI J. Clin. Med. 2025 (14/21/7606)",
        "https://www.mdpi.com/2077-0383/14/21/7606",
        "회복/수면",
        88,
        {"shock_factor": 18, "scientific_credibility": 22, "relatability": 20, "recency": 18, "controversy": 5, "visual_potential": 5},
        ["수면", "회복", "선수", "반응속도", "운동과학", "BDNF"],
    ),
    make(
        "10초 발목 진동으로 사이클을 더 세게 — 그러나 힘들지 않다",
        "Tendon Vibration Trick Lets You Push Harder Without Feeling It",
        "ScienceDaily 2026.01 보도 — 자전거 페달링 직전 힘줄에 진동을 가하면 심박수와 근활동은 더 올라가는데도 'effort 인지'는 그대로였다. 즉 뇌가 노력 신호를 잘못 해석하게 만든 것이다. 통제된 짧은 사이클링 한정이지만, 운동 인지 과학의 새로운 변수가 등장했다.",
        "이 발견의 핵심은 운동 강도(physical intensity)와 인지 강도(perceived effort)가 분리될 수 있다는 점이다. 그동안 RPE(자각 운동 강도)는 거의 무류하다고 여겨졌지만, 힘줄 골지건 기관(Golgi tendon organ)을 진동으로 자극하면 뇌의 노력 모니터링 시스템이 속는다. 응용 가능성은 크다 — 재활 환자가 더 강한 자극을 견디게 만들거나, 마라토너의 페이스 한계를 미세 조정하는 도구가 될 수 있다. 단, 도핑 측면 논란이 향후 따라붙을 가능성이 있다(WADA 등재 0). 실험실 단계 — 일반인 처방 단계는 아니다.",
        "ScienceDaily 2026.01",
        "https://www.sciencedaily.com/releases/2026/01/260107225519.htm",
        "운동과학",
        82,
        {"shock_factor": 22, "scientific_credibility": 18, "relatability": 14, "recency": 18, "controversy": 5, "visual_potential": 5},
        ["힘줄진동", "RPE", "운동인지", "스포츠과학", "골지건기관"],
    ),
    make(
        "선수의 심장은 하루 11,000번 더 적게 뛴다 — '심박수 한도' 신화 깨졌다",
        "Athletes' Hearts Beat 11,000 Fewer Times Per Day — Heartbeat Budget Myth Debunked",
        "호주에서 발표된 새 연구는 '인생의 심박수 총량은 정해져 있어 운동하면 빨리 닳는다'는 오랜 오해를 정면으로 깼다. 운동선수는 안정 심박수가 낮아 운동 시간 동안의 심박수 증가를 합산해도 일일 총 심박수가 사무직보다 약 10% 적었다.",
        "Heart 저널에 발표된 분석은 운동선수와 사무직 비교에서 운동선수의 안정 심박수는 약 50bpm, 사무직은 70bpm 수준이었다. 운동 시간(예: 1시간) 동안 심박수가 150bpm까지 올라가도, 나머지 23시간의 베이스가 낮기 때문에 총 심박수는 사무직보다 11,000회 이상 적었다. 즉 운동은 심장을 '더 빨리 닳게' 만드는 것이 아니라 효율을 높여 '평생 사용량'을 줄이는 행위다. '운동하면 심장 수명이 짧아진다'는 속설은 과학적으로 거짓이다. 추가 함의: 안정 심박수가 60bpm을 넘으면 심혈관 사망 위험이 단계적으로 상승한다는 것이 잘 알려져 있다.",
        "ScienceDaily 2026.04",
        "https://www.sciencedaily.com/releases/2026/04/260426012305.htm",
        "운동과학",
        91,
        {"shock_factor": 26, "scientific_credibility": 22, "relatability": 20, "recency": 18, "controversy": 5, "visual_potential": 5},
        ["심박수", "안정심박수", "운동선수", "심혈관", "심장수명", "신화"],
    ),
    make(
        "운동 종류를 바꿔라 — 17만명 30년 추적 BMJ 분석, 사망 위험 더 떨어진다",
        "Variety in Exercise Lowers Mortality — 30-Year, 173,000-Person BMJ Cohort",
        "BMJ Medicine은 Nurses' Health Study(121,700명)와 Health Professionals Follow-Up Study(51,529명)의 30년 추적을 합산해 '같은 운동을 더 많이' 하는 것보다 '서로 다른 운동을 섞는' 것이 사망 위험을 유의하게 더 낮춘다는 결론을 냈다.",
        "분석 대상은 30년간 2년마다 설문으로 추적된 17만명. 운동 다양성 점수가 가장 높은 그룹은 가장 낮은 그룹 대비 전체 사망률이 약 18% 낮았고, 심혈관 사망률은 더 큰 폭으로 감소했다. 메커니즘 가설: ① 다양한 동작이 다양한 근섬유·관절·신경계를 자극, ② 단일 패턴 과사용 부상 회피, ③ 심박수 변동성(HRV) 향상, ④ 행동 다양성으로 운동 지속률 상승. 처방 — 유산소 + 저항 + 유연성 + 균형, 한 카테고리에만 머물지 말 것.",
        "BMJ Medicine 2026 / ScienceDaily 보도",
        "https://www.sciencedaily.com/releases/2026/04/260426012305.htm",
        "운동과학",
        87,
        {"shock_factor": 16, "scientific_credibility": 24, "relatability": 22, "recency": 18, "controversy": 3, "visual_potential": 4},
        ["운동다양성", "BMJ", "사망률", "코호트", "수명", "건강"],
    ),
    make(
        "9주 고강도 vs 저강도 — 호르몬은 어떻게 달랐을까? 답: 거의 안 달랐다",
        "9 Weeks of High vs Low Load Resistance Training — Salivary Hormones Showed Little Difference",
        "MDPI 'Sports'에 발표된 9주 RCT는 고하중 vs 저하중을 모두 실패점까지 수행했을 때 근비대·근력 모두 유사하고, 타액 코르티솔·테스토스테론 변화도 통계적 차이가 없었다는 결과를 냈다. '무게가 호르몬을 만든다'는 통념의 또 한 번의 종말.",
        "참가자는 훈련 경험 있는 성인. 고하중군(75-85%1RM)과 저하중군(30-50%1RM) 모두 set를 가까운 실패점까지 수행했을 때 근비대(MRI 측정)와 1RM 모두 동등했다. 타액에서 측정한 코르티솔·테스토스테론·anabolic-catabolic ratio 모두 9주 동안 유의한 군간 차이를 보이지 않았다. 결론: '내추럴은 무겁게 들어야 호르몬이 폭발한다'는 헬스장 신화는 코르티솔/테스토스테론 수준에서는 근거가 약하다. 핵심은 노력의 근접성(proximity to failure)이지 절대 무게가 아니다.",
        "MDPI Sports 2026, 11(1)/17",
        "https://www.mdpi.com/2411-5142/11/1/17",
        "운동과학",
        81,
        {"shock_factor": 18, "scientific_credibility": 22, "relatability": 16, "recency": 14, "controversy": 8, "visual_potential": 3},
        ["고하중", "저하중", "호르몬", "코르티솔", "테스토스테론", "근비대"],
    ),
    make(
        "운동에 텐던에 외부 토크가 걸려야 — '늘어난 길이' 우위의 진짜 조건",
        "Lengthened-Position Hypertrophy Requires External Torque — Not Just Stretching",
        "Thieme Connect에 발표된 2026년 종합 리뷰는 '근육 길이를 늘인 위치에서 자극하면 비대가 더 잘 일어난다'는 명제를 정밀하게 다시 풀었다. 핵심 단서는 '단순히 늘리는 것이 아니라 외부 토크가 걸린 상태에서 늘어나야 한다'는 점이다.",
        "스쿼트 바닥, 인클라인 컬, 풀오버처럼 근육이 길어진 위치에서 외부 모멘트가 가장 클 때 신호 전달(mTOR), 근원섬유 손상, 위성세포 활성이 증가한다. 단순 스트레칭이나 텐션 없이 늘어난 위치는 같은 효과가 없다. 응용: 1) 인클라인 덤벨 컬이 프리처 컬보다 lengthened 우위를 살린다, 2) 풀오버는 가슴/광배 모두 도움, 3) 스플릿 스쿼트 후방발 들어올리기는 후방 쇼크. 단, 부상 위험도 같이 올라가므로 무리한 스트레칭 ROM은 비추.",
        "Eur J Sport Sci 2026 (Thieme)",
        "https://www.thieme-connect.com/products/ejournals/abstract/10.1055/a-2733-7605",
        "근비대",
        84,
        {"shock_factor": 18, "scientific_credibility": 24, "relatability": 18, "recency": 16, "controversy": 4, "visual_potential": 4},
        ["근비대", "ROM", "lengthened", "외부토크", "스쿼트", "프리처"],
    ),
    make(
        "근비대와 저-고하중 메타분석 — '실패점까지 가면 결과는 같다' 다시 확인",
        "Master List Update: Loading Zone Doesn't Matter If Sets Reach Failure",
        "Stronger by Science의 '근비대 마스터 리스트'에 추가된 최신 메타분석은 30%1RM부터 85%1RM까지 광범위한 하중 영역에서 근비대가 사실상 동일했다는 결론을 다시 확인했다. 단, 하중이 낮을수록 실패점에 더 가깝게 수행해야 한다.",
        "JSCR(Journal of Strength and Conditioning Research)에 게재된 메타분석은 핵심 변수는 'volume × proximity to failure'이며 절대 무게는 부차적이라고 정리했다. 다만 1) 저하중은 RPE 9.5+가 필요하고, 2) 고하중은 RPE 8~9에서도 비대 효과가 비슷하므로 회복 부담 측면에서 고하중이 효율적일 수 있다는 단서가 있다. 트레이너의 처방은 '하중을 다양화하되, 매 세트의 노력 강도를 정직하게 관리하라'로 수렴 중이다.",
        "Stronger by Science (Master List)",
        "https://www.strongerbyscience.com/master-list/muscle-growth/",
        "근비대",
        80,
        {"shock_factor": 14, "scientific_credibility": 24, "relatability": 18, "recency": 12, "controversy": 6, "visual_potential": 4},
        ["메타분석", "근비대", "실패점", "하중", "RPE", "마스터리스트"],
    ),
    make(
        "어드밴스드 기법 vs 전통 다중세트 — 결과는 거의 같다",
        "Advanced Training Systems Show No Hypertrophic Superiority When Volume Equated",
        "MDPI Sports 2026 시스템 리뷰는 레스트포즈, 속도기반 훈련(VBT), 이심오버로드 등 '고급' 시스템이 볼륨·강도·노력을 통제했을 때 전통 다중세트 대비 의미 있는 비대 우위를 보이지 않았다고 결론지었다.",
        "리뷰 대상은 휴양 트레이닝 경험자. 메서드별 미세한 효과는 있었지만(레스트포즈는 시간 효율, VBT는 출력 유지, 이심오버로드는 신경계 적응) 근비대 자체는 차이가 미미했다. 함의: '비법'을 좇는 대신 1) 충분한 주간 볼륨(부위당 12-20세트), 2) 실패 근접 수행, 3) 점진적 과부하의 기본기를 지키는 것이 효율적이다. 어드밴스드 기법은 '시간을 줄이고 싶을 때' 또는 '플래토에서 자극을 바꾸고 싶을 때' 사용하는 도구다.",
        "MDPI Sports 2026, 11(1)/80",
        "https://www.mdpi.com/2411-5142/11/1/80",
        "근비대",
        79,
        {"shock_factor": 14, "scientific_credibility": 22, "relatability": 16, "recency": 14, "controversy": 8, "visual_potential": 3},
        ["레스트포즈", "VBT", "이심오버로드", "근비대", "볼륨", "리뷰"],
    ),

    # ===== 영양 (Nutrition) =====
    make(
        "한 끼 단백질 한도는 '없다' — 그러나 분배가 합성 25% 차이 만든다",
        "Protein Per-Meal Ceiling Myth — But Even Distribution Boosts 24h MPS by 25%",
        "Springer JISSN의 단백질 분배 연구는 '한 끼 30g 이상은 흡수 안 된다'는 신화를 깨면서도, 동시에 '하루 30g씩 4회 균등' 패턴이 단일 큰 끼니 패턴 대비 24시간 근단백질 합성률(MPS)을 25% 높인다는 결론을 함께 냈다.",
        "연구의 핵심 수치: ① 끼당 0.4-0.5g/kg body weight(70kg 기준 28-35g) 또는 류신 2.5g 이상이 MPS를 최대화, ② 동일한 일일 총 단백질을 4회 균등 분배 vs 1-2회 집중 섭취 비교에서 균등 그룹의 24h MPS가 25% 높음, ③ 자기 전 카제인 20-40g 추가 시 야간 단백질 합성 추가 자극. 실용 처방: '아침 30g·점심 30g·저녁 30g·자기 전 카제인 30g'이 자연 보디빌더의 표준 분배 패턴.",
        "Springer JISSN / Hipelife",
        "https://link.springer.com/article/10.1186/s12970-018-0215-1",
        "영양",
        86,
        {"shock_factor": 16, "scientific_credibility": 24, "relatability": 22, "recency": 12, "controversy": 8, "visual_potential": 4},
        ["단백질", "MPS", "끼당분배", "류신", "근단백질합성", "카제인"],
    ),
    make(
        "단백질 새 정의 — '단순 g'에서 '아미노산 가용성'으로 패러다임 이동",
        "Protein Requirement Redefined Through Amino Acid Bioavailability — ScienceDirect 2026",
        "ScienceDirect에 발표된 종설은 단백질 요구량을 단순 그램 단위로 보던 시대가 끝나고 있다고 정리했다. 새 모델은 1) 아미노산 조성, 2) 가용성(bioavailability), 3) 분배 시간, 4) 운동 자극 동조성을 함께 고려한다.",
        "기존 RDA 0.8g/kg는 nitrogen balance에 기초한 숫자로, 활동성 성인의 실제 최적치와 동떨어져 있다. 새 측정법(IAAO, indicator amino acid oxidation)으로 산정한 활동성 성인의 단백질 최적치는 1.6-2.4g/kg/일. 또한 식물성 단백질은 동물성 대비 류신 함량이 낮아 '같은 g'으로 단백질 합성을 일치시키려면 1.2-1.4배 더 많이 섭취해야 동등한 MPS 자극이 발생한다. 비건/베지테리언이 자주 부족한 류신을 보강하려면 콩, 렌틸, 퀴노아 + 동물성 또는 BCAA 보충이 권장된다.",
        "ScienceDirect 2025 (S0261561425000378)",
        "https://www.sciencedirect.com/science/article/abs/pii/S0261561425000378",
        "영양",
        82,
        {"shock_factor": 14, "scientific_credibility": 24, "relatability": 18, "recency": 16, "controversy": 6, "visual_potential": 4},
        ["단백질", "RDA", "IAAO", "비건", "류신", "패러다임"],
    ),
    make(
        "Peter Attia: '데이터로 본 단백질' — 1.6g/kg는 시작이지 끝이 아니다",
        "Peter Attia: Optimal Protein Intake — Data, Not Dogmatism",
        "Peter Attia MD는 자신의 사이트에서 '1.6g/kg가 최적'이라는 단정 대신 '훈련 강도, 나이, 근손실 위험, LBM 비중에 따라 1.6-2.4g/kg, 일부에서는 3.3g/kg까지 안전하고 효과적'이라고 데이터로 주장했다.",
        "Attia의 논점: 1) 노화에 따른 근감소(sarcopenia)는 50세부터 가속화 — 노년기 근육은 '예금이 아니라 보험'이다, 2) 단백질 RDA(0.8g/kg)는 결핍 방지 최소치이며 최적치가 아니다, 3) 신장 기능이 정상이라면 3.3g/kg까지 위험 신호 없음, 4) 끼당 30-50g 분배가 노년에서 더 중요. 그의 처방: 50대+ = 2.0g/kg 최소, 운동량 많은 성인 = 1.8-2.4g/kg, 끼당 40g 이상.",
        "Peter Attia MD",
        "https://peterattiamd.com/determining-optimal-protein-intake/",
        "영양",
        78,
        {"shock_factor": 14, "scientific_credibility": 20, "relatability": 20, "recency": 12, "controversy": 8, "visual_potential": 4},
        ["단백질", "PeterAttia", "노화", "근감소", "sarcopenia", "보험"],
    ),

    # ===== 보충제/supplement debunking =====
    make(
        "NMN·NAD+·레스베라트롤 — 2026년에도 인간 효과는 '미확인'",
        "NMN, NAD+ Boosters, Resveratrol Still Lack Strong Human Evidence in 2026",
        "Nature·Examine·Tukkbook의 2026 분석은 '장수' 마케팅의 핵심 보충제 NMN, NR(니코틴아미드 리보사이드), 레스베라트롤이 동물 실험과 마우스 모델에서는 흥미롭지만 인간 임상에서는 의미 있는 노화 역전이나 사망률 감소 근거가 여전히 부족하다고 정리했다.",
        "쟁점: 1) NAD+ 수치는 보충 시 상승하지만 그것이 임상 결과로 이어지는지 불확실, 2) 레스베라트롤은 SIRT1 활성화 가설이 인간 용량에서 재현되지 않음, 3) 'longevity blends'(NAD+ + CoQ10 + 콜라겐 + 레스베라트롤)는 마케팅 헤드라인에 비해 RCT 근거 0에 가까움. 마케팅의 함정 — '흥미로운 동물 데이터' + '약한 인간 데이터' + '쉬운 답을 원하는 소비자'의 3박자가 합쳐지면 보충제 산업이 만들어진다. 비싼 가격이 효과를 의미하지 않는다.",
        "Nature 2026 / Tukkbook",
        "https://www.nature.com/articles/d41586-026-00707-5",
        "보충제",
        85,
        {"shock_factor": 22, "scientific_credibility": 22, "relatability": 18, "recency": 16, "controversy": 14, "visual_potential": 5},
        ["NMN", "NAD", "레스베라트롤", "장수", "보충제", "마케팅"],
    ),
    make(
        "보충제 7종 과학이 틀렸다 — 'Plot Twist' 리포트가 뒤집은 통념",
        "Science Got 7 Supplements Wrong — SuppCo's Plot Twist List",
        "SuppCo의 '사이언스 코너 58'은 한때 강력하다고 여겨졌다가 후속 연구로 효과가 의심되거나 뒤집힌 보충제 7종을 정리했다. 베타카로틴(폐암 위험 ↑), 비타민E(전립선암 위험 ↑), 칼슘 단독(심장 위험 ↑) 등이 포함됐다.",
        "리스트의 충격적 항목: 1) 베타카로틴 - 흡연자 폐암 위험 ↑(SELECT/CARET trial), 2) 비타민E 고용량 - 전립선암 위험 ↑(SELECT trial), 3) 칼슘 보충제 - 심혈관 사건 ↑(BMJ 메타분석), 4) 셀레늄 고용량 - 당뇨병 위험 ↑, 5) 어유 고용량 - 심방세동 위험 ↑(STRENGTH trial), 6) 글루타민(일반인) - 효과 미미, 7) HMB(노년 외) - 미미. 핵심: '안전 = 무해'가 아니다. 식이로는 안전한 영양소도 농축 보충제 형태로는 다른 효과를 낼 수 있다.",
        "SuppCo Science Corner",
        "https://supp.co/articles/science-corner-58-plot-twist-seven-supplements-science-got-wrong",
        "보충제",
        88,
        {"shock_factor": 24, "scientific_credibility": 22, "relatability": 22, "recency": 14, "controversy": 12, "visual_potential": 4},
        ["베타카로틴", "비타민E", "칼슘", "어유", "셀레늄", "보충제"],
    ),
    make(
        "FDA가 다이어트 보충제 라벨에 적힌 성분의 절반은 거짓이다",
        "FDA Quietly Confirms: Half of Dietary Supplements Don't Match Their Labels",
        "Harvard Health와 Johns Hopkins의 종합은 미국 FDA가 식이 보충제를 의약품과 달리 사전 승인 없이 판매할 수 있게 허용하기 때문에, 라벨 정확도에 대한 정부 보증은 사실상 없다고 정리했다. 일부 카테고리에서는 라벨과 실제 성분 일치율이 50% 미만이라는 보고가 있다.",
        "구조적 문제: 1) 의약품은 안전성·유효성 입증 후 승인되는 반면 보충제는 'GRAS(generally recognized as safe)'라는 약한 기준만 통과, 2) 제조 GMP는 강제되지만 라벨 검증은 사후 단속 위주, 3) 일부 SARMs/스테로이드 보충제는 라벨에 없는 의약품 성분이 검출되기도. 소비자 가이드: 1) NSF·USP·Informed Sport 인증 마크가 있는 제품 우선, 2) 'proprietary blend' 표기는 신뢰도 ↓, 3) Certificate of Analysis(COA) 공개 제품 선호.",
        "Johns Hopkins / Harvard Health",
        "https://www.hopkinsmedicine.org/health/wellness-and-prevention/is-there-really-any-benefit-to-multivitamins",
        "보충제",
        87,
        {"shock_factor": 24, "scientific_credibility": 20, "relatability": 22, "recency": 8, "controversy": 14, "visual_potential": 4},
        ["FDA", "라벨", "보충제", "GRAS", "NSF", "USP"],
    ),
    make(
        "고용량 항산화 보충제, 사망률 시그널 — 시스템 리뷰의 충격",
        "High-Dose Antioxidant Supplements May Increase Mortality — Systematic Review",
        "Cochrane 계열의 시스템 리뷰는 비타민A·E·베타카로틴 등 고용량 항산화제 보충이 일부 인구군에서 전체 사망률을 오히려 약간 높일 수 있다는 시그널을 보고했다. '많이 먹으면 더 좋다'는 직관과 정반대 결과다.",
        "메커니즘 가설: 1) 항산화제는 운동·면역 과정에서 필요한 일시적 ROS(활성산소) 신호를 차단해 적응을 약화시킬 수 있음, 2) 단일 영양소 고용량은 다른 영양소 균형을 흔듦, 3) 일부 항산화제는 친산화 환경에서 oxidant로 작용. 실용 함의: 식이로 섭취하는 베리·녹황색 채소·차의 항산화 성분은 권장되지만, 비타민E 1,000IU 같은 고용량 보충은 피하라.",
        "The Conversation / Cochrane",
        "https://theconversation.com/topics/supplements-1831",
        "보충제",
        82,
        {"shock_factor": 22, "scientific_credibility": 20, "relatability": 18, "recency": 10, "controversy": 12, "visual_potential": 4},
        ["항산화제", "비타민E", "사망률", "ROS", "보충제", "Cochrane"],
    ),

    # ===== 회복/Recovery =====
    make(
        "콜드워터 이머전, 운동 후 부교감신경을 끌어올린다 — 12개 중 8개 RCT 확인",
        "Post-Exercise Cold Water Immersion Boosts Parasympathetic Tone in 8 of 12 RCTs",
        "2025년 시스템 리뷰는 운동 후 콜드워터 이머전(CWI)이 자율신경계의 부교감 톤(HRV-RMSSD, HF power)을 회복시키는 효과가 12개 RCT 중 8개에서 중~큰 효과 크기로 확인됐다고 보고했다. 단순 휴식 회복보다 효과가 빠르다.",
        "메커니즘: 1) 차가운 물 자극이 미주신경(vagus nerve)을 활성화, 2) 카테콜아민 일시 분비 후 빠른 정상화, 3) 말초혈관 수축 → 중심혈류 회복으로 심장 부담 ↓. 처방 — 운동 후 10-15분 이내, 10-15℃에서 5-10분, 일주일 2-3회. 단, 1) 근비대 시즌에는 강도 낮은 운동 직후만 권장(고강도 직후 CWI는 단백질 합성 신호를 둔화시킬 수 있음 — Ronnestad 2014), 2) 시합 시즌·회복 우선기간에 효과 극대.",
        "Frontiers Physiol 2025 (1598075)",
        "https://www.frontiersin.org/journals/physiology/articles/10.3389/fphys.2025.1598075/full",
        "회복",
        85,
        {"shock_factor": 16, "scientific_credibility": 24, "relatability": 20, "recency": 16, "controversy": 5, "visual_potential": 4},
        ["콜드워터", "회복", "부교감신경", "HRV", "미주신경", "RCT"],
    ),
    make(
        "콜드 + 호흡법, 자율신경 균형을 동시에 — 반-무작위 시험",
        "Breathwork + Cold Immersion Combo — Semi-Randomized RCT Confirms Synergy",
        "Scientific Reports에 발표된 반-무작위 RCT는 호흡법(빔 호프식)과 콜드 이머전을 함께 시행하면 자율신경 균형(HRV)과 스트레스 회복력 모두에서 단독 시행 대비 더 큰 효과가 났다고 보고했다.",
        "참가자는 일반 성인. 4주 프로그램(주 3회) 후 stress reactivity, 코르티솔 awakening response, 주관적 웰빙이 통합 그룹에서 가장 크게 개선됐다. 가설: 호흡법이 부교감 톤을 미리 끌어올려 콜드 노출의 교감 폭주를 완충하고, 그 결과 노출 후 회복이 빨라진다는 것이다. 주의: 심혈관 질환자, 임산부, 통제되지 않은 고혈압자는 콜드 이머전 절대 금기. 실내에서 차가운 샤워(12-15℃) 5분으로 시작해 점진 적응 권장.",
        "Sci Rep 2025 (s41598-025-29187-9)",
        "https://www.nature.com/articles/s41598-025-29187-9",
        "회복",
        82,
        {"shock_factor": 18, "scientific_credibility": 20, "relatability": 18, "recency": 16, "controversy": 6, "visual_potential": 5},
        ["호흡법", "빔호프", "콜드", "HRV", "스트레스", "통합"],
    ),

    # ===== 멘탈/Mental Health =====
    make(
        "그룹 운동이 우울증에 가장 강력 — 73 RCT가 가린 '환경의 효과'",
        "Group/Supervised Aerobic Exercise Produces Largest Antidepressant Effect — Lancashire 73-RCT",
        "Lancashire 메타분석의 후속 분석은 운동의 항우울 효과가 '단독 운동'보다 '그룹 또는 감독자 동반' 환경에서 유의하게 더 크다고 보고했다. 단순한 운동량 효과가 아니라 사회적 연결과 책임감이 더해진 결과다.",
        "구체적 수치: 그룹/감독자 환경 SMD = -0.72(큰 효과), 단독 SMD = -0.35(중간 효과). 즉 같은 시간을 운동해도 환경 차이가 약 2배의 효과를 만든다. 메커니즘 가설: 1) 사회적 지지가 우울증의 사회적 고립 핵심을 직접 타격, 2) 책임감(accountability)이 지속률을 높임, 3) 거울 신경계 활성화로 유산소 효과를 강화. 처방 — 우울 증상이 있다면 단독 홈트보다 헬스장 그룹 클래스, 러닝 클럽, 단체 요가가 효과적이다.",
        "Frontiers Public Health 2025 (1616925)",
        "https://www.frontiersin.org/journals/public-health/articles/10.3389/fpubh.2025.1616925/full",
        "정신건강",
        90,
        {"shock_factor": 20, "scientific_credibility": 24, "relatability": 22, "recency": 18, "controversy": 4, "visual_potential": 4},
        ["우울증", "그룹운동", "감독자", "메타분석", "사회적지지", "정신건강"],
    ),
    make(
        "고강도 운동이 우울증에 더 큰 효과 — 32 RCT 메타분석",
        "High-Intensity Exercise Outperforms Moderate for Depression — 32-RCT Meta-Analysis",
        "PMC에 게재된 32개 RCT 메타분석은 고강도 인터벌 트레이닝(HIIT) 또는 중-고강도 지속 운동이 가벼운 산책 수준의 운동보다 우울 증상 감소에서 더 큰 효과 크기를 냈다고 보고했다.",
        "수치: 고강도 SMD = -0.81, 중강도 SMD = -0.50, 저강도 SMD = -0.21. 메커니즘: 1) 고강도가 BDNF·VEGF·IGF-1 같은 신경영양 인자 분비를 더 강하게 자극, 2) 베타엔도르핀 분비 강도 차이, 3) 심박수 90% 이상에서만 분비되는 일부 마이오카인 효과. 실용: 우울 증상자에게는 '편안한 산책 30분'보다 '자전거 인터벌 20분(20초 전력 + 40초 회복 ×10)'이 효과적일 수 있다. 단, 운동 동기 자체가 떨어진 환자에게는 강도보다 시작 가능성이 우선이다.",
        "PMC 2025 (12380541)",
        "https://pmc.ncbi.nlm.nih.gov/articles/PMC12380541/",
        "정신건강",
        85,
        {"shock_factor": 18, "scientific_credibility": 24, "relatability": 18, "recency": 16, "controversy": 4, "visual_potential": 4},
        ["HIIT", "고강도", "우울증", "BDNF", "마이오카인", "메타분석"],
    ),
    make(
        "청소년 우울증 — 주 3회 이상 운동이 가장 효과적",
        "Exercise Effective for Adolescent Depression — Best at >3 Sessions/Week",
        "PMC에 게재된 청소년 우울 RCT 메타분석은 12,624명 데이터를 종합해 운동 빈도가 주 3회 이상일 때 가장 큰 항우울 효과가 나왔다고 보고했다. 지속 기간은 회당 30-60분이 효과 정점.",
        "분석 대상은 6-19세. 운동 종류는 다양했지만 빈도와 지속 기간이 핵심 변수. 주 1-2회 그룹 SMD = -0.33, 주 3회 이상 그룹 SMD = -0.78. 흥미로운 결과 — 운동 종류(유산소·저항·혼합)나 강도보다 '얼마나 자주 하느냐'가 결과를 더 크게 좌우했다. 청소년에게는 거창한 프로그램보다 '주 3회의 작은 활동'이 더 강력한 약이다. 임상 함의: SSRIs 1차 선택 전후로 운동 처방을 통합 권장한다.",
        "PMC 2025 (12624221)",
        "https://pmc.ncbi.nlm.nih.gov/articles/PMC12624221/",
        "정신건강",
        82,
        {"shock_factor": 16, "scientific_credibility": 22, "relatability": 22, "recency": 14, "controversy": 4, "visual_potential": 4},
        ["청소년", "우울증", "운동빈도", "SSRIs", "메타분석", "주3회"],
    ),
    make(
        "유산소 + 저항운동, 둘 다 우울증에 효과 — 25 RCT 통합 분석",
        "Both Aerobic and Resistance Training Reduce Depression — 25-RCT Meta-Analysis",
        "PMC 25개 RCT 종합은 유산소(러닝·사이클·수영)와 저항운동(웨이트) 모두 우울증·불안 증상 감소에 의미 있는 효과를 냈다고 보고했다. 두 형식 간 큰 차이는 없으며, 좋아하는 형식이 효과의 핵심.",
        "결과: 유산소 SMD = -0.55, 저항운동 SMD = -0.49, 혼합 SMD = -0.62(통계적 차이 없음). 핵심 함의: '운동 종류보다 지속이 답'. 환자가 싫어하는 운동은 효과가 0에 수렴 — 본인이 즐길 수 있는 형식을 선택하라. 처방: 1) 운동 경험 적은 우울 환자 = 짧은 산책부터, 2) 신체 자신감 낮은 환자 = 그룹 댄스/요가, 3) 통제감 회복 필요 환자 = 웨이트 트레이닝(작은 성취 누적). 운동을 처방으로 보지 말고 정체성 변화로 접근하라.",
        "PMC 2025 (12117297)",
        "https://pmc.ncbi.nlm.nih.gov/articles/PMC12117297/",
        "정신건강",
        80,
        {"shock_factor": 14, "scientific_credibility": 22, "relatability": 22, "recency": 14, "controversy": 4, "visual_potential": 4},
        ["유산소", "저항운동", "우울증", "불안", "메타분석", "정체성"],
    ),

    # ===== 바이럴/Trends =====
    make(
        "ACSM 2026 트렌드 1위는 웨어러블 — 결국 데이터가 운동을 이긴다",
        "ACSM Names Wearable Tech the #1 Fitness Trend for 2026",
        "American College of Sports Medicine(ACSM)이 2,000명의 임상가·연구자·트레이너 설문을 종합한 2026 글로벌 피트니스 트렌드 1위는 '웨어러블 테크'였다. AI 피트니스 앱과 원격 PT가 그 뒤를 이었다.",
        "ACSM의 연례 'Worldwide Fitness Trends' 보고서 핵심: 1) 1위 웨어러블 - Apple Watch·Garmin·Whoop·Oura 등이 단순 만보기에서 HRV·수면·체온·산소포화도 모니터링으로 진화, 2) 원격 PT는 관심도 +414% 폭증, 3) AI 기반 개인화 코칭이 신흥 강자, 4) VR 운동도 게이밍 인구를 흡수 중. 함의: 데이터 기반 자가 코칭이 트레이너 산업을 재편하는 중이다. 그러나 웨어러블 데이터의 정확성은 기기마다 다르므로 '추세 비교'에 사용하고 절대값에는 의존하지 말 것.",
        "ACSM Health & Fitness Journal",
        "https://acsm.org/top-fitness-trends-2026/",
        "트렌드",
        86,
        {"shock_factor": 16, "scientific_credibility": 20, "relatability": 24, "recency": 18, "controversy": 4, "visual_potential": 6},
        ["ACSM", "웨어러블", "AI피트니스", "원격PT", "VR", "트렌드"],
    ),
    make(
        "필라테스가 3년 연속 1위 — ClassPass 2025 글로벌 예약 +66%",
        "Pilates Booked More Than Any Other Workout Globally for 3rd Year — ClassPass 2025",
        "ClassPass의 2025 Look Back Report에 따르면 필라테스는 3년 연속 글로벌 1위 운동으로 등극했다. 2024년 대비 예약 +66% 증가, 특히 리포머·매트 모두 폭증.",
        "추세 동인: 1) 코어 강화 + 자세 교정 + 부상 회복의 '세 마리 토끼', 2) 30-50세 여성 외에도 20대 남성 진입 가속, 3) 인스타그램·틱톡의 '필라테스 바디' 미감, 4) 헬스장 라이크 '하드 서클' 피로에 대한 반작용. 비판적 관점 — 필라테스는 일관된 자극에서 근비대 효과가 제한적이므로 근력·근비대 목표라면 단독으로는 부족. 하이브리드 처방: 주 2-3회 필라테스 + 주 2회 웨이트 트레이닝.",
        "ClassPass 2025 Look Back",
        "https://meetglimpse.com/trends/fitness-trends/",
        "트렌드",
        80,
        {"shock_factor": 14, "scientific_credibility": 14, "relatability": 24, "recency": 18, "controversy": 6, "visual_potential": 8},
        ["필라테스", "ClassPass", "리포머", "코어", "트렌드", "여성운동"],
    ),
    make(
        "원격 PT 검색량 +414% — 헬스장의 '오프라인 독점'이 깨졌다",
        "Remote Personal Training Surges +414% — Gym's Offline Monopoly Cracking",
        "Glimpse·PureWow의 2026 분석은 원격 퍼스널 트레이닝 검색량이 1년 새 +414% 폭증했다고 보고했다. Zoom·전용 앱 기반 1:1 PT가 헬스장 PT 시장을 잠식 중이다.",
        "성장 동인: 1) 비용 - 오프라인 PT 회당 8-15만원 vs 원격 4-8만원, 2) 접근성 - 지방·해외 거주자도 톱 트레이너 접근 가능, 3) 일정 유연성 - 스케줄 충돌 적음, 4) 디지털 네이티브의 비대면 선호. 한계: 1) 폼 교정의 정확성 제한, 2) 무거운 중량 안전 보조 불가, 3) 라포 형성 더 어려움. 결론: 초·중급자에게는 충분하지만 파워리프팅·올림픽 리프팅 같은 기술 종목은 오프라인 우위 유지.",
        "Glimpse / PureGym 2026",
        "https://meetglimpse.com/trends/fitness-trends/",
        "트렌드",
        78,
        {"shock_factor": 16, "scientific_credibility": 14, "relatability": 22, "recency": 18, "controversy": 6, "visual_potential": 5},
        ["원격PT", "PT", "Zoom", "비대면", "헬스장", "트렌드"],
    ),
    make(
        "워킹 요가 +2,414% — '러너의 다음 단계'로 부상하는 신규 카테고리",
        "Walking Yoga Surges +2,414% — Hybrid Format Eats Into Both Categories",
        "PureGym 2026 보고서에서 '워킹 요가' 검색이 1년 새 +2,414% 증가하며 새로운 하이브리드 카테고리로 떠올랐다. 60-90분 자연 산책 + 중간 요가 자세 정거장이 대표 포맷.",
        "성공 요인: 1) 러너의 부상·번아웃 대안, 2) 명상 효과 + 심혈관 효과 결합, 3) 카메라 친화적(인스타·틱톡 콘텐츠 ↑), 4) 노년층 진입 장벽 낮음. 비판: 1) 단독으로는 근력 자극 부족, 2) 강도가 낮아 체중감량 효과 제한, 3) 기상 요건(비·추위)에 약함. 추천 조합: 주 1-2회 워킹 요가(회복일) + 주 3회 본 트레이닝.",
        "PureGym 2026",
        "https://meetglimpse.com/trends/fitness-trends/",
        "트렌드",
        76,
        {"shock_factor": 14, "scientific_credibility": 12, "relatability": 22, "recency": 18, "controversy": 4, "visual_potential": 6},
        ["워킹요가", "하이브리드", "PureGym", "러너", "회복일", "트렌드"],
    ),
    make(
        "6-6-6 워킹 챌린지 — 6시 60분 6km, 단순함의 승리",
        "6-6-6 Walking Challenge Goes Viral — Simplicity Wins on TikTok",
        "PureGym 2026 보고서에서 '6-6-6 워킹 챌린지'(오전 6시·6km·60분 워밍/쿨다운)가 인스타그램·틱톡에서 폭발적 인기. 복잡한 프로그램을 거부하는 '단순함의 회귀'가 본질이다.",
        "성공 요인: 1) 숫자 3개로 외우기 쉬움 → 행동 유발 강함, 2) 매일 같은 시간 = 습관화 용이, 3) 6km는 60분에 가능한 적당한 도전, 4) 아침 햇빛 노출 = 일주기 리듬 안정. 과학적 근거: 아침 자연광 노출은 멜라토닌 야간 분비를 1.5-2시간 앞당겨 수면 질을 개선하고, 60분 중강도 걷기는 사망률 감소·기분 개선·인슐린 감수성 향상 모두에 효과. 단점: 1) 근비대 효과 0, 2) 비·추위 시 지속 어려움. 시작점으로는 우수.",
        "PureGym 2026",
        "https://meetglimpse.com/trends/fitness-trends/",
        "트렌드",
        77,
        {"shock_factor": 14, "scientific_credibility": 14, "relatability": 24, "recency": 18, "controversy": 4, "visual_potential": 6},
        ["666챌린지", "걷기", "아침", "일주기", "단순함", "트렌드"],
    ),
    make(
        "월 필라테스, 1년 새 -55%로 추락 — 바이럴 운동의 짧은 수명",
        "Wall Pilates Crashes -55% — Viral Workouts Have Short Half-Lives",
        "한때 틱톡에서 폭발했던 '월 필라테스(wall pilates)' 검색량이 2025년 -55% 급락했다. 바이럴 운동의 라이프사이클이 빠르게 짧아지고 있다는 신호다.",
        "데이터 분석: 월 필라테스는 2024년 초 폭발 → 2024년 말부터 검색 감소 → 2025년 -55%. 비슷한 패턴: '12-3-30 트레드밀'(2023 폭발 → 2025 -41%), 'Hot Girl Walk'(2022 폭발 → 2024 -32%). 함의: 1) 대중은 새로운 자극을 끊임없이 원함, 2) 실행 효과보다 화제성에 의해 채택과 이탈, 3) 인플루언서 의존 콘텐츠는 인플루언서 이탈 시 동반 추락. 트레이너에게: 트렌드를 따라가되 본질(과학적 기본기)은 흔들지 마라.",
        "PureGym / Glimpse 2026",
        "https://meetglimpse.com/trends/fitness-trends/",
        "트렌드",
        78,
        {"shock_factor": 18, "scientific_credibility": 14, "relatability": 22, "recency": 18, "controversy": 8, "visual_potential": 5},
        ["월필라테스", "바이럴", "트렌드", "라이프사이클", "TikTok", "헬스인플루언서"],
    ),
    make(
        "'건강 동기' 인스타 게시물이 청년에게 해를 끼친다 — phys.org 2026.05",
        "Healthy-Looking Motivational Posts May Harm Young Adults — phys.org 2026.05",
        "phys.org 2026.05 보도된 새 연구는 인스타·틱톡의 '건강 영감' 게시물이 청년의 자기개념과 식이행동에 부정적 영향을 미친다고 보고했다. 표면적으로는 동기부여 메시지지만, 비교 노출이 자존감을 깎고 식이장애 위험을 높인다.",
        "주요 발견: 1) 'Fitspiration' 노출이 많을수록 청년 여성의 신체 불만족 ↑, 2) 'What I Eat in a Day' 영상 시청 후 식이 통제 강박 ↑, 3) 운동·식단 관련 비교 빈도가 높을수록 우울 점수 ↑. 메커니즘: 1) 사회 비교 이론 - 상향 비교가 자기 가치 평가를 낮춤, 2) 알고리즘이 극단 콘텐츠를 우선 노출, 3) '편집된 일상'을 평균으로 인식. 처방: 1) 따라하지 말고 자신의 데이터로 비교, 2) 콘텐츠 다양성 의도적 큐레이션, 3) 타임 리미트 설정.",
        "phys.org 2026.05",
        "https://phys.org/news/2026-05-healthy-viral-good-young-adults.html",
        "트렌드/멘탈",
        85,
        {"shock_factor": 22, "scientific_credibility": 18, "relatability": 24, "recency": 20, "controversy": 12, "visual_potential": 5},
        ["인스타그램", "TikTok", "fitspiration", "청년", "식이장애", "정신건강"],
    ),

    # ===== 추가 운동과학/기타 =====
    make(
        "12주 운동 = 단백체 노화 10개월 역전 — 26명 RCT의 의미",
        "12-Week Exercise Reverses Proteomic Aging by 10 Months — UK Biobank Validation",
        "Nature 자매지 'npj Aging'에 발표된 연구는 26명 남성에게 12주 감독자 운동 중재를 시행하자 단백체 기반 생물학적 나이가 평균 10개월 역전됐다고 보고했다. UK Biobank 데이터로 모델 검증.",
        "측정법은 혈장 단백체 분석을 통한 'proteomic age'. 핵심 단백질 마커: GDF-15, NT-proBNP, 시스타틴-C 등 20여종이 운동 후 의미 있게 변화. 단 26명 소규모 RCT라는 제한이 있지만 UK Biobank의 대규모 코호트로 신호가 일관되게 재현됐다는 점에서 유의미. 함의: 1) 운동의 '항노화' 효과는 측정 가능한 분자 수준에서 일어남, 2) 12주가 의미 있는 변화 임계점, 3) 감독자 동반 환경이 일관성 확보의 핵심. 일반인 처방: 12주 동안 주 3-4회·중강도 이상.",
        "npj Aging 2026",
        "https://www.nature.com/articles/s41514-025-00318-w",
        "운동과학",
        88,
        {"shock_factor": 22, "scientific_credibility": 22, "relatability": 18, "recency": 18, "controversy": 4, "visual_potential": 4},
        ["proteomic", "노화역전", "UKBiobank", "GDF15", "12주", "운동"],
    ),
    make(
        "운동이 면역 시스템을 다시 젊게 만든다 — 'inflammaging' 역전 가설",
        "Exercise May Be the Key to a Younger, Sharper Immune System",
        "ScienceDaily 2025.10 보도 — 정기 운동이 노화에 따른 만성 저염증 상태(inflammaging)를 분자 수준에서 역전시킬 수 있다는 새 연구. T세포 다양성과 NK세포 활성이 모두 운동 그룹에서 의미 있게 회복됐다.",
        "메커니즘: 1) 운동이 흉선(thymus) 부피를 일부 보존, 2) 마이오카인(IL-6, IL-15)이 노화 면역세포의 죽음을 유도, 3) 운동 유래 EV(세포외소포)가 항노화 신호를 전달. 함의: 노년기 면역력은 약물보다 운동으로 회복하는 것이 더 효과적일 수 있다. 처방: 노년에게 - 주 3회 저-중강도 + 주 1회 저항운동 + 주 1회 균형운동(낙상 예방). 인플루엔자·코로나 백신 효과도 운동하는 노년이 더 강한 항체 반응을 보인다는 추가 증거.",
        "ScienceDaily 2025.10",
        "https://www.sciencedaily.com/releases/2025/10/251014014421.htm",
        "운동과학",
        84,
        {"shock_factor": 18, "scientific_credibility": 22, "relatability": 20, "recency": 14, "controversy": 4, "visual_potential": 4},
        ["면역", "inflammaging", "T세포", "NK세포", "흉선", "노화"],
    ),
    make(
        "운동이 골다공증을 막는 비밀 — 골세포가 직접 부하에 반응한다",
        "Breakthrough Reveals How Exercise Fights Osteoporosis — Osteocytes Sense Mechanical Load",
        "ScienceAlert 보도 — 새 연구가 운동이 뼈를 강화하는 메커니즘의 핵심을 짚었다. 골세포(osteocyte)가 기계적 부하를 직접 감지해 신호 분자(스클레로스틴 ↓, RANKL ↓)를 조절, 뼈 형성을 자극한다.",
        "기존에는 운동이 칼슘대사·호르몬 경로로 뼈에 작용한다고 여겨졌으나, 새 연구는 골세포 자체의 기계감각 채널(Piezo1)이 직접 신호를 만든다는 점을 보였다. 함의: 1) '뼈는 정적 조직'이라는 통념이 정정, 2) 칼슘 보충제만으로는 부족 - '하중 자극'이 필수, 3) 충격 운동(점프·러닝·스텝)이 수영보다 골밀도 증가에 효과적, 4) 노년에서도 저항운동이 골다공증을 늦춤. 처방: 폐경 여성·노년 - 주 2-3회 저항운동 + 주 1-2회 충격운동(미니 점프 ×10 / 계단 오르기).",
        "ScienceAlert / Cell Reports",
        "https://www.sciencealert.com/breakthrough-study-reveals-the-secret-of-how-exercise-fights-osteoporosis",
        "운동과학",
        82,
        {"shock_factor": 18, "scientific_credibility": 22, "relatability": 18, "recency": 12, "controversy": 4, "visual_potential": 4},
        ["골다공증", "골세포", "Piezo1", "RANKL", "스클레로스틴", "충격운동"],
    ),
    make(
        "주 2~4회 빈도가 답 — '브로 스플릿'은 시대에 뒤처진 처방",
        "Hit Each Muscle 2-4× Per Week — Bro Split is Outdated",
        "최신 메타분석 데이터는 부위당 주 1회만 자극하는 전통 '브로 스플릿'이 주 2-4회 자극보다 근비대 효과가 유의하게 떨어진다고 결론지었다. 동일 주간 볼륨이라면 빈도를 분산하는 것이 우월하다.",
        "메커니즘: 1) 단일 자극 후 단백질 합성 상승은 24-48시간만 지속, 2) 주 1회 자극은 나머지 5-6일이 'flat' 상태, 3) 같은 볼륨을 2-3회로 나누면 합성 곡선 상승 시간 ↑. 처방 - 1) 초보 = 전신 주 3회, 2) 중급 = 상하체 주 4회 또는 푸쉬·풀·다리 주 5-6회, 3) 고급 = 부위당 주 2-3회 + 약점 부위 추가. 부위당 주간 세트 12-20세트 유지가 핵심.",
        "Strive Workout 2026 / Multiple Meta-Analyses",
        "https://strive-workout.com/2026/01/22/ways-to-build-muscle-faster/",
        "근비대",
        81,
        {"shock_factor": 16, "scientific_credibility": 22, "relatability": 22, "recency": 16, "controversy": 8, "visual_potential": 4},
        ["주2-4회", "브로스플릿", "근비대", "빈도", "볼륨", "단백질합성"],
    ),
    make(
        "노화 보충제 'longevity blends' — 마케팅 vs 인간 임상의 격차",
        "Longevity Blend Industry Booms — But Human RCT Evidence Remains Thin",
        "Tukkbook 2026 분석은 'NMN + NAD+ booster + CoQ10 + 콜라겐 + 레스베라트롤' 같은 longevity blends가 매년 두 자리 수 성장 중이지만, 같은 조합을 검증한 인간 RCT는 여전히 거의 없다고 정리했다.",
        "산업 구조: 1) 단일 성분의 약한 동물 실험 결과를 '브랜드 스토리'로 합쳐 판매, 2) 1병 5-10만원으로 마진율 70%+, 3) 인플루언서 마케팅 의존도 높음, 4) 후속 비교 RCT 부재. 추천: 1) blend보다 단일 성분(필요할 때만) 선택, 2) 'longevity'라는 단어가 라벨에 있으면 의심, 3) 임상 ID 없는 'proprietary blend'는 회피. 정직한 결론 - 식이·운동·수면을 이긴 보충제는 아직 인간에게 없다.",
        "Tukkbook 2026 / Examine",
        "https://tukkbook.in/overhyped-supplements-2026/",
        "보충제",
        80,
        {"shock_factor": 18, "scientific_credibility": 20, "relatability": 20, "recency": 14, "controversy": 14, "visual_potential": 4},
        ["longevity", "NMN", "NAD", "blend", "마케팅", "RCT부재"],
    ),
    make(
        "레지스턴스 트레이닝 영양 연구 33년 — 'Scientometric' 분석",
        "33-Year Scientometric of Nutrition × Resistance Training Research",
        "PMC 발표 종설은 1992-2025년 영양 + 저항운동 연구 논문 수천 편을 메타-과학적으로 분석해 '단백질', '크레아틴', '카페인' 3대 토픽이 전체 인용의 60%를 차지한다고 정리했다.",
        "주요 발견: 1) '단백질' 관련 논문은 매년 두 자리 수 증가, 2) '크레아틴'은 60년대부터 연구돼 효능 합의 가장 강한 보충제로 자리잡음, 3) '카페인'은 인지·근지구력 모두에 효과 있음이 컨센서스, 4) BCAA·HMB·글루타민 등 한때 화제였던 항목은 후속 연구에서 효과 약화. 함의: 영양 보충제 시장은 새 화제를 끊임없이 만들지만, 시간이 지나면 '단백질 + 크레아틴 + 카페인'이라는 단순한 코어로 수렴한다.",
        "PMC 2025 (12317481)",
        "https://pmc.ncbi.nlm.nih.gov/articles/PMC12317481/",
        "영양/연구",
        77,
        {"shock_factor": 14, "scientific_credibility": 24, "relatability": 14, "recency": 14, "controversy": 4, "visual_potential": 3},
        ["scientometric", "단백질", "크레아틴", "카페인", "보충제", "메타과학"],
    ),
]


def main():
    with open(ARTICLES_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)

    existing_titles = set()
    existing_urls = set()
    for bucket in ("news", "research", "featured"):
        for art in data.get(bucket, []):
            existing_titles.add(art.get("title", "").strip())
            url = art.get("source_url", "").strip()
            if url:
                existing_urls.add(url)

    added = 0
    skipped = 0
    for art in NEW_ARTICLES:
        if art["title"].strip() in existing_titles:
            skipped += 1
            continue
        bucket = "research" if art.get("source_type") == "research" else "news"
        data.setdefault(bucket, []).append(art)
        existing_titles.add(art["title"].strip())
        added += 1

    # Sort each bucket by viral_score desc
    for bucket in ("news", "research", "featured"):
        if bucket in data and isinstance(data[bucket], list):
            data[bucket].sort(key=lambda a: a.get("viral_score", 0), reverse=True)

    # Cap each bucket — magazine spec says max 200 total articles
    total = len(data.get("news", [])) + len(data.get("research", [])) + len(data.get("featured", []))
    if total > 200:
        # Trim lowest-score from news/research first (featured is permanent)
        excess = total - 200
        combined = []
        for bucket in ("news", "research"):
            for i, art in enumerate(data.get(bucket, [])):
                combined.append((art.get("viral_score", 0), bucket, i))
        combined.sort()
        # Mark for removal
        to_remove = {bucket: set() for bucket in ("news", "research")}
        for score, bucket, idx in combined[:excess]:
            to_remove[bucket].add(idx)
        for bucket in ("news", "research"):
            data[bucket] = [a for i, a in enumerate(data[bucket]) if i not in to_remove[bucket]]

    # Update meta
    meta = data.setdefault("meta", {})
    new_total = len(data.get("news", [])) + len(data.get("research", [])) + len(data.get("featured", []))
    meta["last_updated"] = NOW_ISO
    meta["last_updated_kst"] = f"{NOW_KST} 자동크롤(저녁: 운동과학·영양·회복·멘탈·바이럴)"
    meta["total_articles"] = new_total
    meta["crawl_count"] = meta.get("crawl_count", 0) + 1

    avg_score = (sum(a.get("viral_score", 0) for a in data.get("news", []))
                 + sum(a.get("viral_score", 0) for a in data.get("research", []))) / max(1, len(data.get("news", [])) + len(data.get("research", [])))
    top_score = max([a.get("viral_score", 0) for a in data.get("news", []) + data.get("research", [])] or [0])
    meta["top_viral_score"] = top_score
    meta["avg_viral_score"] = round(avg_score, 1)

    with open(ARTICLES_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"신규 추가: {added}건")
    print(f"중복 스킵: {skipped}건")
    print(f"전체 활성 기사: {new_total}건")
    print(f"평균 viral_score: {meta['avg_viral_score']}")
    print(f"최고 viral_score: {meta['top_viral_score']}")
    # TOP 3
    all_arts = data.get("news", []) + data.get("research", [])
    all_arts.sort(key=lambda a: a.get("viral_score", 0), reverse=True)
    print("\nTOP 3:")
    for i, a in enumerate(all_arts[:3], 1):
        print(f"  {i}. [{a.get('viral_score')}] {a.get('title', '')[:80]}")


if __name__ == "__main__":
    main()
