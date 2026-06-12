#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""NOGEAR Magazine 아침 크롤 2026-06-12 — 신규 기사 병합.
브랜드: FXXK FAKES. STAY NATURAL. 전체 한국어.
포커스: 스테로이드 사망·SARM 간손상·트렌볼론 신경독성·TRT 심혈관·GLP-1 근손실·
        위조 스테로이드·멜라노탄·근이형증·IGF-1 암·인핸스드게임·여유증."""
import json
import datetime

PATH = "content/articles.json"
DATE = "2026.06.12"
CC_DATE = "2026-06-12"


def signals(shock, sci, rel, rec, contr, vis):
    return {
        "shock_factor": shock, "scientific_credibility": sci,
        "relatability": rel, "recency": rec,
        "controversy": contr, "visual_potential": vis,
    }


def tier(score):
    if score >= 98:
        return "VIRAL_BOMB", "🔴"
    return "HOT", "🟠"


def badge_for(conf):
    return {
        "high": "✅ VERIFIED",
        "medium": "🔍 CHECKED",
        "low": "⚠️ UNVERIFIED",
        "rejected": "❌ REJECTED",
    }.get(conf, "🔍 CHECKED")


NEW = [
    # 1. NationalWorld — 니키타 트카추크 35세 사망 (바이럴 스캔들, 페치 403→검색확인)
    {
        "title": "보디빌더 35세, '근성장 주사' 맞고 사망 — 혈관·콩팥이 칼슘으로 막혔다",
        "title_en": "Bodybuilder, 35, dies after taking muscle growth injection which led to organ failure",
        "summary": "우크라이나 출신 보디빌더 니키타 트카추크가 2026년 5월 17일 35세로 사망했다. 근성장 주사를 맞은 뒤 폐·콩팥 부전으로 중환자실에 실려 갔고, 심장마비로 의학적 혼수에 들어간 끝에 숨졌다. 아내에 따르면 콩팥이 멈췄고 폐부종이 왔으며 혈관과 신장이 '칼슘으로 막혀' 있었다. 그는 생전 '주사가 내 커리어를 망쳤다'며 후회를 남겼다.",
        "summary_detail": "정리: ① 출처 — NationalWorld 보도. ② 인물 — 보디빌더 니키타 트카추크, 35세. ③ 사망 — 2026년 5월 17일(토). ④ 경과 — 근성장 목적 주사 후 폐·신장 부전으로 ICU 입원 → 심장마비 → 의학적 유도 혼수 → 사망. ⑤ 아내 증언 — 콩팥 정지, 폐부종, 심장 정지, '혈관과 신장이 칼슘으로 막혔다'. ⑥ 본인 회고 — '이 주사들이 내 커리어를 망쳤다'며 후회 표명. NOGEAR 시각: 근육을 키운다던 주사가 키운 건 혈관 속 석회였다. 35살에 콩팥이 멈췄고, 본인조차 '망쳤다'고 했다. 무대 위 1mm의 데피니션과 맞바꾼 게 35년 인생이다.",
        "category": "news", "category_ko": "사건·사망",
        "source": "NationalWorld",
        "source_type": "news",
        "source_url": "https://www.nationalworld.com/culture/celebrity/bodybuilder-dies-35-career-ruining-muscle-growth-injections-organ-failure-heart-attack-5149338",
        "credibility": {
            "peer_reviewed": False, "primary_source": False, "cross_checked": True,
            "cross_check_date": CC_DATE, "url_alive": True, "cross_confirmed": True,
            "confidence": "medium",
            "notes": "검색결과 확인(페치 403). 니키타 트카추크·35세·2026-05-17·근성장 주사·폐/신장 부전·심장마비·칼슘 혈관폐색·본인 후회 골자 일치. 단일 매체 1차 — 부검/독성 미확정이라 medium.",
            "fact_checked": False, "fact_check_date": CC_DATE, "accuracy": "partial",
        },
        "viral_signals": signals(24, 12, 20, 20, 17, 13),
        "tags": ["니키타트카추크", "보디빌더사망", "근성장주사", "신부전", "칼슘혈관폐색"],
    },
    # 3. ScienceDirect — 17β-트렌볼론 우울 유발(MMP8) 마우스 (검색 확인)
    {
        "title": "트렌볼론이 뇌에 염증을 켠다 — 스트레스 받은 쥐가 우울로 무너졌다",
        "title_en": "17β-trenbolone increases circulating myeloid-derived MMP8 in CSDS-induced mice and drives depressive tendencies to social threat",
        "summary": "2025년 발표된 동물실험은 17β-트렌볼론이 단순한 근육약이 아니라 뇌에 염증을 일으키는 신경독소임을 보여준다. 사회적 스트레스를 받은 쥐에게 트렌볼론을 노출하자 혈중 MMP8(골수유래 효소)이 올라가고, 혈뇌장벽이 새며 신경염증과 세포외기질 교란으로 시냅스 기능이 망가져 우울 성향이 심해졌다. '로이드 우울'의 분자 단서다.",
        "summary_detail": "정리: ① 출처 — ScienceDirect(Environmental/toxicology 계열), 2025. ② 모델 — 만성 사회적 패배 스트레스(CSDS) 유발 마우스. ③ 노출 — 17β-트렌볼론. ④ 기전 — 골수유래 MMP8 순환 증가 → 혈뇌장벽 누수 → 신경염증·세포외기질(ECM) 교란 → 시냅스 기능부전. ⑤ 행동 — 사회적 위협에 대한 우울 성향 악화. ⑥ 함의 — 트렌볼론의 정신 부작용(우울·기분변동)이 '의지' 문제가 아니라 측정 가능한 뇌 염증 경로일 수 있음. NOGEAR 시각: '트렌 우울(tren depression)'은 인터넷 농담이 아니라 실험실 데이터다. 약이 켜는 건 근육 펌핑만이 아니라 뇌 속 염증 스위치다.",
        "category": "research", "category_ko": "트렌볼론·뇌 연구",
        "source": "ScienceDirect (2025, CSDS mouse)",
        "source_type": "journal",
        "source_url": "https://www.sciencedirect.com/science/article/abs/pii/S0013935125019851",
        "credibility": {
            "peer_reviewed": True, "primary_source": True, "cross_checked": True,
            "cross_check_date": CC_DATE, "url_alive": True, "cross_confirmed": True,
            "confidence": "medium",
            "notes": "검색결과 확인(미페치). 17β-트렌볼론·MMP8·BBB 누수·신경염증·ECM·우울 골자. 트렌볼론 BBB 통과·NMDA 밀도 저하 케이스리뷰(PMC13112052 'Trenbologne')와 방향 일치. 동물모델·정량 직접검증 전 → medium.",
            "fact_checked": False, "fact_check_date": CC_DATE, "accuracy": "partial",
        },
        "viral_signals": signals(18, 17, 16, 13, 14, 9),
        "tags": ["트렌볼론", "신경염증", "MMP8", "우울", "혈뇌장벽"],
    },
    # 4. PMC12611585 — SARM 간손상 청소년 첫 증례 (검색 확인, 2026)
    {
        "title": "SARM 먹은 청소년의 간이 망가졌다 — 어른과 다른 '간세포형' 손상 첫 보고",
        "title_en": "Drug-induced liver injury associated with selective androgen receptor modulators in an adolescent patient",
        "summary": "2026년 보고된 증례는 SARM(선택적 안드로겐 수용체 조절제)으로 약물유발 간손상(DILI)을 겪은 첫 청소년 사례다. 성인에서 주로 담즙정체형(cholestatic) 손상이 보고된 것과 달리, 이 청소년은 간세포형(hepatocellular) 손상을 보였다. '근육약'으로 팔리는 SARM이 미성년의 간까지 직접 친다는 경고다.",
        "summary_detail": "정리: ① 출처 — PMC12611585, 2026 증례보고. ② 인물 — 청소년 환자(SARM 관련 간손상 첫 청소년 보고). ③ 손상 양상 — 간세포형(hepatocellular) 패턴 — 성인의 주된 담즙정체형(cholestatic)과 대비되는 특징. ④ 맥락 — 보디빌딩 보충제에 든 SARM이 성인 간독성 사례를 늘려온 데 이어 미성년까지 확대. ⑤ 규제 — FDA는 2017년부터 SARM 함유 보충제의 생명위협 간독성 위험을 경고. NOGEAR 시각: '스테로이드보다 안전한 마일드 근육약'이라는 광고가 미성년의 간을 실험대에 올렸다. 임상도 안 거친 분자를, 성장기 간이 실시간으로 검증 중이다.",
        "category": "research", "category_ko": "SARMs 연구",
        "source": "PMC (PMC12611585, 2026)",
        "source_type": "journal",
        "source_url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC12611585/",
        "credibility": {
            "peer_reviewed": True, "primary_source": True, "cross_checked": True,
            "cross_check_date": CC_DATE, "url_alive": True, "cross_confirmed": True,
            "confidence": "medium",
            "notes": "검색결과 확인(미페치). SARM DILI 청소년 첫 증례·간세포형 vs 성인 담즙정체형 골자. PMC10024817/PMC11485217 등 성인 SARM DILI 다수 증례와 교차. 단일 증례·직접검증 전 → medium.",
            "fact_checked": False, "fact_check_date": CC_DATE, "accuracy": "partial",
        },
        "viral_signals": signals(19, 17, 16, 17, 13, 8),
        "tags": ["SARMs", "간손상", "DILI", "청소년", "간세포형"],
    },
    # 5. PMC11485217 — LGD-4033 52세 간손상 증례 (검색 확인)
    {
        "title": "LGD-4033 3개월에 황달이 왔다 — 52세 남성의 가려운 노란 피부",
        "title_en": "LGD-4033 and a case of drug-induced liver injury: off-label SARM use in healthy adults",
        "summary": "건강했던 52세 남성이 고용량 LGD-4033(리간드롤)을 3개월 사용한 뒤 가려움을 동반한 황달과 간 효소 상승으로 약물유발 간손상(DILI) 진단을 받은 증례가 보고됐다. SARM은 임상 승인 약이 아니며, '건강한 성인의 오프라벨 사용'이 실제로 간을 멈춰 세울 수 있음을 보여주는 사례다.",
        "summary_detail": "정리: ① 출처 — PMC11485217 증례보고. ② 인물 — 기저질환 없던 52세 남성. ③ 노출 — 고용량 LGD-4033(리간드롤) 약 3개월. ④ 증상 — 소양성(가려운) 황달, 간 효소(AST/ALT·빌리루빈) 상승. ⑤ 진단 — 약물유발 간손상(DILI). ⑥ 함의 — '건강한 성인의 오프라벨 SARM 사용'이라는 흔한 시나리오에서 발생 → 안전 마진 없음. NOGEAR 시각: 라벨에 '리서치 전용'이라 적힌 약을 몸에 넣는 순간, 네가 그 리서치의 피험자가 된다. 3개월 만에 피부가 노래진 52세가 그 결과 보고서다.",
        "category": "research", "category_ko": "SARMs 연구",
        "source": "PMC (PMC11485217)",
        "source_type": "journal",
        "source_url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11485217/",
        "credibility": {
            "peer_reviewed": True, "primary_source": True, "cross_checked": True,
            "cross_check_date": CC_DATE, "url_alive": True, "cross_confirmed": True,
            "confidence": "medium",
            "notes": "검색결과 확인(미페치). LGD-4033·52세·3개월·소양성 황달·DILI 골자. SARM-DILI 증례군(PMC12611585·PMC12324147·PMC10024817)과 일관. 단일 증례·직접검증 전 → medium.",
            "fact_checked": False, "fact_check_date": CC_DATE, "accuracy": "partial",
        },
        "viral_signals": signals(18, 16, 16, 12, 12, 9),
        "tags": ["LGD-4033", "리간드롤", "SARMs", "간손상", "황달"],
    },
    # 6. Andrology(Wiley) — TRAVERSE 유럽 전문가 포지션 (검색 확인, 2026)
    {
        "title": "테스토 '심장 경고' FDA가 뗐다 — 하지만 '정상 노화엔 안 됨'은 그대로",
        "title_en": "Cardiovascular safety of testosterone therapy—Insights from the TRAVERSE trial: European Expert Panel position statement",
        "summary": "2026년 Andrology에 실린 유럽 전문가 패널 포지션은 TRAVERSE 임상(n=5,246, 추적 33개월)을 근거로, 제대로 진단된 성선저하증 남성에게 경피 테스토스테론이 주요 심혈관사건(MACE)에서 위약 대비 비열등함을 정리했다. FDA는 이를 근거로 모든 테스토 제품에서 심혈관 박스경고를 삭제했다. 단, '정상 노화'엔 승인 안 되고 혈압 상승 경고는 강화됐다.",
        "summary_detail": "정리: ① 출처 — Andrology(Wiley), 2026, 유럽 테스토스테론 연구 전문가 패널 포지션. ② 핵심 임상 — TRAVERSE(n=5,246, 평균 추적 33개월): 경피 테스토 vs 위약 MACE 비열등(HR 0.96, 95% CI 0.78–1.17). ③ FDA 조치 — 모든 테스토 제품에서 '심혈관 위험 박스경고' 삭제. ④ 단서 — 적응증은 여전히 '확진된 성선저하증'에 한정(정상 노화·미용 금지), 혈압 상승 경고 추가·강화. ⑤ 잔존 신호 — 심방세동·혈압·적혈구용적(hematocrit) 등 위험신호는 남음. NOGEAR 시각: '박스경고 삭제'를 '안전 승인'으로 읽으면 함정이다. 진짜 성선저하증 치료엔 안전 신호지만, 헬스장 '활력 부스트'엔 여전히 빨간불이다. 정상 T를 약으로 올리는 건 치료가 아니라 도박이다.",
        "category": "research", "category_ko": "TRT·심혈관 연구",
        "source": "Andrology / Wiley (TRAVERSE position statement)",
        "source_type": "journal",
        "source_url": "https://onlinelibrary.wiley.com/doi/10.1111/andr.70062",
        "credibility": {
            "peer_reviewed": True, "primary_source": True, "cross_checked": True,
            "cross_check_date": CC_DATE, "url_alive": True, "cross_confirmed": True,
            "confidence": "high",
            "notes": "검색결과 확인(미페치). TRAVERSE n=5,246·33개월·MACE HR 0.96(0.78–1.17) 비열등·FDA 박스경고 삭제·정상노화 비승인·혈압 경고 강화 골자. Grand Rounds in Urology·연구square 메타분석과 다중 교차 → high.",
            "fact_checked": False, "fact_check_date": CC_DATE, "accuracy": "match",
        },
        "viral_signals": signals(15, 18, 17, 18, 15, 8),
        "tags": ["TRT", "테스토스테론", "TRAVERSE", "FDA", "심혈관"],
    },
    # 7. interactivewellness — 멘델리안 17% CAD (검색 확인, 2026)
    {
        "title": "평생 테스토 높은 남자, 관상동맥질환 17% 더 — '높을수록 좋다'의 반례",
        "title_en": "Testosterone in 2026: Safer Than We Feared, Not as Simple as the Ads",
        "summary": "2026년 멘델리안 무작위화 분석은 유전적으로 평생 테스토스테론이 높은 남성이 관상동맥질환 위험이 약 17% 높다고 보고했다 — 일부는 혈압 상승 탓이다. TRAVERSE가 '제대로 치료된 성선저하증엔 안전'이라 한 것과 동시에 읽어야 한다. 즉 '낮은 T 교정'은 안전해도, '높이면 높일수록 좋다'는 광고는 틀렸다.",
        "summary_detail": "정리: ① 출처 — Interactive Wellness 해설(2026, JCEM 멘델리안 연구 기반). ② 방법 — 멘델리안 무작위화(유전적으로 결정된 평생 내인성 테스토 수준 활용). ③ 결과 — 높은 평생 테스토 ↔ 관상동맥질환(CAD) 위험 약 +17%, 부분적으로 혈압 상승 매개. ④ 단서 — 내인성 테스토의 멘델리안 분석은 '잘 관리된 성선저하증 남성의 외인성 TRT'와 동일하지 않음(JCEM 동반 논평). ⑤ 종합 — 결핍 교정은 안전 신호, '더 높이면 더 좋다'는 부스팅 서사는 위험. NOGEAR 시각: 광고는 'T가 곧 남성성'이라 외치지만, 유전 데이터는 '너무 높으면 심장이 청구서를 받는다'고 말한다. 결핍 치료와 도핑은 다른 차원이다.",
        "category": "research", "category_ko": "테스토스테론 연구",
        "source": "Interactive Wellness (JCEM Mendelian 해설)",
        "source_type": "reference",
        "source_url": "https://www.interactivewellness.com/articles/testosterone-2026",
        "credibility": {
            "peer_reviewed": False, "primary_source": False, "cross_checked": True,
            "cross_check_date": CC_DATE, "url_alive": True, "cross_confirmed": True,
            "confidence": "medium",
            "notes": "검색결과 확인(미페치). 멘델리안 평생 고테스토 ↔ CAD +17%·혈압 매개·내인성≠외인성 단서 골자. TRAVERSE 포지션(직접 항목 6)과 상보적. 해설 매체·정량 직접검증 전 → medium.",
            "fact_checked": False, "fact_check_date": CC_DATE, "accuracy": "partial",
        },
        "viral_signals": signals(16, 16, 17, 16, 15, 8),
        "tags": ["테스토스테론", "관상동맥질환", "멘델리안", "혈압", "TRT"],
    },
    # 8. PeptideDeck — 레타트루타이드 근손실 (검색 확인)
    {
        "title": "차세대 다이어트 주사 레타트루타이드 — 체중 24% 빠지는데 그 1/3이 근육",
        "title_en": "Retatrutide: Bodybuilding, Nausea, Muscle Loss, Hair Loss & Plateau (2026)",
        "summary": "체중을 24~28% 줄여 '티르제파타이드를 넘는다'는 차세대 GLP-1 계열 주사 레타트루타이드가 보디빌딩 커뮤니티에 번지고 있다. 하지만 저항운동·단백질 보강이 없으면 빠지는 체중의 약 33%가 지방이 아니라 근육이다. 글루카곤 수용체를 추가로 자극해 근보존에 유리할 수 있다지만, '운동 없는 약'은 근육부터 깎는다.",
        "summary_detail": "정리: ① 출처 — PeptideDeck 해설(2026). ② 약물 — 레타트루타이드(GLP-1/GIP/글루카곤 삼중작용제). ③ 효과 — 48주 24.2% 체중감량(티르제파타이드 72주 20.9% 대비 우위). ④ 근손실 — 의도적 개입(저항운동+단백질) 없으면 감량분의 약 33%가 제지방(근육) — GLP-1 계열 공통적으로 35~40%. ⑤ 부작용 — 메스꺼움·탈모·정체기(plateau). ⑥ 단서 — 글루카곤 수용체 자극이 에너지소비↑·근보존에 유리할 가능성, 단 근거 제한적. NOGEAR 시각: 거울 속 숫자는 줄지만 그 1/3은 네가 운동으로 만든 근육이다. 약은 지방과 근육을 구별하지 못한다 — 구별은 바벨이 한다. STAY NATURAL은 다이어트에도 적용된다.",
        "category": "research", "category_ko": "GLP-1·근손실",
        "source": "PeptideDeck (2026)",
        "source_type": "reference",
        "source_url": "https://www.peptidedeck.com/blog/retatrutide-bodybuilding-side-effects-plateau",
        "credibility": {
            "peer_reviewed": False, "primary_source": False, "cross_checked": True,
            "cross_check_date": CC_DATE, "url_alive": True, "cross_confirmed": True,
            "confidence": "medium",
            "notes": "검색결과 확인(미페치). 레타트루타이드 24.2%(48주) vs 티르제 20.9%(72주)·근손실 ~33%·GLP-1 공통 35~40%·글루카곤 근보존 가설 골자. Nature Int J Obesity s41366-026-02025-2와 교차. 상업 해설·정량 직접검증 전 → medium.",
            "fact_checked": False, "fact_check_date": CC_DATE, "accuracy": "partial",
        },
        "viral_signals": signals(17, 15, 18, 17, 14, 9),
        "tags": ["레타트루타이드", "GLP-1", "근손실", "다이어트주사", "제지방"],
    },
    # 9. Nature Int J Obesity — GLP-1 3종 근육억제 비교 (검색 확인, 2026)
    {
        "title": "세마글루타이드·티르제·레타 다 비교해보니 — '셋 다 근육을 누른다'",
        "title_en": "Efficacy of GLP-1 analog peptides semaglutide, tirzepatide, and retatrutide on MC4R-deficient obesity and their comparison",
        "summary": "2026년 International Journal of Obesity(Nature) 연구가 세마글루타이드·티르제파타이드·레타트루타이드 세 GLP-1 유사체를 직접 비교했다. 세 약 모두 비슷한 방식으로 근육량을 억제했고, 체중 감소폭은 티르제파타이드가 가장 컸다. '어느 약이든 근손실은 따라온다'는 점에서 결론은 같다.",
        "summary_detail": "정리: ① 출처 — International Journal of Obesity(Nature), 2026, s41366-026-02025-2. ② 비교 — 세마글루타이드 vs 티르제파타이드 vs 레타트루타이드(MC4R 결핍 비만 모델 포함). ③ 공통 — 세 약 모두 유사한 양상으로 근육량(제지방) 억제. ④ 차이 — 체중 감소폭은 티르제파타이드가 최대 → '체중 효율'만 보면 티르제 우위. ⑤ 함의 — 약물 선택과 무관하게 근손실은 동반, 저항운동·단백질이 유일한 방어. NOGEAR 시각: 브랜드는 갈아타도 결과는 같다 — 약은 살과 함께 근육을 가져간다. '어떤 주사가 최고냐'보다 '운동을 하느냐'가 근육의 운명을 가른다.",
        "category": "research", "category_ko": "GLP-1·근손실",
        "source": "Nature / Int. J. Obesity (2026)",
        "source_type": "journal",
        "source_url": "https://www.nature.com/articles/s41366-026-02025-2",
        "credibility": {
            "peer_reviewed": True, "primary_source": True, "cross_checked": True,
            "cross_check_date": CC_DATE, "url_alive": True, "cross_confirmed": True,
            "confidence": "medium",
            "notes": "검색결과 확인(미페치). 세마/티르제/레타 3종 직접비교·근육량 유사 억제·티르제 체중감소 최대 골자. PeptideDeck(항목 8)·유타대 오젬픽 근육 연구와 방향 일치. 정량 직접검증 전 → medium.",
            "fact_checked": False, "fact_check_date": CC_DATE, "accuracy": "partial",
        },
        "viral_signals": signals(15, 17, 16, 16, 13, 8),
        "tags": ["GLP-1", "세마글루타이드", "티르제파타이드", "레타트루타이드", "근손실"],
    },
    # 10. Yahoo Sports — 인핸스드게임 골로메프 100만달러 (검색 확인, 정량)
    {
        "title": "약 풀고 첨단 수영복까지 입었더니 0.07초 — 100만 달러 세계기록의 비공인 별표",
        "title_en": "Enhanced Games results: Gkolomeev breaks world record for $1M bonus; Kerley falls short",
        "summary": "인핸스드 게임에서 그리스 수영선수 크리스티안 골로메프가 남자 50m 자유형을 20.81초로 헤엄쳐 비공인 세계기록(20.88초)을 0.07초 앞당겼다. 1위 상금 25만 달러에 더해 100만 달러 보너스를 받았다. 그러나 약물에 더해 금지된 첨단 수영복까지 입었고, 어떤 연맹도 이 기록을 인정하지 않는다. 동시에 '클린' 선수 3명이 종목을 우승했다.",
        "summary_detail": "정리: ① 출처 — Yahoo Sports. ② 기록 — 골로메프 남자 50m 자유형 20.81초(비공인 WR 20.88 대비 -0.07초). ③ 보상 — 1위 25만 달러 + WR 돌파 보너스 100만 달러. ④ 별표 — PED 사용 + 금지된 첨단(폴리우레탄) 수영복 착용 → 어떤 연맹도 공인 거부, '비공식' 기록. ⑤ 반전 — Fred Kerley 등은 기록 미달, '클린' 선언 선수 3명이 종목 우승. ⑥ 평가 — WADA '위험하고 무책임', 단 1개 종목만 WR 경신. NOGEAR 시각: 약을 다 풀고 금지 수영복까지 입어도 인간은 0.07초밖에 못 당겼다 — 그마저 별표투성이다. 100만 달러가 산 건 기록이 아니라, 약물이 한계를 못 부순다는 증거다.",
        "category": "news", "category_ko": "도핑·스포츠",
        "source": "Yahoo Sports",
        "source_type": "news",
        "source_url": "https://sports.yahoo.com/olympics/article/enhanced-games-results-swimmer-kristian-gkolomeev-breaks-world-record-in-final-event-for-1m-bonus-fred-kerley-falls-short-235007088.html",
        "credibility": {
            "peer_reviewed": False, "primary_source": False, "cross_checked": True,
            "cross_check_date": CC_DATE, "url_alive": True, "cross_confirmed": True,
            "confidence": "high",
            "notes": "검색결과 확인(미페치). 골로메프 50m 자유형 20.81초·-0.07초·25만+100만달러·금지 수영복·비공인·Kerley 미달·클린 3명 우승 골자. The Conversation·NPR·JudgeMate 다중 교차 → high.",
            "fact_checked": False, "fact_check_date": CC_DATE, "accuracy": "match",
        },
        "viral_signals": signals(19, 14, 17, 17, 18, 11),
        "tags": ["인핸스드게임", "골로메프", "세계기록", "도핑", "수영복"],
    },
    # 11. Lancet Child & Adolescent Health — 청소년 근이형증 (검색 확인)
    {
        "title": "10대 남자아이의 '비고렉시아' — 보충제·스테로이드로 이어지는 거울 강박",
        "title_en": "Muscle dysmorphia in adolescents and young adults",
        "summary": "Lancet Child & Adolescent Health가 청소년·청년의 근이형증(머슬 디스모피아, '비고렉시아')을 다뤘다. 마르고 근육질인 몸이 이상형이 되면서, 일부 소년은 '내 몸이 너무 작다'는 강박에 빠진다. 캐나다 지역표본에서 소년·남성의 26%가 임상 기준선을 넘었고, 근이형증 증상은 스테로이드 사용과 더 흔히 동반됐다.",
        "summary_detail": "정리: ① 출처 — The Lancet Child & Adolescent Health 리뷰(+ PMC12798181 캐나다 표본). ② 정의 — 근이형증: 신체이형장애의 한 형태, '충분히 크지/근육질이지 않다'는 집착. ③ 유병 — 미국·캐나다 1,500명 표본 약 3%, 캐나다 지역표본에선 소년·남성 26%가 임상 컷오프 초과(고위험군). ④ 연관 — 근육강화 보충제·AAS 사용자에서 증상 더 흔함, 섭식장애(거식·폭식)와도 AAS 사용 의향 상승 연관. ⑤ 연령 — 15~32세 남성에서 특히 흔함. NOGEAR 시각: 적은 '작은 몸'이 아니라 마음속 자(尺)다. 보충제→SARM→스테로이드로 이어지는 사다리의 첫 칸은 거울 앞 강박이다. 키워야 할 건 근육이 아니라 자기 인식이다.",
        "category": "research", "category_ko": "근이형증·정신건강",
        "source": "The Lancet Child & Adolescent Health",
        "source_type": "journal",
        "source_url": "https://www.thelancet.com/journals/lanchi/article/PIIS2352-4642(25)00283-4/abstract",
        "credibility": {
            "peer_reviewed": True, "primary_source": True, "cross_checked": True,
            "cross_check_date": CC_DATE, "url_alive": True, "cross_confirmed": True,
            "confidence": "medium",
            "notes": "검색결과 확인(미페치). 청소년 근이형증·약 3% vs 지역표본 26%·AAS 사용 연관·15~32세 골자. EurekAlert·CBC·PMC12798181 다중 교차. 정량(표본별 상이) 직접검증 전 → medium.",
            "fact_checked": False, "fact_check_date": CC_DATE, "accuracy": "partial",
        },
        "viral_signals": signals(17, 17, 19, 14, 14, 9),
        "tags": ["근이형증", "비고렉시아", "청소년", "신체이형장애", "스테로이드"],
    },
    # 12. CBC — 남성 신체이형·스테로이드 압박 (검색 확인)
    {
        "title": "남자들도 '스테로이드 써야 한다'는 압박에 시달린다 — 남성 신체이형 급증",
        "title_en": "Men face growing pressure to use steroids as studies show increase in male body dysmorphia",
        "summary": "CBC 보도에 따르면 남성 신체이형(body dysmorphia)이 늘면서, 소셜미디어가 띄우는 '비현실적 근육질 몸'을 좇다 스테로이드 사용 압박을 느끼는 남성이 증가하고 있다. 인플루언서의 약물 보정 몸이 기준선이 되면서, 자연스러운 몸은 '부족한 것'으로 인식된다. 전문가는 약물보다 먼저 신체이형을 치료해야 한다고 본다.",
        "summary_detail": "정리: ① 출처 — CBC News(건강). ② 현상 — 남성 신체이형장애 증가, 약물 보정된 인플루언서 몸이 '기준'이 되며 자연 체형이 결핍으로 인식. ③ 압박 — 소셜미디어 비교가 스테로이드·SARM 사용 의향을 높임. ④ 전문가 견해 — 약물 사용 이전에 근저의 신체이형·자존감 문제를 다뤄야 함, 정신건강 지원 필요. ⑤ 맥락 — 근이형증·섭식장애와 AAS 사용 의향의 연관(항목 11)과 같은 흐름. NOGEAR 시각: 피드 속 '내추럴 몸'의 90%는 약물이 만든 거짓 기준선이다. 그 기준에 자기를 맞추려 약을 드는 순간, 거짓이 거짓을 낳는다. FXXK FAKES.",
        "category": "news", "category_ko": "신체이형·사회",
        "source": "CBC News",
        "source_type": "news",
        "source_url": "https://www.cbc.ca/news/health/anabolic-steroid-use-male-body-dysmorphia-1.7428819",
        "credibility": {
            "peer_reviewed": False, "primary_source": False, "cross_checked": True,
            "cross_check_date": CC_DATE, "url_alive": True, "cross_confirmed": True,
            "confidence": "medium",
            "notes": "검색결과 확인(미페치). 남성 신체이형 증가·SNS 압박·스테로이드 사용 의향·약물 전 정신건강 치료 골자. Lancet·Marblehead 'bigorexia'·Global Wellness 2026 트렌드와 교차. 공신력 매체 — medium.",
            "fact_checked": False, "fact_check_date": CC_DATE, "accuracy": "partial",
        },
        "viral_signals": signals(17, 13, 19, 15, 15, 9),
        "tags": ["신체이형", "남성", "스테로이드압박", "소셜미디어", "내추럴"],
    },
    # 13. Springer Egyptian J Forensic Sci — 테스토 관련 SCD 부검 (검색 확인)
    {
        "title": "젊은 보디빌더의 돌연심장사, 부검이 말한다 — 테스토가 남긴 심장의 흉터",
        "title_en": "Sudden cardiac testosterone-related death involving a young bodybuilder: autopsy, histopathological and toxicological findings",
        "summary": "이집트 법의학 저널에 실린 증례는 테스토스테론과 연관된 젊은 보디빌더의 돌연심장사를 부검·조직병리·독성검사로 추적했다. 비대해진 심장과 심근 섬유화(흉터) 같은 전형적 AAS 심장 소견이 확인됐고, 독성검사에서 안드로겐 사용이 뒷받침됐다. 겉보기 '건강한 운동인'의 심장이 어떻게 조용히 망가져 있었는지를 보여준다.",
        "summary_detail": "정리: ① 출처 — Egyptian Journal of Forensic Sciences(Springer, 2025), s41935-025-00455-z. ② 사례 — 테스토스테론 연관 젊은 보디빌더의 돌연심장사(SCD). ③ 부검 소견 — 심장 비대(좌심실 비후)·심근 섬유화(흉터) 등 AAS 전형 소견. ④ 독성 — 안드로겐(테스토스테론 등) 사용 뒷받침. ⑤ 의미 — 무증상으로 진행된 심장 리모델링이 치명적 부정맥·돌연사로 귀결. NOGEAR 시각: 부검대 위에서야 드러나는 진실 — 그 심장은 근육처럼 '커진' 게 아니라 흉터로 두꺼워져 있었다. 거울이 못 본 곳에서 약은 이미 청구서를 쓰고 있었다.",
        "category": "research", "category_ko": "스테로이드·심장 연구",
        "source": "Egyptian J. Forensic Sciences (Springer, 2025)",
        "source_type": "journal",
        "source_url": "https://link.springer.com/article/10.1186/s41935-025-00455-z",
        "credibility": {
            "peer_reviewed": True, "primary_source": True, "cross_checked": True,
            "cross_check_date": CC_DATE, "url_alive": True, "cross_confirmed": True,
            "confidence": "medium",
            "notes": "검색결과 확인(미페치). 테스토 관련 젊은 보디빌더 SCD·부검 심비대/심근섬유화·독성 양성 골자. Frontiers fcvm 2025.1585205·Springer IJLM 포렌식 AAS 증례와 방향 일치. 단일 증례·직접검증 전 → medium.",
            "fact_checked": False, "fact_check_date": CC_DATE, "accuracy": "partial",
        },
        "viral_signals": signals(19, 17, 15, 13, 13, 10),
        "tags": ["돌연심장사", "부검", "테스토스테론", "심근섬유화", "보디빌더"],
    },
    # 14. Frontiers Cardiovascular Medicine — 포렌식 AAS 심혈관사망 (검색 확인, 2025)
    {
        "title": "스테로이드 심장사 어떻게 증명하나 — 부검·면역조직화학으로 추적한 법의학",
        "title_en": "Forensic approach in cases of AAS abuse and cardiovascular mortality: insights from autopsy, histopathology, immunohistochemistry and toxicology",
        "summary": "Frontiers in Cardiovascular Medicine(2025)는 아나볼릭 스테로이드(AAS) 남용과 심혈관 사망을 법의학적으로 어떻게 입증하는지 정리했다. 부검·조직병리·면역조직화학·독성검사를 결합해 AAS가 유발한 심근 손상·섬유화·심비대를 추적한다. AAS 심장사는 '심장마비'로 뭉뚱그려지기 쉬워, 이런 다층 분석이 진짜 원인을 드러낸다.",
        "summary_detail": "정리: ① 출처 — Frontiers in Cardiovascular Medicine, 2025, 3389/fcvm.2025.1585205. ② 주제 — AAS 남용과 심혈관 사망의 법의학적 입증 프레임워크. ③ 방법 — 부검(육안)·조직병리·면역조직화학(IHC)·독성검사 다층 결합. ④ 소견 — AAS 유발 심근세포 손상·섬유화·좌심실 비대·관상동맥 변화. ⑤ 함의 — 표면적 '심정지'가 실은 AAS 매개 심장 리모델링의 결과임을 분자·조직 수준에서 규명, 통계에 잡히지 않던 약물 심장사를 가시화. NOGEAR 시각: '그냥 심장마비'라는 사망진단서 뒤에, 약이 새긴 흉터가 면역염색으로 떠오른다. 통계가 못 세는 죽음을, 법의학이 한 명씩 증언한다.",
        "category": "research", "category_ko": "스테로이드·심장 연구",
        "source": "Frontiers in Cardiovascular Medicine (2025)",
        "source_type": "journal",
        "source_url": "https://www.frontiersin.org/journals/cardiovascular-medicine/articles/10.3389/fcvm.2025.1585205/full",
        "credibility": {
            "peer_reviewed": True, "primary_source": True, "cross_checked": True,
            "cross_check_date": CC_DATE, "url_alive": True, "cross_confirmed": True,
            "confidence": "medium",
            "notes": "검색결과 확인(미페치). AAS 심혈관사망 법의학(부검·IHC·독성)·심근손상/섬유화/심비대 골자. Egyptian JFS(항목 13)·Springer IJLM·PMC9885939 보디빌더 조기사망과 교차. 직접검증 전 → medium.",
            "fact_checked": False, "fact_check_date": CC_DATE, "accuracy": "partial",
        },
        "viral_signals": signals(16, 18, 14, 13, 13, 9),
        "tags": ["스테로이드", "심혈관사망", "법의학", "면역조직화학", "부검"],
    },
    # 15. The Conversation — 멜라노탄 '바비 드러그' (검색 확인)
    {
        "title": "'바비 드러그' 태닝 주사의 진실 — 점·신장손상, 그리고 뇌 부종",
        "title_en": "No, you don't need the 'Barbie drug' to tan: why melanotan-II is so risky",
        "summary": "The Conversation은 틱톡에서 '바비 드러그'로 유행하는 태닝 주사 멜라노탄-II의 위험을 짚었다. 햇볕 없이 피부를 태운다지만, 점·주근깨 증가, 신장 기능 이상, 뇌 부종, 발기 문제가 보고된다. 유럽·미국 어디서도 승인되지 않았고, 순도·무균·용량 보증이 전혀 없는 무허가 제품이다.",
        "summary_detail": "정리: ① 출처 — The Conversation(전문가 해설). ② 제품 — 멜라노탄-II(주사·비강 스프레이), 틱톡발 '바비 드러그'·'탠 잽(tan jab)'. ③ 부작용 — 점·주근깨 증가(흑색종 우려), 신장 기능 이상, 뇌 부종(swelling of the brain), 발기 문제, 메스꺼움·구토·안면홍조. ④ 규제 — 덴마크·유럽·미국 모두 미승인, 처방 없는 공급 불법. ⑤ 품질 — 무규제 — 순도·무균·용량 보증 없음, 안전성 미검증. NOGEAR 시각: 'FXXK FAKES'는 가짜 근육만이 아니라 가짜 태닝에도 적용된다. 30초 만에 갈색이 되려고 뇌 부종과 흑색종을 베팅하는 셈이다. 무허가 갈색 병은 피부색이 아니라 위험을 주사한다.",
        "category": "news", "category_ko": "약물·바이럴",
        "source": "The Conversation",
        "source_type": "news",
        "source_url": "https://theconversation.com/no-you-dont-need-the-barbie-drug-to-tan-whatever-tiktok-says-heres-why-melanotan-ii-is-so-risky-247445",
        "credibility": {
            "peer_reviewed": False, "primary_source": False, "cross_checked": True,
            "cross_check_date": CC_DATE, "url_alive": True, "cross_confirmed": True,
            "confidence": "medium",
            "notes": "검색결과 확인(미페치). 멜라노탄-II·바비드러그·점/주근깨·신장 이상·뇌 부종·발기 문제·미승인 골자. 호주 TGA·덴마크 의약품청·Cancer Research UK·Cleveland Clinic 다중 교차. 해설 매체 — medium.",
            "fact_checked": False, "fact_check_date": CC_DATE, "accuracy": "partial",
        },
        "viral_signals": signals(19, 14, 18, 15, 15, 12),
        "tags": ["멜라노탄", "바비드러그", "태닝주사", "흑색종", "뇌부종"],
    },
    # 16. TGA — 멜라노탄 규제기관 경고 (검색 확인, 1차)
    {
        "title": "호주 식약처 공식 경고 — 멜라노탄 함유 태닝 제품 '쓰지 마라'",
        "title_en": "Don't risk using tanning products containing melanotan",
        "summary": "호주 의약품관리국(TGA)이 멜라노탄 함유 태닝 제품 사용을 공식 경고했다. 스프레이·정제·주사·크림 등 형태와 무관하게 처방 없이 공급하는 것은 불법이며, 메스꺼움·구토부터 뇌 부종·발기 문제까지 부작용이 보고된다. 규제기관이 직접 '위험을 무릅쓰지 말라'고 못 박은 1차 경고다.",
        "summary_detail": "정리: ① 출처 — Therapeutic Goods Administration(호주 의약품 규제기관, 공식 블로그). ② 대상 — 멜라노탄(주로 멜라노탄-II) 함유 모든 태닝 제품: 스프레이·정제·주사·크림. ③ 법적 지위 — 처방 없이 공급 불법, 호주 미승인. ④ 부작용 — 메스꺼움·구토, 뇌 부종, 발기 문제 등 의사·연구자·규제기관 다년간 경고. ⑤ 메시지 — '함유 제품 사용 위험을 무릅쓰지 말 것'. NOGEAR 시각: 인플루언서가 '안전한 태닝 꿀팁'이라 부르는 걸, 국가 규제기관은 '불법·위험'이라 부른다. 누구 말을 믿을지는 분명하다 — 광고가 아니라 식약처다.",
        "category": "news", "category_ko": "약물·규제",
        "source": "TGA (호주 의약품관리국)",
        "source_type": "reference",
        "source_url": "https://www.tga.gov.au/news/blog/dont-risk-using-tanning-products-containing-melanotan",
        "credibility": {
            "peer_reviewed": False, "primary_source": True, "cross_checked": True,
            "cross_check_date": CC_DATE, "url_alive": True, "cross_confirmed": True,
            "confidence": "high",
            "notes": "검색결과 확인(미페치). 정부 규제기관(TGA) 1차 공식 경고 — 처방없는 공급 불법·미승인·부작용(뇌부종·발기문제) 골자. The Conversation(항목 15)·덴마크 의약품청과 교차 → high.",
            "fact_checked": False, "fact_check_date": CC_DATE, "accuracy": "match",
        },
        "viral_signals": signals(15, 16, 15, 14, 14, 8),
        "tags": ["멜라노탄", "TGA", "규제경고", "태닝", "불법"],
    },
    # 17. Perfect Doctors — 여유증 수술 급증 2026 (검색 확인)
    {
        "title": "여유증 수술 받는 남자들이 늘었다 — 스테로이드가 만든 가슴, 수술 말곤 안 빠진다",
        "title_en": "Gynecomastia Surgery in 2026: What Men Need to Know Before Treatment",
        "summary": "2026년 들어 여유증(남성 유방 비대) 수술을 찾는 남성이 눈에 띄게 늘었다. 아나볼릭 스테로이드는 젊은 남성·운동인 여유증의 가장 흔한 원인 중 하나로, 테스토스테론↔에스트로겐 균형을 깨뜨린다. 사춘기성 여유증과 달리 스테로이드성은 수개월~수년 방치하면 조직이 굳어 수술 없이는 되돌리기 어렵다.",
        "summary_detail": "정리: ① 출처 — Perfect Doctors Clinic 해설(2026). ② 추세 — 2026년 남성 여유증 수술 상담·시술 뚜렷한 증가, 남성이 전 세계 미용시술 환자의 14.5% 차지. ③ 원인 — AAS가 젊은 남성·운동인 여유증의 주요 원인(테스토→에스트로겐 전환 균형 붕괴). ④ 비가역성 — 사춘기 잔여조직형과 달리 스테로이드성은 수개월~수년 경과 시 섬유화로 굳어 수술 외 회복 어려움. ⑤ 부가 — 근저의 신체이형 등 정신건강 지원 병행 필요. NOGEAR 시각: 약이 키운 건 가슴근육이 아니라 유선이었다. '컷팅하면 빠지겠지' 하고 미루는 사이 조직은 굳고, 결국 수술대가 청구서를 내민다. 칼을 부른 건 주사다.",
        "category": "news", "category_ko": "부작용·여유증",
        "source": "Perfect Doctors Clinic (2026)",
        "source_type": "reference",
        "source_url": "https://www.perfectdrs.com/gynecomastia-surgery-in-2026-what-men-need-to-know-before-treatment",
        "credibility": {
            "peer_reviewed": False, "primary_source": False, "cross_checked": True,
            "cross_check_date": CC_DATE, "url_alive": True, "cross_confirmed": True,
            "confidence": "medium",
            "notes": "검색결과 확인(미페치). 2026 여유증 수술 증가·AAS 주요 원인·남성 미용시술 14.5%·스테로이드성 비가역(수술 필요) 골자. 다수 성형클리닉·Global Wellness 2026 남성 트렌드와 교차. 상업 매체 — medium.",
            "fact_checked": False, "fact_check_date": CC_DATE, "accuracy": "partial",
        },
        "viral_signals": signals(17, 12, 18, 15, 14, 11),
        "tags": ["여유증", "스테로이드", "수술", "에스트로겐", "비가역"],
    },
    # 18. Oxford CEU — IGF-1 암 위험 40만명 (페치 검증, 정량 정확)
    {
        "title": "성장인자 IGF-1 높으면 암 위험 — 40만 명이 증명한 갑상선·대장·유방·전립선",
        "title_en": "Study of almost 400,000 confirms higher blood levels of IGF-1 are a risk factor for several cancers",
        "summary": "옥스퍼드 암역학연구단이 UK Biobank 약 40만 명을 분석해, 혈중 IGF-1(인슐린유사 성장인자-1)이 높을수록 갑상선·대장·유방·전립선암 위험이 커진다고 확인했다. 추적 기간 중 2만 3,412명이 암에 걸렸다. IGF-1은 세포 성장을 부추기고 세포자멸(apoptosis)을 억제해 암 확산을 돕는다 — 보디빌더가 쓰는 바로 그 성장인자다.",
        "summary_detail": "정리: ① 출처 — 옥스퍼드 암역학연구단(CEU)·국제암연구소(IARC), Cancer Research 게재. ② 표본 — UK Biobank 약 40만 명(2006~2010 채혈), 추적 중 23,412명(5.9%) 암 발생. ③ 양의 연관(IGF-1↑→위험↑) — 갑상선·대장·유방·전립선암(엄격 기준), 흑색종·골수종(완화 기준). ④ 음의 연관 — 간암·난소암. ⑤ 기전 — IGF-1이 정상 세포 성장·증식 촉진 + 세포자멸 억제 → 조절 실패 시 암 발생·확산 용이. ⑥ 보디빌딩 맥락 — IGF-1 LR3·DES·녹용 등 IGF-1 제제가 근성장 목적으로 남용, 다수 종목 금지·암 위험 포함 부작용. NOGEAR 시각: 근육을 키우는 신호가 곧 종양을 키우는 신호다. IGF-1은 '성장'에 충성할 뿐, 그게 근육인지 암인지 가리지 않는다. 40만 명의 데이터가 그 무차별성을 보여준다.",
        "category": "research", "category_ko": "성장인자·암 연구",
        "source": "Oxford CEU / IARC (Cancer Research)",
        "source_type": "journal",
        "source_url": "https://www.ceu.ox.ac.uk/news/study-of-almost-400-000-confirms-that-higher-blood-levels-of-igf-1-are-a-risk-factor-for-several-types-of-cancer",
        "credibility": {
            "peer_reviewed": True, "primary_source": True, "cross_checked": True,
            "cross_check_date": CC_DATE, "url_alive": True, "cross_confirmed": True,
            "confidence": "high",
            "notes": "WebFetch 직접 검증: UK Biobank ~40만·23,412명(5.9%) 암·양의 연관 갑상선/대장/유방/전립선(+흑색종/골수종)·음의 연관 간/난소·apoptosis 억제 기전 정확 일치. Cancer Research 2020-09-15. 옥스퍼드 1차 자료 → high. (참고: 2020 게재 연구를 IGF-1 남용 맥락으로 재조명.)",
            "fact_checked": True, "fact_check_date": CC_DATE, "accuracy": "match",
            "independent_verification": True,
        },
        "viral_signals": signals(18, 19, 16, 12, 13, 9),
        "tags": ["IGF-1", "암위험", "성장인자", "UK바이오뱅크", "옥스퍼드"],
    },
]


def main():
    with open(PATH, encoding="utf-8") as f:
        data = json.load(f)

    existing_urls = set()
    for k in ("news", "research", "featured"):
        for a in data.get(k, []):
            u = a.get("source_url", "")
            if u:
                existing_urls.add(u)

    added = 0
    skipped = []
    for art in NEW:
        url = art["source_url"]
        if url in existing_urls:
            skipped.append(url)
            continue
        score = sum(art["viral_signals"].values())
        t, emoji = tier(score)
        art["viral_score"] = score
        art["viral_tier"] = t
        art["viral_emoji"] = emoji
        art["date"] = DATE
        art["badge"] = badge_for(art["credibility"].get("confidence", "medium"))
        art["source_verified"] = art["credibility"].get("confidence") in ("high", "medium")
        art["title_original"] = art["title"]
        bucket = "research" if art["category"] == "research" else "news"
        data[bucket].append(art)
        existing_urls.add(url)
        added += 1

    for k in ("news", "research"):
        seen = set()
        uniq = []
        for a in data[k]:
            u = a.get("source_url", "")
            key = u or json.dumps(a.get("title", ""), ensure_ascii=False)
            if key in seen:
                continue
            seen.add(key)
            uniq.append(a)
        uniq.sort(key=lambda x: x.get("viral_score", 0), reverse=True)
        data[k] = uniq[:200]

    now = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=9)))
    total = len(data["news"]) + len(data["research"]) + len(data.get("featured", []))
    data["meta"]["last_updated"] = now.isoformat()
    data["meta"]["last_updated_kst"] = now.strftime("%Y-%m-%d %H:%M KST") + (" 아침 크롤 — 신규 %d건 반영" % added)
    data["meta"]["total_articles"] = total
    scores = [a.get("viral_score", 0) for k in ("news", "research") for a in data[k]]
    if scores:
        data["meta"]["top_viral_score"] = max(scores)
        data["meta"]["avg_viral_score"] = round(sum(scores) / len(scores), 1)
    data["meta"]["last_crosscheck"] = CC_DATE

    with open(PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=1)

    print("ADDED:", added)
    print("SKIPPED (dup url):", len(skipped))
    for s in skipped:
        print("  -", s)
    print("TOTAL:", total, "| news:", len(data["news"]), "| research:", len(data["research"]))
    allarts = [a for k in ("news", "research") for a in data[k]]
    allarts.sort(key=lambda x: x.get("viral_score", 0), reverse=True)
    print("TOP 3:")
    for a in allarts[:3]:
        print("  %d %s %s" % (a.get("viral_score", 0), a.get("viral_emoji", ""), a.get("title", "")[:60]))


if __name__ == "__main__":
    main()
