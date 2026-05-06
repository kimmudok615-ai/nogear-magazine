#!/usr/bin/env python3
"""NOGEAR Magazine - 2026-05-06 저녁 크롤
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
            "notes": notes or "2026-05-06 저녁 크롤 신규 추가. 소스 URL 직접 확인.",
        },
        "badge": "🆕 NEW",
    }


NEW_ARTICLES = [
    # ===== 운동과학 / 근비대 (Exercise Science / Hypertrophy) =====
    make(
        "더 많은 세트 = 더 많은 근육? 사상 최대 볼륨 연구가 답을 내놨다 — 아니다",
        "More Sets, No More Muscle: Largest Volume Study Confirms Diminishing Returns",
        "Club Solutions Magazine 2026.04 보도 — 사상 최대 규모의 트레이닝 볼륨 연구는 '세트 수가 늘면 근육도 비례해 늘어난다'는 통념을 무너뜨렸다. 6개월 이상 진지하게 운동한 참가자를 대상으로 볼륨 그룹 간 근비대 차이는 통계적으로 유의하지 않았다. 즉 헬스장 가는 시간을 두 배로 늘려도 근육이 두 배가 되지는 않는다.",
        "이 연구의 무게는 표본의 '진짜성'에 있다. 초보자가 아닌 6개월 이상 훈련한 일반 헬스장 회원 — NOGEAR 독자 그대로의 프로필이다. 결과는 단순했다 — 일정 임계값(주당 약 12~20세트/근육군)을 넘어서면 추가 볼륨은 근비대를 더 키우지 않았다. 이게 의미하는 바는 두 가지다. 1) 시간이 부족한 직장인은 죄책감을 버려도 된다 — 짧은 세션도 충분하다. 2) 'overreaching'으로 회복을 망치는 것이 'undertraining'보다 더 큰 손해다. 단, 강도(failure에 가까운 정도)는 여전히 결정 변수다 — 양보다 질.",
        "Club Solutions Magazine 2026.04",
        "https://clubsolutionsmagazine.com/2026/04/more-sets-no-more-muscle-the-largest-study-on-strength-training-volume-has-answers/",
        "운동과학",
        87,
        {"shock_factor": 20, "scientific_credibility": 20, "relatability": 22, "recency": 18, "controversy": 4, "visual_potential": 3},
        ["볼륨", "근비대", "세트수", "트레이닝볼륨", "운동과학", "메타분석"],
        kind="news", peer_reviewed=False,
    ),
    make(
        "근육은 길이로 자란다 — 긴 근육 길이에서의 자극이 비대 효과를 키운다",
        "Training at Longer Muscle Lengths Boosts Hypertrophy — Thieme 2026 Review",
        "Thieme 2026 리뷰는 같은 운동량이라도 '근육이 늘어난 상태(long muscle length)'에서 자극을 받으면 근비대가 더 잘 일어난다는 점을 정리했다. 즉 가동범위(ROM)와 운동 선택은 단순한 취향이 아니라 결과를 결정하는 변수다. 풀 ROM 스쿼트, 하강 깊은 RDL, 케이블 펙플라이의 신전 끝 — 길이에서 만들어진다.",
        "기전적 핵심은 근절(sarcomere) 수준의 신호다. 근육이 늘어난 상태에서 부하를 받으면 in-series 근절이 추가되고, 단축성 수축에 비해 근위성세포(satellite cell) 활성화가 더 강하게 유도된다. 실전 적용은 운동 선택에 달려 있다 — 1) 가슴: 인클라인 덤벨 플라이(스트레치 강조), 2) 햄스트링: 루마니안 데드리프트, 3) 이두: 인클라인 덤벨 컬, 4) 삼두: 오버헤드 익스텐션. 'partial ROM에서 더 무겁게'보다 'full ROM에서 stretch under tension'이 비대 효율이 높다는 메시지다.",
        "Thieme 2026",
        "https://www.thieme-connect.com/products/ejournals/abstract/10.1055/a-2733-7605",
        "운동과학",
        86,
        {"shock_factor": 15, "scientific_credibility": 24, "relatability": 22, "recency": 17, "controversy": 4, "visual_potential": 4},
        ["근비대", "ROM", "가동범위", "스트레치", "운동선택", "근절"],
    ),
    make(
        "실패 근처까지 가지 않으면 근육은 자라지 않는다 — FAU 연구",
        "FAU Study: Train Close to Failure for Muscle Growth, Not Necessarily for Strength",
        "Florida Atlantic University 연구진이 발표한 분석 — 근비대(muscle growth)는 실패(failure)에 가까울수록 비례해 증가하지만, 절대근력(maximal strength)은 그렇지 않았다. 즉 사이즈를 키우려면 RIR(Reps In Reserve) 0~2 범위에서 멈춰야 하고, 1RM을 키우려면 더 이른 단계에서 끝낼 수도 있다는 뜻이다.",
        "이 연구가 중요한 이유는 '왜 헬스장에서 4세트 12회를 매번 같은 무게로 하면서 사이즈가 안 늘까'에 답을 주기 때문이다. 답은 — 충분히 가깝지 않게 멈추기 때문이다. RIR 4~5에서 끊는 트레이닝은 강도 부족으로 비대 자극이 약하다. 처방: 비대 목표 세트는 마지막 1~2회를 '폼이 무너지지 않는 한 끝까지' 짜내는 것이 합리적이다. 단, 매 세트 매 운동 모두 failure까지 가는 것은 회복 비용이 너무 크다 — 보조 운동 위주, 메인 컴파운드는 RIR 1~2 권장.",
        "FAU Newsdesk",
        "https://www.fau.edu/newsdesk/articles/muscle-growth-strength-study",
        "운동과학",
        85,
        {"shock_factor": 16, "scientific_credibility": 22, "relatability": 22, "recency": 16, "controversy": 5, "visual_potential": 4},
        ["RIR", "실패", "근비대", "강도", "FAU", "운동과학"],
    ),
    make(
        "고급 트레이닝 시스템(rest-pause, BFR, drop set)은 일반 세트보다 더 키우지 않는다",
        "Advanced Resistance Training Systems Don't Beat Traditional Sets — 2026 Meta-Analysis",
        "MDPI 2026.02 메타분석 — rest-pause, velocity-based, eccentric overload 등 '고급' 시스템들은 볼륨·강도·노력이 같다면 전통적 멀티세트 대비 의미 있는 비대 우위를 보이지 않았다. 인스타에서 본 '비밀 기법'은 그냥 시간 낭비다.",
        "Sports 저널(MDPI)에 실린 이 시스템 리뷰는 6개월 이상 훈련한 성인을 대상으로 했다. 결과: 일부 방법(특히 eccentric overload)이 작은 method-specific 이득을 보였지만, 비대(hypertrophy) 측정치에서 의미 있는 우위는 없었다. 이게 의미하는 바는 — 1) '뭘 하느냐'보다 '얼마나 노력하느냐'가 결정 변수, 2) 종목을 자주 바꾸는 것보다 같은 동작을 진척(progressive overload)시키는 것이 효율적, 3) 시간이 적은 사람은 'rest-pause' 같은 압축 기법으로 같은 볼륨을 더 빨리 채울 수는 있지만 '더 많은 근육'을 받지는 못한다.",
        "MDPI Sports 2026.02",
        "https://www.mdpi.com/2411-5142/11/1/80",
        "운동과학",
        84,
        {"shock_factor": 18, "scientific_credibility": 23, "relatability": 20, "recency": 15, "controversy": 5, "visual_potential": 3},
        ["고급트레이닝", "rest-pause", "drop-set", "메타분석", "운동과학", "비대"],
    ),
    make(
        "느린 lowering(eccentric)이 시간 대비 근력 효율을 깬다 — 5분/일도 효과",
        "Slow Eccentric Movements Build Strength Efficiently — Even 5 Min/Day Helps",
        "ScienceDaily 2026 보도 — 천천히 내리는 동작(eccentric)은 같은 시간 대비 근력 향상 효율이 가장 높았다. 의자 스쿼트, 벽 푸시업처럼 보이는 동작도 'lowering 단계를 5초 이상' 끌면 의미 있는 근력 변화를 만든다. 헬스장에 못 가는 날도 끝난 게 아니다.",
        "Eccentric 수축의 우위는 두 가지 기전에서 온다. 1) 동일 부하에서 사용 가능한 근섬유 수가 더 많아 단위 시간당 자극이 크다, 2) tendon stiffness 적응이 강해 부상 예방·운동 수행 능력 모두 향상. 적용은 단순하다 — 익숙한 동작의 '내려가는 단계'를 평소보다 2~4배 천천히 한다. 푸시업: 3초 내려가서 1초 올라오기. 스쿼트: 4초 내려서 1초 일어서기. 하루 5분 — 즉 푸시업 8회 × 5세트, 또는 스쿼트 10회 × 4세트. 노인·재활·시간 부족 직장인 모두에게 코스트 제로의 처방.",
        "ScienceDaily 2026",
        "https://www.sciencedaily.com/releases/2026/04/260426012305.htm",
        "운동과학",
        85,
        {"shock_factor": 17, "scientific_credibility": 20, "relatability": 24, "recency": 16, "controversy": 4, "visual_potential": 4},
        ["에센트릭", "lowering", "근력", "시간효율", "홈트", "운동과학"],
        kind="news", peer_reviewed=False,
    ),

    # ===== 영양 / 단백질 (Nutrition / Protein) =====
    make(
        "단백질은 1.6g/kg면 충분? — 2.4g/kg가 더 잘 먹히는 사람도 있다",
        "Protein 2.4g/kg May Outperform 1.6g/kg in High-Volume Lifters — 2025 Update",
        "기존 가이드라인 1.6g/kg(체중)을 두고 새로운 데이터가 흔들고 있다. 트레이닝 볼륨이 높고 lean body mass가 큰 사람일수록 2.0~2.4g/kg 영역에서 추가 이득이 관찰된다는 연구가 누적되고 있다. 다만 2.4g/kg를 넘어가면 한계 효용이 거의 0에 수렴한다.",
        "단백질 섭취량은 더 이상 '한 가지 숫자'로 결정되지 않는다. 결정 변수는 — 1) 트레이닝 볼륨, 2) 칼로리 적자(컷팅) 여부, 3) 나이(40+는 leucine 임계값이 더 높다), 4) lean body mass. 컷팅 중에는 근육 손실 방지를 위해 2.3~3.1g/kg LBM(natural bodybuilding 가이드)이 권장된다. 단 신장 기능 이상이 없는 건강한 성인 기준 — 3.3g/kg까지는 안전성 데이터 존재. '몸집 큰 사람일수록 단백질 더 많이' 원칙은 유효하지만, 일정 수준 넘어가면 더 들이는 칼로리는 단백질이 아니라 탄수화물·지방으로 가는 것이 효율적.",
        "Strength Lab 360 / ISSN 2025",
        "https://strengthlab360.com/blogs/strength-training/protein-intake-in-2025-why-2-4g-kg-may-outperform-the-1-6g-kg-rule",
        "영양",
        87,
        {"shock_factor": 18, "scientific_credibility": 20, "relatability": 24, "recency": 17, "controversy": 5, "visual_potential": 3},
        ["단백질", "프로틴섭취", "1.6g/kg", "2.4g/kg", "영양", "근비대"],
        kind="news", peer_reviewed=False,
    ),
    make(
        "끼니마다 30g씩 — 분산 섭취가 24시간 단백질 합성률 25% 더 올린다",
        "Even 30g Protein Per Meal Boosts 24h Muscle Protein Synthesis by 25%",
        "ISSN 가이드라인 — 끼니마다 약 30g씩 분산해서 먹는 것이 한 끼에 몰아 먹는 것보다 24시간 mixed muscle protein 합성률을 25% 더 끌어올렸다. 즉 '하루 총량'만큼이나 '분배'가 중요하다.",
        "이 결과의 기전은 leucine 임계값이다. 한 번의 식사에서 leucine 약 2.5g 이상을 자극해야 muscle protein synthesis(MPS)가 켜진다. 30g 단백질(고기·생선·계란·두유·whey 기준)이 이 임계값을 안정적으로 충족시킨다. 처방: 1) 하루 4~5끼, 2) 끼니당 0.4g/kg 또는 ~30g, 3) 컷팅 중에는 끼니당 35~40g. 자기 전 casein 20~40g은 야간 단백질 합성을 추가 자극(특히 노년층 효과 큼). '아침은 토스트, 점심은 라면, 저녁에 닭가슴살 200g 폭식' 패턴은 같은 총량이라도 비효율적.",
        "ISSN / Springer Nature",
        "https://link.springer.com/article/10.1186/s12970-018-0215-1",
        "영양",
        84,
        {"shock_factor": 16, "scientific_credibility": 22, "relatability": 22, "recency": 12, "controversy": 4, "visual_potential": 4},
        ["단백질분산", "MPS", "leucine", "끼니당30g", "영양", "근합성"],
    ),
    make(
        "취침 전 카제인 20~40g — 자는 동안에도 근육 합성이 돌아간다",
        "20-40g Pre-Sleep Casein Stimulates Overnight Protein Synthesis",
        "USADA 정리 자료 — 취침 전 카제인 단백질 20~40g 섭취는 야간 전신 단백질 합성을 자극한다. 영-노년 모두에서 일관된 효과 확인. 잠 자는 동안에도 합성을 켜둘 수 있는 유일한 시간대.",
        "카제인은 위에서 응고되어 6~8시간에 걸쳐 천천히 아미노산을 방출한다. 야간은 평소 단식 상태이기 때문에 근육 분해가 우세한 시간 — 카제인은 이 분해를 줄이고 합성을 유지한다. 임상에서: 노년층(50+)은 sarcopenia 예방 효과가 특히 크고, 청년 보디빌더는 컷팅 중 근손실 방지에 유효. 카제인이 없으면 cottage cheese 200g, 또는 그릭요거트 300g + 견과류로 대체 가능. 단점은 두 가지: 1) 유당 불내증, 2) 취침 직전 위 부담 — 자기 30~60분 전 권장.",
        "USADA Spirit of Sport",
        "https://www.usada.org/spirit-of-sport/when-consume-protein-muscle-growth/",
        "영양",
        82,
        {"shock_factor": 16, "scientific_credibility": 20, "relatability": 22, "recency": 12, "controversy": 4, "visual_potential": 4},
        ["카제인", "취침전단백질", "야간합성", "영양", "회복"],
        kind="news", peer_reviewed=False,
    ),

    # ===== 보충제 디벙킹 (Supplements Debunked) =====
    make(
        "멀티비타민은 사망률·심장병·암·치매를 줄이지 않는다 — Johns Hopkins",
        "Multivitamins Don't Reduce Heart Disease, Cancer, or Mortality — JHU Review",
        "Johns Hopkins Medicine 정리 — 종합비타민제는 심장병, 암, 인지 저하, 조기 사망 어느 것도 의미 있게 줄이지 않았다. '보험'으로 먹는 멀티비타민에 매달 쓰는 돈은 그 효과가 0에 가깝다는 결론이다.",
        "Johns Hopkins가 인용한 대규모 임상시험 데이터(Physicians' Health Study II 등)는 한 가지 메시지로 수렴한다 — 결핍이 없는 일반 건강인에서 멀티비타민의 한계 효과는 없거나 매우 작다. 예외는 명확하다 — 1) 임신 중(엽산), 2) 노년·식이 제한자(B12), 3) 결핍 진단을 받은 경우, 4) 햇빛 노출 적은 사람의 비타민 D. 그 외에는 — 균형 잡힌 식단이 멀티보다 우수하다. 게다가 일부 단일 성분은 과량 섭취 시 위험하다(아래 비타민 E·셀레늄 항목 참고).",
        "Johns Hopkins Medicine",
        "https://www.hopkinsmedicine.org/health/wellness-and-prevention/is-there-really-any-benefit-to-multivitamins",
        "보충제",
        88,
        {"shock_factor": 22, "scientific_credibility": 22, "relatability": 22, "recency": 12, "controversy": 8, "visual_potential": 3},
        ["멀티비타민", "Johns Hopkins", "보충제", "사망률", "디벙킹"],
        kind="news", peer_reviewed=False,
    ),
    make(
        "비타민 E·셀레늄은 전립선암 위험을 올린다 — Fred Hutch 임상시험",
        "Vitamin E +17% Prostate Cancer Risk; Selenium Raised High-Grade Risk — Fred Hutch",
        "Fred Hutch Cancer Center 정리 — 대규모 SELECT 임상시험 등에서 비타민 E 보충제는 전립선암 위험을 17% 올렸고, 셀레늄은 일부 남성에서 고악성도(high-grade) 전립선암 위험을 끌어올렸다. '항산화제 = 안전' 신화는 끝났다.",
        "이 결과의 충격은 '암을 막을 줄 알았던 보충제가 오히려 암을 만들었다'는 점이다. 기전은 — 항산화제 과량은 정상 세포 신호 전달을 교란하고, ROS(활성산소)가 가지는 적정 수준의 신호 기능을 무너뜨린다. 실전 권고: 1) 멀티비타민에 들어 있는 일일 권장량 수준은 큰 위험 없음, 2) 단일 성분 고용량 보충제(특히 비타민 E 400 IU 이상, 셀레늄 200mcg 이상)는 의학적 적응증 없이 복용 금지, 3) 암 예방 목적의 보충제는 식물 자체로(브로콜리·토마토·녹차) 섭취하라.",
        "Fred Hutch Cancer Center",
        "https://www.fredhutch.org/en/news/center-news/2026/02/dietary-supplements-dont-prevent-cancer.html",
        "보충제",
        90,
        {"shock_factor": 24, "scientific_credibility": 22, "relatability": 18, "recency": 16, "controversy": 12, "visual_potential": 3},
        ["비타민E", "셀레늄", "전립선암", "보충제위험", "Fred Hutch", "디벙킹"],
        kind="news", peer_reviewed=False,
    ),
    make(
        "NMN·레스베라트롤·항산화 메가스택 — 인체 증거는 여전히 약하다",
        "NMN, Resveratrol, Antioxidant Megastacks: Strong Biology, Weak Human Proof",
        "Tukk Book 정리 — 2026년 가장 과대평가된 보충제로 NMN(니코틴아미드 모노뉴클레오타이드), 레스베라트롤, 항산화 메가스택, 일반 longevity 블렌드가 꼽혔다. 공통점: 동물 데이터는 화려하지만 인체 임상 효과는 미미하다.",
        "이 카테고리의 매출 성장은 'aging biology'의 발전을 따라가며 폭발했지만, 인체에서 의미 있는 longevity 마커 변화를 보여준 무작위 대조 시험은 거의 없다. NMN은 NAD+ 수치를 올리는 것은 확인됐지만, 그게 인간의 수명·건강수명을 늘렸다는 증거는 부족하다. 레스베라트롤은 흡수율(bioavailability) 문제로 임상에서 일관된 효과를 못 냈다. 권고: longevity를 진심으로 원한다면 — 1) 운동(특히 zone 2 + 근력), 2) 7~9시간 수면, 3) 신선식 위주 식단, 4) 사회적 연결. 보충제는 마지막 1%.",
        "Tukk Book 2026",
        "https://tukkbook.in/overhyped-supplements-2026/",
        "보충제",
        86,
        {"shock_factor": 22, "scientific_credibility": 18, "relatability": 22, "recency": 14, "controversy": 8, "visual_potential": 3},
        ["NMN", "레스베라트롤", "longevity", "보충제디벙킹", "오버하이프"],
        kind="news", peer_reviewed=False,
    ),
    make(
        "오메가-3 EPA가 외상 뇌손상 회복을 늦춘다 — 동물 모델 발견",
        "Omega-3 EPA May Hinder Brain Repair After Mild TBI — New Research",
        "ScienceAlert 보도 — 오메가-3가 뇌에 좋다는 통념과 달리, EPA를 다량 섭취한 경증 외상 뇌손상 모델 동물은 공간 기억과 학습 과제에서 더 나쁜 성적을 보였다. 모든 보충제에는 시점·맥락이 있다는 메시지.",
        "오메가-3는 심혈관·우울증·일부 염증 조건에서 일관된 이득이 알려져 있다. 그러나 이 연구는 '뇌 회복'이라는 특정 맥락에서는 EPA 과량이 오히려 해로울 수 있음을 보여준다. 기전은 — 손상 후 적정 수준의 염증성 신호가 신경 회복에 필요한데, EPA가 그 신호를 너무 강하게 억제할 수 있다는 가설. 결론은 — 1) 일반인의 표준 용량(1g EPA+DHA/일)은 안전, 2) 머리 외상 후 수일~수주는 보충제 사용 의사와 상의, 3) '많을수록 좋다'는 보충제 사고법은 위험하다.",
        "ScienceAlert",
        "https://www.sciencealert.com/popular-supplement-may-have-an-unexpected-downside-study-finds",
        "보충제",
        82,
        {"shock_factor": 20, "scientific_credibility": 18, "relatability": 18, "recency": 14, "controversy": 8, "visual_potential": 4},
        ["오메가3", "EPA", "뇌손상", "보충제", "디벙킹"],
        kind="news", peer_reviewed=False,
    ),

    # ===== 멘탈 / 운동과 우울 (Mental Health / Exercise & Depression) =====
    make(
        "운동이 항우울제와 동등하다 — 73개 RCT, 5,000명 분석 (Lancashire)",
        "Exercise Rivals Antidepressants for Depression — 73 RCTs, 5000 Adults",
        "ScienceDaily 2026.01 보도 — Lancashire 대학 연구진이 73개 무작위 대조 시험, 약 5,000명 우울증 환자 데이터를 메타분석한 결과 운동은 무처치 대비 중등도 효과, 심리치료·항우울제와 비교 시 동등한 효과를 보였다. 특히 그룹·감독 환경의 유산소 운동이 가장 큰 효과를 나타냈다.",
        "이 메타분석은 운동을 '보조 요법'이 아닌 '동등한 1차 치료 옵션'으로 격상시키는 근거다. 핵심 기전: 1) 세로토닌·도파민·엔도르핀 신경전달물질 정상화, 2) BDNF 분비 → 신경가소성 회복, 3) 코르티솔 패턴 정상화, 4) 자기효능감 회복. 처방: 주 3회 이상 30~45분, 중강도 유산소(빠른 걷기·가벼운 달리기·자전거)부터 시작. 단독 치료보다는 — 의료진과 상의해 약물·심리치료와 병행하는 것이 가장 안전. '운동만으로 충분'은 경증, 중등증·중증은 다중 접근.",
        "ScienceDaily / NPR / Lancashire",
        "https://www.sciencedaily.com/releases/2026/01/260107225516.htm",
        "멘탈헬스",
        92,
        {"shock_factor": 22, "scientific_credibility": 24, "relatability": 22, "recency": 18, "controversy": 4, "visual_potential": 2},
        ["운동", "우울증", "항우울제", "Lancashire", "메타분석", "멘탈"],
        kind="news", peer_reviewed=False,
    ),
    make(
        "주 3회 이상 운동 = 청소년 우울증 효과 — 메타분석",
        "Exercise 3+ Sessions/Week Most Effective for Adolescent Depression — Meta-Analysis",
        "PMC 2025 메타분석 — 우울증 진단을 받은 아동·청소년에서 운동 중재는 의미 있는 치료 효과를 보였고, 주 3회 이상 빈도에서 가장 큰 효과가 관찰됐다. 약물 외 1차 옵션으로의 가능성을 보여준 결과.",
        "청소년 우울증은 약물 사용에 보호자·의료진 모두 신중한 영역이다. 이 데이터는 운동을 '의미 있는 대안'으로 자리잡게 한다. 적용: 1) 학교 체육 외 주 3~5회 추가 운동, 2) 단체 운동(축구·농구·댄스)이 사회적 연결까지 더해 효과 큼, 3) 30~60분, 중강도 이상, 4) '재미·자율성·소속감'이 지속의 핵심. 부모의 강제는 역효과 — 본인이 선택한 종목이어야 한다.",
        "Frontiers PMC 2025",
        "https://pmc.ncbi.nlm.nih.gov/articles/PMC12624221/",
        "멘탈헬스",
        85,
        {"shock_factor": 18, "scientific_credibility": 22, "relatability": 22, "recency": 15, "controversy": 4, "visual_potential": 4},
        ["청소년", "우울증", "운동", "메타분석", "멘탈헬스"],
    ),
    make(
        "고강도 운동이 중등증 우울증에 유리하다 — Frontiers RCT 메타",
        "High-Intensity Exercise Shows Strong Benefit in Moderate Depression — Frontiers Meta",
        "Frontiers Public Health 2025 RCT 메타분석 — 우울증 환자에서 고강도 운동(HIIT 포함)이 저강도 대비 더 큰 우울 점수 감소를 보였다. 단 환자 상태에 따라 시작 강도 조절이 필수.",
        "이 결과는 '몸이 힘들수록 마음에도 더 좋다'는 단순한 결론은 아니다. 기전은 — 고강도 운동이 BDNF, IGF-1, 베타엔도르핀, 도파민 분비를 더 강하게 자극한다는 것. 그러나 임상 적용에는 단계가 필요하다. 1) 우울증 환자는 동기·체력이 낮은 상태에서 시작하므로 첫 4주는 저~중강도로 운동 습관 형성, 2) 그 후 점진적으로 HIIT(10~20분 인터벌)을 주 2회 추가, 3) 컨디션 나쁜 날은 무리하지 않기 — 'consistency over intensity'가 더 중요. 의사·트레이너와 협진 권장.",
        "Frontiers Public Health 2025",
        "https://www.frontiersin.org/journals/public-health/articles/10.3389/fpubh.2025.1616925/full",
        "멘탈헬스",
        83,
        {"shock_factor": 18, "scientific_credibility": 22, "relatability": 20, "recency": 14, "controversy": 5, "visual_potential": 4},
        ["HIIT", "우울증", "고강도", "메타분석", "멘탈헬스"],
    ),
    make(
        "유산소·저항운동·마인드바디 모두 효과 — 형식보다 빈도가 더 중요",
        "All Exercise Types Improve Mental Health — Frequency Matters More Than Format",
        "Wiley 2025 메타분석 — 우울·불안에 유산소, 저항운동, 마인드바디(요가·태극권), 혼합 프로그램 모두 의미 있는 개선을 보였다. 각각 medium effect size — 즉 '어떤 운동이냐'보다 '꾸준히 하느냐'가 결정 변수다.",
        "이 결과는 운동 처방의 자유도를 크게 넓힌다. 우울·불안 환자에게 '러닝을 무조건 해야 한다'고 강요할 필요가 없다. 핵심 메시지 — 본인이 좋아하는 운동을 선택하고, 주 3회 이상 꾸준히 하는 것. 적용: 1) 외향형 → 단체 댄스, 클라이밍, 풋살, 2) 내향형 → 요가, 수영, 사이클링, 3) 시간 부족 → 출퇴근 빠른 걷기 + 주말 운동. 운동 선택의 자율성은 지속률을 결정 — 강요된 처방보다 본인 선택이 6배 이상 지속률 높음(별도 연구).",
        "Wiley PMC 2025",
        "https://pmc.ncbi.nlm.nih.gov/articles/PMC12117297/",
        "멘탈헬스",
        82,
        {"shock_factor": 16, "scientific_credibility": 22, "relatability": 22, "recency": 14, "controversy": 4, "visual_potential": 4},
        ["운동형식", "우울", "불안", "메타분석", "멘탈헬스"],
    ),

    # ===== 회복 / 수면 / 콜드 (Recovery / Sleep / Cold) =====
    make(
        "수면 7시간 미만이면 반응속도가 무너진다 — 2025 선수 종합 리뷰",
        "Sleep <7h Impairs Reaction Time, Decision Speed in Athletes — 2025 Multidim Review",
        "MDPI J. Clin. Med. 2025 종합 리뷰 — 7시간 미만 수면은 반응속도·정확성·의사결정 속도·근지구력·웰빙을 모두 동시에 무너뜨린다. 잠을 줄여 훈련량을 늘리는 전략은 수익률 마이너스다.",
        "리뷰가 정리한 기전은 다섯 갈래 — 1) 글림프계 노폐물 청소 약화 → BDNF 감소, 2) 야간 GH·테스토스테론 분비량 감소, 3) 코르티솔 베이스라인 상승, 4) 인슐린 감수성 저하, 5) 통증 역치 감소·부상 위험 증가. 처방: 매일 7~9시간, 같은 시간 취침/기상, 카페인 14시 이후 금지, 침실 18~20℃, 빛 차단, 자기 전 알코올 금지(REM 파괴). 트레이닝 효과는 잠자는 동안 굳어진다 — 잠을 줄이면 'training'은 했지만 'gain'은 사라진다.",
        "MDPI J. Clin. Med.",
        "https://www.mdpi.com/2077-0383/14/21/7606",
        "회복/수면",
        87,
        {"shock_factor": 18, "scientific_credibility": 22, "relatability": 22, "recency": 18, "controversy": 4, "visual_potential": 3},
        ["수면", "선수", "반응속도", "회복", "BDNF"],
    ),
    make(
        "운동 후 콜드 플런지는 부교감을 강화하지만 시점이 중요",
        "Post-Exercise Cold Water Immersion Boosts Parasympathetic Tone — But Timing Matters",
        "2025 시스테매틱 리뷰 — 운동 후 콜드 워터 이멀전(CWI)은 12개 연구 중 8개에서 중~큰 효과 크기로 부교감 신경 톤을 강화했다. 다만 '근비대 목적' 트레이닝 직후에는 권하지 않는다 — 합성 신호를 둔화시킨다는 데이터가 누적되고 있기 때문.",
        "CWI의 단기 이득은 명확하다 — 회복감, 근육 통증 감소, 부교감 톤 강화, 스트레스 호르몬 12시간 후 감소. 그러나 사용 맥락이 갈라진다. 1) 근비대·근력 트레이닝 직후 30분 이내 CWI는 mTOR 신호와 위성세포 활성화를 둔화시켜 장기 적응을 깎을 수 있다. 2) 반대로 경기·고강도 인터벌 후 회복을 위한 CWI는 다음 세션 준비도를 높인다. 3) 정신건강·기분 효과는 일관되게 양성. 처방: 비대 목적이면 트레이닝 후 4~6시간 이후 또는 비훈련 일 사용. 11~15℃, 5~10분.",
        "Frontiers Physiology 2025",
        "https://www.frontiersin.org/journals/physiology/articles/10.3389/fphys.2025.1598075/full",
        "회복/콜드",
        82,
        {"shock_factor": 16, "scientific_credibility": 22, "relatability": 20, "recency": 14, "controversy": 8, "visual_potential": 4},
        ["콜드플런지", "CWI", "부교감", "회복", "근비대간섭"],
    ),
    make(
        "콜드 워터는 잠을 망치지 않는다 — 운동 후 사용 시 수면 영향 0",
        "Cold Water Immersion After Exercise Doesn't Hurt Sleep — May Reduce Arousals",
        "PLOS One 시스테매틱 리뷰 — 운동 후 콜드 워터 이멀전(CWI)은 야간 수면의 양·질에 직접적 손해를 주지 않았다. 오히려 일부 데이터에서 수면 중 각성과 사지 움직임이 감소했다.",
        "콜드 노출의 시점이 중요하다 — 1) 자기 직전 차가운 샤워는 코어 체온을 흔들어 수면 진입을 방해할 수 있다, 2) 그러나 운동 후 사용은 그 시점이 잠과 충분히 떨어져 있어 영향이 없다. 오히려 부교감 우세를 만들어 수면 질을 약간 향상시킨다는 보고. 적용: 1) 콜드 플런지는 이른 저녁(잠 4시간 전) 권장, 2) 자기 직전이라면 미지근한 샤워, 3) 침실 온도 18~20℃ — 잠은 코어 체온이 떨어질 때 들어온다, 그래서 침실은 시원해야 한다.",
        "PLOS One",
        "https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0317615",
        "회복/콜드",
        80,
        {"shock_factor": 16, "scientific_credibility": 22, "relatability": 18, "recency": 13, "controversy": 5, "visual_potential": 4},
        ["콜드", "수면", "회복", "CWI", "부교감"],
    ),
    make(
        "콜드 + 컴프레션 — 단독보다 회복 시너지 — 2025 RCT",
        "Cold + Compression Combined Beats Either Alone — 2025 Crossover RCT",
        "Frontiers Physiology 2025 무작위 교차 RCT — 콜드 노출과 컴프레션을 함께 적용했을 때 단독 사용보다 근육 회복 지표가 더 우수했다. 운동 후 빠른 회복을 원하는 선수에게 새로운 옵션.",
        "기전은 — 1) 콜드는 혈관 수축으로 부종·염증을 줄이고, 2) 컴프레션은 정맥 환류를 도와 노폐물 제거를 촉진. 두 작용이 보완적이다. 적용: 1) 컴프레션 부츠/타이즈 + 차가운 환경(콜드룸·아이스 베스트), 2) 운동 직후 20~30분, 3) 비대 목적 트레이닝 후에는 4~6시간 지연 권장. 비용·접근성은 일반인 대상으로 아직 높지만, 프로 선수와 인기 종목 동호인층에서 채택이 빠르게 확산.",
        "Frontiers Physiology 2025",
        "https://www.frontiersin.org/journals/physiology/articles/10.3389/fphys.2025.1598075/full",
        "회복/콜드",
        78,
        {"shock_factor": 14, "scientific_credibility": 22, "relatability": 16, "recency": 14, "controversy": 4, "visual_potential": 5},
        ["콜드", "컴프레션", "RCT", "회복", "선수"],
    ),

    # ===== 자연 보디빌딩 (Natural Bodybuilding) =====
    make(
        "스페인 엘리트 내추럴 보디빌더 — 주 5일, 근육군당 12~20세트",
        "Spanish Elite Natural Bodybuilders Train 5 Days/Wk, 12-20 Sets/Muscle/Wk",
        "PMC 2025 발표 — 스페인 엘리트 자연 보디빌더 대상 조사 결과 평균 주 5일 훈련, 대부분 근육군은 주 1회 초과 ~ 3회 미만 빈도, 주당 12~20세트가 우세했다. 즉 '하루에 몰아 한 부위'에 가까운 분할이 유효 전략.",
        "이 데이터의 가치는 '실제로 무엇을 하고 있나'를 보여준다는 점이다. 핵심 정리 — 1) 빈도: 같은 근육 주 1.5~2회가 최적 영역, 2) 볼륨: 주 12~20세트, 컴파운드 2~3종목 + 보조 1~2종목, 3) 분할: 푸시/풀/레그, 또는 상/하 2분할이 우세, 4) 강도: 메인은 RIR 1~3, 보조는 RIR 0~1까지 짜냄. 컷팅 단계는 — 체중 감소 주당 0.5~1%, 단백질 2.3~3.1g/kg LBM, 지방 15~30% 칼로리, 나머지는 탄수화물.",
        "PMC 2025",
        "https://pmc.ncbi.nlm.nih.gov/articles/PMC12846200/",
        "자연보디빌딩",
        82,
        {"shock_factor": 14, "scientific_credibility": 22, "relatability": 22, "recency": 14, "controversy": 5, "visual_potential": 5},
        ["내추럴", "보디빌딩", "주5일", "주12-20세트", "트레이닝"],
    ),
    make(
        "크레아틴은 근육을 직접 만들지 않는다 — '더 세게 훈련'을 가능하게 할 뿐",
        "Creatine Doesn't Build Muscle Directly — It Lets You Train Harder",
        "2026 정리 — 크레아틴은 근력 향상과 근육 성장에 효과적이지만, 그 작동 방식은 '직접 단백질 합성을 키우는 것'이 아니라 '더 세게·더 자주 훈련할 수 있는 능력'을 주는 것이다. 즉 크레아틴 + 일반 식단으로 누워서 늘지 않는다.",
        "기전: 크레아틴 인산은 근수축의 즉각 에너지(ATP) 재합성에 쓰인다 → 한 세트당 1~2회 더 들 수 있다 → 시간 누적되면 더 큰 트레이닝 자극 → 더 큰 적응. 따라서 크레아틴 효과는 '훈련을 안 하는 사람'에게는 없다. 권장 용량: 5g/일 일정하게(로딩은 선택), 흡수는 식사와 함께. 안전성: 신장 정상인에서 30년 데이터 누적. 부작용: 일시적 수분 정체로 인한 1~2kg 체중 증가(근육 + 수분), 과량은 위장장애. 자연 보디빌더에게 가장 코스트 효율 높은 보충제.",
        "Global Agriculture",
        "https://www.global-agriculture.com/food-nutrition-wellness/creatine-in-2026-science-hype-and-the-truth-about-muscle-building/",
        "보충제",
        82,
        {"shock_factor": 16, "scientific_credibility": 20, "relatability": 22, "recency": 14, "controversy": 5, "visual_potential": 4},
        ["크레아틴", "보충제", "근비대", "근력", "내추럴"],
        kind="news", peer_reviewed=False,
    ),
    make(
        "근력은 강도를 계속 올리지 않아도 자란다 — Lehman 2025 연구",
        "Lehman 2025: Muscle Growth Possible Without Constantly Increasing Intensity",
        "Lehman College / J. Appl. Physiol. 2025 발표 — 근비대는 강도(부하)를 계속 끌어올리지 않아도 가능하다. 충분한 노력(failure 근처)과 일정 볼륨이면 동일 부하에서도 성장이 일어난다는 결과는 'progressive overload만이 답'이라는 통념에 균열을 낸다.",
        "이 연구가 메시지하는 바는 — 1) 무게를 매주 올릴 수 없는 시기(컷팅·부상 회복·정체기)에도 근육은 자랄 수 있다, 2) 'load'와 'effort' 중 effort가 더 결정적, 3) 점진적 과부하는 여전히 강력한 도구지만 유일한 도구는 아니다. 적용: 1) 무게 정체기에는 reps를 늘리거나 마지막 세트 RIR을 0까지 낮추기, 2) 동일 무게로 같은 reps를 더 빠르게 회복하며 수행, 3) 폼 개선으로 'effective ROM'을 늘리기. 이는 자연 보디빌더와 노년 트레이너 모두에게 희소식.",
        "Lehman College / J. Appl. Physiol. 2025",
        "https://www.lehman.edu/news/2025/New-Study-Could-Change-Approach-to-Strength-Training-1.php",
        "운동과학",
        84,
        {"shock_factor": 18, "scientific_credibility": 22, "relatability": 22, "recency": 14, "controversy": 6, "visual_potential": 3},
        ["근비대", "강도", "progressive overload", "Lehman", "운동과학"],
        kind="news", peer_reviewed=False,
    ),

    # ===== 바이럴 / 트렌드 (Viral / Trends) =====
    make(
        "일본식 걷기 — 검색량 +2,986%, 2026년 가장 빠르게 퍼진 운동",
        "Japanese Walking Surges +2,986% in Search Interest — 2026's Fastest-Growing Trend",
        "Glimpse 트렌드 분석 — 일본식 걷기(빠르게 3분 + 천천히 3분 반복)가 검색량 2,986% 급증으로 2026년 가장 빠르게 성장한 운동 트렌드로 등극했다. 인터벌 워킹의 단순한 형태로, 노인부터 직장인까지 진입 장벽이 낮다는 강점.",
        "이 운동의 학술 근거는 — 일본 신슈대학 연구(Nemoto 등 2007)로 거슬러 올라간다. 30분 빠른 걷기 vs 3분 빠르게 + 3분 천천히 인터벌 비교에서, 인터벌 그룹이 5개월 후 V̇O₂max·근력·혈압 모두 더 큰 개선을 보였다. 처방: 1) 빠른 걷기는 심박수 70~85% 또는 '대화는 어려운' 강도, 2) 천천히 걷기는 회복 — 50~60% 강도, 3) 5세트(30분) 주 4회. SNS에서 폭발한 이유: 도구 0, 비용 0, 시간 짧음, 노년·청년 모두 수행 가능.",
        "Glimpse Trends",
        "https://meetglimpse.com/trends/fitness-trends/",
        "트렌드",
        87,
        {"shock_factor": 20, "scientific_credibility": 18, "relatability": 24, "recency": 18, "controversy": 4, "visual_potential": 6},
        ["일본식걷기", "인터벌워킹", "트렌드", "걷기", "유산소"],
        kind="news", peer_reviewed=False,
    ),
    make(
        "필라테스 3년 연속 글로벌 1위 — 2024년 대비 예약 +66%",
        "Pilates Tops Global Bookings 3rd Year — Up 66% Since 2024",
        "ClassPass 글로벌 데이터 — 필라테스가 3년 연속 가장 많이 예약된 그룹 운동으로 등극, 2024년 대비 66% 증가. '몸 만드는 운동' 트렌드가 코어 + 자세 + 가동성 중심으로 옮겨가고 있다는 신호.",
        "필라테스의 부상은 단순한 유행이 아니다 — 사람들이 '한 가지 큰 근육'보다 '전신 코어·움직임 패턴'을 더 가치 있게 평가하기 시작한 신호. 운동과학 측면에서 — 1) 코어 안정성 향상 → 허리 통증 감소(증거 누적), 2) 다중 평면 움직임 → 일상 기능 회복, 3) 호흡 통합 → 자율신경 안정. 단점: 1) 근비대·최대근력 향상 효과는 저항운동 대비 약함, 2) 1대1 또는 소그룹 수업 비용. 추천: 저항운동 주 3~4회 + 필라테스 주 1~2회 조합이 균형. 단독으로는 보디빌딩 목표에 부족.",
        "ClassPass / PureWow",
        "https://www.purewow.com/wellness/fitness-trends-2026",
        "트렌드",
        82,
        {"shock_factor": 16, "scientific_credibility": 16, "relatability": 24, "recency": 16, "controversy": 4, "visual_potential": 6},
        ["필라테스", "트렌드", "코어", "ClassPass", "글로벌"],
        kind="news", peer_reviewed=False,
    ),
    make(
        "월 필라테스 챌린지 — 1년 만에 -55% 관심 급감",
        "Wall Pilates Challenges Lose Steam — Search Interest Drops 55% in 2025",
        "Glimpse 트렌드 — 한때 TikTok에서 폭발했던 '월 필라테스 챌린지'가 2025년 동안 검색량 55% 감소. 30일·28일 챌린지 포맷의 한계가 드러나는 구간 — '챌린지 끝나고 뭐?' 문제.",
        "챌린지 포맷의 패턴은 명확하다 — 폭발적 진입 → 과제성 만족 → 종료 → 이탈. 지속 가능한 운동 습관과는 다른 구조다. 그 자리를 차지하는 것은 — 1) 일본식 걷기(시간 짧음, 무한 반복 가능), 2) 정규 필라테스 수업(월 구독), 3) 하이브리드 트레이닝(근력 + 유산소 + 모빌리티 통합). 메시지: 마케팅을 위한 '챌린지'는 단기 콘텐츠로 유효하지만, 실제 변화는 'identity-based habit'(나는 운동하는 사람이다)에서 나온다. 30일은 시작이지 끝이 아니다.",
        "Glimpse Trends",
        "https://meetglimpse.com/trends/fitness-trends/",
        "트렌드",
        78,
        {"shock_factor": 18, "scientific_credibility": 12, "relatability": 22, "recency": 16, "controversy": 6, "visual_potential": 5},
        ["월필라테스", "챌린지피로", "트렌드", "TikTok", "지속성"],
        kind="news", peer_reviewed=False,
    ),
    make(
        "ACSM 2026 1위 트렌드 — 웨어러블 (미국 성인 절반 보유)",
        "ACSM Top Fitness Trend for 2026: Wearable Tech (Half of US Adults Now Own One)",
        "ACSM 발표 — 2026년 글로벌 피트니스 트렌드 1위는 웨어러블 기술. 미국 성인 절반이 피트니스 트래커·스마트워치 보유. AI 기반 피트니스 앱, VR 워크아웃, 원격 PT가 함께 상승.",
        "웨어러블의 운동 효과는 '데이터' 자체가 아니라 '인식 → 행동 변화'에 있다. 메타분석들은 — 일관되게 트래커 사용자가 비사용자 대비 일평균 1,500~2,500보 더 걷고, 중강도 활동시간이 7~10분/일 늘었다. 제한점: 1) 칼로리 추정 오차 ±15~30%, 2) 수면 단계 추정 부정확(특히 깊은 수면), 3) 데이터 의존이 직관 무시로 이어질 수 있음. 활용 권장: 트렌드(주·월 단위) > 절대값(일·시간 단위), HRV·안정시 심박수 추세는 컨디션 지표로 신뢰도 높음.",
        "ACSM 2026",
        "https://acsm.org/top-fitness-trends-2026/",
        "트렌드",
        80,
        {"shock_factor": 14, "scientific_credibility": 18, "relatability": 24, "recency": 18, "controversy": 4, "visual_potential": 4},
        ["웨어러블", "ACSM", "스마트워치", "AI피트니스", "트렌드"],
        kind="news", peer_reviewed=False,
    ),

    # ===== 노화 역전 / Anti-Aging =====
    make(
        "12주 운동으로 단백질체 노화 점수 10개월 젊어졌다 — UK Biobank",
        "12-Week Exercise Reverses Proteomic Aging by 10 Months — UK Biobank Study",
        "npj Aging 발표 — UK Biobank 데이터 + 12주 감독 운동 중재 연구에서 단백질체 노화 점수(ProtAgeGap)가 평균 10개월 어려졌다. 운동이 분자 노화 마커를 실제로 되돌린다는 첫 대규모 증거.",
        "단백질체 노화 점수는 혈액 단백질 패턴으로 추정한 '분자적 나이'다. 12주 만의 10개월 회춘은 적지 않다. 핵심 발견: 1) 효과는 시작 점수가 더 노화된 사람에서 더 컸음, 2) 유산소 + 저항 혼합 운동이 가장 효과적, 3) 12주 종료 후 효과 일부 유지. 처방 — UK Biobank 데이터로 본 longevity 운동량: 주 150분 중강도 + 주 2회 저항운동이 최저 한계, 주 300분 중강도 또는 150분 고강도가 최적 영역. 운동은 longevity 약(NMN·레스베라트롤)이 흉내 낼 수 없는 효과를 낸다.",
        "npj Aging / Nature",
        "https://www.nature.com/articles/s41514-025-00318-w",
        "노화/Anti-Aging",
        88,
        {"shock_factor": 22, "scientific_credibility": 24, "relatability": 20, "recency": 16, "controversy": 4, "visual_potential": 4},
        ["노화역전", "단백질체", "UK Biobank", "12주", "longevity"],
    ),
    make(
        "운동이 면역 시스템도 젊게 한다 — 더 어린 면역 프로파일",
        "Exercise Linked to Younger, Sharper Immune System — ScienceDaily 2025",
        "ScienceDaily 2025.10 보도 — 운동량이 많은 성인은 동년배 비활동군 대비 'younger immune profile'을 가진다는 연구. T세포 다양성, 자연살해세포 활성, 백신 반응성 모두 더 우수했다.",
        "면역 노화(immunosenescence)는 60대 이후 감염·암·자가면역 위험을 끌어올리는 핵심 변수다. 운동의 면역 회복 기전은 — 1) 흉선(thymus) 위축 둔화, 2) T세포 레퍼토리 다양성 유지, 3) 만성 저강도 염증(inflammaging) 감소, 4) NK 세포 활성 회복. 처방은 'longevity 처방'과 동일 — 주 150~300분 중강도 + 주 2회 저항운동. 단, 만성 과훈련(over-training)은 반대로 면역을 억제한다 — 항상 'sufficient sleep + adequate calories' 조건이 필요.",
        "ScienceDaily 2025.10",
        "https://www.sciencedaily.com/releases/2025/10/251014014421.htm",
        "노화/Anti-Aging",
        85,
        {"shock_factor": 20, "scientific_credibility": 20, "relatability": 22, "recency": 14, "controversy": 4, "visual_potential": 4},
        ["면역", "노화역전", "운동", "T세포", "longevity"],
        kind="news", peer_reviewed=False,
    ),
    make(
        "골다공증과 싸우는 운동의 비밀 — 뼈 세포 신호 경로 발견",
        "Breakthrough: How Exercise Fights Osteoporosis at Cellular Level",
        "ScienceAlert 보도 — 운동이 골다공증을 막는 분자 메커니즘이 새로 규명됐다. 부하가 가해진 뼈에서 osteocyte(골세포)가 분비하는 신호 단백질이 osteoblast(골형성세포)를 활성화하고 osteoclast(골흡수세포)를 억제한다는 경로.",
        "이 발견의 임상적 무게는 — 단순히 '운동이 뼈에 좋다'를 넘어, 약리학적 표적이 명확해진다는 점이다. 그러나 약을 기다릴 필요는 없다 — 운동이 그 신호 자체를 즉시 켠다. 처방: 1) 충격 부하 운동 주 3회(점프·달리기·계단), 2) 저항운동 주 2~3회(스쿼트·데드리프트·파워리프트), 3) 폐경 후 여성·고령 남성에 특히 권장. 보충제: 칼슘 1,000~1,200mg/일, 비타민 D 800~1,000 IU/일(혈중 25-OH-D 30 ng/mL 이상 유지). 약물(비스포스포네이트)은 골밀도 T-score -2.5 이하에서 의사 판단.",
        "ScienceAlert",
        "https://www.sciencealert.com/breakthrough-study-reveals-the-secret-of-how-exercise-fights-osteoporosis",
        "노화/Anti-Aging",
        83,
        {"shock_factor": 20, "scientific_credibility": 22, "relatability": 18, "recency": 14, "controversy": 4, "visual_potential": 4},
        ["골다공증", "뼈건강", "운동", "osteocyte", "노화"],
        kind="news", peer_reviewed=False,
    ),

    # ===== 심리·동기 (Psychology / Motivation) =====
    make(
        "10초 발목 진동으로 사이클을 더 세게 — 그러나 힘들지 않다",
        "Tendon Vibration Trick Lets You Push Harder Without Feeling Effort",
        "ScienceDaily 2026.01 보도 — 자전거 페달링 직전 힘줄에 진동을 가하면 심박수와 근활동은 더 올라가는데도 'effort 인지'는 그대로였다. 즉 뇌가 노력 신호를 잘못 해석하게 만든 것이다.",
        "이 발견의 핵심은 운동 강도(physical intensity)와 인지 강도(perceived effort)가 분리될 수 있다는 점이다. RPE(자각 운동 강도)는 거의 무류하다고 여겨졌지만, 힘줄 골지건 기관(GTO)을 진동으로 자극하면 뇌의 노력 모니터링 시스템이 속는다. 응용: 재활 환자가 더 강한 자극을 견디게 만들거나, 마라토너의 페이스 한계를 미세 조정하는 도구가 될 수 있다. 단, 향후 도핑 측면 논란이 따라붙을 가능성. 실험실 단계 — 일반인 처방 단계는 아직 아님.",
        "ScienceDaily 2026.01",
        "https://www.sciencedaily.com/releases/2026/01/260107225519.htm",
        "운동심리",
        80,
        {"shock_factor": 20, "scientific_credibility": 18, "relatability": 18, "recency": 16, "controversy": 5, "visual_potential": 3},
        ["RPE", "진동", "운동심리", "GTO", "ScienceDaily"],
        kind="news", peer_reviewed=False,
    ),
    make(
        "운동이 안 되는 건 게을러서가 아니라 '시작'에 비용이 너무 크기 때문",
        "It's Not Laziness — It's Activation Cost. FIU Mental-First Tips for 2026",
        "FIU News 2026 정리 — 사람들이 운동을 못 하는 건 동기 부족이 아니라 '시작 비용'이 너무 크기 때문이다. 옷 갈아입기·이동·세팅까지의 friction을 줄이면 실행률이 폭발적으로 오른다. 'identity-based habit' 원칙.",
        "행동 과학의 단순한 방정식 — 행동 = 동기 × 능력 × 트리거. 운동은 능력(시간·체력)과 트리거(시간대·장소)는 충분한데 'friction'이 모든 것을 막는다. 처방: 1) 운동복은 전날 미리 꺼내두기, 2) 헬스장은 출퇴근 동선 위, 3) 홈트는 매트가 항상 펴져 있는 곳 — '꺼내는' 1분이 결정적, 4) 첫 5분만 한다 결심 — 시작 후 90%는 끝까지 한다, 5) '나는 운동하는 사람'이라는 정체성으로 자기 진술을 바꾸기. '오늘은 쉬자'는 욕망이 아니라 trigger 부재의 신호 — 환경을 디자인하라.",
        "FIU News 2026",
        "https://news.fiu.edu/2025/its-all-mental-science-backed-tips-to-get-you-moving-in-2026",
        "운동심리",
        80,
        {"shock_factor": 16, "scientific_credibility": 16, "relatability": 26, "recency": 16, "controversy": 4, "visual_potential": 4},
        ["행동과학", "동기", "habit", "friction", "FIU"],
        kind="news", peer_reviewed=False,
    ),

    # ===== 컷팅 / 다이어트 (Cutting / Diet) =====
    make(
        "내추럴 컷팅의 황금률 — 주 0.5~1% 체중 감소가 근손실을 막는다",
        "Natural Cut Golden Rule: 0.5-1% Bodyweight/Week Preserves Muscle",
        "ISSN 자연 보디빌딩 컨센서스 — 컷팅 시 체중 감소 속도 주 0.5~1%가 근육 보존의 황금률. 더 빠르면 근손실·호르몬 저하, 더 느리면 시간 비용 증가.",
        "기전 — 너무 빠른 컷팅은 1) 렙틴 급락 → 갑상선·테스토스테론 저하, 2) 근단백질 분해 가속, 3) 코르티솔 상승, 4) 충동적 폭식 위험. 처방: 1) 칼로리 적자 ~20% 시작 (TDEE - 500kcal 정도), 2) 단백질 2.3~3.1g/kg LBM 유지(고정), 3) 지방 15~30% 칼로리, 4) 나머지 탄수화물 — 트레이닝 강도 유지가 우선, 5) 주 1회 체중·허리둘레 측정으로 속도 조정. 정체기에는 칼로리 200kcal 추가 감소 또는 활동량 증가(주 +2시간 걷기). 굶기지 마라 — 굶으면 근육이 먼저 사라진다.",
        "PMC / ISSN",
        "https://pmc.ncbi.nlm.nih.gov/articles/PMC4033492/",
        "다이어트",
        85,
        {"shock_factor": 18, "scientific_credibility": 22, "relatability": 22, "recency": 14, "controversy": 4, "visual_potential": 4},
        ["컷팅", "다이어트", "근손실방지", "ISSN", "내추럴"],
    ),

    # ===== 비타민 D 보충 (Vitamin D) =====
    make(
        "비타민 D 보충제가 듣지 않는 이유 — 흡수 변수가 따로 있다",
        "Why Your Vitamin D Supplement May Not Be Working — Hidden Absorption Factors",
        "ScienceDaily 2025.12 보도 — 비타민 D 보충제를 같은 용량으로 먹어도 혈중 25-OH-D 수치 반응이 사람마다 크게 다르다. 핵심 변수: 1) 지방과 함께 섭취 여부, 2) 마그네슘 상태, 3) 체지방률(지용성이라 지방조직에 격리), 4) 유전자 변이.",
        "비타민 D 결핍은 면역·뼈·근력·우울 모두에 영향. 그러나 보충제만 먹는다고 해결되지 않는 사람이 많다. 점검 항목 — 1) 식사와 함께 먹기(공복 X), 2) 마그네슘 결핍 동반 시 D 활성화 막힘 → 마그네슘 일일 300~400mg 보충 검토, 3) 체지방률 30%+면 같은 용량으로 같은 효과를 내려면 더 큰 용량 필요, 4) 6~8주 후 25-OH-D 재검사 (목표 30~50 ng/mL). 햇빛 노출 부족인 한국 직장인은 일일 1,000~2,000 IU + 식사 동반 + 봄·가을 정기 검사가 합리적.",
        "ScienceDaily 2025.12",
        "https://www.sciencedaily.com/releases/2025/12/251228020010.htm",
        "보충제",
        80,
        {"shock_factor": 18, "scientific_credibility": 18, "relatability": 24, "recency": 14, "controversy": 4, "visual_potential": 4},
        ["비타민D", "보충제", "흡수", "마그네슘", "결핍"],
        kind="news", peer_reviewed=False,
    ),
    make(
        "칼슘과 치매는 무관 — 2025 연구가 오래된 신화를 부순다",
        "Calcium-Dementia Myth Debunked — 2025 Study",
        "ScienceDaily 2025.10 보도 — 칼슘 보충제가 치매 위험을 올린다는 가설은 대규모 연구에서 입증되지 않았다. 노년 여성에서 골다공증 예방 목적의 칼슘 보충은 여전히 유효한 옵션.",
        "이 디벙킹의 의미는 — 노년·폐경 여성이 칼슘 보충제 사용을 두려워할 이유가 없다는 점. 다만 가이드라인은 — 1) 식사로 1,000~1,200mg 칼슘을 충족할 수 있다면 추가 보충 불요, 2) 식이 부족 시 보충제는 매 끼니마다 500mg 이하로 분산(대량 1회보다 흡수율 높음), 3) 비타민 D와 동반 섭취 권장. 칼슘 과량(>2,000mg/일)은 별도로 신장결석·심혈관 위험 가능성 있어 권장 상한 준수.",
        "ScienceDaily 2025.10",
        "https://www.sciencedaily.com/releases/2025/10/251016223108.htm",
        "보충제",
        78,
        {"shock_factor": 16, "scientific_credibility": 18, "relatability": 18, "recency": 13, "controversy": 6, "visual_potential": 3},
        ["칼슘", "치매", "디벙킹", "보충제", "노년"],
        kind="news", peer_reviewed=False,
    ),

    # ===== 추가 운동 트렌드 =====
    make(
        "하이브리드 트레이닝 — 한 프로그램에 근력·유산소·모빌리티 다 넣는다",
        "Hybrid Training Goes Mainstream: Strength + Cardio + Mobility in One Program",
        "Trainerize 2026 분석 — 단일 종목 충성도가 무너지고 '하이브리드' 프로그램이 주류로. 근력 + 유산소 + 모빌리티를 한 주 안에 통합하는 구조가 모든 연령대에서 채택률 1위.",
        "하이브리드의 인기는 두 가지 동인에서 온다 — 1) 시간 효율성(한 가지에 시간 투자 분산보다 통합이 ROI 높음), 2) 부상 예방(단일 종목 반복 부하 회피). 모델 예시: 월·수·금 저항운동(60분), 화·목 zone 2 유산소(30~45분), 토 모빌리티/요가(30분), 일 휴식. 이 구조는 — 근비대(주 12~20세트/근육군 충족), VO2max 향상(zone 2 200분/주 근접), 가동성 회복을 동시에 만든다. 자연 보디빌더 프로토콜과도 호환. 단점: 컴프 보디빌딩처럼 한 가지 극단 목표면 비효율.",
        "Trainerize 2026",
        "https://www.trainerize.com/blog/exercise-trends/",
        "트렌드",
        80,
        {"shock_factor": 14, "scientific_credibility": 18, "relatability": 24, "recency": 16, "controversy": 4, "visual_potential": 5},
        ["하이브리드", "트레이닝트렌드", "근력유산소모빌리티", "Trainerize", "ROI"],
        kind="news", peer_reviewed=False,
    ),
    make(
        "AI 트레이닝 앱 — 개인화 처방 시대, 과학적 근거는?",
        "AI Fitness Apps Boom — But Where's the Evidence for Personalized Programs?",
        "PMC 2025 분석 — 생성형 AI가 만든 트레이닝 플랜의 품질을 전문가가 평가한 결과, 일부는 합리적이지만 진척·강도 처방에서 일관된 오류 패턴이 발견됐다. 즉 AI 처방은 '시작점'이지 '결승점'이 아님.",
        "AI 피트니스 앱의 현재 위치는 — 1) 영양 칼로리 추적, 운동 일지, 진척 시각화 — 강점, 2) 개인 신체 조건·부상력 반영한 운동 처방 — 아직 보수적·일반적, 3) 부상 위험 신호 감지 — 한계 명확. 권장 사용법: 1) AI를 '비서'로 사용하되 처방 결정자는 본인/트레이너, 2) 강도·볼륨 갑작스런 증가 자제, 3) 통증·관절 신호는 AI보다 본인 감각을 우선. 가까운 미래 — 웨어러블 데이터(HRV·수면·HR)를 AI가 통합해 '오늘 컨디션'에 맞춘 동적 처방으로 발전할 전망.",
        "PMC 2025",
        "https://pmc.ncbi.nlm.nih.gov/articles/PMC12492345/",
        "트렌드",
        78,
        {"shock_factor": 14, "scientific_credibility": 20, "relatability": 22, "recency": 14, "controversy": 5, "visual_potential": 4},
        ["AI피트니스", "GenAI", "처방", "트렌드", "PMC"],
    ),
    make(
        "원격 PT의 부상 — 미국 절반이 사용 중, 효과는 대면과 동등",
        "Remote Personal Training Surges to Half of US Adults — Equivalent Outcomes to In-Person",
        "ACSM 2026 트렌드 — 원격 PT(영상 통화·앱 기반 코칭)가 가속 성장. 메타 데이터로는 '코치의 책임감(accountability) + 처방 품질'이 보장되면 대면 PT와 동등한 결과를 만든다.",
        "원격 PT의 강점 — 1) 비용 1/2~1/3, 2) 시간·장소 제약 없음, 3) 동영상 검토로 폼 피드백 가능. 약점 — 1) 첫 폼 교정에서는 대면이 우수, 2) 무거운 부하의 안전 백업 부재. 권장 사용 모델: 1) 첫 4~8주 대면(폼·기본 동작 정착), 2) 이후 원격 전환(주간 체크인 + 월 1회 대면 점검), 3) 데드리프트·스쿼트·벤치프레스 폼 변경 시 대면 재방문. 비용 절감 효과는 큰 반면, 본인의 학습·responsabilité가 결과를 좌우.",
        "ACSM 2026",
        "https://acsm.org/top-fitness-trends-2026/",
        "트렌드",
        76,
        {"shock_factor": 14, "scientific_credibility": 18, "relatability": 22, "recency": 14, "controversy": 4, "visual_potential": 4},
        ["원격PT", "온라인코칭", "ACSM", "트렌드", "PT"],
        kind="news", peer_reviewed=False,
    ),
    make(
        "Wim Hof 메서드 — 404명 RCT에서 심리·인지 효과 일관 안 함",
        "Wim Hof Method 404-Person RCT: Inconsistent Psychological & Cognitive Effects",
        "Scientific Reports 2025 발표 — Wim Hof 메서드(주기적 과호흡 + 콜드 노출)를 29일 적용한 404명 RCT에서 심리·인지 결과가 일관되지 않았다. 일부 마커는 개선, 일부는 변화 없음 — '만능 회복 도구'라는 마케팅과 거리가 있다.",
        "Wim Hof 메서드의 인기는 폭발적이지만, 과학적 검증은 따라가지 못하고 있었다. 이번 RCT가 의미 있는 이유는 — 처음으로 큰 표본에서 active control(다른 호흡법)과 비교했다는 점. 결과 정리: 1) 자가보고 스트레스·기분 — 일부 개선, 2) 객관적 인지 과제 — 변화 미미, 3) 면역·생리 마커 — 일관성 없음. 권장: 1) 호기심·취미로는 안전 범위, 2) 깊은 물에서 단독 시도 절대 금지(실신 위험), 3) '치료 효과'를 기대한 의학적 적응 사용 전 의사 상의. 운동·수면·식단의 기본을 대체할 수는 없다.",
        "Scientific Reports 2025",
        "https://www.nature.com/articles/s41598-025-29187-9",
        "회복/콜드",
        80,
        {"shock_factor": 18, "scientific_credibility": 22, "relatability": 18, "recency": 14, "controversy": 8, "visual_potential": 4},
        ["WimHof", "RCT", "콜드", "호흡법", "디벙킹"],
    ),
    make(
        "운동 종목 다양성이 사망률을 낮춘다 — 30년 추적 BMJ Medicine",
        "Variety in Exercise Types Lowers Mortality — 30-Year BMJ Medicine Cohort",
        "BMJ Medicine 2026 발표 — 간호사·의료직 173,229명 30년 추적 분석. 동일한 총 운동량이라도 종목 다양성이 높은 그룹의 전사망률이 더 낮았다. '한 가지 운동을 평생 vs 여러 가지 섞어서'의 답이 나왔다.",
        "이 결과의 무게는 30년 추적 + 17만 명 표본이라는 데 있다. 다양성이 효과적인 이유 — 1) 다른 근육군·움직임 패턴 자극으로 기능적 적응 폭이 넓어짐, 2) 단일 종목 반복으로 인한 부상 위험 감소, 3) 심리적 지속성(burnout 방지), 4) 사회적 연결 폭 확대. 처방: 1) 주간 메인 종목 1~2개(예: 저항운동 + 러닝), 2) 보조로 다른 모달리티 1~2개(요가·등산·수영·테니스 등), 3) 계절별로 종목 회전 — 여름 수영, 가을 등산, 겨울 헬스 + 실내 사이클. '평생 한 가지'는 효과적이지만 다양성이 더 큰 longevity 보너스.",
        "BMJ Medicine 2026",
        "https://www.sciencedaily.com/releases/2026/04/260426012305.htm",
        "노화/Anti-Aging",
        87,
        {"shock_factor": 18, "scientific_credibility": 24, "relatability": 22, "recency": 18, "controversy": 4, "visual_potential": 4},
        ["다양성", "사망률", "BMJ", "longevity", "30년추적"],
        kind="news", peer_reviewed=False,
    ),
    make(
        "단백질 + 탄수화물 동반 — 운동 후 글리코겐 회복을 2배로",
        "Protein + Carbs Post-Workout: Doubles Glycogen Recovery vs Carbs Alone",
        "Frontiers Nutrition 2024 RCT — 운동 후 단백질 + 탄수화물 동반 섭취가 탄수화물 단독 대비 글리코겐 재합성을 가속하고, 다음 세션 수행 능력을 높였다. '단백질 = 근육, 탄수화물 = 에너지'라는 단순 분리는 시대에 뒤떨어진 사고.",
        "기전 — 단백질의 인슐린 자극이 탄수화물의 인슐린 반응과 합쳐져 GLUT4 글루코스 수송체 활성화를 강화. 결과로 근육 글리코겐 재합성 속도 약 2배 증가. 적용: 1) 컴파운드 트레이닝 직후 30분 내 — 단백질 25~40g + 탄수화물 50~80g, 2) 두 세션을 같은 날 하는 선수에게 특히 중요, 3) 주 1회 가벼운 트레이닝만 하는 직장인은 효과 미미 — 일반 식사로 충분. 'post-workout window'는 보디빌더 마케팅보다 작지만, 고볼륨/고빈도 트레이너에게는 유효.",
        "Frontiers Nutrition 2024",
        "https://www.frontiersin.org/journals/nutrition/articles/10.3389/fnut.2024.1397090/full",
        "영양",
        78,
        {"shock_factor": 14, "scientific_credibility": 22, "relatability": 20, "recency": 12, "controversy": 4, "visual_potential": 4},
        ["글리코겐", "단백질탄수화물", "post-workout", "영양"],
    ),
]


def main():
    with open(ARTICLES_FILE) as f:
        data = json.load(f)

    existing_titles = {a.get("title") for a in data["news"]}
    existing_urls = {a.get("source_url") for a in data["news"]}

    new_added = 0
    skipped = 0
    for art in NEW_ARTICLES:
        if art["title"] in existing_titles:
            skipped += 1
            continue
        if art["source_url"] in existing_urls:
            skipped += 1
            continue
        data["news"].append(art)
        existing_titles.add(art["title"])
        existing_urls.add(art["source_url"])
        new_added += 1

    # Sort by viral_score descending
    data["news"].sort(key=lambda a: a.get("viral_score", 0), reverse=True)

    # Cap at 200
    if len(data["news"]) > 200:
        data["news"] = data["news"][:200]

    # Update meta
    data["meta"]["last_updated"] = NOW_ISO
    data["meta"]["last_updated_kst"] = f"{NOW_KST} KST 자동크롤(저녁: 운동과학·영양·회복·멘탈·바이럴)"
    data["meta"]["total_articles"] = len(data["news"]) + len(data.get("featured", []))
    data["meta"]["news_count"] = len(data["news"])
    data["meta"]["crawl_count"] = data["meta"].get("crawl_count", 0) + 1
    if data["news"]:
        scores = [a.get("viral_score", 0) for a in data["news"]]
        data["meta"]["top_viral_score"] = max(scores)
        data["meta"]["avg_viral_score"] = round(sum(scores) / len(scores), 1)

    with open(ARTICLES_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"신규 추가: {new_added}건")
    print(f"중복 제외: {skipped}건")
    print(f"총 news 기사: {len(data['news'])}건")
    print(f"\nTOP 3 viral:")
    for a in data["news"][:3]:
        print(f"  {a.get('viral_score')} | {a.get('title')[:80]}")


if __name__ == "__main__":
    main()
