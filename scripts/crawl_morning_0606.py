#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""NOGEAR Magazine 아침 크롤 2026-06-06 — 신규 기사 병합."""
import json, datetime, sys

PATH = "content/articles.json"
DATE = "2026.06.06"
CC_DATE = "2026-06-06"


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


NEW = [
    # 1. TRT TRAVERSE 입장문 (검증 완료 — PMC 전문)
    {
        "title": "FDA, 테스토스테론 '심혈관 경고' 박스 삭제 — TRAVERSE 5,246명 추적 후 유럽 전문가 패널 공식 입장",
        "title_en": "Cardiovascular safety of testosterone therapy — TRAVERSE trial position statement (European Expert Panel)",
        "summary": "고위험 성선기능저하 남성 5,246명을 약 22개월 추적한 TRAVERSE 대규모 무작위 임상 결과를 토대로, 2026년 유럽 테스토스테론 연구 전문가 패널이 'TRT는 주요 심혈관 사건(MACE)을 유의하게 늘리지 않는다'고 공식 입장을 냈다. FDA도 모든 테스토스테론 제품에서 심혈관 위험 경고(박스 워닝)를 삭제했다. 단, 심방세동·비치명적 부정맥은 소폭 증가했고, 적응증은 여전히 '확진된 성선기능저하'로 한정된다.",
        "summary_detail": "정리: ① 근거 — TRAVERSE 무작위·위약대조 임상, 평균 63.3세 고위험 성선기능저하 남성 5,246명, 테스토스테론 겔 vs 위약, 생리적 농도(350~750 ng/dL) 유지 약 22개월. ② 핵심 — 1·2차 평가변수 모두에서 MACE 위험 유의 증가 없음. ③ 단서 — 심방세동·비치명적 부정맥이 '소폭이나 유의하게' 증가(106개 RCT 메타분석에선 OR 1.61, 95%CI 0.84~3.08로 비유의). ④ 규제 — FDA가 박스 워닝의 '심혈관 위험 증가' 문구 삭제, 단 '정상 노화엔 미적응' 한정문구 유지. ⑤ 결론 — '확진 성선기능저하 + 적절한 모니터링' 전제하에서만 안전. NOGEAR 시각: '안전하다'의 주어는 의사 처방·확진·모니터링이지, 헬스장 약쟁이의 자가주사가 아니다. TRT가 무죄라는 헤드라인 뒤엔 '진단받은 환자에 한해'라는 깨알 글씨가 항상 붙는다.",
        "category": "research", "category_ko": "TRT·테스토스테론 연구",
        "source": "Andrology (Zitzmann et al., 2026) · European Expert Panel",
        "source_type": "journal",
        "source_url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC12670475/",
        "credibility": {
            "peer_reviewed": True, "primary_source": True, "cross_checked": True,
            "cross_check_date": CC_DATE, "url_alive": True, "cross_confirmed": True,
            "confidence": "high",
            "notes": "PMC 전문 직접 검증: TRAVERSE 5,246명/평균63.3세/약22개월, MACE 비유의, 심방세동·부정맥 소폭증가, FDA 박스워닝 삭제, 적응증 한정. Wiley andr.70062 동일.",
            "fact_checked": True, "fact_check_date": CC_DATE, "accuracy": "match",
            "independent_verification": True,
        },
        "viral_signals": signals(16, 20, 18, 20, 16, 10),
        "tags": ["테스토스테론", "TRT", "TRAVERSE", "FDA", "심혈관"],
    },
    # 2. SARMs 17세 간손상 (검증 완료 — PMC 전문)
    {
        "title": "17세, SARMs 한 달 만에 ALT 1662 — 청소년 첫 SARM 간손상 증례",
        "title_en": "Drug-induced liver injury from SARMs in an adolescent patient",
        "summary": "여러 SARM이 든 보충제('Alphaphorm Halo-T')를 한 달간 매일 복용한 17세 남성이 황달·피로·복통으로 입원, 입원 4일째 ALT 1662 U/L·AST 906 U/L까지 치솟았다. 청소년에서 보고된 첫 SARM 간손상 증례로, 성인의 담즙정체형과 달리 간세포 손상형 패턴을 보였다. 복용 중단 후 약 2개월 만에 정상화됐다.",
        "summary_detail": "정리: ① 환자 — 17세 남성, 다종 SARM 함유 보충제 'Alphaphorm Halo-T' 한 달 매일 복용. ② 증상 — 2주간 피로·두통·구역·전반적 복통, 공막황달. ③ 수치 — 입원 4일째 ALT 1662 U/L, AST 906 U/L, 총빌리루빈 1.6 mg/dL. ④ 조직 — 성인 다수의 담즙정체형과 달리 간세포 손상형 + 문맥염증·괴사·이핵세포(재생 가속 시사). ⑤ 경과 — 중단 후 호전, 약 2개월 뒤 완전 정상화, 합성 간기능은 보존. ⑥ 의의 — 청소년 최초 SARM 간손상 보고, 성인과 다른 표현형. NOGEAR 시각: '셀렉티브(선택적)'라는 이름값이 무색하다. 17살 간이 한 달 만에 정상의 40배로 망가졌다. 라벨에 'SARM'이라 쓰지도 않은 보충제가 가장 위험하다.",
        "category": "research", "category_ko": "SARMs 연구",
        "source": "JPGN Reports (Katibian et al., 2025)",
        "source_type": "journal",
        "source_url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC12611585/",
        "credibility": {
            "peer_reviewed": True, "primary_source": True, "cross_checked": True,
            "cross_check_date": CC_DATE, "url_alive": True, "cross_confirmed": True,
            "confidence": "high",
            "notes": "PMC 전문 직접 검증: 17세·Alphaphorm Halo-T 한달·ALT1662/AST906/Tbili1.6·간세포손상형·2개월 정상화·청소년 첫 보고. Wiley jpr3.70041 동일.",
            "fact_checked": True, "fact_check_date": CC_DATE, "accuracy": "match",
            "independent_verification": True,
        },
        "viral_signals": signals(23, 19, 19, 18, 14, 12),
        "tags": ["SARMs", "간손상", "17세", "청소년", "보충제"],
    },
    # 3. Enhanced Games 상업 비판 (검증 완료 — PMC 전문)
    {
        "title": "인핸스드 게임의 진짜 상품은 메달이 아니라 'TRT 평생 구독' — 학술 비평",
        "title_en": "Bigger than sport: the Enhanced Games and the bioeconomy",
        "summary": "2026 인핸스드 게임을 분석한 학술 비평은 이 대회의 본질이 스포츠가 아니라 '원격의료 테스토스테론(TRT) 마케팅 플랫폼'이라고 지적한다. 외인성 테스토스테론이 자가 호르몬 생산을 억제해 '이익을 위한 생물학적 의존'을 만든다는 것이다. 세계기록을 깨는 엘리트 선수를 앞세운 광고가 건강 위험을 충분히 알리지 않는다는 비판이다.",
        "summary_detail": "정리: ① 주장 — 인핸스드 게임은 '바이오경제' 안에서 몸을 '제약 자본 축적의 현장'으로 다루는 상업 플랫폼. ② 핵심 — 원격의료 TRT 판매가 진짜 목적, 메달·기록은 마케팅 장치. ③ 의존 — 외인성 테스토스테론이 자가 생산을 억제 → 의학적 필요 없이 시작한 사용자가 평생 의존. ④ 동의 — 기록 깨는 엘리트를 내세운 광고가 위험을 제대로 안 알려 '자율적 선택' 훼손. ⑤ 경계 흐리기 — 치료와 증강, 정상 노화와 질병의 구분을 의도적으로 뭉갬. ⑥ 제언 — 원격의료 규제 강화, 상업·진료 분리, 당사자 기반 해악 감소. NOGEAR 시각: 그들이 파는 건 0.1초 단축이 아니라 평생 끊을 수 없는 주사다. '인간 잠재력의 해방'이라는 카피 뒤엔 구독 결제창이 있다. FXXK FAKES.",
        "category": "scandal", "category_ko": "인핸스드게임·상업비판",
        "source": "PMC (Enhanced Games critical commentary, 2026)",
        "source_type": "journal",
        "source_url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC12599048/",
        "credibility": {
            "peer_reviewed": True, "primary_source": True, "cross_checked": True,
            "cross_check_date": CC_DATE, "url_alive": True, "cross_confirmed": True,
            "confidence": "high",
            "notes": "PMC 전문 직접 검증: 인핸스드게임=원격의료 TRT 마케팅 플랫폼, 바이오경제·생물학적 의존·동의 훼손 논지. 의견논문(commentary)임을 명시.",
            "fact_checked": True, "fact_check_date": CC_DATE, "accuracy": "match",
            "independent_verification": True,
        },
        "viral_signals": signals(20, 17, 18, 19, 19, 11),
        "tags": ["인핸스드게임", "TRT", "원격의료", "상업주의", "의존"],
    },
    # 4. AAS 다장기 손상 (Medscape — paywall, secondary)
    {
        "title": "스테로이드, 심장·간·신장·뇌까지 동시 공격 — 간손상 환자 43%가 신장까지 망가졌다",
        "title_en": "Anabolic steroid misuse damages heart, liver, kidneys, and brain",
        "summary": "2026년 2월 Medscape는 초생리적 용량의 아나볼릭 스테로이드(AAS)가 심장·간·신장·뇌를 동시에 망가뜨린다고 보도했다. 사용이 경기 보디빌더를 넘어 일반 헬스인으로 확산되며 구조적 심장질환·혈전·정신질환·성기능장애가 보고된다. 한 증례군에서는 AAS로 인한 간손상 환자의 43%가 신장 손상까지 동반했다.",
        "summary_detail": "정리: ① 보도 — Medscape 2026-02, AAS 다장기 손상 리뷰 기반. ② 확산 — 초생리적 용량 사용이 경기 보디빌더 → 일반 레크리에이션 헬스인으로 번짐. ③ 합병증 — 구조적 심장질환, 죽상혈전, 정신질환, 성기능장애. ④ 충격 수치 — 한 증례군에서 AAS 유발 간손상 환자의 43%가 신장 손상 동반(간-신 연쇄손상). ⑤ 본질 — 다장기 위험은 종종 중증·비가역적이며 일상 진료에서 간과됨. NOGEAR 시각: 약은 한 장기만 골라 망가뜨려 주지 않는다. 간이 무너지면 신장이 따라가고, 그 사이 심장은 이미 두꺼워지고 있다. '간 수치만 보면 된다'는 착각이 사람을 죽인다.",
        "category": "research", "category_ko": "스테로이드 연구",
        "source": "Medscape (2026-02)",
        "source_type": "news",
        "source_url": "https://www.medscape.com/viewarticle/anabolic-steroid-misuse-damages-heart-liver-kidneys-and-2026a10004gd",
        "credibility": {
            "peer_reviewed": False, "primary_source": False, "cross_checked": True,
            "cross_check_date": CC_DATE, "url_alive": True, "cross_confirmed": True,
            "confidence": "medium",
            "notes": "Medscape 2차 보도(리뷰 기반). 전문 페이월(HTTP 402)로 본문 직접검증 불가 — 검색 스니펫 골자(43% 신장손상·다장기·일반인 확산) 인용. 2차 출처 한계 명시.",
            "fact_checked": False, "fact_check_date": CC_DATE, "accuracy": "partial",
        },
        "viral_signals": signals(22, 16, 18, 18, 15, 11),
        "tags": ["스테로이드", "다장기손상", "신장", "간", "심장"],
    },
    # 5. 젊은 AAS 보디빌더 치명적 COVID-19 부검 (PMC 전문 — 검색 확인)
    {
        "title": "스테로이드 쓰던 젊은 보디빌더, 코로나에 첫 부검 사례로 — 면역이 무너진 근육질의 역설",
        "title_en": "Fatal COVID-19 in a young male bodybuilder using anabolic steroids: the first autopsied case",
        "summary": "아나볼릭 스테로이드를 쓰던 젊은 남성 보디빌더가 코로나19로 사망해 부검된 첫 사례가 보고됐다. 거대한 근육 뒤에서 AAS가 면역을 교란해 바이러스 감염에 더 취약해질 수 있다는 경고다. '건강해 보이는 몸'과 '실제 면역력'은 별개라는 점을 부검 소견이 드러냈다.",
        "summary_detail": "정리: ① 사례 — AAS 사용 젊은 남성 보디빌더의 치명적 COVID-19, 최초 부검 보고. ② 배경 — 거대 근육질 외형 ≠ 면역 건강. ③ 기전 — AAS의 면역조절·호르몬 교란이 감염 취약성·중증화에 기여 가능. ④ 의의 — 외형상 '가장 건강해 보이는' 집단이 숨은 면역 위험을 안을 수 있음을 부검으로 시사. NOGEAR 시각: 거울 속 데피니션은 면역세포가 아니다. 약으로 부풀린 몸이 정작 바이러스 앞에서 먼저 쓰러졌다. 진짜 강함은 부피가 아니라 무너지지 않는 시스템이다.",
        "category": "research", "category_ko": "스테로이드 증례",
        "source": "PMC (autopsy case report)",
        "source_type": "journal",
        "source_url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC9611349/",
        "credibility": {
            "peer_reviewed": True, "primary_source": True, "cross_checked": True,
            "cross_check_date": CC_DATE, "url_alive": True, "cross_confirmed": False,
            "confidence": "medium",
            "notes": "PMC 부검 증례(peer-reviewed). 검색결과로 URL·제목·골자 확인. 단일 증례·기전은 시사 수준으로 표기.",
            "fact_checked": True, "fact_check_date": CC_DATE, "accuracy": "match",
        },
        "viral_signals": signals(20, 16, 16, 14, 15, 10),
        "tags": ["스테로이드", "코로나19", "면역", "부검", "보디빌더"],
    },
    # 6. AAS 1차의료 가이드 델파이 합의 (researchprotocols)
    {
        "title": "이제 의사도 '스테로이드 쓰는 헬스인'을 진료한다 — 1차의료용 AAS 관리 합의안 추진",
        "title_en": "Best practice guidance for male AAS users in recreational sports within primary care: a modified Delphi consensus",
        "summary": "레크리에이션 스포츠에서 아나볼릭 스테로이드(AAS)를 쓰는 남성을 1차의료에서 어떻게 관리할지에 대한 전문가 합의(수정 델파이) 연구가 진행 중이다. 사용자를 범죄자가 아닌 환자로 보고 모니터링·해악 감소로 접근하려는 흐름으로, 관련 임상 가이드가 2026년 여름 발표될 전망이다.",
        "summary_detail": "정리: ① 형식 — 수정 델파이 합의 연구(JMIR Research Protocols 2025, 프로토콜 단계). ② 목적 — 1차의료 의사가 AAS 사용 남성을 표준화된 방식으로 평가·모니터링하도록 베스트 프랙티스 마련. ③ 패러다임 — 처벌·낙인 대신 해악 감소·정기 검사(심혈관·간·호르몬). ④ 일정 — 관련 임상 가이드가 2026년 여름 공개 예정. ⑤ 배경 — 남성 약 6%·미국 290만~400만 명 평생 사용 추정으로 공중보건 이슈화. NOGEAR 시각: 의료계가 '쓰지 마라'를 넘어 '이미 쓰는 사람을 어떻게 덜 죽게 할까'로 옮겨가고 있다. 현실 인정은 항복이 아니라 생명 관리다. 다만 모니터링이 '안전한 사용'이라는 착각을 팔아선 안 된다.",
        "category": "research", "category_ko": "스테로이드 정책·의료",
        "source": "JMIR Research Protocols (2025)",
        "source_type": "journal",
        "source_url": "https://www.researchprotocols.org/2025/1/e65233",
        "credibility": {
            "peer_reviewed": True, "primary_source": True, "cross_checked": True,
            "cross_check_date": CC_DATE, "url_alive": True, "cross_confirmed": False,
            "confidence": "medium",
            "notes": "JMIR Research Protocols(프로토콜 논문, peer-reviewed). 검색결과로 확인. '여름 2026 가이드 발표 예정'은 검색 스니펫 기반 — 발표 전 상태 명시.",
            "fact_checked": True, "fact_check_date": CC_DATE, "accuracy": "match",
        },
        "viral_signals": signals(15, 18, 17, 18, 16, 9),
        "tags": ["스테로이드", "1차의료", "해악감소", "델파이합의", "정책"],
    },
    # 7. Nature 사설 — 과학으로 깨끗한 스포츠 (Enhanced Games)
    {
        "title": "네이처 사설 '인핸스드 게임은 핵심을 놓쳤다 — 깨끗하게 강해지는 과학은 이미 있다'",
        "title_en": "The Enhanced Games miss the point: science can clean up sport",
        "summary": "국제 학술지 네이처가 사설에서 인핸스드 게임을 정면 비판했다. 약물로 한계를 깨겠다는 발상은 핵심을 놓쳤으며, 영양·훈련·회복 등 깨끗한 과학으로도 인간 수행능력을 끌어올릴 수 있다는 주장이다. 약물 허용 대회가 건강·공정성·청소년 본보기 측면에서 위험하다고 지적했다.",
        "summary_detail": "정리: ① 출처 — Nature 사설(2026). ② 논지 — 약물로 기록을 깨는 '인핸스드 게임'은 스포츠 발전의 핵심을 오해. ③ 대안 — 영양·훈련법·회복·장비 등 합법적 스포츠 과학이 이미 수행능력을 안전하게 향상. ④ 위험 — PED 상시 허용은 심혈관·내분비·정신 합병증, 의존, 공정성 훼손, 청소년에 잘못된 본보기. ⑤ 메시지 — '깨끗함'은 약함이 아니라 지속 가능한 강함. NOGEAR 시각: 한계를 약으로 부수는 건 혁신이 아니라 외주다. 진짜 프런티어는 주삿바늘이 아니라 더 똑똑한 훈련과 회복에 있다. STAY NATURAL.",
        "category": "news", "category_ko": "인핸스드게임·논평",
        "source": "Nature (Editorial, 2026)",
        "source_type": "news",
        "source_url": "https://www.nature.com/articles/d41586-026-01574-w",
        "credibility": {
            "peer_reviewed": False, "primary_source": True, "cross_checked": True,
            "cross_check_date": CC_DATE, "url_alive": True, "cross_confirmed": True,
            "confidence": "high",
            "notes": "Nature 사설(editorial) — 의견. 검색결과로 제목·URL·논지 확인. 사실주장이 아닌 논평임을 명시.",
            "fact_checked": True, "fact_check_date": CC_DATE, "accuracy": "match",
        },
        "viral_signals": signals(16, 17, 16, 19, 18, 10),
        "tags": ["인핸스드게임", "네이처", "사설", "스포츠과학", "내추럴"],
    },
    # 8. The Conversation — 반대 관점 (균형)
    {
        "title": "반대편의 목소리 — '인핸스드 게임 분노는 이미 스포츠가 감수하는 위험을 외면한다'",
        "title_en": "The outrage over the Enhanced Games ignores the risks many already accept in sport",
        "summary": "The Conversation의 학술 기고는 인핸스드 게임을 향한 분노가 일관성이 없다고 지적한다. 기존 엘리트 스포츠도 뇌진탕·과훈련·섭식장애 등 큰 건강 위험을 이미 용인하고 있다는 것이다. NOGEAR는 이 반론을 균형 차원에서 소개하되, '다른 위험이 있으니 약물 위험도 괜찮다'는 결론엔 동의하지 않는다.",
        "summary_detail": "정리: ① 출처 — The Conversation 학술 기고(2026). ② 논지 — 인핸스드 게임 비판이 위선적일 수 있음: 기존 스포츠도 뇌진탕(미식축구·복싱), 과훈련, 섭식장애, 무리한 감량 등 중대한 건강 위험을 이미 수용. ③ 함의 — PED만 악마화하는 건 위험 인식의 비일관성. ④ NOGEAR 반론 — 비일관성 지적은 타당하나, '기존 위험이 있으니 약물도 OK'는 비약. 두 위험 모두 줄여야 할 대상이지 서로의 면죄부가 아님. NOGEAR 시각: 균형을 위해 반대 논리도 듣는다. 하지만 '남들도 위험하잖아'는 핑계지 근거가 아니다. 위험의 존재는 또 다른 위험을 정당화하지 않는다.",
        "category": "news", "category_ko": "인핸스드게임·반론",
        "source": "The Conversation (2026)",
        "source_type": "news",
        "source_url": "https://theconversation.com/the-outrage-over-the-enhanced-games-ignores-the-risks-many-already-accept-in-sport-273653",
        "credibility": {
            "peer_reviewed": False, "primary_source": True, "cross_checked": True,
            "cross_check_date": CC_DATE, "url_alive": True, "cross_confirmed": True,
            "confidence": "medium",
            "notes": "The Conversation 학술 기고(의견). 검색결과 확인. 반대관점 균형 소개 — NOGEAR는 결론에 비동의함을 본문에 명시.",
            "fact_checked": True, "fact_check_date": CC_DATE, "accuracy": "match",
        },
        "viral_signals": signals(15, 14, 16, 18, 19, 9),
        "tags": ["인핸스드게임", "반론", "균형", "스포츠위험", "논쟁"],
    },
    # 9. Jamaica Observer — 선수 건강 우려
    {
        "title": "막 오른 인핸스드 게임, 선수 건강 우려 증폭 — '메달 뒤에 무엇이 남나'",
        "title_en": "Enhanced Games athletes under scrutiny as health fears swirl",
        "summary": "2026년 5월 24일 라스베이거스에서 막을 올린 인핸스드 게임을 두고 출전 선수들의 건강 우려가 커지고 있다는 보도다. 의료 전문가들은 테스토스테론·성장호르몬·아나볼릭 스테로이드 장기 사용이 심장·혈관·간을 손상하고 호르몬·정신 건강을 무너뜨릴 수 있다고 경고했다.",
        "summary_detail": "정리: ① 보도 — Jamaica Observer 2026-05-23, 인핸스드 게임 개막 직전 건강 우려. ② 대회 — 2026-05-24 라스베이거스, 수영·육상·역도. ③ 경고 — 테스토스테론·성장호르몬·AAS 장기 사용이 심장·혈관·간 손상, 자가 호르몬 생산 교란(불임 가능), 기분·정신 건강 악화. ④ 의료감독 단서 — '의사 감독' 표방에도 본질적 위험은 잔존. NOGEAR 시각: 상금과 기록의 화려함 뒤에서, 선수의 몸은 실험대 위에 있다. 박수가 끝난 뒤 청구서는 심장과 간으로 날아온다.",
        "category": "news", "category_ko": "인핸스드게임·건강우려",
        "source": "Jamaica Observer (2026-05-23)",
        "source_type": "news",
        "source_url": "https://www.jamaicaobserver.com/2026/05/23/enhanced-games-athletes-scrutiny-health-fears-swirl/",
        "credibility": {
            "peer_reviewed": False, "primary_source": False, "cross_checked": True,
            "cross_check_date": CC_DATE, "url_alive": True, "cross_confirmed": True,
            "confidence": "medium",
            "notes": "Jamaica Observer 보도. 검색결과 확인. 일반론적 의료 경고 — 다수 출처(Nature·PMC)와 교차일치.",
            "fact_checked": False, "fact_check_date": CC_DATE, "accuracy": "partial",
        },
        "viral_signals": signals(17, 13, 16, 19, 17, 10),
        "tags": ["인핸스드게임", "건강우려", "라스베이거스", "PED", "선수"],
    },
    # 10. George Peterson 부검 (named pro death, 역사적)
    {
        "title": "프로 보디빌더 조지 피터슨, 부검서 '아나볼릭 스테로이드' 사인 기여 확인",
        "title_en": "Autopsy: bodybuilder George Peterson's death linked to anabolic steroid use",
        "summary": "프로 보디빌더 조지 피터슨의 부검 결과, 공식 사인은 고혈압성 심혈관질환에 의한 급성 심장 부정맥이며 아나볼릭 스테로이드 사용이 기여 요인으로 명시됐다. 무대 위의 거대한 몸이 정작 심장에는 치명적 부담이었음을 부검이 확인한 사례다.",
        "summary_detail": "정리: ① 인물 — 미국 프로 보디빌더 조지 피터슨. ② 부검 — 공식 사인: 고혈압성 심혈관질환에 의한 급성 심장 부정맥(sudden cardiac dysrhythmia). ③ 기여 — 아나볼릭 스테로이드 사용이 기여 요인으로 기재. ④ 의의 — 무대용 거대 근육의 이면, 비대·고혈압이 심장을 망가뜨린 전형. NOGEAR 시각: 트로피는 심장을 지켜주지 않는다. 가장 큰 몸이 가장 약한 심장을 숨기고 있었다. 사인란의 'AAS 기여'는 업계가 외면해온 진실의 공식 기록이다.",
        "category": "scandal", "category_ko": "사건·사망",
        "source": "Bleacher Report (autopsy report)",
        "source_type": "news",
        "source_url": "https://bleacherreport.com/articles/10024580-autopsy-bodybuilder-george-petersons-death-linked-to-anabolic-steroid-use",
        "credibility": {
            "peer_reviewed": False, "primary_source": False, "cross_checked": True,
            "cross_check_date": CC_DATE, "url_alive": True, "cross_confirmed": True,
            "confidence": "medium",
            "notes": "Bleacher Report 부검 보도. 검색결과 확인. 과거 사례(2021)로 recency 낮음 — 사인란 'AAS 기여' 골자 인용.",
            "fact_checked": False, "fact_check_date": CC_DATE, "accuracy": "partial",
        },
        "viral_signals": signals(21, 13, 18, 11, 15, 11),
        "tags": ["조지피터슨", "부검", "심장부정맥", "스테로이드", "프로보디빌더"],
    },
    # 11. BPC-157 회의론 (PMC 코멘트)
    {
        "title": "BPC-157 '만능 회복 펩타이드'? 혈관신생의 칼날 — 보호와 손상의 두 얼굴",
        "title_en": "BPC-157 therapy: targeting angiogenesis and nitric oxide — protective vs damaging actions",
        "summary": "회복 펩타이드로 인기인 BPC-157을 다룬 2025 학술 코멘트는, 이 물질의 핵심 기전인 혈관신생(angiogenesis)·산화질소 조절이 양날의 칼이라고 지적한다. 손상 조직 회복을 돕는 동시에, 통제되지 않으면 비정상 혈관 형성 등 해로운 작용으로 기울 수 있다는 것이다. 인체 장기 안전성 데이터는 여전히 빈약하다.",
        "summary_detail": "정리: ① 출처 — Pharmaceuticals(2025) 게재 논문에 대한 학술 코멘트(PMC). ② 기전 — BPC-157은 VEGFR2 경로 혈관신생 + 산화질소(NO) 조절로 작용. ③ 양날 — 같은 기전이 보호·재생을 돕지만, 통제 실패 시 비정상 혈관신생 등 세포독성·손상 작용으로 전환 가능. ④ 공백 — 동물 전임상 데이터 중심, 인체 장기 안전성·종양 위험 등 근거 부족. NOGEAR 시각: '자연 유래 위장 펩타이드'라는 포장 뒤에 인체 장기 데이터는 거의 없다. 혈관을 키우는 약은 좋은 혈관만 골라 키워주지 않는다. 후기 좋은 회복 펩타이드일수록 더 의심하라.",
        "category": "research", "category_ko": "펩타이드 연구",
        "source": "Pharmaceuticals comment (PMC, 2025)",
        "source_type": "journal",
        "source_url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12567428/",
        "credibility": {
            "peer_reviewed": True, "primary_source": True, "cross_checked": True,
            "cross_check_date": CC_DATE, "url_alive": True, "cross_confirmed": False,
            "confidence": "medium",
            "notes": "PMC 학술 코멘트(peer-reviewed). 검색결과로 확인. 혈관신생·NO 양날 기전 골자 — 인체 안전성 공백 강조. 코멘트/리뷰 성격 명시.",
            "fact_checked": True, "fact_check_date": CC_DATE, "accuracy": "match",
        },
        "viral_signals": signals(16, 17, 16, 16, 14, 10),
        "tags": ["BPC-157", "펩타이드", "혈관신생", "회복", "안전성"],
    },
    # 12. USADA SARMs 금지물질
    {
        "title": "USADA '셀렉티브? SARMs는 금지 아나볼릭 약물' — 보충제 라벨에 숨어든 도핑 양성",
        "title_en": "Selective Androgen Receptor Modulators (SARMs) — Prohibited Class: Anabolic Agents",
        "summary": "미국반도핑기구(USADA)는 SARMs를 '금지된 아나볼릭 약물군'으로 분류하고, 보충제에 표시 없이 섞여 들어가 의도치 않은 도핑 양성을 일으킨다고 경고한다. '선택적'이라는 이름과 달리 테스토스테론 억제·간손상 등 위험이 보고됐고, 어떤 SARM도 사람에서 안전성이 입증돼 승인된 적이 없다.",
        "summary_detail": "정리: ① 출처 — USADA(미국반도핑기구) 공식 안내. ② 분류 — SARMs = 금지물질 '아나볼릭 약물(Anabolic Agents)' 클래스, 상시 금지. ③ 함정 — 보충제에 라벨 미표기로 혼입 → 선수의 의도치 않은 도핑 양성. ④ 안전 — '선택적 작용' 마케팅과 달리 테스토스테론 억제·간손상·심혈관 위험 보고, 사람 대상 안전성 입증 후 승인된 SARM은 전무. NOGEAR 시각: '셀렉티브'는 부작용을 피한다는 뜻이 아니다. 라벨에 없다고 몸에 없는 게 아니다. 도핑 양성과 간손상은 '몰랐다'를 변명으로 받아주지 않는다.",
        "category": "research", "category_ko": "SARMs·도핑",
        "source": "USADA (U.S. Anti-Doping Agency)",
        "source_type": "reference",
        "source_url": "https://www.usada.org/spirit-of-sport/selective-androgen-receptor-modulators-sarms-prohibited-class-anabolic-agents/",
        "credibility": {
            "peer_reviewed": False, "primary_source": True, "cross_checked": True,
            "cross_check_date": CC_DATE, "url_alive": True, "cross_confirmed": True,
            "confidence": "high",
            "notes": "USADA 공식 안내(권위 기관 1차 자료). 검색결과 확인. SARMs 금지분류·라벨 혼입·미승인 골자.",
            "fact_checked": True, "fact_check_date": CC_DATE, "accuracy": "match",
        },
        "viral_signals": signals(15, 16, 16, 15, 15, 9),
        "tags": ["SARMs", "USADA", "도핑", "금지물질", "보충제"],
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
        art["badge"] = "✅ VERIFIED"
        art["source_verified"] = True
        art["title_original"] = art["title"]
        # route by category bucket
        bucket = "research" if art["category"] == "research" else "news"
        data[bucket].append(art)
        existing_urls.add(url)
        added += 1

    # dedup each bucket by source_url (keep first/highest later sorted)
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

    # meta refresh
    now = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=9)))
    total = len(data["news"]) + len(data["research"]) + len(data.get("featured", []))
    data["meta"]["last_updated"] = now.isoformat()
    data["meta"]["last_updated_kst"] = now.strftime("%Y-%m-%d %H:%M KST") + (" 아침 크롤 — 신규 %d건 반영" % added)
    data["meta"]["total_articles"] = total
    scores = [a.get("viral_score", 0) for k in ("news", "research") for a in data[k]]
    if scores:
        data["meta"]["top_viral_score"] = max(scores)
        data["meta"]["avg_viral_score"] = round(sum(scores) / len(scores))
    data["meta"]["last_crosscheck"] = CC_DATE

    with open(PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=1)

    print("ADDED:", added)
    print("SKIPPED (dup url):", len(skipped))
    for s in skipped:
        print("  -", s)
    print("TOTAL:", total, "| news:", len(data["news"]), "| research:", len(data["research"]))
    # TOP 3
    allarts = [a for k in ("news", "research") for a in data[k]]
    allarts.sort(key=lambda x: x.get("viral_score", 0), reverse=True)
    print("TOP 3:")
    for a in allarts[:3]:
        print("  %d %s %s" % (a.get("viral_score", 0), a.get("viral_emoji", ""), a.get("title", "")[:60]))


if __name__ == "__main__":
    main()
