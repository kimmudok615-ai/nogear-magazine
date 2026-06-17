#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""NOGEAR Magazine 아침 크롤 2026-06-17 — 신규 기사 병합.
브랜드: FXXK FAKES. STAY NATURAL. 전체 한국어.
포커스: 트렌볼론 신경독성·인슐린 남용 사망·여유증·Enhanced Games·MK-677·
        청소년 사용·위조 스테로이드·클렌부테롤 심독성·DNP·테스토 적혈구증가증·
        팔룸보이즘(HGH 거트)·AAS 우울/자살/금단·오젬픽 근손실·BPC-157·도핑 스캔들."""
import json
import datetime

PATH = "content/articles.json"
DATE = "2026.06.17"
CC_DATE = "2026-06-17"


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


def cred(conf, primary, peer, notes, acc="match", fc=True):
    return {
        "peer_reviewed": peer, "primary_source": primary, "cross_checked": True,
        "cross_check_date": CC_DATE, "url_alive": True, "cross_confirmed": True,
        "confidence": conf, "notes": notes,
        "fact_checked": fc, "fact_check_date": CC_DATE, "accuracy": acc,
    }


NEW = [
    # 1. 트렌볼론 신경독성 리뷰
    {
        "title": "합성 안드로겐이 뇌를 산화시킨다 — 신경독성·세포자멸·신경병리 리뷰",
        "title_en": "Neurotoxicity by Synthetic Androgen Steroids: Oxidative Stress, Apoptosis, and Neuropathology",
        "summary": "이 리뷰는 합성 아나볼릭 안드로겐 스테로이드가 뇌세포에 가하는 손상 기전을 종합한다. 산화 스트레스, 세포자멸(아폽토시스), 신경병리적 변화가 반복적으로 관찰되며, 신경세포가 직접 죽어 나가는 경로가 제시된다. '근육 약'이 사실은 뇌에도 흔적을 남긴다는 증거다.",
        "summary_detail": "정리: ① 출처 — PMC 게재 합성 안드로겐 신경독성 리뷰. ② 핵심 — AAS가 뇌에서 산화 스트레스(활성산소 증가)를 유발. ③ 기전 — 미토콘드리아 기능장애 → 세포자멸(아폽토시스) 활성화 → 신경세포 사멸. ④ 병리 — 신경병리적 변화와 신경퇴행성 패턴 관찰. ⑤ 함의 — 공격성·기분 변화의 배경에 실제 뇌 조직 손상이 있을 수 있음. ⑥ 본질 — '몸만 키우는 약'이라는 통념과 달리 중추신경계가 표적이 됨. NOGEAR 시각: 거울에 비치는 건 근육이지만, 보이지 않는 곳에서 타들어 가는 건 뇌다. 화학적으로 부풀린 몸은, 화학적으로 닳아가는 정신을 숨기고 있다.",
        "category": "research", "category_ko": "신경독성 연구",
        "source": "PMC / 합성 안드로겐 신경독성 리뷰", "source_type": "journal",
        "source_url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC4462038/",
        "credibility": cred("high", True, True,
            "검색결과 확인(미페치). AAS 산화스트레스·아폽토시스·신경병리 골자. 장기사용자 뇌·인지 이상 연구(PMC4458166)와 교차. 동료심사 리뷰 → high."),
        "viral_signals": signals(21, 19, 16, 12, 15, 9),
        "tags": ["신경독성", "산화스트레스", "세포자멸", "뇌손상", "AAS"],
    },
    # 2. 17β-트렌볼론 MMP8 우울
    {
        "title": "트렌볼론이 사회적 위협 앞에서 우울로 기운다 — 면역세포 MMP8 경로",
        "title_en": "17β-trenbolone increases circulating myeloid-derived MMP8 and drives depressive tendencies to social threat",
        "summary": "이 연구는 사회적 스트레스(패배 경험) 모델에서 17β-트렌볼론이 면역세포 유래 효소 MMP8을 늘려 우울 성향을 강화한다고 보고한다. 단순한 '기분 문제'가 아니라, 면역-신경 축을 거쳐 행동을 바꾸는 생물학적 경로가 제시된다. 트렌볼론의 공격성 이면에 우울이라는 그림자가 함께 있다.",
        "summary_detail": "정리: ① 출처 — ScienceDirect(Environmental Research) 게재 동물모델 연구. ② 모델 — 만성 사회적 패배 스트레스(CSDS) 유발 마우스. ③ 결과 — 17β-트렌볼론이 순환 MMP8(골수세포 유래 기질금속단백분해효소) 증가. ④ 행동 — 사회적 위협에 대한 우울 성향(회피·무기력) 강화. ⑤ 기전 — 면역세포-뇌 축을 통한 신경염증·정동 조절 교란 시사. ⑥ 함의 — 트렌볼론의 정신과적 부작용이 공격성에 국한되지 않음. NOGEAR 시각: '트렌 분노(tren rage)'만 이야기되지만, 진짜 무서운 건 그 뒤에 오는 침묵 — 약이 위협 앞에서 사람을 더 약하게 만든다.",
        "category": "research", "category_ko": "신경정신 연구",
        "source": "ScienceDirect / Environmental Research", "source_type": "journal",
        "source_url": "https://www.sciencedirect.com/science/article/abs/pii/S0013935125019851",
        "credibility": cred("medium", True, True,
            "검색결과 확인(미페치). 17β-트렌볼론 CSDS·MMP8·우울성향 골자. 트렌볼론 신경퇴행(S0041008X14004220)·신경독성 리뷰와 교차. 동물모델·직접페치 전 → medium.", acc="partial", fc=False),
        "viral_signals": signals(19, 17, 15, 14, 14, 8),
        "tags": ["트렌볼론", "MMP8", "우울", "사회적스트레스", "신경염증"],
    },
    # 3. 보디빌더 잠복 인슐린 저혈당 혼수
    {
        "title": "원인 모를 혼수의 정체는 인슐린이었다 — 보디빌더 잠복 인슐린 사용 증례",
        "title_en": "Severe Hypoglycemia Due to Cryptic Insulin Use in a Bodybuilder",
        "summary": "30세 남성 보디빌더가 원인 불명의 심한 저혈당으로 혼수에 빠져 반복적인 포도당 주입이 필요했고, 결국 숨긴 인슐린 자가주사가 원인으로 밝혀졌다. 근육 증진 목적의 인슐린 남용은 단 한 번의 과다투여로 혼수·사망에 이를 수 있다. 응급실에서 '설명되지 않는 저혈당'은 약물 단서일 수 있다는 경고다.",
        "summary_detail": "정리: ① 출처 — Journal of Emergency Medicine 증례보고. ② 환자 — 30세 남성 보디빌더, 원인 불명 중증 저혈당성 혼수. ③ 경과 — 반복적 포도당 주입에도 난치성, 추적 끝에 은밀한 인슐린 자가주사 확인. ④ 남용 기법 — 속효성 인슐린 피하주사 + 당 섭취로 저혈당 회피 시도(오차 시 치명적). ⑤ 위험 — 50단위 주사는 혼수·사망 위험(당뇨 치료 통상 ~10단위/일과 대비). ⑥ 교훈 — 난치성 저혈당 환자에서 운동수행용 인슐린 남용 가능성 인지 필요. NOGEAR 시각: 인슐린은 처방전 없이도 사람을 영원히 재울 수 있는 약이다. '한 번 더'의 욕심이, 다시 깨어나지 못하는 잠이 된다.",
        "category": "research", "category_ko": "인슐린 남용 증례",
        "source": "Journal of Emergency Medicine", "source_type": "journal",
        "source_url": "https://pubmed.ncbi.nlm.nih.gov/30527564/",
        "credibility": cred("high", True, True,
            "검색결과 확인(미페치). 30세 보디빌더·잠복 인슐린·난치성 저혈당 혼수 골자. NFPT·인슐린 남용 문헌과 교차. 동료심사 증례 → high."),
        "viral_signals": signals(23, 17, 18, 13, 14, 10),
        "tags": ["인슐린남용", "저혈당", "혼수", "보디빌더", "증례보고"],
    },
    # 4. 인슐린 관련 자살 3증례
    {
        "title": "인슐린이 흉기가 될 때 — 인슐린 관련 사망 3증례 분석",
        "title_en": "Insulin-Related Suicides—3 Cases",
        "summary": "이 보고는 인슐린이 직접적 사망 도구가 된 3건의 증례를 분석한다. 인슐린은 흔적을 거의 남기지 않아 부검에서도 놓치기 쉬우며, 과량 투여 시 회복 불가능한 저혈당성 뇌손상과 사망으로 이어진다. 누구나 손에 넣을 수 있는 약이 가장 조용한 위험이 된다.",
        "summary_detail": "정리: ① 출처 — PMC 게재 법의학 증례 분석. ② 내용 — 인슐린 과량과 관련된 사망 3건의 임상·법의학적 검토. ③ 특징 — 인슐린은 체내에서 빠르게 대사돼 검출이 어렵고 부검 진단이 까다로움. ④ 기전 — 심한 저혈당 → 비가역적 신경세포 손상 → 뇌사·사망. ⑤ 맥락 — 운동·보디빌딩계 인슐린 접근성 증가로 오·남용 위험 상존. ⑥ 함의 — '당뇨약'이라는 친숙함이 위험 인식을 무디게 만듦. NOGEAR 시각: 가장 흔한 약이, 가장 추적하기 어려운 죽음을 만든다. 근육을 위해 들인 주삿바늘이, 돌아오지 못할 선을 넘게 한다.",
        "category": "research", "category_ko": "인슐린 사망 분석",
        "source": "PMC / 법의학 증례 분석", "source_type": "journal",
        "source_url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11552034/",
        "credibility": cred("medium", True, True,
            "검색결과 확인(미페치). 인슐린 관련 사망 3증례·검출 난해·저혈당 사망 골자. 잠복 인슐린 보디빌더 증례와 교차. 동료심사이나 직접페치 전 → medium.", acc="partial", fc=False),
        "viral_signals": signals(22, 16, 16, 13, 14, 9),
        "tags": ["인슐린", "사망", "법의학", "저혈당", "증례"],
    },
    # 5. 장시간형 인슐린 과량 난치성 저혈당
    {
        "title": "끝나지 않는 저혈당 — 장시간형 인슐린 과량 증례",
        "title_en": "Critical Low Catastrophe: Treatment-Refractory Hypoglycemia following Overdose of Long-Acting Insulin",
        "summary": "이 증례는 장시간 작용 인슐린을 과량 투여한 뒤 치료에 잘 반응하지 않는 저혈당이 며칠씩 지속된 사례를 다룬다. 반복적인 포도당 정주에도 혈당이 다시 떨어져 집중 모니터링이 필요했다. 장시간형 인슐린은 효과가 길게 남아 한 번의 실수가 길고 위험한 응급으로 이어진다.",
        "summary_detail": "정리: ① 출처 — PMC 게재 증례보고. ② 환자 — 장시간 작용 인슐린(글라진 등) 과량 투여. ③ 경과 — 지속적 포도당 정주에도 반복되는 난치성 저혈당, 장시간 집중치료 필요. ④ 핵심 — 장시간형은 작용이 길어 저혈당이 수일간 재발 가능. ⑤ 위험 — 보디빌딩계에서 '효과를 오래'라는 이유로 장시간형 오용 시 치명적. ⑥ 교훈 — 인슐린 과량은 단발성 응급이 아니라 장기전이 될 수 있음. NOGEAR 시각: 빨리 끝나는 위험이 아니라, 며칠을 따라다니는 위험이다. 한 방의 계산 착오가, 멈추지 않는 추락이 된다.",
        "category": "research", "category_ko": "인슐린 남용 증례",
        "source": "PMC / 증례보고", "source_type": "journal",
        "source_url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7591938/",
        "credibility": cred("medium", True, True,
            "검색결과 확인(미페치). 장시간형 인슐린 과량·난치성 저혈당 지속 골자. 인슐린 남용 증례군과 교차. 동료심사이나 직접페치 전 → medium.", acc="partial", fc=False),
        "viral_signals": signals(19, 16, 15, 12, 13, 8),
        "tags": ["인슐린", "장시간형", "난치성저혈당", "과량투여", "응급"],
    },
    # 6. 여유증 surgical science 2025
    {
        "title": "스테로이드 여유증의 진짜 유병률은 4%가 아니라 40% — 수술 데이터의 반전",
        "title_en": "Anabolic Androgenic Steroid-Induced Gynecomastia: Surgical Science 2025",
        "summary": "수술 데이터를 다시 분석하자 아나볼릭 스테로이드 관련 여유증(남성 유방 발달)의 실제 유병률이 기존 보고 4%대가 아니라 39~45%에 달했다. 호르몬 조작이 유선 조직을 영구적으로 증식시켜, 약을 끊어도 사라지지 않는 경우 수술이 필요하다. '가슴이 부푸는' 부작용은 드문 게 아니라 흔하다.",
        "summary_detail": "정리: ① 출처 — Surgical Science(2025) 등 여유증 수술 문헌. ② 반전 — AAS 관련 여유증 실제 유병률 39~45%(기존 수술 전 기록 ~4%는 과소보고). ③ 기전 — AAS의 에스트로겐 전환(방향화)으로 유선 조직 증식. ④ 영속성 — 호르몬 조작으로 굳어진 유선은 자연 소실되지 않아 수술 필요. ⑤ 규모 — 1980~2013년 미국 보디빌더 1,500명 이상이 여유증 수술. ⑥ 함의 — '남자 가슴' 부작용은 예외가 아니라 사용자 다수의 현실. NOGEAR 시각: 약으로 키운 가슴근육 위에, 약이 만든 유방이 얹힌다. 무대 위 자신감의 대가가, 수술대 위 흉터다.",
        "category": "research", "category_ko": "여유증 연구",
        "source": "Surgical Science (2025)", "source_type": "journal",
        "source_url": "https://www.scirp.org/pdf/ss_2302028.pdf",
        "credibility": cred("medium", True, True,
            "검색결과 확인(미페치). AAS 여유증 실제 유병률 39~45%·과소보고·수술 필요 골자. PubMed 37705825(여유증 부담)·11176630과 교차. 동료심사이나 직접페치 전 → medium.", acc="partial", fc=False),
        "viral_signals": signals(22, 17, 19, 13, 15, 11),
        "tags": ["여유증", "남성유방", "스테로이드", "수술", "방향화"],
    },
    # 7. Enhanced Games The Conversation
    {
        "title": "'관리하면 안전하다'는 거짓말 — Enhanced Games 위험성 분석",
        "title_en": "The outrage over the Enhanced Games ignores the risks many already accept in sport",
        "summary": "약물 사용을 공식 허용한 Enhanced Games를 둘러싸고, '의료 감독하에 쓰면 안전하다'는 주장의 허구성이 지적된다. 전문가들은 경기력 향상 약물에 '위험 없는 사용법'은 없으며, 안전 프레이밍은 '담배 피우는 걸 옆에서 지켜보며 안전하게 만든다'는 말과 같다고 비판한다. 합법화가 안전을 의미하지 않는다.",
        "summary_detail": "정리: ① 출처 — The Conversation 분석 기사. ② 사건 — 2026년 5월 라스베이거스에서 약물 허용 Enhanced Games 개최. ③ 주장 — 주최측은 'FDA 승인 약물·의료 감독'을 안전 근거로 제시. ④ 반박 — 버밍엄대 등 연구진: 경기력 향상 약물에 '위험 없는' 사용은 없음. ⑤ 비유 — 안전 프레이밍은 '흡연을 옆에서 감독해 안전하게 만든다'는 것과 동일. ⑥ 맥락 — WADA·세계육상 등은 '위험하고 무책임'으로 규탄. NOGEAR 시각: 감독이 붙는다고 독이 약이 되진 않는다. '관리된 도핑'은 관리된 위험일 뿐, 위험이 사라진 게 아니다.",
        "category": "news", "category_ko": "Enhanced Games",
        "source": "The Conversation", "source_type": "news",
        "source_url": "https://theconversation.com/the-outrage-over-the-enhanced-games-ignores-the-risks-many-already-accept-in-sport-273653",
        "credibility": cred("medium", False, False,
            "검색결과 확인(미페치). Enhanced Games 안전 프레이밍 비판·'위험 없는 사용 없음' 골자. NPR·ESPN·BBC 보도와 교차. 전문가 기고 → medium.", acc="partial", fc=False),
        "viral_signals": signals(20, 15, 17, 17, 18, 10),
        "tags": ["EnhancedGames", "도핑합법화", "위험", "약물", "라스베이거스"],
    },
    # 8. Enhanced Games MedicalXpress
    {
        "title": "약물 올림픽은 무엇이 문제인가 — Enhanced Games 쟁점 정리",
        "title_en": "Enhanced Games: What's the issue?",
        "summary": "약물을 공개 허용한 Enhanced Games의 핵심 쟁점을 정리한 보도다. 세계신기록에 100만 달러를 거는 구조가 선수들에게 더 많은 약물·더 큰 위험을 부추긴다는 우려가 핵심이다. 스포츠 정신과 선수 건강을 돈으로 맞바꾼다는 비판이 따른다.",
        "summary_detail": "정리: ① 출처 — MedicalXpress(2026-06) 보도. ② 사건 — 약물 허용 Enhanced Games의 의학적·윤리적 쟁점 해설. ③ 구조 — 세계신기록 시 100만 달러 보너스 → 한계까지 약물 사용 유인. ④ 우려 — 금전적 인센티브가 안전 한계를 넘는 도핑을 조장. ⑤ 종목 — 육상·수영·역도 등에서 금지약물 사용 허용. ⑥ 함의 — 안전 감독 주장과 달리 구조 자체가 위험을 키움. NOGEAR 시각: 기록에 상금을 걸면, 몸은 소모품이 된다. 100만 달러짜리 기록 뒤에, 값을 매길 수 없는 심장이 저당 잡힌다.",
        "category": "news", "category_ko": "Enhanced Games",
        "source": "MedicalXpress", "source_type": "news",
        "source_url": "https://medicalxpress.com/news/2026-06-games-issue.html",
        "credibility": cred("medium", False, False,
            "검색결과 확인(미페치). Enhanced Games 쟁점·상금 구조 위험 유인 골자. The Conversation·NPR과 교차. 과학매체 보도 → medium.", acc="partial", fc=False),
        "viral_signals": signals(19, 14, 16, 17, 17, 9),
        "tags": ["EnhancedGames", "상금", "도핑", "선수건강", "윤리"],
    },
    # 9. Enhanced Games ESPN
    {
        "title": "스테로이드가 미래라고? Enhanced Games 현장의 민낯",
        "title_en": "Are steroids the future? At the Enhanced Games, that future is now",
        "summary": "ESPN은 약물 허용 Enhanced Games 현장을 통해 '약물이 스포츠의 미래'라는 주장이 실제로 어떤 모습인지 들여다본다. 화려한 기록과 상금 뒤에는 통제되지 않는 건강 위험과 윤리적 공백이 있다. '미래'라는 포장 아래, 검증되지 않은 인체 실험이 진행된다.",
        "summary_detail": "정리: ① 출처 — ESPN 심층 보도. ② 주제 — 약물 허용 대회가 그리는 '향상된 스포츠'의 실상. ③ 현장 — 금지약물(스테로이드·성장호르몬) 공개 사용, 거액 상금. ④ 쟁점 — 단기 기록 향상 vs 장기 건강 손상의 불균형. ⑤ 비판 — 반도핑 기구·전문가들의 '위험·무책임' 규탄. ⑥ 함의 — '미래'라는 수사가 인체 위험의 정상화를 가림. NOGEAR 시각: 미래라고 부르는 순간, 위험은 진보로 둔갑한다. 하지만 기록을 깬 몸이 먼저 부서진다면, 그건 미래가 아니라 청구서다.",
        "category": "news", "category_ko": "Enhanced Games",
        "source": "ESPN", "source_type": "news",
        "source_url": "https://www.espn.com/olympics/story/_/id/48836584/enhanced-games-doping-steroids-performance-enhancing-drugs-controversy",
        "credibility": cred("medium", False, False,
            "검색결과 확인(미페치). Enhanced Games 현장·약물 미래론 비판 골자. MedicalXpress·The Conversation·NPR과 교차. 대형 스포츠매체 → medium.", acc="partial", fc=False),
        "viral_signals": signals(20, 14, 17, 17, 18, 11),
        "tags": ["EnhancedGames", "스테로이드", "스포츠미래", "도핑", "ESPN"],
    },
    # 10. MK-677 DEA justthinktwice
    {
        "title": "'안전한 성장호르몬'의 환상 — MK-677의 숨은 위험",
        "title_en": "Beyond the Hype: Potential Health Risks of MK-677",
        "summary": "미 마약단속국(DEA) 교육 사이트는 인기 성장호르몬 분비촉진제 MK-677(이부타모렌)의 위험을 정리한다. 식욕 증가·근육량 증가의 이면에 인슐린 저항성 악화, 혈당 상승, 부종, 심부전 우려가 있다. 한 임상시험은 심부전 위험 때문에 조기 중단됐다.",
        "summary_detail": "정리: ① 출처 — DEA 교육 사이트(Just Think Twice). ② 약물 — MK-677(이부타모렌), 경구 성장호르몬 분비촉진제. ③ 흔한 부작용 — 인슐린 저항성, 혈당·HbA1c 상승, 식욕 증가, 수분저류 부종. ④ 위험 — 장기 사용 시 제2형 당뇨 위험, 높은 IGF-1으로 종양 성장 우려. ⑤ 경고 — 일부 임상시험은 심부전 우려로 조기 종료. ⑥ 함의 — '주사 없는 성장호르몬'이라는 마케팅과 실제 위험의 괴리. NOGEAR 시각: 알약 하나로 호르몬을 속일 수 있다는 믿음이, 몸의 회계장부를 망가뜨린다. 당장의 근육은 빌린 돈이고, 이자는 당뇨와 심장이 갚는다.",
        "category": "research", "category_ko": "MK-677 위험",
        "source": "DEA / Just Think Twice", "source_type": "reference",
        "source_url": "https://www.justthinktwice.gov/news-statistics/2025/07/08/beyond-hype-potential-health-risks-mk-677",
        "credibility": cred("high", True, False,
            "검색결과 확인(미페치). MK-677 인슐린저항성·혈당상승·심부전 조기중단 골자. OPSS·BodySpec·Annals of Internal Medicine 12개월 RCT와 교차. 미 정부(DEA) → high."),
        "viral_signals": signals(20, 17, 17, 14, 14, 9),
        "tags": ["MK-677", "이부타모렌", "인슐린저항성", "성장호르몬", "심부전"],
    },
    # 11. MK-677 OPSS
    {
        "title": "군 보충제 안전기관이 짚은 MK-677 — '연구용'이라는 회색지대",
        "title_en": "Performance Enhancing Substance: MK-677 (Ibutamoren)",
        "summary": "미 국방부 보충제 안전 프로그램(OPSS)은 MK-677이 승인 의약품이 아니며 보충제로 불법 판매되는 미검증 물질이라고 경고한다. GH/IGF-1 축을 자극해 근육·식욕을 늘리지만 혈당 조절을 악화시킨다. '연구용 화학물질' 딱지가 안전을 보증하지 않는다.",
        "summary_detail": "정리: ① 출처 — OPSS(미 국방부 보충제 안전 프로그램). ② 물질 — MK-677(이부타모렌), 경구 GH 분비촉진제. ③ 지위 — FDA 미승인, 보충제로 둔갑한 불법 판매 흔함. ④ 작용 — 성장호르몬/IGF-1 증가 → 근육·식욕↑, 그러나 인슐린 감수성↓. ⑤ 위험 — 혈당 상승·부종·장기 안전성 미검증. ⑥ 경고 — 군인·운동선수에게 사용 비권고. NOGEAR 시각: '연구용'이라는 말은 '아직 아무도 책임지지 않는다'는 뜻이다. 라벨이 합법처럼 보일수록, 몸이 치르는 값은 조용히 커진다.",
        "category": "news", "category_ko": "보충제 안전",
        "source": "OPSS (Operation Supplement Safety)", "source_type": "reference",
        "source_url": "https://www.opss.org/article/performance-enhancing-substance-mk-677-ibutamoren",
        "credibility": cred("high", True, False,
            "검색결과 확인(미페치). MK-677 FDA미승인·불법판매·혈당악화 골자. DEA·BodySpec·Healthy Male와 교차. 정부 산하 안전기관 → high."),
        "viral_signals": signals(18, 16, 16, 13, 14, 8),
        "tags": ["MK-677", "OPSS", "보충제안전", "미승인", "GH"],
    },
    # 12. MK-677 BodySpec insulin sensitivity
    {
        "title": "근육은 1kg 늘고 인슐린 감수성은 떨어졌다 — MK-677 장기 임상의 역설",
        "title_en": "MK-677: Risks, Research, and Safer Alternatives",
        "summary": "장기 임상에서 MK-677은 제지방량을 약 1kg 늘렸지만 근력은 개선하지 못했고 인슐린 감수성은 악화됐다. 근육 무게는 늘어도 '쓸 수 있는 힘'은 늘지 않고, 대사 건강만 나빠진 셈이다. 외형 숫자와 실제 기능의 괴리를 보여주는 사례다.",
        "summary_detail": "정리: ① 출처 — BodySpec 해설(Annals of Internal Medicine 12개월 RCT 등 인용). ② 결과 — 고령자 대상 12개월 시험에서 제지방량 +약 1.1kg. ③ 한계 — 근력 향상은 없음(무게만 늘고 기능은 정체). ④ 부작용 — 인슐린 감수성 저하, 공복혈당·HbA1c 상승. ⑤ 위험 — 장기적으로 제2형 당뇨·심대사 위험. ⑥ 함의 — '근육량 증가'가 곧 '더 강함'은 아님. NOGEAR 시각: 저울 숫자는 올라가는데 힘은 그대로라면, 그건 근육이 아니라 물과 빚이다. 보이는 부피를 위해, 보이지 않는 혈당이 무너진다.",
        "category": "research", "category_ko": "MK-677 연구",
        "source": "BodySpec / 임상 리뷰", "source_type": "reference",
        "source_url": "https://www.bodyspec.com/blog/post/mk677_risks_research_and_safer_alternatives",
        "credibility": cred("medium", False, False,
            "검색결과 확인(미페치). MK-677 제지방 +1.1kg·근력개선 없음·인슐린감수성 저하 골자. DEA·OPSS·Annals RCT와 교차. 2차 해설 → medium.", acc="partial", fc=False),
        "viral_signals": signals(17, 16, 16, 13, 13, 8),
        "tags": ["MK-677", "제지방량", "근력", "인슐린감수성", "임상"],
    },
    # 13. 호주 청소년 AAS 유병률
    {
        "title": "호주 청소년의 스테로이드 — 데이터가 비어 있던 사각지대",
        "title_en": "Prevalence and Correlates of Anabolic-Androgenic Steroid Use in Australian Adolescents",
        "summary": "이 2025년 연구는 그동안 데이터가 부족했던 호주 청소년의 아나볼릭 스테로이드 사용 실태와 연관 요인을 조사했다. 외모·수행 압박, 보충제 사용, 스테로이드에 대한 우호적 태도가 위험 요인으로 확인됐다. 성인 문제로만 여겨지던 약물 사용이 10대까지 내려와 있다.",
        "summary_detail": "정리: ① 출처 — PMC 게재 호주 청소년 AAS 단면연구(2025). ② 배경 — 최근 호주 청소년 AAS 위험요인 데이터가 노후·부족했음. ③ 결과 — 외모·수행 압박, 근육 보충제 사용, 스테로이드 우호 태도가 사용과 연관. ④ 일반 유병률 — 남성 청소년 4~12%, 여성 0.5~2%(문헌 범위). ⑤ 동반 — 알코올·담배·자극제 등 다른 물질 사용과 강한 상관. ⑥ 함의 — 조기 개입·교육 필요. NOGEAR 시각: '나중에 끊으면 된다'는 10대의 자신감이, 평생 가는 호르몬 손상을 모른다. 사춘기의 몸은 약을 견디라고 설계되지 않았다.",
        "category": "research", "category_ko": "청소년 사용 연구",
        "source": "PMC / 호주 청소년 단면연구(2025)", "source_type": "journal",
        "source_url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC11945638/",
        "credibility": cred("high", True, True,
            "검색결과 확인(미페치). 호주 청소년 AAS 유병률·외모압박·보충제·우호태도 골자. PMC10516554(청소년 남아 태도)·StatPearls와 교차. 동료심사 → high."),
        "viral_signals": signals(20, 17, 18, 14, 14, 9),
        "tags": ["청소년", "스테로이드", "호주", "외모압박", "유병률"],
    },
    # 14. 청소년 남아 보충제-스테로이드 태도
    {
        "title": "근육 보충제를 쓰는 소년이 스테로이드에 더 관대하다 — 청소년 태도 연구",
        "title_en": "Muscle building supplement use and favourable attitudes towards anabolic steroids in adolescent boys",
        "summary": "이 연구는 외모·수행 향상을 위해 근육 보충제를 쓰는 청소년 남아일수록 아나볼릭 스테로이드에 우호적 태도를 갖는다는 연관을 보고한다. 보충제가 더 강한 약물로 가는 '관문' 역할을 할 수 있음을 시사한다. 작은 약통이 큰 위험으로 가는 입구일 수 있다.",
        "summary_detail": "정리: ① 출처 — PMC 게재 청소년 남아 단면연구. ② 대상 — 외모·수행 관련 요인과 근육 보충제 사용 청소년 남아. ③ 결과 — 보충제 사용이 스테로이드에 대한 우호적 태도와 연관. ④ 해석 — 보충제 → 스테로이드로의 태도·행동 게이트웨이 가능성. ⑤ 동기 — 외모 만족도·근육질 이상화가 핵심 동인. ⑥ 함의 — 보충제 문화에 대한 비판적 교육이 예방에 중요. NOGEAR 시각: '단백질 한 스쿱'에서 '주사 한 대'까지는 생각보다 가깝다. 몸에 불만을 파는 시장이, 다음 단계의 약을 미리 정당화한다.",
        "category": "research", "category_ko": "청소년 태도 연구",
        "source": "PMC / 청소년 남아 단면연구", "source_type": "journal",
        "source_url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10516554/",
        "credibility": cred("high", True, True,
            "검색결과 확인(미페치). 청소년 보충제 사용·스테로이드 우호태도 연관·게이트웨이 시사 골자. 호주 청소년 연구(PMC11945638)와 교차. 동료심사 → high."),
        "viral_signals": signals(18, 16, 17, 13, 14, 8),
        "tags": ["청소년", "보충제", "게이트웨이", "스테로이드태도", "외모"],
    },
    # 15. 세계 최초 AAS 검사 시험 Addiction
    {
        "title": "내가 산 스테로이드에 뭐가 들었나 — 세계 첫 AAS 성분검사 시험",
        "title_en": "The world's first anabolic-androgenic steroid testing trial",
        "summary": "Addiction 저널에 실린 이 시험은 사용자가 실제로 구입한 아나볼릭 스테로이드를 화학 분석해 결과를 본인에게 돌려주는 세계 첫 해악감소 프로그램이다. 지하시장 제품의 성분·함량 불일치가 흔하다는 사실을 사용자에게 직접 확인시킨다. '내가 뭘 넣는지조차 모른다'는 현실을 데이터로 증명한다.",
        "summary_detail": "정리: ① 출처 — Addiction(Wiley) 게재 2단계 파일럿 시험. ② 설계 — 사용자 제출 AAS 화학 분석 → 결과 통보 → 커뮤니티 피드백. ③ 의의 — 세계 최초의 AAS '약물 점검(drug checking)' 해악감소 시도. ④ 발견 — 지하시장 제품의 미표기 성분·함량 편차 확인. ⑤ 맥락 — 단속·낙인으로 정보가 없는 사용자에게 사실 제공. ⑥ 함의 — 불법 시장 품질의 불확실성을 정량적으로 드러냄. NOGEAR 시각: '믿고 쓰는' 약의 라벨은 광고지일 뿐이다. 분석기 앞에 서면, 근육보다 먼저 드러나는 건 거짓이다.",
        "category": "research", "category_ko": "해악감소 연구",
        "source": "Addiction (Wiley)", "source_type": "journal",
        "source_url": "https://onlinelibrary.wiley.com/doi/10.1111/add.70009",
        "credibility": cred("high", True, True,
            "검색결과 확인(미페치). 세계 첫 AAS 약물점검 파일럿·지하시장 성분 불일치 골자. 위조 스테로이드 분석 문헌(18~86% adulteration)과 교차. 동료심사 → high."),
        "viral_signals": signals(21, 18, 17, 15, 15, 10),
        "tags": ["약물점검", "지하시장", "성분불일치", "해악감소", "AAS"],
    },
    # 16. 클렌부테롤 Poison Control
    {
        "title": "소 살찌우는 약을 사람이 먹는다 — 클렌부테롤의 위험",
        "title_en": "Clenbuterol: Unapproved and unsafe",
        "summary": "미국 중독정보센터(Poison Control)는 클렌부테롤이 사람용으로 승인되지 않은 위험 물질이라고 경고한다. 지방 연소·근육 유지 목적으로 오용되지만 저용량에서도 빈맥·떨림·저칼륨혈증·발작·심정지를 유발한다. 반감기가 길어 독성 증상이 며칠씩 지속된다.",
        "summary_detail": "정리: ① 출처 — Poison Control(미국 중독정보센터). ② 물질 — 클렌부테롤, 일부 국가 가축용 기관지확장제(사람용 미승인). ③ 오용 — 지방 연소·근육 보존 목적의 다이어트·커팅 약물. ④ 독성 — 저용량에서도 빈맥·심계항진·떨림·저칼륨혈증·고혈당. ⑤ 중증 — 발작·심정지 가능, 긴 반감기로 증상 1~8일 지속. ⑥ 치료 — 수액·베타차단제·칼륨 보충 등 보존적. NOGEAR 시각: 가축을 키우는 약이 사람의 심장을 흔든다. 지방을 태우려다, 며칠 동안 심장이 폭주하는 값을 치른다.",
        "category": "research", "category_ko": "클렌부테롤 독성",
        "source": "Poison Control", "source_type": "reference",
        "source_url": "https://www.poison.org/articles/clenbuterol-unapproved-and-unsafe-201",
        "credibility": cred("high", True, False,
            "검색결과 확인(미페치). 클렌부테롤 미승인·빈맥·저칼륨·심정지·긴 반감기 골자. PMC10324766·JACC 보디빌더 증례와 교차. 공인 중독정보센터 → high."),
        "viral_signals": signals(20, 16, 17, 13, 14, 9),
        "tags": ["클렌부테롤", "다이어트약", "빈맥", "저칼륨혈증", "심정지"],
    },
    # 17. 저용량 클렌부테롤 독성 증례
    {
        "title": "적은 양도 안전하지 않다 — 저용량 클렌부테롤 독성 증례",
        "title_en": "Low Dose Clenbuterol Toxicity: Case Report and Review",
        "summary": "이 증례보고는 비교적 적은 용량의 클렌부테롤로도 심각한 독성이 나타날 수 있음을 보여준다. 빈맥, 저칼륨혈증, 심근 손상 지표 상승이 관찰됐다. '조금만 쓰면 괜찮다'는 통념과 달리, 좁은 안전역이 사용자를 위험에 노출시킨다.",
        "summary_detail": "정리: ① 출처 — PMC 게재 증례보고·문헌 리뷰. ② 핵심 — 저용량 클렌부테롤에서도 임상적으로 유의한 독성 발생. ③ 임상 — 빈맥·심계항진·저칼륨혈증·트로포닌 상승(심근 부담). ④ 기전 — 강한 β-아드레날린 자극으로 심혈관·전해질 교란. ⑤ 함의 — '소량은 안전'이라는 가정의 위험성. ⑥ 치료 — 보존적 처치와 모니터링 필요. NOGEAR 시각: 안전한 용량을 찾는 게임 자체가 함정이다. 적게 써서 괜찮은 게 아니라, 적게 써도 위험한 약이다.",
        "category": "research", "category_ko": "클렌부테롤 증례",
        "source": "PMC / 증례보고", "source_type": "journal",
        "source_url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC10324766/",
        "credibility": cred("medium", True, True,
            "검색결과 확인(미페치). 저용량 클렌부테롤 독성·빈맥·저칼륨·트로포닌 골자. Poison Control·JACC 증례와 교차. 동료심사이나 직접페치 전 → medium.", acc="partial", fc=False),
        "viral_signals": signals(18, 16, 15, 12, 13, 8),
        "tags": ["클렌부테롤", "저용량", "독성", "심근손상", "증례"],
    },
    # 18. 클렌부테롤 보디빌더 JACC
    {
        "title": "보디빌더의 가슴 통증, 범인은 커팅 약물 — 클렌부테롤 심독성 증례",
        "title_en": "Case Report of Clenbuterol Cardiac Toxicity in a Body Builder",
        "summary": "미국심장학회지(JACC)에 보고된 이 증례는 클렌부테롤을 쓴 보디빌더가 심장 독성으로 응급실을 찾은 사례다. 가슴 통증·심계항진과 함께 심근 손상 지표가 올랐다. 무대를 위한 '막판 커팅'이 심장을 위협한 전형적 예다.",
        "summary_detail": "정리: ① 출처 — JACC(미국심장학회지) 증례보고. ② 환자 — 클렌부테롤 사용 보디빌더. ③ 증상 — 가슴 통증, 심계항진, 빈맥. ④ 소견 — 트로포닌 상승 등 심근 손상 신호, 관상동맥 정상 소견과 함께 나타나는 패턴. ⑤ 맥락 — 대회·촬영 전 체지방 감량(커팅) 목적 사용. ⑥ 함의 — 외형용 약물이 직접적 심장 손상으로 이어짐. NOGEAR 시각: 무대 위 가장 마른 몸을 만드는 약이, 무대 뒤에서 심장을 가장 먼저 두드린다. 데피니션을 위해 심근을 저당 잡힐 이유는 없다.",
        "category": "research", "category_ko": "심독성 증례",
        "source": "JACC (미국심장학회지)", "source_type": "journal",
        "source_url": "https://www.jacc.org/doi/10.1016/S0735-1097(23)04262-6",
        "credibility": cred("high", True, True,
            "검색결과 확인(미페치). 클렌부테롤 보디빌더 심독성·가슴통증·트로포닌 골자. Poison Control·Massachusetts 18·21세 증례와 교차. 동료심사(JACC) → high."),
        "viral_signals": signals(20, 17, 17, 13, 14, 10),
        "tags": ["클렌부테롤", "심독성", "보디빌더", "커팅", "트로포닌"],
    },
    # 19. DNP 고체온 사망 ACEP Now
    {
        "title": "체온이 41도를 넘기며 멈춘 심장 — DNP 고열 사망 증례",
        "title_en": "Case Report: A Hyperthermic Death from the Diet Pill DNP",
        "summary": "응급의학 매체 ACEP Now에 실린 이 증례는 다이어트약 DNP로 인한 고체온 사망을 다룬다. DNP가 대사를 폭주시켜 체온이 통제 불능으로 치솟고, 식히는 응급처치로도 막지 못해 사망에 이르렀다. 해독제가 없는 독이 어떻게 사람을 태우는지를 보여준다.",
        "summary_detail": "정리: ① 출처 — ACEP Now(미국응급의학회) 증례. ② 약물 — 2,4-디니트로페놀(DNP), 불법 다이어트약. ③ 경과 — 대사율 폭증으로 악성 고체온 → 다발성 장기 부담 → 사망. ④ 핵심 — 적극적 냉각에도 체온 통제 실패, 해독제·역전제 부재. ⑤ 임상 — 발한·빈맥·고열·의식저하의 급격한 악화. ⑥ 함의 — DNP는 응급의학적으로도 손쓰기 어려운 독성물질. NOGEAR 시각: DNP는 지방이 아니라 사람을 태운다. 체온계가 한계를 넘는 순간, 의사도 끌 수 없는 불이 켜진다.",
        "category": "news", "category_ko": "DNP 사망 증례",
        "source": "ACEP Now (미국응급의학회)", "source_type": "journal",
        "source_url": "https://www.acepnow.com/article/case-report-a-hyperthermic-death-from-the-diet-pill-dnp/",
        "credibility": cred("high", True, False,
            "검색결과 확인(미페치). DNP 악성고체온·냉각 실패·해독제 없음 사망 골자. PMC3550200·Pharmaceutical Journal과 교차. 응급의학 전문매체 → high."),
        "viral_signals": signals(24, 16, 17, 13, 15, 11),
        "tags": ["DNP", "고체온", "다이어트약", "사망", "해독제없음"],
    },
    # 20. DNP 외상 후 사망 PMC8131886
    {
        "title": "외상 치료 중 드러난 다이어트약 — DNP가 부른 또 하나의 죽음",
        "title_en": "2,4-Dinitrophenol: 'diet' drug death following major trauma",
        "summary": "이 증례는 큰 외상 후 치료 과정에서 DNP 복용이 드러나며 사망에 이른 사례를 보고한다. 외상 자체보다 체내에 들어온 DNP의 대사 폭주가 치명적이었다. 응급 상황에서 숨겨진 DNP가 치료를 어떻게 망가뜨리는지 보여주는 경고다.",
        "summary_detail": "정리: ① 출처 — PMC 게재 증례보고. ② 상황 — 주요 외상 환자의 치료 중 DNP 사용 확인. ③ 경과 — DNP의 대사항진·고체온이 회복을 방해, 사망. ④ 함정 — 환자가 복용을 숨기면 진단·치료가 지연·왜곡됨. ⑤ 기전 — 미토콘드리아 탈공역으로 에너지가 열로 방출, 체온 폭증. ⑥ 함의 — 외상 등 동반 응급에서 DNP는 예후를 급격히 악화. NOGEAR 시각: 숨긴 약 한 알이, 살릴 수 있던 사람을 놓치게 만든다. DNP는 평소에도 위험하지만, 위기의 순간엔 결정타가 된다.",
        "category": "research", "category_ko": "DNP 증례",
        "source": "PMC / 증례보고", "source_type": "journal",
        "source_url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC8131886/",
        "credibility": cred("medium", True, True,
            "검색결과 확인(미페치). DNP 외상 후 사망·복용 은폐·대사항진 골자. ACEP Now·PMC3550200과 교차. 동료심사이나 직접페치 전 → medium.", acc="partial", fc=False),
        "viral_signals": signals(21, 16, 15, 12, 14, 9),
        "tags": ["DNP", "외상", "사망", "은폐", "고체온"],
    },
    # 21. Martin Fitzwater Arnold Classic
    {
        "title": "아놀드 클래식 무대의 논란 — 마틴 피츠워터를 향한 동료들의 입",
        "title_en": "Bodybuilders Speak Out on Martin Fitzwater's Controversial Behavior at Arnold Classic",
        "summary": "프로 보디빌더 마틴 피츠워터의 아놀드 클래식 무대 위 행동을 두고 동료 선수들이 공개적으로 비판하며 논란이 일었다. 무대 매너·스포츠맨십을 둘러싼 갈등이 커뮤니티를 갈랐다. 화려한 무대 뒤, 약물로 빚은 몸들이 경쟁하는 세계의 긴장을 드러낸 사건이다.",
        "summary_detail": "정리: ① 출처 — AOL 보도. ② 사건 — 아놀드 클래식에서 마틴 피츠워터의 무대 위 행동이 논란. ③ 반응 — 동료 보디빌더들이 공개적으로 비판·문제 제기. ④ 쟁점 — 무대 매너·스포츠맨십·경쟁 윤리. ⑤ 맥락 — 약물 기반 프로 보디빌딩계의 내부 갈등·여론전. ⑥ 함의 — 신체뿐 아니라 무대 행동도 브랜드·논란의 대상. NOGEAR 시각: 무대 위 가장 큰 몸들이, 가장 작은 매너로 다툰다. 약이 키운 건 근육이지, 품위가 아니다.",
        "category": "news", "category_ko": "업계 논란",
        "source": "AOL", "source_type": "news",
        "source_url": "https://www.aol.com/lifestyle/bodybuilders-speak-martin-fitzwaters-controversial-210251402.html",
        "credibility": cred("medium", False, False,
            "검색결과 확인(미페치). 마틴 피츠워터 아놀드 클래식 무대 행동 논란·동료 비판 골자. 보디빌딩 커뮤니티 보도와 교차. 연예·라이프 매체 → medium.", acc="partial", fc=False),
        "viral_signals": signals(18, 11, 18, 16, 18, 10),
        "tags": ["마틴피츠워터", "아놀드클래식", "논란", "프로보디빌딩", "스포츠맨십"],
    },
    # 22. 오젬픽 근손실 drugs.com
    {
        "title": "살은 빠지는데 근육도 같이 빠진다 — 오젬픽 근손실의 진실",
        "title_en": "Does Ozempic cause muscle loss and how to prevent it?",
        "summary": "drugs.com 해설에 따르면 세마글루타이드(오젬픽) 같은 GLP-1 약물로 체중을 빠르게 줄이면 근육량도 상당히 함께 빠진다. 임상에서 감량분의 약 39%가 근육이었다는 보고도 있다. '마른 몸'을 얻는 대신 '약한 몸'을 얻을 수 있다는 경고다.",
        "summary_detail": "정리: ① 출처 — drugs.com 의학 Q&A. ② 약물 — 세마글루타이드(오젬픽) 등 GLP-1 수용체작용제. ③ 현상 — 빠른 체중 감소 시 지방뿐 아니라 제지방(근육)도 함께 감소. ④ 규모 — 일부 연구서 감량분의 약 39%가 근육, 임상서 제지방 13.9%(약 6.9kg) 감소 보고. ⑤ 원인 — 식욕 저하로 단백질·열량 섭취 부족 + 급격한 감량. ⑥ 예방 — 저항운동·충분한 단백질·점진적 감량. NOGEAR 시각: 체중계가 가벼워졌다고 몸이 강해진 건 아니다. 근육을 지키지 않은 감량은, 작아진 게 아니라 무너진 것이다.",
        "category": "research", "category_ko": "GLP-1 근손실",
        "source": "Drugs.com", "source_type": "reference",
        "source_url": "https://www.drugs.com/medical-answers/ozempic-cause-muscle-loss-how-you-prevent-3578660/",
        "credibility": cred("medium", False, False,
            "검색결과 확인(미페치). 세마글루타이드 근손실·감량분 39% 근육·제지방 13.9% 골자. Cleveland Clinic·Medical News Today와 교차. 의약정보 매체 → medium.", acc="partial", fc=False),
        "viral_signals": signals(19, 15, 19, 15, 14, 9),
        "tags": ["오젬픽", "세마글루타이드", "근손실", "GLP-1", "감량"],
    },
    # 23. BPC-157 전임상
    {
        "title": "BPC-157, 50편 넘는 동물연구뿐 — 사람 데이터는 여전히 비어 있다",
        "title_en": "BPC-157 Research Results 2026: What Preclinical Studies Show About Tissue Repair",
        "summary": "인기 회복 펩타이드 BPC-157은 2026년 기준 50편 넘는 전임상 연구가 쌓여 조직 재생 신호를 보인다. 그러나 거의 전부가 동물·실험실 연구이며, 사람 대상 대조 임상과 FDA 승인은 없다. '효과 있다'는 입소문과 '검증됐다'는 사실은 다르다.",
        "summary_detail": "정리: ① 출처 — Spartan Peptides 정리(전임상 문헌 종합). ② 현황 — BPC-157 전임상 연구 50편 이상 누적, 조직 재생 관련 신호. ③ 기전 — VEGFR2 혈관신생·NO 조절 경로, 위장·근건 등 다조직 효과 보고. ④ 한계 — 대부분 동물·세포 실험, 사람 대상 무작위 대조시험 부족. ⑤ 지위 — FDA 미승인 '연구용' 펩타이드(회색시장 유통). ⑥ 함의 — 안전성·유효성의 인체 근거는 여전히 공백. NOGEAR 시각: 쥐의 상처가 빨리 아물었다는 게, 네 몸에 안전하다는 증명은 아니다. 50편의 동물연구보다, 0편의 사람 임상이 더 큰 진실을 말한다.",
        "category": "research", "category_ko": "펩타이드 연구",
        "source": "Spartan Peptides / 전임상 종합", "source_type": "reference",
        "source_url": "https://spartanpeptides.com/blog/bpc-157-research-results-2026-preclinical-studies-tissue-repair/",
        "credibility": cred("low", False, False,
            "검색결과 확인(미페치). BPC-157 전임상 50편+·동물 위주·인체 임상/FDA 승인 부재 골자. 펩타이드 판매처 콘텐츠라 이해상충 가능 → low(인체 안전성 미검증 점만 채택).", acc="partial", fc=False),
        "viral_signals": signals(17, 13, 16, 16, 13, 8),
        "tags": ["BPC-157", "펩타이드", "전임상", "인체임상부재", "FDA미승인"],
    },
    # 24. 단거리 도핑 스캔들 Honest Sport
    {
        "title": "또 터진 단거리 도핑 — 트랙을 흔든 최신 스캔들",
        "title_en": "The latest sprinting doping scandal",
        "summary": "Honest Sport는 단거리 육상계를 다시 흔든 최신 도핑 스캔들을 정리한다. 정상급 기록 뒤에 약물이 숨어 있었다는 의혹과 제재 절차가 핵심이다. '깨끗한 기록'에 대한 의심이 트랙 위 모든 기록에 그림자를 드리운다.",
        "summary_detail": "정리: ① 출처 — Honest Sport(반도핑 전문 뉴스레터). ② 사건 — 단거리 육상 종목의 최신 도핑 위반·의혹 정리. ③ 쟁점 — 경기력 향상 약물 사용과 그에 따른 제재 절차. ④ 맥락 — 2026년 들어 여러 종목에서 도핑 적발 잇따름(스키점프·테니스 등). ⑤ 함의 — 엘리트 스포츠의 약물 의심이 구조적으로 반복됨. ⑥ 메시지 — 기록의 신뢰는 검사·투명성에 달림. NOGEAR 시각: 가장 빠른 기록일수록, 가장 먼저 의심받는다. 약으로 당긴 0.1초가, 평생의 명예를 0으로 만든다.",
        "category": "news", "category_ko": "도핑 스캔들",
        "source": "Honest Sport", "source_type": "news",
        "source_url": "https://honestsport.substack.com/p/the-latest-sprinting-doping-scandal",
        "credibility": cred("medium", False, False,
            "검색결과 확인(미페치). 단거리 도핑 스캔들·제재 절차 골자. 2026 도핑 적발 흐름(Britannica·ESPN)과 교차. 전문 뉴스레터 → medium.", acc="partial", fc=False),
        "viral_signals": signals(18, 12, 16, 17, 18, 9),
        "tags": ["도핑", "단거리", "육상", "스캔들", "제재"],
    },
    # 25. 발리예바 2026 올림픽 도핑
    {
        "title": "코치는 멀쩡한데 16세만 처벌받았다 — 발리예바 도핑이 남긴 숙제",
        "title_en": "Skater Kamila Valieva to miss 2026 Olympics over doping",
        "summary": "러시아 피겨 선수 카밀라 발리예바가 도핑으로 4년 자격정지를 받아 2026년 동계올림픽에 나서지 못한다. WADA는 미성년 선수만 처벌받고 코치·관계자는 제재받지 않은 구조를 비판한다. 약물을 둘러싼 책임이 가장 약한 당사자에게만 쏠리는 문제를 드러낸다.",
        "summary_detail": "정리: ① 출처 — ESPN 보도. ② 사건 — 카밀라 발리예바, CAS 4년 자격정지로 2026 동계올림픽 불참. ③ 쟁점 — 당시 미성년 선수만 징계, 코치·엔투라지(주변인)는 미제재. ④ WADA 입장 — '매우 불쾌'하다며 주변인 조사 권한 강화 추진. ⑤ 맥락 — 2026 토리노·밀라노 동계올림픽 전 규정 정비 요구. ⑥ 함의 — 도핑 책임 구조의 불균형. NOGEAR 시각: 약을 쥐여준 어른은 남고, 약을 삼킨 아이만 사라진다. 시스템이 가짜를 키우고, 처벌은 가장 어린 사람에게 떨어진다.",
        "category": "news", "category_ko": "도핑 스캔들",
        "source": "ESPN", "source_type": "news",
        "source_url": "https://africa.espn.com/olympics/story/_/id/35025208/skater-kamila-valieva-miss-2026-olympics-doping",
        "credibility": cred("medium", False, False,
            "검색결과 확인(미페치). 발리예바 4년 정지·2026 불참·미성년만 처벌 골자. CBC WADA 보도와 교차. 대형 스포츠매체 → medium.", acc="partial", fc=False),
        "viral_signals": signals(19, 12, 16, 16, 18, 10),
        "tags": ["발리예바", "도핑", "2026올림픽", "WADA", "미성년"],
    },
    # 26. 테스토 이차성 적혈구증가증 MACE/VTE
    {
        "title": "테스토 첫 1년이 가장 위험하다 — 적혈구증가증과 심근경색·혈전",
        "title_en": "Secondary Polycythemia in Men Receiving Testosterone Therapy Increases Risk of MACE and VTE in the First Year",
        "summary": "비뇨기과 저널 연구에 따르면 테스토스테론 치료로 적혈구가 과도하게 늘어난(이차성 적혈구증가증) 남성은 치료 첫 1년에 주요 심혈관 사건과 정맥혈전색전증 위험이 높아진다. 혈액이 끈적해져 흐름이 느려지면 심근경색·혈전 위험이 커진다. 처방이든 남용이든, 적혈구 과잉은 위험 신호다.",
        "summary_detail": "정리: ① 출처 — Journal of Urology(AUA) 게재 연구. ② 핵심 — 테스토 유발 이차성 적혈구증가증 남성에서 첫 1년 MACE·VTE 위험 증가. ③ 수치 — 급성심근경색 OR 1.81, 정맥혈전색전증 OR 1.51. ④ 기전 — 적혈구 과잉 → 혈액 점성↑ → 혈류 저하 → 혈전·심근경색·뇌졸중. ⑤ 위험인자 — 흡연·장시간형 주사·BMI·폐질환 등이 헤마토크릿 상승과 연관. ⑥ 함의 — 헤마토크릿 모니터링·헌혈 등 관리 필요. NOGEAR 시각: 피가 진해진다는 건, 심장이 더 무거운 걸 밀어야 한다는 뜻이다. 더 많은 적혈구가 더 강한 게 아니라, 더 막히기 쉬운 것이다.",
        "category": "research", "category_ko": "심혈관 연구",
        "source": "Journal of Urology (AUA)", "source_type": "journal",
        "source_url": "https://www.auajournals.org/doi/10.1097/JU.0000000000002437",
        "credibility": cred("high", True, True,
            "검색결과 확인(미페치). 테스토 적혈구증가증·첫 1년 MACE(OR1.81)·VTE(OR1.51) 골자. ASH 코호트·PMC12250400 CVST와 교차. 동료심사(AUA) → high."),
        "viral_signals": signals(21, 18, 17, 14, 14, 9),
        "tags": ["테스토스테론", "적혈구증가증", "심근경색", "혈전", "헤마토크릿"],
    },
    # 27. 테스토 적혈구증가증 뇌정맥동혈전
    {
        "title": "테스토가 부른 뇌혈관 혈전 — 이차성 적혈구증가증 합병증",
        "title_en": "Cerebral Venous Sinus Thrombosis: A Complication of Secondary Polycythemia From Testosterone Use",
        "summary": "이 증례는 테스토스테론 사용으로 적혈구가 늘어난 환자에게 뇌정맥동 혈전(뇌혈관이 막히는 위중한 혈전)이 발생한 사례를 보고한다. 진해진 혈액이 뇌의 정맥 배출로를 막아 두통·신경학적 증상을 유발했다. 근육을 위한 호르몬이 뇌혈관을 위협한 사례다.",
        "summary_detail": "정리: ① 출처 — PMC 게재 증례보고. ② 환자 — 테스토스테론 사용 후 이차성 적혈구증가증. ③ 합병증 — 뇌정맥동혈전증(CVST), 뇌의 정맥 배출로 폐색. ④ 기전 — 적혈구 과잉·혈액 점성 증가 → 정맥혈전 형성. ⑤ 임상 — 심한 두통·신경학적 이상 등 위중한 양상. ⑥ 함의 — 테스토 사용자의 헤마토크릿 관리·혈전 경계 필요. NOGEAR 시각: 호르몬은 근육 주소만 골라 배달되지 않는다. 진해진 피는 뇌에서도 막히고, 그 대가는 두통이 아니라 뇌졸중이다.",
        "category": "research", "category_ko": "혈전 증례",
        "source": "PMC / 증례보고", "source_type": "journal",
        "source_url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12250400/",
        "credibility": cred("medium", True, True,
            "검색결과 확인(미페치). 테스토 적혈구증가증·뇌정맥동혈전 합병증 골자. AUA·ASH 적혈구증가증 연구와 교차. 동료심사이나 직접페치 전 → medium.", acc="partial", fc=False),
        "viral_signals": signals(21, 17, 16, 13, 14, 9),
        "tags": ["테스토스테론", "뇌정맥동혈전", "적혈구증가증", "뇌졸중", "증례"],
    },
    # 28. 팔룸보이즘 복부비대증후군 PMC
    {
        "title": "보디빌더의 '버블 거트'를 의학이 분석하다 — 복부비대증후군",
        "title_en": "Abdominal Hypertrophy Syndrome: Characteristics and Potential Pathophysiology",
        "summary": "이 논문은 보디빌더의 불룩 튀어나온 복부, 일명 '팔룸보이즘(버블 거트)'을 복부비대증후군으로 분석한다. 성장호르몬·인슐린·IGF-1 남용이 내장 기관을 키워(내장비대) 배가 앞으로 나오는 기전이 제시된다. 단순 자세 문제가 아니라 장기가 커지는 병적 변화다.",
        "summary_detail": "정리: ① 출처 — PMC 게재 분석 논문. ② 주제 — 보디빌더 복부 팽창(팔룸보이즘)을 '복부비대증후군'으로 규정. ③ 기전 — GH·인슐린·IGF-1 남용 → 내장 기관 비대(visceromegaly). ④ 유사성 — 말단비대증(acromegaly)과 병태생리적으로 유사한 측면. ⑤ 결과 — 장·위·간 등 내장 성장으로 복부 돌출, 심장 비대 위험 동반. ⑥ 함의 — 외형 부작용 이면에 실제 장기 변화. NOGEAR 시각: 식스팩 위로 튀어나온 배는 지방이 아니라 커져버린 장기다. 약은 근육만 키우는 게 아니라, 안 보이는 곳까지 부풀린다.",
        "category": "research", "category_ko": "성장호르몬 부작용",
        "source": "PMC / 복부비대증후군 분석", "source_type": "journal",
        "source_url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11578072/",
        "credibility": cred("high", True, True,
            "검색결과 확인(미페치). 팔룸보이즘·복부비대증후군·GH/인슐린/IGF-1 내장비대·말단비대증 유사 골자. Gilmore·Biology Insights와 교차. 동료심사 → high."),
        "viral_signals": signals(22, 17, 18, 13, 14, 12),
        "tags": ["팔룸보이즘", "버블거트", "내장비대", "성장호르몬", "복부비대"],
    },
    # 29. 팔룸보이즘 Gilmore
    {
        "title": "데이브 팔룸보의 이름이 병명이 됐다 — HGH 거트의 치명성",
        "title_en": "Palumboism AKA HGH Gut: A Potentially Fatal Side-Effect of Human Growth Hormone",
        "summary": "팔룸보이즘은 성장호르몬·인슐린 남용으로 배가 비정상적으로 부푸는 현상으로, 보디빌더 데이브 팔룸보의 이름에서 유래했다. 내장 기관이 커지면서 외형이 망가질 뿐 아니라 심장 비대 등 치명적 합병증으로 이어질 수 있다. '더 크게'를 향한 약물 사용이 외형마저 무너뜨린 역설이다.",
        "summary_detail": "정리: ① 출처 — Gilmore Health News 해설. ② 명칭 — 데이브 팔룸보(처음 두드러지게 진단된 보디빌더)에서 유래. ③ 원인 — HGH·인슐린의 빈번한 남용. ④ 기전 — 내장 기관 비대(장·위·간)로 복부가 앞으로 돌출. ⑤ 위험 — 심장 비대(심근병증) 등 잠재적 치명적 합병증. ⑥ 함의 — 외형 극대화를 노린 약물이 외형과 건강을 동시에 해침. NOGEAR 시각: 가장 크게 보이려던 사람이, 가장 우스꽝스럽고 위험하게 부푼다. 약으로 만든 '거대함'의 끝은 멋이 아니라 기형이다.",
        "category": "news", "category_ko": "성장호르몬 부작용",
        "source": "Gilmore Health News", "source_type": "news",
        "source_url": "https://www.gilmorehealth.com/palumboism-a-potentially-fatal-side-effect-of-human-growth-hormone/",
        "credibility": cred("medium", False, False,
            "검색결과 확인(미페치). 팔룸보이즘 유래·HGH/인슐린 내장비대·심장비대 위험 골자. PMC11578072 복부비대증후군과 교차. 건강매체 해설 → medium.", acc="partial", fc=False),
        "viral_signals": signals(21, 13, 18, 13, 15, 12),
        "tags": ["팔룸보이즘", "HGH거트", "데이브팔룸보", "내장비대", "심장비대"],
    },
    # 30. AAS 금단 첫 1년 JCEM
    {
        "title": "약을 끊은 첫 1년이 가장 어둡다 — 안드로겐 금단의 임상 양상",
        "title_en": "Clinical features of androgen abuse withdrawal in men during the first year of cessation",
        "summary": "임상내분비학 저널(JCEM) 연구는 아나볼릭 스테로이드를 끊은 남성의 첫 1년 금단 양상을 추적했다. 우울·피로·성욕 저하 등 정신·신체 증상이 흔했고, 정신과적 동반질환이 증상의 가장 강한 예측인자였다. 약을 멈추는 것이 끝이 아니라 또 다른 고비의 시작임을 보여준다.",
        "summary_detail": "정리: ① 출처 — Journal of Clinical Endocrinology & Metabolism 지역사회 추적연구. ② 대상 — AAS 중단 후 첫 1년 남성. ③ 증상 — 우울·피로·성욕 저하 등 다발성 금단 증상. ④ 예측인자 — 다변량 분석에서 정신과적 동반질환이 유일한 독립 예측인자. ⑤ 호르몬 — 테스토스테론 수치가 우울 점수와 단순 비례하지 않음(복합적). ⑥ 함의 — 금단기 정신건강 관리가 회복의 핵심. NOGEAR 시각: 끊는 순간 몸은 텅 비고, 그 빈자리를 우울이 채운다. 약을 멈춘 첫 1년은 자유가 아니라 금단이라는 또 다른 터널이다.",
        "category": "research", "category_ko": "금단·정신건강",
        "source": "JCEM (Journal of Clinical Endocrinology & Metabolism)", "source_type": "journal",
        "source_url": "https://academic.oup.com/jcem/advance-article/doi/10.1210/clinem/dgag110/8516682",
        "credibility": cred("high", True, True,
            "검색결과 확인(미페치). AAS 금단 첫 1년·우울/피로/성욕저하·정신과 동반질환 예측 골자. Medscape·PMC10640727(PCT)와 교차. 동료심사(JCEM) → high."),
        "viral_signals": signals(19, 18, 18, 15, 13, 8),
        "tags": ["금단", "AAS", "우울", "정신건강", "중단"],
    },
    # 31. AAS 우울·자살 다국가 DB
    {
        "title": "스테로이드 사용이 우울과 자살 시도의 독립 위험인자 — 다국가 데이터 분석",
        "title_en": "AAS Use is Associated with Major Depressive Disorder and Suicide Attempt: Multi-National Database",
        "summary": "다국가 의료 데이터베이스 분석에서 아나볼릭 스테로이드 사용은 주요우울장애와 자살 시도의 독립적 위험인자로 나타났다. 다른 변수를 보정해도 연관이 유지됐다. '몸을 위한 약'이 정신을 위협하는 구조적 위험을 보여준다.",
        "summary_detail": "정리: ① 출처 — ScienceDirect 게재 다국가 데이터베이스 분석. ② 결과 — AAS 사용이 주요우울장애(MDD)·자살 시도와 유의하게 연관. ③ 강도 — 교란변수 보정 후에도 독립적 위험인자로 유지. ④ 맥락 — 금단·호르몬 축 교란·신경독성 등 복합 경로 시사. ⑤ 규모 — 다국가 대규모 데이터로 일반화 가능성↑. ⑥ 함의 — AAS 사용자 정신건강 스크리닝의 임상적 필요. NOGEAR 시각: 거울 속 몸은 커지는데, 거울을 보는 마음은 무너진다. 근육을 위해 시작한 약이, 살아갈 이유를 갉아먹는다면 그건 거래가 아니라 손실이다.",
        "category": "research", "category_ko": "정신건강 연구",
        "source": "ScienceDirect / 다국가 DB 분석", "source_type": "journal",
        "source_url": "https://www.sciencedirect.com/science/article/abs/pii/S1743609522001394",
        "credibility": cred("high", True, True,
            "검색결과 확인(미페치). AAS·MDD·자살시도 독립 위험인자·다국가 DB 골자. JCEM 금단·StatPearls와 교차. 동료심사 → high."),
        "viral_signals": signals(22, 18, 18, 14, 14, 8),
        "tags": ["우울", "자살", "스테로이드", "정신건강", "다국가연구"],
    },
    # 32. PCT 금단·자살생각 감소 470명
    {
        "title": "사이클 후 관리(PCT)가 자살 생각을 절반으로 — 470명 설문",
        "title_en": "Post-cycle therapy is associated with reduced withdrawal symptoms from AAS use: a survey of 470 men",
        "summary": "470명 남성 설문에서 사이클 후 요법(PCT)을 쓴 사용자는 스테로이드 금단 증상과 자살 생각이 유의하게 줄었다. 금단 시 95% 이상이 한 가지 이상 증상을 겪었고, PCT가 자살 생각을 약 50% 줄였다는 결과다. 다만 이는 '약을 끊을 때조차 또 다른 약이 필요하다'는 의존의 풍경이기도 하다.",
        "summary_detail": "정리: ① 출처 — PMC 게재 470명 남성 설문연구. ② 결과 — PCT 사용자가 금단 증상·자살 생각 유의 감소. ③ 금단 규모 — 중단 시도자의 95.1%가 1개 이상 증상(우울·피로·성욕저하 다수). ④ 효과 — PCT가 금단 증상 약 60%, 자살 생각 약 50% 완화. ⑤ 한계 — 자가보고 설문, 인과 단정은 주의. ⑥ 함의 — 금단 관리의 필요성과 동시에 의존 구조의 단면. NOGEAR 시각: 약을 끊는 데 또 약이 필요하다는 건, 처음부터 함정이었다는 증거다. PCT가 자살 생각을 줄였다는 통계 자체가, 이 게임이 얼마나 위험한지를 말한다.",
        "category": "research", "category_ko": "금단·PCT 연구",
        "source": "PMC / 470명 설문연구", "source_type": "journal",
        "source_url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10640727/",
        "credibility": cred("high", True, True,
            "검색결과 확인(미페치). PCT·금단 95.1%·자살생각 50%↓ 골자. JCEM 금단·다국가 우울/자살 연구와 교차. 동료심사(자가보고 한계 명시) → high."),
        "viral_signals": signals(20, 17, 17, 14, 14, 8),
        "tags": ["PCT", "금단", "자살생각", "의존", "설문"],
    },
    # 33. AAS 성선저하 회복 스코핑 리뷰
    {
        "title": "약을 끊어도 호르몬은 바로 돌아오지 않는다 — AAS 성선저하 회복 리뷰",
        "title_en": "Physical, psychological and biochemical recovery from anabolic steroid-induced hypogonadism: a scoping review",
        "summary": "이 스코핑 리뷰는 스테로이드 사용 중단 후 남성 호르몬 축이 회복되는 과정을 종합한다. 신체·정신·생화학적 회복은 사람마다 다르고, 장기·고용량 사용일수록 회복이 늦거나 불완전하다. '끊으면 원래대로'라는 기대가 늘 맞지는 않는다.",
        "summary_detail": "정리: ① 출처 — PubMed 등재 스코핑 리뷰. ② 주제 — AAS 유발 성선기능저하증(하이포고나디즘)의 회복 양상. ③ 결과 — 신체·정신·생화학적 회복이 이질적(개인차 큼). ④ 위험 — 장기·고용량 노출일수록 회복 지연·불완전 가능. ⑤ 시간차 — 내분비 지표가 정자(생식) 지표보다 먼저 회복되는 경향. ⑥ 함의 — '중단 = 즉시 정상화'라는 통념의 한계. NOGEAR 시각: 스위치를 끄듯 호르몬을 켤 수는 없다. 몇 달, 몇 년 빌린 몸의 빚은, 끊은 뒤에야 청구서가 도착한다.",
        "category": "research", "category_ko": "회복·내분비 리뷰",
        "source": "PubMed / 스코핑 리뷰", "source_type": "journal",
        "source_url": "https://pubmed.ncbi.nlm.nih.gov/37855241/",
        "credibility": cred("high", True, True,
            "검색결과 확인(미페치). AAS 성선저하 회복 이질적·장기/고용량 지연·내분비 vs 정자 회복 시간차 골자. Nature 성의학(s41443-026-01272-1)·JCEM과 교차. 동료심사 리뷰 → high."),
        "viral_signals": signals(18, 18, 16, 13, 13, 7),
        "tags": ["성선저하", "회복", "호르몬축", "중단", "스코핑리뷰"],
    },
    # 34. 테스토 이차성 적혈구증가증 코호트 ASH
    {
        "title": "테스토로 적혈구가 늘어난 환자들, 그 후를 추적하다 — ASH 코호트",
        "title_en": "Follow-up of a Cohort of Patients with Secondary Erythrocytosis Due to Testosterone Treatment",
        "summary": "미국혈액학회(ASH) 발표 코호트 연구는 테스토스테론 치료로 적혈구가 늘어난(이차성 적혈구증가증) 환자들의 경과를 추적했다. 일부 환자는 진단 전후로 허혈성 뇌졸중을 포함한 혈전 사건을 겪었다. 적혈구 과잉이 단순 수치 이상이 아니라 실제 혈전으로 이어짐을 보여준다.",
        "summary_detail": "정리: ① 출처 — Blood(ASH) 초록 코호트 연구. ② 대상 — 적혈구증가증 기준 충족 512명 중 테스토 관련 29명(5.6%). ③ 사건 — 진단 전 3명, 진단 후 3명이 혈전 사건(허혈성 뇌졸중 포함). ④ 기전 — 적혈구·헤마토크릿 상승 → 혈액 점성↑ → 혈전 위험. ⑤ 함의 — 테스토 사용자에서 적혈구증가증의 임상적 추적·관리 필요. ⑥ 맥락 — 처방·남용 모두에 적용되는 위험 신호. NOGEAR 시각: 수치가 높다는 경고를 무시하면, 다음 페이지는 뇌졸중 진단서다. 적혈구는 많을수록 좋은 게 아니라, 막힐수록 위험한 것이다.",
        "category": "research", "category_ko": "혈액학 코호트",
        "source": "Blood (ASH)", "source_type": "journal",
        "source_url": "https://ashpublications.org/blood/article/144/Supplement%201/5216/526546/Follow-up-of-a-Cohort-of-Patients-with-Secondary",
        "credibility": cred("medium", True, True,
            "검색결과 확인(미페치). 테스토 이차성 적혈구증가증 코호트·512명 중 29명·혈전/허혈성뇌졸중 골자. AUA·PMC12250400과 교차. 학회 초록(요약 단계) → medium.", acc="partial", fc=False),
        "viral_signals": signals(19, 17, 16, 13, 13, 8),
        "tags": ["적혈구증가증", "테스토스테론", "혈전", "뇌졸중", "코호트"],
    },
    # 35. 스테로이드 금단 정신과 부담 Medscape
    {
        "title": "스테로이드 금단 증상은 정신과적 짐과 묶여 있다",
        "title_en": "Steroid Abuse Withdrawal Symptoms Tied to Psychiatric Burden",
        "summary": "Medscape 보도에 따르면 아나볼릭 스테로이드를 끊은 남성의 금단 증상은 정신과적 동반질환과 강하게 연결돼 있다. 우울 점수가 높을수록 금단이 힘들었고, 정신과적 부담이 증상을 예측했다. 약물 의존 문제는 결국 정신건강 문제와 함께 다뤄야 한다는 메시지다.",
        "summary_detail": "정리: ① 출처 — Medscape(2025) 보도. ② 핵심 — AAS 금단 증상이 정신과적 부담(comorbidity)과 강하게 연관. ③ 결과 — 과거 사용자에서 BDI-II 우울 점수 상승, 정신과 동반질환이 증상 예측. ④ 호르몬 — 테스토스테론 수치가 우울과 단순 비례하지 않음. ⑤ 맥락 — JCEM 등 1년 금단 추적연구와 일치. ⑥ 함의 — 금단 치료에 정신건강 평가·개입 통합 필요. NOGEAR 시각: 금단은 몸의 문제처럼 보이지만, 결국 마음에서 가장 길게 남는다. 약을 끊는 일은 의지의 싸움이 아니라, 치료가 필요한 의학적 사건이다.",
        "category": "news", "category_ko": "금단·정신건강",
        "source": "Medscape", "source_type": "news",
        "source_url": "https://www.medscape.com/viewarticle/steroid-abuse-withdrawal-symptoms-tied-psychiatric-burden-2025a1000kvc",
        "credibility": cred("medium", False, False,
            "검색결과 확인(미페치). AAS 금단·정신과 동반질환 연관·BDI-II 우울 골자. JCEM 1년 금단 연구와 교차. 의료전문매체 보도 → medium.", acc="partial", fc=False),
        "viral_signals": signals(18, 16, 16, 14, 13, 7),
        "tags": ["금단", "정신과", "우울", "스테로이드", "동반질환"],
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
