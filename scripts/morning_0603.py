#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
NOGEAR Magazine — 아침 크롤 2026-06-03
브랜드: FXXK FAKES. STAY NATURAL.
포커스: 스테로이드/AAS · 보디빌더 돌연사 · SARMs 간독성 · DNP 치명률 · 펩타이드 FDA규제 · 도핑 · 세마글루타이드 근손실
모든 콘텐츠 한국어. 출처 URL은 6/3 웹검색에서 확인한 실제 링크.
정직 원칙: 1차 웹검색 기반 신규 기사이므로 독립 교차검증 전까지 accuracy="unverified".
         별도 crosscheck 단계가 검증을 수행한다. confidence는 소스 등급에 따라 차등.
"""
import json
from datetime import datetime, timezone, timedelta
from pathlib import Path

KST = timezone(timedelta(hours=9))
NOW = datetime.now(KST)
TODAY = NOW.strftime("%Y.%m.%d")
BASE = Path(__file__).parent.parent / "content"
ARTICLES_FILE = BASE / "articles.json"

NEWS_TYPES = {"news", "magazine", "social"}  # → news[] 버킷


def sig(shock, sci, relat, recency, controversy, visual):
    return {
        "shock_factor": shock,
        "scientific_credibility": sci,
        "relatability": relat,
        "recency": recency,
        "controversy": controversy,
        "visual_potential": visual,
    }


def tier(score):
    if score >= 90:
        return "VIRAL_BOMB", "🔴"
    if score >= 85:
        return "HIGH_VIRAL", "🟠"
    return "TRENDING", "🟠"


def cred(peer, primary, conf, notes):
    """정직 모드: 신규 크롤은 미검증 상태로 저장. crosscheck 단계가 검증."""
    badge_map = {"high": "🔍 1차수집(미교차)", "medium": "🔍 미검증", "low": "⚠️ 저신뢰"}
    return {
        "peer_reviewed": peer,
        "primary_source": primary,
        "cross_checked": False,
        "cross_check_date": None,
        "url_alive": True,
        "cross_confirmed": False,
        "confidence": conf,
        "notes": notes,
        "fact_checked": False,
        "fact_check_date": None,
        "accuracy": "unverified",
    }, badge_map.get(conf, "🔍 미검증")


# (title, title_en, summary, summary_detail, category, category_ko, source, source_type,
#  source_url, signals, tags, peer, primary, conf, cred_notes, bucket)
A = [
 # ===== 스테로이드 건강영향 =====
 ("NIH 표준 교과서가 정리한 스테로이드 부작용 — 간·심장·정신까지 전신성",
  "Anabolic Steroids (StatPearls, NIH Bookshelf)",
  "미국 NIH의 임상 표준 레퍼런스 StatPearls는 아나볼릭 스테로이드(AAS)를 합성 테스토스테론 유도체로 정의하며, 안드로겐 수용체를 통해 단백질 합성·근비대를 일으키는 동시에 간 독성·이상지질혈증·고혈압·정신과적 변화를 부른다고 정리한다. 경구 17-알파-알킬화 제제는 특히 간 부담이 크다. 의학 교육의 1차 참고서가 '근육 약'이 아니라 전신 약물임을 못박는다.",
  "정리: ① StatPearls는 의대·전공의가 보는 NIH 표준 임상 레퍼런스다. ② AAS는 합성 테스토스테론 유도체로 안드로겐 수용체를 활성화해 단백질 합성·근비대를 촉진한다. ③ 경구용 17α-알킬화 스테로이드는 간에서 대사 저항성이 커 간세포 손상·담즙정체·간자반증 위험이 높다. ④ 지질대사 교란(HDL↓·LDL↑), 고혈압, 적혈구 증가로 심혈관 위험이 오른다. ⑤ 시상하부-뇌하수체-생식선 축 억제로 고환위축·불임. ⑥ 공격성·기분장애 등 신경정신과적 변화도 기록된다. NOGEAR 시각: 의학 교과서의 부작용 목록이 한 단락을 넘어간다는 사실 자체가 답이다.",
  "research", "스테로이드 연구", "StatPearls / NIH Bookshelf", "journal",
  "https://www.ncbi.nlm.nih.gov/books/NBK482418/",
  sig(18, 20, 17, 14, 14, 9),
  ["스테로이드", "간독성", "StatPearls", "NIH", "전신부작용"],
  True, True, "high", "NIH StatPearls 표준 임상 레퍼런스. AAS 기전·전신 부작용 정리는 표준 내분비학과 일치.", "research"),

 ("스테로이드도 '중독'이다 — NIH가 분류한 아나볼릭 스테로이드 사용장애",
  "Anabolic Steroid Use Disorder (StatPearls, NIH)",
  "NIH StatPearls는 아나볼릭 스테로이드 사용장애(AASUD)를 별도 임상 항목으로 다룬다. 사용자는 부작용을 알면서도 중단하지 못하고, 끊으면 우울·피로·성욕저하·근육감소 우려로 인한 금단 양상을 겪는다. 단순 기호가 아니라 행동·신경생물학적 의존이라는 의학적 규정이다.",
  "정리: ① AAS 사용은 DSM 물질사용장애 틀로 평가될 수 있는 의존 양상을 보인다. ② 내성·갈망·통제 실패·중단 시 금단(우울, 피로, 성욕저하, 신체이형 불안)이 핵심 특징. ③ '몸이 작아질 것'에 대한 공포(근이형증)가 지속 사용을 강화한다. ④ 보상 회로와 안드로겐 신호가 얽혀 신경생물학적 의존을 형성. ⑤ 치료는 중단 지원·심리 개입·내분비 회복 모니터링 병행. NOGEAR 시각: '언제든 끊을 수 있다'는 말이 가장 흔한 중독의 증상이다.",
  "research", "스테로이드 연구", "StatPearls / NIH Bookshelf", "journal",
  "https://www.ncbi.nlm.nih.gov/books/NBK538174/",
  sig(19, 18, 19, 13, 16, 9),
  ["스테로이드", "사용장애", "중독", "금단", "근이형증"],
  True, True, "high", "NIH StatPearls 별도 임상 항목. AAS 의존·금단 규정은 중독의학 표준과 일치.", "research"),

 ("스테로이드 사용자도 '치료 대상'으로 — 무작위 대조 해악감소 임상 등록",
  "Harm reduction RCT for people who use anabolic-androgenic steroids",
  "ClinicalTrials.gov에 등록된 무작위 대조시험(RCT)은 AAS 사용자를 대상으로 한 해악감소 개입의 효과를 검증한다. 처벌·금지 일변도에서 벗어나 검진·상담·모니터링으로 사망과 합병증을 줄이려는 흐름이다. 사용자가 일반 헬스인으로 확산됐다는 공중보건 인식이 임상시험으로 제도화되는 신호다.",
  "정리: ① ClinicalTrials.gov 등록 RCT(NCT07039539) — AAS 사용자 대상 해악감소 개입의 무작위 대조 검증. ② 배경 — 사용자가 엘리트 선수에서 일반 헬스인으로 확산. ③ 개입 — 정기 혈액·심장 검진, 상담, 모니터링 기반. ④ 목표 — 심혈관·내분비 합병증과 사망 감소. ⑤ 함의 — 음지의 사용자를 제도권 의료로 끌어오려는 시도. ⑥ 한계 — 해악감소는 안전을 보증하지 않으며 '안전한 스테로이드'를 의미하지 않는다. NOGEAR 시각: 의료가 RCT까지 설계한다는 건 그만큼 다치는 사람이 많다는 통계적 고백이다.",
  "research", "스테로이드 연구", "ClinicalTrials.gov NCT07039539", "journal",
  "https://clinicaltrials.gov/study/NCT07039539",
  sig(15, 18, 17, 17, 15, 8),
  ["스테로이드", "해악감소", "임상시험", "RCT", "공중보건"],
  True, True, "high", "ClinicalTrials.gov 1차 등록 임상시험. 해악감소 RCT 설계는 검색 결과와 일치.", "research"),

 ("'근육 약'의 진짜 청구서 — 회복 시설 정리한 스테로이드 장기 영향",
  "Anabolic Steroids: Effects, Risks, and Long-Term Impact",
  "중독 회복 전문 매체 Recovered.org는 아나볼릭 스테로이드를 근성장을 돕지만 심혈관 문제와 호르몬 불균형 등 심각한 위험을 동반하는 합성 테스토스테론 변형으로 정리한다. 효과의 이면에 장기 호르몬 교란이 자리한다는 점을 대중적 언어로 짚는다.",
  "정리: ① 정의 — AAS는 근비대를 돕는 합성 테스토스테론 변형 물질. ② 단기 효과 뒤에 심혈관 위험과 호르몬 불균형이 따라온다. ③ 장기 사용은 자체 테스토스테론 생산 억제로 이어진다. ④ 회복·재활 관점에서 의존·중단 어려움을 강조. ⑤ 비전문 매체이므로 1차 근거가 아닌 2차 정리로 취급해야 한다. NOGEAR 시각: 회복 시설이 별도 항목으로 다룬다는 건, 끊는 것 자체가 치료가 필요한 일이라는 뜻이다.",
  "research", "스테로이드 연구", "Recovered.org", "magazine",
  "https://recovered.org/stimulants/anabolic-steroids",
  sig(16, 12, 18, 13, 14, 9),
  ["스테로이드", "장기영향", "호르몬불균형", "회복", "재활"],
  False, False, "medium", "Recovered.org 회복 전문 2차 매체. 일반론은 표준과 일치하나 1차 근거 아님.", "research"),

 # ===== 보디빌더 돌연사 =====
 ("20세 보디빌더 돌연심장사 — 1995년 부검 보고서가 30년째 경고하는 것",
  "Sudden cardiac death in a 20-year-old bodybuilder using anabolic steroids",
  "PubMed에 색인된 고전적 증례는 아나볼릭 스테로이드를 사용한 20세 보디빌더의 돌연심장사를 부검으로 기록했다. 심근 비대와 관련 병변이 확인됐고, 이는 이후 수십 년간 'AAS-심장사' 인과 논의의 출발점이 됐다. 한 명의 부검이 한 세대의 경고가 됐다.",
  "정리: ① 20세 보디빌더가 AAS 사용 중 돌연심장사. ② 부검에서 심근 비대 등 구조 변화 확인. ③ 이 증례는 AAS와 돌연심장사의 인과를 다룬 초기 문헌으로 반복 인용된다. ④ 기전 — AAS에 의한 심근 비대·섬유화, 부정맥 기질 형성. ⑤ 30년 뒤 EHJ 대규모 코호트(45.3세·SCD 38%)가 이 단일 증례의 경고를 통계로 확증했다. NOGEAR 시각: 20세. 부검대 위에서 두꺼워진 심장은 거짓말을 하지 않는다.",
  "research", "보디빌더 돌연사", "PubMed (case report)", "journal",
  "https://pubmed.ncbi.nlm.nih.gov/7728810/",
  sig(23, 17, 17, 11, 17, 10),
  ["보디빌더", "돌연심장사", "부검", "심근비대", "20세"],
  True, True, "medium", "PubMed 색인 증례보고. 단일 케이스라 일반화엔 한계, 그러나 고전적 인용 문헌.", "research"),

 ("스테로이드 사용자 돌연심장사 — 문헌 리뷰가 모은 부검의 공통 소견",
  "Sudden Cardiac Death in Anabolic-Androgenic Steroid Users: A Literature Review",
  "PMC에 실린 문헌 리뷰는 AAS 사용자의 돌연심장사 증례들을 종합한다. 부검의 공통 소견은 심근 비대, 심장 확대, 일부 관상동맥질환과 섬유화다. 개별 사인 입증은 어렵지만, 반복되는 병리 패턴이 AAS-심장사 연결을 강하게 시사한다.",
  "정리: ① AAS 사용자 SCD 증례들을 묶은 문헌 리뷰. ② 공통 부검 소견 — 좌심실 비대, 심장 확대, 심근 섬유화, 일부 관상동맥질환. ③ 기전 — 심근 비대가 부정맥 기질을 만들고, 지질·혈전 악화가 허혈을 더한다. ④ 한계 — 증례 기반이라 개별 인과 입증은 어려움. ⑤ 그러나 반복되는 병리 패턴은 우연으로 설명되지 않는다. NOGEAR 시각: 한 건은 우연, 열 건은 패턴, 수십 건은 경고다.",
  "research", "보디빌더 돌연사", "PMC literature review", "journal",
  "https://pmc.ncbi.nlm.nih.gov/articles/PMC7694262/",
  sig(22, 18, 16, 13, 17, 10),
  ["보디빌더", "돌연심장사", "문헌리뷰", "심근섬유화", "부검소견"],
  True, False, "high", "PMC 게재 문헌 리뷰. 부검 공통 소견 종합은 AAS 심독성 문헌과 일치.", "research"),

 ("유럽심장학회 공식 보도자료: '남성 보디빌더, 돌연심장사 고위험 — 프로는 특히'",
  "Male bodybuilders face high risk of sudden cardiac death (ESC press)",
  "유럽심장학회(ESC)는 공식 보도자료를 통해 남성 보디빌더, 특히 프로 경쟁자들이 돌연심장사 고위험군이라고 발표했다. 121명 사망·평균 45.3세·SCD 38%·프로 5배 위험이라는 EHJ 연구가 근거다. 세계 최대 심장 학회가 공식 경보를 낸 것이다.",
  "정리: ① ESC 보도자료가 EHJ 코호트 연구를 대중에 발표. ② 핵심 — 남성 보디빌더는 돌연심장사 고위험, 프로는 아마추어 대비 5배+. ③ 평균 사망연령 45.3세. ④ 추정 요인 — AAS·PED, 극단 훈련, 급격한 감량·탈수. ⑤ 권고 — 심장 스크리닝과 위험 인지. NOGEAR 시각: 가장 보수적인 심장 학회가 보도자료까지 냈다. 이건 의견이 아니라 합의다.",
  "research", "보디빌더 돌연사", "European Society of Cardiology", "journal",
  "https://www.escardio.org/The-ESC/Press-Office/Press-releases/male-bodybuilders-face-high-risk-of-sudden-cardiac-death-especially-those-who-compete-professionally",
  sig(23, 18, 16, 16, 18, 10),
  ["보디빌더", "유럽심장학회", "돌연심장사", "프로5배", "심장스크리닝"],
  True, False, "high", "ESC 공식 보도자료, EHJ 원연구 기반. 121명·45.3세·프로5배 수치 검색결과와 일치.", "research"),

 ("'보디빌더들이 죽어간다' — 현대 보디빌딩·PED 사용 심층 조사",
  "Bodybuilders Are Dying: An Investigation Into Modern Bodybuilding, Health & PED Use",
  "보디빌딩 전문 매체 Generation Iron은 현대 보디빌딩의 사망과 PED(경기력 향상 약물) 사용을 심층 취재했다. 경쟁이 요구하는 극단적 약물·감량·체중조작이 젊은 선수들의 연쇄 사망과 무관하지 않다고 본다. 업계 내부 매체의 자기 고발이라는 점이 무게를 더한다.",
  "정리: ① Generation Iron(업계 전문 매체)의 PED·사망 심층 조사. ② 진단 — 극단적 약물 스택, 이뇨제·탈수, 과도한 감량이 결합. ③ 최근 젊은 선수 연쇄 사망과의 연관 제기. ④ 업계 내부에서조차 '뭔가 잘못됐다'는 공감대 형성. ⑤ 한계 — 저널리즘 기사로 통제된 연구는 아님. NOGEAR 시각: 약을 파는 문화의 한복판에서 나온 경고라 더 아프다.",
  "news", "사건·보디빌더", "Generation Iron", "magazine",
  "https://generationiron.com/bodybuilding-investigation-death-ped-use/",
  sig(22, 12, 18, 16, 18, 12),
  ["보디빌더", "PED", "심층취재", "연쇄사망", "업계고발"],
  False, False, "medium", "Generation Iron 전문 매체 탐사 기사. 정황 종합으로 통제 연구는 아님.", "news"),

 ("브라질 보디빌더 19세, 심장마비로 사망 — '스테로이드가 죽음을 부르나'",
  "Famous Brazilian bodybuilder dies at 19 due to heart attack",
  "WION 보도에 따르면 한 유명 브라질 보디빌더가 19세에 심장마비로 숨졌다. 보도는 스테로이드 사용 가능성과 죽음의 연관을 제기한다. 10대 보디빌더의 심장사라는 점에서 약물 조기 노출의 위험을 다시 부각한다.",
  "정리: ① 브라질 유명 보디빌더가 19세에 심장마비로 사망. ② 보도는 스테로이드·PED 사용 정황과 죽음을 연결. ③ 10대 후반의 심장사는 자연적 원인으로 설명하기 어렵다. ④ 미확정 — 공식 부검·사인 발표 대기. ⑤ 맥락 — 22세 갠리, 30세 티펫 등 젊은 보디빌더 연쇄 사망 흐름. NOGEAR 시각: 19살에 심장이 멈췄다. 트로피보다 빨리 도착한 청구서다.",
  "news", "사건·보디빌더", "WION News", "news",
  "https://www.wionews.com/world/steroids-lead-to-death-famous-brazilian-bodybuilder-dies-at-19-due-to-heart-attack-755817",
  sig(24, 10, 18, 16, 18, 12),
  ["보디빌더", "19세사망", "심장마비", "브라질", "스테로이드"],
  False, False, "low", "WION 보도. 사인-스테로이드 연관은 정황 추정, 공식 부검 미확정. 교차검증 필요.", "news"),

 # ===== SARMs =====
 ("SARMs, '안전한 스테로이드'라는 거짓말 — 약인성 간손상 의심사례 분석",
  "SARM use and adverse events including drug-induced liver injury (suspected cases)",
  "PMC에 실린 분석은 SARMs(선택적 안드로겐 수용체 조절제) 사용과 관련된 이상반응, 특히 약인성 간손상(DILI) 의심사례를 정리한다. 2020~2022년 SARMs 관련 DILI 증례가 급증했고, 횡문근융해·힘줄 파열 보고도 나왔다. '부작용 없는 스테로이드 대체재'라는 마케팅과 정반대다.",
  "정리: ① SARMs는 안드로겐 수용체에 선택적으로 작용하는 물질로 '부작용 적은 스테로이드 대체재'로 팔린다. ② 그러나 PMC 분석은 약인성 간손상(DILI) 의심사례를 다수 보고. ③ 2020~2022년 SARMs 관련 DILI 증례 급증. ④ 횡문근융해(rhabdomyolysis)·힘줄 파열 증례도 동반. ⑤ AST·ALT·CK 등 간·근육 지표 이상이 사용 전후로 관찰. ⑥ 대부분 미허가·미규제 온라인 유통. NOGEAR 시각: '선택적'이라는 단어가 안전을 보장하지 않는다. 간은 선택적으로 망가지지 않는다.",
  "research", "SARMs 연구", "PMC (DILI case analysis)", "journal",
  "https://pmc.ncbi.nlm.nih.gov/articles/PMC10847181/",
  sig(21, 18, 18, 15, 16, 10),
  ["SARMs", "간손상", "DILI", "횡문근융해", "힘줄파열"],
  True, False, "high", "PMC 게재 이상반응 분석. SARMs DILI 급증·횡문근융해는 검색 결과와 일치.", "research"),

 ("건강한 성인 대상 SARMs 안전성 체계적 문헌고찰 — '안전하다는 근거가 없다'",
  "Systematic Review of Safety of SARMs in Healthy Adults",
  "PMC 게재 체계적 문헌고찰은 건강한 성인에서 SARMs의 안전성을 평가했다. 결론은 명확하다 — 안전성을 입증할 임상 근거가 부족하고, 테스토스테론 억제·지질 악화·간효소 상승이 관찰된다. 레크리에이션 사용자에게 '미지의 위험'을 경고한다.",
  "정리: ① 건강 성인 대상 SARMs 임상연구를 체계적으로 종합. ② 핵심 결론 — 안전성을 보증할 충분한 근거가 없다. ③ 관찰된 영향 — 총 테스토스테론 억제, HDL 저하, 간효소 상승. ④ 장기 영향·약물상호작용 데이터는 거의 부재. ⑤ 함의 — 레크리에이션 사용은 사실상 '인체 실험'. NOGEAR 시각: '안전하다는 증거가 없다'와 '위험하다는 증거가 없다'는 전혀 다른 말이다. 후자에 베팅하는 게 도박이다.",
  "research", "SARMs 연구", "PMC systematic review", "journal",
  "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10204391/",
  sig(20, 19, 17, 14, 15, 9),
  ["SARMs", "체계적고찰", "안전성근거부족", "테스토스테론억제", "지질악화"],
  True, False, "high", "PMC 게재 체계적 문헌고찰. 안전성 근거 부족 결론은 검색 결과와 일치.", "research"),

 ("미국 국립도서관 LiverTox: SARMs는 '간독성 약물' 목록에 올랐다",
  "Selective Androgen Receptor Modulators — LiverTox (NCBI)",
  "NIH의 약물 간독성 데이터베이스 LiverTox는 SARMs를 독립 항목으로 등재했다. 임상적으로 뚜렷한 간손상(담즙정체형 간염 포함)을 유발할 수 있다는 의미다. 정부 차원의 간독성 레퍼런스에 이름을 올린 것 자체가 위험의 공식 인정이다.",
  "정리: ① LiverTox는 NIH가 운영하는 약물 유발 간손상 표준 데이터베이스. ② SARMs가 별도 항목으로 등재. ③ 보고된 양상 — 담즙정체형/혼합형 간손상, 황달, 간효소 상승. ④ 다수가 미허가 보충제로 유통되어 성분·용량 불확실. ⑤ 의미 — 정부 레퍼런스가 SARMs 간독성을 공식 기록. NOGEAR 시각: LiverTox에 이름이 올랐다는 건, 누군가의 간이 이미 그 대가를 치렀다는 뜻이다.",
  "research", "SARMs 연구", "LiverTox / NCBI Bookshelf", "journal",
  "https://www.ncbi.nlm.nih.gov/books/NBK619971/",
  sig(20, 19, 16, 13, 15, 9),
  ["SARMs", "LiverTox", "간독성", "담즙정체", "NIH"],
  True, True, "high", "NIH LiverTox 표준 데이터베이스 등재. SARMs 간손상 등재는 검색 결과와 일치.", "research"),

 ("약사들이 경고하는 SARMs 레크리에이션 남용 — 처방 없는 안드로겐의 함정",
  "Recreational Use of Selective Androgen Receptor Modulators (U.S. Pharmacist)",
  "U.S. Pharmacist 기고는 SARMs의 레크리에이션 남용을 약학적 관점에서 경고한다. 미허가·미규제 상태로 온라인 유통되며, 표시 성분과 실제 성분이 다른 경우가 흔하다. 약사가 일선에서 마주하는 현실을 통해 '셀프 처방'의 위험을 짚는다.",
  "정리: ① 약학 전문지가 SARMs 레크리에이션 남용을 다룸. ② SARMs는 어느 나라에서도 일반 의약품으로 승인되지 않았다. ③ 온라인 제품은 라벨-실제 성분 불일치가 빈번. ④ 테스토스테론 억제·간효소 상승 등 부작용 모니터링 필요. ⑤ 약사 관점의 환자 교육·해악감소 강조. NOGEAR 시각: 약국에서도 못 파는 걸 인터넷에서 산다. 그 차이가 곧 위험의 크기다.",
  "research", "SARMs 연구", "U.S. Pharmacist", "magazine",
  "https://www.uspharmacist.com/article/recreational-use-of-selective-androgen-receptor-modulators",
  sig(17, 16, 17, 13, 14, 8),
  ["SARMs", "약사경고", "미허가", "성분불일치", "셀프처방"],
  False, False, "medium", "U.S. Pharmacist 약학 전문지 기고. 임상 일반론은 표준과 일치, 2차 자료.", "research"),

 ("USADA: SARMs는 '금지 약물 — 아나볼릭 계열'로 분류된다",
  "Selective Androgen Receptor Modulators (USADA)",
  "미국반도핑기구(USADA)는 SARMs를 상시 금지 약물(아나볼릭 계열)로 분류한다. 경기 내외를 막론하고 금지되며, '연구용'이라는 표기로 유통돼도 선수에게는 도핑 위반이다. 반도핑 당국의 분류는 SARMs가 본질적으로 아나볼릭 약물임을 확인한다.",
  "정리: ① USADA는 SARMs를 WADA 금지목록의 아나볼릭 계열로 분류. ② 경기 내·외 상시 금지. ③ '연구 화학물질(research chemical)' 표기는 규제 회피용일 뿐 도핑 면죄부가 아니다. ④ 보충제 오염으로 의도치 않은 양성도 보고된다. ⑤ 의미 — 반도핑 당국이 SARMs를 스테로이드와 동급으로 본다. NOGEAR 시각: '연구용'이라는 라벨은 면책이 아니라 책임 회피의 다른 이름이다.",
  "research", "SARMs 연구", "USADA", "magazine",
  "https://www.usada.org/spirit-of-sport/selective-androgen-receptor-modulators-sarms-prohibited-class-anabolic-agents/",
  sig(17, 16, 16, 13, 16, 8),
  ["SARMs", "USADA", "금지약물", "도핑", "연구용라벨"],
  False, True, "medium", "USADA 반도핑 당국 공식 분류. 금지 분류 사실은 신뢰, 의학적 위해는 별도.", "research"),

 ("'벌크업 SARMs 추천'의 함정 — 안전성 미입증 물질의 마케팅",
  "Best SARMs For Bulking 2025 (vendor guide) — 비판적 검토",
  "벌크업용 SARMs를 추천하는 상업 가이드들이 2025~2026년에도 검색 상위를 점한다. 그러나 임상적으로 안전성이 입증된 SARM은 없으며, 이런 가이드는 부작용을 축소하고 효과를 과장한다. NOGEAR는 이 마케팅 구조 자체를 경고 대상으로 다룬다.",
  "정리: ① '최고의 벌크업 SARMs'류 가이드가 검색 상위에 노출된다. ② 공통 패턴 — 효과 과장, 간·호르몬 부작용 축소, 출처 불명 '후기'. ③ 실제로는 어떤 SARM도 인체 안전성이 임상 입증되지 않았다. ④ 다수가 제품 판매·제휴 링크와 연결된 상업 콘텐츠. ⑤ 소비자는 '정보'로 오인하기 쉽다. NOGEAR 시각: 추천 글의 진짜 상품은 SARMs가 아니라 당신의 신뢰다. 그걸 팔지 마라.",
  "news", "업계 비판", "Fit Science (vendor) — 비판", "magazine",
  "https://fitscience.co/sarms/best-sarms-for-bulking-2025-expert-guide-real-results/",
  sig(16, 10, 17, 14, 17, 9),
  ["SARMs", "마케팅", "벌크업", "상업가이드", "효과과장"],
  False, False, "low", "벤더성 상업 가이드를 비판적으로 인용. 추천 내용은 의학적 근거 아님(NOGEAR 비판 대상).", "news"),

 # ===== DNP =====
 ("DNP, '치명률 12%'의 다이어트 약 — 외상 후 사망 증례가 드러낸 위험",
  "2,4-Dinitrophenol: 'diet' drug death following major trauma",
  "PMC 증례보고는 DNP(2,4-디니트로페놀)를 복용하던 사람이 외상 후 사망한 사례를 다룬다. DNP는 미토콘드리아 산화적 인산화를 '탈공역'시켜 에너지를 ATP가 아닌 열로 방출하게 만들어 급격한 체온 상승(최대 44℃)과 사망을 부른다. 2010~2020년 보고된 중독의 치명률은 약 12%였다.",
  "정리: ① DNP는 20세기 초 다이어트 약으로 쓰였다 금지된 산업용 화학물질. ② 기전 — 미토콘드리아 산화적 인산화 탈공역으로 에너지를 열로 방출, ATP 생성 차단. ③ 결과 — 통제 불가능한 고열(최대 44℃), 탈수, 빈맥, 혼수, 사망. ④ 2010~2020년 전 세계 최소 50명 사망, 중독 치명률 약 12%. ⑤ 치료법 없음 — 과량 복용 시 효과적 해독제가 없다. ⑥ '권장 용량'에서도 치명적 부작용 보고. NOGEAR 시각: 몸을 '난로'로 만드는 약이다. 지방과 함께 사람도 태운다.",
  "research", "DNP 위험", "PMC case report", "journal",
  "https://pmc.ncbi.nlm.nih.gov/articles/PMC8131886/",
  sig(25, 18, 16, 13, 18, 11),
  ["DNP", "다이어트약", "고열사망", "미토콘드리아", "치명률12%"],
  True, True, "high", "PMC 증례보고. DNP 탈공역 기전·치명률·해독제 부재는 독성학 표준과 일치.", "research"),

 ("응급의학 증례: DNP 다이어트 약이 부른 '고열사' — 체온 41℃를 넘다",
  "Case Report: A Hyperthermic Death from the Diet Pill DNP (ACEP Now)",
  "미국응급의사회(ACEP) 매체 ACEP Now는 DNP 복용 후 고열로 사망한 응급 증례를 소개한다. 환자는 통제되지 않는 고체온·빈맥·발한으로 응급실에 왔고, 표준 해열·냉각으로도 막지 못했다. 응급 현장에서 DNP가 '해독제 없는 응급'임을 보여준다.",
  "정리: ① ACEP Now가 DNP 고열사 응급 증례 보고. ② 임상 양상 — 고열, 발한, 빈맥, 초조, 홍조, 급속 악화. ③ 기전 — 미토콘드리아 탈공역으로 발생한 열은 해열제로 잡히지 않는다. ④ 적극적 냉각·수액에도 사망에 이를 수 있다. ⑤ 응급의가 'DNP 의심 시 즉시 공격적 냉각'을 강조. NOGEAR 시각: 해독제가 없다는 말은, 일단 삼키면 의사도 손쓸 수 없다는 뜻이다.",
  "research", "DNP 위험", "ACEP Now", "magazine",
  "https://www.acepnow.com/article/case-report-a-hyperthermic-death-from-the-diet-pill-dnp/",
  sig(24, 16, 16, 13, 17, 11),
  ["DNP", "고열사", "응급의학", "ACEP", "냉각치료"],
  False, False, "medium", "ACEP Now 응급의학 매체 증례. 임상 양상·기전 정확, 2차 매체.", "research"),

 ("약사 저널이 경고하는 DNP — '약사가 알아야 할 가장 위험한 다이어트 약'",
  "DNP: the dangerous diet pill pharmacists should know about",
  "Pharmaceutical Journal은 DNP를 '약사가 반드시 알아야 할 가장 위험한 다이어트 약'으로 다룬다. 온라인에서 체중감량 보충제로 팔리지만, 안전 용량이 존재하지 않고 피부·호흡 노출만으로도 독성이 나타난다. 보디빌더와 섭식장애 환자가 주 사용층이다.",
  "정리: ① Pharmaceutical Journal이 DNP의 약학적 위험을 정리. ② 온라인 체중감량 보충제로 위장 판매. ③ 안전 용량 없음 — 약 4.3mg/kg(체중 180lb당 약 350mg)로도 치사 가능. ④ 경구뿐 아니라 피부·호흡 노출도 독성. ⑤ 주 사용층 — 보디빌더, 섭식장애·신체이형 환자. NOGEAR 시각: '소량은 괜찮다'는 안전선이 아예 없는 약이다. 안전한 용량 = 0.",
  "research", "DNP 위험", "Pharmaceutical Journal", "magazine",
  "https://pharmaceutical-journal.com/article/feature/dnp-the-dangerous-diet-pill-pharmacists-should-know-about",
  sig(22, 16, 16, 12, 16, 9),
  ["DNP", "약사경고", "안전용량없음", "피부노출", "섭식장애"],
  False, False, "medium", "Pharmaceutical Journal 약학 전문지. 치사용량·노출 경로 정보는 표준과 일치.", "research"),

 ("영국 보건안전청 'Deadly DNP' — 정부가 직접 낸 사망 경고",
  "Deadly DNP — UK Health Security Agency",
  "영국 보건안전청(UKHSA)은 'Deadly DNP'라는 제목으로 직접 공개 경고를 냈다. DNP가 치명적이며 해독제가 없다는 점, 특히 다이어트·보디빌딩 목적 사용자에게 위험하다는 점을 정부 차원에서 명시한다. 공중보건 당국의 직접 경고는 드물다.",
  "정리: ① UKHSA(영국 보건안전청) 공식 블로그 경고. ② 메시지 — DNP는 치명적이며 효과적 해독제가 없다. ③ 온라인 구매·다이어트 목적 사용의 위험 강조. ④ 고열·다발 장기부전으로 사망 가능. ⑤ 의미 — 정부 보건당국이 개별 물질을 지목해 경고하는 이례적 사례. NOGEAR 시각: 국가가 이름을 콕 집어 '치명적'이라 부를 때는, 이미 시신이 쌓였다는 뜻이다.",
  "research", "DNP 위험", "UK Health Security Agency", "magazine",
  "https://ukhsa.blog.gov.uk/2018/08/13/deadly-dnp/",
  sig(21, 15, 16, 11, 16, 9),
  ["DNP", "UKHSA", "정부경고", "해독제없음", "공중보건"],
  False, True, "medium", "UKHSA 정부 보건당국 공식 경고. 사실 신뢰도 높음, 2018년 게시(최신성 낮음).", "research"),

 # ===== 도핑 / 가짜 내추럴 =====
 ("올림픽 도핑 사건사 — 100년 약물 적발의 역사가 말하는 것",
  "Sports and Drugs — Doping Cases at the Olympics (Britannica)",
  "Britannica ProCon은 올림픽 역사상 주요 도핑 사건을 정리한다. 약물은 스포츠의 그림자처럼 100년 넘게 따라다녔고, 적발 기술이 발전할수록 더 정교한 회피가 등장했다. 도핑이 예외가 아니라 구조적 문제임을 역사가 증언한다.",
  "정리: ① Britannica가 올림픽 도핑 사건을 연대기로 정리. ② 도핑은 근대 스포츠 초기부터 존재한 만성 문제. ③ 검출 기술 발전 ↔ 회피 기술 진화의 끝없는 군비경쟁. ④ 사후 재검사로 메달 박탈되는 사례 반복(리우 올림픽 등). ⑤ 함의 — '깨끗한 경기'는 끊임없는 감시 없이는 유지되지 않는다. NOGEAR 시각: 100년의 적발 역사는, 약을 이기는 유일한 길이 '안 쓰는 것'뿐임을 증명한다.",
  "research", "도핑 스캔들", "Britannica ProCon", "magazine",
  "https://www.britannica.com/procon/sports-and-drugs-debate/Doping-Cases-at-the-Olympics",
  sig(16, 14, 16, 12, 17, 9),
  ["도핑", "올림픽", "약물역사", "메달박탈", "군비경쟁"],
  False, False, "medium", "Britannica 백과 정리. 역사적 사실 종합, 1차 연구 아님.", "research"),

 ("미국 육상 도핑 적발 명단 — 실명 공개되는 'PED의 대가'",
  "USA Track & Field — Doping Suspensions and Public Warnings",
  "미국육상연맹(USATF)은 도핑 적발 선수의 자격정지·실격·공개 경고를 명단으로 공시한다. 약물 사용은 기록 말소를 넘어 실명 공개라는 대가를 동반한다. '잠깐의 기록'과 '영구히 남는 낙인'을 대비시키는 공적 기록이다.",
  "정리: ① USATF가 도핑 적발 선수를 실명·사유와 함께 공시. ② 처분 — 자격정지, 기록 실격, 공개 경고. ③ 적발 약물에는 아나볼릭 제제·SARMs·자극제 등이 포함. ④ 의미 — 도핑의 대가는 메달 박탈만이 아니라 공적 낙인. ⑤ 투명 공개는 억제와 경고의 도구. NOGEAR 시각: 기록은 지워지고 이름은 남는다. 약이 주는 건 잠깐, 빼앗는 건 평생이다.",
  "research", "도핑 스캔들", "USA Track & Field", "magazine",
  "https://www.usatf.org/record-views/doping-suspensions-disqualifications-and-public-wa",
  sig(16, 13, 16, 14, 17, 8),
  ["도핑", "USATF", "자격정지", "실명공개", "기록말소"],
  False, True, "medium", "USATF 공식 적발 공시. 처분 사실 신뢰, 개별 사례는 별도 확인 필요.", "research"),

 ("'가짜 내추럴' 해부 — 약 쓰면서 자연이라 속이는 인플루언서들",
  "Top Fake Natural Bodybuilders (NattyOrNot) — 현상 분석",
  "보디빌딩 비평 매체 NattyOrNot은 '내추럴'을 표방하면서 실제로는 약물을 쓰는 인플루언서 현상을 분석한다. 비현실적 근육·혈관·건조도를 '자연산'으로 포장하는 콘텐츠가 일반인에게 왜곡된 기준을 심는다. NOGEAR가 가장 경계하는 'STAY NATURAL의 적'이다.",
  "정리: ① '가짜 내추럴(fake natty)' = 약물을 쓰면서 자연을 주장하는 사용자. ② 단서 — 비현실적 제지방·근육량, 급격한 변화, 혈관·건조도. ③ 문제 — 팔로워가 '약 없이도 가능'으로 오인해 무리·약물 진입. ④ 광고·코칭 판매와 결합된 상업 구조. ⑤ 한계 — 개별 지목은 추정이며 증명 어려움. NOGEAR 시각: 가장 위험한 거짓말은 '나는 자연산'이다. 그 한마디가 수천 명을 약으로 민다.",
  "news", "가짜 내추럴", "NattyOrNot.com", "magazine",
  "https://nattyornot.com/top-10-fake-natural-bodybuilders-youtube/",
  sig(20, 10, 19, 13, 19, 11),
  ["가짜내추럴", "fakenatty", "인플루언서", "왜곡된기준", "STAYNATURAL"],
  False, False, "low", "NattyOrNot 비평 매체. 개별 지목은 의견·추정이며 증명 불가, 현상 분석으로 인용.", "news"),

 # ===== 펩타이드 / FDA 규제 =====
 ("STAT 단독: BPC-157 '큰 주장, 빈약한 근거' — 펩타이드 열풍의 민낯",
  "BPC-157: The peptide with big claims and scant evidence (STAT)",
  "의학 전문 매체 STAT은 2026년 2월 보도에서 BPC-157 펩타이드가 회복·재생을 내세우지만 인체 임상 근거가 빈약하다고 짚었다. 대부분 동물·전임상 데이터이며, 안전성·규제 지위도 불확실하다. 'SNS가 만든 기대'와 '실제 과학' 사이의 간극을 드러낸다.",
  "정리: ① STAT(권위 있는 의학 저널리즘)이 BPC-157을 비판적 검토. ② 마케팅 주장 — 힘줄·근육·장 회복, 항염. ③ 실제 — 근거 대부분이 동물·전임상, 통제된 인체 임상 거의 없음. ④ 안전성·장기 영향 데이터 부재. ⑤ 규제 지위 불확실(미허가 회색지대 유통). NOGEAR 시각: '큰 주장, 빈약한 근거'는 보충제 업계의 사훈 같다. 쥐 실험을 사람 몸에 베팅하지 마라.",
  "research", "펩타이드 규제", "STAT News", "magazine",
  "https://www.statnews.com/2026/02/03/bpc-157-peptide-science-safety-regulatory-questions/",
  sig(20, 16, 18, 17, 16, 10),
  ["BPC157", "펩타이드", "근거빈약", "전임상", "STAT"],
  False, False, "high", "STAT 의학 전문 저널리즘 2026-02 보도. 인체 근거 부족·규제 불확실 지적 정확.", "research"),

 ("FDA, 펩타이드 12종 지위 변경 — BPC-157·TB-500 규제 분수령",
  "FDA Announces Change in Status of 12 Peptides",
  "FDA가 BPC-157·TB-500을 포함한 12종 펩타이드의 규제 지위 변경을 발표했다. 2026년 7월 약국 조제 자문위(Pharmacy Compounding Advisory Committee)에서 503A 벌크 목록 포함 여부를 논의한다. 그동안 회색지대에 있던 펩타이드가 규제의 시험대에 오른 것이다.",
  "정리: ① FDA가 BPC-157·TB-500 등 12종 펩타이드의 규제 지위를 재검토. ② 2026년 7월 약국 조제 자문위에서 503A 벌크 목록 포함 여부 논의 예정. ③ 그간 펩타이드는 '연구용·조제용' 회색지대로 유통. ④ 규제 명확화는 합법 조제와 불법 유통의 경계를 가른다. ⑤ 함의 — '합법처럼 보였던' 시장이 재편될 수 있다. NOGEAR 시각: 규제 당국이 손대기 시작했다는 건, 시장이 통제 불능으로 커졌다는 신호다.",
  "research", "펩타이드 규제", "FDA / SSRP Institute", "magazine",
  "https://ssrpinstitute.org/news/fda-announces-change-in-status-of-12-peptides/",
  sig(18, 15, 16, 18, 16, 9),
  ["펩타이드", "FDA규제", "BPC157", "TB500", "503A"],
  False, False, "medium", "SSRP Institute 정리(FDA 발표 기반). FDA 7월 자문위 일정은 FDA 공식 페이지와 교차 필요.", "research"),

 ("FDA 약국조제 자문위 7월 개최 — BPC-157·TB-500 운명 결정",
  "July 2026 Meeting of the Pharmacy Compounding Advisory Committee (FDA)",
  "FDA는 2026년 7월 23~24일 약국 조제 자문위원회를 열어 BPC-157·TB-500 관련 벌크 의약품 물질의 503A 목록 포함 여부를 논의한다. 이 결정은 펩타이드의 합법 조제 가능성을 가른다. FDA 1차 공지로, 규제 향방의 직접 근거다.",
  "정리: ① FDA 공식 일정 — 2026.7.23~24 약국 조제 자문위(PCAC). ② 안건 — BPC-157·TB-500 벌크 물질의 503A 목록 포함 검토. ③ 503A 포함 시 약국 조제 합법화 경로, 배제 시 사실상 차단. ④ FDA가 4월 일부 펩타이드를 '안전 우려 카테고리2'에서 제외한 데 이은 후속. ⑤ 의미 — 펩타이드 규제의 분수령. NOGEAR 시각: 자문위 회의실에서 결판난다. 그때까지 'FDA가 곧 승인'이라는 마케팅을 믿지 마라.",
  "research", "펩타이드 규제", "FDA (official)", "journal",
  "https://www.fda.gov/advisory-committees/advisory-committee-calendar/july-23-24-2026-meeting-pharmacy-compounding-advisory-committee-07232026",
  sig(17, 16, 15, 18, 15, 8),
  ["펩타이드", "FDA", "조제자문위", "503A", "BPC157"],
  False, True, "high", "FDA 공식 자문위 일정 페이지. 1차 출처, 일정·안건 신뢰도 높음.", "research"),

 ("BPC-157 학술 논평: '혈관신생·산화질소' 양날의 칼",
  "BPC-157 Therapy: angiogenesis and nitric oxide — academic comment (Pharmaceuticals)",
  "PMC에 실린 학술 논평은 BPC-157이 혈관신생(VEGFR2)과 산화질소(NO) 경로를 동시에 조절한다고 정리하면서, 이 작용이 보호적일 수도 손상·세포독성으로 작용할 수도 있는 양날의 칼임을 지적한다. '만능 회복 펩타이드'라는 단순 서사를 학계가 견제한다.",
  "정리: ① Pharmaceuticals 저널 논평(PMC 게재). ② BPC-157은 VEGFR2 매개 혈관신생과 NO 경로를 동시 조절. ③ 이 작용은 조직 보호에 기여할 수도, 반대로 세포독성·손상으로 작용할 수도 있다. ④ 즉 '무조건 좋은 회복 물질'이 아니라 맥락 의존적. ⑤ 인체 안전성·용량 데이터는 여전히 부족. NOGEAR 시각: 같은 칼이 수술도 하고 상처도 낸다. 기전을 모르고 찌르는 게 가장 위험하다.",
  "research", "펩타이드 규제", "Pharmaceuticals / PMC", "journal",
  "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12567428/",
  sig(17, 18, 15, 14, 15, 9),
  ["BPC157", "혈관신생", "산화질소", "양날의칼", "학술논평"],
  True, False, "high", "PMC 게재 학술 논평(Pharmaceuticals). 기전 양면성 지적은 약리학적으로 타당.", "research"),

 # ===== 세마글루타이드 / 오젬픽 근손실 =====
 ("클리블랜드클리닉: 오젬픽 체중감량의 '숨은 비용'은 근육이다",
  "Ozempic and Muscle Loss: What To Know (Cleveland Clinic)",
  "클리블랜드클리닉은 GLP-1 약물(세마글루타이드/오젬픽)의 급격한 체중감량이 근육 손실을 동반한다고 설명한다. 빠진 무게의 상당 부분이 지방이 아닌 제지방(근육)이며, 이는 약물 자체보다 급속 감량의 결과다. 근력운동과 단백질 섭취가 핵심 방어책이다.",
  "정리: ① 클리블랜드클리닉이 오젬픽-근손실 관계를 정리. ② 급격한 체중감량은 지방과 함께 근육(제지방)도 빼앗는다. ③ 근손실은 약물 직접 작용보다 '빠른 감량'에 기인. ④ 방어 — 저항성 운동, 충분한 단백질, 점진적 감량. ⑤ 근감소는 대사·근력·장기 건강에 악영향. NOGEAR 시각: 약으로 줄인 체중계 숫자가, 약으로 줄인 근육이라면 그건 발전이 아니라 손해다.",
  "research", "세마글루타이드 근손실", "Cleveland Clinic", "magazine",
  "https://health.clevelandclinic.org/ozempic-muscle-loss",
  sig(18, 16, 19, 16, 14, 10),
  ["오젬픽", "세마글루타이드", "근손실", "제지방", "단백질"],
  False, False, "high", "클리블랜드클리닉 의료기관 자료. 급속 감량-근손실 기전은 표준과 일치.", "research"),

 ("임상시험 등록: 세마글루타이드의 심장·근육 영향 정면 추적",
  "Impact of Semaglutide on Heart and Muscle Mass (ClinicalTrials.gov)",
  "ClinicalTrials.gov에 등록된 임상시험은 세마글루타이드(오젬픽/위고비)가 심장과 근육량에 미치는 영향을 직접 측정한다. GLP-1 약물의 근손실·심근 영향이 일화가 아니라 통제된 연구의 대상이 됐다. 약물의 '몸 구성 변화'를 과학이 정조준한 것이다.",
  "정리: ① ClinicalTrials.gov 등록 임상시험(NCT07272837). ② 목표 — 세마글루타이드의 심장·근육량 영향 정량 측정. ③ 배경 — GLP-1 약물의 근손실 우려가 임상적으로 부상. ④ 제지방·심근 변화를 영상·체성분으로 추적. ⑤ 함의 — 일화적 우려를 통제된 데이터로 검증. NOGEAR 시각: '살 빠진다'만 보던 약을, 이제 '심장·근육은 어떤가'로 본다. 그게 과학의 책임이다.",
  "research", "세마글루타이드 근손실", "ClinicalTrials.gov NCT07272837", "journal",
  "https://clinicaltrials.gov/study/NCT07272837",
  sig(16, 17, 16, 17, 13, 8),
  ["세마글루타이드", "임상시험", "심장", "근육량", "체성분"],
  True, True, "high", "ClinicalTrials.gov 1차 등록 임상시험. 심장·근육 영향 추적 설계는 검색 결과와 일치.", "research"),

 ("미국 대표표본 조사: 오젬픽·세마글루타이드 '오남용' 보고",
  "Ozempic/Semaglutide Injection Misuse in a Nationally Representative US Sample",
  "medRxiv 프리프린트는 미국 대표표본에서 세마글루타이드 주사제의 오남용 실태를 보고한다. 의학적 적응증 밖 사용, 비처방 경로 구매, 미용·체중 목적 남용이 확인된다. 'GLP-1 만능'이라는 분위기 속에서 오남용이 통계로 잡히기 시작했다.",
  "정리: ① medRxiv 프리프린트 — 미국 대표표본 대상 세마글루타이드 오남용 조사. ② 적응증 밖 사용·비처방 구매·미용 목적 남용 보고. ③ 온라인·비공식 경로 유통이 오남용을 키운다. ④ 부적절 용량·의학적 감독 부재의 위험. ⑤ 한계 — 프리프린트로 동료심사 미완료, 결과 변경 가능. NOGEAR 시각: '다들 맞는다'는 분위기가 오남용의 온상이다. 처방전 없는 주사는 보충제가 아니라 도박이다.",
  "research", "세마글루타이드 근손실", "medRxiv (preprint)", "journal",
  "https://www.medrxiv.org/content/10.64898/2025.12.25.25343021.full.pdf",
  sig(18, 13, 17, 17, 16, 9),
  ["세마글루타이드", "오젬픽", "오남용", "비처방", "프리프린트"],
  False, True, "medium", "medRxiv 프리프린트(동료심사 전). 오남용 보고는 흥미로우나 결과 잠정, 교차검증 필요.", "research"),

 ("오젬픽 근손실 막는 법 — Drugs.com이 정리한 방어 전략",
  "Does Ozempic cause muscle loss and how to prevent it? (Drugs.com)",
  "약물 정보 사이트 Drugs.com은 오젬픽 사용 시 근손실 여부와 예방법을 정리한다. 핵심은 저항성 운동과 충분한 단백질로, 감량 속도를 관리해 제지방 손실을 최소화하는 것이다. 약을 끊는 대신 '근육을 지키며 빼는' 실용 가이드다.",
  "정리: ① Drugs.com이 오젬픽-근손실 Q&A를 정리. ② 급격한 감량은 근육 손실을 동반할 수 있다. ③ 예방 — 주 2~3회 저항성 운동, 체중당 충분한 단백질. ④ 점진적 감량과 수분·영양 유지. ⑤ 근력·대사 보존이 장기 건강의 관건. NOGEAR 시각: 약이 식욕을 줄여도, 근육을 지키는 건 결국 운동과 단백질이다. 지름길은 없다.",
  "research", "세마글루타이드 근손실", "Drugs.com", "magazine",
  "https://www.drugs.com/medical-answers/ozempic-cause-muscle-loss-how-you-prevent-3578660/",
  sig(15, 13, 18, 14, 12, 8),
  ["오젬픽", "근손실예방", "저항성운동", "단백질", "Drugs.com"],
  False, False, "medium", "Drugs.com 약물 정보 사이트. 예방 일반론은 표준 권고와 일치, 2차 자료.", "research"),

 ("GLP-1 약물과 근손실 — 환자단체가 짚은 '근육질환자'의 위험",
  "Muscle loss with Ozempic and similar drugs (FSHD Society)",
  "근이영양증 환자단체 FSHD Society는 오젬픽 등 GLP-1 약물의 근손실 위험을 환자 관점에서 경고한다. 이미 근육이 약한 사람에게 추가 근손실은 더 치명적일 수 있다. 일반 다이어트 담론이 놓치는 '취약 집단'의 위험을 부각한다.",
  "정리: ① FSHD Society(안면견갑상완형 근이영양증 환자단체)의 경고. ② GLP-1 약물의 체중감량은 근손실을 동반할 수 있다. ③ 이미 근력이 약한 근육질환자에게는 추가 근손실이 더 위험. ④ 처방 전 근육 건강 평가와 운동·영양 동반 필요. ⑤ 의미 — '취약 집단'은 일반 다이어트 가이드의 사각지대. NOGEAR 시각: 같은 약이라도, 약한 근육을 가진 사람에겐 더 큰 칼이 된다.",
  "research", "세마글루타이드 근손실", "FSHD Society", "magazine",
  "https://www.fshdsociety.org/2024/08/12/muscle-loss-with-ozempic-and-similar-drugs/",
  sig(16, 14, 17, 13, 13, 8),
  ["GLP1", "오젬픽", "근손실", "근이영양증", "취약집단"],
  False, False, "medium", "FSHD Society 환자단체 자료. 취약집단 관점 경고는 합리적, 2차 자료.", "research"),

 ("오젬픽, 근육 '크기'만이 아니라 '기능'도 바꾼다 — 유타대 연구 제기",
  "New Study Raises Questions About How Ozempic Affects Muscle Size and Strength",
  "유타대 헬스 연구는 오젬픽이 근육의 크기뿐 아니라 질·기능에도 영향을 줄 수 있다는 의문을 제기한다. 단순 근육량 감소를 넘어 근력·근질 변화 가능성을 시사한다. 'GLP-1 = 좋은 감량'이라는 통념에 과학적 물음표를 단다.",
  "정리: ① 유타대 헬스가 오젬픽의 근육 영향을 연구. ② 쟁점 — 근육 '크기'뿐 아니라 '질·기능(근력)'까지 변할 수 있는가. ③ 단순 체중·근량 감소를 넘어선 질적 변화 가능성. ④ 추가 연구로 임상 의미 규명 필요. ⑤ 함의 — 감량의 '질'을 평가해야 한다. NOGEAR 시각: 근육은 무게가 아니라 기능이다. 숫자만 줄고 힘이 빠지면 그건 퇴보다.",
  "research", "세마글루타이드 근손실", "University of Utah Health", "magazine",
  "https://healthcare.utah.edu/newsroom/news/2025/08/new-study-raises-questions-about-how-ozempic-affects-muscle-size-and-strength",
  sig(17, 16, 17, 14, 14, 9),
  ["오젬픽", "근기능", "근력", "유타대", "감량의질"],
  False, False, "medium", "유타대 헬스 뉴스룸. 연구 제기 단계로 결론 아님, 추가 검증 필요.", "research"),

 ("'근손실 없는 세마글루타이드'라는 마케팅 — 자연요법 사이트의 주장 검토",
  "Semaglutide for Bodybuilding Without Muscle Wasting — 비판적 검토",
  "일부 자연요법·웰니스 사이트는 '근손실 없는 세마글루타이드 사용법'을 내세운다. 그러나 급속 감량에 따른 근손실은 운동·단백질로 줄일 뿐 완전히 막을 수 없으며, 'no muscle wasting' 같은 단정은 과장이다. NOGEAR는 이 마케팅 화법을 경계 대상으로 본다.",
  "정리: ① 웰니스 사이트가 '근손실 없는 세마글루타이드'를 표방. ② 실제 — 저항성 운동·단백질은 근손실을 '줄일' 뿐 '제거'하지 못한다. ③ 임상 데이터는 GLP-1 감량 시 상당한 제지방 손실을 보고. ④ '완전 방지' 단정은 마케팅 과장. ⑤ 의학적 감독 없는 사용은 위험. NOGEAR 시각: '근손실 없이'라는 약속은 대부분 판매 멘트다. 몸은 그렇게 공짜로 작동하지 않는다.",
  "news", "업계 비판", "LivvNatural (wellness) — 비판", "magazine",
  "https://livvnatural.com/how-to-prevent-muscle-wasting-while-on-semaglutide/",
  sig(15, 11, 17, 13, 15, 8),
  ["세마글루타이드", "마케팅", "근손실없음", "과장", "웰니스"],
  False, False, "low", "웰니스 상업 사이트를 비판적으로 인용. 'no wasting' 주장은 과장(NOGEAR 비판 대상).", "news"),
]


def build(rec):
    (title, title_en, summary, detail, cat, cat_ko, source, stype, url,
     signals, tags, peer, primary, conf, cnotes, bucket) = rec
    score = sum(signals.values())
    t, emoji = tier(score)
    credibility, badge = cred(peer, primary, conf, cnotes)
    return {
        "title": title,
        "title_en": title_en,
        "summary": summary,
        "summary_detail": detail,
        "category": cat,
        "category_ko": cat_ko,
        "source": source,
        "source_type": stype,
        "source_url": url,
        "credibility": credibility,
        "viral_signals": signals,
        "tags": tags,
        "viral_score": score,
        "viral_tier": t,
        "viral_emoji": emoji,
        "date": TODAY,
        "badge": badge,
        "source_verified": False,
        "title_original": title,
        "title_rewrite": title,
    }, bucket


def main():
    data = json.load(open(ARTICLES_FILE, encoding="utf-8"))
    news = data.get("news", [])
    research = data.get("research", [])

    existing_urls = {a.get("source_url") for a in news + research}
    existing_titles = {a.get("title", "")[:40] for a in news + research}

    added_news = added_research = dup = 0
    new_items = []
    for rec in A:
        art, bucket = build(rec)
        if art["source_url"] in existing_urls or art["title"][:40] in existing_titles:
            dup += 1
            continue
        existing_urls.add(art["source_url"])
        existing_titles.add(art["title"][:40])
        new_items.append(art)
        if bucket == "news":
            news.append(art)
            added_news += 1
        else:
            research.append(art)
            added_research += 1

    # 정렬 (viral_score 내림차순)
    news.sort(key=lambda x: x.get("viral_score", 0), reverse=True)
    research.sort(key=lambda x: x.get("viral_score", 0), reverse=True)

    # research 캡: 최신/고바이럴 우선 150 유지 (archive_manager가 별도 정리)
    RESEARCH_CAP = 150
    if len(research) > RESEARCH_CAP:
        research = research[:RESEARCH_CAP]

    data["news"] = news
    data["research"] = research

    meta = data.setdefault("meta", {})
    meta["last_updated"] = NOW.isoformat()
    meta["last_updated_kst"] = (
        f"{NOW.strftime('%Y-%m-%d %H:%M KST')} 아침 크롤 "
        f"(스테로이드NIH·보디빌더돌연사EHJ/ESC·SARMs간독성LiverTox·DNP치명률12%·"
        f"펩타이드FDA자문위·도핑사건사·세마글루타이드근손실) +{len(new_items)}건 (1차수집·미교차)"
    )
    all_scores = [a.get("viral_score", 0) for a in news + research]
    meta["total_articles"] = len(news) + len(research)
    meta["news_count"] = len(news)
    meta["research_count"] = len(research)
    meta["crawl_count"] = meta.get("crawl_count", 0) + 1
    meta["model"] = "claude-opus-4-8"
    meta["top_viral_score"] = max(all_scores) if all_scores else 0
    meta["avg_viral_score"] = round(sum(all_scores) / len(all_scores)) if all_scores else 0

    json.dump(data, open(ARTICLES_FILE, "w", encoding="utf-8"),
              ensure_ascii=False, indent=2)

    print(f"신규 추가: {len(new_items)}건 (news +{added_news}, research +{added_research})")
    print(f"중복 스킵: {dup}건")
    print(f"활성 합계: news {len(news)} + research {len(research)} = {len(news)+len(research)}")
    print("TOP3:")
    for a in sorted(new_items, key=lambda x: -x['viral_score'])[:3]:
        print(f"  {a['viral_emoji']} {a['viral_score']} {a['title']}")


if __name__ == "__main__":
    main()
