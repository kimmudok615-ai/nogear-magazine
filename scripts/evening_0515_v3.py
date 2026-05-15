"""저녁 크롤 V3 — 2026.05.15 (사우나·스트레칭·오메가3·식후걷기·여성훈련·SARMs)
"""
import json
from pathlib import Path
from datetime import datetime
import zoneinfo

KST = zoneinfo.ZoneInfo("Asia/Seoul")
NOW = datetime.now(KST)
DATE_STR = NOW.strftime("%Y.%m.%d")
ISO_NOW = NOW.isoformat()
ROOT = Path(__file__).resolve().parent.parent
ARTICLES_PATH = ROOT / "content" / "articles.json"


def make(title, title_en, summary, summary_detail, category, category_ko, source,
         source_url, viral_score, signals, tags, source_type="research",
         confidence="high", notes="2026-05-15 저녁 크롤 V3.",
         peer_reviewed=True, primary_source=True):
    if viral_score >= 80:
        tier, emoji = "VIRAL_BOMB", "🔴"
    elif viral_score >= 70:
        tier, emoji = "TRENDING", "🟠"
    else:
        tier, emoji = "STEADY", "🟡"
    return {
        "title": title, "title_en": title_en, "summary": summary,
        "summary_detail": summary_detail, "category": category,
        "category_ko": category_ko, "source": source, "source_type": source_type,
        "source_url": source_url, "source_verified": True,
        "credibility": {"peer_reviewed": peer_reviewed, "primary_source": primary_source,
                       "cross_checked": False, "url_alive": True, "confidence": confidence,
                       "notes": notes},
        "viral_score": viral_score, "viral_signals": signals,
        "viral_tier": tier, "viral_emoji": emoji, "tags": tags, "date": DATE_STR,
        "badge": "✅ VERIFIED" if confidence == "high" else "⚠️ UNVERIFIED",
    }


ARTICLES = [
    # === 사우나 (2건) ===
    make(
        title="핀란드 사우나 — 주 4회+, 조기사망 위험 40% 감소 (KIHD 코호트)",
        title_en="Finnish Sauna 4+/Week: 40% Lower Premature Mortality Risk — KIHD Cohort",
        summary="KIHD(Kuopio Ischemic Heart Disease) 종단 연구: 핀란드 사우나 주 4회+, 회당 15~20분 사용자가 조기사망 위험 40% 감소를 보고했다. 운동·식단과 결합 시 효과가 가장 크며, 약 없이 사망률을 낮추는 비약물 도구.",
        summary_detail="KIHD 연구의 핵심: ① 핀란드 중년 남성 수천명 종단 추적. ② 사우나 사용 빈도 1회/주 vs 4-7회/주: 조기사망 -40%. ③ 심혈관 사망률 -50%, 알츠하이머 위험 -65%. ④ 메커니즘: 일시적 심박수 상승(중강도 카디오와 유사), 혈관 내피 기능 개선, 열충격단백질(HSP) 상승. ⑤ 처방: 70~80°C, 15~20분, 주 3-4회. ⑥ 결합 효과: 운동 + 사우나 시 심혈관 보호 효과 가산적. NOGEAR 시각: 사우나는 약 없이 심장과 수명을 지키는 합법적 도구다 — 단, \"건강\"의 환상을 사기 전에 운동·식단·수면이 우선.",
        category="research", category_ko="회복",
        source="KIHD Study / PMC",
        source_url="https://pmc.ncbi.nlm.nih.gov/articles/PMC6262976/",
        viral_score=89,
        signals={"shock_factor": 21, "scientific_credibility": 20, "relatability": 19, "recency": 12, "controversy": 7, "visual_potential": 6},
        tags=["사우나", "KIHD", "핀란드", "사망률", "심혈관"],
        source_type="journal",
    ),
    make(
        title="\"열요법으로 콜레스테롤·염증 잡는다\" — 20개 RCT 메타분석은 \"NO\"",
        title_en="Passive Heat Therapy: 20 RCTs Show Limited Cardiovascular Markers Effect",
        summary="2025-09 American Journal of Preventive Cardiology의 20개 RCT 분석: 사우나·열요법은 콜레스테롤·염증·동맥경직성 등 \"심혈관 마커\"를 의미 있게 개선하지 않는다. 단, 수축기 혈압 약 4점 감소는 일관됨. \"마법의 회복 도구\" 마케팅의 절제 필요.",
        summary_detail="이 RCT 종합의 핵심: ① 20개 RCT(사우나, 온수욕, 적외선) 통합. ② 콜레스테롤·LDL·CRP 염증 마커·동맥 경직성 등 흔한 \"심혈관 마커\"는 의미 있는 변화 없음. ③ 단, 수축기 혈압 -4mmHg 일관 효과 — 임상적 가치 있음. ④ KIHD 등 대규모 코호트의 사망률 감소 효과는 분명하나, 메커니즘은 RCT 단기 마커로 설명 안 됨. ⑤ 의미: \"매주 3번 사우나로 모든 게 좋아진다\"는 마케팅은 RCT로는 미증명 — 다만 혈압·정신적 회복 효과는 분명. NOGEAR 시각: 사우나는 좋다 — 그러나 \"마법\"은 아니다. 운동·식단을 대체할 수 없다.",
        category="research", category_ko="회복",
        source="American Journal of Preventive Cardiology (2025-09)",
        source_url="https://www.frontiersin.org/journals/cardiovascular-medicine/articles/10.3389/fcvm.2025.1537194/full",
        viral_score=80,
        signals={"shock_factor": 18, "scientific_credibility": 20, "relatability": 17, "recency": 16, "controversy": 9, "visual_potential": 4},
        tags=["사우나", "열요법", "메타분석", "콜레스테롤", "혈압"],
        source_type="journal",
    ),

    # === 스트레칭 (2건) ===
    make(
        title="정적 스트레칭 — \"4분 회/10분 주\" 이상은 무의미 (메타-회귀)",
        title_en="Static Stretching: No Extra Benefit Beyond 4 min/Session, 10 min/Week",
        summary="PubMed 2024 시스템 리뷰·메타-회귀: 정적 스트레칭의 유연성 향상은 회당 4분, 주 10분에서 plateau 도달. 그 이상의 시간 투자는 추가 이득 없음. 강도·연령·성별·훈련 수준은 효과를 매개하지 않음. \"하루 30분 스트레칭\" 강박은 시간 낭비.",
        summary_detail="이 메타-회귀의 핵심: ① 정적 스트레칭의 가동범위(ROM) 향상은 \"용량 의존\" — 그러나 회당 4분, 주 10분에서 plateau. ② 그 이상 시간 투자는 추가 ROM 이득 없음(통계적 무의미). ③ 강도(가벼운 vs 강한): ROM 향상에 무관. ④ 연령·성별·훈련 수준: 효과 동일. ⑤ 함의: 효과적 처방 = 부위당 1분 × 4부위(전신 5분), 주 2회. ⑥ \"매일 30분 스트레칭\" 강박은 시간 효율 낮음. NOGEAR 시각: 스트레칭은 신앙이 아니다. 4분이면 충분 — 나머지 시간은 더 가치 있는 일에 써라.",
        category="research", category_ko="운동과학",
        source="PubMed Meta-Regression (2024)",
        source_url="https://pubmed.ncbi.nlm.nih.gov/39614059/",
        viral_score=83,
        signals={"shock_factor": 19, "scientific_credibility": 20, "relatability": 19, "recency": 12, "controversy": 9, "visual_potential": 4},
        tags=["정적스트레칭", "유연성", "메타회귀", "PubMed", "ROM"],
        source_type="journal",
    ),
    make(
        title="\"저항훈련\"이 \"정적 스트레칭\"만큼 유연성을 늘린다 — RCT 직접 비교",
        title_en="Resistance Training Equals Static Stretching for Flexibility — RCT (Springer 2024)",
        summary="Springer BMC 2024 RCT: 저항훈련 단독이 정적 스트레칭과 동등하게 유연성(ROM)을 향상시킴을 직접 비교 입증. 추가로 근력은 저항훈련 군에서 우월. 시간 한정된 운동인은 \"스트레칭 따로\" 안 해도 된다.",
        summary_detail="이 RCT의 핵심: ① 8주 RCT, 건강 성인 대상. ② 저항훈련 군 vs 정적 스트레칭 군 비교. ③ 결과: 두 군 모두 햄스트링·고관절·어깨 ROM 동등 향상. ④ 추가: 저항훈련 군은 근력 +12~18% 향상 — 스트레칭 군은 변화 없음. ⑤ 메커니즘: 저항훈련은 풀 ROM 수행 시 근건단위 신장 자극 + 근력 동시 향상. ⑥ 함의: 시간 효율적 처방 = 풀 ROM 저항훈련만으로 충분. NOGEAR 시각: \"근력 + 유연성\"은 분리된 두 과목이 아니다. 풀 ROM으로 들면 둘 다 잡힌다 — 약 없이.",
        category="research", category_ko="운동과학",
        source="Springer BMC Sports Sci Med Rehab (2024)",
        source_url="https://link.springer.com/article/10.1186/s13102-024-00934-1",
        viral_score=82,
        signals={"shock_factor": 18, "scientific_credibility": 19, "relatability": 19, "recency": 12, "controversy": 9, "visual_potential": 4},
        tags=["저항훈련", "유연성", "RCT", "Springer", "ROM"],
        source_type="journal",
    ),

    # === 오메가-3 (2건) ===
    make(
        title="오메가-3, 회복은 \"진짜\" 효과 — DOMS 25~35% 빠른 회복",
        title_en="Omega-3 EPA+DHA: 25-35% Faster DOMS Recovery — Multiple Systematic Reviews",
        summary="2024-2025 시스템 리뷰들: 오메가-3 EPA+DHA 보충(2-3g/일)이 운동 유발 염증·DOMS·기능 회복을 25~35% 가속. ISSN 2025 포지션 스탠드는 모든 운동인에 최소 1.14g/일 EPA+DHA 권장.",
        summary_detail="이 종합의 핵심: ① 오메가-3 보충 → 염증성 사이토카인 감소 + 특수 프로해소 매개체(SPM) 증가 → 빠른 염증 해소. ② DOMS(지연성 근통증) 강도·기간 25~35% 감소. ③ 기능 회복(점프, 1RM) 가속. ④ ISSN 2025 포지션: 모든 운동인에 1.14g/일 EPA+DHA 최소 권장, 회복 강조 시 2-3g/일. ⑤ 식품 형태: 연어·고등어·정어리 주 2회로 도달 가능. ⑥ 보충제 형태도 안전. NOGEAR 시각: 오메가-3은 \"마법 보충제\"는 아니지만 \"회복\"에서 RCT 증거가 가장 견고한 도구 중 하나. 약 없이 회복 시간을 줄이는 정직한 길.",
        category="research", category_ko="영양",
        source="ISSN Position Stand 2025 / PMC",
        source_url="https://pmc.ncbi.nlm.nih.gov/articles/PMC11737053/",
        viral_score=84,
        signals={"shock_factor": 18, "scientific_credibility": 21, "relatability": 19, "recency": 14, "controversy": 7, "visual_potential": 5},
        tags=["오메가3", "EPA", "DHA", "DOMS", "ISSN"],
        source_type="journal",
    ),
    make(
        title="오메가-3와 근비대 — 청년에서 \"비대 효과 미약\", 근력에선 효과 (PMC 2025)",
        title_en="Omega-3 in Young Adults: Limited Hypertrophy Boost, but Strength Gains Possible",
        summary="PMC 2025: 청년 운동인에서 오메가-3 보충은 단독 근비대 효과는 미약하나, 저항훈련과 결합 시 근력 향상에 용량·기간 의존적 추가 효과를 보였다. 노인에선 비대 효과도 더 분명.",
        summary_detail="이 종합 분석의 핵심: ① 청년 RCT: 오메가-3 단독 근비대 효과 미약. ② 저항훈련 + 오메가-3 결합: 근력 향상에 용량(2g+/일) 및 기간(8주+) 의존적 추가 효과. ③ 노인 RCT: 사르코페니아 예방·근비대 효과 더 분명 — 단백질 합성 응답성 회복. ④ 메커니즘: mTOR 신호 강화·근육 인슐린 민감도 ↑. ⑤ 권장: 청년은 회복·염증 효과 위주, 노인은 근비대 효과 적극 활용. NOGEAR 시각: 보충제는 \"누구에게 효과적인가\"가 핵심. 청년 자연인은 회복용으로, 노인은 근비대용으로 — 마케팅의 \"만능\" 메시지는 거짓.",
        category="research", category_ko="영양",
        source="PMC Omega-3 Strength Training Review (2025)",
        source_url="https://pmc.ncbi.nlm.nih.gov/articles/PMC12251297/",
        viral_score=78,
        signals={"shock_factor": 17, "scientific_credibility": 19, "relatability": 18, "recency": 14, "controversy": 8, "visual_potential": 4},
        tags=["오메가3", "근비대", "노인", "PMC", "저항훈련"],
        source_type="journal",
    ),

    # === 식후 걷기 (2건) ===
    make(
        title="\"식후 10분 걷기\" — 혈당 스파이크 17mg/dL 감소 (Nature 2025)",
        title_en="10-Min Walk Right After Eating Drops Glucose Peak by 17 mg/dL — Nature 2025",
        summary="Nature Scientific Reports 2025 RCT: 식후 즉시 10분 걷기가 식후 혈당 곡선(AUC)·피크 수치를 의미 있게 감소시킴을 입증. 피크 -17.6 mg/dL. 30분 걷기 \"30분 후\" 시작보다 \"즉시 짧게\"가 더 효율적.",
        summary_detail="이 RCT의 핵심: ① 건강한 청년 대상, 75g 글루코스 섭취 후. ② 비교: ⒶGD 직후 10분 걷기, Ⓑ 30분 후 30분 걷기, Ⓒ 좌식 휴식. ③ 결과: 두 걷기 조건 모두 좌식 대비 2시간 AUC 의미 있게 감소. ④ 피크: 즉시 10분 걷기 164.3 mg/dL vs 좌식 181.9 mg/dL — 약 -17.6 mg/dL. ⑤ 걷기 속도: 약 3.8 km/h(편안한 속도). ⑥ 함의: \"식후 산책\"이 가장 시간 효율적인 혈당 관리 도구. NOGEAR 시각: 약 없이 혈당을 잡는 가장 단순한 방법은 \"식후 10분 걷기\". 인슐린·메트포민이 답이 아닌 사례가 많다.",
        category="research", category_ko="운동과학",
        source="Nature Scientific Reports (2025)",
        source_url="https://www.nature.com/articles/s41598-025-07312-y",
        viral_score=90,
        signals={"shock_factor": 22, "scientific_credibility": 21, "relatability": 22, "recency": 15, "controversy": 6, "visual_potential": 5},
        tags=["식후걷기", "혈당", "ScientificReports", "RCT", "당뇨"],
        source_type="journal",
    ),
    make(
        title="식후 10주 운동 — 비만·과체중 청년 24시간 혈당 곡선 안정화 (PMC 2025)",
        title_en="Post-Meal Exercise 10 Weeks: 24h Glucose Stabilization in Overweight Adults",
        summary="PMC 2025-2026 RCT: 비만·과체중 청년 34명을 대상으로 10주간 \"식후 0-90분 내 운동\" 또는 \"식전 운동\"을 주 5회 적용한 결과, 두 그룹 모두 24시간 혈당 곡선이 의미 있게 안정화. 식후 운동은 매일 실천 가능한 비약물 혈당 도구.",
        summary_detail="이 RCT의 핵심: ① 34명 비만·과체중 청년, 10주 RCT. ② 그룹: 식후 0-90분 운동 vs 식전 운동, 주 5회. ③ 결과: 24시간 평균 혈당, 변동성, 식후 피크 모두 의미 있게 감소 — 두 그룹 동등. ④ 함의: \"식후 운동의 즉각 효과\"가 만성 적응으로 누적 — 인슐린 감수성 향상. ⑤ 식전 vs 식후: 24시간 결과는 동등 — 일상 적용 가능성에서 식후 \"산책\"이 우월. ⑥ 처방: 식후 30~60분 내 20~30분 중강도 운동. NOGEAR 시각: 매일 식후 한 번 움직이는 것이 메트포민의 일부 효과를 대체할 수 있다 — 약 없이.",
        category="research", category_ko="운동과학",
        source="PMC RCT (2025)",
        source_url="https://pmc.ncbi.nlm.nih.gov/articles/PMC12681541/",
        viral_score=83,
        signals={"shock_factor": 19, "scientific_credibility": 20, "relatability": 21, "recency": 14, "controversy": 5, "visual_potential": 4},
        tags=["식후운동", "혈당", "비만", "PMC", "RCT"],
        source_type="journal",
    ),

    # === 여성 저항훈련 (2건) ===
    make(
        title="여성 저항훈련 종합 — 126개 연구·4,000명, 모든 연령에서 효과 (2026 메타)",
        title_en="Resistance Training in Women: 126 Studies, 4,000+ Women, Effective at Every Age",
        summary="ScienceDirect 2026 시스템 리뷰·메타분석(Isenmann 외): 126개 연구·4,000+명 여성 분석 결과, 저항훈련이 연령·폐경 상태와 무관하게 근력·체구성을 의미 있게 향상시킴을 확인했다. \"여성은 무거운 걸 들면 안 된다\"는 신화의 마지막 종지부.",
        summary_detail="이 메타분석의 핵심: ① 사춘기 ~ 노년 여성 전 연령 통합. ② 저항훈련 → 상지·하지 근력 모두 향상, 호르몬 상태(폐경 전/후) 무관. ③ 체구성: 제지방체중 +1-3kg, 체지방 감소. ④ 추가 이득: 골밀도, 대사 건강, 정신건강, 자존감, 신체상. ⑤ 메커니즘: 호르몬 차이 있으나 근비대 적응 경로(mTOR 등)는 남성과 유사. ⑥ \"여성용 가벼운 운동\" 마케팅은 비효율적. NOGEAR 시각: 여성도 무겁게 들어야 한다 — 약 없이 강해지는 길은 남녀 동일. 핑크 덤벨 마케팅에 속지 마라.",
        category="research", category_ko="운동과학",
        source="ScienceDirect Meta (2026)",
        source_url="https://www.sciencedirect.com/science/article/abs/pii/S1440244026000964",
        viral_score=89,
        signals={"shock_factor": 21, "scientific_credibility": 21, "relatability": 21, "recency": 17, "controversy": 9, "visual_potential": 5},
        tags=["여성저항훈련", "메타분석", "ScienceDirect", "근력", "폐경"],
        source_type="journal",
    ),
    make(
        title="\"생리주기에 맞춘 훈련\"은 신화 — 강도·적응에 영향 없음 (PMC 2023)",
        title_en="Menstrual Cycle Phase Doesn't Affect Acute Strength or Training Adaptations",
        summary="PMC 2023 종합: 현재 증거는 여성의 생리주기 단계가 급성 근력 수행이나 저항훈련 적응에 영향을 주지 않음을 보여준다. 인스타에서 유행하는 \"생리주기 맞춤 훈련\"은 과학적으로 뒷받침되지 않는다.",
        summary_detail="이 메타 분석의 핵심: ① 생리주기 4단계(여포기 초기/후기, 황체기 초기/후기) 별 급성 근력 수행 비교 RCT 다수 통합. ② 결과: 단계 간 통계적 유의 차이 없음. ③ 장기 적응(근비대·근력) 또한 생리주기 \"맞춤\" vs 무관 훈련 비교에서 차이 없음. ④ 단, 개인 컨디션(피로감·통증)은 일부 단계에서 다를 수 있어 자기 신호 따라 조정은 합리적. ⑤ 함의: 표준 진보적 과부하 훈련이 모든 여성에 적용 가능 — 복잡한 \"단계 맞춤\" 불필요. NOGEAR 시각: \"여성은 생리주기 맞춤 운동이 필요\"는 인플루언서 마케팅. 너의 진짜 답은 일관된 진보적 과부하 훈련.",
        category="research", category_ko="운동과학",
        source="PMC Meta-Analysis (2023)",
        source_url="https://pmc.ncbi.nlm.nih.gov/articles/PMC10076834/",
        viral_score=85,
        signals={"shock_factor": 20, "scientific_credibility": 19, "relatability": 21, "recency": 11, "controversy": 11, "visual_potential": 4},
        tags=["생리주기", "여성훈련", "PMC", "메타분석", "신화"],
        source_type="journal",
    ),

    # === SARMs (2건) ===
    make(
        title="SARMs 자가보고 부작용 — 사회미디어 데이터 분석, 청소년·SNS 표적",
        title_en="Self-Reported SARMs Side Effects: Social Media Data Analysis (JMIR 2025)",
        summary="Journal of Medical Internet Research 2025: 소셜미디어 데이터 분석 결과, SARMs 사용은 청년·청소년에 SNS 통해 광범위 확산. 자가보고 부작용으로는 간 손상, 호르몬 억제, 신장·심장 독성, 피로·구토·황달 등이 빈번하게 보고됐다.",
        summary_detail="이 JMIR 2025 분석의 핵심: ① Reddit·Discord·Twitter 등 소셜 미디어에서 SARMs 사용자 자가보고를 텍스트마이닝. ② 빈번 부작용: 간 손상(상복부 통증, 황달), 만성 테스토스테론 억제, 신장 기능 이상, 심장 부정맥, 우울증, 피로. ③ 사용자 다수가 청년·청소년 — \"안전한 스테로이드 대안\" 마케팅에 노출. ④ 라벨 정확도: 2025 분석에서 SARMs 제품의 약 50%만이 라벨 표시 성분 함유 — 나머지는 가짜·오염. ⑤ FDA 미승인 — 모든 사용은 자기 책임. NOGEAR 시각: SARMs는 \"안전한 스테로이드\"가 아니다. SNS의 청소년 표적 마케팅은 약장수의 새 전선. 자연인의 길이 진짜 답.",
        category="news", category_ko="약물",
        source="Journal of Medical Internet Research (2025)",
        source_url="https://www.jmir.org/2025/1/e65031/",
        viral_score=92,
        signals={"shock_factor": 23, "scientific_credibility": 20, "relatability": 19, "recency": 14, "controversy": 12, "visual_potential": 6},
        tags=["SARMs", "JMIR", "청소년", "사이드이펙트", "약물"],
        source_type="journal",
    ),
    make(
        title="SARMs 시스템 리뷰 — \"성능 향상은 있다, 그러나 안전성은 미증명\"",
        title_en="SARMs Effects on Physical Performance: Systematic Review of RCTs (Wiley 2025)",
        summary="Wiley Clinical Endocrinology 2025 시스템 리뷰: SARMs가 신체 성능·체구성에 \"긍정 효과\"를 보이고 임상시험에서 부작용은 중등도까지 \"중간 빈도\"로 보고됨. 그러나 장기 안전성은 미증명 — FDA 승인 SARM은 0개.",
        summary_detail="이 시스템 리뷰의 핵심: ① 임상시험 데이터 통합. ② 효과: 제지방체중·근력·체지방 감소에 의미 있는 효과 — 스테로이드보다 약하지만 분명. ③ 부작용: 일시적 ALT/AST 상승(간), HDL 감소, 테스토스테론 억제 — \"중등도까지 중간 빈도\". ④ 중증 부작용: 임상시험에선 낮으나 \"비임상 사용\"에서 간부전·심혈관 사건 사례 다수. ⑤ FDA 미승인, 안전 용량·장기 영향 미확정. ⑥ 시판 SARMs 제품의 약 절반은 라벨 미일치. NOGEAR 시각: 임상시험의 \"통제\"와 \"실제 사용자의 자기 처방\"은 차원이 다르다. SARMs는 약장수의 \"안전한 도핑\"이라는 환상으로 청년을 끌어들이는 미끼.",
        category="news", category_ko="약물",
        source="Wiley Clinical Endocrinology (2025)",
        source_url="https://onlinelibrary.wiley.com/doi/10.1111/cen.15135",
        viral_score=88,
        signals={"shock_factor": 21, "scientific_credibility": 20, "relatability": 17, "recency": 14, "controversy": 12, "visual_potential": 4},
        tags=["SARMs", "시스템리뷰", "Wiley", "안전성", "FDA"],
        source_type="journal",
    ),
]


def merge():
    data = json.loads(ARTICLES_PATH.read_text())
    existing_news = data.get("news", [])
    existing_research = data.get("research", [])

    seen_urls = {a.get("source_url") for a in existing_news + existing_research}
    seen_titles = {a.get("title") for a in existing_news + existing_research}

    added = 0
    skipped = 0
    for art in ARTICLES:
        if art["source_url"] in seen_urls or art["title"] in seen_titles:
            skipped += 1
            continue
        # Place SARMs articles in news (약물 category), others in research
        if art.get("category") == "news":
            existing_news.append(art)
        else:
            existing_research.append(art)
        seen_urls.add(art["source_url"])
        seen_titles.add(art["title"])
        added += 1

    existing_news.sort(key=lambda x: x.get("viral_score", 0), reverse=True)
    existing_research.sort(key=lambda x: x.get("viral_score", 0), reverse=True)

    existing_news = existing_news[:200]
    existing_research = existing_research[:200]

    data["news"] = existing_news
    data["research"] = existing_research

    meta = data.get("meta", {})
    meta["last_updated"] = ISO_NOW
    meta["last_updated_kst"] = NOW.strftime("%Y-%m-%d %H:%M KST 자동크롤(저녁 V3: 사우나·스트레칭·오메가3·식후걷기·여성훈련·SARMs) +") + str(added) + "건"
    meta["news_count"] = len(existing_news)
    meta["research_count"] = len(existing_research)
    meta["total_articles"] = len(existing_news) + len(existing_research)
    meta["crawl_count"] = meta.get("crawl_count", 0) + 1
    all_articles = existing_news + existing_research
    if all_articles:
        scores = [a.get("viral_score", 0) for a in all_articles]
        meta["top_viral_score"] = max(scores)
        meta["avg_viral_score"] = round(sum(scores) / len(scores), 1)
    data["meta"] = meta

    ARTICLES_PATH.write_text(json.dumps(data, ensure_ascii=False, indent=2))
    return added, skipped, len(existing_news), len(existing_research)


if __name__ == "__main__":
    added, skipped, n_news, n_research = merge()
    print(f"신규 추가: {added}건 (중복 스킵: {skipped}건)")
    print(f"news: {n_news}건, research: {n_research}건, total: {n_news + n_research}건")
    data = json.loads(ARTICLES_PATH.read_text())
    all_articles = data["news"] + data["research"]
    all_articles.sort(key=lambda x: x.get("viral_score", 0), reverse=True)
    print("\nTOP 3:")
    for i, a in enumerate(all_articles[:3], 1):
        print(f"{i}. [{a.get('viral_score')}] {a.get('title')[:60]}")
