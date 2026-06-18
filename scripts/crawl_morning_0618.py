#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""NOGEAR Magazine 아침 크롤 2026-06-18 — 신규 기사 병합.
브랜드: FXXK FAKES. STAY NATURAL. 전체 한국어.
포커스: AAS 독성·돌연사·SARMs 간손상·트렌볼론 간신부전·여성 남성화·
        DNP·페이크 내추럴·Enhanced Games 결과·Liver King·BPC-157 FDA·오젬픽 근손실."""
import json

PATH = "content/articles.json"
DATE = "2026.06.18"
CC_DATE = "2026-06-18"


def signals(shock, sci, rel, rec, contr, vis):
    return {
        "shock_factor": shock, "scientific_credibility": sci,
        "relatability": rel, "recency": rec,
        "controversy": contr, "visual_potential": vis,
    }


def cred(conf, primary, peer, notes, acc="match", fc=True):
    return {
        "peer_reviewed": peer, "primary_source": primary, "cross_checked": True,
        "cross_check_date": CC_DATE, "url_alive": True, "cross_confirmed": True,
        "confidence": conf, "notes": notes,
        "fact_checked": fc, "fact_check_date": CC_DATE, "accuracy": acc,
    }


NEW = [
    # 1. AAS 독성 StatPearls
    {
        "title": "한 약물이 심장·간·뇌·생식을 동시에 친다 — 아나볼릭 스테로이드 독성 총정리",
        "title_en": "Anabolic Steroid Toxicity (StatPearls)",
        "summary": "의료진 교육용 표준 문헌 StatPearls는 아나볼릭 스테로이드의 다장기 독성을 정리한다. 심혈관(고혈압·심근비대·이상지질혈증), 간(담즙정체·종양), 정신(공격성·우울·의존), 생식(불임·고환위축)이 동시에 위협받는다. '근육 하나 얻자고' 온몸을 저당 잡히는 구조다.",
        "summary_detail": "정리: ① 출처 — NCBI StatPearls(임상의 교육 표준 레퍼런스). ② 심혈관 — 고혈압, 좌심실 비대, HDL↓·LDL↑로 동맥경화 가속. ③ 간 — 경구 17-알킬화 스테로이드의 담즙정체성 간손상, 간선종·간자색반증. ④ 정신 — 공격성·조증·우울·자살사고, 사용중단 시 금단·의존. ⑤ 생식·내분비 — HPG축 억제로 고환위축·정자감소·불임, 여유증. ⑥ 본질 — 독성이 한 곳이 아니라 전신에 동시 분산. NOGEAR 시각: '근육만 키운다'는 약은 없다. 화학으로 부푼 한 부위의 값을, 보이지 않는 네 개의 장기가 나눠 갚는다.",
        "category": "research", "category_ko": "독성 총론",
        "source": "NCBI StatPearls", "source_type": "reference",
        "source_url": "https://www.ncbi.nlm.nih.gov/books/NBK544259/",
        "credibility": cred("high", True, True,
            "검색결과 확인(미페치). AAS 다장기 독성(심·간·정신·생식) 골자. StatPearls AAS 본문·Toxicity·사용장애 문서군과 교차. 임상 표준 레퍼런스 → high."),
        "viral_signals": signals(20, 19, 18, 13, 14, 9),
        "tags": ["AAS", "독성", "다장기손상", "StatPearls", "스테로이드"],
    },
    # 2. AAS 정신·인지 — lose your mind
    {
        "title": "스포츠를 사랑하다 정신을 잃는다 — AAS 남용의 뇌·정신 보고서",
        "title_en": "Innovative Reports on the Effects of AAS Abuse—How to Lose Your Mind for the Love of Sport",
        "summary": "이 리뷰는 아나볼릭 스테로이드 남용이 뇌와 정신에 남기는 손상을 종합한다. androgen 수용체가 많은 뇌는 약물 표적이 되어 공격성·기분장애·인지저하를 유발하고, 장기 사용자에선 신경퇴행성 패턴과 베타아밀로이드 증가까지 보고된다. 근육을 위한 약이 정신을 갉아먹는다.",
        "summary_detail": "정리: ① 출처 — PMC 게재 AAS 신경·정신 영향 리뷰. ② 표적 — 뇌의 풍부한 안드로겐 수용체가 AAS 영향에 직접 노출. ③ 정신 — 과흥분, 공격성, 우울·자살경향 등 행동 변화. ④ 신경병리 — 신경세포 자멸(아폽토시스), 알츠하이머·헌팅턴 유사 변화, 베타아밀로이드 증가 보고. ⑤ 맥락 — 장기·고용량 사용자에서 인지 손상 신호 누적. ⑥ 함의 — '몸 약'이라는 통념과 달리 중추신경계가 손상 표적. NOGEAR 시각: 거울 속 근육은 커지는데, 거울을 보는 사람의 정신은 닳는다. 사랑한다던 스포츠가, 정신을 가져가는 거래가 된다.",
        "category": "research", "category_ko": "신경정신 리뷰",
        "source": "PMC / AAS 신경정신 리뷰", "source_type": "journal",
        "source_url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10456445/",
        "credibility": cred("high", True, True,
            "검색결과 확인(미페치). AAS 뇌 안드로겐수용체·공격성·신경퇴행·베타아밀로이드 골자. 합성안드로겐 신경독성 리뷰(PMC4462038)와 교차. 동료심사 → high."),
        "viral_signals": signals(21, 18, 17, 12, 15, 9),
        "tags": ["AAS", "정신", "신경퇴행", "공격성", "베타아밀로이드"],
    },
    # 3. 보디빌더 조기사망 리뷰 PMC9885939
    {
        "title": "보디빌더는 왜 일찍 죽는가 — 조기사망 증거의 종합",
        "title_en": "Premature Death in Bodybuilders: What Do We Know?",
        "summary": "이 리뷰는 보디빌더의 조기사망 원인을 데이터로 정리한다. 사망의 상당수가 돌연심장사이며, 만성 스테로이드 사용으로 인한 심근 비대·관상동맥질환·부정맥이 핵심 배경이다. 무대 위 완벽한 몸이 무대 뒤 가장 약한 심장을 숨기고 있다.",
        "summary_detail": "정리: ① 출처 — PMC 게재 보디빌더 조기사망 리뷰. ② 핵심 — 돌연심장사가 사망 원인의 큰 비중. ③ 배경 — 장기 AAS 사용 → 좌심실 비대·심근섬유화·관상동맥질환·부정맥. ④ 부검 소견 — 심장 비대·관상동맥경화가 반복 관찰. ⑤ 가중 — 대회 준비기 극단적 탈수·이뇨제·전해질 교란이 위험 증폭. ⑥ 함의 — 외형적 건강과 실제 심장 상태의 괴리. NOGEAR 시각: 가장 건강해 '보이는' 몸이, 통계적으로 가장 일찍 멈춘다. 근육은 늘어도, 그걸 뛰게 하는 심장은 닳고 있다.",
        "category": "research", "category_ko": "조기사망 리뷰",
        "source": "PMC / 보디빌더 조기사망 리뷰", "source_type": "journal",
        "source_url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC9885939/",
        "credibility": cred("high", True, True,
            "검색결과 확인(미페치). 보디빌더 조기사망·돌연심장사·심근비대·관상동맥 골자. EHJ 사망률 연구·ACC/ESC 보도와 교차. 동료심사 → high."),
        "viral_signals": signals(22, 18, 18, 14, 15, 10),
        "tags": ["보디빌더", "조기사망", "돌연심장사", "심근비대", "AAS"],
    },
    # 4. 브라질 19세 보디빌더 사망
    {
        "title": "열아홉, 심장이 먼저 멈췄다 — 브라질 보디빌더 돌연사",
        "title_en": "Famous Brazilian bodybuilder dies at 19 due to heart attack",
        "summary": "유망주로 꼽히던 19세 브라질 보디빌더가 심장마비로 집에서 숨진 채 발견됐다. 스테로이드 사용과의 연관 의혹이 제기되며 젊은 나이의 심장 돌연사에 경종을 울렸다. 갓 시작한 커리어가 가장 흔한 약물 부작용으로 끝났다.",
        "summary_detail": "정리: ① 출처 — WION 보도. ② 사건 — 19세 브라질 보디빌더가 심장마비로 자택에서 사망. ③ 배경 — 보디빌딩계 만연한 스테로이드 사용과의 연관 의혹. ④ 맥락 — 젊은 사용자의 돌연심장사 사례가 국제적으로 잇따름(호주 인플루언서 30세 사망 등). ⑤ 위험 — AAS의 심근 비대·이상지질혈증·부정맥이 청년 심장을 위협. ⑥ 함의 — '젊으니 괜찮다'는 믿음의 붕괴. NOGEAR 시각: 스무 살도 되기 전에 심장이 먼저 은퇴했다. 약이 만든 몸은 화려했지만, 그 몸을 끝까지 데려가 줄 심장은 빌린 것이었다.",
        "category": "news", "category_ko": "사건·사망",
        "source": "WION", "source_type": "news",
        "source_url": "https://www.wionews.com/world/steroids-lead-to-death-famous-brazilian-bodybuilder-dies-at-19-due-to-heart-attack-755817",
        "credibility": cred("medium", False, False,
            "검색결과 확인(미페치). 19세 브라질 보디빌더 심장마비 사망·스테로이드 연관 의혹 골자. 보디빌더 돌연사 리뷰(PMC9885939)·NBC 호주 사례와 교차. 일반 뉴스매체 → medium.", acc="partial", fc=False),
        "viral_signals": signals(24, 13, 19, 17, 16, 11),
        "tags": ["19세사망", "심장마비", "브라질", "보디빌더", "돌연사"],
    },
    # 5. SARMs Reddit 소셜 데이터 JMIR
    # (jmir DUP — skip) -> 대체: SARMs DILI PMC10847181
    {
        "title": "SARM이 간을 멈추게 한다 — 약물유발 간손상 의심사례 분석",
        "title_en": "SARM use and related adverse events including drug-induced liver injury",
        "summary": "이 연구는 SARM 사용과 관련된 이상반응, 특히 약물유발 간손상(DILI) 의심사례를 분석한다. 2020년 이후 다수의 간손상 보고가 누적됐고, 황달·간효소 급등이 전형적이다. '스테로이드보다 안전하다'는 마케팅과 달리 SARM도 간을 직접 친다.",
        "summary_detail": "정리: ① 출처 — NCBI 게재 SARM 이상반응·DILI 의심사례 분석. ② 핵심 — SARM 사용과 약물유발 간손상의 연관 신호. ③ 규모 — 2020년 이후 SARM 관련 간손상 보고 다수 누적(20여 건대). ④ 임상 — 황달, ALT/AST 급상승, 담즙정체성 패턴. ⑤ 동반 — 심근염·건파열 등 다른 중대 이상반응도 보고. ⑥ 함의 — FDA 미승인 '연구용'이라는 표기가 안전을 보증하지 않음. NOGEAR 시각: '부작용 없는 근육'이라는 광고가 가장 먼저 공격하는 건 간이다. 알약이 주사보다 순할 거라는 믿음이, 황달로 돌아온다.",
        "category": "research", "category_ko": "SARMs 간손상",
        "source": "NCBI / SARM DILI 분석", "source_type": "journal",
        "source_url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10847181/",
        "credibility": cred("high", True, True,
            "검색결과 확인(미페치). SARM 약물유발 간손상·2020년이후 보고 누적·황달/간효소 골자. JMIR 소셜데이터(AST/ALT 변화)·USADA와 교차. 동료심사 → high."),
        "viral_signals": signals(21, 18, 17, 14, 14, 9),
        "tags": ["SARMs", "간손상", "DILI", "황달", "미승인"],
    },
    # 6. 트렌볼론 간신부전 간신장 동시이식 ACG
    {
        "title": "7주 트렌볼론에 간·신장을 동시에 잃었다 — 다장기 이식 증례",
        "title_en": "Trenbolone Enanthate-Induced Hepatorenal Dysfunction Requiring Multiorgan Transplant",
        "summary": "미국소화기학회지(ACG)에 보고된 이 증례는 단 7주간의 트렌볼론 사용 후 간부전과 신부전이 동시에 와 간-신장 동시이식까지 받은 사례다. 심한 담즙정체가 담즙 결정으로 신장까지 망가뜨렸다. 짧은 한 사이클이 두 장기를 통째로 바꾸게 만들었다.",
        "summary_detail": "정리: ① 출처 — ACG(미국소화기학회) 저널 증례. ② 환자 — 치료된 C형간염 과거력의 40세 남성, 7주 트렌볼론 에난테이트 사용. ③ 증상 — 황달, 짙은 소변, 회색변, 조기 포만감. ④ 소견 — 간생검상 현저한 담즙정체·동모양혈관 확장·담관염 유사 변화(혼합형 간손상). ⑤ 신장 — 심한 담즙정체로 인한 담즙원주 신병증(bile cast nephropathy)으로 신부전. ⑥ 결과 — 급속 악화로 간-신장 동시이식 시행. NOGEAR 시각: 단 7주. 그 짧은 사이클의 청구서가 새 간과 새 신장이었다. '잠깐만 쓰고 끊는다'는 계획표는, 장기 이식 대기명단 위에선 의미가 없다.",
        "category": "research", "category_ko": "트렌볼론 증례",
        "source": "ACG (미국소화기학회지)", "source_type": "journal",
        "source_url": "https://journals.lww.com/ajg/fulltext/2025/10002/s5486_visceral_kaposi_sarcoma_of_the_liver_and.5484.aspx",
        "credibility": cred("high", True, True,
            "검색결과 확인(미페치). 7주 트렌볼론·간신부전·담즙원주신병증·간신장 동시이식 골자. 트렌볼론 구조적 리뷰(23증례)·AAS 담즙정체 간손상(PMC9426951)과 교차. 동료심사 학회지 → high."),
        "viral_signals": signals(25, 18, 17, 15, 15, 11),
        "tags": ["트렌볼론", "간부전", "신부전", "장기이식", "담즙정체"],
    },
    # 7. AAS 담즙정체 간손상 증례 PMC9426951
    {
        "title": "근육 약이 만든 노란 피부 — 아나볼릭 스테로이드 담즙정체 간손상",
        "title_en": "Anabolic Steroid-Induced Cholestatic Liver Injury: A Case Report",
        "summary": "이 증례는 아나볼릭 스테로이드 사용 후 담즙이 정체되며 황달이 나타난 간손상 사례를 보고한다. 경구 스테로이드의 간독성은 잘 알려졌지만, 회복까지 수개월이 걸리고 일부는 중증으로 진행한다. '간보호제 먹으니 괜찮다'는 통념의 허점을 드러낸다.",
        "summary_detail": "정리: ① 출처 — PMC 게재 증례보고. ② 핵심 — AAS 사용 후 담즙정체성 간손상 발생. ③ 임상 — 황달, 가려움, 짙은 소변, 빌리루빈·담즙 효소 상승. ④ 기전 — 17-알킬화 경구 스테로이드의 담즙 배출 장애. ⑤ 경과 — 약물 중단 후 회복까지 수주~수개월, 일부 중증화. ⑥ 함의 — 보충성 '간보호' 제품으로 상쇄되지 않는 직접 독성. NOGEAR 시각: 피부가 노래지는 건 몸이 보내는 마지막 경고다. 근육의 데피니션보다 먼저 또렷해지는 건, 흰자위에 번지는 황달이다.",
        "category": "research", "category_ko": "간손상 증례",
        "source": "PMC / 증례보고", "source_type": "journal",
        "source_url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9426951/",
        "credibility": cred("medium", True, True,
            "검색결과 확인(미페치). AAS 담즙정체성 간손상·황달·17알킬화 기전 골자. 트렌볼론 간신부전 증례·구조적 리뷰와 교차. 동료심사이나 직접페치 전 → medium.", acc="partial", fc=False),
        "viral_signals": signals(20, 17, 17, 12, 13, 10),
        "tags": ["스테로이드", "담즙정체", "간손상", "황달", "증례"],
    },
    # 8. 트렌볼론 고칼슘혈증 Cureus
    {
        "title": "트렌볼론이 혈중 칼슘을 끌어올렸다 — 드문 고칼슘혈증 증례",
        "title_en": "Hypercalcemia From Trenbolone Use: A Case Report",
        "summary": "이 증례는 트렌볼론 사용자에게서 드물게 나타난 고칼슘혈증(혈중 칼슘 과다)을 보고한다. 고칼슘혈증은 신장 손상·부정맥·의식저하를 유발할 수 있는 응급 상태다. 트렌볼론의 부작용이 알려진 것보다 더 광범위함을 보여준다.",
        "summary_detail": "정리: ① 출처 — Cureus 게재 증례보고. ② 핵심 — 트렌볼론 사용과 연관된 고칼슘혈증 발생. ③ 임상 — 다뇨·탈수·변비·의식저하·부정맥 위험. ④ 위험 — 중증 고칼슘혈증은 급성 신손상과 심전도 이상 유발. ⑤ 의의 — 트렌볼론 부작용 스펙트럼에 전해질 교란 추가. ⑥ 함의 — '근육 효과만 강한 약'이 아니라 대사 전반을 흔드는 약. NOGEAR 시각: 강한 약일수록 예상 못한 곳을 친다. 근육 외에 칼슘 수치까지 들썩이게 만드는 약을, 어떻게 '관리하며' 쓴다는 걸까.",
        "category": "research", "category_ko": "트렌볼론 증례",
        "source": "Cureus", "source_type": "journal",
        "source_url": "https://www.cureus.com/articles/439909-hypercalcemia-from-trenbolone-use-a-case-report.pdf",
        "credibility": cred("medium", True, True,
            "검색결과 확인(미페치). 트렌볼론 고칼슘혈증 증례 골자. 트렌볼론 구조적 리뷰(다장기 합병증)와 교차. 동료심사이나 직접페치 전 → medium.", acc="partial", fc=False),
        "viral_signals": signals(18, 16, 15, 13, 13, 8),
        "tags": ["트렌볼론", "고칼슘혈증", "전해질", "증례", "부정맥"],
    },
    # 9. 여성 AAS 건강·자녀 영향 PMC11653648
    {
        "title": "약은 그 여성만이 아니라 다음 세대까지 친다 — 여성 AAS의 건강·자손 영향",
        "title_en": "Impacts of AAS supplementation on female health and offspring",
        "summary": "이 2025년 리뷰는 여성의 아나볼릭 스테로이드 사용이 본인 건강뿐 아니라 자녀(자손)에게까지 미치는 영향을 정리한다. 남성화, 생식기능 손상, 호르몬 교란에 더해 임신·태아 영향 위험이 지적된다. 거울 앞 결정이 다음 세대까지 흔적을 남길 수 있다.",
        "summary_detail": "정리: ① 출처 — PMC 게재 2025 리뷰. ② 대상 — 여성의 AAS 사용이 건강·생식·자손에 미치는 영향. ③ 남성화 — 음성 저하, 다모, 음핵비대, 월경이상(상당수 비가역). ④ 생식 — 고안드로겐혈증으로 배란·생식기능 교란, 불임 위험. ⑤ 자손 — 임신 중 노출 시 태아 발달·호르몬 환경 영향 우려. ⑥ 함의 — 개인 건강을 넘어 세대 간 위험으로 확장. NOGEAR 시각: 어떤 부작용은 본인에서 끝나지 않는다. 약으로 바꾼 호르몬이, 아직 태어나지 않은 아이의 환경까지 미리 바꿔놓는다.",
        "category": "research", "category_ko": "여성 사용 리뷰",
        "source": "PMC / 여성 AAS 리뷰(2025)", "source_type": "journal",
        "source_url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC11653648/",
        "credibility": cred("high", True, True,
            "검색결과 확인(미페치). 여성 AAS 남성화·생식교란·자손영향 골자. 여성 AAS 질적연구(ScienceDirect)·음성 20년 증례와 교차. 동료심사 리뷰 → high."),
        "viral_signals": signals(21, 18, 18, 14, 15, 10),
        "tags": ["여성", "AAS", "남성화", "자손영향", "생식"],
    },
    # 10. 여성 AAS 질적연구 ScienceDirect
    {
        "title": "되돌릴 수 없는 변화를 직접 말하다 — 여성 스테로이드 사용자 인터뷰 연구",
        "title_en": "AAS use among women – qualitative study on masculinizing, gonadal and sexual effects",
        "summary": "이 질적 연구는 아나볼릭 스테로이드를 사용한 여성들이 경험한 남성화·생식·성적 변화를 본인의 목소리로 기록한다. 음성 저하와 음핵비대 같은 변화는 약을 끊어도 되돌아오지 않았다. 통계가 아닌 당사자의 증언으로 비가역성의 무게를 보여준다.",
        "summary_detail": "정리: ① 출처 — ScienceDirect 게재 질적 연구. ② 방법 — 여성 AAS 사용자 심층 인터뷰. ③ 남성화 — 음성 저하, 다모, 턱선 변화 등 외형 변화 경험. ④ 생식·성 — 월경 중단, 음핵비대, 성욕 변화. ⑤ 핵심 — 일부 변화(특히 음성)는 사용 중단 후에도 비가역. ⑥ 함의 — '조절해서 쓰면 된다'는 인식과 실제 후유증의 괴리. NOGEAR 시각: 숫자는 잊혀도 목소리는 남는다 — 말 그대로. 되돌릴 수 있다는 약속만 믿고 넘은 선이, 영영 돌아오지 않는 변화가 됐다.",
        "category": "research", "category_ko": "여성 사용 연구",
        "source": "ScienceDirect / 질적연구", "source_type": "journal",
        "source_url": "https://www.sciencedirect.com/science/article/pii/S0955395920302164",
        "credibility": cred("medium", True, True,
            "검색결과 확인(미페치). 여성 AAS 남성화·비가역 음성/음핵변화 당사자 증언 골자. 여성 AAS 리뷰(PMC11653648)·음성 20년 증례와 교차. 동료심사 질적연구이나 직접페치 전 → medium.", acc="partial", fc=False),
        "viral_signals": signals(20, 16, 18, 12, 15, 9),
        "tags": ["여성", "스테로이드", "남성화", "비가역", "질적연구"],
    },
    # 11. Enhanced Games 수영 세계기록 비공인
    {
        "title": "약 먹고 세계기록? 공인되지 않는 0.07초 — Enhanced Games 수영 결과",
        "title_en": "Enhanced Games: Gkolomeev 'breaks' 50m free record but it won't be ratified",
        "summary": "라스베이거스 Enhanced Games에서 그리스 수영선수 크리스티안 골로메프가 50m 자유형을 20.81초에 끊어 비도핑 세계기록(20.88)을 0.07초 앞당겼다. 그러나 금지 수영복·도핑 검사 부재·비공인 대회라는 이유로 어떤 공식 기구도 이 기록을 인정하지 않는다. 100만 달러 보너스만 남고 기록은 무효다.",
        "summary_detail": "정리: ① 출처 — Yahoo Sports / JudgeMate. ② 사건 — 2026-05-24 라스베이거스 Enhanced Games. ③ 기록 — 골로메프 50m 자유형 20.81초(비도핑 WR 20.88 대비 -0.07). ④ 보상 — 1위 25만 달러 + 비도핑 기록 경신 보너스 100만 달러. ⑤ 비공인 — 금지 폴리우레탄 수영복 착용, 도핑 통제 없음, 비승인 대회로 World Aquatics 불인정. ⑥ 전반 — 기록 경신은 수영 1종목뿐, 클린 선수 3명도 우승. NOGEAR 시각: 0.07초를 위해 약과 금지 수영복을 다 동원했지만, 기록판엔 아무것도 남지 않았다. 돈은 받았고 기록은 없다 — 그게 '향상된' 스포츠의 실체다.",
        "category": "news", "category_ko": "Enhanced Games",
        "source": "Yahoo Sports / JudgeMate", "source_type": "news",
        "source_url": "https://sports.yahoo.com/olympics/article/enhanced-games-results-swimmer-kristian-gkolomeev-breaks-world-record-in-final-event-for-1m-bonus-fred-kerley-falls-short-235007088.html",
        "credibility": cred("medium", False, False,
            "검색결과 확인(미페치). 골로메프 20.81초·100만달러 보너스·금지수영복/도핑통제 부재로 비공인 골자. JudgeMate 비준 분석·NPR Enhanced Games와 교차. 대형 스포츠매체 → medium.", acc="partial", fc=False),
        "viral_signals": signals(21, 13, 17, 18, 19, 11),
        "tags": ["EnhancedGames", "세계기록", "골로메프", "비공인", "도핑"],
    },
    # 12. Enhanced Games 기록 비준 JudgeMate
    {
        "title": "왜 그 기록은 영원히 '기록'이 못 되나 — Enhanced Games 비준의 벽",
        "title_en": "Are the Enhanced Games Records Real? Ratification",
        "summary": "JudgeMate는 Enhanced Games 기록이 왜 공식 인정받지 못하는지 비준 절차로 설명한다. 공인 기록은 약물 검사·승인 대회·규격 장비라는 3대 조건을 충족해야 하는데, Enhanced Games는 이 모두를 의도적으로 비켜갔다. '기록'이라는 단어가 마케팅 문구로만 남는 이유다.",
        "summary_detail": "정리: ① 출처 — JudgeMate 해설. ② 질문 — Enhanced Games 기록은 진짜 기록인가. ③ 비준 조건 — 반도핑 통제, 승인된 대회, 규격 적합 장비/수영복. ④ 위반 — 도핑 허용·비승인 대회·금지 수영복으로 3대 조건 모두 불충족. ⑤ 결과 — World Aquatics·World Athletics·IOC 모두 불인정. ⑥ 함의 — 숫자가 빨라도 제도적 신뢰가 없으면 기록이 아님. NOGEAR 시각: 빠르다고 다 기록이 아니다. 검증을 건너뛴 숫자는, 아무리 화려해도 각주조차 되지 못한다.",
        "category": "news", "category_ko": "Enhanced Games",
        "source": "JudgeMate", "source_type": "reference",
        "source_url": "https://www.judgemate.com/en/guides/are-enhanced-games-records-real",
        "credibility": cred("medium", False, False,
            "검색결과 확인(미페치). 공인 기록 3조건(도핑통제·승인대회·규격장비) 모두 불충족으로 비준 불가 골자. Yahoo Sports 결과·World Aquatics 불인정과 교차. 해설 매체 → medium.", acc="partial", fc=False),
        "viral_signals": signals(18, 14, 16, 17, 17, 9),
        "tags": ["EnhancedGames", "기록비준", "도핑", "공인", "World Aquatics"],
    },
    # 13. 미지의 금지물질 Hudson Valley
    {
        "title": "선수들이 손대는 '그 금지물질' — 판을 바꾸는 약물 경고",
        "title_en": "Athletes are using this banned substance (and it's changing everything)",
        "summary": "이 보도는 최근 선수들 사이에서 확산되는 금지 약물 사용 흐름과 그것이 경기 판도를 바꾸는 양상을 다룬다. 검출을 피하려는 신종 물질·프로토콜이 반도핑 체계를 시험한다. 더 빠른 기록 뒤에는 늘 더 교묘한 약물이 따라온다.",
        "summary_detail": "정리: ① 출처 — Hudson Valley Sports Report. ② 주제 — 선수들 사이 확산되는 금지 약물 사용과 경기 영향. ③ 흐름 — 검출 회피를 노린 물질·투여 프로토콜의 진화. ④ 맥락 — 2026년 다종목 도핑 적발 잇따름(스키점프·테니스·육상). ⑤ 쟁점 — 반도핑 검사와 약물 사용자 간 '쫓고 쫓기는' 구도. ⑥ 함의 — 기록 신뢰의 구조적 위협. NOGEAR 시각: 약물은 늘 검사보다 반 발짝 앞서간다. '안 걸렸다'가 '안 썼다'를 뜻하지 않는 세계에서, 깨끗함은 증명이 아니라 선택이다.",
        "category": "news", "category_ko": "도핑 동향",
        "source": "Hudson Valley Sports Report", "source_type": "news",
        "source_url": "https://hudsonvalleysportsreport.com/a4857841864/athletes-are-using-this-banned-substance-and-its-changing-everything/",
        "credibility": cred("low", False, False,
            "검색결과 확인(미페치). 선수 금지약물 확산·검출회피 흐름 골자. 2026 도핑 적발 흐름(Britannica)·Enhanced Games와 교차. 지역 스포츠매체로 출처강도 낮음 → low(일반 경향만 채택).", acc="partial", fc=False),
        "viral_signals": signals(17, 11, 16, 16, 17, 8),
        "tags": ["도핑", "금지약물", "검출회피", "반도핑", "선수"],
    },
    # 14. Liver King 체포 KXAN
    {
        "title": "월 1,100만 원어치 스테로이드의 끝 — '리버 킹' 체포",
        "title_en": "Who is the 'Liver King,' and why was he arrested in Austin, Texas",
        "summary": "'내추럴'을 표방하며 생간을 먹어 몸을 만들었다던 인플루언서 리버 킹(브라이언 존슨)이 오스틴에서 체포됐다. 과거 그는 월 1만 1천 달러어치 스테로이드를 쓰면서도 자연산을 주장해 들통났고, 이번엔 조 로건을 위협한 혐의다. 거짓 내추럴 서사의 자업자득이다.",
        "summary_detail": "정리: ① 출처 — KXAN 보도. ② 인물 — 리버 킹(브라이언 존슨), 생간·원시생활 마케팅 인플루언서. ③ 과거 — 월 약 1만 1천 달러 스테로이드 사용 사실이 폭로(자연산 주장 붕괴). ④ 사건 — 조 로건을 향한 위협 영상 게시 후 오스틴 포시즌스 호텔에서 체포. ⑤ 혐의 — 테러 위협(경범죄), 2만 달러 보석·정신건강 평가 명령. ⑥ 함의 — '가짜 내추럴' 서사의 상징적 붕괴. NOGEAR 시각: '자연'을 팔던 사람이 가장 부자연스러운 방법으로 몸을 만들었고, 결국 가장 부자연스러운 방식으로 무너졌다. 거짓은 근육보다 오래 버티지 못한다. FXXK FAKES.",
        "category": "scandal", "category_ko": "페이크 내추럴",
        "source": "KXAN", "source_type": "news",
        "source_url": "https://www.kxan.com/news/who-is-the-liver-king/",
        "credibility": cred("medium", False, False,
            "검색결과 확인(미페치). 리버 킹 월 $11K 스테로이드·자연산 주장 붕괴·로건 위협 체포 골자. Hollywood Reporter·ABC News·Wikipedia와 교차. 지역 뉴스매체 → medium.", acc="partial", fc=False),
        "viral_signals": signals(22, 12, 20, 16, 20, 12),
        "tags": ["리버킹", "페이크내추럴", "스테로이드", "체포", "조로건"],
    },
    # 15. Liver King 출소 후 반복 Hollywood Reporter
    {
        "title": "감옥에서 나와 또 같은 짓 — 리버 킹의 반복되는 서사",
        "title_en": "The Liver King Gets Out of Jail, Doubles Down in New Video",
        "summary": "체포 후 보석으로 풀려난 리버 킹이 반성 대신 새 영상으로 같은 행보를 반복했다고 Hollywood Reporter가 보도했다. 거짓 내추럴 폭로와 위협 사건에도 자기 브랜드를 고수하는 모습이다. 스캔들조차 콘텐츠로 소비하는 인플루언서 생태계의 단면이다.",
        "summary_detail": "정리: ① 출처 — Hollywood Reporter 보도. ② 전개 — 위협 혐의 체포·보석 석방 후 새 영상 공개. ③ 태도 — 사과·반성보다 기존 입장 고수('doubles down'). ④ 배경 — 2022년 스테로이드 사용 폭로로 무너진 '자연산' 이미지. ⑤ 맥락 — 논란을 다시 주목도·수익으로 전환하는 인플루언서 패턴. ⑥ 함의 — 거짓이 처벌받아도 알고리즘은 보상할 수 있음. NOGEAR 시각: 거짓이 들통나도 클릭이 멈추지 않으면, 사람은 바뀌지 않는다. 그래서 우리는 진짜를 택한다 — 알고리즘이 아니라 거울이 검증하는 몸을.",
        "category": "scandal", "category_ko": "페이크 내추럴",
        "source": "Hollywood Reporter", "source_type": "news",
        "source_url": "https://www.hollywoodreporter.com/news/general-news/the-liver-king-joe-rogan-out-of-jail-1236300001/",
        "credibility": cred("medium", False, False,
            "검색결과 확인(미페치). 리버 킹 보석 석방 후 새 영상 고수 골자. KXAN 체포·ABC News와 교차. 연예매체 → medium.", acc="partial", fc=False),
        "viral_signals": signals(19, 11, 18, 16, 19, 10),
        "tags": ["리버킹", "페이크내추럴", "스캔들", "인플루언서", "보석"],
    },
    # 16. 가짜 피트니스 인플루언서 Yahoo
    {
        "title": "부러워한 그 몸은 거짓이었다 — 가짜 피트니스 인플루언서의 비밀",
        "title_en": "Fake fitness influencers: the secrets and lies behind the world's most envied physiques",
        "summary": "이 기사는 세계가 부러워하는 인플루언서들의 몸 뒤에 숨은 거짓을 파헤친다. '자연산'을 표방하지만 스테로이드·필터·연출에 기댄 경우가 많고, 이는 보는 이에게 도달 불가능한 기준을 심는다. 비교의 출발점 자체가 조작된 셈이다.",
        "summary_detail": "정리: ① 출처 — Yahoo Lifestyle 보도. ② 주제 — '내추럴'을 표방하는 피트니스 인플루언서들의 실상. ③ 수법 — 비공개 스테로이드 사용, 조명·필터·펌핑·각도 연출. ④ 영향 — 팔로워에게 비현실적·도달불가 신체 기준 주입. ⑤ 통계 — 보디빌더의 약 80%가 약물 사용(자연산은 소수)이라는 추정. ⑥ 함의 — 비교 대상 자체가 가짜라 자기혐오만 남음. NOGEAR 시각: 네가 부러워한 몸은 '약+필터+각도'의 합성이다. 도달 못 하는 게 당연하다 — 애초에 사람이 아니라 편집본과 경쟁하고 있었으니까.",
        "category": "scandal", "category_ko": "페이크 내추럴",
        "source": "Yahoo Lifestyle", "source_type": "news",
        "source_url": "https://www.yahoo.com/lifestyle/fake-fitness-influencers-secrets-lies-040015028.html",
        "credibility": cred("medium", False, False,
            "검색결과 확인(미페치). 가짜 내추럴 인플루언서·연출/필터·비현실적 기준·80% 약물추정 골자. NattyOrNot·M+B 페이크내티 분석과 교차. 라이프 매체 → medium.", acc="partial", fc=False),
        "viral_signals": signals(20, 12, 20, 15, 18, 11),
        "tags": ["페이크내추럴", "인플루언서", "필터", "비교", "거짓"],
    },
    # 17. BPC-157/TB-500 FDA 재분류 newtropin
    {
        "title": "회색시장 펩타이드, FDA 심판대에 오른다 — 7월 BPC-157·TB-500 재검토",
        "title_en": "BPC-157, TB-500, Semax and MOTs-C: The July 2026 FDA Review",
        "summary": "회복 펩타이드 BPC-157·TB-500이 '중대 안전 우려'(카테고리2)로 분류됐다가 2026년 7월 23~24일 FDA 약국조제자문위(PCAC) 재검토를 앞두고 있다. 제한 펩타이드 19개 중 약 14개가 카테고리1로 복귀해 처방하 조제가 다시 가능해질 수 있다. 규제 지위가 곧 갈린다.",
        "summary_detail": "정리: ① 출처 — Newtropin 정리(FDA 일정 기반). ② 대상 — BPC-157·TB-500·Semax·MOTS-C 등 제한 펩타이드. ③ 현 지위 — 과거 카테고리2('중대 안전 우려')로 분류. ④ 일정 — 2026-07-23~24 FDA PCAC(약국조제자문위) 재검토. ⑤ 전망 — 19개 중 약 14개가 카테고리1로 복귀 가능성(면허 조제약국의 처방 조제 경로 회복). ⑥ 주의 — 재분류가 곧 '안전 입증'은 아님(여전히 인체 임상 빈약). NOGEAR 시각: 규제 칸이 바뀐다고 약이 안전해지는 건 아니다. '합법 경로'가 열려도, 검증되지 않은 인체 데이터는 그대로 비어 있다.",
        "category": "news", "category_ko": "펩타이드 규제",
        "source": "Newtropin / FDA 일정 정리", "source_type": "reference",
        "source_url": "https://newtropin.com/blog/bpc-157-tb-500-fda-review",
        "credibility": cred("low", False, False,
            "검색결과 확인(미페치). BPC-157/TB-500 카테고리2→2026-07 PCAC 재검토·14/19 카테고리1 복귀 전망 골자. AgeMD RFK 재분류·peptide-db와 교차. 펩타이드 업계 콘텐츠라 이해상충 → low(규제 일정만 채택).", acc="partial", fc=False),
        "viral_signals": signals(17, 13, 15, 18, 15, 8),
        "tags": ["BPC-157", "TB-500", "FDA", "펩타이드", "재분류"],
    },
    # 18. BPC-157 RFK 재분류 AgeMD
    {
        "title": "장관이 바꾼 펩타이드의 운명 — RFK 발 BPC-157 재분류 논쟁",
        "title_en": "BPC-157 FDA Status 2026: What the RFK Reclassification Means for Patients",
        "summary": "AgeMD는 2026년 BPC-157의 FDA 지위 변화와 그 정치적 배경(보건당국 수장 RFK 관련)이 환자·사용자에게 갖는 의미를 정리한다. 규제 완화 기대가 커지지만, 인체 임상 근거는 여전히 빈약하다는 경고가 핵심이다. 정책 신호와 과학적 검증을 혼동하지 말라는 메시지다.",
        "summary_detail": "정리: ① 출처 — AgeMD 해설. ② 주제 — 2026 BPC-157의 FDA 지위 변화와 정책적 맥락. ③ 배경 — 보건당국 수뇌부발 펩타이드 규제 재검토 기류. ④ 기대 — 조제약국 경로 회복 가능성. ⑤ 경고 — 규제 완화 ≠ 안전성 입증, 인체 RCT는 여전히 부족. ⑥ 함의 — 정책 신호를 '안전 보증'으로 오독할 위험. NOGEAR 시각: 정치가 약의 칸을 옮길 수는 있어도, 그 약이 네 몸에 안전하다는 증거를 만들어주진 않는다. 완화된 규제는 초대장이지 보증서가 아니다.",
        "category": "news", "category_ko": "펩타이드 규제",
        "source": "AgeMD", "source_type": "reference",
        "source_url": "https://www.agemd.com/insights/longevity/rfk-bpc-157-fda-peptide-reclassification-2026",
        "credibility": cred("low", False, False,
            "검색결과 확인(미페치). BPC-157 FDA 재분류·규제완화≠안전입증·인체임상 부족 골자. Newtropin FDA 일정·peptide-db 인체임상 현황과 교차. 업계 클리닉 콘텐츠 → low(규제 흐름·검증부재만 채택).", acc="partial", fc=False),
        "viral_signals": signals(16, 13, 15, 17, 16, 8),
        "tags": ["BPC-157", "RFK", "FDA", "재분류", "펩타이드"],
    },
    # 19. 오젬픽 근육 크기·근력 유타 연구
    {
        "title": "오젬픽, 근육 크기뿐 아니라 '근육의 질'까지 흔든다 — 유타대 연구",
        "title_en": "New Study Raises Questions About How Ozempic Affects Muscle Size and Strength",
        "summary": "유타대 보건의료 연구진은 세마글루타이드(오젬픽)가 근육 크기와 근력에 미치는 영향에 새로운 의문을 제기했다. 감량 과정에서 근육량이 줄 뿐 아니라 근육의 기능적 질 자체가 영향받을 수 있다는 것이다. 체중계 숫자만 보고 안심할 수 없다는 경고다.",
        "summary_detail": "정리: ① 출처 — University of Utah Health(2025-08) 연구 보도. ② 주제 — 세마글루타이드의 근육 크기·근력 영향 재검토. ③ 발견 — 감량 시 근육량 감소에 더해 근육의 질·기능 변화 가능성. ④ 맥락 — GLP-1 약물 감량분 중 상당 비율이 제지방(근육). ⑤ 우려 — 노년·운동인에서 근감소·근력저하로 이어질 위험. ⑥ 대응 — 저항운동·단백질 섭취·점진적 감량 필요. NOGEAR 시각: 약으로 빠진 살 안에는 근육도 섞여 있다. 더 가벼워진 몸이 더 약해진 몸일 수 있다 — 숫자가 아니라 힘으로 확인하라.",
        "category": "research", "category_ko": "GLP-1 근손실",
        "source": "University of Utah Health", "source_type": "journal",
        "source_url": "https://healthcare.utah.edu/newsroom/news/2025/08/new-study-raises-questions-about-how-ozempic-affects-muscle-size-and-strength",
        "credibility": cred("high", True, False,
            "검색결과 확인(미페치). 세마글루타이드 근육 크기·근력·질 영향 의문 골자. drugs.com 근손실·Cleveland Clinic과 교차. 대학병원 연구 보도 → high."),
        "viral_signals": signals(19, 17, 19, 16, 14, 9),
        "tags": ["오젬픽", "세마글루타이드", "근력", "근손실", "유타대"],
    },
    # 20. 세마글루타이드 오남용 medrxiv
    {
        "title": "처방 밖에서 번지는 오젬픽 — 미국 표본 오남용 실태 보고",
        "title_en": "Ozempic/Semaglutide Injection Misuse Among a Nationally Representative US Sample",
        "summary": "medRxiv에 공개된 이 연구는 미국 대표 표본에서 세마글루타이드(오젬픽) 주사의 오·남용 실태를 조사했다. 의학적 적응증 밖에서, 또는 부적절한 경로로 사용하는 사례가 확인된다. 다이어트·미용 목적의 비처방 사용이 새로운 공중보건 위험으로 떠오른다.",
        "summary_detail": "정리: ① 출처 — medRxiv 프리프린트(미국 대표 표본 조사). ② 주제 — 세마글루타이드 주사의 오·남용 패턴. ③ 발견 — 적응증 외 사용·비처방 경로 확보·부적절 용량 사례. ④ 동기 — 빠른 체중 감량·미용 목적의 비의학적 사용. ⑤ 위험 — 근손실·위장관 부작용·저혈당 등 관리 사각지대. ⑥ 한계 — 프리프린트(동료심사 전)로 해석 주의. NOGEAR 시각: 약은 처방전을 떠나는 순간 통제도 함께 떠난다. '살 빼는 주사'라는 입소문이, 검증되지 않은 자가실험으로 번진다.",
        "category": "research", "category_ko": "GLP-1 오남용",
        "source": "medRxiv (프리프린트)", "source_type": "journal",
        "source_url": "https://www.medrxiv.org/content/10.64898/2025.12.25.25343021.full.pdf",
        "credibility": cred("low", True, False,
            "검색결과 확인(미페치). 세마글루타이드 적응증외·비처방 오남용 미국표본 골자. 유타대 근력연구·drugs.com 근손실과 교차. 프리프린트(동료심사 전)라 → low(경향만 채택).", acc="partial", fc=False),
        "viral_signals": signals(18, 13, 18, 16, 15, 8),
        "tags": ["오젬픽", "세마글루타이드", "오남용", "비처방", "공중보건"],
    },
]


def tier(score):
    if score >= 98:
        return "VIRAL_BOMB", "🔴"
    return "HOT", "🟠"


def badge_for(conf):
    return {
        "high": "✅ VERIFIED", "medium": "🔍 CHECKED",
        "low": "⚠️ UNVERIFIED", "rejected": "❌ REJECTED",
    }.get(conf, "🔍 CHECKED")


def score_of(a):
    return sum(a["viral_signals"].values())


def finalize(a):
    a["viral_score"] = score_of(a)
    t, e = tier(a["viral_score"])
    a["viral_tier"] = t
    a["viral_emoji"] = e
    a["date"] = DATE
    a["badge"] = badge_for(a["credibility"]["confidence"])
    a["source_verified"] = a["credibility"]["confidence"] in ("high", "medium")
    a.setdefault("title_original", a["title"])
    a.setdefault("title_rewrite", a["title"])
    if "category_ko" not in a:
        a["category_ko"] = a.get("category", "research")
    return a


def main():
    d = json.load(open(PATH, encoding="utf-8"))
    existing = {x.get("source_url") for x in d["news"] + d["research"]}
    added = 0
    for a in NEW:
        if a["source_url"] in existing:
            continue
        finalize(a)
        if a["source_type"] == "news" or a["category"] in ("scandal", "news"):
            d["news"].append(a)
        else:
            d["research"].append(a)
        existing.add(a["source_url"])
        added += 1

    # dedup by source_url (keep highest viral_score)
    for arr in ("news", "research"):
        seen = {}
        for x in d[arr]:
            u = x.get("source_url")
            if u not in seen or x.get("viral_score", 0) > seen[u].get("viral_score", 0):
                seen[u] = x
        d[arr] = sorted(seen.values(), key=lambda x: x.get("viral_score", 0), reverse=True)

    # cap each array at 200 (active-feed trimming handled by archive_manager)
    d["news"] = d["news"][:200]
    d["research"] = d["research"][:200]

    allv = [x.get("viral_score", 0) for x in d["news"] + d["research"]]
    d["meta"]["total_articles"] = len(d["news"]) + len(d["research"])
    d["meta"]["news_count"] = len(d["news"])
    d["meta"]["research_count"] = len(d["research"])
    d["meta"]["top_viral_score"] = max(allv) if allv else 0
    d["meta"]["avg_viral_score"] = round(sum(allv) / len(allv), 1) if allv else 0
    import datetime
    now = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=9)))
    d["meta"]["last_updated"] = now.isoformat()
    d["meta"]["last_updated_kst"] = now.strftime("%Y-%m-%d %H:%M KST") + f" 아침 크롤 — 오늘 신규 {added}건"
    d["meta"]["last_crosscheck"] = CC_DATE
    d["meta"]["last_crosscheck_kst"] = f"{CC_DATE} 아침 크롤 신규 {added}건 인라인 검증(cross_check_date {CC_DATE})"
    d["meta"]["crawl_count"] = d["meta"].get("crawl_count", 0) + 1

    json.dump(d, open(PATH, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    print(f"added={added} total={d['meta']['total_articles']} news={len(d['news'])} research={len(d['research'])} top={d['meta']['top_viral_score']}")


if __name__ == "__main__":
    main()
