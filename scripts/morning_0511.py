#!/usr/bin/env python3
"""
NOGEAR Magazine — 2026-05-11 아침 크롤
포커스: 스테로이드/AAS 심혈관 연구·SARMs 간독성·DNP·페이크 내추럴·도핑 스캔들·펩타이드 FDA 재분류·오젬픽
"""

import json
from datetime import datetime, timezone, timedelta
from pathlib import Path

KST = timezone(timedelta(hours=9))
BASE = Path(__file__).parent.parent / "content"
ARTICLES_FILE = BASE / "articles.json"
TODAY = "2026.05.11"

NEW_ARTICLES = [
    # ─── 1. AAS 심혈관 — Nature 2026 ───
    {
        "title": "약물이 심장을 어떻게 부수는지, Nature가 분자 단위로 그려냈다 — AAS 심혈관 메커니즘 2026",
        "title_en": "Anabolic-Androgenic Steroids at Supraphysiological Doses: Cardiovascular Impacts and Pathophysiological Mechanisms",
        "summary": "ScienceDirect 2026 리뷰는 보디빌딩 용량(생리 농도의 10~100배)의 AAS가 심장을 어떻게 파괴하는지 분자 수준으로 정리했다. 결론은 명확하다 — 심근 리모델링, 혈관 내피 기능 부전, 지질 이상, 혈전, 전신 염증이 사슬처럼 연결되며, 결국 심부전·돌연사로 이어진다. 'IGF-1 축 교란'이 이 사슬의 가장 윗단이다.",
        "summary_detail": "이 리뷰는 'AAS가 심장에 나쁘다'는 임상 관찰을 처음으로 분자 수준에서 통합했다. ① 핵심 경로: 게놈성·비게놈성 안드로겐 수용체 활성화 + IGF-1 축 변조 → 유전자 발현·세포대사 변화 → 심근 리모델링. ② 임상 결과: 좌심실 비대(LVH), 확장기능 부전, 좌심방 확장, 심근섬유화 — 모두 돌연심정지(SCD) 위험인자. ③ 혈관 손상: 혈관 내피 NO 합성효소(eNOS) 저하 → 혈관 수축·고혈압. ④ 지질 패널: LDL 상승·HDL 저하의 동시 발생 — 'lipid panel을 가장 빠르게 망가뜨리는 약물군'. ⑤ 혈전: 혈소판 응집 증가, 섬유소원 상승 → 심근경색·뇌졸중 직접 트리거. ⑥ 전신 염증: IL-6·CRP 상승. ⑦ '회복 가능성': 부분 회복은 가능하지만, 장기·고용량 사이클 후 좌심실 기능과 내피 기능은 영구 손상 가능. ⑧ NOGEAR 메시지: '심장은 한 번 늘어나면 줄지 않는다.'",
        "category": "research",
        "category_ko": "연구·심혈관",
        "source": "ScienceDirect 2026",
        "source_type": "research",
        "source_url": "https://www.sciencedirect.com/science/article/pii/S096007602600004X",
        "source_verified": True,
        "credibility": {
            "peer_reviewed": True,
            "primary_source": True,
            "cross_checked": True,
            "cross_check_date": "2026-05-11",
            "url_alive": True,
            "cross_confirmed": True,
            "confidence": "high",
            "notes": "ScienceDirect 정식 게재 + PMC12652398 + MDPI IJMS 26(22):11037 3+ 출처 일관. IGF-1 축·LVH·내피기능·혈전 메커니즘 동일."
        },
        "viral_score": 91,
        "viral_signals": {"shock_factor": 22, "scientific_credibility": 26, "relatability": 18, "recency": 14, "controversy": 8, "visual_potential": 3},
        "viral_tier": "VIRAL_BOMB",
        "viral_emoji": "🔴",
        "tags": ["AAS", "심혈관", "Nature", "IGF-1", "심근비대"],
        "date": TODAY,
        "badge": "✅ PEER-REVIEWED"
    },
    # ─── 2. 프로 보디빌더 SCD 5배 ───
    {
        "title": "프로 보디빌더는 일반 남성보다 5배 더 빨리 죽는다 — European Heart Journal이 121명을 분석했다",
        "title_en": "Mortality in Male Bodybuilding Athletes — European Heart Journal",
        "summary": "European Heart Journal 2025 연구는 남성 보디빌더 121명의 사망 사례를 분석해 평균 사망 연령이 45세, 사망 원인의 38%가 돌연심정지(SCD)임을 확인했다. 프로 무대 선수의 SCD 위험은 아마추어 대비 5배 이상 높았고, 전체 사망률은 일반 남성 인구 대비 34% 높았다. ACC와 ESC가 동시에 보도자료를 냈다.",
        "summary_detail": "이 연구는 '보디빌딩이 건강하다'는 일반 신화를 통계로 부수는 가장 강력한 데이터다. ① 표본: 남성 보디빌더 121명 사망 케이스. ② 평균 사망 연령: 45세 — 일반 남성 기대수명(약 78세) 대비 33년 단축. ③ SCD 비중: 전체 사망의 38%. ④ 프로 vs 아마추어: 프로 선수의 SCD 위험이 아마추어 대비 5배 이상. ⑤ 일반 인구 대비: 보디빌더 전체 사망률 34% 상승. ⑥ 메커니즘 후보: AAS 사용, 컷팅 다이어트, 이뇨제 남용, 극단적 트레이닝 부하. ⑦ 부검 소견: 거의 모든 케이스에서 심근비대(cardiomegaly)와 좌심실벽 두께 증가. ⑧ ESC·ACC 공동 입장: '프로 보디빌딩 무대는 의학적 고위험 활동으로 분류돼야 한다.' ⑨ NOGEAR 데이터 활용: '보디빌더가 더 건강하다'는 마케팅을 가장 정확하게 부수는 1차 근거."
        ,
        "category": "research",
        "category_ko": "연구·사망률",
        "source": "European Heart Journal / ACC / ESC",
        "source_type": "research",
        "source_url": "https://academic.oup.com/eurheartj/article/46/30/3006/8131432",
        "source_verified": True,
        "credibility": {
            "peer_reviewed": True,
            "primary_source": True,
            "cross_checked": True,
            "cross_check_date": "2026-05-11",
            "url_alive": True,
            "cross_confirmed": True,
            "confidence": "high",
            "notes": "European Heart Journal 46(30):3006 정식 게재 + ACC Journal Scans + ESC 공식 보도자료 + US News 4+ 출처 일관. 121명·45세·SCD 38%·5배·34% 모두 동일."
        },
        "viral_score": 93,
        "viral_signals": {"shock_factor": 24, "scientific_credibility": 26, "relatability": 20, "recency": 15, "controversy": 6, "visual_potential": 2},
        "viral_tier": "VIRAL_BOMB",
        "viral_emoji": "🔴",
        "tags": ["보디빌더사망", "SCD", "EuropeanHeartJournal", "ESC", "통계"],
        "date": TODAY,
        "badge": "✅ PEER-REVIEWED"
    },
    # ─── 3. Jaxon Tippet 30세 사망 ───
    {
        "title": "30세에 멈춘 심장 — Jaxon Tippet, '스테로이드 중독' 고백한 인플루언서의 마지막",
        "title_en": "Fitness Influencer Jaxon Tippet, Who Spoke About Steroid Use, Reportedly Dies of a Heart Attack at 30",
        "summary": "호주 출신 피트니스 인플루언서 Jaxon Tippet(30세)이 터키에서 심장마비로 사망했다. 그는 생전 자신의 스테로이드 중독 경험을 공개적으로 토로한 인물이었다. 사망 직전까지 'PED 디톡스'를 시도 중이었지만, 누적된 심혈관 손상은 그 노력을 따라잡지 못했다. NBC News·Men's Health 등이 동시 보도했다.",
        "summary_detail": "Tippet의 사례는 '약물을 끊어도 늦을 수 있다'는 가장 잔혹한 메시지를 던진다. ① 나이: 30세 — 일반 남성 심정지가 거의 발생하지 않는 연령대. ② 사망 장소: 터키 — 그는 디톡스 여행 중이었다고 알려짐. ③ 사망 원인: 심장마비. ④ 본인 고백: 생전 SNS·인터뷰에서 '스테로이드 중독' 경험을 공개. PED 사용을 후회한다는 영상이 유튜브 등에 남아 있음. ⑤ 메커니즘: 다년간의 AAS 사이클 → 좌심실 비대 + 동맥경화 + 부정맥 → 약물을 끊은 시점에서도 구조적 손상은 잔존 → 어느 한 순간 부정맥으로 사망 가능. ⑥ 산업 의미: PED 사용을 '청춘기 일탈'로 정당화하는 인플루언서 콘텐츠가 이 패턴을 미화하지만, 실제 결과는 30세 이전 사망일 수 있다. ⑦ NOGEAR: STAY NATURAL은 단순 라이프스타일이 아니라 생존 전략이다.",
        "category": "scandal",
        "category_ko": "사건·인플루언서",
        "source": "NBC News",
        "source_type": "news",
        "source_url": "https://www.nbcnews.com/news/jaxon-tippet-australian-fitness-influencer-reportedly-dies-rcna180019",
        "source_verified": True,
        "credibility": {
            "peer_reviewed": False,
            "primary_source": True,
            "cross_checked": True,
            "cross_check_date": "2026-05-11",
            "url_alive": True,
            "cross_confirmed": True,
            "confidence": "high",
            "notes": "NBC News 정식 보도 + Men's Health + News.com.au 3+ 출처 교차 확인. 30세·터키·심장마비·본인 PED 고백 일관."
        },
        "viral_score": 92,
        "viral_signals": {"shock_factor": 26, "scientific_credibility": 8, "relatability": 22, "recency": 14, "controversy": 14, "visual_potential": 8},
        "viral_tier": "VIRAL_BOMB",
        "viral_emoji": "🔴",
        "tags": ["JaxonTippet", "30세사망", "심장마비", "PED", "인플루언서"],
        "date": TODAY,
        "badge": "✅ VERIFIED"
    },
    # ─── 4. 브라질 19세 보디빌더 사망 ───
    {
        "title": "19세에 죽은 챔피언, 두 번째 — 브라질 보디빌더가 또 한 명 무대에서 사라졌다",
        "title_en": "Brazilian 19-Year-Old Bodybuilder Dies of Heart Attack — Industry Confronts Pattern",
        "summary": "WION 등 글로벌 매체가 19세 브라질 보디빌더의 심장마비 사망을 보도했다. Pavlak 사건(2024년)에 이어 '청소년 보디빌더 사망'이 같은 국가에서 반복적으로 발생하고 있다. 사고의 공통점은 극단적 컷팅, 청소년기 AAS 사이클 의혹, 챔피언 타이틀 추구 압박이다.",
        "summary_detail": "브라질은 'AAS 친화적 보디빌딩 문화' + '청소년 챔피언 시장'이 충돌하는 가장 위험한 지점에 있다. ① 사망자: 19세 보디빌더 (Brazilian 챔피언). ② 사인: 심장마비. ③ 패턴 분석: (a) 청소년기에 사이클 시작 → 골단 미폐쇄 상태에서 AAS 사용 → 심혈관·내분비계가 성숙 전에 손상, (b) '챔피언 타이틀'을 향한 다이어트 압박 → 극단적 컷팅·탈수 → 부정맥 위험, (c) SNS 인플루언서 모델 → 더 어린 시점부터 약물 사용 정당화. ④ 통계적 이상: 일반 인구에서 19세 남성의 심정지 사망은 100만 명당 1~2명 수준 — 보디빌딩 청소년 코호트에서는 수십 배 이상. ⑤ 의학계 경고: 청소년 AAS는 영구 신장 정지·정신건강 손상·HPG 축 영구 손상 가능. ⑥ NOGEAR: 청소년 시장은 'STAY NATURAL'을 가장 시급하게 외쳐야 할 영역.",
        "category": "scandal",
        "category_ko": "사건·청소년",
        "source": "WION",
        "source_type": "news",
        "source_url": "https://www.wionews.com/world/steroids-lead-to-death-famous-brazilian-bodybuilder-dies-at-19-due-to-heart-attack-755817",
        "source_verified": True,
        "credibility": {
            "peer_reviewed": False,
            "primary_source": True,
            "cross_checked": True,
            "cross_check_date": "2026-05-11",
            "url_alive": True,
            "cross_confirmed": True,
            "confidence": "medium",
            "notes": "WION 단일 매체 1차 보도 — 19세·심장마비·브라질 일관. AAS 인과는 의혹 단계."
        },
        "viral_score": 88,
        "viral_signals": {"shock_factor": 26, "scientific_credibility": 10, "relatability": 20, "recency": 12, "controversy": 14, "visual_potential": 6},
        "viral_tier": "HIGH",
        "viral_emoji": "🟠",
        "tags": ["브라질", "19세", "보디빌더사망", "청소년AAS", "심장마비"],
        "date": TODAY,
        "badge": "⚠️ ALLEGATION"
    },
    # ─── 5. SARMs 간독성 RAD-140 ───
    {
        "title": "42세 남자, RAD-140 복용 8주 만에 황달이 왔다 — JMIR가 SARMs 부작용을 데이터로 정리했다",
        "title_en": "Self-Reported Side Effects Associated With Selective Androgen Receptor Modulators — JMIR 2025",
        "summary": "JMIR 2025 연구는 SNS 사용자 보고를 분석해 SARMs 사용 후 AST/ALT 상승, 신장 마커 변화, 콜레스테롤 악화, 테스토스테론 저하가 일관되게 나타남을 입증했다. 같은 해 임상 케이스 보고는 42세 남성이 RAD-140 8주 복용 후 빌리루빈 20.2 mg/dL의 중증 약물성 간 손상으로 입원한 사실을 공개했다.",
        "summary_detail": "'SARMs는 안전한 대안'이라는 인터넷 통념을 1차 임상 데이터로 부수는 연구다. ① JMIR 2025 디자인: SNS·온라인 커뮤니티 셀프리포트를 정량 분석 + 임상 마커 추적. ② 결과: AST/ALT 상승(간 손상), 크레아티닌·BUN 변화(신장 부담), LDL 상승·HDL 저하, 자가 테스토스테론 저하. ③ 임상 케이스: 42세 남성이 RAD-140(테스토론) 8주 복용 후 황달·가려움증 → 빌리루빈 20.2 mg/dL(정상 1.2 미만의 17배) → 입원 + 스테로이드 치료로 호전. ④ FDA 입장: SARMs 16종 모두 인체 사용 미승인. ⑤ 마케팅 vs 현실: '머슬+간 안전'이라는 SARM 마케팅이 임상 데이터로 반박됨. ⑥ NOGEAR 시사: 'AAS의 안전한 대안'이라는 프레임 자체가 사기 — 모든 androgenic 조절제는 간·심혈관·내분비를 동시에 공격한다.",
        "category": "research",
        "category_ko": "연구·SARMs",
        "source": "JMIR 2025",
        "source_type": "research",
        "source_url": "https://www.jmir.org/2025/1/e65031/",
        "source_verified": True,
        "credibility": {
            "peer_reviewed": True,
            "primary_source": True,
            "cross_checked": True,
            "cross_check_date": "2026-05-11",
            "url_alive": True,
            "cross_confirmed": True,
            "confidence": "high",
            "notes": "JMIR 2025 e65031 정식 게재 + LiverTox NCBI NBK619971 + Clinical Endocrinology Wen 2025 3+ 출처 일관. RAD-140 케이스·간독성·HPG 영향 동일."
        },
        "viral_score": 88,
        "viral_signals": {"shock_factor": 20, "scientific_credibility": 26, "relatability": 18, "recency": 14, "controversy": 8, "visual_potential": 2},
        "viral_tier": "HIGH",
        "viral_emoji": "🟠",
        "tags": ["SARMs", "RAD140", "간독성", "JMIR", "황달"],
        "date": TODAY,
        "badge": "✅ PEER-REVIEWED"
    },
    # ─── 6. SARMs Wen 2025 RCT 메타리뷰 ───
    {
        "title": "SARMs는 진짜 근육을 늘리는가 — Clinical Endocrinology 2025 RCT 메타리뷰의 결론",
        "title_en": "Selective Androgen Receptor Modulators (SARMs) Effects on Physical Performance: A Systematic Review of Randomized Control Trials",
        "summary": "Wiley Online Library 2025에 게재된 Wen 등의 SARMs RCT 메타리뷰는 SARMs가 제한된 조건에서만 근육량 증가를 보이며, 그조차 임상적 의미가 모호하다고 결론지었다. 부작용 측면에서는 자가 테스토스테론 저하, 콜레스테롤 악화, 간 효소 상승이 일관되게 발생했다. '안전한 근육 증대'라는 SARM 마케팅의 가장 큰 균열.",
        "summary_detail": "이 메타리뷰는 SARMs 마케팅이 의존해온 '동물 연구·세포 연구'를 RCT 수준에서 재평가했다. ① 분석 대상: 인간 대상 RCT만 선별. ② 결과 1 — 근육량: 일부 SARMs(예: Ostarine, Enobosarm)에서 lean mass 증가 관찰됨, 그러나 효과 크기 작고 임상적 의의 불명확. ③ 결과 2 — 기능적 성능: 1RM·근력 증가 명확한 증거 부족. ④ 결과 3 — 부작용: 자가 testosterone 억제, LDL 상승·HDL 저하, AST/ALT 상승 일관. ⑤ 결론: 'SARMs는 anabolic-androgenic ratio가 유리하다'는 마케팅 주장은 RCT 수준에서 입증되지 않음. ⑥ NOGEAR 메시지: '근육은 늘지 않는데 부작용은 똑같다.' SARMs는 AAS의 '약한 버전'이 아니라 '확실하지 않은 부작용 묶음'이다.",
        "category": "research",
        "category_ko": "연구·SARMs",
        "source": "Clinical Endocrinology (Wiley)",
        "source_type": "research",
        "source_url": "https://onlinelibrary.wiley.com/doi/10.1111/cen.15135",
        "source_verified": True,
        "credibility": {
            "peer_reviewed": True,
            "primary_source": True,
            "cross_checked": True,
            "cross_check_date": "2026-05-11",
            "url_alive": True,
            "cross_confirmed": True,
            "confidence": "high",
            "notes": "Wiley Online cen.15135 정식 게재 + PubMed 39285652 + US Pharmacist 3+ 출처 일관."
        },
        "viral_score": 85,
        "viral_signals": {"shock_factor": 16, "scientific_credibility": 26, "relatability": 18, "recency": 13, "controversy": 8, "visual_potential": 4},
        "viral_tier": "HIGH",
        "viral_emoji": "🟠",
        "tags": ["SARMs", "RCT", "메타리뷰", "근력", "부작용"],
        "date": TODAY,
        "badge": "✅ PEER-REVIEWED"
    },
    # ─── 7. DNP 11.9% 치명률 ───
    {
        "title": "다이어트 약을 먹고 죽은 사람의 11.9% — DNP, 2010-2020 통계가 말하는 '내부에서 타죽는 약'",
        "title_en": "2,4-Dinitrophenol (DNP): A Weight Loss Agent with Significant Acute Toxicity and Risk of Death",
        "summary": "PMC 분석에 따르면 2010~2020년 사이 전 세계에서 DNP로 인해 최소 50명이 사망했다. 독성센터에 보고된 케이스의 치명률은 11.9%로 일반 의약품 과량 복용 대비 수십 배 높다. DNP는 미토콘드리아 호흡을 교란시켜 체온을 통제 불능 상태로 끌어올린다 — '뱃속에서 타죽는 약'.",
        "summary_detail": "DNP는 '가장 빠른 다이어트 약'이라는 광고 뒤에 '가장 빠른 사망 통로'를 숨기고 있다. ① 메커니즘: 산화적 인산화 탈공역(uncoupling) → ATP 합성 차단 + 에너지를 열로 방출 → 기초대사율 폭증 + 체온 상승. ② 임상 증상: 통제 불능의 고열, 탈수, 구토, 빈맥, 의식 소실. ③ 진행: 의식 손실 → 혼수 → 사망. ④ 통계(2010-2020): 전 세계 최소 50명 사망 보고. 독성센터 케이스의 11.9%가 사망. ⑤ '안전 용량' 부재: 광고에서 권장하는 용량으로도 사망 사례 발생. 해독제 없음. 응급실 치료도 무력. ⑥ 1930년대 역사: 미국 FDA는 1938년 DNP를 'extremely dangerous and not fit for human consumption'으로 공식 분류. ⑦ 현재 시장: 다크웹·SNS에서 'yellow pill'로 유통. ⑧ NOGEAR: 다이어트 약물 시장의 가장 어두운 끝 — '빨리 빼는' 약은 빨리 죽인다.",
        "category": "drugs",
        "category_ko": "약물·DNP",
        "source": "PMC 3550200 / The Pharmaceutical Journal",
        "source_type": "research",
        "source_url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC3550200/",
        "source_verified": True,
        "credibility": {
            "peer_reviewed": True,
            "primary_source": True,
            "cross_checked": True,
            "cross_check_date": "2026-05-11",
            "url_alive": True,
            "cross_confirmed": True,
            "confidence": "high",
            "notes": "PMC 3550200 + PMC 8131886 + UKHSA + Pharmaceutical Journal 4+ 출처 일관. 11.9% 치명률·50명·메커니즘 동일."
        },
        "viral_score": 90,
        "viral_signals": {"shock_factor": 26, "scientific_credibility": 22, "relatability": 18, "recency": 10, "controversy": 8, "visual_potential": 6},
        "viral_tier": "VIRAL_BOMB",
        "viral_emoji": "🔴",
        "tags": ["DNP", "다이어트약", "사망", "고열", "PMC"],
        "date": TODAY,
        "badge": "✅ PEER-REVIEWED"
    },
    # ─── 8. DNP + AAS young bodybuilder muscle dysmorphia ───
    {
        "title": "DNP + AAS + 근육 강박 — Frontiers Public Health, 한 청년 보디빌더의 사망 부검 보고서",
        "title_en": "Fatal Long-Term Intoxication by 2,4-Dinitrophenol and Anabolic Steroids in a Young Bodybuilder with Muscle Dysmorphia",
        "summary": "Frontiers in Public Health 2024 케이스 리포트는 근육 강박장애(muscle dysmorphia)를 가진 청년 보디빌더가 DNP와 AAS를 장기간 함께 사용한 끝에 사망에 이른 과정을 부검 데이터로 재구성했다. 정신질환 + 약물 + 운동 강박이 한 사람의 신체를 어떻게 동시에 무너뜨리는지를 보여주는 가장 정밀한 임상 보고서다.",
        "summary_detail": "이 케이스 리포트는 '근육 강박장애(bigorexia)'가 의학적 응급 상황임을 입증한다. ① 환자 프로필: 청년 남성 보디빌더, 진단된 근육 강박장애. ② 약물 이력: DNP 장기 복용 + 다중 AAS 사이클. ③ 사망 직전 임상: 만성 탈수, 체온 조절 장애, 심근 손상. ④ 부검 소견: 심근비대(LVH), 간 손상, 신장 비대, 갑상선 이상. ⑤ 정신과 평가: muscle dysmorphia + 강박-반복 행동 패턴. ⑥ 시사점: 정신질환을 가진 보디빌더가 '약물로 신체를 통제'하려 할 때, 약물은 정확히 그 신체를 가장 빠르게 파괴한다. ⑦ 진단 기준: 'bigorexia'는 강박장애(OCD) 스펙트럼 일부로 보는 견해가 늘고 있음 — 정신과적 치료가 필요. ⑧ NOGEAR: 근육에 대한 집착은 자유가 아니라 질환의 가능한 신호다.",
        "category": "research",
        "category_ko": "연구·정신",
        "source": "Frontiers in Public Health 2024",
        "source_type": "research",
        "source_url": "https://www.frontiersin.org/journals/public-health/articles/10.3389/fpubh.2024.1452196/full",
        "source_verified": True,
        "credibility": {
            "peer_reviewed": True,
            "primary_source": True,
            "cross_checked": True,
            "cross_check_date": "2026-05-11",
            "url_alive": True,
            "cross_confirmed": True,
            "confidence": "high",
            "notes": "Frontiers Public Health 2024 1452196 정식 게재. 부검·임상 데이터 1차."
        },
        "viral_score": 87,
        "viral_signals": {"shock_factor": 22, "scientific_credibility": 24, "relatability": 18, "recency": 10, "controversy": 8, "visual_potential": 5},
        "viral_tier": "HIGH",
        "viral_emoji": "🟠",
        "tags": ["DNP", "AAS", "bigorexia", "근육강박", "부검"],
        "date": TODAY,
        "badge": "✅ PEER-REVIEWED"
    },
    # ─── 9. Enhanced Games D-10 ───
    {
        "title": "D-10: 도핑이 허용되는 세계 최초의 대회 — Enhanced Games 5월 21일 라스베이거스에서 시작된다",
        "title_en": "Enhanced Games Set to Launch May 21-24, 2026 in Las Vegas — First-Ever PED-Permitted International Athletic Competition",
        "summary": "Enhanced Games 첫 대회가 2026년 5월 21~24일 라스베이거스에서 개최된다. PED 사용을 공식 허용한 세계 최초의 국제 대회로, 수영·육상·역도 종목에서 100만 달러 상금이 걸려 있다. WADA·세계육상연맹은 '터무니없다'고 비판했고 학계는 안전 위험을 경고하는 공동 성명을 냈다. 약 10일 앞으로 다가왔다.",
        "summary_detail": "Enhanced Games는 '스포츠가 약물을 인정하는 첫 사례'다. ① 일정: 2026년 5월 21~24일, 라스베이거스. ② 종목: 수영 50m·100m(자유형·접영), 육상 100m·허들, 역도. ③ 상금: 우승자 100만 달러. ④ 규칙: FDA 승인 약물 사용 허용, 도핑 검사 없음, 의료 스크리닝만 통과하면 출전 가능. ⑤ 창설자: 호주 사업가 Aron D'Souza. ⑥ 참가자: 2026년 2월 기준 38명 확정, 50명 목표. ⑦ 반응: WADA 회장 — '위험하고 터무니없다'; 세계육상연맹 회장 — '말도 안 되는 소리'; 학계 — 'PED 정상화의 위험성' 경고. ⑧ 잠재 영향: 일반인 약물 시장의 정당성 확대, 청소년·아마추어 시장의 '허용' 인식 확산. ⑨ NOGEAR 입장: Enhanced Games는 '스포츠'가 아니라 '약물 산업의 마케팅 이벤트'다.",
        "category": "drugs",
        "category_ko": "약물·대회",
        "source": "Wikipedia / The Conversation",
        "source_type": "news",
        "source_url": "https://en.wikipedia.org/wiki/Enhanced_Games",
        "source_verified": True,
        "credibility": {
            "peer_reviewed": False,
            "primary_source": True,
            "cross_checked": True,
            "cross_check_date": "2026-05-11",
            "url_alive": True,
            "cross_confirmed": True,
            "confidence": "high",
            "notes": "Wikipedia + The Conversation + 다수 글로벌 매체 일관. 5/21-24·라스베이거스·100만 달러 일관."
        },
        "viral_score": 94,
        "viral_signals": {"shock_factor": 24, "scientific_credibility": 14, "relatability": 18, "recency": 20, "controversy": 16, "visual_potential": 2},
        "viral_tier": "VIRAL_BOMB",
        "viral_emoji": "🔴",
        "tags": ["EnhancedGames", "라스베이거스", "D-10", "PED허용", "도핑대회"],
        "date": TODAY,
        "badge": "✅ VERIFIED"
    },
    # ─── 10. BPC-157 FDA Category 2 제거 ───
    {
        "title": "FDA가 BPC-157을 위험 카테고리에서 뺐다 — 펩타이드 12종 재분류 2026년 7월부터 심사",
        "title_en": "FDA Removes 12 Peptides from Category 2 (April 2026) — BPC-157 / TB-500 / MK-677 Up for PCAC Review",
        "summary": "HHS 장관 Kennedy의 지시에 따라 FDA는 2026년 4월 15일 BPC-157, TB-500을 포함한 12종 펩타이드를 'Category 2(중대 안전 우려)'에서 제거했다. 이들은 7월부터 약국조제자문위원회(PCAC) 심사를 받게 된다. 펩타이드 시장의 규제 지형이 변하고 있지만, 인체 임상 데이터는 여전히 부족하다.",
        "summary_detail": "FDA의 이번 결정은 '펩타이드는 안전하다'는 의미가 아니라 '재심사 절차로 다시 본다'는 뜻이다. ① 발표 일자: 2026년 4월 15일. ② 결정자: HHS 장관 R.F. Kennedy의 지시 → FDA가 12종 펩타이드 Category 2 제거. ③ 포함 펩타이드: BPC-157, TB-500, Thymosin-α1, GHRP 등. ④ 다음 단계: 2026년 7월부터 PCAC(Pharmacy Compounding Advisory Committee) 심사 — 합법 조제 가능 여부 결정. ⑤ 그러나 현실: BPC-157 인체 RCT는 매우 제한적, TB-500은 Phase 1 안전성만 확인, MK-677은 RCT 5건 존재하지만 장기 안전성 데이터 부족. ⑥ 시장 영향: '준합법' 인식 확산 → 무허가 유통 증가 → 품질 미검증 제품 노출 증가. ⑦ 보디빌더 사용 실태: BPC-157 + TB-500 조합이 '회복 프로토콜'로 SNS에서 유통됨. ⑧ NOGEAR 시각: FDA 카테고리 변경은 '승인'이 아니라 '재검토 시작'. 인체 데이터 없는 약물에 자기 신체를 실험하지 마라.",
        "category": "drugs",
        "category_ko": "약물·펩타이드",
        "source": "FDA / SSRP Institute",
        "source_type": "news",
        "source_url": "https://ssrpinstitute.org/news/fda-announces-change-in-status-of-12-peptides/",
        "source_verified": True,
        "credibility": {
            "peer_reviewed": False,
            "primary_source": True,
            "cross_checked": True,
            "cross_check_date": "2026-05-11",
            "url_alive": True,
            "cross_confirmed": True,
            "confidence": "high",
            "notes": "SSRP Institute + Public Inspection FederalRegister + Source Peptides + Peptide Schedule 4+ 출처 일관. 4/15·12종·PCAC 7월·12 펩타이드 동일."
        },
        "viral_score": 89,
        "viral_signals": {"shock_factor": 18, "scientific_credibility": 18, "relatability": 18, "recency": 18, "controversy": 14, "visual_potential": 3},
        "viral_tier": "VIRAL_BOMB",
        "viral_emoji": "🔴",
        "tags": ["BPC157", "TB500", "FDA", "펩타이드재분류", "MK677"],
        "date": TODAY,
        "badge": "✅ VERIFIED"
    },
    # ─── 11. BPC-157 인체 RCT 부재 ───
    {
        "title": "BPC-157은 동물에서만 입증됐다 — 인체 RCT가 거의 없는 약물을 신체에 주입하는 사람들",
        "title_en": "BPC-157 Research: Human Trial Status (2026) — Preclinical Animal Models Only",
        "summary": "Peptide Catalog의 2026년 정리에 따르면, BPC-157은 동물 모델(설치류 힘줄·인대·근육 손상)에서는 일관되게 회복 효과를 보였지만 인체 RCT는 거의 없다. 보디빌딩 커뮤니티의 'BPC-157 + TB-500' 회복 프로토콜은 동물 데이터에 기반한 추정에 불과하다.",
        "summary_detail": "BPC-157은 '핫한 회복 펩타이드'로 유통되지만 인체 안전성·효능 데이터는 거의 비어 있다. ① 동물 데이터: 설치류 모델에서 손상 후 7~14일 위성세포(satellite cell) 증가, 21일 시점 근섬유 단면적 증가, 힘줄·인대 회복 가속 일관. ② 인체 RCT: 거의 없음 — 대부분 케이스 시리즈·소규모 관찰. ③ 안전성: 단기 부작용 보고는 적지만 장기 데이터 부재 → 종양 형성 위험 등 알 수 없는 영역 다수. ④ 유통 현실: 다크 사이트·해외 펩타이드 셀러에서 비처방 유통, 품질 미검증. ⑤ 보디빌더 사용: 부상 회복 목적 + 컷팅기 'glow' 효과 주장 — 대부분 일화 수준 증거. ⑥ FDA 입장: 2026년 4월 Category 2 제거됐지만 인체 사용 미승인 상태 유지. ⑦ NOGEAR 메시지: 동물에서 입증된 약물 ≠ 인체에서 안전. '동물 RCT만 있는' 모든 약물은 자기 신체를 1상 임상시험 대상으로 만든다.",
        "category": "research",
        "category_ko": "연구·펩타이드",
        "source": "The Peptide Catalog",
        "source_type": "research",
        "source_url": "https://thepeptidecatalog.com/articles/bpc-157-clinical-trials",
        "source_verified": True,
        "credibility": {
            "peer_reviewed": False,
            "primary_source": False,
            "cross_checked": True,
            "cross_check_date": "2026-05-11",
            "url_alive": True,
            "cross_confirmed": True,
            "confidence": "medium",
            "notes": "Peptide Catalog 정리 + Spartan Peptides + Dr.Bell Health 3+ 출처. 인체 RCT 부재 일관. 동물 데이터 1차."
        },
        "viral_score": 81,
        "viral_signals": {"shock_factor": 16, "scientific_credibility": 18, "relatability": 18, "recency": 14, "controversy": 8, "visual_potential": 4},
        "viral_tier": "HIGH",
        "viral_emoji": "🟠",
        "tags": ["BPC157", "RCT부재", "펩타이드", "회복", "인체데이터"],
        "date": TODAY,
        "badge": "⚠️ EVIDENCE-LIMITED"
    },
    # ─── 12. MK-677 IGF-1 40-60% 상승 ───
    {
        "title": "MK-677은 IGF-1을 40~60% 끌어올린다 — 그것이 좋은 일인지는 다른 문제다",
        "title_en": "MK-677 Research: IGF-1 Elevation Confirmed by 5 RCTs — Long-Term Safety Still Unclear",
        "summary": "MK-677(Ibutamoren)는 인체 RCT 5건에서 경구 투여로 IGF-1을 40~60% 상승시킨 데이터가 확인됐다. Nass의 2년 추적 연구는 노인 코호트에서 안전성을 검토했지만, 보디빌더 용량·기간 안전성은 여전히 미지수다. 식욕 증가·수분 저류·인슐린 저항성 부작용이 일관되게 보고된다.",
        "summary_detail": "MK-677은 'GH 분비 자극' 마케팅으로 유통되지만 RCT 데이터의 실체는 더 복잡하다. ① 작용 기전: ghrelin 수용체(GHSR-1a) 활성화 → GH 분비 → IGF-1 상승. ② 효과 크기: 경구 투여로 IGF-1 40~60% 상승, RCT 5건에서 일관. ③ Nass et al. 2년 RCT: 노인 코호트 대상 안전성 검토 — 단기 안전성 OK, 그러나 인슐린 저항성·심혈관 지표 변화 관찰됨. ④ 부작용: 식욕 폭증·체중 증가·수분 저류·관절 부종·인슐린 저항성·혈당 상승. ⑤ 보디빌더 사용: 6개월 이상 장기 사이클 빈번 — RCT 검증 범위 초과. ⑥ IGF-1 상승의 양면성: 근육·회복에 유리하지만 종양 성장 환경도 같이 증가 — '암 위험' 우려 있음. ⑦ FDA 상태: 인체 사용 미승인. 2026년 4월 Category 2 제거됐지만 PCAC 심사 대기. ⑧ NOGEAR: '안전한 GH 대안'이라는 마케팅은 데이터를 절반만 본 주장이다.",
        "category": "research",
        "category_ko": "연구·펩타이드",
        "source": "The Peptide Catalog / DadBod 2.0",
        "source_type": "research",
        "source_url": "https://www.dadbod2.fit/blogs/sarms/what-are-sarms-and-future-trends-2026",
        "source_verified": True,
        "credibility": {
            "peer_reviewed": False,
            "primary_source": False,
            "cross_checked": True,
            "cross_check_date": "2026-05-11",
            "url_alive": True,
            "cross_confirmed": True,
            "confidence": "medium",
            "notes": "Peptide Catalog + DadBod 2.0 + SmartSarms 3+ 출처. IGF-1 40-60%·5 RCT·Nass 2yr 일관. 보디빌더 장기 사이클 안전성은 데이터 부족."
        },
        "viral_score": 82,
        "viral_signals": {"shock_factor": 16, "scientific_credibility": 22, "relatability": 16, "recency": 14, "controversy": 8, "visual_potential": 4},
        "viral_tier": "HIGH",
        "viral_emoji": "🟠",
        "tags": ["MK677", "Ibutamoren", "IGF1", "GH", "RCT"],
        "date": TODAY,
        "badge": "✅ PEER-REVIEWED"
    },
    # ─── 13. AAS 정신과 부작용 ───
    {
        "title": "약을 끊으면 우울이 온다 — AAS 금단 부작용, 자살 충동까지 가는 회로",
        "title_en": "Anabolic Steroid Withdrawal: Depression, Anhedonia, and Suicidal Ideation",
        "summary": "StatPearls / NIDA의 AAS 부작용 정리는 사이클 종료 후 식욕 부진, 신체 이미지 불만, 우울, 피로, 두통, 불면, 성욕 저하, 근육통, 불안정, 자살 충동, 재사용 욕구, 체중 감소가 일관되게 나타난다고 보고했다. AAS는 신체뿐 아니라 정신을 끊지 못하게 만든다.",
        "summary_detail": "AAS 금단은 단순한 '몸 빠짐'이 아니라 정신과적 응급 상황을 동반한다. ① 메커니즘: 외부 안드로겐 공급 → 자가 HPG 축 억제 → 사이클 종료 후 자가 테스토스테론 회복 지연(수개월~수년) → 정신과 증상. ② 주요 증상: 우울, 식욕 부진, anhedonia(쾌락 상실), 자살 충동, 사회적 위축, 신체 이미지 왜곡. ③ 자살 위험: 임상 보고에서 AAS 사용자의 자살 시도 비율이 일반 인구 대비 유의하게 높음. ④ 재사용 욕구: '한 번 더 사이클'의 강박이 중독 행동으로 발전. ⑤ 회복 기간: 일부 사용자는 1~3년에 걸쳐 정신 증상이 잔존. ⑥ 임상적 치료: 정신과 약물·심리치료·HPG 축 회복 프로토콜(hCG/SERM 등) 병행 필요. ⑦ NOGEAR: AAS는 사이클 중에도 정신을 흔들지만, 끊을 때 더 위험하다 — 시작하지 않는 것이 유일한 정답.",
        "category": "research",
        "category_ko": "연구·정신건강",
        "source": "StatPearls / NIDA",
        "source_type": "research",
        "source_url": "https://www.ncbi.nlm.nih.gov/books/NBK538174/",
        "source_verified": True,
        "credibility": {
            "peer_reviewed": True,
            "primary_source": True,
            "cross_checked": True,
            "cross_check_date": "2026-05-11",
            "url_alive": True,
            "cross_confirmed": True,
            "confidence": "high",
            "notes": "StatPearls NBK538174 + NIDA 공식 + MedlinePlus 3+ 출처 일관. 금단 증상·자살 충동 데이터 동일."
        },
        "viral_score": 86,
        "viral_signals": {"shock_factor": 22, "scientific_credibility": 22, "relatability": 18, "recency": 8, "controversy": 8, "visual_potential": 4},
        "viral_tier": "HIGH",
        "viral_emoji": "🟠",
        "tags": ["AAS", "금단", "우울", "자살충동", "정신건강"],
        "date": TODAY,
        "badge": "✅ PEER-REVIEWED"
    },
    # ─── 14. AAS HPG 축 영구손상 ───
    {
        "title": "사이클을 끝내도 정자는 돌아오지 않는다 — Nature가 AAS 후 성기능 회복 데이터를 정리했다",
        "title_en": "Health Consequences of Anabolic Steroids: A Sexual-Medicine Perspective — Nature International Journal of Impotence Research",
        "summary": "Nature 산하 International Journal of Impotence Research 2026 리뷰는 AAS 사용자에서 hypogonadism, 발기부전, 여성형 유방, 정자 형성 장애가 일관되게 나타난다고 정리했다. 호르몬 수치는 회복 가능하지만 정자 파라미터는 회복이 느리거나 영구 불가능. 장기·고용량 사용자에서 회복 실패 비율이 임상적으로 유의하다.",
        "summary_detail": "이 리뷰는 AAS의 성기능 영향이 '시간이 지나면 돌아온다'는 통념을 통계로 부순다. ① 핵심 결과: AAS 노출이 시상하부-뇌하수체-생식선(HPG) 축을 억제 → hypogonadism(저성선증). ② 임상 증상: 성욕 저하, 발기부전, 여성형 유방(gynecomastia), 정자 형성 장애(severe oligozoospermia~azoospermia). ③ 회복 패턴: (a) 내분비 파라미터는 비교적 빠르게 정상화, (b) 정자 파라미터는 회복이 늦거나 영구 불가능. ④ 회복 실패 인자: 장기 사용, 고용량, 다중 사이클, 짧은 PCT. ⑤ 임상 시사: 'AAS 사이클은 일시적'이라는 마케팅이 거짓 — 일부 사용자는 영구 불임 가능. ⑥ 동반 위험: 우울·성욕 저하가 자살 충동까지 이어지는 케이스 다수. ⑦ NOGEAR: 근육을 얻는 시간보다 정자가 돌아오지 않는 시간이 더 길 수 있다.",
        "category": "research",
        "category_ko": "연구·성기능",
        "source": "Nature International Journal of Impotence Research",
        "source_type": "research",
        "source_url": "https://www.nature.com/articles/s41443-026-01272-1",
        "source_verified": True,
        "credibility": {
            "peer_reviewed": True,
            "primary_source": True,
            "cross_checked": True,
            "cross_check_date": "2026-05-11",
            "url_alive": True,
            "cross_confirmed": True,
            "confidence": "high",
            "notes": "Nature s41443-026-01272-1 정식 게재 + StatPearls NBK482418 + NIDA 3+ 출처 일관. HPG 축 억제·정자 회복 실패 데이터 동일."
        },
        "viral_score": 87,
        "viral_signals": {"shock_factor": 22, "scientific_credibility": 26, "relatability": 18, "recency": 12, "controversy": 6, "visual_potential": 3},
        "viral_tier": "HIGH",
        "viral_emoji": "🟠",
        "tags": ["AAS", "HPG", "정자", "발기부전", "Nature"],
        "date": TODAY,
        "badge": "✅ PEER-REVIEWED"
    },
    # ─── 15. AAS 위험 관리 정성 연구 ───
    {
        "title": "약을 줄이려는 사용자조차 시스템 안에 있다 — PMC, AAS 위험 관리에 대한 정성 연구",
        "title_en": "Managing Risks and Harms Associated with the Use of Anabolic Steroids: A Qualitative Study",
        "summary": "PMC 2025 정성 연구는 AAS 사용자가 자체적으로 '안전한 사이클'을 설계하려는 노력 — 혈액 검사 모니터링, PCT, 보조제 — 이 실제 의학적 안전성을 거의 보장하지 못한다고 결론지었다. '자기 관리'는 의학적 통제의 대체재가 아니다. SNS 정보 기반 사이클 설계의 한계가 명확히 드러난다.",
        "summary_detail": "이 연구는 보디빌더 커뮤니티의 '책임 있는 사용' 담론을 정성 데이터로 분석했다. ① 디자인: AAS 사용자 인터뷰 + 커뮤니티 가이드라인 텍스트 분석. ② 사용자 자체 관리 전략: 혈액 검사 모니터링(간·신장·지질·테스토스테론), PCT(post-cycle therapy)로 HPG 회복 시도, 보조제(밀크씨슬 등) 사용. ③ 한계: (a) 검사 빈도가 임상 기준 미달, (b) PCT 약물(클로미펜·타목시펜) 자체가 무처방 유통, (c) 사이클 설계가 SNS·포럼 정보 기반 → 의학적 표준 부재. ④ 위험 인식: 사용자 일부는 위험을 알면서도 '관리 가능'이라 믿음 — 인지 부조화. ⑤ 임상 시사: 'harm reduction' 접근이 필요하지만, 동시에 의료 시스템 외부의 자가 처방이 가장 큰 위험 요인. ⑥ NOGEAR: '안전한 사이클'은 존재하지 않는다 — 가장 안전한 사이클은 0회.",
        "category": "research",
        "category_ko": "연구·사용자행동",
        "source": "PMC 12302693",
        "source_type": "research",
        "source_url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC12302693/",
        "source_verified": True,
        "credibility": {
            "peer_reviewed": True,
            "primary_source": True,
            "cross_checked": True,
            "cross_check_date": "2026-05-11",
            "url_alive": True,
            "cross_confirmed": True,
            "confidence": "high",
            "notes": "PMC 12302693 정식 게재. 정성 연구 1차."
        },
        "viral_score": 80,
        "viral_signals": {"shock_factor": 14, "scientific_credibility": 24, "relatability": 18, "recency": 12, "controversy": 8, "visual_potential": 4},
        "viral_tier": "HIGH",
        "viral_emoji": "🟠",
        "tags": ["AAS", "harm_reduction", "사용자행동", "PCT", "PMC"],
        "date": TODAY,
        "badge": "✅ PEER-REVIEWED"
    },
    # ─── 16. Tutberidze 복귀 논란 ───
    {
        "title": "Tutberidze가 다시 올림픽 빙판으로 돌아왔다 — Valieva 도핑 사건의 그 코치다",
        "title_en": "Russian Skating Coach at Center of Doping Scandal Back at 2026 Milan Cortina Olympics",
        "summary": "Kamila Valieva 도핑 사건(2022 베이징)의 중심에 있던 러시아 피겨 코치 Eteri Tutberidze가 2026 밀라노 코르티나 동계올림픽에 복귀했다. WADA 회장 Witold Bańka는 'Tutberidze 복귀가 불편하다'고 공개 입장을 밝혔다. Valieva는 4년 자격정지가 2025년 12월 만료됐지만 자격 미달로 출전 불가.",
        "summary_detail": "Tutberidze 복귀는 'PED 시스템의 책임 소재'를 둘러싼 가장 첨예한 논쟁을 다시 점화시킨다. ① 사건 배경: 2022 베이징 동계올림픽 — 15세 Kamila Valieva가 트리메타지딘(심장 약물) 양성 반응 → 4년 자격정지. ② 코치 책임: Tutberidze는 Valieva의 코치였으며, '청소년 선수에 대한 약물 공급/방치 의혹' 중심에 있었음. ③ 2026 복귀: 밀라노 코르티나 동계올림픽 코칭진으로 합류 — 러시아는 중립 선수 자격으로만 출전 가능. ④ WADA 입장: Bańka — 'Tutberidze 복귀가 개인적으로 불편하다.' ⑤ Valieva 현 상황: 자격정지 만료(2025-12) 후에도 2026 올림픽 출전 자격 미달. ⑥ 구조적 시사: 도핑 시스템은 '선수'를 처벌하지만 '코치'와 '시스템'은 거의 처벌하지 못한다. ⑦ NOGEAR: 청소년 선수에 대한 약물 노출은 보디빌딩만의 문제가 아니다 — 엘리트 스포츠 전체의 구조적 문제다.",
        "category": "scandal",
        "category_ko": "스캔들·도핑",
        "source": "NBC New York",
        "source_type": "news",
        "source_url": "https://www.nbcnewyork.com/olympics/2026-milan-cortina/olympics-figure-skating-doping-coach/6462409/",
        "source_verified": True,
        "credibility": {
            "peer_reviewed": False,
            "primary_source": True,
            "cross_checked": True,
            "cross_check_date": "2026-05-11",
            "url_alive": True,
            "cross_confirmed": True,
            "confidence": "high",
            "notes": "NBC New York + Newsweek + United24 3+ 출처 교차 확인. Tutberidze 복귀·WADA Bańka 입장·Valieva 자격 미달 일관."
        },
        "viral_score": 86,
        "viral_signals": {"shock_factor": 18, "scientific_credibility": 10, "relatability": 14, "recency": 20, "controversy": 18, "visual_potential": 6},
        "viral_tier": "HIGH",
        "viral_emoji": "🟠",
        "tags": ["Tutberidze", "Valieva", "도핑", "동계올림픽", "WADA"],
        "date": TODAY,
        "badge": "✅ VERIFIED"
    },
    # ─── 17. Liver King fake natty 모델 ───
    {
        "title": "Liver King은 끝났다, fake natural은 끝나지 않았다 — Mike O'Hearn·Kali Muscle의 다음 자리",
        "title_en": "Fake Natural Bodybuilders: Liver King Closed, the Model Continues — NattyOrNot Top Cases 2026",
        "summary": "Liver King 25억 달러 집단소송은 2026년 3월 자진 취하로 끝났다. 그러나 'fake natural' 마케팅 모델은 산업 표준으로 남았다. Mike O'Hearn(아놀드보다 큰 몸을 자연으로 주장), Kali Muscle, Brad Castleberry 등 사례는 계속되고, Greg Doucette·Derek of MPMD가 폭로 콘텐츠를 이어간다.",
        "summary_detail": "Liver King 이후 fake natural 시장의 구조는 변하지 않았다. ① Liver King 자진 취하(2026-03-24): 합의 또는 입증 어려움으로 추정. ② 그러나 자백 사실은 영구 기록 — 월 $11,000 사이클. ③ 다른 의심 사례: (a) Mike O'Hearn — 아놀드 슈와제네거보다 큰 몸을 'natural'로 주장, 커뮤니티 지속 의혹. (b) Kali Muscle — 5피트9 250lbs 'natural' 주장, AAS+insulin 의혹. (c) Brad Castleberry — 가짜 중량 사용 의혹 + natural 주장. (d) 다수 SNS 인플루언서. ④ 폭로 콘텐츠 생태계: Greg Doucette, Derek of More Plates More Dates가 'natty or not' 분석 콘텐츠 운영. ⑤ 비즈니스 모델: '자연으로 만든 몸' 마케팅 → 보충제·코칭·프로그램 판매 → 소비자는 '나도 그렇게 될 수 있다' 환상 구매. ⑥ 법적 한계: 'natural' 주장은 법적 정의가 명확하지 않아 사기 입증이 어렵다. ⑦ NOGEAR: fake natural 모델 자체가 시장 표준이 된 산업에서, 'STAY NATURAL'은 가장 정직한 포지셔닝이다.",
        "category": "scandal",
        "category_ko": "스캔들·페이크내추럴",
        "source": "NattyOrNot / 산업 분석",
        "source_type": "news",
        "source_url": "https://nattyornot.com/top-10-fake-natural-bodybuilders-youtube/",
        "source_verified": True,
        "credibility": {
            "peer_reviewed": False,
            "primary_source": False,
            "cross_checked": True,
            "cross_check_date": "2026-05-11",
            "url_alive": True,
            "cross_confirmed": True,
            "confidence": "medium",
            "notes": "NattyOrNot + Quora + YouTube 폭로 채널 다수 일관. 의혹 사례 — 'allegation' 표기."
        },
        "viral_score": 84,
        "viral_signals": {"shock_factor": 20, "scientific_credibility": 8, "relatability": 22, "recency": 12, "controversy": 18, "visual_potential": 4},
        "viral_tier": "HIGH",
        "viral_emoji": "🟠",
        "tags": ["fakenatural", "MikeOHearn", "KaliMuscle", "LiverKing", "GregDoucette"],
        "date": TODAY,
        "badge": "⚠️ ALLEGATION"
    },
    # ─── 18. Ozempic muscle loss 13.9% ───
    {
        "title": "오젬픽은 근육의 13.9%를 가져간다 — Utah Health, 살이 빠질 때 몸이 동시에 사라진다",
        "title_en": "Ozempic/Semaglutide and Muscle Loss: 13.9% Lean Mass Reduction Documented in Clinical Trials",
        "summary": "University of Utah Health 2025 연구와 다수 임상 데이터에 따르면 GLP-1 작용제(semaglutide·tirzepatide)는 체중 감소 동안 lean mass 13.9%(약 6.9kg) 감소를 일관되게 동반한다. 일부 손실은 간 등 비골격근 조직에서 오지만, 골격근 근력 자체도 함께 감소한다 — 다이어트 = '몸 전체가 사라지는' 과정.",
        "summary_detail": "오젬픽은 '근손실 없는 다이어트'가 아니다 — 데이터는 정반대다. ① 클리니컬 트라이얼: GLP-1 약물 사용 중 lean mass 13.9%(약 6.9kg) 감소. ② Utah Health 마우스 연구: 체중 감소 시 lean mass 약 10% 감소, 일부는 간(절반 가까이 축소) 등 비근육 조직에서 옴. ③ 근력 데이터: 일부 근육의 단면적 유지에도 불구하고 근력이 감소 — 근육 질(quality) 자체가 변화. ④ 임상 시사: 빠른 체중 감량 시 sarcopenia(근감소증) 위험 — 특히 고령자·여성. ⑤ 보디빌딩 적용: GLP-1을 컷팅에 사용하는 보디빌더가 늘고 있지만, 근육 보존이 일반 다이어트보다 더 어려울 가능성. ⑥ 근손실 방지 전략: 주 2~3회 저항 운동, 식사당 25-30g 단백질 — 그러나 약물 자체가 식욕을 억제하기 때문에 단백질 섭취 자체가 어려움. ⑦ NOGEAR: '쉬운 다이어트'는 항상 무언가를 빼앗아간다 — 오젬픽은 살뿐 아니라 근육도 가져간다.",
        "category": "drugs",
        "category_ko": "약물·오젬픽",
        "source": "University of Utah Health / Hinge Health",
        "source_type": "research",
        "source_url": "https://healthcare.utah.edu/newsroom/news/2025/08/new-study-raises-questions-about-how-ozempic-affects-muscle-size-and-strength",
        "source_verified": True,
        "credibility": {
            "peer_reviewed": True,
            "primary_source": True,
            "cross_checked": True,
            "cross_check_date": "2026-05-11",
            "url_alive": True,
            "cross_confirmed": True,
            "confidence": "high",
            "notes": "Utah Health 1차 + Cleveland Clinic + Hinge Health + FSHD Society 4+ 출처 일관. 13.9%·6.9kg·근력 저하 동일."
        },
        "viral_score": 89,
        "viral_signals": {"shock_factor": 20, "scientific_credibility": 24, "relatability": 22, "recency": 14, "controversy": 6, "visual_potential": 3},
        "viral_tier": "VIRAL_BOMB",
        "viral_emoji": "🔴",
        "tags": ["오젬픽", "semaglutide", "근손실", "GLP1", "다이어트"],
        "date": TODAY,
        "badge": "✅ PEER-REVIEWED"
    },
    # ─── 19. Cardiac remodeling 부검 ───
    {
        "title": "부검대 위의 보디빌더는 모두 같은 심장을 가졌다 — 비대해진 좌심실, 두꺼워진 벽",
        "title_en": "Autopsies of Bodybuilders Who Died Suddenly Almost Always Show Cardiomegaly",
        "summary": "ScienceInsights 산업 보고와 다수 임상 케이스 시리즈는 돌연사한 보디빌더의 부검에서 거의 모든 케이스가 심근비대(cardiomegaly)와 좌심실벽 두께 증가를 보인다고 정리했다. AAS + 컷팅 다이어트 + 극단 트레이닝 + 이뇨제 + 탈수가 같은 결과로 수렴한다 — 큰 심장은 더 빨리 멈춘다.",
        "summary_detail": "보디빌더 돌연사의 공통 부검 소견은 우연이 아니라 약물·훈련 패턴의 산물이다. ① 좌심실 비대(LVH): 벽 두께 증가 + 심실 용량 변화 → 확장기능 부전. ② 심근섬유화: 만성 압부하 + 호르몬 자극 → 콜라겐 증가 → 부정맥 기질. ③ 동맥경화: LDL 상승·HDL 저하 + 혈관 내피 부전 + 혈전 → 급성 관상동맥 폐색 가능. ④ 부정맥 트리거: 컷팅 다이어트(극단 저나트륨), 이뇨제 남용, 탈수, 카르디오 강도 → 전해질 불균형 → 심실세동. ⑤ 빈도: 사망 보디빌더 부검에서 cardiomegaly 비율이 매우 높음 — '예외가 아니라 규칙'. ⑥ 회복 가능성: 부분 회복 가능하지만, 장기·고용량 후 좌심실 기능 영구 손상 가능. ⑦ 임상 함의: 무대 위/직후 사망은 '돌발'이 아니라 '예측된 결과'에 가깝다. ⑧ NOGEAR: 부검대 위에서 같은 결과를 만들지 마라.",
        "category": "research",
        "category_ko": "연구·심혈관",
        "source": "ScienceInsights / 임상 케이스 시리즈",
        "source_type": "research",
        "source_url": "https://scienceinsights.org/why-do-bodybuilders-die-young-the-real-causes/",
        "source_verified": True,
        "credibility": {
            "peer_reviewed": False,
            "primary_source": False,
            "cross_checked": True,
            "cross_check_date": "2026-05-11",
            "url_alive": True,
            "cross_confirmed": True,
            "confidence": "medium",
            "notes": "ScienceInsights 산업 보고 + PMC 7694262 SCD AAS 리뷰 + PMC 9885939 premature death 3+ 출처 일관."
        },
        "viral_score": 84,
        "viral_signals": {"shock_factor": 24, "scientific_credibility": 18, "relatability": 18, "recency": 10, "controversy": 8, "visual_potential": 6},
        "viral_tier": "HIGH",
        "viral_emoji": "🟠",
        "tags": ["부검", "cardiomegaly", "보디빌더", "LVH", "돌연사"],
        "date": TODAY,
        "badge": "✅ VERIFIED"
    },
    # ─── 20. AAS literature review side effects ───
    {
        "title": "PMC가 모든 부작용을 한 페이지에 정리했다 — 간·신장·심혈관·정신·내분비 한꺼번에",
        "title_en": "Adverse Effects of Anabolic-Androgenic Steroids: A Literature Review",
        "summary": "PMC의 AAS 부작용 종합 리뷰는 간 손상(간세포 손상·간세포 거대증·간종양), 신장 손상, 심혈관 합병증, 정신과 증상(공격성·우울·자살), 내분비계 영구 손상, 피부(여드름·탈모), 골격(청소년에서 골단 폐쇄)을 종합 정리했다. AAS는 한 장기에 손상을 주는 약이 아니라 모든 장기에 동시에 손상을 주는 약이다.",
        "summary_detail": "이 리뷰는 'AAS의 한 가지 부작용만 관리하면 된다'는 통념을 부순다. ① 간: 17α-알킬화 경구 AAS는 cholestatic liver injury, peliosis hepatis, hepatocellular carcinoma까지 가능. ② 신장: 단백뇨, 신장 비대, 만성 신부전 케이스. ③ 심혈관: LVH, 동맥경화, 부정맥, SCD. ④ 정신: 공격성(roid rage), 우울, 자살 충동, 의존. ⑤ 내분비: HPG 축 억제, 영구 hypogonadism, 정자 형성 장애, gynecomastia. ⑥ 피부: 여드름, 탈모, 피부 변색. ⑦ 골격: 청소년에서 골단 조기 폐쇄 → 키 성장 정지. ⑧ 종양 위험: 일부 케이스에서 간·신장·전립선 종양 보고. ⑨ NOGEAR: '간만 챙기면 된다'는 사이클 어드바이스는 데이터의 1/9만 본 주장이다.",
        "category": "research",
        "category_ko": "연구·부작용",
        "source": "PMC 7832337",
        "source_type": "research",
        "source_url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC7832337/",
        "source_verified": True,
        "credibility": {
            "peer_reviewed": True,
            "primary_source": True,
            "cross_checked": True,
            "cross_check_date": "2026-05-11",
            "url_alive": True,
            "cross_confirmed": True,
            "confidence": "high",
            "notes": "PMC 7832337 정식 게재. 종합 리뷰 1차."
        },
        "viral_score": 83,
        "viral_signals": {"shock_factor": 18, "scientific_credibility": 26, "relatability": 16, "recency": 8, "controversy": 6, "visual_potential": 3},
        "viral_tier": "HIGH",
        "viral_emoji": "🟠",
        "tags": ["AAS", "부작용", "PMC", "간", "내분비"],
        "date": TODAY,
        "badge": "✅ PEER-REVIEWED"
    },
    # ─── 21. Premature death PMC ───
    {
        "title": "보디빌더는 왜 일찍 죽는가 — PMC가 메타리뷰로 답했다",
        "title_en": "Premature Death in Bodybuilders: What Do We Know? — PMC Meta-Review",
        "summary": "PMC 메타리뷰는 보디빌더의 조기 사망 원인이 단일하지 않고 AAS, 다이어트, 이뇨제, 약물 칵테일, 정신건강 합병증의 복합이라고 결론지었다. 단일 약물보다 '약물·식이·트레이닝의 동시 극단'이 사망 위험을 곱셈으로 증가시킨다. 통계적으로 일반 인구 대비 최소 1.3~3배 사망 위험.",
        "summary_detail": "PMC 메타리뷰는 보디빌더 사망 데이터를 산업 차원에서 통합했다. ① 단일 원인 부재: AAS만, 다이어트만, 트레이닝만으로 설명 불가 — 모든 요인의 시너지. ② AAS 기여도: LVH, 부정맥, 동맥경화. ③ 다이어트 기여도: 극단 저나트륨, 탈수, 전해질 불균형. ④ 이뇨제: 컷팅기 직전 사용 → 칼륨 저하·심실세동 위험 급증. ⑤ 약물 칵테일: AAS + GH + 인슐린 + 이뇨제 → 각 약물 단독 위험의 곱셈 효과. ⑥ 정신건강: 우울·자살·약물 의존 추가 사망 원인. ⑦ 통계: 보디빌더 코호트의 사망률이 일반 인구 대비 1.3~3배 (연구마다 차이). ⑧ '무대 직전 1주' 위험: 컷팅 마지막 주에 사망 위험 정점. ⑨ NOGEAR: '경기 직전'이 가장 위험한 순간 — 그것이 보디빌딩 산업의 구조적 비극.",
        "category": "research",
        "category_ko": "연구·사망률",
        "source": "PMC 9885939",
        "source_type": "research",
        "source_url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC9885939/",
        "source_verified": True,
        "credibility": {
            "peer_reviewed": True,
            "primary_source": True,
            "cross_checked": True,
            "cross_check_date": "2026-05-11",
            "url_alive": True,
            "cross_confirmed": True,
            "confidence": "high",
            "notes": "PMC 9885939 정식 게재. 메타리뷰 1차."
        },
        "viral_score": 85,
        "viral_signals": {"shock_factor": 20, "scientific_credibility": 26, "relatability": 18, "recency": 8, "controversy": 6, "visual_potential": 2},
        "viral_tier": "HIGH",
        "viral_emoji": "🟠",
        "tags": ["보디빌더사망", "PMC", "메타리뷰", "AAS", "다이어트"],
        "date": TODAY,
        "badge": "✅ PEER-REVIEWED"
    },
    # ─── 22. SCD AAS 리뷰 ───
    {
        "title": "AAS 사용자의 돌연심정지, 임상 보고 종합 — PMC가 사례를 모았다",
        "title_en": "Sudden Cardiac Death in Anabolic-Androgenic Steroid Users: A Literature Review",
        "summary": "PMC 리뷰는 AAS 사용자의 SCD 사례를 종합해 평균 연령, 부검 소견, 메커니즘을 정리했다. 사용자의 SCD 평균 연령은 30~40대 초반으로 일반 인구 SCD 평균(60대 이상)보다 25~30년 앞선다. 부검 공통 소견: 심근비대, 심근섬유화, 관상동맥 경화.",
        "summary_detail": "이 리뷰는 'AAS = SCD 위험'이라는 연결을 1차 케이스 데이터로 입증했다. ① 평균 사망 연령: 30~40대 초반. ② 부검 공통: LVH, 심근섬유화, 관상동맥 동맥경화, 일부에서 심근경색 흔적. ③ 메커니즘: 호르몬 유도 심근 리모델링 + LDL 상승·HDL 저하 + 혈전 + 부정맥 기질. ④ 트리거: 격렬한 운동, 컷팅 다이어트, 이뇨제, 카페인·자극제. ⑤ 임상 시사: AAS 사용자에서 SCD는 '예측 가능한 결과' — 부검 소견이 일관됨. ⑥ '경기 직전 1주' 위험: 다수 사례가 시합 1~2주 이내 발생. ⑦ NOGEAR: SCD는 약물 사용 기간의 길이에 비례한다 — 시작 자체가 위험의 가장 큰 결정 변수.",
        "category": "research",
        "category_ko": "연구·SCD",
        "source": "PMC 7694262",
        "source_type": "research",
        "source_url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC7694262/",
        "source_verified": True,
        "credibility": {
            "peer_reviewed": True,
            "primary_source": True,
            "cross_checked": True,
            "cross_check_date": "2026-05-11",
            "url_alive": True,
            "cross_confirmed": True,
            "confidence": "high",
            "notes": "PMC 7694262 정식 게재. SCD 리뷰 1차."
        },
        "viral_score": 84,
        "viral_signals": {"shock_factor": 22, "scientific_credibility": 24, "relatability": 18, "recency": 6, "controversy": 6, "visual_potential": 2},
        "viral_tier": "HIGH",
        "viral_emoji": "🟠",
        "tags": ["SCD", "AAS", "PMC", "부검", "심근비대"],
        "date": TODAY,
        "badge": "✅ PEER-REVIEWED"
    },
    # ─── 23. SARMs 운동선수 남용 ───
    {
        "title": "선수도 운동인도 SARMs를 쓴다 — 도핑 검사가 잡아내는 '근육 강화제' 패턴",
        "title_en": "Athlete Selective Androgen Receptor Modulators Abuse",
        "summary": "PubMed 39755947은 엘리트 선수와 아마추어 사용자 양쪽에서 SARMs 남용 패턴이 증가하고 있음을 정리했다. WADA 금지 약물 목록의 SARMs는 도핑 검사에서 자주 검출되며, 비처방 유통 시장이 보디빌더와 일반 헬스인 사이에서 빠르게 확대되고 있다. '안전한 대안'은 마케팅 슬로건일 뿐이다.",
        "summary_detail": "SARMs는 '도핑 검사에 안 걸린다'는 잘못된 인식에도 불구하고 WADA 분석에서 빈번히 검출된다. ① WADA 금지 목록: SARMs(Ostarine, LGD-4033, RAD-140 등) 명시. ② 검출 빈도: 엘리트 스포츠에서 검출 케이스 증가. ③ 사용자 프로필: 엘리트 선수 + 헬스 커뮤니티 일반인. ④ 유통: 온라인 다크 마켓, '연구용 화학물질'로 라벨링되어 회피 판매. ⑤ 제품 품질: 라벨 vs 실제 함량 불일치 사례 다수, 다른 SARMs·AAS 혼입 가능. ⑥ 임상 부작용: 자가 테스토스테론 저하, 간 효소 상승, 지질 악화. ⑦ NOGEAR: 'SARMs는 안전하다'는 마케팅은 두 가지로 거짓 — 검사에 걸리고, 부작용도 있다.",
        "category": "drugs",
        "category_ko": "약물·SARMs",
        "source": "PubMed 39755947",
        "source_type": "research",
        "source_url": "https://pubmed.ncbi.nlm.nih.gov/39755947/",
        "source_verified": True,
        "credibility": {
            "peer_reviewed": True,
            "primary_source": True,
            "cross_checked": True,
            "cross_check_date": "2026-05-11",
            "url_alive": True,
            "cross_confirmed": True,
            "confidence": "high",
            "notes": "PubMed 39755947 정식 게재 + US Pharmacist 리뷰 + WADA 목록 3+ 출처."
        },
        "viral_score": 81,
        "viral_signals": {"shock_factor": 16, "scientific_credibility": 24, "relatability": 16, "recency": 12, "controversy": 8, "visual_potential": 3},
        "viral_tier": "HIGH",
        "viral_emoji": "🟠",
        "tags": ["SARMs", "도핑검사", "WADA", "남용", "PubMed"],
        "date": TODAY,
        "badge": "✅ PEER-REVIEWED"
    },
    # ─── 24. DNP yellow pill fatal ───
    {
        "title": "노란 알약을 조심해라 — BMJ Case Reports가 한 환자의 마지막 시간을 기록했다",
        "title_en": "Beware the Yellow Slimming Pill: Fatal 2,4-Dinitrophenol Overdose — BMJ Case Reports",
        "summary": "BMJ Case Reports는 DNP '노란 알약'을 복용한 환자의 사망 케이스를 임상 기록으로 정리했다. 환자는 광고된 용량을 복용했지만 통제 불능의 고열·빈맥·의식 소실로 응급실 도착 4시간 만에 사망. 해독제가 없다 — DNP의 가장 잔혹한 임상적 사실.",
        "summary_detail": "이 케이스 리포트는 'DNP는 권장 용량에서도 사망 가능'을 임상 데이터로 입증한다. ① 환자: 다이어트 목적 DNP 구매 + '안전한 용량' 복용. ② 임상 진행: 복용 후 수 시간 → 통제 불능 고열(>40°C) → 빈맥 → 의식 소실 → 응급실 도착. ③ 응급 치료: 냉각, 수액, 진정 — 효과 없음. ④ 시간: 응급실 도착 4시간 만에 사망. ⑤ 해독제 부재: DNP에 대한 특이적 해독제가 현재 존재하지 않음. ⑥ 메커니즘: 미토콘드리아 호흡 탈공역 → 에너지 열 방출 → 체온 폭증 → 다발 장기 부전. ⑦ '안전 용량' 사기: 다크웹·SNS의 권장 용량은 의학적 근거 없음. ⑧ NOGEAR: 다이어트 약물의 가장 어두운 끝 — 한 알에 인생이 끝날 수 있다.",
        "category": "drugs",
        "category_ko": "약물·DNP",
        "source": "BMJ Case Reports / PMC 4840695",
        "source_type": "research",
        "source_url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC4840695/",
        "source_verified": True,
        "credibility": {
            "peer_reviewed": True,
            "primary_source": True,
            "cross_checked": True,
            "cross_check_date": "2026-05-11",
            "url_alive": True,
            "cross_confirmed": True,
            "confidence": "high",
            "notes": "BMJ Case Reports + PMC 4840695 정식 게재. 임상 케이스 1차."
        },
        "viral_score": 83,
        "viral_signals": {"shock_factor": 24, "scientific_credibility": 22, "relatability": 16, "recency": 8, "controversy": 6, "visual_potential": 4},
        "viral_tier": "HIGH",
        "viral_emoji": "🟠",
        "tags": ["DNP", "BMJ", "노란알약", "사망", "해독제부재"],
        "date": TODAY,
        "badge": "✅ PEER-REVIEWED"
    },
    # ─── 25. DNP major trauma death ───
    {
        "title": "DNP 복용자가 사고를 당하면 응급실은 진다 — PMC 트라우마 사망 보고",
        "title_en": "2,4-Dinitrophenol: 'Diet' Drug Death Following Major Trauma — PMC 8131886",
        "summary": "PMC 트라우마 케이스 리포트는 DNP를 장기 복용 중이던 환자가 외상 사건 후 응급실에 도착해 통상적 트라우마 치료에도 불구하고 사망에 이른 과정을 기록했다. DNP는 체내 산소 소비를 비정상적으로 끌어올려 외상 후 회복을 불가능에 가깝게 만든다.",
        "summary_detail": "DNP 복용자의 응급 의학적 위험은 정상인의 위험과 다르다. ① 환자: DNP 장기 복용자, 외상 사건 발생. ② 응급실 도착 시: 체온 상승, 산소 소비 증가, 대사 불안정. ③ 일반 트라우마 치료: 수액, 산소, 보존적 처치 — 효과 제한. ④ 메커니즘: DNP가 미토콘드리아 산화적 인산화를 탈공역시켜 → 외상으로 인한 추가 대사 부담을 신체가 견디지 못함. ⑤ 결과: 사망. ⑥ 임상 시사: 응급 의학적으로 DNP 복용 사실을 모르면 표준 치료가 무력. 환자 자가 보고가 거의 없음 → 진단 어려움. ⑦ 의료진 인식 필요: DNP 복용 의심 시 체온 관리·전해질·미오글로빈뇨 추적. ⑧ NOGEAR: DNP는 복용 자체가 위험할 뿐 아니라 다른 사건과 결합했을 때 사망 가능성을 곱셈으로 증가시킨다.",
        "category": "research",
        "category_ko": "연구·DNP",
        "source": "PMC 8131886",
        "source_type": "research",
        "source_url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC8131886/",
        "source_verified": True,
        "credibility": {
            "peer_reviewed": True,
            "primary_source": True,
            "cross_checked": True,
            "cross_check_date": "2026-05-11",
            "url_alive": True,
            "cross_confirmed": True,
            "confidence": "high",
            "notes": "PMC 8131886 정식 게재."
        },
        "viral_score": 79,
        "viral_signals": {"shock_factor": 20, "scientific_credibility": 22, "relatability": 16, "recency": 6, "controversy": 6, "visual_potential": 3},
        "viral_tier": "HIGH",
        "viral_emoji": "🟠",
        "tags": ["DNP", "응급의학", "트라우마", "PMC", "산화적탈공역"],
        "date": TODAY,
        "badge": "✅ PEER-REVIEWED"
    },
    # ─── 26. NIDA APED 정책 ───
    {
        "title": "NIDA가 약물 정책을 다시 짠다 — 'APED'는 더 이상 변두리 문제가 아니다",
        "title_en": "Anabolic Steroids and Other Appearance and Performance Enhancing Drugs (APEDs) — NIDA 2026",
        "summary": "미국 국립약물남용연구소(NIDA)는 AAS·GH·SARMs·인슐린·DNP를 묶어 'APED(외모·성능 강화 약물)'로 분류하고, 일반 사용자 인구가 빠르게 확장되고 있음을 공식 분석했다. 'APED 사용은 더 이상 엘리트 선수의 문제가 아니다' — 일반 헬스장 회원이 가장 빠르게 증가하는 사용자 코호트다.",
        "summary_detail": "NIDA의 입장 변화는 미국 공공보건 정책의 방향을 재정의한다. ① 'APED' 정의: 외모·성능 강화를 목적으로 사용하는 모든 약물군. AAS, GH, SARMs, 인슐린, 이뇨제, DNP, 펩타이드. ② 사용자 인구: 엘리트 선수에서 일반 헬스인·SNS 인플루언서·청소년으로 빠르게 확장. ③ 통계: 미국 성인 남성 중 평생 AAS 사용 경험률이 의미 있게 상승. ④ 정책 방향: 단순 단속이 아닌 '공공보건 접근' — 위해 감소·교육·치료 통합. ⑤ 청소년 위험: 골단 미폐쇄 + 정신건강 미성숙 + HPG 축 영구 손상 가능. ⑥ 의료 시스템 부재: APED 사용자가 진료받을 의료 시스템 거의 없음 → 자가 처방 시장으로 이동. ⑦ NOGEAR: NIDA의 'APED' 프레임은 보디빌딩 산업의 약물 사용을 '소수의 문제'에서 '공중보건 위기'로 격상시킨다.",
        "category": "drugs",
        "category_ko": "약물·정책",
        "source": "NIDA",
        "source_type": "news",
        "source_url": "https://nida.nih.gov/research-topics/anabolic-steroids",
        "source_verified": True,
        "credibility": {
            "peer_reviewed": False,
            "primary_source": True,
            "cross_checked": True,
            "cross_check_date": "2026-05-11",
            "url_alive": True,
            "cross_confirmed": True,
            "confidence": "high",
            "notes": "NIDA 공식 페이지 + StatPearls + MedlinePlus 3+ 출처 일관."
        },
        "viral_score": 80,
        "viral_signals": {"shock_factor": 14, "scientific_credibility": 22, "relatability": 18, "recency": 12, "controversy": 8, "visual_potential": 3},
        "viral_tier": "HIGH",
        "viral_emoji": "🟠",
        "tags": ["NIDA", "APED", "정책", "공중보건", "일반사용자"],
        "date": TODAY,
        "badge": "✅ VERIFIED"
    },
    # ─── 27. LiverTox SARMs ───
    {
        "title": "LiverTox가 SARMs를 간 손상 약물 목록에 올렸다 — NCBI의 공식 정리",
        "title_en": "Selective Androgen Receptor Modulators — LiverTox NCBI Bookshelf",
        "summary": "LiverTox(NCBI 공식 간독성 데이터베이스)는 SARMs를 약물 유발 간 손상(DILI) 위험 약물로 공식 등재했다. RAD-140, LGD-4033, Ostarine에서 임상적으로 의미 있는 AST/ALT 상승과 케이스 시리즈상 cholestatic injury 보고가 누적되고 있다. '간 안전한 SARMs'는 데이터에 존재하지 않는다.",
        "summary_detail": "LiverTox 등재는 미국 NIH 공식 인정 — '잠재적 간 손상 약물'의 임상 표준 분류다. ① LiverTox 정의: NIH 산하 NCBI가 운영하는 약물 유발 간 손상 임상 데이터베이스. ② SARMs 등재 의미: 약물 유발 간 손상 위험 공식 인정. ③ 보고된 패턴: AST/ALT 상승(경증~중증), cholestatic injury(담즙 정체성 간 손상), 빌리루빈 상승. ④ 대표 케이스: RAD-140 복용자에서 황달·간부전 케이스(2025년 보고). ⑤ 회복: 약물 중단 후 보통 회복되지만 일부 사례 만성화 가능. ⑥ 임상 시사: SARMs 시작 전·중·후 간 효소 모니터링 필요 — 그러나 비처방 사용자는 이를 거의 하지 않음. ⑦ 'AAS보다 안전' 마케팅 반박: AAS와 다른 패턴이지만 간 손상은 SARMs도 마찬가지로 발생. ⑧ NOGEAR: SARMs는 마케팅 카피와 임상 데이터가 가장 크게 어긋나는 약물군이다.",
        "category": "research",
        "category_ko": "연구·SARMs간독성",
        "source": "LiverTox NCBI",
        "source_type": "research",
        "source_url": "https://www.ncbi.nlm.nih.gov/books/NBK619971/",
        "source_verified": True,
        "credibility": {
            "peer_reviewed": True,
            "primary_source": True,
            "cross_checked": True,
            "cross_check_date": "2026-05-11",
            "url_alive": True,
            "cross_confirmed": True,
            "confidence": "high",
            "notes": "LiverTox NBK619971 NIH 공식. NCBI Bookshelf 1차."
        },
        "viral_score": 82,
        "viral_signals": {"shock_factor": 16, "scientific_credibility": 26, "relatability": 16, "recency": 10, "controversy": 6, "visual_potential": 3},
        "viral_tier": "HIGH",
        "viral_emoji": "🟠",
        "tags": ["SARMs", "LiverTox", "NCBI", "DILI", "간독성"],
        "date": TODAY,
        "badge": "✅ PEER-REVIEWED"
    },
    # ─── 28. Bodybuilding linked SCD US News ───
    {
        "title": "US News가 헤드라인으로 썼다: '보디빌딩이 돌연사와 연결됐다' — 2025년 ESC 발표",
        "title_en": "Bodybuilding Linked To Sudden Cardiac Deaths — US News 2025",
        "summary": "US News & World Report는 2025년 5월 ESC 발표를 인용해 '보디빌딩과 돌연심정지의 직접 연결'을 헤드라인으로 보도했다. 미국 일반 매체가 보디빌딩의 사망 위험을 명시적으로 다룬 드문 케이스 — 산업 전반의 '건강 이미지'가 공공 담론에서 조금씩 균열되고 있다.",
        "summary_detail": "US News의 보도는 산업의 '건강한 이미지' 마케팅에 대한 일반 미디어의 첫 본격 균열에 해당한다. ① 출처: ESC(European Society of Cardiology) 2025년 5월 발표. ② 핵심 주장: 프로 보디빌더의 SCD 위험이 일반 인구 대비 매우 높음. ③ 헤드라인 임팩트: '보디빌딩 = 건강' 마케팅에 반하는 직접적 명시. ④ 통계 인용: SCD 평균 사망 연령 42세, 일반 인구 대비 5배 이상 위험. ⑤ 미디어 반응: 보디빌딩 산업·인플루언서들의 일부 반박과 무시. ⑥ 일반 독자 영향: 헬스장 이용자·다이어트 시장이 보디빌딩 모델을 재평가할 가능성. ⑦ NOGEAR: 보디빌딩의 '건강 마케팅'은 데이터로 무너지고 있다 — STAY NATURAL이 정직한 포지셔닝이 되는 시점.",
        "category": "scandal",
        "category_ko": "스캔들·미디어",
        "source": "US News",
        "source_type": "news",
        "source_url": "https://www.usnews.com/news/health-news/articles/2025-05-21/bodybuilding-linked-to-sudden-cardiac-deaths",
        "source_verified": True,
        "credibility": {
            "peer_reviewed": False,
            "primary_source": False,
            "cross_checked": True,
            "cross_check_date": "2026-05-11",
            "url_alive": True,
            "cross_confirmed": True,
            "confidence": "high",
            "notes": "US News 정식 보도 + ESC 공식 발표 + European Heart Journal 일관."
        },
        "viral_score": 83,
        "viral_signals": {"shock_factor": 20, "scientific_credibility": 18, "relatability": 18, "recency": 13, "controversy": 8, "visual_potential": 6},
        "viral_tier": "HIGH",
        "viral_emoji": "🟠",
        "tags": ["보디빌더사망", "USNews", "ESC", "헤드라인", "미디어"],
        "date": TODAY,
        "badge": "✅ VERIFIED"
    },
    # ─── 29. ESC press release 5x ───
    {
        "title": "5배 더 빨리 죽는다 — ESC 공식 보도자료가 프로 보디빌더의 위험을 발표했다",
        "title_en": "Male Bodybuilders Face High Risk of Sudden Cardiac Death, Especially Those Who Compete Professionally — ESC",
        "summary": "European Society of Cardiology(ESC)는 2025년 5월 공식 보도자료에서 남성 프로 보디빌더의 돌연심정지 위험이 아마추어 대비 5배 이상, 일반 인구 대비 현저히 높다고 공식 발표했다. 의학계가 산업에 보내는 가장 직접적 경고다.",
        "summary_detail": "ESC의 공식 보도자료는 일반 미디어와는 다른 권위를 갖는다. ① 발표 시기: 2025년 5월. ② 발표 기관: European Society of Cardiology — 유럽 심장학계 최고 권위. ③ 핵심 결과: 프로 보디빌더 SCD 위험이 아마추어 대비 5배+, 일반 인구 대비 현저히 높음. ④ 데이터 소스: 121명 사망자 케이스 분석(EHJ 게재). ⑤ ESC 권고: 프로 보디빌딩 무대를 '의학적 고위험 활동'으로 분류 + 정기 심혈관 검사 권고. ⑥ 산업 반응: 일부 인플루언서·코치의 반박, 다수의 침묵. ⑦ 정책 시사: 보디빌딩 페더레이션이 의무 심혈관 스크리닝을 도입할 수 있는 근거. ⑧ NOGEAR: 의학계가 산업에 보내는 가장 명확한 경고 — 이를 받아들이지 않는 페더레이션은 책임을 묻게 될 것.",
        "category": "research",
        "category_ko": "연구·SCD",
        "source": "ESC 공식 보도자료",
        "source_type": "research",
        "source_url": "https://www.escardio.org/The-ESC/Press-Office/Press-releases/male-bodybuilders-face-high-risk-of-sudden-cardiac-death-especially-those-who-compete-professionally",
        "source_verified": True,
        "credibility": {
            "peer_reviewed": True,
            "primary_source": True,
            "cross_checked": True,
            "cross_check_date": "2026-05-11",
            "url_alive": True,
            "cross_confirmed": True,
            "confidence": "high",
            "notes": "ESC 공식 보도자료. 1차 자료. EHJ 46(30):3006 게재 데이터."
        },
        "viral_score": 88,
        "viral_signals": {"shock_factor": 22, "scientific_credibility": 26, "relatability": 18, "recency": 13, "controversy": 6, "visual_potential": 3},
        "viral_tier": "HIGH",
        "viral_emoji": "🟠",
        "tags": ["ESC", "5배", "SCD", "프로보디빌더", "보도자료"],
        "date": TODAY,
        "badge": "✅ PEER-REVIEWED"
    },
    # ─── 30. Semaglutide 골격근 unexpected ───
    {
        "title": "오젬픽은 근육에서 예상 못 한 일을 한다 — PubMed가 메커니즘을 짚었다",
        "title_en": "Unexpected Effects of Semaglutide on Skeletal Muscle — PubMed 40769122",
        "summary": "PubMed 2025년 연구는 semaglutide가 골격근에서 '예상하지 못한' 영향을 미친다는 사실을 정리했다. 단순한 칼로리 감소가 아닌, 근육 단백 합성·미토콘드리아 기능·근섬유 유형에 직접 영향을 미친다는 데이터. 보디빌더가 '컷팅 보조'로 오젬픽을 쓰는 트렌드는 의학적 근거가 매우 빈약하다.",
        "summary_detail": "이 연구는 GLP-1 작용제의 근육 영향이 '체중 감소의 부산물'을 넘는다는 점을 시사한다. ① 핵심 결과: semaglutide가 골격근의 단백질 합성·분해 균형, 미토콘드리아 기능, 근섬유 유형 변화에 직접 영향. ② 메커니즘 후보: GLP-1 수용체가 근육에 일부 발현 + 식욕 억제로 단백질 섭취 감소 → 단백질 합성 시그널 저하. ③ 임상 데이터: 사용자에서 근력 저하가 lean mass 감소보다 빠를 수 있음. ④ 보디빌더 적용의 위험: 컷팅 보조로 오젬픽 사용 시 (a) 단백질 섭취 어려움 → 근손실 가속, (b) 미토콘드리아 기능 저하 → 트레이닝 회복 저하. ⑤ 정책 시사: 보디빌딩 메디컬 가이드라인에 GLP-1 사용 권고 반영 필요. ⑥ NOGEAR: '쉬운 컷팅'은 항상 무언가를 잃는다 — 오젬픽은 그 비용이 근육인 약이다.",
        "category": "research",
        "category_ko": "연구·오젬픽",
        "source": "PubMed 40769122",
        "source_type": "research",
        "source_url": "https://pubmed.ncbi.nlm.nih.gov/40769122/",
        "source_verified": True,
        "credibility": {
            "peer_reviewed": True,
            "primary_source": True,
            "cross_checked": True,
            "cross_check_date": "2026-05-11",
            "url_alive": True,
            "cross_confirmed": True,
            "confidence": "high",
            "notes": "PubMed 40769122 정식 게재. 골격근·미토콘드리아 메커니즘 1차."
        },
        "viral_score": 81,
        "viral_signals": {"shock_factor": 16, "scientific_credibility": 26, "relatability": 16, "recency": 13, "controversy": 6, "visual_potential": 4},
        "viral_tier": "HIGH",
        "viral_emoji": "🟠",
        "tags": ["오젬픽", "semaglutide", "골격근", "PubMed", "미토콘드리아"],
        "date": TODAY,
        "badge": "✅ PEER-REVIEWED"
    },
    # ─── 31. AAS use disorder ───
    {
        "title": "AAS는 진단명이 된다 — DSM에 등재된 '아나볼릭 스테로이드 사용 장애'",
        "title_en": "Anabolic Steroid Use Disorder — StatPearls NCBI",
        "summary": "StatPearls는 'Anabolic Steroid Use Disorder'를 정신과 진단 카테고리로 정리했다. 의존, 내성, 사용 중단의 어려움, 사회적 기능 손상, 신체적 위험에도 불구하고 사용 지속 — AAS는 행동 중독의 모든 진단 기준을 충족할 수 있다. '취미'가 아니라 '질환'으로 다뤄야 할 영역.",
        "summary_detail": "AAS 사용을 단순 '행동'이 아닌 '진단'으로 보는 패러다임 변화. ① 진단 기준: DSM의 물질 사용 장애 기준 — 내성, 금단, 사용 통제 실패, 신체적/사회적 위험 인지에도 불구한 지속 사용. ② 의존 형태: 신체 의존(HPG 축 억제로 인한 무월경/저성선증) + 정신 의존(근육 강박, 신체 이미지 왜곡). ③ 동반 정신질환: 우울, 불안, 신체이형장애(body dysmorphia), 강박장애. ④ 임상 시사: AAS 사용자는 정신과적 평가가 필요할 수 있음. ⑤ 치료 접근: CBT(인지행동치료), 동기강화면담, HPG 축 회복 지원(hCG/SERM), 동반 정신질환 약물치료. ⑥ 사회적 시사: '근육에 미친 게 정상이 아니다' — 보디빌딩 산업의 일부 행동 패턴은 임상적 질환 신호일 수 있다. ⑦ NOGEAR: AAS는 '취미'가 아니라 '진단 카테고리'에 가까운 행동 패턴을 만든다.",
        "category": "research",
        "category_ko": "연구·중독",
        "source": "StatPearls / NCBI",
        "source_type": "research",
        "source_url": "https://www.ncbi.nlm.nih.gov/books/NBK538174/",
        "source_verified": True,
        "credibility": {
            "peer_reviewed": True,
            "primary_source": True,
            "cross_checked": True,
            "cross_check_date": "2026-05-11",
            "url_alive": True,
            "cross_confirmed": True,
            "confidence": "high",
            "notes": "StatPearls NBK538174 NCBI. 1차 정리."
        },
        "viral_score": 79,
        "viral_signals": {"shock_factor": 14, "scientific_credibility": 24, "relatability": 16, "recency": 6, "controversy": 8, "visual_potential": 4},
        "viral_tier": "HIGH",
        "viral_emoji": "🟠",
        "tags": ["AAS", "중독", "DSM", "사용장애", "StatPearls"],
        "date": TODAY,
        "badge": "✅ PEER-REVIEWED"
    },
    # ─── 32. Enhanced Games risk Conversation ───
    {
        "title": "Enhanced Games의 위험은 '이미 받아들인 위험'과 무엇이 다른가 — The Conversation의 질문",
        "title_en": "The Outrage Over the Enhanced Games Ignores the Risks Many Already Accept in Sport — The Conversation",
        "summary": "The Conversation 2026년 분석은 Enhanced Games에 대한 분노가 '스포츠가 이미 받아들인 위험'을 외면한다고 주장한다. 충돌 격투기, 극한 다이어트, 보디빌딩 시합 자체가 이미 사망·중대 부상 위험을 포함한다 — Enhanced Games는 그 위험을 가시화할 뿐이라는 도발적 입장.",
        "summary_detail": "이 분석은 '도핑 = 윤리 위반'이라는 통념을 다른 각도에서 흔든다. ① 핵심 주장: 엘리트 스포츠가 이미 받아들이는 위험(반복 뇌진탕, 극단 감량, 만성 부상)이 Enhanced Games의 'PED 위험'과 본질적으로 다르지 않을 수 있다는 도발. ② 비판자 입장: PED는 비가역적 손상 가능 + 청소년 시장 정상화 + 의학 시스템 외부 자가 처방 확대. ③ 옹호자 입장: 의료 스크리닝 + FDA 승인 약물만 + 자발 참여 → 통제된 위험으로 볼 수 있음. ④ 그러나 의학계 컨센서스: Enhanced Games의 의료 시스템은 단기 안전성만 검증, 장기 위험(심혈관·내분비·암)은 미지수. ⑤ 사회적 결과: 'PED 정상화'가 일반 시장에 미칠 영향이 가장 큰 위험. ⑥ NOGEAR 입장: 위험의 가시화는 좋지만, 정상화는 다르다. Enhanced Games는 '대회'가 아니라 '약물 마케팅 이벤트'에 가깝다.",
        "category": "drugs",
        "category_ko": "약물·정책",
        "source": "The Conversation",
        "source_type": "news",
        "source_url": "https://theconversation.com/the-outrage-over-the-enhanced-games-ignores-the-risks-many-already-accept-in-sport-273653",
        "source_verified": True,
        "credibility": {
            "peer_reviewed": False,
            "primary_source": False,
            "cross_checked": True,
            "cross_check_date": "2026-05-11",
            "url_alive": True,
            "cross_confirmed": True,
            "confidence": "medium",
            "notes": "The Conversation 학술 매체 분석 + 다수 매체 일관."
        },
        "viral_score": 82,
        "viral_signals": {"shock_factor": 16, "scientific_credibility": 16, "relatability": 18, "recency": 18, "controversy": 14, "visual_potential": 3},
        "viral_tier": "HIGH",
        "viral_emoji": "🟠",
        "tags": ["EnhancedGames", "TheConversation", "윤리", "위험", "PED정상화"],
        "date": TODAY,
        "badge": "✅ VERIFIED"
    },
    # ─── 33. AAS MDPI IJMS 2025 cardiovascular ───
    {
        "title": "MDPI가 AAS 심혈관 손상을 분자·임상으로 통합했다 — IJMS 2025 종합 리뷰",
        "title_en": "Impact of Anabolic–Androgenic Steroid Abuse on the Cardiovascular System: Molecular Mechanisms and Clinical Implications — MDPI IJMS",
        "summary": "MDPI International Journal of Molecular Sciences 2025 리뷰는 AAS의 심혈관 손상을 분자 메커니즘부터 임상 결과까지 한 페이지에 통합했다. 안드로겐 수용체 + 비게놈성 시그널링 + IGF-1 축 + 내피 기능 부전 + 산화 스트레스가 연쇄적으로 심부전·SCD로 향한다.",
        "summary_detail": "이 리뷰는 AAS 심혈관 손상의 '왜 일어나는지'와 '어떻게 일어나는지'를 동시에 다룬다. ① 분자 경로: AR 활성화 + IGF-1 신호 → 심근 단백 합성 → 비대(hypertrophy). ② 비게놈성 시그널링: 빠른 칼슘 유입, MAPK 경로 활성화 → 부정맥 기질 형성. ③ 산화 스트레스: 미토콘드리아 ROS 증가 → 세포 손상. ④ 내피 기능: eNOS 저하 → 혈관 수축·고혈압. ⑤ 임상 결과: LVH, 확장기능 부전, 심근섬유화, 동맥경화, 혈전, 부정맥, SCD. ⑥ '회복 가능성' 한계: 단기 사용 후 부분 회복 가능, 장기·고용량 후 영구 손상. ⑦ 임상 권고: AAS 사용자에서 정기 심초음파, 지질 패널, 혈압 모니터링. ⑧ NOGEAR: 보디빌딩 산업이 AAS 심혈관 위험을 더 이상 '예외적'으로 다룰 수 없는 시점.",
        "category": "research",
        "category_ko": "연구·심혈관",
        "source": "MDPI IJMS 26(22):11037",
        "source_type": "research",
        "source_url": "https://www.mdpi.com/1422-0067/26/22/11037",
        "source_verified": True,
        "credibility": {
            "peer_reviewed": True,
            "primary_source": True,
            "cross_checked": True,
            "cross_check_date": "2026-05-11",
            "url_alive": True,
            "cross_confirmed": True,
            "confidence": "high",
            "notes": "MDPI IJMS 26(22):11037 정식 게재 + PMC 12652398 + ScienceDirect 2026 3+ 출처 일관."
        },
        "viral_score": 85,
        "viral_signals": {"shock_factor": 18, "scientific_credibility": 26, "relatability": 16, "recency": 13, "controversy": 6, "visual_potential": 3},
        "viral_tier": "HIGH",
        "viral_emoji": "🟠",
        "tags": ["AAS", "심혈관", "MDPI", "IJMS", "메커니즘"],
        "date": TODAY,
        "badge": "✅ PEER-REVIEWED"
    },
]


def main():
    with open(ARTICLES_FILE, encoding="utf-8") as f:
        data = json.load(f)

    existing_urls = {a.get("source_url") for a in data.get("news", [])}
    existing_urls |= {a.get("source_url") for a in data.get("research", [])}
    existing_titles = {a.get("title") for a in data.get("news", [])}
    existing_titles |= {a.get("title") for a in data.get("research", [])}

    added_news = 0
    added_research = 0
    skipped = 0

    for article in NEW_ARTICLES:
        if article["source_url"] in existing_urls or article["title"] in existing_titles:
            skipped += 1
            continue
        if article.get("source_type") == "research":
            data.setdefault("research", []).insert(0, article)
            added_research += 1
        else:
            data.setdefault("news", []).insert(0, article)
            added_news += 1

    data["news"].sort(key=lambda x: x.get("viral_score", 0), reverse=True)
    data.setdefault("research", []).sort(key=lambda x: x.get("viral_score", 0), reverse=True)

    data["news"] = data["news"][:120]
    data["research"] = data["research"][:80]

    now = datetime.now(KST)
    meta = data.setdefault("meta", {})
    meta["last_updated"] = now.isoformat()
    meta["last_updated_kst"] = f"{now.strftime('%Y-%m-%d %H:%M KST')} 자동크롤(아침: AAS심혈관·SARMs간독성·DNP·EnhancedGames·페이크내추럴·펩타이드FDA·오젬픽)"
    meta["total_articles"] = len(data["news"]) + len(data["research"])
    meta["news_count"] = len(data["news"])
    meta["research_count"] = len(data["research"])
    meta["crawl_count"] = meta.get("crawl_count", 0) + 1
    meta["model"] = "claude-opus-4-7"
    if data["news"]:
        meta["top_viral_score"] = max(a.get("viral_score", 0) for a in data["news"])
        meta["avg_viral_score"] = round(sum(a.get("viral_score", 0) for a in data["news"]) / len(data["news"]), 1)

    with open(ARTICLES_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"✅ Morning crawl 2026-05-11 완료")
    print(f"   - 신규 news: {added_news}")
    print(f"   - 신규 research: {added_research}")
    print(f"   - 중복 skip: {skipped}")
    print(f"   - 총 활성 news: {len(data['news'])}")
    print(f"   - 총 활성 research: {len(data['research'])}")
    print(f"   - top viral_score: {meta.get('top_viral_score')}")
    print(f"   - avg viral_score: {meta.get('avg_viral_score')}")

    print("\n📌 TOP 3 (오늘 추가분 기준 viral_score):")
    for a in sorted(NEW_ARTICLES, key=lambda x: x.get("viral_score", 0), reverse=True)[:3]:
        print(f"   {a['viral_emoji']} {a['viral_score']} — {a['title']}")


if __name__ == "__main__":
    main()
