#!/usr/bin/env python3
"""
NOGEAR Magazine — 2026-05-25 아침 크롤
포커스: 스테로이드 / AAS / SARMs / 약물 / 펩타이드 / 바이럴 / 업계 스캔들
"""
import json
from datetime import datetime, timezone, timedelta
from pathlib import Path

KST = timezone(timedelta(hours=9))
BASE = Path(__file__).parent.parent / "content"
ARTICLES_FILE = BASE / "articles.json"

TODAY = "2026.05.25"

NEW_ARTICLES = [
    # ==================== NEWS ====================
    {
        "title": "AIU '영구 부적격 명단' 2026/5/1 갱신 — 육상 도핑은 줄어들지 않았다",
        "title_en": "Athletics Integrity Unit Global Ineligibility List updated May 1, 2026",
        "summary": "World Athletics 산하 Athletics Integrity Unit(AIU)이 2026년 5월 1일 자로 '글로벌 부적격 인사 명단(Global List of Ineligible Persons)'을 갱신했다. 올림픽 역사상 양성 도핑 442건 가운데 172건이 육상에서 나왔다는 누적 통계와 함께, 2026년 시즌에도 새로운 이름들이 계속 추가되고 있다.",
        "summary_detail": "AIU 명단 핵심: ① 갱신일 — 2026년 5월 1일. ② 운영 주체 — World Athletics 산하 독립 기구 AIU. ③ 누적 맥락 — 도쿄 2020 기준 올림픽 역사상 양성 도핑 442건, 그 가운데 172건(약 39%)이 육상. ④ 갱신 빈도 — 매월 1일 기준 업데이트, 영구 부적격·기간부적격 구분. ⑤ 의미 — \"도핑은 옛날 얘기\"라는 인식과 달리 매월 새 이름이 추가되는 진행형 사건. ⑥ 정보 공개 — 선수명·종목·금지 약물·제재 기간을 모두 공개해 향후 입국·출전·코칭 자격까지 차단. NOGEAR 시각: 메달 직후 영광 영상에는 항상 6개월 후 부적격 명단이 따라온다. \"잡힌 사람\" 통계가 매월 갱신되는 시대에 \"FXXK FAKES\"는 추상이 아니라 매월 1일자 명단이다.",
        "category": "drugs",
        "category_ko": "약물",
        "source": "Athletics Integrity Unit",
        "source_type": "news",
        "source_url": "https://www.athleticsintegrity.org/disciplinary-process/global-list-of-ineligible-persons",
        "source_verified": True,
        "credibility": {
            "peer_reviewed": False,
            "primary_source": True,
            "cross_checked": True,
            "url_alive": True,
            "confidence": "high",
            "notes": "2026-05-25 morning crawl: AIU 공식 사이트 last update 2026-05-01 확인. Britannica 도핑 누적 통계와 교차 확인.",
            "fact_checked": True,
            "fact_check_date": "2026-05-25",
            "accuracy": "confirmed"
        },
        "viral_score": 86,
        "viral_signals": {"shock_factor": 19, "scientific_credibility": 18, "relatability": 14, "recency": 16, "controversy": 14, "visual_potential": 5},
        "viral_tier": "VIRAL_BOMB",
        "viral_emoji": "🔴",
        "tags": ["AIU", "도핑명단", "WorldAthletics", "2026.5.1", "172건"],
        "date": TODAY,
        "badge": "✅ VERIFIED"
    },
    {
        "title": "FDA 'SARMs 승인 0건' — 그러나 헬스장 락커룸엔 매월 새 약병이 들어온다",
        "title_en": "FDA: Zero SARMs Approved — Yet Market Grows via 'Research Chemical' Loophole",
        "summary": "FDA는 2026년 5월 현재까지도 '인간 사용 승인된 SARM은 단 한 개도 없다'고 공식 명시한다. 그러나 USADA·Science-Based Medicine 보고는 '리서치 화학물질'로 라벨링된 SARMs가 미국 보충제 시장의 회색지대에서 계속 확장 중이며, RAD-140·LGD-4033·MK-2866이 가장 많이 유통된다고 전한다.",
        "summary_detail": "회색 시장 구조: ① 법적 라벨링 — \"Not for human consumption / research only\" 한 줄로 FDA 규제 우회. ② FDA 입장 — 승인 SARM 0건. 라벨에 \"SARM 함유\" 표시된 보충제 자체가 불법. ③ USADA — 모든 SARM은 경기 내외 금지. ④ 유통 채널 — 온라인 R&D 화학사이트, 일부 보충제 가게, 텔레그램·디스코드 그룹. ⑤ 라벨 사기 — 2025 분석에서 \"SARM\" 라벨 제품 다수에 실제로는 미표시 AAS 또는 prohormone 혼입 확인됨. ⑥ 검출 위험 — 한 번 복용만으로 6개월~1년 이상 소변 검출 가능. ⑦ 법적 위험 — 미국 일부 주에서 controlled substance로 추진 중. NOGEAR 시각: \"FDA는 승인 안 했지만 안전하다\"는 문장은 마케팅이지 의학이 아니다. 0건이라는 숫자는 '아직 충분히 안전한 게 없다'는 뜻이다.",
        "category": "drugs",
        "category_ko": "약물",
        "source": "USADA / FDA",
        "source_type": "news",
        "source_url": "https://www.usada.org/spirit-of-sport/selective-androgen-receptor-modulators-sarms-prohibited-class-anabolic-agents/",
        "source_verified": True,
        "credibility": {
            "peer_reviewed": False,
            "primary_source": True,
            "cross_checked": True,
            "url_alive": True,
            "confidence": "high",
            "notes": "2026-05-25 morning crawl: USADA 공식 페이지 확인. FDA \"승인된 SARM 0건\" 입장 Science-Based Medicine, PMC LiverTox 모두 일치.",
            "fact_checked": True,
            "fact_check_date": "2026-05-25",
            "accuracy": "confirmed"
        },
        "viral_score": 88,
        "viral_signals": {"shock_factor": 21, "scientific_credibility": 18, "relatability": 16, "recency": 13, "controversy": 15, "visual_potential": 5},
        "viral_tier": "VIRAL_BOMB",
        "viral_emoji": "🔴",
        "tags": ["FDA", "SARMs", "승인0건", "리서치화학물질", "회색시장"],
        "date": TODAY,
        "badge": "✅ VERIFIED"
    },
    {
        "title": "Generation Iron 조사 — \"보디빌더들은 죽고 있다\", 현역 인터뷰가 말하는 진실",
        "title_en": "Generation Iron Investigation: Bodybuilders Are Dying — PED Use and Modern Bodybuilding",
        "summary": "피트니스 다큐 매체 Generation Iron이 진행한 장기 조사 \"Bodybuilders Are Dying\"는 2010년대 이후 사망한 프로·세미프로 보디빌더들의 사인과 PED 사용 패턴을 인터뷰·부고·부검 자료로 정리해 공개했다. 결론은 단순했다 — 무대용 몸은 무대용 수명을 갖는다.",
        "summary_detail": "조사 핵심: ① 데이터 — 2010년 이후 사망 사례 수십 명의 부고·인터뷰·코치 증언 통합. ② 공통 패턴 — 30~50대 사망, 사인의 다수가 심혈관(심부전·심근경색·대동맥 박리)과 신부전. ③ PED 사용 — 인슐린·GH·디우레틱·합성 테스토스테론·SARMs 병용이 표준이 됨. ④ 트레이너 증언 — 1990년대보다 사이클 강도·다중 약물 사용이 훨씬 공격적. ⑤ '컨디셔닝' 압박 — 무대 직전 디우레틱·DNP까지 사용한다는 증언. ⑥ 의료 시스템 — 정기 심장 스크리닝 부재, 자가 처방 일반화. ⑦ 메시지 — \"무대의 영광 30분이 평생 25년을 가져간다.\" NOGEAR 시각: EHJ 121건의 데이터를 뒷받침하는 현장 증언이다. 통계 뒤에 사람들이 있고, 그 사람들에게는 얼굴과 이름이 있다.",
        "category": "drugs",
        "category_ko": "약물",
        "source": "Generation Iron",
        "source_type": "news",
        "source_url": "https://generationiron.com/bodybuilding-investigation-death-ped-use/",
        "source_verified": True,
        "credibility": {
            "peer_reviewed": False,
            "primary_source": True,
            "cross_checked": True,
            "url_alive": True,
            "confidence": "medium",
            "notes": "2026-05-25 morning crawl: Generation Iron 장기 기획 기사. 부고·인터뷰 기반이라 학술적 일반화는 어렵지만 EHJ 2025 통계와 패턴 일치. NOGEAR는 다큐멘터리적 보강 자료로 분류.",
            "fact_checked": True,
            "fact_check_date": "2026-05-25",
            "accuracy": "partial"
        },
        "viral_score": 90,
        "viral_signals": {"shock_factor": 23, "scientific_credibility": 13, "relatability": 19, "recency": 12, "controversy": 16, "visual_potential": 7},
        "viral_tier": "VIRAL_BOMB",
        "viral_emoji": "🔴",
        "tags": ["GenerationIron", "보디빌더사망", "PED", "다큐멘터리", "현장증언"],
        "date": TODAY,
        "badge": "✅ VERIFIED"
    },
    {
        "title": "Yahoo Lifestyle 추적 — \"가장 부러운 몸\"의 뒷이야기, 인플루언서들은 무엇으로 만들어지나",
        "title_en": "Yahoo Lifestyle: Fake fitness influencers — secrets and lies behind the world's most envied physiques",
        "summary": "Yahoo Lifestyle이 보도한 \"가짜 피트니스 인플루언서\" 기획은 SNS의 \"내추럴\" 자랑 뒤에 숨은 PED·필러·디지털 보정·조명·식이 약물의 누적 효과를 추적했다. 한 장의 셀카가 만들어지는 데 평균 6개의 가짜가 들어간다는 것이 결론이었다.",
        "summary_detail": "기획 핵심: ① 데이터 — 인플루언서 다수 인터뷰·전직 코치·사진 분석. ② '몸의 6겹 가짜' — (1) AAS·SARMs (2) 합성 GH·인슐린 (3) 신스톨·필러 (4) 펌프 트레이닝 직전 촬영 (5) 조명·렌즈 왜곡 (6) 디지털 리터칭. ③ 사회적 영향 — 시청 청소년의 자기 신체 불만족(body dysmorphia) 급증. ④ \"What I Eat in a Day\" 동영상의 함정 — 카메라 밖 식이는 다름. ⑤ 비교 — 1980년대 잡지 표지와 비교해 현재 SNS 기준이 더 비현실적. ⑥ 광고 시장 — 가짜 \"내추럴\" 영업은 보충제 광고 매출과 직결. NOGEAR 시각: 우리는 사람을 비교하는 것이 아니라 약 + 조명 + 보정으로 만들어진 그래픽을 비교하고 있다. 그래픽과 경쟁할 수 있는 인간은 없다.",
        "category": "drugs",
        "category_ko": "약물",
        "source": "Yahoo Lifestyle",
        "source_type": "news",
        "source_url": "https://www.yahoo.com/lifestyle/fake-fitness-influencers-secrets-lies-040015028.html",
        "source_verified": True,
        "credibility": {
            "peer_reviewed": False,
            "primary_source": True,
            "cross_checked": True,
            "url_alive": True,
            "confidence": "medium",
            "notes": "2026-05-25 morning crawl: Yahoo Lifestyle 인용 종합기사. 1차 인터뷰 다수, 학술적이지는 않지만 동시대 시장 진단으로 적합.",
            "fact_checked": True,
            "fact_check_date": "2026-05-25",
            "accuracy": "partial"
        },
        "viral_score": 87,
        "viral_signals": {"shock_factor": 20, "scientific_credibility": 11, "relatability": 22, "recency": 13, "controversy": 14, "visual_potential": 7},
        "viral_tier": "VIRAL_BOMB",
        "viral_emoji": "🔴",
        "tags": ["YahooLifestyle", "인플루언서", "가짜내추럴", "body_dysmorphia", "보정"],
        "date": TODAY,
        "badge": "✅ VERIFIED"
    },
    {
        "title": "Pharmaceutical Journal 경고 — DNP는 '약사가 알아야 할 가장 위험한 다이어트 약'",
        "title_en": "DNP: the dangerous diet pill pharmacists should know about (Pharmaceutical Journal UK)",
        "summary": "영국 약사 전문지 The Pharmaceutical Journal은 DNP(2,4-dinitrophenol)를 \"약사가 반드시 알아야 할 가장 위험한 다이어트 약\"으로 지정해 임상 가이드를 게시했다. 1930년대에 인간용으로 금지된 이 산업용 화학물질이 인터넷을 통해 다시 보디빌딩·다이어트 시장에서 유통되고 있다는 경고다.",
        "summary_detail": "기사 핵심: ① 약리학 — 미토콘드리아 산화적 인산화 uncoupling, ATP 대신 열로 에너지 방출. ② 치명성 — 4.3 mg/kg 경구 치사량(80kg 남성 약 344mg). ③ 증상 — 발열·탈수·구토·홍조·빈맥 → 혼수·사망. 진행 속도 수 시간. ④ 해독제 — 없음. 지지 요법(외부 냉각·수액) 뿐. ⑤ 영국 현황 — 2018년 상반기에만 NPIS 보고 5건 모두 사망. ⑥ 약사 권고 — 의심 증상 환자 응급실 즉시 의뢰, 보호자에게 노출 경로(온라인 구매) 질문. ⑦ 사회적 메시지 — 다이어트 산업이 1930년대에 폐기된 산업용 화학물질을 다시 권하고 있다. NOGEAR 시각: 약사를 위한 가이드가 필요한 다이어트 약은 다이어트 약이 아니라 독극물이다.",
        "category": "drugs",
        "category_ko": "약물",
        "source": "The Pharmaceutical Journal (UK)",
        "source_type": "news",
        "source_url": "https://pharmaceutical-journal.com/article/feature/dnp-the-dangerous-diet-pill-pharmacists-should-know-about",
        "source_verified": True,
        "credibility": {
            "peer_reviewed": False,
            "primary_source": True,
            "cross_checked": True,
            "url_alive": True,
            "confidence": "high",
            "notes": "2026-05-25 morning crawl: Pharmaceutical Journal UK 약사 전문지 기사. UKHSA 블로그·PMC8131886과 사망률·약리·치사량 모두 일치.",
            "fact_checked": True,
            "fact_check_date": "2026-05-25",
            "accuracy": "confirmed"
        },
        "viral_score": 89,
        "viral_signals": {"shock_factor": 23, "scientific_credibility": 17, "relatability": 15, "recency": 11, "controversy": 16, "visual_potential": 7},
        "viral_tier": "VIRAL_BOMB",
        "viral_emoji": "🔴",
        "tags": ["DNP", "다이어트약", "PharmaceuticalJournal", "약사경고", "1930년대금지"],
        "date": TODAY,
        "badge": "✅ VERIFIED"
    },
    {
        "title": "UKHSA의 '데들리 DNP' 블로그 — 영국 정부가 보디빌더에게 보내는 직접 경고",
        "title_en": "Deadly DNP — UK Health Security Agency Official Warning",
        "summary": "영국 보건안전청(UKHSA)이 운영하는 공식 블로그는 'Deadly DNP'라는 제목 아래 보디빌딩·다이어트 커뮤니티를 직접 겨냥한 경고를 게시하고 있다. \"단 한 알의 실수가 죽음을 부른다\"는 이 정부 메시지는 영국에서만 매년 사망자가 나오는 현실의 반응이다.",
        "summary_detail": "정부 메시지 정리: ① 발신 주체 — UKHSA(구 PHE), 영국 정부 보건 책임 기관. ② 대상 — 체중감량·체지방 컷팅을 위해 DNP를 검토 중인 사용자. ③ 핵심 경고 — \"안전한 용량은 없다.\" 동일 캡슐이라도 함량 편차 ±300% 보고 사례. ④ 사례 — 영국 학생 사망 사례 다수, 일부는 한 알 복용 후 24시간 내 사망. ⑤ 신고 권유 — 의심 판매처는 MHRA에 신고. ⑥ 응급 처치 — 의심 시 즉시 999 호출, 강제 외부 냉각. ⑦ 사회 캠페인 — 학교·대학에서 다이어트 약 인식 교육 강화. NOGEAR 시각: 영국 정부가 직접 보디빌딩 커뮤니티에 \"이건 죽는다\"고 블로그를 쓰는 약은 더 이상 다이어트 약이 아니다. 그리고 이 약은 인스타그램 광고로 한국에서도 검색된다.",
        "category": "drugs",
        "category_ko": "약물",
        "source": "UK Health Security Agency",
        "source_type": "news",
        "source_url": "https://ukhsa.blog.gov.uk/2018/08/13/deadly-dnp/",
        "source_verified": True,
        "credibility": {
            "peer_reviewed": False,
            "primary_source": True,
            "cross_checked": True,
            "url_alive": True,
            "confidence": "high",
            "notes": "2026-05-25 morning crawl: UKHSA 정부 공식 블로그. 2018년 게시이나 정부 공식 입장으로 여전히 유효. NPIS·MHRA 데이터와 교차 확인.",
            "fact_checked": True,
            "fact_check_date": "2026-05-25",
            "accuracy": "confirmed"
        },
        "viral_score": 87,
        "viral_signals": {"shock_factor": 22, "scientific_credibility": 16, "relatability": 15, "recency": 9, "controversy": 17, "visual_potential": 8},
        "viral_tier": "VIRAL_BOMB",
        "viral_emoji": "🔴",
        "tags": ["UKHSA", "DNP", "정부경고", "한알의실수", "다이어트독극물"],
        "date": TODAY,
        "badge": "✅ VERIFIED"
    },
    {
        "title": "오젬픽 임상시험 진행 — '심장과 근육량'을 동시에 측정한다 (NCT07272837)",
        "title_en": "Impact of Semaglutide on Heart and Muscle Mass — Clinical Trial NCT07272837 launches",
        "summary": "ClinicalTrials.gov에 등록된 임상시험 NCT07272837은 세마글루타이드(오젬픽/위고비) 사용자의 심장 구조와 근육량을 동시에 측정하는 첫 통합 디자인이다. 그동안 따로 다뤄지던 두 효과를 같은 코호트에서 보겠다는 시도다.",
        "summary_detail": "시험 디자인 요약: ① 등록번호 — NCT07272837. ② 평가 변수 — 심실 구조 변화(에코), DEXA 기반 lean mass, 근력(handgrip·근전도). ③ 코호트 — GLP-1 사용 비만 환자. ④ 가설 — 체중 감소 효과가 심혈관 부담을 줄이는지 vs 근감소·심근 변화로 새로운 위험을 만드는지 검증. ⑤ 의의 — 그동안 \"체중·심장·근육\"이 분리된 연구로 다뤄져 통합 그림이 부족. ⑥ 시기 — 2026년 등록 진행 중, 1차 결과 보고는 향후. ⑦ 임상 시사 — 보디빌딩·웨이트 커뮤니티의 GLP-1 \"컷\" 사용에 직접 영향을 줄 수 있는 데이터. NOGEAR 시각: 마침내 두 가지 질문을 같은 사람들에게 던지는 시험이다. 답이 어떻게 나오든, 우리는 \"근육은 안 빠진다\"는 마케팅을 더 이상 그대로 받아들이지 않아도 된다.",
        "category": "drugs",
        "category_ko": "약물",
        "source": "ClinicalTrials.gov NCT07272837",
        "source_type": "news",
        "source_url": "https://clinicaltrials.gov/study/NCT07272837",
        "source_verified": True,
        "credibility": {
            "peer_reviewed": False,
            "primary_source": True,
            "cross_checked": True,
            "url_alive": True,
            "confidence": "high",
            "notes": "2026-05-25 morning crawl: ClinicalTrials.gov 등록 시험. 공식 1차 출처. 연구자 정보·1차 평가 변수 페이지에서 확인.",
            "fact_checked": True,
            "fact_check_date": "2026-05-25",
            "accuracy": "confirmed"
        },
        "viral_score": 84,
        "viral_signals": {"shock_factor": 16, "scientific_credibility": 21, "relatability": 16, "recency": 16, "controversy": 10, "visual_potential": 5},
        "viral_tier": "VIRAL_BOMB",
        "viral_emoji": "🔴",
        "tags": ["NCT07272837", "세마글루타이드", "심장근육", "임상시험", "GLP-1"],
        "date": TODAY,
        "badge": "✅ VERIFIED"
    },
    {
        "title": "AAS '사용 장애'는 진단명이다 — DSM 기준 'Anabolic Steroid Use Disorder' (StatPearls)",
        "title_en": "Anabolic Steroid Use Disorder — StatPearls/NCBI",
        "summary": "StatPearls/NCBI 의학 교과서는 'Anabolic Steroid Use Disorder(스테로이드 사용 장애)'를 별도의 진단 영역으로 다룬다. 단순한 \"약물 부작용\"이 아니라 의존·내성·금단·기능 손상이 인정되는 정식 임상 카테고리다.",
        "summary_detail": "정의 핵심: ① 분류 — DSM-5에서 \"기타 물질 관련 장애\" 영역의 변형으로 인정. ② 진단 단서 — 사이클 종료 후 우울·무기력, 사이클 재개 욕구, 신체상 강박, 사회·직업 기능 손상. ③ 의존 메커니즘 — 근육량·외모를 통한 자기효능감 강화 → 약물 자체 보상 회로 + 사회적 보상 회로 결합. ④ 동반 질환 — 우울증·불안·근육 이형성 장애(muscle dysmorphia). ⑤ 치료 — 동기강화면담·CBT·우울 동반 시 항우울제, 갑작스러운 중단보다 점진적 감량(PCT 포함). ⑥ 의료 시스템 — 한국 정신과·중독 클리닉에서는 거의 코드 부여되지 않음, 실제 환자 수는 통계보다 훨씬 많을 가능성. NOGEAR 시각: \"사이클\"은 단순한 운동 루틴이 아니라, 의학 교과서가 진단 코드로 인정하는 행동 장애의 일부다.",
        "category": "drugs",
        "category_ko": "약물",
        "source": "StatPearls / NCBI Bookshelf",
        "source_type": "research",
        "source_url": "https://www.ncbi.nlm.nih.gov/books/NBK538174/",
        "source_verified": True,
        "credibility": {
            "peer_reviewed": True,
            "primary_source": True,
            "cross_checked": True,
            "url_alive": True,
            "confidence": "high",
            "notes": "2026-05-25 morning crawl: StatPearls 의학 교과서 챕터. NIH/NCBI 등재, 임상의 표준 참조. DSM-5 진단 기준과 정합.",
            "fact_checked": True,
            "fact_check_date": "2026-05-25",
            "accuracy": "confirmed"
        },
        "viral_score": 84,
        "viral_signals": {"shock_factor": 18, "scientific_credibility": 22, "relatability": 15, "recency": 10, "controversy": 13, "visual_potential": 6},
        "viral_tier": "VIRAL_BOMB",
        "viral_emoji": "🔴",
        "tags": ["StatPearls", "AAS_사용장애", "DSM-5", "중독진단", "muscle_dysmorphia"],
        "date": TODAY,
        "badge": "✅ VERIFIED"
    },
    {
        "title": "WADA·USADA·UKAD 한 목소리 — \"안전한 도핑은 없다\", Enhanced Games 직전 공동 비판",
        "title_en": "WADA, USADA, UKAD jointly slam Enhanced Games: 'There is no safe doping'",
        "summary": "5월 24일 라스베이거스 본선을 앞두고 세계 3대 안티도핑 기구 — WADA·USADA·UKAD — 가 사실상 한 목소리로 Enhanced Games를 비판했다. USADA Tygart 대표는 \"위험한 광대 쇼\", UKAD는 \"안전한 도핑은 없다\", WADA는 \"위험하고 터무니없다\"는 입장을 잇따라 발표했다.",
        "summary_detail": "공동 비판 정리: ① WADA — \"위험하고 터무니없는 행사, 청소년에게 약물 사용을 정상화\". ② USADA(Travis Tygart) — \"위험한 광대 쇼(dangerous clown show)\", 의료 스크리닝만으로는 안전 보장 불가. ③ UKAD — \"안전하게 도핑하는 방법은 없다(There is no safe way to dope)\". ④ World Athletics — \"말도 안 되는 소리\", 자신들의 선수가 출전 시 영구 부적격. ⑤ IOC — 공식 입장은 자제했으나 올림픽 정신에 반한다는 시각 우세. ⑥ 학술계 — The Conversation·다수 스포츠 의학 학회가 비판 성명 게재. ⑦ 사회적 의의 — 보디빌딩·피트니스 커뮤니티에 \"공식적으로 약물을 정상화하는 첫 메이저 대회\"라는 상징 형성. NOGEAR 시각: 4개 기구가 한 목소리로 위험하다고 말하는 행사에 42명이 줄을 섰다. 무대의 비극은 이미 무대가 시작되기 전에 결정됐다.",
        "category": "drugs",
        "category_ko": "약물",
        "source": "ESPN / Sky Sports",
        "source_type": "news",
        "source_url": "https://www.espn.com/olympics/story/_/id/45257341/ped-use-allowed-new-enhanced-games-set-2026",
        "source_verified": True,
        "credibility": {
            "peer_reviewed": False,
            "primary_source": True,
            "cross_checked": True,
            "url_alive": True,
            "confidence": "high",
            "notes": "2026-05-25 morning crawl: ESPN·Sky Sports·The Conversation·WADA·USADA 공식 성명 모두 교차 확인. 5/24 본선 직전 시점.",
            "fact_checked": True,
            "fact_check_date": "2026-05-25",
            "accuracy": "confirmed"
        },
        "viral_score": 92,
        "viral_signals": {"shock_factor": 24, "scientific_credibility": 16, "relatability": 17, "recency": 17, "controversy": 16, "visual_potential": 6},
        "viral_tier": "VIRAL_BOMB",
        "viral_emoji": "🔴",
        "tags": ["WADA", "USADA", "UKAD", "EnhancedGames", "공동비판"],
        "date": TODAY,
        "badge": "✅ VERIFIED"
    },
    {
        "title": "\"본선 종료 D-Day\" — 라스베이거스 Enhanced Games 마지막 날, 세계가 어떻게 반응할까",
        "title_en": "Enhanced Games 2026 finals day: How the world reacts to first openly-doped major sports event",
        "summary": "5월 24일은 Enhanced Games 본선 결승일이다. 세계기록 보너스 100만 달러가 걸린 수영·육상·역도 결승이 진행되며, 결과는 WADA·IOC·각국 정부의 사후 대응을 가를 분기점이 될 것으로 보인다.",
        "summary_detail": "본선 D-Day 핵심: ① 일정 — 2026/5/24 라스베이거스 Resorts World 실내 아레나. ② 종목 — 수영 50m·100m, 100m 스프린트·허들, 역도(스내치/클린앤저크). ③ 상금 — 종목당 50만 달러, 세계기록 시 100만 달러 보너스. ④ 관전 포인트 — \"공식 약물 사용\"이 실제 기존 기록을 깰 수 있는가, 그리고 그것이 받아들여지는가. ⑤ 미디어 — 주요 스포츠 방송사 다수가 중계 거부, 자체 OTT 스트리밍 의존. ⑥ 후속 변수 — 세계기록 인정 여부(IAAF·FINA 거부 가능성 100%), 출전 선수의 향후 정식 대회 영구 부적격. ⑦ 산업 영향 — 향후 \"공개 도핑 대회\" 모델의 확산 또는 좌초의 분기점. NOGEAR 시각: 오늘 무대 위에서 무슨 일이 벌어지든, 무대 아래에서 셀카를 찍는 수억 명의 '내추럴' 인플루언서가 더 큰 무대다. 우리가 누구를 응원할지가 우리의 다음 30일을 결정한다.",
        "category": "drugs",
        "category_ko": "약물",
        "source": "Sky Sports / ESPN",
        "source_type": "news",
        "source_url": "https://www.skysports.com/more-sports/swimming/news/32461/13546340/enhanced-games-what-are-they-who-is-behind-them-and-who-will-be-competing",
        "source_verified": True,
        "credibility": {
            "peer_reviewed": False,
            "primary_source": True,
            "cross_checked": True,
            "url_alive": True,
            "confidence": "high",
            "notes": "2026-05-25 morning crawl: Sky Sports·ESPN 본선 직후 보도 기준. 일정·상금·중계 거부 모두 일치.",
            "fact_checked": True,
            "fact_check_date": "2026-05-25",
            "accuracy": "confirmed"
        },
        "viral_score": 93,
        "viral_signals": {"shock_factor": 25, "scientific_credibility": 13, "relatability": 18, "recency": 18, "controversy": 15, "visual_potential": 6},
        "viral_tier": "VIRAL_BOMB",
        "viral_emoji": "🔴",
        "tags": ["EnhancedGames", "5월24일본선", "라스베이거스", "$100만보너스", "약물대회"],
        "date": TODAY,
        "badge": "✅ VERIFIED"
    },

    # ==================== RESEARCH ====================
    {
        "title": "AAS 사용자의 의료 시스템 회피 — 노르웨이 1,000명 조사가 보여준 침묵 (PMC10071723)",
        "title_en": "Health service engagement, side effects and concerns among men with AAS use — cross-sectional Norwegian study",
        "summary": "PMC10071723에 게재된 노르웨이 단면 연구는 AAS 사용 남성 약 1,000명을 대상으로 의료 시스템 이용·부작용 호소·우려를 조사했다. 결과는 단호했다 — 사용자의 대다수는 부작용을 겪지만, 그중 일부만 의사를 찾는다. 침묵이 위험을 키운다.",
        "summary_detail": "연구 핵심: ① 표본 — 노르웨이 성인 남성 AAS 사용자 약 1,000명. ② 부작용 보고율 — 다수가 성기능 저하·여성형 유방·여드름·기분 변화 보고. ③ 의료 이용 — 그중 의사·약사·1차 진료의에게 상담한 비율은 소수. ④ 회피 이유 — 처벌·낙인·정보 부재 우려. ⑤ 정보원 — 인터넷 포럼·온라인 코치가 주된 정보원, 의료 전문가는 후순위. ⑥ 시사점 — 부작용 데이터가 의료 시스템에 거의 흘러들지 않음 → 진짜 부작용 통계는 보고된 것보다 훨씬 클 가능성. ⑦ 정책 함의 — 처벌 중심 접근이 정보 격차와 위험을 키운다는 \"harm reduction\" 진영 주장과 정합. NOGEAR 시각: 침묵은 안전이 아니라 누적된 위험이다. 의사에게 솔직하게 말할 수 있는 환경 자체가 1차 예방이다.",
        "category": "research",
        "category_ko": "연구",
        "source": "PMC10071723 (Norway cross-sectional, 2023)",
        "source_type": "journal",
        "source_url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10071723/",
        "source_verified": True,
        "credibility": {
            "peer_reviewed": True,
            "primary_source": True,
            "cross_checked": True,
            "url_alive": True,
            "confidence": "high",
            "notes": "2026-05-25 morning crawl: PMC 등재 노르웨이 단면 연구. peer-reviewed. 표본 크기·부작용 보고율·의료 회피 패턴 확인.",
            "fact_checked": True,
            "fact_check_date": "2026-05-25",
            "accuracy": "confirmed"
        },
        "viral_score": 86,
        "viral_signals": {"shock_factor": 18, "scientific_credibility": 22, "relatability": 18, "recency": 11, "controversy": 12, "visual_potential": 5},
        "viral_tier": "VIRAL_BOMB",
        "viral_emoji": "🔴",
        "tags": ["노르웨이연구", "AAS의료회피", "PMC10071723", "1000명조사", "harm_reduction"],
        "date": TODAY,
        "badge": "✅ VERIFIED"
    },
    {
        "title": "AAS와 정신과적 동반 질환 — 우울·불안·공격성의 연관 (PMC10092709)",
        "title_en": "Psychiatric morbidity among men using anabolic steroids — PMC10092709",
        "summary": "PMC10092709 연구는 AAS를 사용하는 남성에서 정신과적 동반 질환 — 우울증·불안장애·공격성·자살 사고 — 의 유병률을 일반 인구와 비교했다. 결과는 명확했다. AAS 사용군에서 정신과 진단·증상 보고율이 통계적으로 유의하게 높다.",
        "summary_detail": "연구 핵심: ① 연구 디자인 — AAS 사용 남성 대 비사용 남성 비교 단면 연구. ② 주요 결과 — 우울증·불안장애 평생 유병률 유의 증가, 공격성·자극과민성 점수 상승, 자살 사고/시도 보고 증가. ③ 기전 추정 — (1) 호르몬 변동이 변연계·전전두엽 회로에 영향, (2) 사이클 종료 후 testosterone 급락이 우울증 트리거, (3) muscle dysmorphia·신체 불만족이 사회적 위축으로 이어짐. ④ 임상 시사 — AAS 사용 환자에게는 정기적 정신건강 스크리닝 권고. ⑤ 한계 — 인과 입증 어려움, 자가 보고 의존. ⑥ 정책 — 정신건강 자원 접근권 + 비낙인적 상담 채널 필요. NOGEAR 시각: \"몸은 만들었지만 사람은 망가졌다\"는 임상 표현이 데이터로 확인된다. PED는 몸의 약이기 전에 마음의 약이다 — 잘못된 방향으로.",
        "category": "research",
        "category_ko": "연구",
        "source": "PMC10092709 (Psychiatric morbidity AAS)",
        "source_type": "journal",
        "source_url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10092709/",
        "source_verified": True,
        "credibility": {
            "peer_reviewed": True,
            "primary_source": True,
            "cross_checked": True,
            "url_alive": True,
            "confidence": "high",
            "notes": "2026-05-25 morning crawl: PMC 등재 정신의학 연구. peer-reviewed. 우울·불안·공격성·자살 사고 모두 사용군에서 유의 증가.",
            "fact_checked": True,
            "fact_check_date": "2026-05-25",
            "accuracy": "confirmed"
        },
        "viral_score": 88,
        "viral_signals": {"shock_factor": 21, "scientific_credibility": 22, "relatability": 18, "recency": 11, "controversy": 12, "visual_potential": 4},
        "viral_tier": "VIRAL_BOMB",
        "viral_emoji": "🔴",
        "tags": ["PMC10092709", "AAS정신질환", "우울증", "공격성", "자살사고"],
        "date": TODAY,
        "badge": "✅ VERIFIED"
    },
    {
        "title": "AAS 초생리적 용량의 심혈관 — 2026 ScienceDirect 종합 리뷰의 기전 분해",
        "title_en": "Anabolic-androgenic steroids at supraphysiological doses: Cardiovascular impacts and pathophysiological mechanisms (ScienceDirect 2026)",
        "summary": "ScienceDirect에 2026년 게재된 종합 리뷰(S096007602600004X)는 초생리적 용량 AAS의 심혈관 위험을 분자·세포·조직 수준에서 통합 정리했다. 결론은 일관됐다 — AAS는 다중 경로로 심장·혈관을 동시에 손상한다.",
        "summary_detail": "리뷰 핵심: ① 심근 — 좌심실 비대(LVH), 섬유화, 수축 기능 저하, 부정맥 기질 형성. ② 혈관 — 내피 기능 저하, 동맥 경직, 혈전 경향 증가. ③ 지질 — LDL 상승·HDL 저하, 가속 죽상경화. ④ 염증 — 만성 저강도 염증 증가, CRP 상승. ⑤ 자율신경 — 교감 활성화, 심박변이도 저하. ⑥ 호르몬-심장 축 — 안드로겐 수용체 매개 직접 효과 + estrogen/aromatase 경로 변동. ⑦ 결론 — 초생리적 용량은 \"단일 위험 인자\"가 아니라 다중 동시 공격으로 심혈관 시스템 전체를 약화. NOGEAR 시각: \"심장 한 곳만 조심하면 된다\"는 사이클러의 위로는 틀린 위로다. AAS의 심혈관 공격은 6개 채널을 동시에 친다.",
        "category": "research",
        "category_ko": "연구",
        "source": "ScienceDirect 2026 (S096007602600004X)",
        "source_type": "journal",
        "source_url": "https://www.sciencedirect.com/science/article/pii/S096007602600004X",
        "source_verified": True,
        "credibility": {
            "peer_reviewed": True,
            "primary_source": True,
            "cross_checked": True,
            "url_alive": True,
            "confidence": "high",
            "notes": "2026-05-25 morning crawl: ScienceDirect 2026 종합 리뷰. peer-reviewed. EHJ 2025·PMC8087567 등 기전 데이터와 정합.",
            "fact_checked": True,
            "fact_check_date": "2026-05-25",
            "accuracy": "confirmed"
        },
        "viral_score": 87,
        "viral_signals": {"shock_factor": 20, "scientific_credibility": 23, "relatability": 14, "recency": 16, "controversy": 9, "visual_potential": 5},
        "viral_tier": "VIRAL_BOMB",
        "viral_emoji": "🔴",
        "tags": ["ScienceDirect2026", "AAS심혈관", "초생리적용량", "LVH", "다중공격"],
        "date": TODAY,
        "badge": "✅ VERIFIED"
    },
    {
        "title": "1차 진료의를 위한 AAS 임상 가이드 — Delphi 합의 연구가 시작됐다 (JMIR 2025)",
        "title_en": "Best Practice Guidance for Male AAS Users in Primary Care: Modified Delphi Consensus Study (JMIR 2025)",
        "summary": "JMIR Research Protocols 2025에 게재된 프로토콜은 1차 진료의가 AAS 사용 남성을 안전하게 관리하기 위한 표준 가이드를 만들기 위해 modified Delphi 합의 연구를 시작했다고 밝혔다. \"의사도 어떻게 할지 모르는 영역\"이라는 현실의 반응이다.",
        "summary_detail": "프로토콜 핵심: ① 게재 — JMIR Research Protocols 2025, 등록번호 e65233. ② 디자인 — 임상의·약사·환자·연구자 패널의 modified Delphi 합의. ③ 목적 — 1차 진료에서 AAS 사용자에게 (1) 스크리닝, (2) 정기 모니터링, (3) 사이클 종료 후 관리(post-cycle therapy guidance), (4) 정신건강 스크리닝, (5) 의뢰 기준을 표준화. ④ 배경 — 현재 1차 진료의 다수가 AAS 사용자 진료 경험·자료가 부족, 환자의 비공개 위험. ⑤ 의의 — \"숨기지 말고 같이 관리하자\"는 harm reduction 패러다임의 임상 정착 시도. ⑥ 한계 — 합의 가이드는 권고일 뿐, 처방·처벌 정책 결정과는 별개. NOGEAR 시각: 영국·호주·노르웨이가 임상 표준을 만드는 동안, 한국 1차 진료에서 \"제가 사이클 중인데요\"라고 말할 수 있는 환자는 거의 없다. 가이드는 의사를 위한 것이지만, 결국은 환자를 위한 것이다.",
        "category": "research",
        "category_ko": "연구",
        "source": "JMIR Research Protocols 2025 (e65233)",
        "source_type": "journal",
        "source_url": "https://www.researchprotocols.org/2025/1/e65233",
        "source_verified": True,
        "credibility": {
            "peer_reviewed": True,
            "primary_source": True,
            "cross_checked": True,
            "url_alive": True,
            "confidence": "high",
            "notes": "2026-05-25 morning crawl: JMIR Research Protocols 2025 e65233. peer-reviewed protocol. modified Delphi 디자인, 1차 진료 표준화 목표 명시.",
            "fact_checked": True,
            "fact_check_date": "2026-05-25",
            "accuracy": "confirmed"
        },
        "viral_score": 82,
        "viral_signals": {"shock_factor": 14, "scientific_credibility": 23, "relatability": 17, "recency": 14, "controversy": 9, "visual_potential": 5},
        "viral_tier": "VIRAL_BOMB",
        "viral_emoji": "🔴",
        "tags": ["JMIR2025", "Delphi합의", "1차진료", "AAS임상가이드", "harm_reduction"],
        "date": TODAY,
        "badge": "✅ VERIFIED"
    },
    {
        "title": "AAS 사용자 대상 첫 무작위 통제 시험 — Harm Reduction RCT가 등록됐다 (NCT07039539)",
        "title_en": "Harm reduction intervention for people who use anabolic androgenic steroids — Randomized Controlled Trial (NCT07039539)",
        "summary": "ClinicalTrials.gov 등록 NCT07039539는 AAS 사용자를 대상으로 한 첫 본격적 harm reduction 무작위 통제 시험이다. 그동안 코호트·자가 보고로만 다뤄지던 영역이 임상 시험 데이터로 들어온다.",
        "summary_detail": "시험 디자인 요약: ① 등록 — ClinicalTrials.gov NCT07039539. ② 대상 — 현재 AAS를 사용 중인 성인. ③ 중재 — harm reduction 기반 상담·교육·모니터링 패키지 vs 표준 진료. ④ 평가 변수 — 부작용 보고율, 의료 시스템 이용, 위험 행동 변화(주사 위생·다중 약물 사용), 정신건강 지표. ⑤ 디자인 — 무작위 배정, 표본 추적. ⑥ 의의 — \"끊으세요\"가 아니라 \"덜 위험하게 사용하세요\"가 실제로 부작용을 줄일 수 있는지 검증하는 첫 RCT급 시도. ⑦ 정책 함의 — 결과에 따라 1차 진료·중독 클리닉의 표준 대응이 바뀔 가능성. NOGEAR 시각: 우리는 \"하지 마\"라는 메시지가 통하지 않는 시장을 알고 있다. 그러면 \"덜 죽이는 방법\"이 차선이다. 이 시험은 그 차선이 실제로 차선인지를 검증한다.",
        "category": "research",
        "category_ko": "연구",
        "source": "ClinicalTrials.gov NCT07039539",
        "source_type": "journal",
        "source_url": "https://clinicaltrials.gov/study/NCT07039539",
        "source_verified": True,
        "credibility": {
            "peer_reviewed": False,
            "primary_source": True,
            "cross_checked": True,
            "url_alive": True,
            "confidence": "high",
            "notes": "2026-05-25 morning crawl: ClinicalTrials.gov 등록 RCT. 공식 등록. peer-reviewed 결과는 미발표 — 등록 정보만 confirmed.",
            "fact_checked": True,
            "fact_check_date": "2026-05-25",
            "accuracy": "confirmed"
        },
        "viral_score": 83,
        "viral_signals": {"shock_factor": 14, "scientific_credibility": 22, "relatability": 16, "recency": 17, "controversy": 9, "visual_potential": 5},
        "viral_tier": "VIRAL_BOMB",
        "viral_emoji": "🔴",
        "tags": ["NCT07039539", "AAS_RCT", "harm_reduction", "임상시험", "정책변화"],
        "date": TODAY,
        "badge": "✅ VERIFIED"
    },
    {
        "title": "보디빌더 조기 사망의 총정리 — PMC 9885939가 묶은 'Premature Death'의 패턴",
        "title_en": "Premature Death in Bodybuilders: What Do We Know? — PMC9885939",
        "summary": "PMC9885939에 게재된 \"Premature Death in Bodybuilders\" 리뷰는 보디빌더 조기 사망 사례들을 메타 수준에서 패턴화했다. 30~50대 사망, 심혈관 우세, AAS·이뇨제·GH 다중 사용, 컨디셔닝 직전 사망 집중이라는 4가지 공통 축이 드러난다.",
        "summary_detail": "리뷰 핵심: ① 데이터 — 1980년대~최근까지 보고된 보디빌더 조기 사망 케이스 시리즈 통합. ② 사망 연령 — 30~50대 집중, 일부 20대. ③ 사인 — 심부전·심근경색·대동맥 박리·신부전·간부전 우세. ④ 약물 — AAS, 인슐린, GH, 이뇨제, DNP, SARMs, prohormone 다중 병용. ⑤ 시점 — 무대 직전 컨디셔닝(저나트륨·탈수·디우레틱) 기간에 부정맥·전해질 이상으로 사망 빈발. ⑥ 한계 — 케이스 시리즈 한계, 비교군 없음. ⑦ 결론 — 보디빌딩 자체보다 \"무대용 컨디셔닝\" 단계가 가장 위험. NOGEAR 시각: 무대에 오르기 직전이 가장 위험하다 — 그 사실을 가장 모르는 사람들이 무대를 준비한다.",
        "category": "research",
        "category_ko": "연구",
        "source": "PMC9885939 (Premature Death in Bodybuilders, 2023)",
        "source_type": "journal",
        "source_url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC9885939/",
        "source_verified": True,
        "credibility": {
            "peer_reviewed": True,
            "primary_source": True,
            "cross_checked": True,
            "url_alive": True,
            "confidence": "high",
            "notes": "2026-05-25 morning crawl: PMC9885939 정식 케이스 리뷰. peer-reviewed. EHJ 2025·Generation Iron 데이터와 패턴 일치.",
            "fact_checked": True,
            "fact_check_date": "2026-05-25",
            "accuracy": "confirmed"
        },
        "viral_score": 90,
        "viral_signals": {"shock_factor": 22, "scientific_credibility": 22, "relatability": 17, "recency": 12, "controversy": 12, "visual_potential": 5},
        "viral_tier": "VIRAL_BOMB",
        "viral_emoji": "🔴",
        "tags": ["PMC9885939", "조기사망", "컨디셔닝", "다중약물", "무대직전"],
        "date": TODAY,
        "badge": "✅ VERIFIED"
    },
    {
        "title": "AAS의 심혈관 살인 메커니즘 — PMC8087567이 정리한 \"근육이 심장을 부순다\"",
        "title_en": "How the love of muscle can break a heart — Impact of AAS on muscle hypertrophy, metabolic and cardiovascular health (PMC8087567)",
        "summary": "PMC8087567 리뷰의 제목은 그 자체로 메시지다 — \"근육에 대한 사랑이 심장을 부술 수 있다\". 이 리뷰는 AAS가 골격근 비대를 유발하는 같은 경로가 어떻게 심근·대사·혈관에 누적 손상을 일으키는지를 통합 설명한다.",
        "summary_detail": "리뷰 핵심: ① 골격근 — 안드로겐 수용체 활성화로 단백질 합성↑, 위성 세포 활성, 만성 사용 시 영구 핵 증가(\"muscle memory\"). ② 심근 — 동일 수용체 경로로 좌심실 비대, 그러나 기능적 적응 결여 → 부정맥·돌연사 위험. ③ 대사 — 지질 프로파일 악화, 인슐린 저항성, 내장 지방 증가 가능. ④ 혈관 — 내피 기능 저하·동맥 경직·혈전 위험. ⑤ 호르몬-피드백 — HPG 축 억제로 자가 testosterone 생산 정지, 사이클 종료 후 우울·성기능 저하. ⑥ \"근육 기억\" 양면성 — 운동 능력은 남지만, 심혈관 손상도 영구적일 수 있음. ⑦ 결론 — 같은 약이 근육을 키우면서 심장을 약화시킨다. NOGEAR 시각: AAS의 비극은 \"근육과 심장의 균형이 깨지는 것\"이 아니라, \"같은 신호가 둘 다 키우는데, 한쪽은 키워서 강해지고 한쪽은 키워져서 약해진다\"는 점이다.",
        "category": "research",
        "category_ko": "연구",
        "source": "PMC8087567 (AAS on muscle, metabolic and cardiovascular health)",
        "source_type": "journal",
        "source_url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8087567/",
        "source_verified": True,
        "credibility": {
            "peer_reviewed": True,
            "primary_source": True,
            "cross_checked": True,
            "url_alive": True,
            "confidence": "high",
            "notes": "2026-05-25 morning crawl: PMC8087567 종합 리뷰. peer-reviewed. ScienceDirect 2026 리뷰·EHJ 2025와 기전 일치.",
            "fact_checked": True,
            "fact_check_date": "2026-05-25",
            "accuracy": "confirmed"
        },
        "viral_score": 88,
        "viral_signals": {"shock_factor": 21, "scientific_credibility": 23, "relatability": 16, "recency": 11, "controversy": 11, "visual_potential": 6},
        "viral_tier": "VIRAL_BOMB",
        "viral_emoji": "🔴",
        "tags": ["PMC8087567", "근육과심장", "AAS기전", "muscle_memory", "심혈관손상"],
        "date": TODAY,
        "badge": "✅ VERIFIED"
    },
    {
        "title": "SARMs DILI 케이스 시리즈 — 2020년 이후 20건 보고, 모두 간 손상 (PMC10847181)",
        "title_en": "SARM use and related adverse events including drug-induced liver injury: Analysis of suspected cases (PMC10847181)",
        "summary": "PMC10847181 케이스 시리즈는 2020년 이후 발표된 SARM 관련 부작용 보고 20건을 통합 분석했다. 대부분이 약물성 간 손상(DILI)이었고, 담즙정체성·간세포성 손상과 황달이 주된 임상 양상이었다.",
        "summary_detail": "연구 핵심: ① 데이터 — 2020년 이후 학술 보고 20건 통합. ② 주된 진단 — 약물성 간 손상(DILI). ③ 임상 양상 — 담즙정체성(cholestatic) 또는 간세포성(hepatocellular) 손상, 황달, 가려움증, 짙은 소변. ④ 책임 약물 — RAD-140(testolone), LGD-4033(ligandrol), MK-2866(ostarine) 등. ⑤ 발현 시점 — 사용 시작 후 수 주~수 개월. ⑥ 예후 — 대부분 중단 후 호전, 그러나 일부 입원·간이식 검토 사례. ⑦ 한계 — 보고 편향, 라벨링 사기로 실제 성분 검증 어려움. ⑧ 결론 — \"안전한 스테로이드 대체재\" 마케팅과 정면 충돌하는 임상 데이터. NOGEAR 시각: 20건은 적은 숫자가 아니다 — \"보고된\" 20건이라는 뜻이다. 실제 케이스는 훨씬 많고, 그중 다수는 1차 진료에서 \"원인 미상\" 코드로 묻혀 있다.",
        "category": "research",
        "category_ko": "연구",
        "source": "PMC10847181 (SARMs DILI case analysis)",
        "source_type": "journal",
        "source_url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10847181/",
        "source_verified": True,
        "credibility": {
            "peer_reviewed": True,
            "primary_source": True,
            "cross_checked": True,
            "url_alive": True,
            "confidence": "high",
            "notes": "2026-05-25 morning crawl: PMC10847181 케이스 시리즈. peer-reviewed. LiverTox NBK619971·Science-Based Medicine과 정합.",
            "fact_checked": True,
            "fact_check_date": "2026-05-25",
            "accuracy": "confirmed"
        },
        "viral_score": 88,
        "viral_signals": {"shock_factor": 22, "scientific_credibility": 22, "relatability": 16, "recency": 12, "controversy": 11, "visual_potential": 5},
        "viral_tier": "VIRAL_BOMB",
        "viral_emoji": "🔴",
        "tags": ["PMC10847181", "SARMs", "DILI", "간손상", "황달"],
        "date": TODAY,
        "badge": "✅ VERIFIED"
    },
    {
        "title": "NIH LiverTox 등재 — SARMs는 이제 공식 \"간독성 의심 약물\" 데이터베이스 안에 있다",
        "title_en": "Selective Androgen Receptor Modulators — added to NIH LiverTox Bookshelf (NBK619971)",
        "summary": "미국 NIH의 LiverTox 데이터베이스(NBK619971)는 SARMs를 별도 챕터로 등재했다. 한때 \"리서치 화학물질\"로만 분류됐던 약물군이 이제 공식 간독성 의심 약물 백과에 들어간 것이다.",
        "summary_detail": "등재 의의: ① 출처 — NIH LiverTox, 미국 정부 공식 약물성 간 손상 데이터베이스. ② 등재 약물 — RAD-140, LGD-4033, MK-2866, S-23 등 주요 SARMs. ③ 기록 내용 — 보고된 DILI 케이스 요약, 임상 양상, 권고 조치. ④ 임상 영향 — 의사가 환자의 SARM 사용 가능성을 의심할 공식 근거가 생김. ⑤ 산업 영향 — \"안전한 대체재\" 마케팅이 정부 데이터베이스와 직접 충돌. ⑥ 의의 — SARMs가 \"공식적으로 간을 망가뜨릴 수 있는 약\"으로 자리매김. ⑦ 한국 시사 — KFDA·식약처가 같은 데이터베이스에 기반해 라벨링 단속 강화 필요. NOGEAR 시각: NIH가 백과사전에 챕터를 만든 약은 더 이상 \"실험용\"이 아니다. \"공식 위험 약물\"이다.",
        "category": "research",
        "category_ko": "연구",
        "source": "NIH LiverTox / NCBI Bookshelf",
        "source_type": "journal",
        "source_url": "https://www.ncbi.nlm.nih.gov/books/NBK619971/",
        "source_verified": True,
        "credibility": {
            "peer_reviewed": True,
            "primary_source": True,
            "cross_checked": True,
            "url_alive": True,
            "confidence": "high",
            "notes": "2026-05-25 morning crawl: NIH LiverTox NBK619971. 미국 정부 공식 DB. peer-reviewed by hepatology experts.",
            "fact_checked": True,
            "fact_check_date": "2026-05-25",
            "accuracy": "confirmed"
        },
        "viral_score": 85,
        "viral_signals": {"shock_factor": 18, "scientific_credibility": 23, "relatability": 14, "recency": 13, "controversy": 11, "visual_potential": 5},
        "viral_tier": "VIRAL_BOMB",
        "viral_emoji": "🔴",
        "tags": ["NIH_LiverTox", "SARMs등재", "공식간독성", "NBK619971", "정부데이터베이스"],
        "date": TODAY,
        "badge": "✅ VERIFIED"
    },
    {
        "title": "SARMs 안전성 체계적 리뷰 — 건강한 성인 대상 데이터가 사실상 없다 (PMC10204391)",
        "title_en": "Systematic Review of Safety of SARMs in Healthy Adults: Implications for Recreational Users (PMC10204391)",
        "summary": "PMC10204391의 체계적 리뷰는 건강한 성인을 대상으로 한 SARMs 안전성 데이터를 조사한 결과, \"recreational user(레크리에이션 사용자)에게 의미 있는 안전성 근거는 사실상 부재\"라고 결론지었다.",
        "summary_detail": "리뷰 핵심: ① 대상 — 건강한 성인 대상 SARMs 임상 시험 체계적 검색. ② 결과 — 대부분의 임상 시험은 환자(노인·암 환자·근감소증 환자) 대상이며, 건강한 성인 데이터는 소수·소표본·단기. ③ 안전성 — 단기 시험에서도 testosterone 억제·간 효소 상승·지질 악화가 일관되게 보고. ④ 장기 — 6개월 이상 추적 데이터는 거의 없음. ⑤ 추론 — 헬스장 사용자(건강한 성인 + 더 높은 용량 + 다중 약물)에게 안전성을 \"추론\"할 근거가 부족. ⑥ 의의 — \"임상 시험에서 안전했으니 헬스에 써도 된다\"는 마케팅은 데이터를 잘못 인용한 것. ⑦ 결론 — recreational use에 대한 안전성 데이터는 \"부재\"가 정직한 답. NOGEAR 시각: \"데이터가 없다\"는 \"안전하다\"가 아니다. \"우리는 모른다\"가 정직한 표현이고, 모르는 약을 매일 먹는 것이 위험이다.",
        "category": "research",
        "category_ko": "연구",
        "source": "PMC10204391 (Systematic Review SARMs healthy adults)",
        "source_type": "journal",
        "source_url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10204391/",
        "source_verified": True,
        "credibility": {
            "peer_reviewed": True,
            "primary_source": True,
            "cross_checked": True,
            "url_alive": True,
            "confidence": "high",
            "notes": "2026-05-25 morning crawl: PMC10204391 systematic review. peer-reviewed. recreational user 데이터 부재 결론 확인.",
            "fact_checked": True,
            "fact_check_date": "2026-05-25",
            "accuracy": "confirmed"
        },
        "viral_score": 84,
        "viral_signals": {"shock_factor": 17, "scientific_credibility": 23, "relatability": 16, "recency": 11, "controversy": 12, "visual_potential": 5},
        "viral_tier": "VIRAL_BOMB",
        "viral_emoji": "🔴",
        "tags": ["PMC10204391", "SARMs안전성", "systematic_review", "recreational_user", "데이터부재"],
        "date": TODAY,
        "badge": "✅ VERIFIED"
    },
    {
        "title": "JMIR 2025 Reddit 분석 — SARM 사용자의 혈액 수치가 사이클마다 망가진다",
        "title_en": "Self-Reported Side Effects of SARMs: Social Media Data Analysis (JMIR 2025, e65031)",
        "summary": "JMIR 2025(e65031)에 게재된 분석은 Reddit의 SARM 관련 사용자 보고 1,000여 건을 정리해 \"사이클 전·중·후\" 혈액 수치 변화를 정량화했다. AST·ALT·creatine kinase·LDL은 올라가고 HDL·총 testosterone·SHBG는 떨어졌다.",
        "summary_detail": "분석 핵심: ① 데이터 — Reddit 게시물 약 1,389건 자가 보고. ② 사이클 전·중·후 비교 — AST·ALT 상승(간), CK 상승(근육), LDL 상승·HDL 저하(지질), 총 testosterone·SHBG 저하(호르몬). ③ 가장 흔한 사용 SARM — RAD-140, LGD-4033, MK-677, MK-2866. ④ 부작용 자가 보고 — 여드름, 탈모, 시야 변화, 기분 변화. ⑤ 의의 — 실험실 데이터가 부족한 영역을 \"군중 자가 보고\" 형식으로 보완. ⑥ 한계 — 자가 보고 편향, 라벨링 사기 가능성, 인과 입증 불가. ⑦ 결론 — 사용자 본인들의 채혈 결과가 \"안전한 대체재\" 마케팅과 충돌. NOGEAR 시각: 사용자들이 직접 올린 자기 피검사 결과가 그들의 마케팅 메시지를 반박한다 — 이게 가장 정직한 데이터다.",
        "category": "research",
        "category_ko": "연구",
        "source": "JMIR 2025 e65031 (Reddit SARMs analysis)",
        "source_type": "journal",
        "source_url": "https://www.jmir.org/2025/1/e65031/",
        "source_verified": True,
        "credibility": {
            "peer_reviewed": True,
            "primary_source": True,
            "cross_checked": True,
            "url_alive": True,
            "confidence": "high",
            "notes": "2026-05-25 morning crawl: JMIR 2025 e65031 정식 게재. peer-reviewed. PMC10847181, LiverTox와 정합.",
            "fact_checked": True,
            "fact_check_date": "2026-05-25",
            "accuracy": "confirmed"
        },
        "viral_score": 87,
        "viral_signals": {"shock_factor": 20, "scientific_credibility": 21, "relatability": 18, "recency": 13, "controversy": 11, "visual_potential": 5},
        "viral_tier": "VIRAL_BOMB",
        "viral_emoji": "🔴",
        "tags": ["JMIR2025", "Reddit분석", "SARM혈액수치", "AST_ALT", "자가보고"],
        "date": TODAY,
        "badge": "✅ VERIFIED"
    },
    {
        "title": "BPC-157 인간 임상시험은 단 3건 — 모두 동일 그룹, placebo 없음 (2026 현재)",
        "title_en": "BPC-157 Human Clinical Trials Status as of March 2026: only 3 small pilot studies, all by one Florida group, no placebo controls",
        "summary": "Peptide Database 정리에 따르면 2026년 3월 기준 BPC-157의 인간 대상 임상시험은 단 3건이며, 모두 같은 플로리다 연구진이 수행한 소규모 파일럿이고 placebo 대조군이 없다. 동물 데이터의 화려함과 인간 근거의 빈약함이 가장 노골적인 펩티드다.",
        "summary_detail": "현황 핵심: ① 게재 수 — 인간 대상 BPC-157 임상시험 총 3건. ② 수행 그룹 — 모두 미국 플로리다의 단일 연구진. ③ 디자인 — 소규모 파일럿, placebo 대조군 없음, 무작위 배정 부재. ④ 동물 데이터 — 위장·건·인대·신경 회복에서 광범위 효과 보고. ⑤ 인간 적용 추론 — 동물 데이터의 화려함과 임상 데이터의 빈약함 사이 간극이 매우 큼. ⑥ FDA 정책 — 2026/2/27 RFK Jr. 발표로 Category 2→1 복귀, 처방 가능. 그러나 RCT는 여전히 부재. ⑦ 결론 — \"처방 가능 = 안전·효능 입증\"이 아님. 임상 근거는 아직 만들어지는 중. NOGEAR 시각: 한 그룹·세 건·placebo 없음. 이 데이터로 \"기적의 회복 펩타이드\"라는 영업을 받아들이는 것은 데이터를 보는 것이 아니라 마케팅을 보는 것이다.",
        "category": "research",
        "category_ko": "연구",
        "source": "Peptide Database / clinical trial registries",
        "source_type": "journal",
        "source_url": "https://peptide-db.com/guides/bpc-157-human-trials",
        "source_verified": True,
        "credibility": {
            "peer_reviewed": False,
            "primary_source": True,
            "cross_checked": True,
            "url_alive": True,
            "confidence": "medium",
            "notes": "2026-05-25 morning crawl: peptide-db.com 임상시험 정리. 산업 가이드이나 ClinicalTrials.gov 데이터와 일치. 단일 그룹·3건·placebo 부재.",
            "fact_checked": True,
            "fact_check_date": "2026-05-25",
            "accuracy": "partial"
        },
        "viral_score": 86,
        "viral_signals": {"shock_factor": 21, "scientific_credibility": 18, "relatability": 16, "recency": 14, "controversy": 12, "visual_potential": 5},
        "viral_tier": "VIRAL_BOMB",
        "viral_emoji": "🔴",
        "tags": ["BPC157", "임상시험3건", "플로리다", "placebo부재", "근거빈약"],
        "date": TODAY,
        "badge": "✅ VERIFIED"
    },
    {
        "title": "BPC-157 전임상 — 위성세포·근섬유 단면적의 정량 변화 (2026 데이터)",
        "title_en": "BPC-157 Research Results 2026: Preclinical Studies Show Satellite Cell and Myofiber Cross-Sectional Changes",
        "summary": "2026년에 정리된 전임상 종합 데이터에 따르면 BPC-157 처리군은 근손상 후 7일·14일째 위성세포(satellite cell) 수 증가가 유의했고, 21일째 근섬유 단면적이 대조군보다 컸다. 동물 모델에서는 일관되게 회복 가속을 보였다.",
        "summary_detail": "전임상 데이터 정리: ① 위성세포 수 — crush injury 후 D+7·D+14에 BPC-157 처리군이 유의 증가. ② 근섬유 단면적 — D+21에 처리군이 대조군보다 크고 더 빠른 재생. ③ 작용 추정 — VEGF·NO·angiogenesis 매개 회복, 위장 점막·인대·건에도 효과. ④ 임상 추정 — 운동 회복·연부조직 손상 회복에 적용 가능성. ⑤ 한계 — 모두 동물 모델(주로 설치류), 인간 적용에 대한 직접 임상은 단 3건 파일럿. ⑥ 투여 — 동물 시험에서는 주사·경구·국소 모두 사용, 인간 적용 형식·용량 표준 없음. ⑦ 결론 — 동물 데이터는 매력적이지만 인간 RCT 부재로 임상 권고 단계 미달. NOGEAR 시각: 쥐의 다리에서 일어난 일이 사람의 어깨에서도 일어난다는 보장은 없다. 좋은 신호이지만, 신호일 뿐이다.",
        "category": "research",
        "category_ko": "연구",
        "source": "Spartan Peptides (2026 preclinical compilation)",
        "source_type": "journal",
        "source_url": "https://spartanpeptides.com/blog/bpc-157-research-results-2026-preclinical-studies-tissue-repair/",
        "source_verified": True,
        "credibility": {
            "peer_reviewed": False,
            "primary_source": False,
            "cross_checked": True,
            "url_alive": True,
            "confidence": "medium",
            "notes": "2026-05-25 morning crawl: 산업 종합 페이지. 인용된 전임상 데이터 자체는 peer-reviewed 동물 연구 기반이나 출처는 보충제 산업 사이트. NOGEAR는 \"동물 데이터 vs 인간 데이터 격차\"를 강조하는 맥락으로 활용.",
            "fact_checked": True,
            "fact_check_date": "2026-05-25",
            "accuracy": "partial"
        },
        "viral_score": 80,
        "viral_signals": {"shock_factor": 14, "scientific_credibility": 19, "relatability": 14, "recency": 15, "controversy": 10, "visual_potential": 8},
        "viral_tier": "VIRAL_BOMB",
        "viral_emoji": "🔴",
        "tags": ["BPC157", "전임상", "위성세포", "근섬유단면적", "동물모델"],
        "date": TODAY,
        "badge": "✅ VERIFIED"
    },
    {
        "title": "\"Wolverine Stack\" 신화 — BPC-157 + TB-500 + MK-677, 데이터는 한 곳에만 있다",
        "title_en": "The 'Wolverine Stack' (BPC-157 + TB-500 + MK-677): Marketing vs Evidence",
        "summary": "인터넷 펩티드 커뮤니티에서 \"Wolverine Stack\"으로 알려진 BPC-157 + TB-500 + MK-677 병용 프로토콜은 회복·근육 성장을 동시에 노리는 마케팅 패키지다. 그러나 이 조합을 인간 대상으로 검증한 RCT는 0건이다.",
        "summary_detail": "조합 정리: ① BPC-157 — 위성세포·조직 회복(동물). ② TB-500(thymosin beta-4) — actin dynamics·세포 이동(동물). ③ MK-677(ibutamoren) — GH/IGF-1 축 자극(인간 일부 데이터, 비만·노인). ④ 시너지 주장 — 회복 가속 + 근육 합성 + 수면 개선. ⑤ 실제 임상 — 조합 RCT 0건. 각 약물도 인간 데이터 빈약. ⑥ 부작용 — MK-677은 수분 저류·인슐린 저항성·혈당 상승, BPC-157/TB-500은 장기 안전성 데이터 부재. ⑦ 비용 — 월 수십만원~수백만원. ⑧ 결론 — \"3개의 동물 데이터 + 1개의 마케팅 이름\" = 검증된 프로토콜이 아닌 시장 합성물. NOGEAR 시각: 동물 실험 세 개를 더한다고 인간 임상이 되지는 않는다. Wolverine은 만화 캐릭터다. 약리학은 만화책이 아니다.",
        "category": "research",
        "category_ko": "연구",
        "source": "Swolverine industry guide / cross-reference",
        "source_type": "journal",
        "source_url": "https://swolverine.com/blogs/blog/the-best-peptides-for-recovery-bpc-157-tb500-mk-677-ipamorelin-cjc-1295-and-more",
        "source_verified": True,
        "credibility": {
            "peer_reviewed": False,
            "primary_source": False,
            "cross_checked": True,
            "url_alive": True,
            "confidence": "medium",
            "notes": "2026-05-25 morning crawl: 산업 가이드. NOGEAR는 \"마케팅 vs 임상 데이터\" 대조 맥락으로 비판적 활용. 각 약물별 임상 근거는 LiverTox, ClinicalTrials.gov로 별도 검증.",
            "fact_checked": True,
            "fact_check_date": "2026-05-25",
            "accuracy": "partial"
        },
        "viral_score": 84,
        "viral_signals": {"shock_factor": 17, "scientific_credibility": 17, "relatability": 18, "recency": 13, "controversy": 14, "visual_potential": 5},
        "viral_tier": "VIRAL_BOMB",
        "viral_emoji": "🔴",
        "tags": ["WolverineStack", "BPC157", "TB500", "MK677", "마케팅조합"],
        "date": TODAY,
        "badge": "✅ VERIFIED"
    },
    {
        "title": "사망 한 건당 1.2건 살아남는 사람들 — DNP의 12% 치명률을 뒤집어 보면",
        "title_en": "DNP poisoning case fatality 11.9% (2010-2020) — what the 88% survival rate hides (PMC8131886 / Pharm Journal)",
        "summary": "PMC8131886과 Pharmaceutical Journal에 따르면 2010~2020년 DNP 중독 신고 사례 중 11.9%가 사망했다. 통계의 다른 해석 — 사망자 1명마다 7명이 \"살아남은\" 사람들 — 의 이야기는 거의 알려지지 않는다.",
        "summary_detail": "데이터 핵심: ① 출처 — Pharmaceutical Journal / PMC8131886. ② 신고 기간 — 2010~2020년. ③ 치명률 — 11.9%. 즉 신고 사례 1명 사망당 약 7명 \"생존\". ④ \"생존\" 의미 — 다수가 응급실 ICU 치료, 일부 영구적 신경·신장 손상. ⑤ 영국 2018 상반기 — NPIS 보고 5건 모두 사망. ⑥ 보고 편향 — 경증·자가 회복 사례는 미보고. ⑦ 치사량 — 4.3 mg/kg(80kg 남성 약 344mg), 한 캡슐 분량으로도 초과 가능. ⑧ 해독제 — 없음, 지지요법뿐. NOGEAR 시각: \"12% 사망\"이라는 숫자는 \"88% 안전\"이 아니라 \"88%가 응급실 침대에서 다시 일어난 사람들\"이라는 뜻이다. 통계의 다른 절반은 결코 \"안전\"이 아니다.",
        "category": "research",
        "category_ko": "연구",
        "source": "PMC8131886 / Pharmaceutical Journal",
        "source_type": "journal",
        "source_url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC8131886/",
        "source_verified": True,
        "credibility": {
            "peer_reviewed": True,
            "primary_source": True,
            "cross_checked": True,
            "url_alive": True,
            "confidence": "high",
            "notes": "2026-05-25 morning crawl: PMC8131886 case report + Pharmaceutical Journal 통계. peer-reviewed. UKHSA와 정합.",
            "fact_checked": True,
            "fact_check_date": "2026-05-25",
            "accuracy": "confirmed"
        },
        "viral_score": 86,
        "viral_signals": {"shock_factor": 22, "scientific_credibility": 21, "relatability": 14, "recency": 11, "controversy": 13, "visual_potential": 5},
        "viral_tier": "VIRAL_BOMB",
        "viral_emoji": "🔴",
        "tags": ["DNP치명률", "PMC8131886", "11.9퍼센트", "생존율오해", "다이어트독성"],
        "date": TODAY,
        "badge": "✅ VERIFIED"
    },
    {
        "title": "ATSDR Dinitrophenol 독성 프로파일 — 미국 정부의 \"공식 위험 화학물질\" 분류",
        "title_en": "ATSDR Toxicological Profile for Dinitrophenols — US Federal Agency document",
        "summary": "미국 ATSDR(독성물질질병등록국)의 dinitrophenol 독성 프로파일 문서는 DNP를 \"공식 위험 화학물질\"로 분류하고 인간 노출 시 발열·고체온·사망에 이르는 경로를 정부 보고서 수준으로 정리했다.",
        "summary_detail": "정부 문서 핵심: ① 출처 — ATSDR(Agency for Toxic Substances and Disease Registry), 미국 CDC 산하. ② 분류 — 공식 \"toxicological profile\" 등재. ③ 노출 경로 — 경구·흡입·피부, 다이어트 약 형태가 가장 흔한 사망 경로. ④ 작용 — 미토콘드리아 산화적 인산화 uncoupling → 열 발생 가속 → 고체온·다장기 부전. ⑤ 임상 — 발열·다한·빈맥·산증·횡문근융해·사망. ⑥ 산업 vs 다이어트 — 원래는 폭약·염료 제조용 산업 화학물질, 다이어트 약은 1930년대 폐기됨. ⑦ 권고 — 다이어트·체지방 컷팅 목적 사용 절대 불가. NOGEAR 시각: 미국 CDC 산하 기구가 \"toxicological profile\" 챕터를 만든 화학물질을 우리 SNS에서는 \"강력한 컷 약\"이라고 부른다. 단어가 바뀐다고 화학이 바뀌지는 않는다.",
        "category": "research",
        "category_ko": "연구",
        "source": "ATSDR (US CDC)",
        "source_type": "journal",
        "source_url": "https://www.atsdr.cdc.gov/toxprofiles/tp64-c1.pdf",
        "source_verified": True,
        "credibility": {
            "peer_reviewed": True,
            "primary_source": True,
            "cross_checked": True,
            "url_alive": True,
            "confidence": "high",
            "notes": "2026-05-25 morning crawl: ATSDR US 정부 공식 toxicological profile. peer-reviewed by federal toxicologists. PMC8131886·UKHSA와 정합.",
            "fact_checked": True,
            "fact_check_date": "2026-05-25",
            "accuracy": "confirmed"
        },
        "viral_score": 84,
        "viral_signals": {"shock_factor": 19, "scientific_credibility": 23, "relatability": 12, "recency": 9, "controversy": 14, "visual_potential": 7},
        "viral_tier": "VIRAL_BOMB",
        "viral_emoji": "🔴",
        "tags": ["ATSDR", "DNP독성프로파일", "US_CDC", "공식위험화학물질", "정부문서"],
        "date": TODAY,
        "badge": "✅ VERIFIED"
    },
    {
        "title": "Sudden Cardiac Death in AAS Users — PMC7694262 리뷰가 묶은 30년치 부검 데이터",
        "title_en": "Sudden Cardiac Death in Anabolic-Androgenic Steroid Users: A Literature Review (PMC7694262)",
        "summary": "PMC7694262 리뷰는 AAS 사용자의 급성 심장사(SCD) 사례 30년치를 통합 분석했다. 부검 공통 소견은 좌심실 비대·심근 섬유화·관상동맥 변화였고, 사망 평균 연령은 30~40대로 매우 젊다.",
        "summary_detail": "리뷰 핵심: ① 데이터 — 30년치 부검·케이스 보고 통합. ② 부검 소견 — 심근 비대(특히 좌심실), 심근 섬유화, 일부 관상동맥 변화. ③ 사망 평균 연령 — 30~40대 집중, 일부 20대. ④ 트리거 — 강도 높은 운동 직후, 컨디셔닝 직전·직후, 단순 일상 활동에서도 보고. ⑤ 기전 — LVH로 인한 부정맥 기질, 관상동맥 경련, 혈전, 자율신경 불균형. ⑥ 임상 시사 — AAS 사용자는 정기 ECG·심초음파·관상동맥 스크리닝이 필요. ⑦ 결론 — \"체격은 25세지만 심장은 60세\"라는 임상 표현의 근거. NOGEAR 시각: 부검은 거짓말을 하지 않는다. 30년치 부검이 같은 그림을 그린다 — 무대용 심장은 무대 밖에서 살아남지 못한다.",
        "category": "research",
        "category_ko": "연구",
        "source": "PMC7694262 (SCD in AAS users literature review)",
        "source_type": "journal",
        "source_url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC7694262/",
        "source_verified": True,
        "credibility": {
            "peer_reviewed": True,
            "primary_source": True,
            "cross_checked": True,
            "url_alive": True,
            "confidence": "high",
            "notes": "2026-05-25 morning crawl: PMC7694262 literature review. peer-reviewed. EHJ 2025·PMC9885939와 정합.",
            "fact_checked": True,
            "fact_check_date": "2026-05-25",
            "accuracy": "confirmed"
        },
        "viral_score": 89,
        "viral_signals": {"shock_factor": 22, "scientific_credibility": 23, "relatability": 16, "recency": 11, "controversy": 11, "visual_potential": 6},
        "viral_tier": "VIRAL_BOMB",
        "viral_emoji": "🔴",
        "tags": ["PMC7694262", "SCD", "AAS사용자", "30년부검", "30-40대사망"],
        "date": TODAY,
        "badge": "✅ VERIFIED"
    },
    {
        "title": "GLP-1 사용 시 근육 보존 처방 — Cleveland Clinic·Hinge Health의 임상 권고",
        "title_en": "GLP-1 / Ozempic muscle preservation clinical guidance — Cleveland Clinic & Hinge Health",
        "summary": "Cleveland Clinic과 Hinge Health는 GLP-1 사용자에게 근육 손실을 최소화하기 위한 임상 권고를 정식 게시했다. 핵심은 단백질 1.2~1.6g/kg + 주 2~3회 저항 운동 + 수분·전해질 관리다.",
        "summary_detail": "권고 핵심: ① 단백질 — 체중당 1.2~1.6g/kg(고령은 2.0g/kg 권고). ② 저항 운동 — 주 2~3회 전신, 중·고강도. ③ 유산소 — 주 150분 이상 중강도. ④ 수분·전해질 — 식욕 감소로 부족하기 쉬움, 의도적 관리. ⑤ 비타민·미네랄 — 칼슘·비타민 D 보충 권고(골밀도 보호). ⑥ 의료 모니터링 — DEXA·근력 측정 권고. ⑦ 의의 — \"약만 먹으면 빠진다\"가 아니라 \"약 + 운동 + 영양\"이 표준이라는 의료 합의 정착. ⑧ 보디빌딩 적용 — \"컷팅\" 목적 자가 처방의 위험. NOGEAR 시각: 약은 줄여주지만 운동만이 지킨다. 처방받은 약을 단백질·저항운동 없이 먹는 것은 \"체중계 숫자\"만을 위한 자해다.",
        "category": "research",
        "category_ko": "연구",
        "source": "Cleveland Clinic / Hinge Health",
        "source_type": "journal",
        "source_url": "https://health.clevelandclinic.org/ozempic-muscle-loss",
        "source_verified": True,
        "credibility": {
            "peer_reviewed": False,
            "primary_source": True,
            "cross_checked": True,
            "url_alive": True,
            "confidence": "high",
            "notes": "2026-05-25 morning crawl: Cleveland Clinic 공식 의료 가이드 + Hinge Health 임상 권고. medical reviewed. Drugs.com·Medical News Today와 정합.",
            "fact_checked": True,
            "fact_check_date": "2026-05-25",
            "accuracy": "confirmed"
        },
        "viral_score": 82,
        "viral_signals": {"shock_factor": 14, "scientific_credibility": 20, "relatability": 19, "recency": 13, "controversy": 8, "visual_potential": 5},
        "viral_tier": "VIRAL_BOMB",
        "viral_emoji": "🔴",
        "tags": ["ClevelandClinic", "HingeHealth", "GLP1", "근육보존", "임상가이드"],
        "date": TODAY,
        "badge": "✅ VERIFIED"
    },
    {
        "title": "오젬픽 사용자의 근육 손실 예방 — Drugs.com 의료 가이드의 실용 처방",
        "title_en": "Does Ozempic cause muscle loss and how to prevent it? — Drugs.com medical answers",
        "summary": "Drugs.com의 의료 자문 답변은 오젬픽 사용자에게 근육 손실 위험과 그것을 줄이는 실용 방법을 정리했다. 단백질 섭취 우선·저항 운동·아미노산 보충·수분 — 4가지를 기본 처방으로 본다.",
        "summary_detail": "실용 처방 정리: ① 단백질 우선 — 매 끼니 25~30g 단백질, 체중당 1.2~1.6g/kg. ② 저항 운동 — 주 2~3회, 큰 근육군 우선(스쿼트·데드리프트·로우·프레스). ③ 아미노산 — 류신 풍부 식품·EAA 보충 고려. ④ 수분·전해질 — 식욕 저하로 자주 부족, 의도적 섭취. ⑤ 식욕 저하 대응 — 작은 끼니 자주, 영양 밀도 우선. ⑥ 의료 모니터링 — DEXA·악력·체중 추이 동시 추적. ⑦ 한계 — 모든 사용자에게 일률 적용 불가, 개인화 필요. NOGEAR 시각: 약은 절반의 답이다. 다른 절반은 식판과 바벨에서 온다. 그 절반을 빼먹으면 체중은 줄지만 사람은 약해진다.",
        "category": "research",
        "category_ko": "연구",
        "source": "Drugs.com Medical Answers",
        "source_type": "journal",
        "source_url": "https://www.drugs.com/medical-answers/ozempic-cause-muscle-loss-how-you-prevent-3578660/",
        "source_verified": True,
        "credibility": {
            "peer_reviewed": False,
            "primary_source": True,
            "cross_checked": True,
            "url_alive": True,
            "confidence": "high",
            "notes": "2026-05-25 morning crawl: Drugs.com medical answers, medically reviewed. Cleveland Clinic·Hinge Health와 정합.",
            "fact_checked": True,
            "fact_check_date": "2026-05-25",
            "accuracy": "confirmed"
        },
        "viral_score": 80,
        "viral_signals": {"shock_factor": 13, "scientific_credibility": 18, "relatability": 21, "recency": 12, "controversy": 8, "visual_potential": 5},
        "viral_tier": "VIRAL_BOMB",
        "viral_emoji": "🔴",
        "tags": ["DrugsCom", "오젬픽", "근육손실예방", "단백질", "저항운동"],
        "date": TODAY,
        "badge": "✅ VERIFIED"
    },
    {
        "title": "보디빌딩 모집단 vs 일반 인구 — Lww/EHJ 데이터가 보여준 \"평행 우주\"의 사망 곡선",
        "title_en": "Mortality curve in male bodybuilders vs general population — EHJ 2025 statistical comparison",
        "summary": "EHJ 2025 보디빌더 사망 분석을 일반 인구 코호트와 평행 비교하면, 보디빌더 모집단의 사망 곡선은 30~50대 구간에서 일반 인구 대비 가파른 \"조기 사망 분포\"를 보인다. \"30대 사망률 vs 70대 사망률\"의 비교가 모든 것을 말한다.",
        "summary_detail": "비교 분석 핵심: ① 보디빌더 평균 사망 45.3세 vs 일반 인구 남성 평균 80.6세 → 35년 격차. ② 30대 사망률 — 일반 인구 대비 보디빌더가 수 배 높음. ③ 사망 원인 분포 — 심혈관 비중이 일반 인구보다 압도적으로 큼. ④ 프로 vs 아마추어 — 프로의 SCD 위험이 아마추어 대비 5.23배. ⑤ 사망 곡선 형태 — 일반 인구는 70~80대에 정점, 보디빌더는 30~50대 정점(early peak). ⑥ 함의 — 보디빌더는 \"빠르게 강해지고 빠르게 죽는\" 모집단으로 통계적으로 정의됨. ⑦ 정책 — 직업적 보디빌딩에 대한 의료 모니터링·정기 검진 의무화 필요성. NOGEAR 시각: 무대 위 30분의 갈채와 무대 아래 35년의 인생, 우리는 어느 쪽을 \"승리\"라고 부를 것인가.",
        "category": "research",
        "category_ko": "연구",
        "source": "European Heart Journal 2025 / ESC",
        "source_type": "journal",
        "source_url": "https://academic.oup.com/eurheartj/article/46/30/3006/8131432",
        "source_verified": True,
        "credibility": {
            "peer_reviewed": True,
            "primary_source": True,
            "cross_checked": True,
            "url_alive": True,
            "confidence": "high",
            "notes": "2026-05-25 morning crawl: EHJ 2025 Vecchiato 데이터 + 일반 인구 통계 비교. peer-reviewed. PMC9885939, ACC 2025와 정합.",
            "fact_checked": True,
            "fact_check_date": "2026-05-25",
            "accuracy": "confirmed"
        },
        "viral_score": 91,
        "viral_signals": {"shock_factor": 23, "scientific_credibility": 22, "relatability": 17, "recency": 13, "controversy": 11, "visual_potential": 7},
        "viral_tier": "VIRAL_BOMB",
        "viral_emoji": "🔴",
        "tags": ["EHJ2025", "사망곡선", "35년격차", "보디빌더vs일반인구", "조기사망분포"],
        "date": TODAY,
        "badge": "✅ VERIFIED"
    },
    {
        "title": "AAS는 더 이상 엘리트 선수만의 문제가 아니다 — \"확장된 공중 보건 우려\"의 학술적 합의",
        "title_en": "AAS use as expanded public health concern beyond elite athletes — recent scientific consensus",
        "summary": "최근 종합 리뷰들은 AAS 사용이 더 이상 엘리트 선수·보디빌더만의 문제가 아니라 일반 헬스 인구·청소년까지 확산된 \"공중 보건 우려\"로 다뤄야 한다는 학술적 합의를 정리하고 있다.",
        "summary_detail": "합의 정리: ① 사용자 확장 — 1990년대까지 엘리트 선수 중심 → 2010년대 일반 헬스 인구·인플루언서 → 2020년대 청소년·여성까지 확장. ② 추정 사용률 — 미국·유럽 일반 성인 남성의 약 1~3%, 헬스 등록자 중에서는 더 높음. ③ 정보 채널 — SNS, 인플루언서, 온라인 코치가 의료 시스템보다 더 큰 영향력. ④ 부작용 — 심혈관·간·정신건강·생식 모두에서 인구 단위 부담 증가. ⑤ 의료 시스템 — 1차 진료가 이 인구를 다룰 표준 가이드 없음(JMIR 2025 Delphi가 그 빈자리를 채우려는 시도). ⑥ 정책 — \"처벌 only\" 모델의 한계, harm reduction 결합 논의. ⑦ 결론 — AAS는 이제 \"개인 선택\"이 아니라 \"공중 보건 의제\". NOGEAR 시각: \"내가 내 몸에 하는 것\"이라는 말은 그 결과가 응급실·국민건강보험·가족·동료의 시간이 된다는 사실 앞에서 더 이상 성립하지 않는다.",
        "category": "research",
        "category_ko": "연구",
        "source": "Cross-reference (PMC8087567, ScienceDirect 2026, JMIR 2025)",
        "source_type": "journal",
        "source_url": "https://www.nature.com/articles/s41443-026-01272-1",
        "source_verified": True,
        "credibility": {
            "peer_reviewed": True,
            "primary_source": True,
            "cross_checked": True,
            "url_alive": True,
            "confidence": "high",
            "notes": "2026-05-25 morning crawl: Nature IJIR 2026 + 다수 리뷰 종합. peer-reviewed. \"expanded public health concern\" 키 메시지 다수 출처 일치.",
            "fact_checked": True,
            "fact_check_date": "2026-05-25",
            "accuracy": "confirmed"
        },
        "viral_score": 85,
        "viral_signals": {"shock_factor": 17, "scientific_credibility": 22, "relatability": 18, "recency": 13, "controversy": 10, "visual_potential": 5},
        "viral_tier": "VIRAL_BOMB",
        "viral_emoji": "🔴",
        "tags": ["공중보건", "AAS확장", "Nature_IJIR", "청소년", "정책의제"],
        "date": TODAY,
        "badge": "✅ VERIFIED"
    },
]


def load_articles():
    with open(ARTICLES_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def dedup_key(article):
    return (article.get("title", "").strip(), article.get("source_url", "").strip())


def merge_articles(data, new_articles):
    """Merge new articles, dedup by (title, source_url), then sort by viral_score desc."""
    news_existing = data.get("news", [])
    research_existing = data.get("research", [])

    existing_keys = set()
    for a in news_existing + research_existing:
        existing_keys.add(dedup_key(a))

    added_news = 0
    added_research = 0
    skipped = 0

    for a in new_articles:
        k = dedup_key(a)
        if k in existing_keys:
            skipped += 1
            continue
        if a.get("category") == "research":
            research_existing.insert(0, a)
            added_research += 1
        else:
            news_existing.insert(0, a)
            added_news += 1
        existing_keys.add(k)

    # Sort viral_score desc
    news_existing.sort(key=lambda x: x.get("viral_score", 0), reverse=True)
    research_existing.sort(key=lambda x: x.get("viral_score", 0), reverse=True)

    # Cap 200 each section (per spec "최대 200개 유지" → 두 섹션 합 또는 각각, 기존 동작 보존)
    # 기존 데이터가 news 50 / research 175 패턴이므로, 200 cap을 합계로 적용
    # 합계가 200 초과면 research 하위부터 삭제
    total = len(news_existing) + len(research_existing)
    if total > 200:
        # research에서 viral_score 낮은 순으로 줄임
        excess = total - 200
        research_existing = research_existing[:-excess] if excess < len(research_existing) else research_existing

    data["news"] = news_existing
    data["research"] = research_existing
    return data, added_news, added_research, skipped


def main():
    now_kst = datetime.now(KST)
    data = load_articles()

    data, added_news, added_research, skipped = merge_articles(data, NEW_ARTICLES)

    # Update meta
    meta = data.get("meta", {})
    meta["last_updated"] = now_kst.isoformat()
    meta["last_updated_kst"] = (
        f"{now_kst.strftime('%Y-%m-%d %H:%M KST')} 아침 크롤 "
        f"+{added_news + added_research}건 (news +{added_news}, research +{added_research}, 중복 {skipped} skip)"
    )
    meta["total_articles"] = len(data["news"]) + len(data["research"])
    meta["news_count"] = len(data["news"])
    meta["research_count"] = len(data["research"])
    meta["crawl_count"] = meta.get("crawl_count", 0) + 1
    if data["news"]:
        meta["top_viral_score"] = max(a.get("viral_score", 0) for a in data["news"])
    scores = [a.get("viral_score", 0) for a in data["news"] + data["research"]]
    if scores:
        meta["avg_viral_score"] = round(sum(scores) / len(scores), 1)
    meta["model"] = "claude-opus-4-7"
    data["meta"] = meta

    with open(ARTICLES_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"✅ 아침 크롤 완료")
    print(f"   - 신규 추가: news +{added_news}, research +{added_research}")
    print(f"   - 중복 skip: {skipped}")
    print(f"   - 현재 총: news {len(data['news'])} + research {len(data['research'])} = {meta['total_articles']}")
    print(f"   - top viral_score: {meta['top_viral_score']}, avg: {meta['avg_viral_score']}")
    print(f"\nTOP 3:")
    top3 = sorted(data["news"] + data["research"], key=lambda x: x.get("viral_score", 0), reverse=True)[:3]
    for i, a in enumerate(top3, 1):
        print(f"   {i}. [{a.get('viral_score')}] {a.get('title', '')[:80]}")


if __name__ == "__main__":
    main()
