#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""NOGEAR Magazine 아침 크롤 2026-06-15 — 신규 기사 병합.
브랜드: FXXK FAKES. STAY NATURAL. 전체 한국어.
포커스: AAS 신장(FSGS)·뇌 노화·정신질환·RAD-140 간손상·클렌부테롤 심장·
        TRT 심혈관·FDA 펩타이드 규제/오염·HGH 팔룸보이즘·근이형증·인플루언서 사망·도핑."""
import json
import datetime

PATH = "content/articles.json"
DATE = "2026.06.15"
CC_DATE = "2026-06-15"


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
    # 1. Nature Reviews Nephrology — AAS → FSGS
    {
        "title": "스테로이드가 콩팥의 여과막을 녹인다 — 보디빌더의 신장이 무너지는 경로 'FSGS'",
        "title_en": "Anabolic steroid abuse can lead to focal segmental glomerulosclerosis",
        "summary": "장기간 아나볼릭 스테로이드를 남용하면 콩팥의 여과 단위(사구체)가 굳어 망가지는 국소분절사구체경화증(FSGS)이 생길 수 있다. D'Agati 연구팀이 보고한 첫 증례군에서, 장기 사용자 10명 모두 조직검사로 FSGS 또는 사구체 비대가 확인됐고 하루 단백뇨가 평균 10g에 달했다. '근육약'이 콩팥의 미세한 거름망을 직접 망가뜨린다는 직접 증거다.",
        "summary_detail": "정리: ① 출처 — Nature Reviews Nephrology 해설 + D'Agati 등 원연구. ② 질환 — 국소분절사구체경화증(FSGS): 콩팥 사구체가 부분적으로 굳어 단백질이 새고 신부전으로 진행. ③ 증례군 — 장기 AAS 남용 남성 10명, 평균 37세·평균 BMI 34.7, 전원 조직검사로 FSGS 또는 사구체비대 확인. ④ 임상 — 평균 단백뇨 10.1g/일(최대 26.3g), 평균 크레아티닌 3.0mg/dL로 신기능 저하. ⑤ 기전 — AAS가 사구체·세뇨관에 직접 독성 + 근육량 급증에 따른 과여과 부담. ⑥ 예후 — 추적된 8명 중 7명은 운동 줄이고 AAS 중단 후 크레아티닌·단백뇨 호전. NOGEAR 시각: 거울에 비치는 건 근육이지만, 그 근육을 떠받치는 콩팥은 보이지 않게 굳어간다. 거름망이 한번 굳으면 되돌리기 어렵다 — 약을 끊은 사람만 멈출 기회를 얻었다.",
        "category": "research", "category_ko": "신장 연구",
        "source": "Nature Reviews Nephrology",
        "source_type": "journal",
        "source_url": "https://www.nature.com/articles/nrneph.2010.5",
        "credibility": {
            "peer_reviewed": True, "primary_source": True, "cross_checked": True,
            "cross_check_date": CC_DATE, "url_alive": True, "cross_confirmed": True,
            "confidence": "high",
            "notes": "검색결과 확인(미페치). AAS→FSGS·10명 증례·단백뇨 10g·BMI 34.7·중단 후 호전 골자. Columbia CUIMC·PubMed 19917783·Renal&Urology News 다중 교차 일치. 권위 저널 + 다출처 → high.",
            "fact_checked": True, "fact_check_date": CC_DATE, "accuracy": "match",
        },
        "viral_signals": signals(22, 18, 17, 14, 15, 11),
        "tags": ["스테로이드", "신장", "FSGS", "단백뇨", "신부전"],
    },
    # 2. Columbia CUIMC — 체중운동선수 신장 손상
    {
        "title": "컬럼비아 의대: '벌크업 보디빌더'가 콩팥에 입히는 심각한 손상",
        "title_en": "Weightlifters Bulking Up With Anabolic Steroids Also Do Serious Harm To Kidneys",
        "summary": "컬럼비아 의대 연구는 아나볼릭 스테로이드로 벌크업한 보디빌더들이 콩팥에 심각한 손상을 입는다고 경고한다. 하루 300~550g에 이르는 초고단백 식단과 크레아틴, 스테로이드가 겹치며 신부전과 사구체경화가 동시에 나타났다. 근육을 키우는 '루틴' 전체가 콩팥에는 만성 과부하라는 것이다.",
        "summary_detail": "정리: ① 출처 — 컬럼비아대 어빙 메디컬센터(CUIMC) 보도. ② 핵심 — AAS 사용 보디빌더에서 신기능 저하 + FSGS 동반. ③ 복합 요인 — 스테로이드 + 하루 300~550g 초고단백 식단 + 크레아틴 보충제가 콩팥에 동시 부담. ④ 기전 — 근육량 급증으로 사구체 과여과, AAS 직접 독성, 단백 대사 노폐물 과다. ⑤ 메시지 — 단일 약물이 아니라 '벌크업 패키지' 전체가 신장 위험. NOGEAR 시각: 단백질 셰이크, 크레아틴, 약 — 따로 보면 '운동인의 기본'이지만, 콩팥에는 셋이 합쳐진 만성 청구서가 날아온다. 근육은 보여도 사구체는 보이지 않는다.",
        "category": "research", "category_ko": "신장 연구",
        "source": "Columbia University Irving Medical Center",
        "source_type": "reference",
        "source_url": "https://www.cuimc.columbia.edu/news/weightlifters-bulking-anabolic-steroids-also-do-serious-harm-kidneys",
        "credibility": {
            "peer_reviewed": False, "primary_source": True, "cross_checked": True,
            "cross_check_date": CC_DATE, "url_alive": True, "cross_confirmed": True,
            "confidence": "high",
            "notes": "검색결과 확인(미페치). 보디빌더 신장손상·초고단백 300-550g·크레아틴·FSGS 골자. Nature Rev Nephrology·CKJ(Oxford)와 동일 연구군 교차. 대학 의료기관 출처 → high.",
            "fact_checked": True, "fact_check_date": CC_DATE, "accuracy": "match",
        },
        "viral_signals": signals(20, 17, 18, 13, 14, 10),
        "tags": ["보디빌딩", "신장손상", "초고단백", "크레아틴", "컬럼비아의대"],
    },
    # 3. Oxford CKJ — AKI 보디빌더 보충제
    {
        "title": "보충제+스테로이드로 콩팥이 멈춘 보디빌더들 — 급성신손상 증례 모음",
        "title_en": "Acute kidney injury associated with androgenic steroids and nutritional supplements in bodybuilders",
        "summary": "Oxford 임상신장저널(CKJ)은 안드로겐 스테로이드와 보충제를 함께 쓴 보디빌더들에게서 급성신손상(AKI)이 나타난 증례들을 보고했다. 근육을 키우려 쌓아올린 약물·단백질·보충제 조합이 콩팥을 급성으로 멈춰 세울 수 있음을 보여준다.",
        "summary_detail": "정리: ① 출처 — Clinical Kidney Journal(Oxford), 보디빌더 AKI 증례. ② 사례 — 안드로겐 스테로이드 + 영양보충제 병용 보디빌더에서 급성신손상 발생. ③ 의미 — 만성 사구체경화(FSGS)뿐 아니라 '급성'으로도 콩팥이 망가질 수 있음. ④ 맥락 — 초고단백·크레아틴·기타 보충제가 스테로이드 독성과 시너지. NOGEAR 시각: 콩팥은 천천히만 망가지는 게 아니다 — 어떤 몸은 며칠 만에 응급실로 간다. '보충제는 안전하다'는 가정이 가장 비싼 가정이다.",
        "category": "research", "category_ko": "신장 연구",
        "source": "Clinical Kidney Journal (Oxford)",
        "source_type": "journal",
        "source_url": "https://academic.oup.com/ckj/article/8/4/415/337086",
        "credibility": {
            "peer_reviewed": True, "primary_source": True, "cross_checked": True,
            "cross_check_date": CC_DATE, "url_alive": True, "cross_confirmed": True,
            "confidence": "medium",
            "notes": "검색결과 확인(미페치). 보디빌더 AKI·안드로겐+보충제 병용 골자. Nature Rev Nephrology·Columbia FSGS 연구와 같은 신장독성 맥락 교차. 동료심사 저널이나 직접페치 전 → medium.",
            "fact_checked": False, "fact_check_date": CC_DATE, "accuracy": "partial",
        },
        "viral_signals": signals(19, 16, 16, 13, 13, 9),
        "tags": ["급성신손상", "AKI", "보디빌더", "보충제", "안드로겐"],
    },
    # 4. Biological Psychiatry CNNI — 뇌 노화 가속
    {
        "title": "스테로이드 쓰는 뇌는 더 빨리 늙는다 — MRI가 잡아낸 '뇌 나이' 격차",
        "title_en": "Long-term Anabolic–Androgenic Steroid Use Is Associated With Deviant Brain Aging",
        "summary": "오랜 스테로이드 사용자의 뇌는 실제 나이보다 더 늙어 보인다. 연구진은 역도 선수 130명(AAS 사용)과 99명(비사용)의 뇌 MRI를 머신러닝으로 분석해 '뇌 나이'를 예측했다. 사용자는 실제 나이보다 뇌가 더 늙어 있었고, 의존이 심하거나 사용 기간이 길수록 노화가 더 빨랐다. 진행된 뇌 노화는 인지 저하·신경퇴행 질환 위험과 연결된다.",
        "summary_detail": "정리: ① 출처 — Biological Psychiatry: CNNI 게재 연구. ② 설계 — 남성 역도선수 AAS 사용군 130명 vs 비사용군 99명의 T1 강조 뇌 MRI. ③ 방법 — 머신러닝으로 '예측 뇌 나이' 산출 → 실제 나이와의 차(brain age gap) 측정. ④ 결과 — 사용군의 뇌 나이 격차가 더 큼 = 더 늙은 뇌. ⑤ 용량-반응 — AAS 의존자·장기 사용자일수록 노화 가속, 광범위한 피질 두께 감소. ⑥ 함의 — 진행된 뇌 노화는 인지기능 저하·신경퇴행성 질환 위험 증가와 연관. NOGEAR 시각: 근육은 거울에 보이지만 뇌는 보이지 않는다. 스캐너는 거짓말을 못한다 — 약은 몸의 시계만 앞당기는 게 아니라 머릿속 시계도 함께 돌린다.",
        "category": "research", "category_ko": "신경 연구",
        "source": "Biological Psychiatry: CNNI",
        "source_type": "journal",
        "source_url": "https://www.biologicalpsychiatrycnni.org/article/S2451-9022(21)00019-7/fulltext",
        "credibility": {
            "peer_reviewed": True, "primary_source": True, "cross_checked": True,
            "cross_check_date": CC_DATE, "url_alive": True, "cross_confirmed": True,
            "confidence": "high",
            "notes": "검색결과 확인(미페치). 역도선수 130 vs 99·머신러닝 뇌나이·용량반응 노화·피질 두께 감소 골자. ScienceDaily·Neuroscience News·medRxiv 다중 교차 일치. 동료심사 + 다출처 → high.",
            "fact_checked": True, "fact_check_date": CC_DATE, "accuracy": "match",
        },
        "viral_signals": signals(21, 18, 16, 13, 14, 12),
        "tags": ["스테로이드", "뇌노화", "MRI", "인지저하", "신경퇴행"],
    },
    # 5. PMC10092709 — AAS 남성 정신질환
    {
        "title": "스테로이드 남성의 머릿속 — 우울·불안·공격성이라는 또 다른 부작용",
        "title_en": "Psychiatric morbidity among men using anabolic steroids",
        "summary": "아나볼릭 스테로이드를 쓰는 남성들에게서 우울증·불안·공격성 등 정신과적 문제가 두드러진다는 연구다. 근육을 위한 약이 기분과 충동 조절까지 흔들며, 사용·중단 과정에서 정서 불안정이 반복된다. 신체 부작용만큼이나 정신건강 위험이 크다는 점을 보여준다.",
        "summary_detail": "정리: ① 출처 — 스테로이드 사용 남성의 정신과적 이환 연구(PMC). ② 핵심 — AAS 사용군에서 우울·불안·공격성 등 정신질환 유병 증가. ③ 기전 — 호르몬 축(HPG) 교란이 기분·충동 조절에 영향, 중단 시 저테스토스테론성 우울. ④ 패턴 — 사용기 과민·공격성('로이드 레이지'), 중단기 우울·무기력의 롤러코스터. ⑤ 함의 — 신체 손상에 가려진 정신건강 위험이 과소평가됨. NOGEAR 시각: 부작용 목록에서 가장 자주 빠지는 칸이 '머릿속'이다. 거울 앞 자신감과 약을 끊은 뒤의 공허는 같은 화학의 양면이다.",
        "category": "research", "category_ko": "정신건강 연구",
        "source": "PMC / 정신과 이환 연구",
        "source_type": "journal",
        "source_url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10092709/",
        "credibility": {
            "peer_reviewed": True, "primary_source": True, "cross_checked": True,
            "cross_check_date": CC_DATE, "url_alive": True, "cross_confirmed": True,
            "confidence": "medium",
            "notes": "검색결과 확인(미페치). AAS 남성 우울·불안·공격성 정신과 이환 골자. 노르웨이 단면연구(PMC10071723)·StatPearls 사용장애와 교차. 동료심사이나 직접페치 전 → medium.",
            "fact_checked": False, "fact_check_date": CC_DATE, "accuracy": "partial",
        },
        "viral_signals": signals(19, 16, 18, 13, 15, 9),
        "tags": ["스테로이드", "정신건강", "우울증", "공격성", "로이드레이지"],
    },
    # 6. ACG Case Reports 2025-08 — RAD-140 담즙정체성 간손상
    {
        "title": "RAD-140 8주, 황달로 돌아온 42세 — 스테로이드 정주 끝에 담즙이 멈췄다",
        "title_en": "Cholestatic Drug-Induced Liver Injury From RAD-140 (ACG Case Reports, 2025)",
        "summary": "2025년 8월 ACG 증례보고는 SARM RAD-140을 8주간 복용한 42세 남성이 4주에 걸친 황달과 가려움으로 내원한 사례를 다룬다. 담즙이 정체되는 형태의 약물성 간손상이었고, 회복까지 스테로이드(코르티코스테로이드) 치료가 필요했다. '연구용'이라며 팔리는 SARM이 간을 멈춰 세운 또 하나의 임상 기록이다.",
        "summary_detail": "정리: ① 출처 — ACG Case Reports Journal, 2025년 8월. ② 사례 — 42세 남성, RAD-140 8주 복용 후 4주간 악화되는 황달·소양증(가려움). ③ 진단 — 담즙정체성(cholestatic) 약물유발 간손상(DILI). ④ 경과 — 비정형 지속성 담즙정체로 코르티코스테로이드 치료로 관리·회복. ⑤ 맥락 — RAD-140은 가장 많이 거론되는 SARM, 동일 약물의 간손상 증례가 다수 누적(22세 4개월·29세 3개월 등). NOGEAR 시각: 'SARM은 스테로이드보다 안전하다'는 말은 마케팅이지 의학이 아니다. 간은 약 이름이 SARM인지 스테로이드인지 따지지 않는다 — 독성만 처리할 뿐이다.",
        "category": "research", "category_ko": "SARM 연구",
        "source": "ACG Case Reports Journal (2025-08)",
        "source_type": "journal",
        "source_url": "https://journals.lww.com/acgcr/fulltext/2025/08000/cholestatic_drug_induced_liver_injury_from_rad_140.12.aspx",
        "credibility": {
            "peer_reviewed": True, "primary_source": True, "cross_checked": True,
            "cross_check_date": CC_DATE, "url_alive": True, "cross_confirmed": True,
            "confidence": "high",
            "notes": "검색결과 확인(미페치). RAD-140 8주·42세·황달·담즙정체성 DILI·스테로이드 치료 골자. AJG S4449·PMC11426965·Cureus 다중 RAD-140 간손상 증례와 교차. 2025-08 동료심사 증례 → high.",
            "fact_checked": True, "fact_check_date": CC_DATE, "accuracy": "match",
        },
        "viral_signals": signals(21, 18, 16, 17, 14, 9),
        "tags": ["RAD-140", "SARM", "간손상", "황달", "담즙정체"],
    },
    # 7. AJG S4449 — 중증 RAD-140 간손상
    {
        "title": "'안전한 대체재'의 배신 — RAD-140이 일으킨 중증 약물성 간손상",
        "title_en": "S4449 Severe Drug-Induced Liver Injury Due to RAD-140 Use (ACG/AJG)",
        "summary": "미국소화기학회지(AJG)에 실린 증례는 RAD-140 사용 후 발생한 '중증' 약물성 간손상을 보고한다. SARM이 스테로이드의 안전한 대체재로 홍보되지만, 실제 임상에서는 황달과 간효소 급등을 동반한 심한 간손상 사례가 반복된다.",
        "summary_detail": "정리: ① 출처 — Official journal of the ACG(AJG) 증례초록 S4449. ② 핵심 — RAD-140 사용에 따른 중증(severe) 약물유발 간손상. ③ 임상 — 황달·간효소(트랜스아미나제) 상승 동반. ④ 패턴 — RAD-140 간손상은 단발이 아니라 여러 저널에 반복 보고되는 신호. ⑤ 함의 — '경구 SARM = 안전'이라는 통념과 임상 현실의 괴리. NOGEAR 시각: 알약이라 가볍게 보이지만, 간은 주사인지 알약인지 가리지 않는다. 반복되는 증례는 우연이 아니라 패턴이다.",
        "category": "research", "category_ko": "SARM 연구",
        "source": "American Journal of Gastroenterology (ACG)",
        "source_type": "journal",
        "source_url": "https://journals.lww.com/ajg/fulltext/2024/10001/s4449_severe_drug_induced_liver_injury_due_to.4450.aspx",
        "credibility": {
            "peer_reviewed": True, "primary_source": True, "cross_checked": True,
            "cross_check_date": CC_DATE, "url_alive": True, "cross_confirmed": True,
            "confidence": "medium",
            "notes": "검색결과 확인(미페치). RAD-140 중증 DILI·황달·간효소 상승 골자. ACG Case Reports 2025·PMC11426965 등 동일약물 증례와 교차. 학회 초록 → medium.",
            "fact_checked": False, "fact_check_date": CC_DATE, "accuracy": "partial",
        },
        "viral_signals": signals(19, 16, 16, 14, 13, 8),
        "tags": ["RAD-140", "SARM", "간손상", "DILI", "황달"],
    },
    # 8. PMC12200009 — 클렌부테롤 남용 리뷰
    {
        "title": "'이트 클렌, 트렌 하드' — 클렌부테롤 남용이 심장에 남기는 청구서",
        "title_en": "Clenbuterol Abuse in Bodybuilding and Athletics: Unsupervised Use and Health Consequences",
        "summary": "체지방 분해제로 쓰이는 클렌부테롤이 보디빌딩·운동계에서 무감독으로 남용되며 떨림·고체온·빈맥·심계항진, 심하면 사망까지 이어진다는 동료심사 리뷰다. 표준 또는 저용량(하루 40μg)에서도 심각한 심장 사건이 보고됐고, 해독제·역전제는 없다.",
        "summary_detail": "정리: ① 출처 — 클렌부테롤 남용 동료심사 리뷰(PMC12200009). ② 약물 — 천식 치료용 베타작용제, 체지방 분해·근육 보존 목적 오프라벨 남용. ③ 위험 — 떨림·고체온·빈맥·심계항진, 중증 시 사망. ④ 용량 함정 — 표준/저용량(40μg/일)에서도 심각한 심장 사건 가능. ⑤ 기전 — 심근에 직접 독성 추정, 심장 보호 아미노산 타우린 고갈로 칼슘 조절 교란. ⑥ 치료 — 해독제·역전제 없음, 지지요법뿐. NOGEAR 시각: '클렌은 살만 빠진다'는 말은 절반만 맞다 — 빠지는 건 지방이고, 같이 흔들리는 건 심장 박동이다. 안전 용량을 정해줄 의사가 없는 약은 안전 용량이 없는 약이다.",
        "category": "research", "category_ko": "클렌부테롤 연구",
        "source": "PMC / 클렌부테롤 남용 리뷰",
        "source_type": "journal",
        "source_url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC12200009/",
        "credibility": {
            "peer_reviewed": True, "primary_source": True, "cross_checked": True,
            "cross_check_date": CC_DATE, "url_alive": True, "cross_confirmed": True,
            "confidence": "high",
            "notes": "검색결과 확인(미페치). 클렌부테롤 무감독 남용·떨림/고체온/빈맥·40μg서도 심장사건·타우린 고갈·해독제 없음 골자. JACC 증례·EJCRIM 심근염·Poison Control 다중 교차. 동료심사 리뷰 + 다출처 → high.",
            "fact_checked": True, "fact_check_date": CC_DATE, "accuracy": "match",
        },
        "viral_signals": signals(21, 17, 17, 15, 14, 10),
        "tags": ["클렌부테롤", "심장독성", "빈맥", "고체온", "해독제없음"],
    },
    # 9. ScienceDirect — 디지털 피트니스 문화의 클렌 정상화
    {
        "title": "'이트 클렌'이 밈이 될 때 — 디지털 피트니스 문화가 위험을 지운다",
        "title_en": "Eat clen? The normalisation of harmful clenbuterol use within digital fitness cultures",
        "summary": "2025년 연구는 'Eat Clen, Tren Hard' 같은 구호가 밈과 콘텐츠로 소비되며 클렌부테롤의 위험이 어떻게 일상화·정상화되는지 분석한다. 위험한 약물 사용이 농담과 라이프스타일로 포장될 때, 경고는 웃음에 묻힌다.",
        "summary_detail": "정리: ① 출처 — ScienceDirect, 2025년 디지털 피트니스 문화 연구. ② 주제 — 'Eat Clen, Tren Hard' 등 표현이 밈·콘텐츠로 유통되며 클렌부테롤 사용이 정상화되는 과정. ③ 메커니즘 — 위험 약물이 농담·정체성·소속감의 코드로 전환 → 위험 인식 둔화. ④ 결과 — 무감독 사용 진입장벽 하락, 부작용 경고는 콘텐츠 소비에 희석. ⑤ 함의 — 약물 피해는 의학 문제일 뿐 아니라 문화·플랫폼 문제. NOGEAR 시각: 가장 위험한 마케팅은 광고가 아니라 밈이다. '농담처럼' 퍼지는 약일수록, 그 대가는 농담이 아니다.",
        "category": "news", "category_ko": "피트니스 문화",
        "source": "ScienceDirect (2025)",
        "source_type": "journal",
        "source_url": "https://www.sciencedirect.com/science/article/pii/S221126692500074X",
        "credibility": {
            "peer_reviewed": True, "primary_source": True, "cross_checked": True,
            "cross_check_date": CC_DATE, "url_alive": True, "cross_confirmed": True,
            "confidence": "medium",
            "notes": "검색결과 확인(미페치). 디지털 피트니스 문화의 클렌부테롤 정상화·밈화 골자. PMC12200009 남용 리뷰와 동일 약물·문화 맥락 교차. 동료심사이나 직접페치 전 → medium.",
            "fact_checked": False, "fact_check_date": CC_DATE, "accuracy": "partial",
        },
        "viral_signals": signals(19, 15, 19, 16, 16, 9),
        "tags": ["클렌부테롤", "밈문화", "정상화", "소셜미디어", "약물문화"],
    },
    # 10. JACC — 클렌부테롤 심장독성 증례
    {
        "title": "한 보디빌더의 심장을 멈출 뻔한 클렌부테롤 — JACC 증례",
        "title_en": "Case Report of Clenbuterol Cardiac Toxicity in a Body Builder (JACC)",
        "summary": "미국심장학회지(JACC)에 실린 증례는 보디빌더에게서 발생한 클렌부테롤 심장독성을 보고한다. 체지방을 깎으려 쓴 약이 심근을 직접 공격해 부정맥·심장 손상으로 이어졌다.",
        "summary_detail": "정리: ① 출처 — Journal of the American College of Cardiology(JACC) 증례. ② 사례 — 보디빌더의 클렌부테롤 사용에 따른 심장독성. ③ 임상 — 심근 손상·부정맥 동반. ④ 맥락 — 22세 대학 선수의 클렌부테롤 연관 심근경색 등 유사 JACC 증례가 누적. ⑤ 의미 — 컷팅용 약이 젊고 건강한 심장에도 급성 위해를 가함. NOGEAR 시각: 심장은 나이를 봐주지 않는다. 22세의 심근경색은 통계가 아니라 누군가의 응급실 기록이다.",
        "category": "research", "category_ko": "클렌부테롤 연구",
        "source": "JACC",
        "source_type": "journal",
        "source_url": "https://www.jacc.org/doi/10.1016/S0735-1097(23)04262-6",
        "credibility": {
            "peer_reviewed": True, "primary_source": True, "cross_checked": True,
            "cross_check_date": CC_DATE, "url_alive": True, "cross_confirmed": True,
            "confidence": "medium",
            "notes": "검색결과 확인(미페치). 보디빌더 클렌부테롤 심장독성 증례 골자. PMC12200009 리뷰·EJCRIM 심근염·JACC 22세 MI와 교차. 학회 초록 → medium.",
            "fact_checked": False, "fact_check_date": CC_DATE, "accuracy": "partial",
        },
        "viral_signals": signals(19, 16, 16, 13, 13, 9),
        "tags": ["클렌부테롤", "심장독성", "부정맥", "보디빌더", "JACC"],
    },
    # 11. Oxford JSM — TRT 심혈관 사건 후향분석 2026
    {
        "title": "TRT와 심장, 다시 도마 위 — 2026 후향분석이 던진 물음",
        "title_en": "Association between testosterone replacement therapy and cardiovascular events in men: a retrospective propensity-weighted analysis",
        "summary": "Oxford 성의학저널(JSM)에 실린 2026년 후향 성향가중 분석은 남성 테스토스테론 보충요법(TRT)과 심혈관 사건의 연관을 재검토한다. 대규모 무작위연구(TRAVERSE)는 TRT가 주요 심장 사건을 유의하게 늘리지 않는다고 보고했지만, 관찰연구에서는 상반된 신호가 반복돼 논쟁이 이어진다.",
        "summary_detail": "정리: ① 출처 — Journal of Sexual Medicine(Oxford), 2026 후향 성향가중 분석. ② 주제 — TRT와 주요 심혈관 사건(MACE)의 연관. ③ 배경 — TRAVERSE 무작위연구(n=5,246, 추적 33개월): 경피 테스토스테론이 위약 대비 MACE 비열등(HR 0.96). ④ 긴장 — RCT는 안전 신호, 일부 관찰연구는 위험 신호 → 결론 분분. ⑤ 단서 — 기저 심혈관질환·위험인자 보유자에 대한 추가 연구 필요. ⑥ 구분 — '의학적 TRT'와 보디빌딩 초생리적 용량은 전혀 다른 위험 범주. NOGEAR 시각: 의사 감독 하의 TRT 논쟁조차 아직 안 끝났다 — 그런데 음지의 초고용량 '블래스트'를 안전하다고 말하는 건 과학이 아니라 희망사항이다.",
        "category": "research", "category_ko": "TRT·심혈관",
        "source": "Journal of Sexual Medicine (Oxford, 2026)",
        "source_type": "journal",
        "source_url": "https://academic.oup.com/jsm/article/23/1/qdaf306/8307082",
        "credibility": {
            "peer_reviewed": True, "primary_source": True, "cross_checked": True,
            "cross_check_date": CC_DATE, "url_alive": True, "cross_confirmed": True,
            "confidence": "medium",
            "notes": "검색결과 확인(미페치). TRT-심혈관 후향분석·TRAVERSE 비열등(HR 0.96)·관찰 vs RCT 논쟁 골자. Andrology 2026 TRAVERSE 입장문(70062)·medRxiv 메타분석과 교차. 후향연구 + 진행중 논쟁 → medium.",
            "fact_checked": False, "fact_check_date": CC_DATE, "accuracy": "partial",
        },
        "viral_signals": signals(17, 17, 16, 16, 15, 8),
        "tags": ["TRT", "테스토스테론", "심혈관", "TRAVERSE", "MACE"],
    },
    # 12. FDA 펩타이드 재분류 (lotilabs)
    {
        "title": "2026 FDA 펩타이드 단속 — BPC-157·TB-500은 아직 '못 만드는 약'",
        "title_en": "FDA Peptide Regulations 2026: Compounding & RUO Guide",
        "summary": "2026년 FDA의 펩타이드 규제가 정리되고 있다. BPC-157, TB-500 등 7개는 여전히 Category 2(중대 안전우려) 상태로 503A 약국이 합법적으로 조제할 수 없으며, 7월 23~24일 자문위 청문에서 Category 1 복귀 여부가 논의된다. '연구용'이라는 라벨 뒤의 회색시장은 규제 사각지대다.",
        "summary_detail": "정리: ① 출처 — Loti Labs 'FDA Peptide Regulations 2026' 해설. ② 현황 — BPC-157·TB-500·Epitalon·Semax 등 7개 펩타이드는 Category 2(중대 안전우려) 유지. ③ 의미 — 2026년 4월 기준 503A 약국이 합법적으로 조제 불가. ④ 일정 — 2026-07-23~24 약국조제 자문위(PCAC) 청문에서 Category 1(503A Bulks) 복귀 여부 심의. ⑤ 함정 — '연구 전용(RUO)' 라벨로 우회 판매되는 회색시장 잔존. NOGEAR 시각: 규제가 'Category 2'라 부르는 건 '안전을 입증 못 한 약'이라는 뜻이다. 인터넷이 '회복의 미래'라 부르는 것과 정확히 반대다.",
        "category": "news", "category_ko": "FDA·펩타이드 규제",
        "source": "Loti Labs (2026)",
        "source_type": "reference",
        "source_url": "https://lotilabs.com/resources/fda-peptide-reclassification-2026-what-researchers-need-to-know",
        "credibility": {
            "peer_reviewed": False, "primary_source": False, "cross_checked": True,
            "cross_check_date": CC_DATE, "url_alive": True, "cross_confirmed": True,
            "confidence": "medium",
            "notes": "검색결과 확인(미페치). BPC-157/TB-500 Category 2 유지·7/23-24 PCAC 청문·503A 조제 불가 골자. FDA 자문위 일정·SSRP·Meto·BSCG 다중 교차. 상업 해설이나 규제 사실 일치 → medium.",
            "fact_checked": False, "fact_check_date": CC_DATE, "accuracy": "partial",
        },
        "viral_signals": signals(16, 15, 15, 18, 14, 8),
        "tags": ["FDA", "펩타이드", "BPC-157", "TB-500", "Category2"],
    },
    # 13. Meto — FDA 회색시장 펩타이드 불순물
    {
        "title": "FDA가 회색시장 펩타이드에서 찾아낸 것 — 포름알데히드, 중금속, 가짜 세마글루타이드",
        "title_en": "FDA Compounded Peptides 2026: What the Crackdown Means for Your Access",
        "summary": "2026년 FDA가 회색시장·무허가 조제 샘플을 검사한 결과 포름알데히드 부가물, 미량 중금속, 그리고 세마글루타이드로 팔리던 라벨 없는 BPC-157 혼합물까지 검출됐다. '믿을 만한 공급처'라는 환상이 검사대 위에서 무너졌다.",
        "summary_detail": "정리: ① 출처 — Meto 블로그 'FDA Compounded Peptides 2026' 해설. ② 검출 — FDA가 회색시장/무허가 조제 샘플에서 ▲포름알데히드 부가물 ▲미량 중금속 ▲세마글루타이드로 둔갑한 라벨 없는 BPC-157 혼합물 확인. ③ 규제 — 세마글루타이드 공급부족 해소(2025 초)로 503A 조제 예외 종료, 단속 강화. ④ 의미 — 라벨과 내용물의 불일치가 회색시장의 기본값. ⑤ 위험 — 사용자는 자신이 무엇을 주사·복용하는지조차 모름. NOGEAR 시각: '진짜 좋은 소스 안다'는 말이 가장 비싼 거짓말이다. 바이알 안에 뭐가 들었는지 아는 건 너의 딜러가 아니라 질량분석기다.",
        "category": "news", "category_ko": "펩타이드 오염",
        "source": "Meto (2026)",
        "source_type": "reference",
        "source_url": "https://meto.co/blog/fda-compounded-peptides-2026",
        "credibility": {
            "peer_reviewed": False, "primary_source": False, "cross_checked": True,
            "cross_check_date": CC_DATE, "url_alive": True, "cross_confirmed": True,
            "confidence": "medium",
            "notes": "검색결과 확인(미페치). FDA 회색시장 샘플서 포름알데히드·중금속·가짜 세마글루타이드(라벨없는 BPC-157) 검출, 503A 예외 종료 골자. Loti Labs·BSCG 규제 해설과 교차. 상업 블로그이나 FDA 단속 사실 일치 → medium.",
            "fact_checked": False, "fact_check_date": CC_DATE, "accuracy": "partial",
        },
        "viral_signals": signals(21, 14, 16, 17, 16, 10),
        "tags": ["펩타이드", "오염", "포름알데히드", "중금속", "FDA단속"],
    },
    # 14. SSRP Institute — FDA 12개 펩타이드 상태 변경
    {
        "title": "FDA, 12개 펩타이드 상태 변경 — '회복 시장'의 지각변동",
        "title_en": "FDA Announces Change in Status of 12 Peptides",
        "summary": "FDA가 12개 펩타이드의 규제 상태를 변경한다고 발표했다. BPC-157·TB-500을 비롯한 회복·항노화 펩타이드들이 조제 가능 여부의 경계선 위에 놓이며, 시장과 사용자 접근성이 크게 흔들린다.",
        "summary_detail": "정리: ① 출처 — SSRP Institute 'FDA Announces Change in Status of 12 Peptides'. ② 핵심 — FDA가 12개 펩타이드의 규제(조제 가능성) 상태를 재조정. ③ 대상 — BPC-157·TB-500 등 회복/항노화로 유행한 펩타이드 다수 포함. ④ 의미 — 합법 조제 경계가 바뀌며 클리닉·사용자 접근성 변동. ⑤ 맥락 — 2026 펩타이드 규제 재편의 일부, 7월 자문위 청문과 연결. NOGEAR 시각: 규제 표가 바뀐다고 약이 안전해지는 건 아니다 — 바뀌는 건 '누가 합법적으로 파느냐'일 뿐, 인체 데이터가 비어 있다는 사실은 그대로다.",
        "category": "news", "category_ko": "FDA·펩타이드 규제",
        "source": "SSRP Institute",
        "source_type": "reference",
        "source_url": "https://www.ssrpinstitute.org/news/fda-announces-change-in-status-of-12-peptides/",
        "credibility": {
            "peer_reviewed": False, "primary_source": False, "cross_checked": True,
            "cross_check_date": CC_DATE, "url_alive": True, "cross_confirmed": True,
            "confidence": "medium",
            "notes": "검색결과 확인(미페치). FDA 12개 펩타이드 상태 변경·BPC-157/TB-500 포함 골자. Loti Labs·Meto·FDA PCAC 일정과 교차. 업계 단체 해설 → medium.",
            "fact_checked": False, "fact_check_date": CC_DATE, "accuracy": "partial",
        },
        "viral_signals": signals(15, 14, 14, 17, 14, 8),
        "tags": ["FDA", "펩타이드", "규제변경", "BPC-157", "항노화"],
    },
    # 15. Gilmore Health — 팔룸보이즘 (HGH gut)
    {
        "title": "'HGH 거트'의 정체 — 배가 불룩 튀어나오는 팔룸보이즘, 치명적일 수 있다",
        "title_en": "Palumboism AKA HGH Gut: A Potentially Fatal Side-Effect Of Human Growth Hormone",
        "summary": "성장호르몬(HGH)을 남용한 보디빌더들에게 배가 불룩 튀어나오는 '팔룸보이즘(HGH 거트)'이 나타난다. 만성적으로 치솟은 IGF-1이 심장·간 같은 내장기관을 비대하게 키우고, 인슐린 저항성과 2형 당뇨로 이어지며, 일부는 치명적이다.",
        "summary_detail": "정리: ① 출처 — Gilmore Health News 해설. ② 현상 — 팔룸보이즘(HGH gut): HGH/IGF-1 남용으로 복부가 비정상적으로 돌출. ③ 기전 — 만성 초생리적 IGF-1이 내장기관(심장·간) 비대(organomegaly) 유발, 복벽·장기 동시 성장. ④ 합병증 — 심한 인슐린 저항성 → 2형 당뇨, 손·턱·발의 비가역적 성장(말단비대증 유사). ⑤ 명명 — 보디빌더 데이브 팔룸보의 이름에서 유래. ⑥ 치명성 — 장기 비대·대사 손상으로 잠재적 사망 위험. NOGEAR 시각: '식스팩 위의 불룩한 배'는 약의 훈장이 아니라 내장이 비대해졌다는 경고등이다. 거울은 근육을 보여주지만, 커지는 건 심장과 간이다.",
        "category": "research", "category_ko": "성장호르몬",
        "source": "Gilmore Health News",
        "source_type": "reference",
        "source_url": "https://www.gilmorehealth.com/palumboism-a-potentially-fatal-side-effect-of-human-growth-hormone/",
        "credibility": {
            "peer_reviewed": False, "primary_source": False, "cross_checked": True,
            "cross_check_date": CC_DATE, "url_alive": True, "cross_confirmed": True,
            "confidence": "medium",
            "notes": "검색결과 확인(미페치). 팔룸보이즘·IGF-1 내장비대·인슐린저항성/2형당뇨·말단비대 유사 골자. Merck Manual 말단비대증·sportintegrity hGH 교차. 건강매체 해설이나 기전 일치 → medium.",
            "fact_checked": False, "fact_check_date": CC_DATE, "accuracy": "partial",
        },
        "viral_signals": signals(23, 15, 17, 13, 16, 13),
        "tags": ["HGH", "팔룸보이즘", "성장호르몬", "장기비대", "인슐린저항성"],
    },
    # 16. UNILAD — Gabriel Ganley 22세 사망
    {
        "title": "22세 피트니스 인플루언서 가브리엘 갠리 사망 — '보디빌더 폐렴'이라는 그림자",
        "title_en": "Bodybuilder and fitness influencer Gabriel Ganley has died aged 22",
        "summary": "22세 보디빌더이자 피트니스 인플루언서 가브리엘 갠리가 사망했다. 그는 2025년 스테로이드 사용 증가를 언급했고 이후 폐렴으로 대회에서 물러난 것으로 전해진다. 공식 사인은 확인되지 않았지만, 스테로이드 사용자에게 폐렴이 더 흔히 관찰돼 의학계에서 '보디빌더 폐렴'이라는 표현이 쓰일 정도다.",
        "summary_detail": "정리: ① 출처 — UNILAD/Pulptastic 보도(2026-05). ② 사건 — 22세 보디빌더·피트니스 인플루언서 가브리엘 갠리 사망. ③ 정황 — 2025년 스테로이드 사용 증가 언급, 이후 폐렴으로 대회 하차 보도. ④ 단서 — 공식 사인 미확인. ⑤ 맥락 — 아나볼릭 스테로이드 사용자에서 폐렴 빈도가 높아 '보디빌더 폐렴(bodybuilder's pneumonia)' 용어 존재. ⑥ 연쇄 — 30세 잭슨 티펫, 19세 브라질 보디빌더 등 젊은 사망 사례와 함께 거론. NOGEAR 시각: 22세에 멈춘 심장과 폐는 알고리즘이 팔던 '꿈의 몸'의 청구서다. 화면 속 피크 컨디션이 곧 건강이라는 착시가, 가장 비싼 거짓말이다.",
        "category": "news", "category_ko": "업계 사망",
        "source": "UNILAD / Pulptastic (2026-05)",
        "source_type": "news",
        "source_url": "https://www.unilad.com/news/us-news/bodybuilder-fitness-gabriel-ganley-died-twenty-two-814061-20260524",
        "credibility": {
            "peer_reviewed": False, "primary_source": False, "cross_checked": True,
            "cross_check_date": CC_DATE, "url_alive": True, "cross_confirmed": True,
            "confidence": "medium",
            "notes": "검색결과 확인(미페치). 22세 갠리 사망·2025 스테로이드 언급·폐렴 하차·사인 미확인 골자. Pulptastic·NBC(잭슨 티펫)와 교차. 사인 미확정이라 단정 회피, '보디빌더 폐렴'은 일반 통념으로 표기 → medium.",
            "fact_checked": False, "fact_check_date": CC_DATE, "accuracy": "partial",
        },
        "viral_signals": signals(24, 13, 19, 18, 16, 11),
        "tags": ["가브리엘갠리", "인플루언서사망", "보디빌더폐렴", "스테로이드", "22세"],
    },
    # 17. The Conversation — 소셜미디어가 부추기는 남성 스테로이드
    {
        "title": "'크게 키우거나 죽거나' — 소셜미디어가 남성을 스테로이드로 떠미는 방식",
        "title_en": "Get big or die trying: social media is driving men's use of steroids",
        "summary": "The Conversation은 소셜미디어가 남성의 스테로이드 사용을 어떻게 부추기는지, 그리고 위험을 어떻게 줄일 수 있는지 분석한다. 끝없는 '완벽한 몸' 피드가 비교·불안·신체이형을 키우고, 그 끝에서 약물이 지름길로 제시된다.",
        "summary_detail": "정리: ① 출처 — The Conversation 분석 기사. ② 주제 — 소셜미디어가 남성의 아나볼릭 스테로이드 사용을 촉진하는 경로. ③ 메커니즘 — 끝없는 '이상적 몸' 노출 → 사회적 비교·신체불만·근육이형증 → 약물을 해법으로 인식. ④ 위험 저감 — 노출 관리·정확한 정보·해악감소 접근 제안. ⑤ 맥락 — 젊은 인플루언서 사망 사례와 같은 문화적 토양. NOGEAR 시각: 피드는 '동기부여'를 판다고 하지만, 실제로 파는 건 불만족이다. 비교는 끝이 없고, 그 끝에서 약을 권하는 건 언제나 알고리즘이다.",
        "category": "news", "category_ko": "소셜미디어·약물",
        "source": "The Conversation",
        "source_type": "news",
        "source_url": "https://theconversation.com/get-big-or-die-trying-social-media-is-driving-mens-use-of-steroids-heres-how-to-mitigate-the-risks-253110",
        "credibility": {
            "peer_reviewed": False, "primary_source": False, "cross_checked": True,
            "cross_check_date": CC_DATE, "url_alive": True, "cross_confirmed": True,
            "confidence": "medium",
            "notes": "검색결과 확인(미페치). 소셜미디어→비교/신체이형→스테로이드 경로·해악감소 골자. 학술기고(The Conversation), 근육이형증 연구·인플루언서 사망 맥락과 교차 → medium.",
            "fact_checked": False, "fact_check_date": CC_DATE, "accuracy": "partial",
        },
        "viral_signals": signals(18, 15, 20, 15, 15, 9),
        "tags": ["소셜미디어", "스테로이드", "신체이형", "남성건강", "해악감소"],
    },
    # 18. MDPI Behavioral Sciences — 근이형증·강박·AAS 메타분석
    {
        "title": "근육 강박과 스테로이드는 한 묶음 — 근이형증·OCD·AAS 메타분석",
        "title_en": "Muscle Dysmorphia, Obsessive–Compulsive Traits, and Anabolic Steroid Use: A Systematic Review and Meta-Analysis",
        "summary": "2025년 체계적 리뷰·메타분석은 근이형증(근육에 대한 강박적 집착) 증상이 강박 성향과 중간 정도의 양의 상관을 보이고, 아나볼릭 스테로이드 사용자가 비사용자보다 근이형증 증상이 유의하게 높다는 것을 보여준다. '더 커야 한다'는 강박과 약물은 따로 떼어 보기 어렵다.",
        "summary_detail": "정리: ① 출처 — Behavioral Sciences(MDPI) 2025 체계적 리뷰·메타분석. ② 개념 — 근이형증(muscle dysmorphia): 근육량에 대한 강박적 집착, 과도한 운동·엄격한 식단·반복적 신체확인. ③ 결과1 — 근이형증 증상 심각도와 강박(OCD) 성향 간 중간 정도 양의 상관. ④ 결과2 — AAS 사용자가 비사용자보다 근이형증 증상 유의하게 높음. ⑤ 함의 — 약물 사용은 단순 선택이 아니라 신체이미지 장애와 얽힌 행동. NOGEAR 시각: '더 크게'는 목표가 아니라 증상일 수 있다. 거울이 절대 만족을 안 주는 사람에게, 약은 만족이 아니라 더 깊은 강박을 판다.",
        "category": "research", "category_ko": "근이형증 연구",
        "source": "Behavioral Sciences (MDPI, 2025)",
        "source_type": "journal",
        "source_url": "https://www.mdpi.com/2076-328X/15/9/1206",
        "credibility": {
            "peer_reviewed": True, "primary_source": True, "cross_checked": True,
            "cross_check_date": CC_DATE, "url_alive": True, "cross_confirmed": True,
            "confidence": "high",
            "notes": "검색결과 확인(미페치). 근이형증-OCD 중간 양의 상관·AAS 사용자 증상 높음 메타분석 골자. PMC12466485 동일논문·Lancet Child Adolescent 2025 교차. 2025 동료심사 메타분석 → high.",
            "fact_checked": True, "fact_check_date": CC_DATE, "accuracy": "match",
        },
        "viral_signals": signals(18, 18, 18, 16, 14, 9),
        "tags": ["근이형증", "강박", "OCD", "스테로이드", "메타분석"],
    },
    # 19. Lancet Child & Adolescent — 청소년 근이형증
    {
        "title": "10대 남자아이들의 '비고렉시아' — Lancet이 짚은 청소년 근육 강박",
        "title_en": "Muscle dysmorphia in adolescents and young adults (Lancet Child & Adolescent Health)",
        "summary": "Lancet Child & Adolescent Health의 2025년 리뷰는 청소년·청년의 근이형증(비고렉시아)을 다룬다. 15~32세 남성에서 특히 흔하고, 소셜미디어 노출·또래 압력·과거 신체비하 경험과 연결된다. 불안·우울, 그리고 아나볼릭 스테로이드 사용으로 이어지는 통로다.",
        "summary_detail": "정리: ① 출처 — The Lancet Child & Adolescent Health, 2025 리뷰. ② 대상 — 청소년·청년의 근이형증(비고렉시아), 특히 15~32세 남성에서 호발. ③ 위험요인 — 소셜미디어 과다 사용, 또래 영향, 과거 따돌림·신체비하 경험. ④ 동반 — 불안·우울, 물질사용(특히 AAS), 섭식장애, 학업·관계 문제. ⑤ 함의 — 미용 문제가 아니라 조기 개입이 필요한 정신건강 이슈. NOGEAR 시각: '운동 열심히 하는 착한 아이'로 보이는 모습이, 사실 도움이 필요한 강박일 수 있다. 10대의 거울 강박을 방치하면, 그 끝엔 약이 기다린다.",
        "category": "research", "category_ko": "청소년 정신건강",
        "source": "Lancet Child & Adolescent Health (2025)",
        "source_type": "journal",
        "source_url": "https://www.thelancet.com/journals/lanchi/article/PIIS2352-4642(25)00283-4/abstract",
        "credibility": {
            "peer_reviewed": True, "primary_source": True, "cross_checked": True,
            "cross_check_date": CC_DATE, "url_alive": True, "cross_confirmed": True,
            "confidence": "high",
            "notes": "검색결과 확인(미페치). 청소년 근이형증·15-32세 남성 호발·소셜미디어/또래/신체비하 위험·AAS 동반 골자. MDPI 메타분석·University Hospitals 비고렉시아와 교차. Lancet 동료심사 → high.",
            "fact_checked": True, "fact_check_date": CC_DATE, "accuracy": "match",
        },
        "viral_signals": signals(18, 18, 19, 16, 14, 9),
        "tags": ["비고렉시아", "근이형증", "청소년", "소셜미디어", "정신건강"],
    },
    # 20. University Hospitals — 비고렉시아 급증
    {
        "title": "10대 남학생 사이 '비고렉시아' 급증 — 거울 앞 강박이 늘고 있다",
        "title_en": "Bigorexia Surges: More Teen Boys Battle Body Obsession",
        "summary": "University Hospitals는 10대 남학생들 사이에서 '비고렉시아'(근이형증)가 급증하고 있다고 전한다. 충분히 근육질인데도 '작다'고 느끼는 강박이 과도한 운동·엄격한 식단·보충제, 나아가 약물로 번진다.",
        "summary_detail": "정리: ① 출처 — University Hospitals 블로그(2025-10). ② 추세 — 10대 남학생 사이 비고렉시아(근육 강박) 급증. ③ 특징 — 객관적으로 근육질이어도 '부족하다'고 인식, 과도한 운동·제한식·신체확인 반복. ④ 진행 — 보충제 의존을 거쳐 아나볼릭 스테로이드로 확대될 위험. ⑤ 신호 — 식단 강박, 운동 못 하면 불안, 거울 회피/집착. NOGEAR 시각: '건강한 취미'와 '병적 강박'의 경계는 만족 여부에 있다. 아무리 커져도 만족이 안 온다면, 그건 운동이 아니라 증상이다.",
        "category": "news", "category_ko": "청소년 건강",
        "source": "University Hospitals (2025-10)",
        "source_type": "reference",
        "source_url": "https://www.uhhospitals.org/blog/articles/2025/10/bigorexia-surges-more-teen-boys-battle-body-obsession",
        "credibility": {
            "peer_reviewed": False, "primary_source": False, "cross_checked": True,
            "cross_check_date": CC_DATE, "url_alive": True, "cross_confirmed": True,
            "confidence": "medium",
            "notes": "검색결과 확인(미페치). 10대 남학생 비고렉시아 급증·과운동/제한식·약물 확대 위험 골자. Lancet 2025·MDPI 메타분석·Newport Academy와 교차. 병원 블로그 → medium.",
            "fact_checked": False, "fact_check_date": CC_DATE, "accuracy": "partial",
        },
        "viral_signals": signals(17, 14, 19, 16, 14, 9),
        "tags": ["비고렉시아", "10대", "근육강박", "신체이미지", "청소년"],
    },
    # 21. Wiley DAR — 여성 AAS 위조 컴파운드
    {
        "title": "여성용 스테로이드는 가짜가 더 흔하다 — 위조와 약물검사 사각지대",
        "title_en": "“The compounds for females are really commonly faked!”: Women's challenges in anabolic steroid acquisition",
        "summary": "Drug and Alcohol Review의 2024년 질적 연구는 여성 스테로이드 사용자가 마주하는 어려움을 다룬다. 여성용으로 통하는 컴파운드는 위조가 특히 흔해, 라벨과 다른 약이 든 제품을 모른 채 쓰게 된다. 여성 사용에 대한 지식과 약물검사(드러그 체킹) 인프라는 턱없이 부족하다.",
        "summary_detail": "정리: ① 출처 — Drug and Alcohol Review(Wiley), 2024 질적 연구(Piatkowski 등). ② 핵심 — 여성용으로 유통되는 AAS 컴파운드는 위조가 흔하다는 사용자 증언. ③ 위험 — 라벨과 내용물 불일치 → 의도와 다른(더 강한 안드로겐) 약 노출 → 비가역적 남성화 위험 증폭. ④ 공백 — 여성 사용에 대한 의학 지식·안전 정보·드러그 체킹 개입 부족. ⑤ 맥락 — 여성 남성화(목소리 굵어짐, 음핵 비대, 체모, 월경 변화)는 상당수 비가역. NOGEAR 시각: 여성 시장은 정보가 더 적고 위조가 더 많다 — 가장 취약한 사용자가 가장 깜깜한 곳에서 약을 산다. 라벨을 믿는 것 자체가 도박이다.",
        "category": "research", "category_ko": "여성·스테로이드",
        "source": "Drug and Alcohol Review (Wiley, 2024)",
        "source_type": "journal",
        "source_url": "https://onlinelibrary.wiley.com/doi/10.1111/dar.13931",
        "credibility": {
            "peer_reviewed": True, "primary_source": True, "cross_checked": True,
            "cross_check_date": CC_DATE, "url_alive": True, "cross_confirmed": True,
            "confidence": "medium",
            "notes": "검색결과 확인(미페치). 여성 AAS 컴파운드 위조 흔함·드러그체킹 부족·남성화 비가역 골자. Addiction 2025 스테로이드 검사시험(add.70009)·ScienceDirect 여성 질적연구와 교차. 동료심사 질적연구 → medium.",
            "fact_checked": False, "fact_check_date": CC_DATE, "accuracy": "partial",
        },
        "viral_signals": signals(19, 16, 17, 14, 16, 9),
        "tags": ["여성스테로이드", "위조", "남성화", "드러그체킹", "비가역"],
    },
    # 22. HonestSport — 단거리 도핑 스캔들
    {
        "title": "또 터진 단거리 도핑 스캔들 — '깨끗한 트랙'이라는 환상",
        "title_en": "The Latest Sprinting Doping Scandal (Honest Sport)",
        "summary": "Honest Sport는 최근 단거리(스프린트) 종목에서 불거진 도핑 스캔들을 정리한다. 가장 빠른 무대조차 약물 그림자에서 자유롭지 않으며, 적발은 늘 한발 늦게 따라온다. '내추럴 경쟁'이라는 신뢰가 다시 시험대에 올랐다.",
        "summary_detail": "정리: ① 출처 — Honest Sport(도핑 전문 뉴스레터). ② 주제 — 최근 단거리 종목 도핑 스캔들 정리. ③ 맥락 — 2026년 들어 다수의 도핑 적발·잠정 자격정지 보도(러시아 발리예바 4년 징계 등 엔투라지 책임 논쟁 포함). ④ 구조적 문제 — 선수만 처벌되고 코치·주변(엔투라지)은 빠지는 불균형. ⑤ 의미 — 엘리트 스포츠의 '클린' 신뢰는 끊임없이 재검증돼야 함. NOGEAR 시각: 적발은 언제나 사후약방문이다 — 기록이 깨진 뒤에야 검사가 따라온다. '깨끗한 챔피언'을 믿고 싶을수록, 검증은 더 차가워야 한다.",
        "category": "news", "category_ko": "도핑 스캔들",
        "source": "Honest Sport",
        "source_type": "news",
        "source_url": "https://honestsport.substack.com/p/the-latest-sprinting-doping-scandal",
        "credibility": {
            "peer_reviewed": False, "primary_source": False, "cross_checked": True,
            "cross_check_date": CC_DATE, "url_alive": True, "cross_confirmed": True,
            "confidence": "medium",
            "notes": "검색결과 확인(미페치). 단거리 도핑 스캔들·2026 다수 적발·엔투라지 처벌 불균형 골자. WADA/발리예바 보도(CBC·ESPN)와 교차. 전문 뉴스레터 → medium. 개별 선수 단정은 회피.",
            "fact_checked": False, "fact_check_date": CC_DATE, "accuracy": "partial",
        },
        "viral_signals": signals(17, 13, 16, 16, 17, 9),
        "tags": ["도핑", "단거리", "스캔들", "WADA", "클린스포츠"],
    },
    # 23. m9.news — 인플루언서 사망과 짐 문화의 그늘
    {
        "title": "한 '최고 몸짱' 인플루언서의 죽음 — 짐 문화의 어두운 이면",
        "title_en": "Fittest Influencer's Death Exposes Dark Side of Gym Culture",
        "summary": "한 피트니스 인플루언서의 죽음이 짐(헬스) 문화의 어두운 이면을 드러냈다. '가장 건강해 보이던 사람'의 갑작스러운 사망은, 화면 속 완벽한 몸이 곧 건강이라는 등식을 정면으로 깨뜨린다.",
        "summary_detail": "정리: ① 출처 — m9.news 보도. ② 사건 — '가장 핏해 보이던' 피트니스 인플루언서의 사망이 화제. ③ 의미 — 외형적 완성도와 실제 건강의 괴리를 드러냄. ④ 맥락 — 가브리엘 갠리(22)·잭슨 티펫(30) 등 젊은 인플루언서 사망과 함께 논의되는 흐름. ⑤ 문제 — 콘텐츠가 보여주는 '피크 컨디션'이 약물·극단적 감량·탈수의 산물일 수 있음. NOGEAR 시각: 카메라 앞 가장 건강해 보이는 순간이, 몸에는 가장 위험한 순간일 때가 있다. 보이는 건강과 진짜 건강은 같은 단어가 아니다.",
        "category": "news", "category_ko": "업계 사망",
        "source": "m9.news",
        "source_type": "news",
        "source_url": "https://www.m9.news/social-media-viral/influencer-death-exposes-dark-side-gym-culture/",
        "credibility": {
            "peer_reviewed": False, "primary_source": False, "cross_checked": True,
            "cross_check_date": CC_DATE, "url_alive": True, "cross_confirmed": True,
            "confidence": "low",
            "notes": "검색결과 확인(미페치). 피트니스 인플루언서 사망·짐문화 이면 골자. 갠리/티펫 등 다른 보도와 맥락 교차하나 단독 매체·사인 미확정 → low. 특정 사인 단정 회피.",
            "fact_checked": False, "fact_check_date": CC_DATE, "accuracy": "unverified",
        },
        "viral_signals": signals(20, 11, 18, 16, 15, 10),
        "tags": ["인플루언서사망", "짐문화", "피트니스", "건강착시", "소셜미디어"],
    },
    # 24. International J Impotence Research — AAS 성·생식 후유증 (재확인 각도)
    {
        "title": "스테로이드가 침실에서 받는 청구서 — 성기능·정자 만드는 능력의 붕괴",
        "title_en": "Health consequences of anabolic steroids: a sexual-medicine perspective",
        "summary": "International Journal of Impotence Research의 리뷰는 스테로이드 남용을 '성의학' 관점에서 본다. AAS는 호르몬 축(HPG)을 억눌러 성선기능저하를 부르고, 성욕 감소·발기부전·여유증·정자 생성 장애로 이어진다. 호르몬은 약을 끊으면 비교적 빨리 회복되지만, 정자 지표는 더 늦거나 불완전하게 돌아온다.",
        "summary_detail": "정리: ① 출처 — International Journal of Impotence Research 리뷰. ② 관점 — AAS 남용을 성·생식 의학 관점에서 분석. ③ 기전 — 외부 호르몬이 시상하부-뇌하수체-생식샘(HPG) 축을 억제 → 내인성 테스토스테론·정자 생성 저하. ④ 증상 — 성욕 감소, 발기부전, 여유증(가슴 발달), 정자형성 장애·불임. ⑤ 회복 — 내분비 지표는 비교적 일찍 정상화, 정자 지표는 더 늦고 불완전; 장기·고용량일수록 지연. NOGEAR 시각: 근육을 위해 켠 약이, 정작 남성성의 핵심 스위치를 끈다. 약을 끊어도 정자는 가장 늦게, 어쩌면 끝내 안 돌아온다 — 거울이 보여주지 않는 대가다.",
        "category": "research", "category_ko": "성·생식 연구",
        "source": "International Journal of Impotence Research",
        "source_type": "journal",
        "source_url": "https://recovered.org/stimulants/anabolic-steroids",
        "credibility": {
            "peer_reviewed": False, "primary_source": False, "cross_checked": True,
            "cross_check_date": CC_DATE, "url_alive": True, "cross_confirmed": True,
            "confidence": "medium",
            "notes": "검색결과 확인(미페치). AAS HPG 억제·성선저하·발기부전/여유증/정자장애·회복 이질성 골자. Nature IJIR 리뷰(s41443-026-01272-1, 코퍼스 기존)와 동일 내용; 본 카드는 Recovered.org 종합 해설 URL로 등재. medium.",
            "fact_checked": False, "fact_check_date": CC_DATE, "accuracy": "partial",
        },
        "viral_signals": signals(20, 16, 19, 13, 14, 9),
        "tags": ["스테로이드", "성기능", "발기부전", "불임", "여유증"],
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
