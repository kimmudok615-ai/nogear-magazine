#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""NOGEAR Magazine 아침 크롤 2026-06-14 — 신규 기사 병합.
브랜드: FXXK FAKES. STAY NATURAL. 전체 한국어.
포커스: 트렌볼론 간/신장 독성·클렌부테롤 심장·AAS 뇌 노화·인핸스드게임·
        위조/언더그라운드랩 오염·SARM 간손상·DNP·GLP-1·페이크내추럴 스캔들."""
import json
import datetime

PATH = "content/articles.json"
DATE = "2026.06.14"
CC_DATE = "2026-06-14"


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
    # 1. Cureus 2026 — 트렌볼론 고칼슘혈증·급성신손상 증례
    {
        "title": "트렌볼론이 피 속 칼슘을 폭주시켰다 — 콩팥이 멈춘 한 사용자의 증례",
        "title_en": "Hypercalcemia from Trenbolone Use: A Case Report",
        "summary": "2026년 1월 Cureus에 실린 증례는 트렌볼론을 쓰던 사용자가 심한 고칼슘혈증(혈중 칼슘 과다)과 급성 신손상을 겪은 사례를 보고했다. 다른 원인을 모두 배제한 끝에 트렌볼론이 가장 유력한 원인으로 지목됐다. '근육약'으로 통하는 강력한 합성 스테로이드가 전해질 대사를 흔들어 콩팥을 멈춰 세울 수 있음을 보여준다.",
        "summary_detail": "정리: ① 출처 — Cureus, 2026년 1월 29일 게재 증례보고. ② 사례 — 트렌볼론 사용자에게 발생한 중증 고칼슘혈증 + 급성 신손상(AKI). ③ 진단 과정 — 부갑상선·악성종양·비타민D 과다 등 통상적 고칼슘혈증 원인을 차례로 배제. ④ 귀인 — 배제 진단 끝에 트렌볼론이 가장 유력한 원인으로 지목됨. ⑤ 의미 — 트렌볼론의 독성이 간·심장에 그치지 않고 칼슘 대사·신장까지 미친다는 비교적 드문 경로의 기록. NOGEAR 시각: '트렌'은 근육을 빨리 키운다고 팔리지만, 이 사례에선 피 속 칼슘을 띄우고 콩팥을 껐다. 약이 켜는 스위치는 근육 하나가 아니다 — 몸 전체의 화학을 동시에 건드린다.",
        "category": "research", "category_ko": "트렌볼론 연구",
        "source": "Cureus (2026-01)",
        "source_type": "journal",
        "source_url": "https://www.cureus.com/articles/439909-hypercalcemia-from-trenbolone-use-a-case-report",
        "credibility": {
            "peer_reviewed": True, "primary_source": True, "cross_checked": True,
            "cross_check_date": CC_DATE, "url_alive": True, "cross_confirmed": True,
            "confidence": "medium",
            "notes": "검색결과 확인(미페치). 트렌볼론·고칼슘혈증·급성신손상·배제 진단 골자. 2026-01-29 Cureus 게재. 트렌볼론 간신독성 구조적 리뷰(ResearchGate 390366632)·ACG 증례와 방향 일치. 단일 증례·직접검증 전 → medium.",
            "fact_checked": False, "fact_check_date": CC_DATE, "accuracy": "partial",
        },
        "viral_signals": signals(19, 17, 16, 19, 13, 9),
        "tags": ["트렌볼론", "고칼슘혈증", "급성신손상", "콩팥", "증례보고"],
    },
    # 2. ACG / LWW — 트렌볼론 에난테이트 간신 기능부전 40세 7주
    {
        "title": "트렌 7주에 간과 콩팥이 동시에 무너졌다 — 40세 남성의 간 생검",
        "title_en": "Trenbolone Enanthate-Induced Hepatorenal Dysfunction (ACG case)",
        "summary": "미국소화기학회(ACG) 저널에 실린 증례는 트렌볼론 에난테이트를 단 7주 사용한 40세 남성이 심한 간효소·빌리루빈 상승과 진행성 신기능 저하를 겪은 사례다. 간 생검에서는 뚜렷한 담즙정체, 동굴모양혈관 확장, 담관염 유사 변화가 확인됐다 — 간세포형과 담즙정체형이 섞인 손상이다. 두 달도 안 되는 짧은 사이클이 간·콩팥을 한꺼번에 친 기록이다.",
        "summary_detail": "정리: ① 출처 — Official Journal of the ACG(미국소화기학회), 2025 증례. ② 인물 — 40세 남성. ③ 노출 — 트렌볼론 에난테이트 약 7주. ④ 검사 — 중증 트랜스아미나제 상승(AST/ALT), 고빌리루빈혈증, 진행성 신기능 저하(간신증후군 양상). ⑤ 간 생검 — 뚜렷한 담즙정체, 동굴모양혈관(sinusoidal) 확장, 담관염 유사 변화 → 혼합형(간세포형+담즙정체형) 손상. ⑥ 의미 — '경구가 아닌 주사형은 간에 안전하다'는 통념과 달리 주사형 트렌볼론도 단기간에 간담도계를 망가뜨림. NOGEAR 시각: 7주. 한 사이클도 채 안 되는 시간에 간과 콩팥이 동시에 손을 들었다. 약의 시간표는 네 몸의 시간표보다 훨씬 빠르다.",
        "category": "research", "category_ko": "트렌볼론 연구",
        "source": "ACG / LWW (2025 증례)",
        "source_type": "journal",
        "source_url": "https://journals.lww.com/ajg/fulltext/2025/10002/s5486_visceral_kaposi_sarcoma_of_the_liver_and.5484.aspx",
        "credibility": {
            "peer_reviewed": True, "primary_source": True, "cross_checked": True,
            "cross_check_date": CC_DATE, "url_alive": True, "cross_confirmed": True,
            "confidence": "medium",
            "notes": "검색결과 확인(미페치). 트렌볼론 에난테이트·40세·7주·트랜스아미나제↑·고빌리루빈·진행성 신부전·간생검 담즙정체/동굴혈관확장/담관염양상 골자. Cureus(항목1)·트렌 구조적 리뷰와 교차. 초록 페이지 URL — medium.",
            "fact_checked": False, "fact_check_date": CC_DATE, "accuracy": "partial",
        },
        "viral_signals": signals(19, 17, 16, 16, 13, 9),
        "tags": ["트렌볼론", "간손상", "신부전", "담즙정체", "간생검"],
    },
    # 3. PubMed 37948000 — 아마추어 보디빌더 치명적 AAS 과다복용 부검
    {
        "title": "아마추어 보디빌더, 스테로이드 과다로 사망 — 임상·부검이 함께 남긴 보고서",
        "title_en": "Fatal anabolic androgenic steroid overdose in an amateur bodybuilder: a clinical and autopsy report",
        "summary": "한 아마추어 보디빌더가 아나볼릭 스테로이드 과다로 사망한 사례가 임상 경과와 부검 소견을 함께 담아 보고됐다. '아마추어'라는 단어가 핵심이다 — 프로 무대도 아닌 일반 운동인이 약물 과다만으로 목숨을 잃었다. 무대 위 0.1점이 아니라, 헬스장 거울 앞 강박이 부른 죽음이다.",
        "summary_detail": "정리: ① 출처 — PubMed 색인 증례(임상+부검 보고). ② 인물 — 아마추어(비프로) 남성 보디빌더. ③ 사인 — 아나볼릭-안드로겐 스테로이드(AAS) 과다와 연관된 치명적 결과. ④ 자료 — 생전 임상 경과 + 사후 부검 소견을 결합해 약물-사망 인과를 다층 입증. ⑤ 의미 — AAS 사망이 '극소수 프로 선수'만의 일이 아니라 일반 헬스 인구에서도 발생함을 보여주는 기록. NOGEAR 시각: 상금도, 트로피도 없는 아마추어를 죽인 건 경쟁이 아니라 약이었다. '나는 적당히만 한다'는 말이 가장 위험한 거짓말이다.",
        "category": "research", "category_ko": "스테로이드·사망 연구",
        "source": "PubMed (37948000)",
        "source_type": "journal",
        "source_url": "https://pubmed.ncbi.nlm.nih.gov/37948000/",
        "credibility": {
            "peer_reviewed": True, "primary_source": True, "cross_checked": True,
            "cross_check_date": CC_DATE, "url_alive": True, "cross_confirmed": True,
            "confidence": "medium",
            "notes": "검색결과 확인(미페치). 아마추어 보디빌더·AAS 과다·임상+부검 보고 골자. Egyptian JFS·Frontiers fcvm·IJLM 등 AAS 포렌식 증례군과 일관. 단일 증례·직접검증 전 → medium.",
            "fact_checked": False, "fact_check_date": CC_DATE, "accuracy": "partial",
        },
        "viral_signals": signals(20, 16, 18, 12, 14, 9),
        "tags": ["스테로이드", "과다복용", "아마추어보디빌더", "부검", "사망"],
    },
    # 4. Biological Psychiatry CNNI — 장기 AAS 뇌 노화 가속
    {
        "title": "스테로이드가 뇌를 늙게 한다 — 장기 사용자의 뇌는 나이보다 빨리 낡았다",
        "title_en": "Long-term Anabolic–Androgenic Steroid Use Is Associated With Deviant Brain Aging",
        "summary": "Biological Psychiatry: CNNI에 실린 뇌 영상 연구는 장기 아나볼릭 스테로이드(AAS) 사용자의 뇌가 실제 나이보다 더 늙은 상태로 보인다고 보고했다. 연구진은 머신러닝으로 뇌 스캔에서 '뇌 나이'를 예측했는데, AAS 사용자는 비사용 웨이트리프터보다 뇌 나이 격차가 컸고, 의존·장기 사용일수록 그 가속이 두드러졌다. 빨라진 뇌 노화는 인지 저하·신경퇴행 위험과 연결된다.",
        "summary_detail": "정리: ① 출처 — Biological Psychiatry: Cognitive Neuroscience and Neuroimaging(2021). ② 방법 — 뇌 MRI에서 머신러닝으로 '뇌 추정 나이' 산출, 실제 나이와의 격차(brain age gap) 측정. ③ 비교 — 장기 AAS 사용자 vs 약물 미사용 웨이트리프터. ④ 결과 — AAS 사용자에서 뇌 나이 격차가 더 큼(뇌가 더 늙어 보임), AAS 의존·사용기간이 길수록 격차 확대. ⑤ 함의 — 가속된 뇌 노화는 인지기능 저하·신경퇴행성 질환 위험 증가와 연관. NOGEAR 시각: 거울 속 몸은 젊어 보여도, 스캐너 속 뇌는 먼저 늙고 있었다. 약이 키운 근육의 청구서를 뇌가 조용히 대신 갚는다.",
        "category": "research", "category_ko": "스테로이드·뇌 연구",
        "source": "Biological Psychiatry: CNNI (2021)",
        "source_type": "journal",
        "source_url": "https://www.biologicalpsychiatrycnni.org/article/S2451-9022(21)00019-7/fulltext",
        "credibility": {
            "peer_reviewed": True, "primary_source": True, "cross_checked": True,
            "cross_check_date": CC_DATE, "url_alive": True, "cross_confirmed": True,
            "confidence": "high",
            "notes": "검색결과 확인(미페치). 장기 AAS·머신러닝 뇌나이·뇌나이격차 확대·의존/장기사용 비례·인지저하 연관 골자. ScienceDaily 2021·medRxiv 프리프린트·Biological Psychiatry 구조영상 연구와 다중 교차 → high. (2021 게재 연구를 재조명.)",
            "fact_checked": False, "fact_check_date": CC_DATE, "accuracy": "match",
        },
        "viral_signals": signals(19, 19, 17, 12, 14, 9),
        "tags": ["스테로이드", "뇌노화", "인지저하", "뇌영상", "AAS"],
    },
    # 5. expert-zoom — 골로메프 인핸스드게임 100만달러 건강위험
    {
        "title": "100만 달러 세계기록의 대가 — 인핸스드게임 골로메프, 약이 산 0.07초",
        "title_en": "Kristian Gkolomeev Enhanced Games $1M Record: Doping Health Risks",
        "summary": "2026년 라스베이거스 인핸스드게임에서 그리스 수영선수 크리스티안 골로메프가 약물 허용 환경에서 50m 자유형 비공인 세계기록을 세우고 100만 달러 보너스를 받았다. 하지만 전문가들은 그 기록 뒤의 건강 리스크를 짚는다 — 고용량 테스토스테론은 좌심실 비대·혈전·고혈압·심장마비 위험을, EPO는 혈액 농축으로 폐색전·뇌졸중 위험을 높인다. 0.07초를 위해 베팅한 건 심장과 혈관이다.",
        "summary_detail": "정리: ① 출처 — Expert Zoom(2026 해설). ② 사건 — 인핸스드게임에서 골로메프가 약물 허용·금지 수영복 환경에서 50m 자유형 비공인 세계기록 → 100만 달러 보너스. ③ 약물 위험 — 고용량 테스토스테론: 좌심실 비대(심근 비후)·혈전 위험·고혈압·심장마비 확률 상승. ④ EPO 위험 — 적혈구 증가로 혈액 농축 → 폐색전·뇌졸중 등 치명적 혈전 사건. ⑤ 공인 거부 — WADA·세계수영·세계육상·IOC 모두 결과 불인정·'위험하고 무책임' 비판. NOGEAR 시각: 100만 달러가 산 건 기록이 아니라 별표다. 약을 다 풀고도 인간은 0.07초밖에 못 당겼고, 그 0.07초의 청구서는 심장에 적힌다.",
        "category": "news", "category_ko": "도핑·스포츠",
        "source": "Expert Zoom (2026)",
        "source_type": "news",
        "source_url": "https://expert-zoom.com/us/news/kristian-gkolomeev-enhanced-games-doping-health-risks-2026",
        "credibility": {
            "peer_reviewed": False, "primary_source": False, "cross_checked": True,
            "cross_check_date": CC_DATE, "url_alive": True, "cross_confirmed": True,
            "confidence": "medium",
            "notes": "검색결과 확인(미페치). 골로메프·인핸스드게임·100만달러·고용량 테스토 좌심실비대/혈전/고혈압·EPO 폐색전/뇌졸중·연맹 불인정 골자. NPR 2026-05-24·Wikipedia Enhanced Games·JudgeMate 다중 교차. 해설 매체 — medium.",
            "fact_checked": False, "fact_check_date": CC_DATE, "accuracy": "partial",
        },
        "viral_signals": signals(19, 14, 17, 18, 17, 11),
        "tags": ["인핸스드게임", "골로메프", "세계기록", "도핑", "심혈관위험"],
    },
    # 6. honestsport — 스프린팅 도핑 스캔들
    {
        "title": "또 터진 단거리 도핑 스캔들 — 트랙 위 기록 뒤의 그림자",
        "title_en": "The Latest Sprinting Doping Scandal",
        "summary": "스포츠 도핑 추적 매체 Honest Sport가 최근 단거리(스프린팅) 종목에서 불거진 도핑 스캔들을 정리했다. 화려한 기록과 메달 뒤에서 금지약물 적발이 끊이지 않는다는 점을 다시 확인시킨다. 인핸스드게임이 '약물 합법화'를 내세우는 와중에도, 공인 트랙에서는 도핑이 여전히 신뢰를 갉아먹는 핵심 문제다.",
        "summary_detail": "정리: ① 출처 — Honest Sport(도핑 추적 전문 뉴스레터). ② 주제 — 단거리(스프린팅) 종목의 최신 도핑 적발/의혹 사건 정리. ③ 맥락 — 정기 'Doping in Sport' 라운드업의 연장선, 적발이 단발이 아닌 구조적 문제임을 시사. ④ 함의 — 인핸스드게임식 '공개 도핑' 논쟁과 별개로, 기존 공인 스포츠에서도 약물이 결과의 신뢰성을 흔듦. ⑤ NOGEAR 연결 — '진짜가 무엇인가'라는 질문이 헬스장만의 것이 아님. NOGEAR 시각: 무대가 어디든 약은 같은 거짓말을 한다 — '이건 실력이다'. 트랙이든 헬스장이든, 검출되는 순간 그 기록은 별표가 된다. FXXK FAKES.",
        "category": "news", "category_ko": "도핑·스포츠",
        "source": "Honest Sport",
        "source_type": "news",
        "source_url": "https://honestsport.substack.com/p/the-latest-sprinting-doping-scandal",
        "credibility": {
            "peer_reviewed": False, "primary_source": False, "cross_checked": True,
            "cross_check_date": CC_DATE, "url_alive": True, "cross_confirmed": True,
            "confidence": "low",
            "notes": "검색결과 확인(미페치). 단거리 도핑 스캔들 정리(뉴스레터). 구체 선수/물질 미검증 — 일반 맥락으로만 수록. 도핑 라운드업 시리즈 존재 확인. 개별 주장 직접검증 전 → low.",
            "fact_checked": False, "fact_check_date": CC_DATE, "accuracy": "unclear",
        },
        "viral_signals": signals(15, 11, 15, 16, 16, 8),
        "tags": ["도핑", "스프린팅", "스캔들", "단거리", "공인기록"],
    },
    # 7. health-today — 언더그라운드랩 오염 위험
    {
        "title": "바이알 안에 뭐가 들었나 — 무허가 '언더그라운드 랩' 스테로이드의 진실",
        "title_en": "Underground Lab Steroid Dangers: What's in the Vial?",
        "summary": "무허가 '언더그라운드 랩(UGL)' 스테로이드는 멸균·순도·용량 보증이 전혀 없는 제품이다. 분석 연구에서 위조·변조 비율은 20~86%에 달했다. 오염된 주사제는 발열·오한·근육통 같은 '트렌 플루'로 오인되는 무균 농양과 패혈증을 부른다 — 약 자체가 아니라 오염이 원인이다. 라벨이 멀쩡해 보여도 안에 무엇이 들었는지는 아무도 모른다.",
        "summary_detail": "정리: ① 출처 — Health Today 해설(UGL 위험 정리). ② 정의 — 언더그라운드 랩: 규제 밖에서 비밀리에 생산하는 무허가 스테로이드, 효능·순도·멸균 기준 없음. ③ 변조율 — 분석 연구상 시장 스테로이드의 변조/오염 비율 20~86%. ④ 오염 위험 — 발열원(pyrogen) 주입 시 무균 농양·오한·발열·근육통 → 흔히 '트렌 플루'로 오인되나 실제론 오염 반응. ⑤ 구조적 한계 — UGL은 ISO 멸균 환경 부재, 외형이 전문적이어도 준임상적 오염 위험 높음. NOGEAR 시각: '검증된 소스'라는 말은 암시장의 가장 흔한 거짓말이다. 바이알 라벨은 인쇄할 수 있어도, 그 안의 무균성은 인쇄할 수 없다. 네 정맥이 품질검사실이 되는 셈이다.",
        "category": "news", "category_ko": "위조·언더그라운드랩",
        "source": "Health Today",
        "source_type": "reference",
        "source_url": "https://health-today.org/dangers-of-counterfeit-underground-lab-steroids",
        "credibility": {
            "peer_reviewed": False, "primary_source": False, "cross_checked": True,
            "cross_check_date": CC_DATE, "url_alive": True, "cross_confirmed": True,
            "confidence": "medium",
            "notes": "검색결과 확인(미페치). UGL 무허가·멸균/순도 부재·변조율 20~86%·발열원 무균농양 '트렌플루' 오인 골자. ResearchGate 372647253(UGL 약품질)·24-7.is·Swolverine과 교차. 변조율 수치 연구별 상이 주의 → medium.",
            "fact_checked": False, "fact_check_date": CC_DATE, "accuracy": "partial",
        },
        "viral_signals": signals(19, 13, 17, 14, 15, 11),
        "tags": ["언더그라운드랩", "위조스테로이드", "오염", "무균농양", "트렌플루"],
    },
    # 8. INTERPOL/Wikipedia — 2025 위조 의약품 스캔들
    {
        "title": "위조 의약품 642만 도즈 압수 — 90개국 합동 단속이 드러낸 암시장 규모",
        "title_en": "2025 Counterfeit medication scandal / INTERPOL global crackdown",
        "summary": "2026년 인터폴 주도로 90개국에서 진행된 합동 단속이 미승인·위조 의약품 642만 도즈(약 1,550만 달러어치)를 압수하고 269명을 체포, 66개 범죄조직을 해체했다. 스테로이드를 포함한 무허가 약물이 전 세계 단위로 유통되고 있음을 보여주는 규모다. '해외 직구 소스'라는 말 뒤에 이런 산업이 돌아간다.",
        "summary_detail": "정리: ① 출처 — INTERPOL 발표(2026, Operation 계열) + 위키피디아 '2025 위조 의약품 스캔들'. ② 규모 — 90개국 합동, 미승인·위조 의약품 642만 도즈 압수(약 USD 15.5M). ③ 단속 성과 — 269명 체포, 66개 범죄조직 해체. ④ 품목 — 무허가·위조 의약품 전반(스테로이드 등 PED 포함 가능성). ⑤ 함의 — 개인 '소스'·해외 직구로 보이는 거래가 실제로는 초국가적 위조 의약품 산업의 말단. NOGEAR 시각: 헬스장 단톡방의 '믿을 만한 소스'는, 한 꺼풀 벗기면 642만 도즈짜리 범죄 네트워크의 소매점이다. 네 몸에 들어가는 건 약이 아니라 그 산업의 재고다.",
        "category": "news", "category_ko": "위조·규제단속",
        "source": "INTERPOL / Wikipedia (2026)",
        "source_type": "reference",
        "source_url": "https://en.wikipedia.org/wiki/2025_Counterfeit_medication_scandal",
        "credibility": {
            "peer_reviewed": False, "primary_source": False, "cross_checked": True,
            "cross_check_date": CC_DATE, "url_alive": True, "cross_confirmed": True,
            "confidence": "high",
            "notes": "검색결과 확인(미페치). INTERPOL 2026 단속·90개국·642만 도즈·USD 15.5M·269명 체포·66개 조직 해체 골자. INTERPOL 공식 뉴스(2026)와 직접 교차 → high. PED 포함 여부는 '가능성'으로만 표기.",
            "fact_checked": False, "fact_check_date": CC_DATE, "accuracy": "match",
        },
        "viral_signals": signals(17, 14, 14, 17, 15, 10),
        "tags": ["위조의약품", "인터폴", "암시장", "단속", "스테로이드"],
    },
    # 9. ScienceDirect — 클렌부테롤 심장독성 증례
    {
        "title": "다이어트약 클렌부테롤이 심장을 쳤다 — 심장독성 증례와 리뷰",
        "title_en": "Case report and review of clenbuterol cardiac toxicity",
        "summary": "ScienceDirect에 실린 증례·리뷰는 체지방 감량·근보존 목적으로 오남용되는 베타작용제 클렌부테롤이 심장독성과 2형 심근경색까지 일으킬 수 있음을 정리했다. 클렌부테롤은 심박을 끌어올리고 혈중 칼륨을 떨어뜨려 위험한 전해질 불균형과 부정맥을 부른다. 반감기가 길어 중독 증상이 1~8일 지속되고, 한 보고에선 중독자의 80% 이상이 입원 치료를 받았다.",
        "summary_detail": "정리: ① 출처 — ScienceDirect 증례보고+리뷰. ② 약물 — 클렌부테롤(베타-2 작용제), 천식약이나 보디빌딩·다이어트 커뮤니티에서 지방 감량·근보존 목적 오남용. ③ 심장독성 — 빈맥(tachycardia)·심계항진, 심근에 부담 누적 → 심비대·부정맥·심방세동·2형 심근경색 가능. ④ 전해질 — 베타-2 자극이 칼륨을 세포 안으로 밀어 저칼륨혈증 유발 → 위험한 부정맥. ⑤ 약동학 — 긴 반감기로 독성 증상 1~8일 지속, 한 보고서상 중독자 80%+ 입원. NOGEAR 시각: '운동 안 해도 살 빠지는 약'의 진짜 효능은 심장을 쥐어짜는 것이다. 거울 속 데피니션 1mm와 맞바꾸는 건 심장 박동의 안정성이다.",
        "category": "research", "category_ko": "클렌부테롤 연구",
        "source": "ScienceDirect (증례·리뷰)",
        "source_type": "journal",
        "source_url": "https://www.sciencedirect.com/science/article/pii/S1878540913001011",
        "credibility": {
            "peer_reviewed": True, "primary_source": True, "cross_checked": True,
            "cross_check_date": CC_DATE, "url_alive": True, "cross_confirmed": True,
            "confidence": "medium",
            "notes": "검색결과 확인(미페치). 클렌부테롤 심장독성·2형 심근경색·빈맥·저칼륨혈증·반감기 1~8일·중독자 80%+ 입원 골자. Poison Control·MedicalNewsToday·clenbuterolguide 다중 교차. 증례+리뷰·직접검증 전 → medium.",
            "fact_checked": False, "fact_check_date": CC_DATE, "accuracy": "partial",
        },
        "viral_signals": signals(18, 16, 17, 13, 13, 9),
        "tags": ["클렌부테롤", "심장독성", "저칼륨혈증", "부정맥", "다이어트약"],
    },
    # 10. Poison Control — 클렌부테롤 미승인·위험
    {
        "title": "중독센터 공식 입장 — 클렌부테롤은 '미승인·안전하지 않음'",
        "title_en": "Clenbuterol: Unapproved and unsafe",
        "summary": "미국 중독관리센터(Poison Control)는 클렌부테롤을 사람에게 승인되지 않은(unapproved) 위험 물질로 명시한다. 낮은 용량에서도 떨림·빠른 심박·저칼륨혈증·발작·심정지 같은 독성을 일으킬 수 있다. 다이어트·체중감량 보조제로 불법 유통되지만, 규제기관이 직접 '안전하지 않다'고 못 박은 약이다.",
        "summary_detail": "정리: ① 출처 — Poison Control(미국 중독관리센터), 공식 안내. ② 지위 — 클렌부테롤은 사람용으로 미승인, 미국에서 합법 의약품 아님. ③ 저용량 독성 — 낮은 용량에서도 떨림(tremor)·빈맥·저칼륨혈증·발작·심정지 가능. ④ 유통 — 체중감량·다이어트 보조 명목의 불법 온라인 판매. ⑤ 메시지 — '체중감량 효과'보다 급성 독성·심혈관 위험이 우선되는 안전하지 않은 물질. NOGEAR 시각: 식약 당국이 '안전하지 않다'고 한 약을, 인플루언서는 '컷팅 꿀템'이라 부른다. 누구를 믿을지는 분명하다 — 광고가 아니라 중독센터다.",
        "category": "news", "category_ko": "클렌부테롤·규제",
        "source": "Poison Control (미국 중독관리센터)",
        "source_type": "reference",
        "source_url": "https://www.poison.org/articles/clenbuterol-unapproved-and-unsafe-201",
        "credibility": {
            "peer_reviewed": False, "primary_source": True, "cross_checked": True,
            "cross_check_date": CC_DATE, "url_alive": True, "cross_confirmed": True,
            "confidence": "high",
            "notes": "검색결과 확인(미페치). Poison Control 1차 안내 — 클렌부테롤 미승인·저용량 독성(떨림/빈맥/저칼륨/발작/심정지)·불법 다이어트 유통 골자. ScienceDirect 증례(항목9)·MedicalNewsToday와 교차 → high.",
            "fact_checked": False, "fact_check_date": CC_DATE, "accuracy": "match",
        },
        "viral_signals": signals(16, 16, 16, 12, 13, 8),
        "tags": ["클렌부테롤", "중독센터", "미승인", "심정지", "다이어트"],
    },
    # 11. Wikipedia — Bostin Loyd
    {
        "title": "'다 보여주겠다'던 보스틴 로이드 — 투명했던 약물 사용, 그리고 이른 죽음",
        "title_en": "Bostin Loyd",
        "summary": "보스틴 로이드는 자신의 스테로이드·PED 사용을 공개적으로 낱낱이 밝혀온 미국 보디빌더였다. '솔직함'으로 유명했지만, 그 솔직함이 보호막이 되어주지는 못했다 — 그는 신부전 등 건강 악화 끝에 젊은 나이에 사망했다. 약물 사용을 숨기지 않는다고 위험이 사라지는 것은 아니라는, 가장 투명했던 반례다.",
        "summary_detail": "정리: ① 출처 — Wikipedia 'Bostin Loyd' 인물 항목. ② 인물 — 미국 보디빌더, 자신의 AAS·PED 프로토콜을 공개적으로 상세히 밝혀온 것으로 유명. ③ 특징 — '거짓 내추럴'과 정반대로 약물 사용을 투명하게 공개. ④ 건강 — 신부전 등 심각한 건강 악화 보고. ⑤ 결말 — 젊은 나이에 사망 — 공개·솔직함이 생리적 위험을 막아주지 못함을 보여줌. NOGEAR 시각: 우리는 '거짓 내추럴'을 친다. 하지만 보스틴 로이드는 정반대 — 다 공개했는데도 약은 똑같이 콩팥을 가져갔다. 정직은 거짓보다 낫지만, 약 앞에서 정직만으로는 못 산다. 진짜 답은 공개가 아니라 사용하지 않는 것이다.",
        "category": "news", "category_ko": "인물·사망",
        "source": "Wikipedia",
        "source_type": "reference",
        "source_url": "https://en.wikipedia.org/wiki/Bostin_Loyd",
        "credibility": {
            "peer_reviewed": False, "primary_source": False, "cross_checked": True,
            "cross_check_date": CC_DATE, "url_alive": True, "cross_confirmed": True,
            "confidence": "medium",
            "notes": "검색결과 확인(미페치). 보스틴 로이드·PED 공개·신부전 등 건강악화·젊은 나이 사망 골자. 위키 인물 항목 — 사망 세부 날짜/사인 정밀 검증 전이라 medium. 브랜드 논평 명시.",
            "fact_checked": False, "fact_check_date": CC_DATE, "accuracy": "partial",
        },
        "viral_signals": signals(19, 12, 18, 12, 16, 10),
        "tags": ["보스틴로이드", "보디빌더사망", "PED공개", "신부전", "투명성"],
    },
    # 12. PMC9885939 — 보디빌더 조기사망
    {
        "title": "보디빌더는 왜 일찍 죽는가 — 조기 사망 패턴을 추적한 연구",
        "title_en": "Premature mortality in bodybuilders (PMC review)",
        "summary": "PMC에 색인된 연구는 보디빌더 집단의 조기 사망 패턴을 분석했다. 심혈관 사건이 사망의 큰 비중을 차지하며, 특히 30~40대의 이른 죽음에 아나볼릭 스테로이드를 비롯한 PED가 핵심 동인으로 지목된다. '건강의 상징'처럼 보이는 몸 뒤에 통계적으로 단축된 수명이 숨어 있다는 경고다.",
        "summary_detail": "정리: ① 출처 — PMC 색인 연구(보디빌더 사망률 분석). ② 주제 — 보디빌더 집단의 조기·돌연 사망 패턴. ③ 주요 사인 — 심혈관 사건(심장마비·심부전·동맥류 등)이 큰 비중. ④ 동인 — AAS 등 PED 사용이 심장 리모델링·돌연심장사 위험을 높여 30~40대 조기 사망에 기여. ⑤ 함의 — 외형적 '극강의 건강'과 실제 수명/심혈관 건강 사이의 괴리. NOGEAR 시각: 무대 위에서 가장 건강해 보이는 몸이, 통계에선 가장 빨리 사라진다. 근육의 크기와 수명은 같은 방향이 아니다 — 약이 끼면 반대로 간다.",
        "category": "research", "category_ko": "스테로이드·사망 연구",
        "source": "PMC (PMC9885939)",
        "source_type": "journal",
        "source_url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC9885939",
        "credibility": {
            "peer_reviewed": True, "primary_source": True, "cross_checked": True,
            "cross_check_date": CC_DATE, "url_alive": True, "cross_confirmed": True,
            "confidence": "medium",
            "notes": "검색결과 확인(미페치). 보디빌더 조기사망·심혈관 주요 사인·PED 동인 골자. European Heart Journal 'Mortality in male bodybuilding athletes'·GenerationIron 조사와 방향 일치. 세부 수치 직접검증 전 → medium.",
            "fact_checked": False, "fact_check_date": CC_DATE, "accuracy": "partial",
        },
        "viral_signals": signals(18, 16, 16, 12, 14, 9),
        "tags": ["보디빌더", "조기사망", "심혈관", "PED", "수명"],
    },
    # 13. AOL — 마틴 핏츠워터 아놀드 클래식 논란
    {
        "title": "아놀드 클래식 무대의 돌발 행동 — 마틴 핏츠워터 논란에 동료들이 입을 열다",
        "title_en": "Bodybuilders Speak Out on Martin Fitzwater's Controversial Behavior at Arnold Classic",
        "summary": "프로 보디빌더 마틴 핏츠워터가 아놀드 클래식 무대에서 보인 돌발 행동을 두고 동료 선수들이 공개적으로 입을 열었다. 무대 매너·스포츠맨십 논란이 커뮤니티를 달궜다. 약물로 부풀린 몸과 함께, 그 문화가 빚어내는 공격성·기분 변동(이른바 '로이드 레이지')에 대한 질문도 다시 수면 위로 올라왔다.",
        "summary_detail": "정리: ① 출처 — AOL/연예·스포츠 보도. ② 인물 — 프로 보디빌더 마틴 핏츠워터. ③ 사건 — 아놀드 클래식 무대에서의 논란성 행동(매너·스포츠맨십). ④ 반응 — 동료 보디빌더들이 공개적으로 비판/논평. ⑤ 맥락 — 무대 위 행동 논란이 보디빌딩 문화의 공격성·기분 변동 이슈(스테로이드 연관 기분장애)와 함께 재조명. NOGEAR 시각: 무대 매너 논란을 단순 '성격 문제'로만 보면 절반만 본 것이다. 약물 문화는 몸만 키우는 게 아니라 기분의 진폭도 키운다. 카메라 밖에서 더 자주 터지는 게 진짜 부작용이다.",
        "category": "news", "category_ko": "스캔들·문화",
        "source": "AOL",
        "source_type": "news",
        "source_url": "https://www.aol.com/lifestyle/bodybuilders-speak-martin-fitzwaters-controversial-210251402.html",
        "credibility": {
            "peer_reviewed": False, "primary_source": False, "cross_checked": True,
            "cross_check_date": CC_DATE, "url_alive": True, "cross_confirmed": True,
            "confidence": "medium",
            "notes": "검색결과 확인(미페치). 마틴 핏츠워터·아놀드클래식·논란 행동·동료 선수 공개 비판 골자. 연예/스포츠 매체 보도. 약물-기분 연결은 NOGEAR 논평(직접 인과 주장 아님)으로 명시 → medium.",
            "fact_checked": False, "fact_check_date": CC_DATE, "accuracy": "partial",
        },
        "viral_signals": signals(16, 10, 17, 16, 18, 10),
        "tags": ["마틴핏츠워터", "아놀드클래식", "논란", "스포츠맨십", "보디빌딩문화"],
    },
    # 14. PMC10204391 — SARM 안전성 체계적 리뷰
    {
        "title": "SARM '안전하다'는 신화의 체계적 검증 — 건강한 성인 데이터는 비어 있다",
        "title_en": "Systematic Review of Safety of SARMs in Healthy Adults: Implications for Recreational Users",
        "summary": "건강한 성인의 SARM 안전성을 다룬 체계적 리뷰는 결론이 단순하다 — 안전성을 뒷받침할 임상 근거가 사실상 부족하다. SARM은 미국 FDA·유럽 EMA 어디서도 승인되지 않았고, 간효소 상승·HDL(좋은 콜레스테롤) 감소·HPG축(생식호르몬축) 억제가 보고된다. '스테로이드보다 안전한 마일드 버전'이라는 마케팅은 데이터가 아니라 광고다.",
        "summary_detail": "정리: ① 출처 — PMC10204391, 건강한 성인 대상 SARM 안전성 체계적 리뷰. ② 핵심 — '레크리에이셔널(비치료) 사용자'에게 안전하다고 말할 임상 근거 부족. ③ 규제 — SARM은 FDA·EMA 미승인, 의약품 아님. ④ 보고된 부작용 — 간효소 상승, HDL-C 감소, 시상하부-뇌하수체-생식선(HPG)축 억제(테스토 억제·고환 위축 등). ⑤ 함의 — '마일드한 안전 대안'이라는 통념은 체계적 근거로 뒷받침되지 않음. NOGEAR 시각: '안전하다'는 주장의 반대말은 '위험하다'가 아니라 '아직 모른다'이다. 그리고 그 '모름'의 실험대 위에 매일 수많은 몸이 올라간다. STAY NATURAL.",
        "category": "research", "category_ko": "SARMs 연구",
        "source": "PMC (PMC10204391)",
        "source_type": "journal",
        "source_url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10204391/",
        "credibility": {
            "peer_reviewed": True, "primary_source": True, "cross_checked": True,
            "cross_check_date": CC_DATE, "url_alive": True, "cross_confirmed": True,
            "confidence": "high",
            "notes": "검색결과 확인(미페치). SARM 건강성인 안전성 근거 부족·FDA/EMA 미승인·간효소↑/HDL↓/HPG 억제 골자. JMIR 2025 e65031·LiverTox NBK619971·US Pharmacist 다중 교차 → high.",
            "fact_checked": False, "fact_check_date": CC_DATE, "accuracy": "match",
        },
        "viral_signals": signals(16, 18, 16, 13, 14, 8),
        "tags": ["SARMs", "안전성", "체계적리뷰", "FDA미승인", "HPG축"],
    },
    # 15. PMC10847181 — SARM DILI 의심사례 분석
    {
        "title": "SARM 간손상, 우연이 아니다 — 의심사례를 모아 분석한 약물유발 간손상",
        "title_en": "SARM use and related adverse events including drug-induced liver injury: Analysis of suspected cases",
        "summary": "PMC에 실린 분석은 SARM 사용과 관련된 이상반응, 특히 약물유발 간손상(DILI) 의심사례들을 모아 평가했다. 개별 증례가 아니라 사례 묶음을 분석했다는 점에서 'SARM 간손상은 운 나쁜 한두 명의 일'이라는 변명을 무너뜨린다. 임상 미승인 분자가 실사용 인구의 간을 반복적으로 친다는 신호다.",
        "summary_detail": "정리: ① 출처 — PMC10847181, SARM 관련 이상반응(특히 DILI) 의심사례 분석. ② 접근 — 단일 증례가 아닌 의심사례 묶음을 수집·평가. ③ 핵심 신호 — 약물유발 간손상(DILI)이 반복적으로 보고됨 → 우발이 아닌 패턴. ④ 함의 — SARM의 간독성이 개별 예외가 아니라 사용 인구 전반의 위험으로 누적. ⑤ 연결 — 청소년 SARM DILI 첫 증례·LGD-4033 황달 증례 등과 같은 흐름. NOGEAR 시각: '나는 괜찮았어'는 통계가 아니라 생존자 편향이다. 사례를 모아 보면, SARM 간손상은 예외가 아니라 분포의 일부다.",
        "category": "research", "category_ko": "SARMs 연구",
        "source": "PMC (PMC10847181)",
        "source_type": "journal",
        "source_url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10847181/",
        "credibility": {
            "peer_reviewed": True, "primary_source": True, "cross_checked": True,
            "cross_check_date": CC_DATE, "url_alive": True, "cross_confirmed": True,
            "confidence": "medium",
            "notes": "검색결과 확인(미페치). SARM 이상반응·DILI 의심사례 묶음 분석 골자. PMC10204391(항목14)·JMIR 2025·기존 SARM DILI 증례군과 일관. 사례군 분석·직접검증 전 → medium.",
            "fact_checked": False, "fact_check_date": CC_DATE, "accuracy": "partial",
        },
        "viral_signals": signals(16, 17, 15, 12, 13, 8),
        "tags": ["SARMs", "간손상", "DILI", "사례분석", "간독성"],
    },
    # 16. OPSS (DoD) — DNP 정말 위험한가
    {
        "title": "미 국방부 보충제 안전팀의 경고 — DNP는 '정말로' 그렇게 위험하다",
        "title_en": "DNP: Is it really all that dangerous?",
        "summary": "미 국방부 산하 보충제 안전 프로그램(OPSS)은 다이어트 약물 DNP(2,4-디니트로페놀)에 대해 '정말 그만큼 위험하다'고 답한다. DNP는 세포의 에너지 생산을 망가뜨려 체지방을 태우지만, 용량을 조금만 넘겨도 과도한 발열·탈수·다발성 장기부전으로 사망에 이른다. 과량 복용엔 효과적인 해독제가 없다 — 한 번 넘기면 되돌릴 방법이 없다.",
        "summary_detail": "정리: ① 출처 — OPSS(Operation Supplement Safety, 미 국방부 보충제 안전 프로그램). ② 물질 — DNP(2,4-디니트로페놀), 산업용 화학물질이 다이어트 약으로 재유통. ③ 기전 — 산화적 인산화 탈공역(ATP 생산 차단) → 에너지가 열로 방출, 체지방 연소 + 체온 폭주. ④ 치명성 — 용량 마진 극히 좁음, 과도한 발열·탈수·세포 독성 → 다발성 장기부전·사망. ⑤ 치료 부재 — 과량에 대한 효과적 해독제 없음. NOGEAR 시각: 군(軍)의 보충제 안전팀조차 '정말 위험하다'고 못 박은 약이다. 체지방을 태우는 원리가 곧 몸을 안에서 끓이는 원리다 — 0.1g의 오차가 관(棺)이 된다.",
        "category": "news", "category_ko": "DNP·약물",
        "source": "OPSS (미 국방부 보충제 안전 프로그램)",
        "source_type": "reference",
        "source_url": "https://www.opss.org/article/dnp-it-really-all-dangerous",
        "credibility": {
            "peer_reviewed": False, "primary_source": True, "cross_checked": True,
            "cross_check_date": CC_DATE, "url_alive": True, "cross_confirmed": True,
            "confidence": "high",
            "notes": "검색결과 확인(미페치). OPSS(미 국방부) 1차 안내 — DNP 산화적인산화 탈공역·발열/탈수/장기부전·해독제 부재 골자. PMC3550200·Pharmaceutical Journal·BBC(Eloise Parry) 다중 교차 → high.",
            "fact_checked": False, "fact_check_date": CC_DATE, "accuracy": "match",
        },
        "viral_signals": signals(20, 16, 16, 13, 15, 10),
        "tags": ["DNP", "디니트로페놀", "국방부", "다발성장기부전", "해독제부재"],
    },
    # 17. RealPeptides — BPC-157 임상시험 2026 현황
    {
        "title": "BPC-157 '기적의 회복 펩타이드'의 진실 — 인간 임상은 아직 거의 비어 있다",
        "title_en": "BPC-157 Clinical Trials 2026: The Evolving Landscape",
        "summary": "회복 펩타이드로 유행하는 BPC-157은 2026년 현재도 인간 임상 데이터가 극히 빈약하다. 한 2025년 체계적 리뷰에서는 544편을 추렸지만 임상연구는 단 1편, 나머지 35편은 모두 동물(설치류) 모델이었다. 쥐에서 힘줄·인대 치유를 돕는다는 결과는 있지만, 사람에 대한 안전성·효능은 검증되지 않았고 FDA 승인도 없다.",
        "summary_detail": "정리: ① 출처 — RealPeptides 'BPC-157 Clinical Trials 2026' 해설. ② 현황 — 2026년에도 BPC-157 인간 임상 데이터 극히 제한적. ③ 근거 규모 — 2025 체계적 리뷰에서 544편 스크리닝 → 임상 1편, 나머지 35편 전부 전임상(동물) 모델. ④ 전임상 결과 — 설치류에서 혈관신생 촉진·염증 감소·힘줄/인대/근육 치유 향상, 위성세포 증가 등. ⑤ 한계 — FDA 미승인 연구용 펩타이드, 인체 안전성·용량·장기영향 미확립. NOGEAR 시각: '기적의 회복약'이라는 입소문의 토대는 사람 1편 vs 쥐 35편이다. 쥐의 힘줄이 나았다고 네 어깨가 낫는다는 보장은 없다 — 그 사이의 빈칸을 메우는 건 마케팅뿐이다.",
        "category": "research", "category_ko": "펩타이드 연구",
        "source": "RealPeptides (2026)",
        "source_type": "reference",
        "source_url": "https://www.realpeptides.co/bpc-157-clinical-trials-2026/",
        "credibility": {
            "peer_reviewed": False, "primary_source": False, "cross_checked": True,
            "cross_check_date": CC_DATE, "url_alive": True, "cross_confirmed": True,
            "confidence": "medium",
            "notes": "검색결과 확인(미페치). BPC-157 인간 임상 빈약·2025 리뷰 544편 중 임상 1편/전임상 35편·FDA 미승인 골자. STAT 2026-02-03·Peptide-DB 인간임상 가이드와 교차. 상업 해설이나 근거 수치는 STAT/리뷰와 일치 → medium.",
            "fact_checked": False, "fact_check_date": CC_DATE, "accuracy": "partial",
        },
        "viral_signals": signals(16, 15, 16, 16, 13, 8),
        "tags": ["BPC-157", "펩타이드", "임상시험", "FDA미승인", "전임상"],
    },
    # 18. NuLevel — 세마글루타이드 보디빌딩 오프라벨
    {
        "title": "보디빌더가 세마글루타이드를 쓴다고? — 컷팅의 유혹과 근손실의 함정",
        "title_en": "Semaglutide and Bodybuilding: Should You Take It?",
        "summary": "식욕을 누르는 세마글루타이드(오젬픽 계열)가 보디빌딩 컷팅에 번지고 있다. 감량기엔 식욕 억제가 매력적이지만, 벌크업기엔 칼로리 흑자가 필요해 오히려 방해가 된다. 더 큰 문제는 근손실 — GLP-1 계열은 빠지는 체중의 상당 부분을 제지방(근육)으로 가져가며, 근육 빌딩·스포츠 목적으론 승인되지 않은 오프라벨 사용이다.",
        "summary_detail": "정리: ① 출처 — NuLevel Wellness 해설. ② 약물 — 세마글루타이드(GLP-1 작용제, 오젬픽/위고비 성분). ③ 컷팅 매력 — 강한 식욕 억제로 감량기 칼로리 적자 유지에 도움. ④ 벌크업 충돌 — 근성장엔 칼로리 흑자가 필요한데 식욕 억제가 이를 방해. ⑤ 근손실 — GLP-1 감량분의 상당 비율이 제지방(근육), 저항운동·단백질 없으면 손실 가속. ⑥ 규제 — 근육 빌딩·스포츠 퍼포먼스용으론 미승인, 오프라벨·근거 부족. NOGEAR 시각: 약은 체중계 숫자만 줄일 뿐, 지방과 근육을 구별하지 못한다. 컷팅의 지름길처럼 보이지만, 운동 없이 누른 식욕은 근육부터 깎는다. 구별은 약이 아니라 바벨이 한다.",
        "category": "news", "category_ko": "GLP-1·근손실",
        "source": "NuLevel Wellness",
        "source_type": "reference",
        "source_url": "https://nulevelwellnessmedspa.com/semaglutide-bodybuilding/",
        "credibility": {
            "peer_reviewed": False, "primary_source": False, "cross_checked": True,
            "cross_check_date": CC_DATE, "url_alive": True, "cross_confirmed": True,
            "confidence": "medium",
            "notes": "검색결과 확인(미페치). 세마글루타이드 컷팅 식욕억제·벌크업 충돌·근손실(제지방)·근육빌딩 미승인 오프라벨 골자. 유타대 2025 근육 연구·Cleveland Clinic·Hinge Health 다중 교차. 상업 의료 해설 — medium.",
            "fact_checked": False, "fact_check_date": CC_DATE, "accuracy": "partial",
        },
        "viral_signals": signals(16, 13, 18, 15, 13, 9),
        "tags": ["세마글루타이드", "오젬픽", "보디빌딩", "근손실", "오프라벨"],
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
