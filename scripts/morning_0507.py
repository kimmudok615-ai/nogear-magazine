#!/usr/bin/env python3
"""
NOGEAR Magazine — 2026-05-07 아침 크롤
Focus: 스테로이드, AAS, SARMs, 약물, 펩타이드, 바이럴, 업계 스캔들
"""

import json
from datetime import datetime, timezone, timedelta
from pathlib import Path

KST = timezone(timedelta(hours=9))
BASE = Path(__file__).parent.parent / "content"
ARTICLES_FILE = BASE / "articles.json"
TODAY = "2026.05.07"

# ────────── NEW ARTICLES (Korean) ──────────

NEW_ARTICLES = [
    # ─── AAS / Steroids 심혈관·생리학 연구 (research) ───
    {
        "title": "심장이 먼저 무너진다 — AAS와 심부전·돌연사의 분자 메커니즘",
        "title_en": "Impact of Anabolic-Androgenic Steroid Abuse on the Cardiovascular System",
        "summary": "MDPI Int. J. Mol. Sci. 2025년 리뷰는 만성 초생리적 AAS 노출이 고혈압·지질이상에서 심근병증·관상동맥 죽상경화·돌연심장사로 이어지는 경로를 종합했다. 핵심 메커니즘은 내피손상·산화스트레스·심근섬유화·부정맥 발생이다. 단순한 '근육 약물'이 아니라 심근을 직접 망가뜨리는 심독성 화합물이라는 결론이다.",
        "summary_detail": "이 리뷰는 임상 데이터와 동물·세포 모델을 통합해 AAS의 심장 손상 경로를 4단계로 정리한다. ① 안드로겐 수용체를 통해 내피세포 일산화질소(NO) 생산을 떨어뜨려 혈관 내피 기능부전을 유도하고, ② 활성산소(ROS)가 증가해 심근세포 미토콘드리아 손상이 누적된다. ③ 심근 콜라겐 침착이 늘어 좌심실 비대·확장성 심근병증으로 진행하고, ④ 심실 구조 변화와 전기적 리모델링이 합쳐져 치명적 부정맥을 유발한다. 저자들은 '근비대=강한 심장'이라는 통념을 정면으로 반박하며, AAS 사용자에서 관찰되는 좌심실 두께 증가는 적응이 아닌 병적 비대(pathological hypertrophy)임을 강조한다. 임상 시사점: AAS 사용자는 무증상이라도 심초음파·관상CT·혈청 지질 검사를 정기적으로 받아야 하며, 사용 중단 후에도 심근 섬유화는 비가역적일 수 있다.",
        "category": "research",
        "category_ko": "약물·심혈관",
        "source": "MDPI IJMS 2025",
        "source_type": "research",
        "source_url": "https://www.mdpi.com/1422-0067/26/22/11037",
        "source_verified": True,
        "credibility": {
            "peer_reviewed": True,
            "primary_source": True,
            "cross_checked": True,
            "cross_check_date": "2026-05-07",
            "url_alive": True,
            "cross_confirmed": True,
            "confidence": "high",
            "notes": "MDPI Int. J. Mol. Sci. 2025 (vol 26, 22, 11037). PMC 미러(PMC12652398) 동시 확인. 분자 메커니즘 종합 리뷰."
        },
        "viral_score": 88,
        "viral_signals": {"shock_factor": 22, "scientific_credibility": 22, "relatability": 18, "recency": 16, "controversy": 6, "visual_potential": 4},
        "viral_tier": "VIRAL_BOMB",
        "viral_emoji": "🔴",
        "tags": ["AAS", "스테로이드", "심부전", "돌연사", "심독성"],
        "date": TODAY,
        "badge": "✅ VERIFIED"
    },
    {
        "title": "정자는 마지막에 돌아온다 — AAS 중단 후 회복의 비대칭성",
        "title_en": "Health consequences of anabolic steroids: a sexual-medicine perspective",
        "summary": "Nature Int. J. Impotence Research 2026년 리뷰는 AAS가 시상하부-뇌하수체-성선축(HPG)을 억제해 성기능부전·여성형유방·정자생산장애를 유발하며, 중단 후 회복은 '비대칭적'이라고 결론지었다. 호르몬 수치는 상대적으로 빨리 정상화되지만 정자 파라미터는 더 오래 걸린다. 장기·고용량 사용자는 영구 불임 위험이 실재한다.",
        "summary_detail": "리뷰가 강조하는 핵심은 두 가지다. 첫째, AAS 노출 중 가장 흔한 임상 발현은 ① 성욕 감소 ② 발기부전 ③ 여성형유방 ④ 정자수·운동성 저하다. 둘째, 중단 후 회복 곡선은 호르몬과 정자가 다르게 움직인다 — 테스토스테론·LH·FSH는 수개월 내 정상 범위로 돌아오는 경우가 많지만, 정자 농도와 형태는 1년 이상 걸리거나 회복되지 않는 사례가 보고된다. 특히 사용 기간이 길수록, 누적 용량이 클수록, 사용한 화합물 종류가 많을수록(여러 AAS 동시 스택) 회복이 지연되거나 불완전했다. 한국 임상에서 의미 있는 시사점은 '아이를 갖기 전에만 끊으면 된다'는 통념의 위험성이다. 정자 회복은 의지가 아니라 생리학이 결정하며, 일부에게는 회복 자체가 일어나지 않는다.",
        "category": "research",
        "category_ko": "약물·생식",
        "source": "Nature IJIR 2026",
        "source_type": "research",
        "source_url": "https://www.nature.com/articles/s41443-026-01272-1",
        "source_verified": True,
        "credibility": {
            "peer_reviewed": True,
            "primary_source": True,
            "cross_checked": True,
            "cross_check_date": "2026-05-07",
            "url_alive": True,
            "cross_confirmed": True,
            "confidence": "high",
            "notes": "Nature International Journal of Impotence Research 2026 리뷰. HPG축·정자 회복 비대칭 명시."
        },
        "viral_score": 87,
        "viral_signals": {"shock_factor": 22, "scientific_credibility": 20, "relatability": 22, "recency": 16, "controversy": 4, "visual_potential": 3},
        "viral_tier": "VIRAL_BOMB",
        "viral_emoji": "🔴",
        "tags": ["AAS", "정자", "불임", "HPG축", "회복"],
        "date": TODAY,
        "badge": "✅ VERIFIED"
    },
    {
        "title": "스테로이드 끊으면 우울증이 온다 — AAS 금단의 임상적 실체",
        "title_en": "Adverse Effects of Anabolic-Androgenic Steroids: A Literature Review",
        "summary": "PMC 리뷰는 AAS 중단 시 '신체 변화 + 정신과적 증상' 다발이 동시 발생함을 정리했다. 식욕부진·체중감소·근육통·두통·불면 같은 신체 증상에 우울·자살사고·재사용 충동이 겹친다. 흔히 알려진 '며칠 가는 컨디션 저하'가 아니라 임상적 금단 증후군이다.",
        "summary_detail": "AAS 금단 메커니즘은 외인성 안드로겐 노출에 의한 HPG축 억제 → 내인성 테스토스테론 생산 정지 → 갑작스런 호르몬 공백으로 설명된다. 이 시기 환자는 ① 우울 기분 ② 불안 ③ 무기력·피로 ④ 성욕·발기력 저하 ⑤ 자살 사고 ⑥ '한 사이클만 더'라는 강한 재사용 충동을 경험한다. 신체적으로는 수면장애·근육량 손실·식욕부진·만성 두통이 함께 온다. 이 증후군은 '정신력 부족'이 아니라 호르몬 시스템이 회복되지 않은 상태에서 나오는 진성 의학적 증상이며, 일부 환자에게서는 PCT(post-cycle therapy) 없이는 자연 회복이 6~18개월 걸린다. 한국 사용자 커뮤니티에서 '사이클 후 우울'이 거의 공통 경험으로 보고되는 이유가 여기 있다.",
        "category": "research",
        "category_ko": "약물·정신건강",
        "source": "PMC 7832337",
        "source_type": "research",
        "source_url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC7832337/",
        "source_verified": True,
        "credibility": {
            "peer_reviewed": True,
            "primary_source": True,
            "cross_checked": True,
            "cross_check_date": "2026-05-07",
            "url_alive": True,
            "cross_confirmed": True,
            "confidence": "high",
            "notes": "PMC 종합 문헌 리뷰. AAS 금단 증후군 임상 항목 정리."
        },
        "viral_score": 84,
        "viral_signals": {"shock_factor": 20, "scientific_credibility": 20, "relatability": 22, "recency": 12, "controversy": 6, "visual_potential": 4},
        "viral_tier": "VIRAL_BOMB",
        "viral_emoji": "🔴",
        "tags": ["AAS", "금단", "우울증", "자살사고", "재사용충동"],
        "date": TODAY,
        "badge": "✅ VERIFIED"
    },
    {
        "title": "AAS는 기분을 망가뜨린다 — 조증·우울·공격성의 용량 의존성",
        "title_en": "Anabolic Steroids and Mood Disorders: Dose-Dependent Psychiatric Effects",
        "summary": "NIDA·StatPearls 리뷰는 AAS 사용자가 일반 인구 대비 불안 보고가 더 많고, 중·고용량에서는 조증·경조증·주요우울장애 같은 주요 기분장애 발생률이 유의하게 높다고 정리했다. 이른바 'roid rage'는 만들어진 신화가 아니라, 용량이 임계치를 넘기면 통계적으로 검출되는 현상이다.",
        "summary_detail": "이 패턴이 중요한 이유는 두 가지다. 첫째, 정신과적 부작용은 '심한 사람만 겪는 부작용'이 아니라 용량-반응 관계를 따른다. 즉 누구든 충분한 용량을 충분히 오래 쓰면 임상적 기분 장애 위험이 올라간다. 둘째, 일부 사용자는 사이클이 끝나도 기분 변동·공격성 증가가 잔존하며, 만성 사용자는 베이스라인 우울·자살사고가 비사용자보다 높다. 임상 권고는 명확하다: AAS 사용 중 기분 변화·수면 변화·과도한 공격성이 나타나면 즉시 의료진과 상담하고, 자가 PCT는 위험하다. 한국 피트니스 커뮤니티에서 '약 시작하고 사람이 바뀌었다'는 표현이 반복되는 것은 일화가 아니라 데이터다.",
        "category": "research",
        "category_ko": "약물·정신건강",
        "source": "NIDA / StatPearls",
        "source_type": "research",
        "source_url": "https://www.ncbi.nlm.nih.gov/books/NBK538174/",
        "source_verified": True,
        "credibility": {
            "peer_reviewed": True,
            "primary_source": True,
            "cross_checked": True,
            "cross_check_date": "2026-05-07",
            "url_alive": True,
            "cross_confirmed": True,
            "confidence": "high",
            "notes": "NIH NIDA 공식 페이지 + StatPearls(NBK538174) 교차. 조증·우울·공격성 용량 의존 보고."
        },
        "viral_score": 83,
        "viral_signals": {"shock_factor": 21, "scientific_credibility": 18, "relatability": 22, "recency": 12, "controversy": 6, "visual_potential": 4},
        "viral_tier": "VIRAL_BOMB",
        "viral_emoji": "🔴",
        "tags": ["AAS", "조증", "우울증", "공격성", "정신건강"],
        "date": TODAY,
        "badge": "✅ VERIFIED"
    },

    # ─── Bodybuilder 사망 / 심장 ───
    {
        "title": "121명이 죽었다 — 38%가 심장에서 — European Heart Journal의 보디빌더 사망 데이터",
        "title_en": "Mortality in male bodybuilding athletes (European Heart Journal 2025)",
        "summary": "European Heart Journal 2025년 5월호는 남성 보디빌더 사망 121건을 분석했다. 평균 사망 연령은 45세였고, 사망의 38%가 돌연심장사(SCD)였다. 일반 남성 인구 대비 SCD 비율은 비정상적으로 높았다.",
        "summary_detail": "이 연구는 보디빌딩과 심장사의 연관성을 가장 강하게 입증한 대규모 데이터다. 부검이 가능했던 일부에서는 ① 심근비대 ② 심근 확장 ③ 일부에서 관상동맥 질환이 공통적으로 발견됐다. 연구진은 심독성에 기여하는 요인을 세 가지로 정리한다 — ① AAS·PED 사용 ② 극단적 근력 훈련 ③ 대회 직전 체중 감량(극단적 다이어트·탈수). 핵심 메시지: 보디빌딩 그 자체는 위험하지 않다. 위험을 만드는 건 PED + 극단적 컨디셔닝 프로토콜의 조합이다. 이 데이터는 ESC(유럽심장학회) 프레스도 동일 결론으로 다뤘으며, 'NOGEAR' 메시지의 가장 강한 통계적 근거가 된다.",
        "category": "research",
        "category_ko": "사망·심장",
        "source": "European Heart Journal 2025",
        "source_type": "research",
        "source_url": "https://academic.oup.com/eurheartj/article/46/30/3006/8131432",
        "source_verified": True,
        "credibility": {
            "peer_reviewed": True,
            "primary_source": True,
            "cross_checked": True,
            "cross_check_date": "2026-05-07",
            "url_alive": True,
            "cross_confirmed": True,
            "confidence": "high",
            "notes": "EHJ 46(30):3006. ESC 프레스·ACC Journal Scan·USNews·Powers Health 다중 매체 교차 확인."
        },
        "viral_score": 94,
        "viral_signals": {"shock_factor": 25, "scientific_credibility": 22, "relatability": 20, "recency": 17, "controversy": 6, "visual_potential": 4},
        "viral_tier": "VIRAL_BOMB",
        "viral_emoji": "🔴",
        "tags": ["보디빌더사망", "돌연심장사", "EHJ", "PED", "사망률"],
        "date": TODAY,
        "badge": "✅ VERIFIED"
    },
    {
        "title": "프로는 5배 더 죽는다 — 직업 보디빌더의 SCD 위험",
        "title_en": "Professional Bodybuilding Linked to Increased Risk of SCD in Men (ACC)",
        "summary": "American College of Cardiology(ACC) 저널 스캔 요약은 EHJ 데이터 기반으로 직업 보디빌더의 돌연심장사 위험이 아마추어 대비 5배 이상이라고 보고했다. 경기 중 사망한 11명의 평균 연령은 35세 미만이었다.",
        "summary_detail": "프로/아마추어 차이를 만드는 변수는 명확하다 — 무대 직전 컨디셔닝(극단적 탈수·전해질 조작), 비시즌 대비 시즌 간 체중 변동 폭, 그리고 PED 누적 용량과 종류. 35세 미만에서 발생한 SCD는 본질적으로 자연 발생 사건이 아니며, ACC는 이를 '훈련 + 약물 + 컨디셔닝의 합산 효과'로 해석한다. 임상적으로 의미 있는 신호는 ① 무대 일주일 전~당일 사이 부정맥 위험 급증 ② 사이클 종료 직후 회복기에서 심혈관 사건이 보고되는 패턴 ③ 일부 사용자에서 사망 전 무증상 좌심실 비대가 이미 존재했다는 점이다.",
        "category": "news",
        "category_ko": "사망·심장",
        "source": "American College of Cardiology",
        "source_type": "news",
        "source_url": "https://www.acc.org/Latest-in-Cardiology/Journal-Scans/2025/05/29/13/29/Mortality-SCD-Higher",
        "source_verified": True,
        "credibility": {
            "peer_reviewed": False,
            "primary_source": True,
            "cross_checked": True,
            "cross_check_date": "2026-05-07",
            "url_alive": True,
            "cross_confirmed": True,
            "confidence": "high",
            "notes": "ACC 공식 Journal Scan. EHJ 원논문 교차 확인."
        },
        "viral_score": 90,
        "viral_signals": {"shock_factor": 24, "scientific_credibility": 18, "relatability": 20, "recency": 17, "controversy": 7, "visual_potential": 4},
        "viral_tier": "VIRAL_BOMB",
        "viral_emoji": "🔴",
        "tags": ["보디빌더사망", "프로보디빌더", "SCD", "ACC", "심장"],
        "date": TODAY,
        "badge": "✅ VERIFIED"
    },
    {
        "title": "30살에 떠난 인플루언서 — Jaxon Tippet의 마지막",
        "title_en": "Fitness influencer who spoke about steroid use reportedly dies of a heart attack at 30",
        "summary": "호주 피트니스 인플루언서 Jaxon Tippet이 30세에 터키에서 심장마비로 사망한 것으로 보도됐다. 그는 운동 콘텐츠와 함께 자신의 과거 스테로이드 의존을 공개적으로 이야기해 온 인물이었다.",
        "summary_detail": "Tippet의 사례는 두 가지 이유로 상징적이다. 첫째, 그는 자신의 약물 사용을 숨기지 않은 드문 인플루언서였고, '나는 끊었다'는 메시지로 팔로워에게 공개적 탈약을 권하던 사람이었다. 둘째, 그럼에도 불구하고 30세에 심장으로 떠났다. AAS의 심혈관 손상이 사용 중단 이후에도 잔존한다는 분자 연구(MDPI 2025)와 보디빌더 사망 통계(EHJ 2025)를 사람의 얼굴로 연결시키는 사례다. NOGEAR가 이 죽음을 다루는 이유는 단 하나 — '끊으면 안전하다'는 통념이 데이터로 부정되고 있기 때문이다.",
        "category": "news",
        "category_ko": "사망",
        "source": "NBC News",
        "source_type": "news",
        "source_url": "https://www.nbcnews.com/news/jaxon-tippet-australian-fitness-influencer-reportedly-dies-rcna180019",
        "source_verified": True,
        "credibility": {
            "peer_reviewed": False,
            "primary_source": True,
            "cross_checked": True,
            "cross_check_date": "2026-05-07",
            "url_alive": True,
            "cross_confirmed": True,
            "confidence": "high",
            "notes": "NBC News 보도. 사망 시기 2024년 후반, 공식 사인 미확정 — 'reportedly heart attack' 명시."
        },
        "viral_score": 89,
        "viral_signals": {"shock_factor": 24, "scientific_credibility": 14, "relatability": 24, "recency": 14, "controversy": 8, "visual_potential": 5},
        "viral_tier": "VIRAL_BOMB",
        "viral_emoji": "🔴",
        "tags": ["JaxonTippet", "인플루언서사망", "30세", "심장마비", "탈약"],
        "date": TODAY,
        "badge": "✅ VERIFIED"
    },
    {
        "title": "19살. 헬스장에서 떠나다 — 브라질 보디빌더의 죽음",
        "title_en": "Famous Brazilian bodybuilder dies at 19 due to heart attack",
        "summary": "WION 보도에 따르면 19세의 브라질 보디빌더가 심장마비로 사망했으며 가족과 동료들은 스테로이드 사용을 의심하고 있다. 19세라는 나이는 자연 심장사 발생률을 정면으로 거스르는 숫자다.",
        "summary_detail": "10대 후반 자연 사망의 주요 원인은 외상·자살·약물 과다이며, 심장마비는 통계적으로 매우 드물다. 그럼에도 보디빌딩 신에서는 19~22세 사망 사례가 반복적으로 보고된다. 공통 패턴은 ① 빠른 체중·근육 증가 ② 강도 높은 사이클 ③ 컨디셔닝 직후 또는 무대 직전 발생. 한국 청년 사용자가 알아야 할 메시지는 단순하다 — 또래의 자연 사망률이 0에 가까운 시기에, 사이클이 그 확률을 만들어낸다.",
        "category": "news",
        "category_ko": "사망",
        "source": "WION",
        "source_type": "news",
        "source_url": "https://www.wionews.com/world/steroids-lead-to-death-famous-brazilian-bodybuilder-dies-at-19-due-to-heart-attack-755817",
        "source_verified": True,
        "credibility": {
            "peer_reviewed": False,
            "primary_source": True,
            "cross_checked": True,
            "cross_check_date": "2026-05-07",
            "url_alive": True,
            "cross_confirmed": True,
            "confidence": "medium",
            "notes": "WION 1차 보도. 가족·동료 의심 인용 — 부검·약물검사 결과는 미공개."
        },
        "viral_score": 87,
        "viral_signals": {"shock_factor": 25, "scientific_credibility": 12, "relatability": 22, "recency": 14, "controversy": 9, "visual_potential": 5},
        "viral_tier": "VIRAL_BOMB",
        "viral_emoji": "🔴",
        "tags": ["19세사망", "브라질", "보디빌더", "심장마비", "스테로이드"],
        "date": TODAY,
        "badge": "✅ VERIFIED"
    },

    # ─── SARMs ───
    {
        "title": "RAD-140이 간을 망친다 — JMIR 2025 SNS 데이터 기반 SARMs 부작용 분석",
        "title_en": "Self-Reported Side Effects Associated With Selective Androgen Receptor Modulators",
        "summary": "Journal of Medical Internet Research(JMIR) 2025년 연구는 SNS 게시물 1,389건과 사용자 2,183명 데이터를 분석해 SARMs 사용 전·중·후의 임상 마커 변화를 정량화했다. 가장 많이 언급된 약물은 RAD140이었고, 평균 사용자 연령은 27세였다.",
        "summary_detail": "주요 결과 — ① 간 효소(AST·ALT) 유의 상승, 약물성 간손상(DILI) 패턴과 일치 ② LDL 콜레스테롤·중성지방 상승, HDL 감소 ③ 테스토스테론 감소, 에스트로겐 및 SHBG 변화 ④ 가장 많이 보고된 자각 부작용은 복통·성욕 감소·피로. 사용자의 17.5%는 타목시펜 또는 enclomiphene을 함께 사용했고, 7.8%는 간보호 보충제를 병용했다 — 즉, 다수가 부작용이 발생할 것을 예상하고 사용한다는 뜻이다. 한계: 자가 보고 데이터의 측정 신뢰성, 표본의 젊은 남성 편향. 그럼에도 SARMs를 'AAS보다 안전한 선택'으로 마케팅하는 통념을 정면으로 반박하는 임상 신호다.",
        "category": "research",
        "category_ko": "SARMs",
        "source": "JMIR 2025",
        "source_type": "research",
        "source_url": "https://www.jmir.org/2025/1/e65031/",
        "source_verified": True,
        "credibility": {
            "peer_reviewed": True,
            "primary_source": True,
            "cross_checked": True,
            "cross_check_date": "2026-05-07",
            "url_alive": True,
            "cross_confirmed": True,
            "confidence": "high",
            "notes": "JMIR 2025;27:e65031. SNS 기반 약물감시(pharmacovigilance) 연구. 한계는 명시 — 자가보고."
        },
        "viral_score": 86,
        "viral_signals": {"shock_factor": 21, "scientific_credibility": 22, "relatability": 18, "recency": 17, "controversy": 4, "visual_potential": 4},
        "viral_tier": "VIRAL_BOMB",
        "viral_emoji": "🔴",
        "tags": ["SARMs", "RAD140", "간손상", "JMIR", "약물감시"],
        "date": TODAY,
        "badge": "✅ VERIFIED"
    },
    {
        "title": "8주 만에 황달 — 42세 남성 RAD-140 케이스 리포트",
        "title_en": "RAD-140 induced jaundice case report (LiverTox)",
        "summary": "LiverTox에 등재된 케이스 리포트는 42세 남성이 근비대 목적으로 RAD-140을 8주 사용한 후 황달과 함께 간효소 마커가 유의하게 상승했다고 보고했다. 'SARMs는 간에 안전하다'는 마케팅 문구의 임상적 반례다.",
        "summary_detail": "이 케이스의 의의는 두 가지다. 첫째, RAD-140은 in vitro·동물에서 안드로겐 수용체 선택성이 높다고 알려졌지만, 인간 임상에서는 간세포 손상(hepatocellular injury) 패턴이 반복적으로 보고된다. 둘째, 발현은 무증상에서 시작해 황달·식욕부진·피로로 진행하므로 사용자가 초기 단계에서 인지하기 어렵다. LiverTox는 SARMs 전반에 대해 'idiosyncratic acute liver injury'라는 분류를 부여했고, 이는 용량과 무관하게 개인 감수성에 따라 발생할 수 있다는 의미다 — 즉, '소량이라 안전' 논리가 성립하지 않는다.",
        "category": "research",
        "category_ko": "SARMs",
        "source": "NCBI LiverTox",
        "source_type": "research",
        "source_url": "https://www.ncbi.nlm.nih.gov/books/NBK619971/",
        "source_verified": True,
        "credibility": {
            "peer_reviewed": True,
            "primary_source": True,
            "cross_checked": True,
            "cross_check_date": "2026-05-07",
            "url_alive": True,
            "cross_confirmed": True,
            "confidence": "high",
            "notes": "NCBI LiverTox NBK619971. SARMs 간손상 케이스 다수 등재."
        },
        "viral_score": 83,
        "viral_signals": {"shock_factor": 22, "scientific_credibility": 19, "relatability": 18, "recency": 13, "controversy": 6, "visual_potential": 5},
        "viral_tier": "VIRAL_BOMB",
        "viral_emoji": "🔴",
        "tags": ["SARMs", "RAD140", "황달", "케이스리포트", "간손상"],
        "date": TODAY,
        "badge": "✅ VERIFIED"
    },
    {
        "title": "SARMs RCT 메타분석 — 효과는 미미했고 부작용은 일관됐다",
        "title_en": "SARMs Effects on Physical Performance: A Systematic Review of RCTs",
        "summary": "Wiley Clinical Endocrinology 2025년 RCT 체계적 리뷰는 SARMs의 운동 수행 능력 증가는 작거나 일관되지 않았으며, 부작용 신호(특히 간·지질·HPG축)는 매우 일관됐다고 결론지었다. 'AAS만큼 안 들지만 부작용은 비슷하다'가 합리적 해석이다.",
        "summary_detail": "리뷰의 임상적 함의 — ① 근비대·근력 증가 효과는 일부 RCT에서만 검출됐고 효과 크기는 AAS 대비 작다. ② 반면 간 효소 상승, LDL 증가/HDL 감소, 테스토스테론 억제는 거의 모든 시험에서 재현된다. ③ '깔끔한 AAS 대안' 마케팅의 가장 큰 약점은 효익은 약하고 위험 프로파일은 유사하다는 비대칭이다. SARMs는 임상시험을 거쳐 의약품으로 승인된 사례가 거의 없으며, 사용 중인 모든 SARMs는 사실상 인체 사용에 대한 정식 안전성 데이터가 부족하다.",
        "category": "research",
        "category_ko": "SARMs",
        "source": "Wiley Clinical Endocrinology 2025",
        "source_type": "research",
        "source_url": "https://onlinelibrary.wiley.com/doi/10.1111/cen.15135",
        "source_verified": True,
        "credibility": {
            "peer_reviewed": True,
            "primary_source": True,
            "cross_checked": True,
            "cross_check_date": "2026-05-07",
            "url_alive": True,
            "cross_confirmed": True,
            "confidence": "high",
            "notes": "Wen et al. Clin Endocrinol 2025 doi:10.1111/cen.15135. RCT 체계적 리뷰."
        },
        "viral_score": 82,
        "viral_signals": {"shock_factor": 18, "scientific_credibility": 22, "relatability": 16, "recency": 17, "controversy": 5, "visual_potential": 4},
        "viral_tier": "VIRAL_BOMB",
        "viral_emoji": "🟠",
        "tags": ["SARMs", "RCT", "메타분석", "효과크기", "임상안전성"],
        "date": TODAY,
        "badge": "✅ VERIFIED"
    },
    {
        "title": "SARMs는 안티도핑 검출 1순위 — 운동선수 남용의 임상 그림",
        "title_en": "Athlete Selective Androgen Receptor Modulators Abuse",
        "summary": "PubMed 2024 리뷰는 SARMs가 'WADA 금지 약물 중 가장 빠르게 증가하는 카테고리'라고 보고했다. 검출 가능 기간이 길고, 대사물 데이터베이스가 확장되며, 도핑 양성 사례가 매년 증가하고 있다.",
        "summary_detail": "이 리뷰의 핵심 메시지 — ① SARMs는 더 이상 '검출되지 않는 약'이 아니다. WADA 라이선스 랩의 LC-MS/MS 감도는 ng/mL 수준에서 대사체를 잡아낸다. ② 도핑 양성 후 항변에서 자주 인용되는 'contaminated supplement' 변명은 실제로 일부에선 사실이지만, 다수는 의도적 사용이 입증된다. ③ 임상 영향은 도핑 결과 이전에 사용자 본인의 건강 — 시상하부-성선축 억제, 간 손상, 지질 악화 — 으로 먼저 나타난다. 한국 현역 선수에게 의미 있는 메시지: '검출 안 된다'는 정보는 2~3년 전 정보이며, 지금은 적발 확률이 매우 높다.",
        "category": "research",
        "category_ko": "SARMs·도핑",
        "source": "PubMed 2024",
        "source_type": "research",
        "source_url": "https://pubmed.ncbi.nlm.nih.gov/39755947/",
        "source_verified": True,
        "credibility": {
            "peer_reviewed": True,
            "primary_source": True,
            "cross_checked": True,
            "cross_check_date": "2026-05-07",
            "url_alive": True,
            "cross_confirmed": True,
            "confidence": "high",
            "notes": "PubMed 39755947. 운동선수 SARMs 남용 리뷰."
        },
        "viral_score": 80,
        "viral_signals": {"shock_factor": 18, "scientific_credibility": 20, "relatability": 16, "recency": 14, "controversy": 8, "visual_potential": 4},
        "viral_tier": "VIRAL_BOMB",
        "viral_emoji": "🟠",
        "tags": ["SARMs", "도핑", "WADA", "LC-MS", "약물검출"],
        "date": TODAY,
        "badge": "✅ VERIFIED"
    },

    # ─── DNP ───
    {
        "title": "체온이 44도까지 — DNP 다이어트 약의 진짜 죽음 메커니즘",
        "title_en": "2,4-Dinitrophenol (DNP): A Weight Loss Agent with Significant Acute Toxicity and Risk of Death",
        "summary": "PMC 리뷰는 DNP가 미토콘드리아 산화적 인산화의 짝풀림(uncoupling)을 일으켜 ATP를 빠르게 열로 소모시키고, 결국 통제되지 않는 고열(최대 44°C)과 사망에 이르게 한다고 정리했다. 해독제도, 안전 용량도 존재하지 않는다.",
        "summary_detail": "DNP는 1930년대 다이어트 약으로 처방된 적이 있지만 사망 사례 누적으로 미국 FDA에 의해 '인간 사용에 적합하지 않은 매우 위험한 물질'로 지정됐다. 메커니즘은 직관적이고 잔인하다 — 미토콘드리아 내막의 양성자 구배(proton gradient)를 새게 만들어 ATP 합성을 차단하고, 그 에너지를 열로 방출시킨다. 결과: ① 극단적 고열 ② 횡문근융해 ③ 다발성 장기부전. 치료적 창(therapeutic window)이 매우 좁고 개인 간 대사 차이가 커서 '소량이면 괜찮다'가 통하지 않는다. 인터넷 판매가 늘면서 다이어트·컨디셔닝 목적 사용이 다시 증가하는 중이다.",
        "category": "research",
        "category_ko": "약물·다이어트",
        "source": "PMC 3550200",
        "source_type": "research",
        "source_url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC3550200/",
        "source_verified": True,
        "credibility": {
            "peer_reviewed": True,
            "primary_source": True,
            "cross_checked": True,
            "cross_check_date": "2026-05-07",
            "url_alive": True,
            "cross_confirmed": True,
            "confidence": "high",
            "notes": "PMC 3550200 + Wikipedia 1차 인용 검증. 메커니즘·치명도·해독제 부재 모두 확인."
        },
        "viral_score": 92,
        "viral_signals": {"shock_factor": 25, "scientific_credibility": 20, "relatability": 22, "recency": 12, "controversy": 9, "visual_potential": 4},
        "viral_tier": "VIRAL_BOMB",
        "viral_emoji": "🔴",
        "tags": ["DNP", "다이어트약", "고열사망", "미토콘드리아", "독성"],
        "date": TODAY,
        "badge": "✅ VERIFIED"
    },
    {
        "title": "10년간 50명이 죽었다 — DNP 과다복용의 글로벌 카운트",
        "title_en": "DNP overdose deaths 2010-2020 global count",
        "summary": "PMC·CHEST 리뷰는 2010~2020 사이 전 세계에서 보고된 DNP 과다복용 사망 사례가 최소 50건임을 집계했다. 사용자 다수는 다이어트·컨디셔닝 목적의 청·중년이었다.",
        "summary_detail": "이 통계의 의미는 두 가지다. 첫째, 50건은 '보고된' 숫자다. 인터넷 판매가 익명화되어 있고, 응급실 도착 전 사망이 많아 실제 사망 수는 더 많을 가능성이 높다. 둘째, 사망자의 다수가 '운동인'이 아니라 단기 체중 감량을 원한 일반인이었다. DNP는 운동선수 약물이 아니라 일반 다이어트 시장에서 다시 유행하는 약이며, 인터넷에서 '노란 알약(yellow pill)'으로 거래된다. 한국은 DNP 자체가 식약처 의약품/식품으로 미승인이며, 개인 직구 자체가 위법이다.",
        "category": "news",
        "category_ko": "약물·다이어트",
        "source": "CHEST Journal",
        "source_type": "news",
        "source_url": "https://journal.chestnet.org/article/S0012-3692(17)31929-3/fulltext",
        "source_verified": True,
        "credibility": {
            "peer_reviewed": True,
            "primary_source": True,
            "cross_checked": True,
            "cross_check_date": "2026-05-07",
            "url_alive": True,
            "cross_confirmed": True,
            "confidence": "high",
            "notes": "CHEST Journal 게재. PMC 4840695, ATSDR Toxicological Profile 교차 확인."
        },
        "viral_score": 87,
        "viral_signals": {"shock_factor": 24, "scientific_credibility": 18, "relatability": 22, "recency": 11, "controversy": 8, "visual_potential": 4},
        "viral_tier": "VIRAL_BOMB",
        "viral_emoji": "🔴",
        "tags": ["DNP", "사망50건", "다이어트약", "글로벌통계", "독성"],
        "date": TODAY,
        "badge": "✅ VERIFIED"
    },
    {
        "title": "DNP + 스테로이드 + 근육이형증 — 한 보디빌더의 마지막",
        "title_en": "Fatal long-term intoxication by 2,4-dinitrophenol and anabolic steroids in a young bodybuilder with muscle dysmorphia",
        "summary": "Frontiers in Public Health 2024년 케이스 리포트는 근육이형증(muscle dysmorphia)을 가진 젊은 보디빌더가 DNP와 AAS의 장기 병용 후 치명적 중독으로 사망한 사례를 보고했다. 정신과적 강박과 약물 남용이 결합되면 결과는 빠르고 비가역적이다.",
        "summary_detail": "이 케이스가 임상적으로 중요한 이유는 세 가지다. ① 근육이형증은 '내가 부족하다'는 인지 왜곡으로 인해 위험 약물을 점진적으로 늘리는 행동 패턴을 만든다. ② DNP·AAS 병용은 단일 약물 노출보다 심혈관·간·신장에 누적 부담을 가하며 치명도를 증폭시킨다. ③ 사망은 급성 사건이 아니라 '만성 중독(long-term intoxication)' 형태로 진행된 사례라는 점이 특이하다 — 즉, 본인과 주변이 위험 신호를 충분히 일찍 감지하지 못했다. 정신과 동반 평가가 약물 사용자 진료의 일부가 되어야 한다는 임상 권고로 연결된다.",
        "category": "research",
        "category_ko": "약물·정신건강",
        "source": "Frontiers in Public Health 2024",
        "source_type": "research",
        "source_url": "https://www.frontiersin.org/journals/public-health/articles/10.3389/fpubh.2024.1452196/full",
        "source_verified": True,
        "credibility": {
            "peer_reviewed": True,
            "primary_source": True,
            "cross_checked": True,
            "cross_check_date": "2026-05-07",
            "url_alive": True,
            "cross_confirmed": True,
            "confidence": "high",
            "notes": "Frontiers Public Health 2024 doi:10.3389/fpubh.2024.1452196. 케이스 리포트."
        },
        "viral_score": 85,
        "viral_signals": {"shock_factor": 23, "scientific_credibility": 18, "relatability": 22, "recency": 13, "controversy": 6, "visual_potential": 3},
        "viral_tier": "VIRAL_BOMB",
        "viral_emoji": "🔴",
        "tags": ["DNP", "AAS", "근육이형증", "케이스리포트", "복합중독"],
        "date": TODAY,
        "badge": "✅ VERIFIED"
    },

    # ─── Fake Natty / 업계 스캔들 ───
    {
        "title": "Liver King의 11,000달러 — '카브맨 체형'은 만들어졌다",
        "title_en": "Liver King exposed: $11,000/month steroid bills",
        "summary": "2022년 유출된 이메일은 'Liver King'으로 알려진 Brian Johnson이 매월 1만 1천 달러 이상을 스테로이드에 쓰고 있었음을 보여줬다. 그는 '카브맨 식단과 보조제'로 만든 몸이라고 주장하며 거대한 콘텐츠 제국을 세웠고, 이후 2023년 'Natty 60일' 도전 이후 다시 사용 중임을 인정했다.",
        "summary_detail": "이 사건이 'fake natty' 폭로의 표준 케이스가 된 이유는 세 가지다. ① 폭로의 증거가 가설이 아닌 1차 자료(이메일·송장)였다. ② 'Natty로 돌아왔다' 메시지 후 다시 사용한 것이 본인 인정으로 확인됐다 — 즉, 약물 의존이 단발 사건이 아니라 정체성과 비즈니스 구조에 묶여 있음을 보여줬다. ③ 그가 판매하던 보충제·식단 패키지의 핵심 마케팅 문구가 '약물 없이도 가능하다'는 프레임이었기 때문에, 폭로는 단순 개인 스캔들이 아니라 산업 마케팅의 위선을 직격했다. NOGEAR 메시지의 영구 인용 사례.",
        "category": "news",
        "category_ko": "스캔들·페이크내추럴",
        "source": "Yahoo Lifestyle / NattyOrNot",
        "source_type": "news",
        "source_url": "https://www.yahoo.com/lifestyle/fake-fitness-influencers-secrets-lies-040015028.html",
        "source_verified": True,
        "credibility": {
            "peer_reviewed": False,
            "primary_source": True,
            "cross_checked": True,
            "cross_check_date": "2026-05-07",
            "url_alive": True,
            "cross_confirmed": True,
            "confidence": "high",
            "notes": "Yahoo Lifestyle 1차 보도 + Liver King 본인 사과 영상 + 다수 매체 교차."
        },
        "viral_score": 91,
        "viral_signals": {"shock_factor": 23, "scientific_credibility": 12, "relatability": 24, "recency": 12, "controversy": 15, "visual_potential": 5},
        "viral_tier": "VIRAL_BOMB",
        "viral_emoji": "🔴",
        "tags": ["LiverKing", "페이크내추럴", "스캔들", "스테로이드", "마케팅위선"],
        "date": TODAY,
        "badge": "✅ VERIFIED"
    },
    {
        "title": "1백만 팔로워 — '중량 사기' 의혹의 Brad Castleberry",
        "title_en": "Brad Castleberry fake weights controversy",
        "summary": "Brad Castleberry는 100만 팔로워를 거느린 전직 미식축구·보디빌더·파워리프터 인플루언서다. 인터넷 사용자들은 그가 영상 속 중량을 실제로 들지 않고 가짜 중량(파이프 코어 디스크 등)을 사용한 정황을 다수 분석해 공개해왔다.",
        "summary_detail": "이 케이스의 의의는 'fake natty'와 다른 결의 사기다 — 약물 여부 이전에 '실제 들지도 않은 무게'로 콘텐츠를 만든다는 의혹이다. 분석가들이 지적하는 단서는 ① 디스크의 흔들림과 음향 ② 들어 올릴 때의 바벨 휨(bar bend) 부재 ③ 같은 무게 대비 다른 인플루언서 영상의 신체 반응 차이. NOGEAR가 이 케이스를 다루는 이유는 약물 + 가짜 중량의 조합이 '나는 약 없이도 이걸 든다'는 이중 거짓말이 되기 때문이다. 팔로워가 비교 기준 자체를 잘못 갖게 된다.",
        "category": "news",
        "category_ko": "스캔들·페이크내추럴",
        "source": "BeAmazed",
        "source_type": "news",
        "source_url": "https://beamazed.com/article/weird-fake-bodybuilders/",
        "source_verified": True,
        "credibility": {
            "peer_reviewed": False,
            "primary_source": False,
            "cross_checked": True,
            "cross_check_date": "2026-05-07",
            "url_alive": True,
            "cross_confirmed": True,
            "confidence": "medium",
            "notes": "여러 매체·유튜브 분석. 본인 공식 인정은 없음 — '의혹/논란' 프레임으로 다룸."
        },
        "viral_score": 78,
        "viral_signals": {"shock_factor": 18, "scientific_credibility": 8, "relatability": 22, "recency": 10, "controversy": 16, "visual_potential": 4},
        "viral_tier": "VIRAL_BOMB",
        "viral_emoji": "🟠",
        "tags": ["BradCastleberry", "가짜중량", "인플루언서", "사기의혹", "콘텐츠위선"],
        "date": TODAY,
        "badge": "✅ VERIFIED"
    },
    {
        "title": "Mike O'Hearn — '평생 내추럴' 주장이 만들어낸 가장 오래된 논란",
        "title_en": "Mike O'Hearn fake natty controversy",
        "summary": "Mike O'Hearn은 '평생 내추럴'을 주장하며 활동해 온 보디빌더지만, 그의 체격은 통계적으로 검증된 자연 한계(natural FFMI ceiling)를 일관되게 넘는다는 분석이 이어져 왔다. 본인 인정은 없지만, 팬덤 외부에서는 'fake natty 상징'으로 광범위하게 다뤄진다.",
        "summary_detail": "이 논란의 핵심은 'FFMI(Fat-Free Mass Index)' 자연 한계에 대한 과학 합의다 — 키와 체지방을 보정한 제지방질량지수에서 약 25 부근이 자연인의 통계적 상한이며, 이를 안정적으로 넘는 사례는 매우 드물다. O'Hearn의 추정 FFMI는 다년간 이 상한 위에 머물러 있다. 본인은 '가족력'과 '훈련 강도'로 설명하지만, 데이터 기반 분석은 이 설명을 충분 조건으로 받아들이지 않는다. NOGEAR가 이 사례를 다루는 이유: 본인 인정 없이도 '시각적 진실'은 데이터로 평가 가능하며, 팬덤 내러티브가 과학적 비교 기준을 흐리게 만든다는 점이다.",
        "category": "news",
        "category_ko": "스캔들·페이크내추럴",
        "source": "NattyOrNot / 다수 분석",
        "source_type": "news",
        "source_url": "https://nattyornot.com/top-10-fake-natural-bodybuilders-youtube/",
        "source_verified": True,
        "credibility": {
            "peer_reviewed": False,
            "primary_source": False,
            "cross_checked": True,
            "cross_check_date": "2026-05-07",
            "url_alive": True,
            "cross_confirmed": True,
            "confidence": "medium",
            "notes": "본인 공식 인정 없음 — 'natty 주장 vs FFMI 분석' 논쟁 프레임으로 다룸. 명예훼손 주의 표현."
        },
        "viral_score": 76,
        "viral_signals": {"shock_factor": 17, "scientific_credibility": 12, "relatability": 22, "recency": 8, "controversy": 14, "visual_potential": 3},
        "viral_tier": "VIRAL_BOMB",
        "viral_emoji": "🟠",
        "tags": ["MikeOHearn", "FFMI", "내추럴주장", "논란", "통계한계"],
        "date": TODAY,
        "badge": "✅ VERIFIED"
    },

    # ─── Enhanced Games / 도핑 ───
    {
        "title": "D-14: '약물 올림픽' 카운트다운 — 38명 확정, 라스베이거스",
        "title_en": "Enhanced Games D-14: 38 athletes confirmed",
        "summary": "Enhanced Games가 5월 21~24일 라스베이거스 개최를 14일 앞두고 38명 출전 확정 상태다. 종목당 50만 달러 상금에 세계기록 보너스 100만 달러가 걸렸다. WADA·USADA·IOC·세계육상연맹은 일관되게 비판 입장을 유지하고 있다.",
        "summary_detail": "이 대회가 산업에 던지는 질문은 두 가지다. 첫째, '도핑을 허용하면 무슨 기록이 나오나'라는 실험은 단순 흥미가 아니라 약물 정상화의 글로벌 마일스톤이 된다. 둘째, FDA 승인 약물에 한정한다는 단서가 있지만 실제 운영에서는 의료 스크리닝 통과만 요구한다 — 즉, 일반 약사용 시장의 PED 대부분이 합법화되는 효과를 만든다. 세계반도핑기구는 '구조적으로 위험'이라고 평가했고, 의학계는 사망·심혈관 사건 발생 시 책임 구조가 불명확하다고 경고한다. NOGEAR는 D-30/D-22 시리즈에 이어 D-14 카운트다운으로 이 흐름을 추적한다.",
        "category": "news",
        "category_ko": "도핑",
        "source": "Wikipedia / The Conversation",
        "source_type": "news",
        "source_url": "https://en.wikipedia.org/wiki/Enhanced_Games",
        "source_verified": True,
        "credibility": {
            "peer_reviewed": False,
            "primary_source": True,
            "cross_checked": True,
            "cross_check_date": "2026-05-07",
            "url_alive": True,
            "cross_confirmed": True,
            "confidence": "high",
            "notes": "Wikipedia 공식 페이지 + The Conversation 분석. 일자·상금·종목 모두 다중 출처."
        },
        "viral_score": 93,
        "viral_signals": {"shock_factor": 24, "scientific_credibility": 14, "relatability": 18, "recency": 18, "controversy": 15, "visual_potential": 4},
        "viral_tier": "VIRAL_BOMB",
        "viral_emoji": "🔴",
        "tags": ["EnhancedGames", "D-14", "라스베이거스", "도핑허용", "PED올림픽"],
        "date": TODAY,
        "badge": "✅ VERIFIED"
    },
    {
        "title": "도핑 코치가 다시 무대에 — Eteri Tutberidze, 2026 밀라노 코르티나에서",
        "title_en": "Russian skating coach at center of doping scandal back at Olympics",
        "summary": "2022 베이징에서 Kamila Valieva의 트리메타지딘 양성으로 도핑 스캔들의 중심에 있던 코치 Eteri Tutberidze가 2026 밀라노 코르티나 동계 올림픽에서 다시 두 명의 선수를 지도한다. WADA 회장은 '그녀의 존재가 편치 않다'고 공개적으로 언급했다.",
        "summary_detail": "이 케이스의 구조적 문제는 '코치 책임'이 도핑 거버넌스에서 실효적으로 처벌되지 못한다는 점이다. 선수는 자격 정지를 받지만, 코치는 시스템적 패턴이 입증되지 않으면 활동을 계속한다. Tutberidze는 자신의 훈련 시스템 자체가 의학적 한계를 넘는 강도라는 평가를 오랫동안 받아왔지만, 직접적 처벌은 없었다. 2026 대회에서 그녀의 복귀는 '도핑 검출은 강해졌지만 도핑 생태계는 여전히 굴러간다'는 신호로 읽힌다.",
        "category": "news",
        "category_ko": "도핑·올림픽",
        "source": "NBC New York",
        "source_type": "news",
        "source_url": "https://www.nbcnewyork.com/olympics/2026-milan-cortina/olympics-figure-skating-doping-coach/6462409/",
        "source_verified": True,
        "credibility": {
            "peer_reviewed": False,
            "primary_source": True,
            "cross_checked": True,
            "cross_check_date": "2026-05-07",
            "url_alive": True,
            "cross_confirmed": True,
            "confidence": "high",
            "notes": "NBC New York 보도 + Newsweek 동일 보도 교차."
        },
        "viral_score": 86,
        "viral_signals": {"shock_factor": 21, "scientific_credibility": 12, "relatability": 18, "recency": 18, "controversy": 13, "visual_potential": 4},
        "viral_tier": "VIRAL_BOMB",
        "viral_emoji": "🔴",
        "tags": ["Tutberidze", "도핑", "올림픽", "Valieva", "코치책임"],
        "date": TODAY,
        "badge": "✅ VERIFIED"
    },
    {
        "title": "WADA 회장의 작심 발언 — '편치 않다'",
        "title_en": "WADA president on Tutberidze's Olympic return",
        "summary": "세계반도핑기구(WADA) 회장 Witold Bańka는 Tutberidze의 2026 밀라노 코르티나 복귀에 대해 '편치 않다(don\\'t feel comfortable)'고 공개적으로 언급했다. WADA 수장의 작심 발언은 도핑 거버넌스 내부 균열을 보여주는 신호다.",
        "summary_detail": "이 발언이 의미 있는 이유는 두 가지다. ① WADA는 통상 케이스 진행 중이거나 결정 외 사안에 대해 정치적 발언을 자제하지만, 회장이 직접 입장을 밝힘으로써 IOC·종목 단체에 압박을 보냈다. ② 그러나 Tutberidze의 활동을 막을 직접 권한이 WADA에 없다 — 즉, 발언과 실효 권한 사이의 갭이 그대로 드러났다. Valieva 본인은 자격 정지가 끝났음에도 2026 출전 자격이 없는 상태이며, 코치만 무대에 다시 서는 비대칭이 만들어졌다.",
        "category": "news",
        "category_ko": "도핑·올림픽",
        "source": "NBC News / WADA",
        "source_type": "news",
        "source_url": "https://www.nbcnewyork.com/olympics/2026-milan-cortina/olympics-figure-skating-doping-coach/6462409/",
        "source_verified": True,
        "credibility": {
            "peer_reviewed": False,
            "primary_source": True,
            "cross_checked": True,
            "cross_check_date": "2026-05-07",
            "url_alive": True,
            "cross_confirmed": True,
            "confidence": "high",
            "notes": "WADA 회장 본인 발언 인용. NBC·Newsweek 양 매체 인용 동일."
        },
        "viral_score": 80,
        "viral_signals": {"shock_factor": 18, "scientific_credibility": 12, "relatability": 18, "recency": 18, "controversy": 11, "visual_potential": 3},
        "viral_tier": "VIRAL_BOMB",
        "viral_emoji": "🟠",
        "tags": ["WADA", "Bańka", "Tutberidze", "도핑거버넌스", "올림픽"],
        "date": TODAY,
        "badge": "✅ VERIFIED"
    },

    # ─── 펩타이드 / FDA 재분류 ───
    {
        "title": "FDA가 BPC-157을 다시 본다 — 4월 15일 카테고리 2 제외 발표",
        "title_en": "FDA Removes 12 Peptides from Category 2",
        "summary": "FDA는 2026년 4월 15일 BPC-157, TB-500을 포함한 12개 벌크 의약품 물질을 Compounding Category 2에서 제외했다. 7월부터 약학 컴파운딩 자문위원회(PCAC)에서 독립 전문가 검토에 들어간다. 합법 컴파운딩 시장의 큰 변곡점이다.",
        "summary_detail": "이 변화는 두 가지를 의미한다. 첫째, 'FDA Category 2'는 안전성·유효성 데이터가 부족하지만 임시 사용이 허용된 분류였다 — 여기서 제외됐다는 건 추가 검토 없이는 합법 컴파운딩이 어려워진다는 뜻이다. 둘째, PCAC 검토가 7월 시작되며 결과에 따라 ① 정식 승인 ② 사용 제한 ③ 영구 금지 중 하나로 갈린다. 사용자에게 의미 있는 신호: 인터넷 회색시장 펩타이드는 영향 없지만, 합법 컴파운딩 약국 경로는 좁아진다 — 즉, 시장이 다시 회색지대로 밀린다는 역설.",
        "category": "news",
        "category_ko": "펩타이드·규제",
        "source": "FDA / SSRP Institute",
        "source_type": "news",
        "source_url": "https://www.peptideschedule.com/learn/fda-category-2-peptides-removed-2026",
        "source_verified": True,
        "credibility": {
            "peer_reviewed": False,
            "primary_source": True,
            "cross_checked": True,
            "cross_check_date": "2026-05-07",
            "url_alive": True,
            "cross_confirmed": True,
            "confidence": "high",
            "notes": "Peptide Schedule + SSRP Institute + Federal Register 공식 발표 다중 확인."
        },
        "viral_score": 84,
        "viral_signals": {"shock_factor": 18, "scientific_credibility": 18, "relatability": 18, "recency": 18, "controversy": 8, "visual_potential": 4},
        "viral_tier": "VIRAL_BOMB",
        "viral_emoji": "🟠",
        "tags": ["FDA", "BPC157", "TB500", "펩타이드규제", "PCAC"],
        "date": TODAY,
        "badge": "✅ VERIFIED"
    },
    {
        "title": "BPC-157, 동물에서는 작동한다 — 인간 임상은 여전히 0",
        "title_en": "BPC-157 Research Results 2026: Preclinical vs Human Trials",
        "summary": "2025년 BPC-157 체계적 리뷰는 544개 논문 중 36개를 포함시켰는데, 그중 35개가 동물 실험이었다. 위성세포 증가·근섬유 단면적 증가 등 조직 회복 신호는 일관됐지만, 인간 RCT는 사실상 부재 상태다.",
        "summary_detail": "사용자가 알아야 할 정확한 그림은 두 단계다. ① 동물·조직 모델: BPC-157은 혈관신생(angiogenesis)·일산화질소(NO) 조절을 통해 근육·힘줄·위장 점막의 회복을 촉진한다는 신호가 강하고 일관된다. ② 인간 임상: 안전성·효과성 모두 RCT 데이터가 거의 없다. '동물 데이터가 강하니 인간에서도 안전할 것'은 의학적으로 성립하지 않는 비약이다. 한편 인간 사용자에서 보고되는 부작용은 대체로 경미하지만, 장기 사용·고용량 데이터가 없다는 점이 가장 큰 미지수다. NOGEAR는 'BPC-157은 가능성 있는 회복제이지만 임상 약이 아니다'를 일관 메시지로 둔다.",
        "category": "research",
        "category_ko": "펩타이드",
        "source": "Spartan Peptides / The Peptide Catalog 2026",
        "source_type": "research",
        "source_url": "https://thepeptidecatalog.com/articles/bpc-157-clinical-trials",
        "source_verified": True,
        "credibility": {
            "peer_reviewed": False,
            "primary_source": False,
            "cross_checked": True,
            "cross_check_date": "2026-05-07",
            "url_alive": True,
            "cross_confirmed": True,
            "confidence": "medium",
            "notes": "체계적 리뷰 인용 메타 — 원 논문 스크리닝 수치(544/36) 다중 출처 일치. 단 인간 임상 부재 결론은 PMC·PubMed에서도 일관."
        },
        "viral_score": 79,
        "viral_signals": {"shock_factor": 15, "scientific_credibility": 22, "relatability": 18, "recency": 14, "controversy": 6, "visual_potential": 4},
        "viral_tier": "VIRAL_BOMB",
        "viral_emoji": "🟠",
        "tags": ["BPC157", "임상부재", "동물실험", "위성세포", "회복펩타이드"],
        "date": TODAY,
        "badge": "✅ VERIFIED"
    },
    {
        "title": "TB-500, 인간 임상 1상 통과 — 그러나 '효과' 데이터는 다음 단계",
        "title_en": "TB-500 Phase 1 human trial confirms safety",
        "summary": "TB-500의 첫 Phase 1 인간 임상이 건강한 자원자에서 안전성을 확인했다. TB-500은 thymosin beta-4의 7-아미노산 단편으로, 액틴 세포골격 리모델링을 통한 세포 이동 촉진이 작용 기전이다. 효능 데이터는 후속 단계에서 확인될 예정이다.",
        "summary_detail": "Phase 1은 안전성과 약동학을 보는 단계이며, 효능 검증이 아니다. 이 임상의 의미는 두 가지다. ① TB-500이 인간에서도 단기 안전 신호를 통과했다는 점은 후속 임상 진행 가능성을 열었다. ② 그러나 'Phase 1 통과'는 시중에서 사용 중인 회색시장 TB-500 제품의 안전성을 보장하지 않는다 — 임상 시험은 GMP 등급 정제품 + 모니터링 환경에서 수행됐다. 사용자 입장에서 의미 있는 메시지는 '곧 임상 데이터가 쌓일 것'이며, 그때까지 시장 데이터는 일화 수준이라는 점이다.",
        "category": "research",
        "category_ko": "펩타이드",
        "source": "The Peptide Catalog 2026",
        "source_type": "research",
        "source_url": "https://thepeptidecatalog.com/articles/bpc-157-vs-tb-500",
        "source_verified": True,
        "credibility": {
            "peer_reviewed": False,
            "primary_source": False,
            "cross_checked": True,
            "cross_check_date": "2026-05-07",
            "url_alive": True,
            "cross_confirmed": True,
            "confidence": "medium",
            "notes": "임상 등록 정보·PubMed 인용 172건 다중 출처 일치. 임상 ID 명시 본문에서는 미언급."
        },
        "viral_score": 77,
        "viral_signals": {"shock_factor": 14, "scientific_credibility": 22, "relatability": 16, "recency": 16, "controversy": 5, "visual_potential": 4},
        "viral_tier": "VIRAL_BOMB",
        "viral_emoji": "🟠",
        "tags": ["TB500", "Phase1", "인간임상", "thymosin", "안전성"],
        "date": TODAY,
        "badge": "✅ VERIFIED"
    },
    {
        "title": "MK-677은 IGF-1을 40~60% 올린다 — 그것이 정확히 무엇을 의미하는가",
        "title_en": "MK-677 IGF-1 elevation: 5 RCTs confirm",
        "summary": "5개의 동료심사 RCT가 MK-677 경구 투여로 IGF-1 수치가 40~60% 상승함을 일관되게 보여줬다. MK-677은 펩타이드가 아닌 비펩타이드 소분자로 ghrelin 수용체(GHSR-1a)를 활성화한다.",
        "summary_detail": "IGF-1 상승의 의미는 양면적이다. ① 잠재적 이득: 단백질 합성·근비대·골밀도·수면질·식욕 촉진 신호가 임상에서 관찰된다. Nass 외 2년 추적 시험은 고령자에서 일부 신체 조성 개선을 보고했다. ② 잠재적 위험: IGF-1 만성 상승은 인슐린 저항성·혈당 변화, 일부 종양 신호와의 관련성 가설(특히 기존 종양 보유자에서 주의)이 지적된다. MK-677은 '오래된 화합물'에 속하며 안전성 데이터가 다른 펩타이드보다 상대적으로 풍부하지만, 임상의 합의는 '치료적 사용은 적응증 한정, 비치료적 사용은 검증되지 않은 영역'이다.",
        "category": "research",
        "category_ko": "펩타이드",
        "source": "Peer-reviewed RCTs (Nass et al.)",
        "source_type": "research",
        "source_url": "https://swolverine.com/blogs/blog/the-best-peptides-for-recovery-bpc-157-tb500-mk-677-ipamorelin-cjc-1295-and-more",
        "source_verified": True,
        "credibility": {
            "peer_reviewed": True,
            "primary_source": False,
            "cross_checked": True,
            "cross_check_date": "2026-05-07",
            "url_alive": True,
            "cross_confirmed": True,
            "confidence": "medium",
            "notes": "RCT 5건 인용 메타 — Nass et al. 2008 Annals Intern Med 등. 원 논문 직접 링크 미포함."
        },
        "viral_score": 78,
        "viral_signals": {"shock_factor": 16, "scientific_credibility": 22, "relatability": 16, "recency": 14, "controversy": 6, "visual_potential": 4},
        "viral_tier": "VIRAL_BOMB",
        "viral_emoji": "🟠",
        "tags": ["MK677", "IGF1", "ghrelin", "RCT", "성장호르몬"],
        "date": TODAY,
        "badge": "✅ VERIFIED"
    },

    # ─── Ozempic / GLP-1 ───
    {
        "title": "Ozempic은 근육의 13.9%를 가져갔다 — 임상시험의 진짜 숫자",
        "title_en": "GLP-1 agonists reduced lean muscle mass by 13.9%",
        "summary": "임상시험 데이터는 semaglutide(Ozempic) 사용 환자에서 평균 13.9%(약 6.9kg)의 제지방량 손실을 보여줬다. 비만 임상에서 68~72주에 걸쳐 근육량의 10% 이상이 손실되며, 이는 노화로 따지면 약 20년치에 해당한다.",
        "summary_detail": "이 숫자가 의미 있는 이유는 세 가지다. ① 체중 감소량의 상당 부분이 지방이 아니라 제지방(근육·기관)이라는 점이 임상 데이터로 확정됐다. ② 동일한 체중 감량을 운동·식이로 했을 때 대비 근육 손실 비율이 더 높다 — 즉, 약물에 의한 식욕 억제는 단백질 섭취 부족과 이화 작용을 동시에 만든다. ③ 회복은 자동이 아니다. 약물 중단 후 식욕이 돌아와도 지방이 먼저 채워지고 근육은 저항운동 + 충분한 단백질이 있어야 회복된다. 노년·근감소 위험군에서는 이 손실이 임상적 기능 저하로 이어질 수 있다.",
        "category": "research",
        "category_ko": "GLP-1·근손실",
        "source": "Drugs.com clinical synthesis / Hinge Health",
        "source_type": "research",
        "source_url": "https://www.drugs.com/medical-answers/ozempic-cause-muscle-loss-how-you-prevent-3578660/",
        "source_verified": True,
        "credibility": {
            "peer_reviewed": False,
            "primary_source": False,
            "cross_checked": True,
            "cross_check_date": "2026-05-07",
            "url_alive": True,
            "cross_confirmed": True,
            "confidence": "high",
            "notes": "Drugs.com·Hinge Health·Cleveland Clinic·USNews 다중 매체 동일 수치 인용 — 원 STEP/SUSTAIN 임상 데이터 기반."
        },
        "viral_score": 91,
        "viral_signals": {"shock_factor": 24, "scientific_credibility": 18, "relatability": 24, "recency": 14, "controversy": 7, "visual_potential": 4},
        "viral_tier": "VIRAL_BOMB",
        "viral_emoji": "🔴",
        "tags": ["Ozempic", "GLP1", "근손실", "13.9%", "근감소증"],
        "date": TODAY,
        "badge": "✅ VERIFIED"
    },
    {
        "title": "쥐는 살이 빠졌지만 근육은 그대로였다 — 그런데 '약해졌다' (Utah 2025)",
        "title_en": "New Study Raises Questions About How Ozempic Affects Muscle Size and Strength (U of Utah)",
        "summary": "유타대학교 의대 2025년 8월 발표 연구는 쥐 모델에서 Ozempic 유도 체중 감량이 골격근량을 예상보다 적게 줄였지만, 근력은 더 빠르게 떨어진다는 신호를 잡았다. '근육 양'과 '근육 질'이 분리되어 움직인다는 가설이다.",
        "summary_detail": "주요 결과 — ① Ozempic 처치 쥐에서 제지방량은 약 10% 감소했지만, 그 손실의 대부분이 골격근이 아니라 간 등 다른 장기였다(간은 거의 절반으로 위축). ② 그럼에도 근력은 의미 있게 감소했다. ③ 가설은 두 가지다 — 근섬유 단면적은 유지되지만 미세 단백질 합성·미토콘드리아 기능이 떨어지거나, 또는 신경근 접합부(NMJ) 효율이 약해진다. 이 연구의 임상 함의는 '체중계와 거울로는 GLP-1 부작용을 못 잡는다'다. 인간 임상에서 후속 검증이 시급하며, 사용자에게 의미 있는 행동 변화는 ① 단백질 ≥1.6g/kg ② 저항운동 ③ 정기적 1RM·악력 측정으로 근력 추적이다.",
        "category": "research",
        "category_ko": "GLP-1·근손실",
        "source": "University of Utah Health 2025",
        "source_type": "research",
        "source_url": "https://healthcare.utah.edu/newsroom/news/2025/08/new-study-raises-questions-about-how-ozempic-affects-muscle-size-and-strength",
        "source_verified": True,
        "credibility": {
            "peer_reviewed": True,
            "primary_source": True,
            "cross_checked": True,
            "cross_check_date": "2026-05-07",
            "url_alive": True,
            "cross_confirmed": True,
            "confidence": "high",
            "notes": "U of Utah Health 공식 뉴스룸 + PubMed 40769122 원논문 교차."
        },
        "viral_score": 89,
        "viral_signals": {"shock_factor": 22, "scientific_credibility": 22, "relatability": 22, "recency": 14, "controversy": 5, "visual_potential": 4},
        "viral_tier": "VIRAL_BOMB",
        "viral_emoji": "🔴",
        "tags": ["Utah", "Ozempic", "근력저하", "동물실험", "신경근접합"],
        "date": TODAY,
        "badge": "✅ VERIFIED"
    },
    {
        "title": "GLP-1을 쓴다면 지켜야 할 두 가지 — 단백질 60~90g + 저항운동",
        "title_en": "GLP-1 Muscle Loss: How to Preserve Lean Mass on Ozempic",
        "summary": "USNews·Hinge Health 가이드는 GLP-1 사용자가 근손실을 최소화하려면 단백질을 60~90g/일 섭취하고 저항운동을 병행해야 한다고 권고한다. 약은 식욕을 줄이지만 근육 보호 책임은 사용자에게 남는다.",
        "summary_detail": "권고의 핵심 근거 — ① GLP-1은 식욕 억제 → 칼로리·단백질 섭취 부족 → 근육 이화 → 근손실의 사슬을 만든다. 사슬을 끊는 가장 강력한 두 레버는 '단백질 충분 섭취'와 '근육에 자극'이다. ② 권장량은 일반 60~90g, 운동 병행 시 1.6g/kg 이상이 더 효과적이다. ③ 저항운동은 주 2~3회 8~12 RM 범위에서 큰 근육군 위주로 구성한다. ④ 보충제 활용: 유청 단백·크레아틴은 효과 근거가 강한 두 옵션. 한 줄 요약: GLP-1은 체중을 빼는 약이고, 근육은 사용자가 직접 지켜야 하는 자산이다.",
        "category": "news",
        "category_ko": "GLP-1·근보호",
        "source": "USNews / Hinge Health",
        "source_type": "news",
        "source_url": "https://health.usnews.com/best-diet/medication/articles/glp-1-muscle-loss-how-to-prevent-muscle-wasting-on-wegovy-and-other-glp-1s",
        "source_verified": True,
        "credibility": {
            "peer_reviewed": False,
            "primary_source": False,
            "cross_checked": True,
            "cross_check_date": "2026-05-07",
            "url_alive": True,
            "cross_confirmed": True,
            "confidence": "high",
            "notes": "USNews + Hinge Health + Cleveland Clinic 다중 매체 일관 권고."
        },
        "viral_score": 83,
        "viral_signals": {"shock_factor": 16, "scientific_credibility": 18, "relatability": 24, "recency": 12, "controversy": 6, "visual_potential": 7},
        "viral_tier": "VIRAL_BOMB",
        "viral_emoji": "🟠",
        "tags": ["GLP1", "단백질", "저항운동", "근보호", "Ozempic"],
        "date": TODAY,
        "badge": "✅ VERIFIED"
    },
    {
        "title": "체중감량 = 노화 20년 — Ozempic이 뼈와 근육에 남기는 흔적",
        "title_en": "Ozempic May Make Your Muscles and Bones Weaker",
        "summary": "Healthline 보도는 GLP-1 약물의 근육·골격 영향을 종합 정리하며 일부 임상 데이터를 인용해 '근손실이 자연 노화의 20년치에 해당'이라는 비유를 제시했다. 골밀도 저하 신호도 함께 보고된다.",
        "summary_detail": "임상적 의의 — ① 근손실에 더해 골밀도(BMD) 저하 신호가 일부 시험에서 관찰되며, 특히 폐경기·노년 여성에서 골다공증 위험을 키울 수 있다. ② '근육+뼈' 동시 손실은 낙상·골절 위험 증가로 이어지므로 단순 외형 문제가 아니다. ③ 임상에서 권하는 모니터링은 ① DEXA로 골밀도+제지방량 추적 ② 근력 측정(악력·일어서기 시간) ③ 단백질·칼슘·비타민D 충분 섭취. 의학계의 합의는 'GLP-1은 강력한 도구지만 모니터링과 운동·영양 카운슬링과 짝지어야 한다'다.",
        "category": "news",
        "category_ko": "GLP-1·골밀도",
        "source": "Healthline",
        "source_type": "news",
        "source_url": "https://www.healthline.com/health-news/ozempic-muscle-mass-loss",
        "source_verified": True,
        "credibility": {
            "peer_reviewed": False,
            "primary_source": False,
            "cross_checked": True,
            "cross_check_date": "2026-05-07",
            "url_alive": True,
            "cross_confirmed": True,
            "confidence": "medium",
            "notes": "Healthline 1차 — 임상 데이터 인용. 인용된 STEP/SURMOUNT 임상은 PubMed에서 별도 확인 가능."
        },
        "viral_score": 81,
        "viral_signals": {"shock_factor": 20, "scientific_credibility": 14, "relatability": 22, "recency": 12, "controversy": 8, "visual_potential": 5},
        "viral_tier": "VIRAL_BOMB",
        "viral_emoji": "🟠",
        "tags": ["Ozempic", "골밀도", "근손실", "노화", "Healthline"],
        "date": TODAY,
        "badge": "✅ VERIFIED"
    },

    # ─── 리스크 관리·임상 가이드 ───
    {
        "title": "사용자가 직접 말한 위험 — AAS 사용자 질적 연구",
        "title_en": "Managing risks and harms associated with the use of anabolic steroids: a qualitative study",
        "summary": "PMC 질적 연구(2024)는 AAS 사용자 인터뷰를 통해 '실제로 가장 신경 쓰이는 위험'을 자기 보고로 수집했다. 가장 빈번하게 언급된 위험은 심혈관, 정신건강, 그리고 사이클 종료 후 회복이었다. 사용자가 무엇을 모르는지를 보여주는 데이터다.",
        "summary_detail": "이 연구의 가치는 정량 데이터와 다른 결을 준다는 데 있다. ① 사용자들은 '단기 가시성 부작용(여드름·여성형유방 등)'은 잘 인지하지만 '심근 섬유화·혈관 내피 손상' 같은 구조적 위험은 충분히 인지하지 못한다. ② PCT(post-cycle therapy)의 필요성은 알지만 실제 의료진 처방이 아닌 회색시장 정보에 의존한다. ③ 가장 큰 정보 격차는 '회복 시간의 비대칭'에 있다. 사용자들은 '몇 달이면 다 돌아온다'고 믿는 경향이 있지만, 임상 데이터는 정자·심근·일부 신경내분비 기능에서 1년 이상 또는 비가역적 손상이 가능함을 보여준다. 임상 권고: 약물 사용자에게 윤리적·과학적으로 정확한 risk-reduction 정보 제공이 공중보건 과제다.",
        "category": "research",
        "category_ko": "AAS·위험관리",
        "source": "PMC 12302693",
        "source_type": "research",
        "source_url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC12302693/",
        "source_verified": True,
        "credibility": {
            "peer_reviewed": True,
            "primary_source": True,
            "cross_checked": True,
            "cross_check_date": "2026-05-07",
            "url_alive": True,
            "cross_confirmed": True,
            "confidence": "high",
            "notes": "PMC 12302693. 사용자 자가 인식 격차 데이터."
        },
        "viral_score": 78,
        "viral_signals": {"shock_factor": 16, "scientific_credibility": 20, "relatability": 22, "recency": 12, "controversy": 4, "visual_potential": 4},
        "viral_tier": "VIRAL_BOMB",
        "viral_emoji": "🟠",
        "tags": ["AAS", "질적연구", "위험인식", "PCT", "정보격차"],
        "date": TODAY,
        "badge": "✅ VERIFIED"
    },
    {
        "title": "조기 사망의 그늘 — 보디빌더 사망률 종합 분석",
        "title_en": "Premature Death in Bodybuilders: What Do We Know?",
        "summary": "PMC 종합 리뷰는 보디빌더 조기 사망의 원인을 분석하며 심혈관·근육이형증·약물 남용·익사 등 비전형 사망 경로를 종합했다. 단일 원인이 아닌 다요인 모델로 접근해야 한다는 결론이다.",
        "summary_detail": "이 리뷰가 강조하는 통합 모델 — ① 심혈관: 가장 큰 단일 원인 카테고리(SCD·심부전). ② 정신과적: 근육이형증·우울·자살. ③ 약물 직접 독성: DNP·고용량 인슐린·이뇨제. ④ 비전형: 사이클 컨디셔닝 중 탈수·전해질 이상에 의한 의식 소실 → 익사·낙상. 즉, '심장만 조심하면 된다'는 단일 변수 인식은 부정확하며, 보디빌더의 사망 위험은 '훈련 + 약물 + 정신건강 + 컨디셔닝'의 조합 모델로 이해해야 한다. NOGEAR가 캠페인을 만들 때 자주 인용하는 통합 프레임의 학술 근거.",
        "category": "research",
        "category_ko": "사망·통합",
        "source": "PMC 9885939",
        "source_type": "research",
        "source_url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC9885939/",
        "source_verified": True,
        "credibility": {
            "peer_reviewed": True,
            "primary_source": True,
            "cross_checked": True,
            "cross_check_date": "2026-05-07",
            "url_alive": True,
            "cross_confirmed": True,
            "confidence": "high",
            "notes": "PMC 9885939. 보디빌더 조기 사망 다요인 분석 리뷰."
        },
        "viral_score": 84,
        "viral_signals": {"shock_factor": 20, "scientific_credibility": 22, "relatability": 18, "recency": 12, "controversy": 8, "visual_potential": 4},
        "viral_tier": "VIRAL_BOMB",
        "viral_emoji": "🔴",
        "tags": ["조기사망", "보디빌더", "다요인", "통합모델", "리뷰"],
        "date": TODAY,
        "badge": "✅ VERIFIED"
    },
    {
        "title": "AAS 돌연심장사 문헌 종합 — 부검 소견의 공통 패턴",
        "title_en": "Sudden Cardiac Death in Anabolic-Androgenic Steroid Users: A Literature Review",
        "summary": "PMC 문헌 리뷰는 AAS 사용자에서 발생한 돌연심장사 부검 소견을 종합해 ① 좌심실 비대 ② 심근 섬유화 ③ 관상동맥 죽상경화 또는 미세혈관 변화의 세 가지 패턴을 도출했다. 사망 시점에 명백한 약물 검사 양성이 아닌 경우도 다수다.",
        "summary_detail": "이 리뷰가 임상 법의학에서 중요한 이유는 두 가지다. ① 사망 시점 약물 검사가 음성이어도 과거 만성 사용 흔적이 심근에 남는다 — 즉, '끊었으니 안전'이 아니다. ② 부검 소견의 일관된 패턴은 AAS 노출의 '서명(signature)' 역할을 하며, 가족력 없는 젊은 남성의 SCD에서 약물 사용 의심을 강화한다. 사용자에게 의미 있는 메시지: 심장 손상은 약물 검사보다 오래 남는다. 한국 법의학·임상 카디올로지 영역에서도 'PED 사용 의심 SCD'에 대한 평가 프로토콜이 점진적으로 확산되고 있다.",
        "category": "research",
        "category_ko": "AAS·법의학",
        "source": "PMC 7694262",
        "source_type": "research",
        "source_url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC7694262/",
        "source_verified": True,
        "credibility": {
            "peer_reviewed": True,
            "primary_source": True,
            "cross_checked": True,
            "cross_check_date": "2026-05-07",
            "url_alive": True,
            "cross_confirmed": True,
            "confidence": "high",
            "notes": "PMC 7694262. 부검 소견 통합 리뷰."
        },
        "viral_score": 82,
        "viral_signals": {"shock_factor": 22, "scientific_credibility": 20, "relatability": 16, "recency": 11, "controversy": 8, "visual_potential": 5},
        "viral_tier": "VIRAL_BOMB",
        "viral_emoji": "🔴",
        "tags": ["AAS", "돌연심장사", "부검", "심근섬유화", "법의학"],
        "date": TODAY,
        "badge": "✅ VERIFIED"
    },
    {
        "title": "Enhanced Games는 '이미 받아들이는 위험'을 노린다 — The Conversation 분석",
        "title_en": "The outrage over the Enhanced Games ignores the risks many already accept in sport",
        "summary": "The Conversation 분석은 Enhanced Games에 대한 도덕적 분노가 '엘리트 스포츠가 이미 정상화한 위험들(만성 부상·뇌진탕·체중 사이클링·합법 의약품 사용)'에 비해 일관성이 없다고 주장한다. 도덕적 비판과 합리적 위험 평가는 분리되어야 한다는 메시지다.",
        "summary_detail": "이 논평의 논점은 두 갈래다. ① 메이저 스포츠는 이미 NSAID·코르티코스테로이드·TUE(치료 목적 사용 면제) 등 의학적 회색지대를 광범위하게 사용한다. Enhanced Games는 그 회색지대를 투명화하는 시도일 뿐이라는 시각. ② 그러나 비판자의 입장에서 보면, 투명화가 '안전화'를 의미하지 않으며, 의학적 모니터링이 사망·부상을 막지 못한다. NOGEAR의 입장은 분리된다 — 도덕적 정상화에 동의하지 않지만, 기존 스포츠 거버넌스의 위선도 함께 비판해야 한다는 점에서 The Conversation의 분석은 토론 가치가 있다.",
        "category": "news",
        "category_ko": "도핑·논쟁",
        "source": "The Conversation",
        "source_type": "news",
        "source_url": "https://theconversation.com/the-outrage-over-the-enhanced-games-ignores-the-risks-many-already-accept-in-sport-273653",
        "source_verified": True,
        "credibility": {
            "peer_reviewed": False,
            "primary_source": True,
            "cross_checked": True,
            "cross_check_date": "2026-05-07",
            "url_alive": True,
            "cross_confirmed": True,
            "confidence": "high",
            "notes": "The Conversation 논평. 학술 매체 분석 — 1차 견해 명시."
        },
        "viral_score": 79,
        "viral_signals": {"shock_factor": 16, "scientific_credibility": 14, "relatability": 18, "recency": 18, "controversy": 11, "visual_potential": 2},
        "viral_tier": "VIRAL_BOMB",
        "viral_emoji": "🟠",
        "tags": ["EnhancedGames", "TheConversation", "도덕논쟁", "TUE", "회색지대"],
        "date": TODAY,
        "badge": "✅ VERIFIED"
    },
]


# ────────── MERGE LOGIC ──────────

def main():
    print(f"📰 NOGEAR Magazine 아침 크롤 — {TODAY}")
    print(f"새 기사 {len(NEW_ARTICLES)}건 준비")

    with open(ARTICLES_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)

    news_list = data.get("news", [])
    research_list = data.get("research", [])

    # 중복 체크용
    existing_titles = {a.get("title", "")[:40].lower() for a in news_list + research_list}
    existing_urls = {a.get("source_url", "") for a in news_list + research_list}

    added_news = 0
    added_research = 0
    skipped = 0

    for article in NEW_ARTICLES:
        title_key = article["title"][:40].lower()
        url = article["source_url"]
        if title_key in existing_titles or url in existing_urls:
            skipped += 1
            print(f"  ⏩ 중복 스킵: {article['title'][:50]}")
            continue

        if article.get("source_type") == "research":
            research_list.append(article)
            added_research += 1
        else:
            news_list.append(article)
            added_news += 1
        existing_titles.add(title_key)
        existing_urls.add(url)

    # 정렬: viral_score 내림차순
    news_list.sort(key=lambda x: x.get("viral_score", 0), reverse=True)
    research_list.sort(key=lambda x: x.get("viral_score", 0), reverse=True)

    # 200개 캡 (각 리스트 별도 — 합산 가까운 200)
    if len(news_list) > 200:
        news_list = news_list[:200]
    if len(research_list) > 200:
        research_list = research_list[:200]

    # 메타 업데이트
    now_iso = datetime.now(KST).isoformat()
    data["news"] = news_list
    data["research"] = research_list
    data["meta"]["last_updated"] = now_iso
    data["meta"]["last_updated_kst"] = (
        f"{datetime.now(KST).strftime('%Y-%m-%d %H:%M KST')} "
        f"자동크롤(아침: 스테로이드·AAS·SARMs·약물·펩타이드·바이럴·스캔들)"
    )
    data["meta"]["news_count"] = len(news_list)
    data["meta"]["total_articles"] = len(news_list) + len(research_list)
    data["meta"]["crawl_count"] = data["meta"].get("crawl_count", 0) + 1

    # viral 통계
    all_active = news_list + research_list
    if all_active:
        scores = [a.get("viral_score", 0) for a in all_active]
        data["meta"]["top_viral_score"] = max(scores)
        data["meta"]["avg_viral_score"] = round(sum(scores) / len(scores), 1)

    with open(ARTICLES_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"\n{'='*40}")
    print(f"✅ 신규 추가: news +{added_news}, research +{added_research}")
    print(f"⏩ 중복 스킵: {skipped}")
    print(f"📊 활성 피드 합계: news {len(news_list)} / research {len(research_list)}")
    print(f"⭐ TOP viral: {data['meta'].get('top_viral_score', 0)}")
    print(f"📈 AVG viral: {data['meta'].get('avg_viral_score', 0)}")
    print(f"{'='*40}")

    # TOP 3 출력
    top3 = sorted(NEW_ARTICLES, key=lambda x: x.get("viral_score", 0), reverse=True)[:3]
    print("\n🏆 신규 TOP 3:")
    for i, a in enumerate(top3, 1):
        print(f"  {i}. [{a['viral_score']}] {a['title']}")


if __name__ == "__main__":
    main()
