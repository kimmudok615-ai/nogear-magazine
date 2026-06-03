#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
NOGEAR Magazine — 아침 크롤 2026-06-03 (2차 배치)
브랜드: FXXK FAKES. STAY NATURAL.
포커스 확장: 트렌볼론 신경/심독성 · TRT 심혈관(뉘앙스) · HGH 장기비대/스테로이드거트 ·
            인슐린 남용 저혈당사 · 클렌부테롤 심독성 · 여유증 · 펠리오시스간염 · 신장 FSGS
모든 콘텐츠 한국어. 출처 URL은 6/3 웹검색에서 확인한 실제 링크. 정직 모드(미교차).
"""
import json
from datetime import datetime, timezone, timedelta
from pathlib import Path

KST = timezone(timedelta(hours=9))
NOW = datetime.now(KST)
TODAY = NOW.strftime("%Y.%m.%d")
BASE = Path(__file__).parent.parent / "content"
ARTICLES_FILE = BASE / "articles.json"


def sig(shock, sci, relat, recency, controversy, visual):
    return {"shock_factor": shock, "scientific_credibility": sci, "relatability": relat,
            "recency": recency, "controversy": controversy, "visual_potential": visual}


def tier(score):
    if score >= 90:
        return "VIRAL_BOMB", "🔴"
    if score >= 85:
        return "HIGH_VIRAL", "🟠"
    return "TRENDING", "🟠"


def cred(peer, primary, conf, notes):
    badge_map = {"high": "🔍 1차수집(미교차)", "medium": "🔍 미검증", "low": "⚠️ 저신뢰"}
    return {"peer_reviewed": peer, "primary_source": primary, "cross_checked": False,
            "cross_check_date": None, "url_alive": True, "cross_confirmed": False,
            "confidence": conf, "notes": notes, "fact_checked": False,
            "fact_check_date": None, "accuracy": "unverified"}, badge_map.get(conf, "🔍 미검증")


A = [
 # ===== 트렌볼론 =====
 ("트렌볼론 쓰는 남성, '안 쓰는 스테로이드 사용자'보다 더 망가진다 — 2026 국제연구",
  "The Trenbolo(g)ne Sandwich: International study comparing harms among AAS users with/without trenbolone",
  "Drug and Alcohol Review에 2026년 실린 국제연구(Bonenti 등)는 트렌볼론을 쓰는 남성과 다른 스테로이드만 쓰는 남성을 비교했다. 트렌볼론 그룹은 기분 불안정·과민·우울 같은 정신사회적 문제, 그리고 심혈관·간 부작용이 유의하게 더 흔했다. 같은 '약쟁이' 안에서도 트렌볼론은 별도의 위험 등급임을 데이터로 보여준다.",
  "정리: ① Wiley Drug and Alcohol Review 2026 게재 국제 비교연구. ② 설계 — 트렌볼론 사용군 vs 비사용(타 AAS) 사용군의 자가보고 건강문제 비교. ③ 트렌볼론군에서 기분 불안정·과민·우울 등 정신과적 문제 유의하게 증가. ④ 심혈관·간 부작용도 유의하게 더 높음. ⑤ 기전 — 트렌볼론은 지용성이 커 혈액뇌장벽을 통과해 피질·NMDA 수용체에 직접 영향. ⑥ 함의 — 모든 스테로이드가 같지 않으며 트렌볼론은 고위험. NOGEAR 시각: '트렌'이 별명까지 가진 이유가 있다. 근육은 더, 머리와 심장은 훨씬 더 비싸다.",
  "research", "트렌볼론 위험", "Drug and Alcohol Review 2026 (Wiley)", "journal",
  "https://onlinelibrary.wiley.com/doi/10.1111/dar.70162",
  sig(22, 19, 18, 18, 18, 10),
  ["트렌볼론", "정신과부작용", "심혈관", "간독성", "국제연구"],
  True, True, "high", "Wiley Drug and Alcohol Review 2026 게재 비교연구. 트렌볼론군 정신·심혈관·간 위험 증가 검색결과와 일치.", "research"),

 ("트렌볼론은 뇌를 통과한다 — 신경세포 사멸·미토콘드리아 기능 저하",
  "17β-trenbolone contributes to neurodegeneration / neurotoxicity in neuronal cultures",
  "신경세포 배양 연구들은 트렌볼론이 여러 아나볼릭 스테로이드 중 유일하게 신경세포 생존율과 미토콘드리아 기능을 떨어뜨렸다고 보고한다. 지용성이 높아 혈액뇌장벽을 쉽게 통과해 피질에 직접 작용하고, 신경 위축과 NMDA 수용체 밀도 감소를 유발한다. '근육 약'이 뇌를 깎는다는 직접 증거다.",
  "정리: ① 1차 신경세포 배양 실험에서 트렌볼론의 신경독성 평가. ② 트렌볼론은 검사한 AAS 중 유일하게 신경세포 수·미토콘드리아 기능을 유의하게 감소. ③ 높은 지용성으로 혈액뇌장벽 통과 → 피질 직접 작용. ④ 신경 위축·NMDA 수용체 밀도 감소로 인지·기분에 영향 가능. ⑤ 환경호르몬으로서 신경퇴행 기여 보고. NOGEAR 시각: 거울 속 근육은 커지는데 거울을 보는 뇌는 깎인다. 그 거래의 영수증은 늦게 도착한다.",
  "research", "트렌볼론 위험", "ResearchGate (neuronal culture studies)", "journal",
  "https://www.researchgate.net/publication/269174935_17_beta-trenbolone_an_anabolic-androgenic_steroid_as_well_as_an_environmental_hormone_contributes_to_neurodegeneration",
  sig(22, 17, 16, 13, 17, 10),
  ["트렌볼론", "신경독성", "혈액뇌장벽", "NMDA", "신경퇴행"],
  True, False, "medium", "전임상 신경세포 배양 연구. 트렌볼론 단독 신경독성은 검색결과와 일치, 동물·세포 수준.", "research"),

 ("장기 스테로이드 사용자의 '뇌 영상' — 비사용 웨이트리프터와 다르다",
  "Structural Brain Imaging of Long-Term AAS Users and Nonusing Weightlifters (Biological Psychiatry)",
  "Biological Psychiatry 연구는 장기 AAS 사용 웨이트리프터와 비사용 웨이트리프터의 뇌를 영상으로 비교했다. 같은 운동을 해도 스테로이드 사용군에서 구조적 차이가 관찰됐다. 약물이 근육뿐 아니라 뇌 구조에 흔적을 남긴다는 영상 근거다.",
  "정리: ① Biological Psychiatry 게재 뇌 구조 영상 연구. ② 대상 — 장기 AAS 사용 웨이트리프터 vs 비사용 웨이트리프터(운동 변수 통제). ③ 사용군에서 뇌 구조적 차이 관찰. ④ 의미 — 운동이 아니라 약물에 귀속될 가능성 시사. ⑤ 인과·기능적 함의는 추가 연구 필요. NOGEAR 시각: 같은 헬스장, 같은 운동. 차이는 약이었다. 그 차이가 뇌에 남았다.",
  "research", "트렌볼론 위험", "Biological Psychiatry", "journal",
  "https://www.biologicalpsychiatryjournal.com/article/S0006-3223(16)32529-X/fulltext",
  sig(20, 18, 16, 12, 16, 10),
  ["스테로이드", "뇌영상", "구조변화", "웨이트리프터", "신경"],
  True, False, "high", "Biological Psychiatry 게재 영상 연구. 사용군 뇌 구조 차이 보고는 검색결과와 일치.", "research"),

 # ===== TRT 뉘앙스 =====
 ("'TRT는 위험하다'의 반전 — TRAVERSE 트라이얼이 말하는 진짜 조건",
  "Cardiovascular safety of testosterone therapy: TRAVERSE trial & European Expert Panel position",
  "2026년 1월 유럽 전문가 패널 입장문(PMC)은 TRAVERSE 대규모 무작위 임상을 근거로, 적절히 선별·관리된 환자에서 테스토스테론 보충요법(TRT)은 심혈관 측면에서 안전하다고 정리했다. 핵심은 '적절한 처방과 정기 모니터링'이라는 조건이다. 이는 의학적 TRT와 무분별한 스테로이드 남용이 전혀 다른 범주임을 보여준다.",
  "정리: ① 2026.1 유럽 전문가 패널 입장문, TRAVERSE 트라이얼 기반. ② TRAVERSE — 대규모 무작위 위약대조 연구에서 적절한 TRT가 주요 심혈관 사건을 유의하게 늘리지 않음. ③ 전제 — '적절히 선별된 환자 + 정기 모니터링'. ④ 의학적 TRT(진단·처방·추적) ≠ 음지의 고용량 스테로이드 스택. ⑤ 무분별한 자가 주사·초생리적 용량은 이 안전성 결론의 범위 밖. NOGEAR 시각: 의사가 관리하는 TRT와 '브로사이언스' 스택은 같은 약이라도 전혀 다른 게임이다. 처방전이 그 경계다.",
  "research", "TRT·테스토스테론", "European Expert Panel / PMC (TRAVERSE)", "journal",
  "https://pmc.ncbi.nlm.nih.gov/articles/PMC12670475/",
  sig(18, 19, 17, 18, 15, 8),
  ["TRT", "테스토스테론", "TRAVERSE", "심혈관안전", "처방vs남용"],
  True, False, "high", "PMC 게재 유럽 전문가 패널 입장문(2026.1). 적절 TRT의 심혈관 안전성 결론은 TRAVERSE와 일치. 남용과 구분 필수.", "research"),

 # ===== HGH / 스테로이드 거트 =====
 ("'스테로이드 거트'의 정체 — 복부비대증후군, 성장호르몬·인슐린의 합작",
  "Abdominal Hypertrophy Syndrome (steroid gut): Characteristics and Pathophysiology",
  "PMC 논문은 보디빌더의 '스테로이드 거트(steroid gut)'를 복부비대증후군으로 규정한다. 장기간 성장호르몬·인슐린·아나볼릭 약물 사용으로 복부 장기와 조직이 커지면서 배가 비정상적으로 돌출한다. 팔룸보이즘으로도 불리는 이 현상은 '유발성 말단비대증'에 가깝다.",
  "정리: ① 복부비대증후군(스테로이드 거트)을 다룬 PMC 논문. ② 원인 — 장기간 성장호르몬(GH)·인슐린·아나볼릭 약물 병용. ③ 기전 — GH 과잉이 복부 장기·조직을 비대시켜 '유발성 말단비대증' 양상. ④ 결과 — 마른 사지에 돌출한 복부라는 기형적 체형. ⑤ 데이브 팔룸보 사례에서 '팔룸보이즘' 명명. NOGEAR 시각: 식스팩을 좇다 장기를 키웠다. 거울이 보여주지 않는 건 부풀어 오른 내장이다.",
  "research", "HGH·성장호르몬", "PMC (Abdominal Hypertrophy Syndrome)", "journal",
  "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11578072/",
  sig(22, 17, 18, 14, 17, 13),
  ["스테로이드거트", "팔룸보이즘", "성장호르몬", "복부비대", "말단비대증"],
  True, True, "high", "PMC 게재. 복부비대증후군 GH/인슐린 기전·팔룸보이즘 명명은 검색결과와 일치.", "research"),

 ("성장호르몬 남용 = '유발성 말단비대증' — 심장·간까지 커진다",
  "HGH: What It Is, Benefits & Side Effects (Cleveland Clinic)",
  "클리블랜드클리닉은 성장호르몬(HGH) 과잉이 말단비대증처럼 뼈·연골·장기를 비대시킨다고 설명한다. 보디빌더의 HGH 남용은 사실상 '유발성 말단비대증'으로, 심장·간 비대, 고혈압, 당뇨, 수면무호흡, 관절·신경 압박을 부른다. 키우려던 건 근육인데 커지는 건 장기다.",
  "정리: ① 클리블랜드클리닉의 HGH 정보. ② HGH 과잉 → 뼈·연골·장기 비대(말단비대증 양상). ③ 보디빌더 HGH 남용 = 유발성 말단비대증. ④ 합병증 — 심장·간 비대, 고혈압, 2형 당뇨, 수면무호흡. ⑤ 손목터널증후군·관절통·이목구비 변형도 동반. NOGEAR 시각: 성장호르몬은 '성장'을 가리지 않는다. 근육도, 심장도, 종양도 함께 키운다.",
  "research", "HGH·성장호르몬", "Cleveland Clinic", "magazine",
  "https://my.clevelandclinic.org/health/articles/23309-human-growth-hormone-hgh",
  sig(20, 16, 18, 13, 15, 11),
  ["HGH", "성장호르몬", "말단비대증", "장기비대", "심장비대"],
  False, False, "high", "클리블랜드클리닉 의료기관 자료. HGH 과잉-말단비대 기전은 내분비학 표준과 일치.", "research"),

 # ===== 인슐린 남용 =====
 ("보디빌더 '잠재적 인슐린 사용' 증례 — 저혈당으로 응급실에 실려오다",
  "Severe Hypoglycemia Due to Cryptic Insulin Use in a Bodybuilder",
  "ScienceDirect/PubMed에 실린 증례는 한 보디빌더가 근성장 목적의 은밀한 인슐린 사용으로 심각한 저혈당에 빠진 사례를 보고한다. 인슐린은 강력한 아나볼릭 호르몬이지만 탄수화물 없이 주사하면 혈당이 급락해 발작·혼수·사망으로 이어진다. '근육 펌핑'의 대가가 의식 상실이다.",
  "정리: ① 보디빌더의 은밀한(cryptic) 인슐린 사용 증례. ② 인슐린은 아나볼릭 효과로 근성장에 오용된다. ③ 탄수화물 섭취 없이 주사 시 급격한 저혈당. ④ 증상 — 혼란·발한·발작·혼수, 최악의 경우 사망. ⑤ 진단이 어려워 '잠재적' 사용으로 늦게 밝혀진다. NOGEAR 시각: 당뇨 치료제를 근육에 쓴다. 10단위가 치료라면 50단위는 관(棺)이다.",
  "research", "인슐린 남용", "ScienceDirect / PubMed (case report)", "journal",
  "https://www.sciencedirect.com/science/article/abs/pii/S0736467918310564",
  sig(23, 17, 18, 13, 17, 10),
  ["인슐린", "저혈당", "보디빌더", "혼수", "아나볼릭"],
  True, True, "medium", "ScienceDirect/PubMed 증례보고. 은밀한 인슐린 사용-중증 저혈당은 검색결과와 일치, 단일 증례.", "research"),

 ("사후 대사체 분석으로 잡는 '인슐린 중독사' — 보이지 않는 죽음의 추적",
  "Postmortem Metabolomics of Insulin Intoxications and Hypoglycemia-Related Deaths",
  "PMC 연구는 사후 대사체 분석(metabolomics)으로 인슐린 중독·저혈당 관련 사망을 식별하는 방법을 다룬다. 인슐린 과량은 흔적을 거의 남기지 않아 사인 규명이 어렵기로 악명 높다. 보디빌딩계 인슐린 남용 사망이 '보이지 않게' 묻힐 수 있음을 시사한다.",
  "정리: ① PMC 게재, 인슐린 중독사의 사후 진단 연구. ② 문제 — 인슐린 과량사는 부검에서 흔적이 거의 없어 규명이 어렵다. ③ 사후 대사체 분석으로 저혈당 관련 사망을 잡아내려는 시도. ④ 함의 — '원인 불명' 돌연사 중 일부가 인슐린일 수 있다. ⑤ 보디빌딩계 인슐린 남용의 통계가 과소 집계될 위험. NOGEAR 시각: 가장 무서운 약은 시신에 흔적조차 안 남기는 약이다. 인슐린이 그렇다.",
  "research", "인슐린 남용", "PMC (postmortem metabolomics)", "journal",
  "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9912265/",
  sig(22, 18, 15, 13, 17, 10),
  ["인슐린", "중독사", "사후분석", "대사체", "돌연사"],
  True, False, "high", "PMC 게재 법의학 연구. 인슐린 과량사 진단 난이도·대사체 추적은 검색결과와 일치.", "research"),

 # ===== 클렌부테롤 =====
 ("클렌부테롤, '살 빼는 약'이 심장을 친다 — 80%가 입원한 부작용 보고",
  "A descriptive study of adverse events from clenbuterol misuse for weight loss and bodybuilding",
  "PubMed에 색인된 부작용 연구는 체중감량·보디빌딩 목적의 클렌부테롤 오남용 사례를 분석했다. 빈맥·저칼륨혈증·트로포닌 상승 등 심장 부작용이 흔했고, 독성을 겪은 사람의 80% 이상이 입원이 필요했다. 베타작용제 특유의 긴 반감기로 증상이 1~8일 지속된다.",
  "정리: ① 클렌부테롤 오남용 부작용 기술연구(PubMed). ② 용도 — 지방연소·근육유지 목적의 비승인 사용. ③ 심장 부작용 — 빈맥, 저칼륨혈증, 고혈당, ECG 변화, 트로포닌·CPK 상승. ④ 독성 경험자의 80%+가 입원 필요. ⑤ 긴 반감기로 증상이 1~8일 지속. NOGEAR 시각: 지방을 태우려다 심장을 태운다. 거울 앞 건조함의 대가가 응급실 침대다.",
  "research", "클렌부테롤", "PubMed (adverse events study)", "journal",
  "https://pubmed.ncbi.nlm.nih.gov/23844963/",
  sig(21, 18, 18, 14, 16, 10),
  ["클렌부테롤", "심독성", "빈맥", "저칼륨혈증", "입원"],
  True, True, "high", "PubMed 색인 기술연구. 심장 부작용·80% 입원·반감기 정보는 검색결과와 일치.", "research"),

 ("클렌부테롤이 부른 심근염 — 한 증례가 보여준 심장의 비명",
  "Clenbuterol-Induced Myocarditis: A Case Report",
  "PMC에 실린 증례는 클렌부테롤이 심근염(심장 근육 염증)을 유발한 사례를 보고한다. 베타작용제가 심장을 과도하게 몰아붙이면 염증·손상으로 이어진다. 다이어트 약 한 알이 심근을 직접 공격할 수 있음을 보여준다.",
  "정리: ① PMC 게재 클렌부테롤 유발 심근염 증례. ② 기전 — 베타작용제가 심장을 과도하게 자극해 염증·손상 유발. ③ 임상 — 흉통, 트로포닌 상승, 심전도 변화. ④ 베타작용제의 심장 부하가 만성화되면 심비대로 진행. ⑤ 다이어트·커팅 목적 사용의 직접 심장 위해. NOGEAR 시각: 심근염은 '잠깐의 컨디션'이 아니다. 심장 근육에 새겨진 흉터다.",
  "research", "클렌부테롤", "PMC (myocarditis case)", "journal",
  "https://pmc.ncbi.nlm.nih.gov/articles/PMC7473675/",
  sig(21, 17, 16, 13, 16, 10),
  ["클렌부테롤", "심근염", "베타작용제", "흉통", "심장손상"],
  True, False, "high", "PMC 게재 증례보고. 클렌부테롤-심근염 연관은 검색결과와 일치, 단일 증례.", "research"),

 ("'저용량이면 괜찮다'? — 소량 클렌부테롤도 중독시킨다",
  "Low Dose Clenbuterol Toxicity: Case Report and Review of Literature",
  "PMC 증례·문헌고찰은 '저용량'이라고 안전하지 않음을 보여준다. 소량 클렌부테롤로도 빈맥·떨림·저칼륨혈증 등 독성이 나타났다. 베타작용제 특유의 약동학 탓에 '조금'의 안전 마진이 좁다는 경고다.",
  "정리: ① 저용량 클렌부테롤 독성 증례·문헌고찰(PMC). ② '소량이면 안전'이라는 통념을 반박. ③ 저용량에서도 빈맥·떨림·저칼륨혈증 등 독성 발현. ④ 긴 반감기·체내 축적으로 안전 마진이 좁다. ⑤ 자가 용량 조절의 위험성 강조. NOGEAR 시각: 독은 용량을 봐주지 않는다. '조금'이라는 자기위안이 가장 위험하다.",
  "research", "클렌부테롤", "PMC (low dose toxicity)", "journal",
  "https://pmc.ncbi.nlm.nih.gov/articles/PMC10324766/",
  sig(19, 17, 16, 13, 15, 9),
  ["클렌부테롤", "저용량독성", "반감기", "축적", "안전마진"],
  True, False, "high", "PMC 게재 증례·문헌고찰. 저용량 독성 발현은 검색결과와 일치.", "research"),

 ("미국 중독정보센터: '클렌부테롤은 비승인·안전하지 않다'",
  "Clenbuterol: Unapproved and unsafe (Poison Control)",
  "미국 중독정보센터(Poison Control)는 클렌부테롤을 인체용으로 승인되지 않은 위험 물질로 규정한다. 동물용·연구용으로 유통되지만 인체 사용 시 심혈관·신경 독성을 일으킨다. 공신력 있는 독성 기관의 직접 경고다.",
  "정리: ① Poison Control(미국 중독정보센터)의 공식 안내. ② 클렌부테롤은 미국 내 인체용 미승인. ③ 동물용·연구용 표기로 유통되나 인체 사용 시 독성. ④ 심혈관·신경계 부작용 경고. ⑤ 응급 시 즉시 중독센터·응급실 안내. NOGEAR 시각: 가축에게 쓰는 약을 사람이 다이어트에 쓴다. 그 문장 하나로 충분하다.",
  "research", "클렌부테롤", "Poison Control (US)", "magazine",
  "https://www.poison.org/articles/clenbuterol-unapproved-and-unsafe-201",
  sig(18, 15, 16, 12, 15, 9),
  ["클렌부테롤", "중독센터", "미승인", "독성", "경고"],
  False, True, "medium", "Poison Control 공신력 있는 독성 기관 안내. 미승인·독성 사실 신뢰도 높음.", "research"),

 # ===== 여유증 =====
 ("스테로이드 사용자 39%가 '여유증' — 끊어도 가슴은 돌아오지 않는다",
  "The Burden of Anabolic Androgenic Steroid-Induced Gynecomastia",
  "PubMed 연구는 AAS 관련 여성형유방(여유증)의 실제 유병률이 약 39.2%로, 수술 전 문진만으로 잡힌 4.1%보다 훨씬 높다고 보고했다. 스테로이드가 에스트로겐으로 전환되며 유선조직이 자라고, 한번 생긴 조직은 약을 끊어도 사라지지 않고 영구화된다. 1980~2013년 미국에서만 보디빌더 1,500명 이상이 여유증 수술을 받았다.",
  "정리: ① AAS 유발 여유증의 부담을 다룬 PubMed 연구. ② 정밀 재평가 시 실제 유병률 약 39.2%(문진 기반 4.1%의 ~10배). ③ 기전 — 스테로이드가 에스트로겐으로 방향족화(aromatization)되어 유선조직 증식. ④ 영구성 — 한번 형성된 유선조직은 중단 후에도 사라지지 않고, 근육이 줄면 오히려 더 도드라진다. ⑤ 1980~2013년 미국 보디빌더 1,500명+ 수술. NOGEAR 시각: 약은 끊을 수 있어도 가슴은 못 끊는다. 칼로 도려내야 사라지는 흉터다.",
  "research", "여유증", "PubMed (AAS-induced gynecomastia)", "journal",
  "https://pubmed.ncbi.nlm.nih.gov/37705825/",
  sig(22, 18, 19, 14, 17, 12),
  ["여유증", "여성형유방", "에스트로겐전환", "영구화", "수술"],
  True, True, "high", "PubMed 게재 연구. 유병률 39.2%·영구성·수술 1500명은 검색결과와 일치.", "research"),

 # ===== 펠리오시스 간염 / 간 =====
 ("스테로이드가 간에 '핏빛 구멍'을 낸다 — 펠리오시스 간염, 파열하면 출혈사",
  "Peliosis Hepatis: A Vascular Tumor-Like Liver Lesion",
  "Annals of Internal Medicine 임상증례는 펠리오시스 간염을 간에 혈액이 고인 낭성 병변으로 설명한다. 아나볼릭 스테로이드는 이 만성 혈관 손상과 간선종·간세포암의 원인으로 지목된다. 무증상에서 간부전·복강내 출혈(간 파열)까지 진행할 수 있는 침묵의 병변이다.",
  "정리: ① Annals of Internal Medicine(ACP) 임상증례. ② 펠리오시스 간염 — 간 내 혈액이 고이는 낭성·혈관성 병변. ③ 아나볼릭 스테로이드가 만성 혈관 손상과 간선종·간세포암의 원인. ④ 경과 — 무증상~간부전, 문맥압항진, 담즙정체, 간 파열로 인한 복강내 출혈. ⑤ 종양처럼 보여 암과 감별이 필요. NOGEAR 시각: 간은 비명을 안 지른다. 핏빛 구멍이 터지는 날, 처음으로 안다.",
  "research", "간 손상", "Annals of Internal Medicine (ACP)", "journal",
  "https://www.acpjournals.org/doi/10.7326/aimcc.2024.0078",
  sig(23, 18, 16, 14, 17, 12),
  ["펠리오시스간염", "간선종", "간파열", "복강내출혈", "스테로이드"],
  True, True, "high", "ACP Annals 임상증례. 펠리오시스 간염-AAS 연관·간파열 위험은 간장학 표준과 일치.", "research"),

 ("NIH LiverTox: 안드로겐 스테로이드는 '간독성 약물'로 등재돼 있다",
  "Androgenic Steroids — LiverTox (NCBI)",
  "NIH의 약물 간독성 데이터베이스 LiverTox는 안드로겐 스테로이드를 독립 항목으로 등재하고, 담즙정체성 간손상·펠리오시스 간염·간선종·간세포암과의 연관을 정리한다. 경구 17α-알킬화 제제가 특히 위험하다. 정부 표준 레퍼런스가 스테로이드 간독성을 공식 기록한 것이다.",
  "정리: ① NIH LiverTox에 안드로겐 스테로이드 등재. ② 연관 간질환 — 담즙정체성 간손상, 펠리오시스 간염, 간선종, 간세포암. ③ 경구 17α-알킬화 제제가 간 부담 최대. ④ 황달·간효소 상승이 흔한 초기 신호. ⑤ 정부 표준 레퍼런스의 공식 기록이라는 무게. NOGEAR 시각: '간 보호제'를 같이 먹는다는 발상 자체가, 그 약이 간을 친다는 자백이다.",
  "research", "간 손상", "LiverTox / NCBI Bookshelf", "journal",
  "https://www.ncbi.nlm.nih.gov/books/NBK548931/",
  sig(20, 19, 16, 13, 15, 9),
  ["안드로겐스테로이드", "LiverTox", "간독성", "간세포암", "17알파알킬화"],
  True, True, "high", "NIH LiverTox 표준 데이터베이스 등재. 담즙정체·간선종·HCC 연관은 간장학 표준과 일치.", "research"),

 # ===== 신장 FSGS =====
 ("스테로이드 보디빌더 10명 중 9명이 '신장 흉터' — 단백뇨·신부전으로",
  "The development of focal segmental glomerulosclerosis secondary to anabolic steroid abuse",
  "컬럼비아대 연구진은 장기 스테로이드 사용 보디빌더 10명을 분석해 9명에게서 국소분절사구체경화증(FSGS)을 확인했다. 거대 근육량과 고단백 섭취가 신장을 만성 과여과 상태로 몰아 사구체에 흉터를 남기고, 단백뇨와 신부전으로 이어졌다. 평균 단백뇨 10.1g/일, 30%는 신증후군으로 발현했다.",
  "정리: ① 컬럼비아대 의료센터의 첫 AAS-신장손상 기술 연구. ② 장기 사용 보디빌더 10명 중 9명에서 FSGS(사구체 흉터) 확인. ③ 기전 — 거대 근육량·고단백(300~550g/일)·크레아틴이 신장을 만성 과여과로 내몰아 사구체 경화. ④ 임상 — 평균 단백뇨 10.1g/일, 평균 크레아티닌 3.0mg/dl, 30% 신증후군. ⑤ 일부는 신기능 심각 저하. NOGEAR 시각: '클린 벌크'라던 고단백·약물의 끝에 투석이 기다린다. 신장은 두 번째 기회를 잘 안 준다.",
  "research", "신장 손상", "PMC (FSGS / Columbia study)", "journal",
  "https://pmc.ncbi.nlm.nih.gov/articles/PMC3233923/",
  sig(23, 19, 18, 14, 17, 11),
  ["신장손상", "FSGS", "단백뇨", "신부전", "고단백"],
  True, True, "high", "PMC 게재 컬럼비아대 연구. 10명 중 9명 FSGS·단백뇨 수치는 검색결과와 일치.", "research"),

 ("'헬스 신증' — 보디빌딩 보충제·스테로이드가 부르는 급성 신손상",
  "Acute kidney injury associated with androgenic steroids and nutritional supplements in bodybuilders",
  "Clinical Kidney Journal(옥스퍼드) 연구는 보디빌더에서 안드로겐 스테로이드와 보충제 사용에 동반된 급성 신손상(AKI)을 보고한다. 스테로이드, 고단백·크레아틴, 탈수·이뇨가 겹쳐 신장을 급격히 망가뜨린다. '짐 네프로파시(gym nephropathy)'라는 용어까지 등장했다.",
  "정리: ① Clinical Kidney Journal(옥스퍼드) 게재 연구. ② 보디빌더의 급성 신손상(AKI)과 스테로이드·보충제 사용 연관. ③ 복합 요인 — 스테로이드, 고단백·크레아틴, 탈수, 이뇨제, NSAID. ④ '짐 네프로파시'로 불리는 운동·약물성 신질환 개념. ⑤ 급성에서 만성 신질환으로 진행 가능. NOGEAR 시각: 근육 1kg을 위해 신장을 건다. 거울엔 안 보이는 장기가 가장 먼저 무너진다.",
  "research", "신장 손상", "Clinical Kidney Journal (Oxford)", "journal",
  "https://academic.oup.com/ckj/article/8/4/415/337086",
  sig(21, 18, 18, 13, 16, 10),
  ["신장손상", "급성신손상", "짐네프로파시", "크레아틴", "탈수"],
  True, True, "high", "Oxford Clinical Kidney Journal 게재. AKI-스테로이드/보충제 연관은 검색결과와 일치.", "research"),

 ("Nature 자매지: '아나볼릭 스테로이드 남용이 FSGS를 부를 수 있다'",
  "Anabolic steroid abuse can lead to focal segmental glomerulosclerosis (Nature Reviews Nephrology)",
  "Nature Reviews Nephrology는 아나볼릭 스테로이드 남용이 국소분절사구체경화증(FSGS)을 유발할 수 있다고 정리했다. 거대 근육량에 의한 사구체 과부하와 스테로이드의 직접 영향이 결합한다. 최고 권위 신장학 리뷰지가 스테로이드 신독성을 공식 기술한 것이다.",
  "정리: ① Nature Reviews Nephrology의 리뷰. ② 핵심 — AAS 남용이 FSGS(사구체 흉터)를 유발 가능. ③ 기전 — 거대 근육량에 의한 사구체 과여과 + 스테로이드 직접 영향. ④ 결과 — 단백뇨·신기능 저하·신부전. ⑤ 권위 신장학지의 공식 기술이라는 의미. NOGEAR 시각: 근육이 클수록 신장 한 개가 감당할 짐이 커진다. 몸은 공짜 점심을 주지 않는다.",
  "research", "신장 손상", "Nature Reviews Nephrology", "journal",
  "https://www.nature.com/articles/nrneph.2010.5",
  sig(20, 19, 16, 12, 16, 10),
  ["FSGS", "신장손상", "NatureReviews", "사구체과여과", "스테로이드"],
  True, False, "high", "Nature Reviews Nephrology 게재. AAS-FSGS 연관 기술은 신장학 표준과 일치.", "research"),

 ("'짐 네프로파시' — 보디빌딩이 신장을 깎는다는 신질환 개념",
  "Gym nephropathy: bodybuilding versus kidney damaging",
  "이집트 신장이식학회지 논문은 '짐 네프로파시'라는 개념으로 보디빌딩 관련 신장 손상을 정리한다. 스테로이드·고단백·보충제·탈수가 신장을 만성적으로 압박한다. 헬스 문화가 만든 새로운 신질환 범주라는 점에서 주목된다.",
  "정리: ① 이집트 신장이식학회지(ESNT)의 '짐 네프로파시' 논문. ② 보디빌딩 관련 신장 손상을 하나의 개념으로 묶음. ③ 위험 요인 — 아나볼릭 스테로이드, 고단백, 크레아틴·보충제, 탈수. ④ 만성 과여과·독성으로 신기능 저하. ⑤ 헬스 문화가 만든 신질환 범주로 인식 확산. NOGEAR 시각: 운동이 건강이라는 공식이, 약과 보충제 앞에선 깨진다. 신장은 그 차이를 정확히 안다.",
  "research", "신장 손상", "J. Egyptian Society of Nephrology and Transplantation", "journal",
  "https://journals.lww.com/esnt/fulltext/2019/19040/gym_nephropathy__bodybuilding_versus_kidney.4.aspx",
  sig(19, 16, 18, 12, 16, 9),
  ["짐네프로파시", "신장손상", "고단백", "보충제", "탈수"],
  True, False, "medium", "ESNT 학회지 게재. 짐 네프로파시 개념·위험요인은 검색결과와 일치.", "research"),

 ("팔룸보이즘 'HGH 거트'의 경고 — 잠재적으로 치명적인 성장호르몬 부작용",
  "Palumboism AKA HGH Gut: A Potentially Fatal Side-Effect of Human Growth Hormone",
  "Gilmore Health는 '팔룸보이즘(HGH 거트)'을 성장호르몬 남용의 잠재적 치명 부작용으로 소개한다. 마른 사지에 비정상적으로 돌출한 복부는 단순 미용 문제가 아니라 장기 비대의 외형적 신호다. 대중 매체가 이 현상의 위험을 환기한다.",
  "정리: ① Gilmore Health의 팔룸보이즘 해설. ② 정의 — HGH 남용으로 복부 장기·조직이 비대해 배가 돌출. ③ 데이브 팔룸보 사례에서 명명. ④ 단순 미용이 아니라 장기 비대의 외형 신호로 잠재적 치명. ⑤ 인슐린·아나볼릭 병용이 악화 요인. NOGEAR 시각: 무대 위 '괴물 복부'는 트로피가 아니라 진단서다. 부푼 건 근육이 아니라 내장이다.",
  "news", "HGH·성장호르몬", "Gilmore Health News", "magazine",
  "https://www.gilmorehealth.com/palumboism-a-potentially-fatal-side-effect-of-human-growth-hormone/",
  sig(20, 11, 18, 13, 17, 13),
  ["팔룸보이즘", "HGH거트", "성장호르몬", "복부돌출", "장기비대"],
  False, False, "low", "Gilmore Health 대중 건강매체. 팔룸보이즘 일반론은 PMC 논문과 일치하나 1차 근거 아님.", "news"),

 ("보디빌더의 은밀한 인슐린 — '치료용 10단위 vs 죽음의 50단위'",
  "Insulin Use and Abuse: Helpful or Lethal? (NFPT)",
  "피트니스 교육기관 NFPT는 보디빌딩계 인슐린 남용의 치명성을 경고한다. 당뇨 치료 1일 약 10단위에 비해 남용자는 50단위까지 주사해 혼수·사망 위험을 자초한다. 특히 취침 전 주사는 저혈당을 인지하지 못해 그대로 사망으로 이어질 수 있다.",
  "정리: ① NFPT(피트니스 교육기관)의 인슐린 남용 경고. ② 치료 용량(약 10단위/일) 대비 남용은 50단위까지. ③ 탄수화물 없이 고용량 주사 → 저혈당 혼수·사망. ④ 취침 전 주사는 저혈당을 인지 못해 특히 치명적. ⑤ 다수 프로 보디빌더가 인슐린 유발 혼수로 사망. NOGEAR 시각: 잠들기 전 주사 한 방이 다시 못 깨는 잠이 된다. 인슐린에 '브로사이언스'는 없다.",
  "news", "인슐린 남용", "NFPT", "magazine",
  "https://nfpt.com/the-lethal-risks-of-insulin-abuse/",
  sig(21, 12, 18, 13, 17, 10),
  ["인슐린", "저혈당", "50단위", "취침주사", "혼수"],
  False, False, "low", "NFPT 피트니스 교육기관 자료. 용량 비교·취침 위험은 임상 일반론과 일치, 2차 자료.", "news"),
]


def build(rec):
    (title, title_en, summary, detail, cat, cat_ko, source, stype, url,
     signals, tags, peer, primary, conf, cnotes, bucket) = rec
    score = sum(signals.values())
    t, emoji = tier(score)
    credibility, badge = cred(peer, primary, conf, cnotes)
    return {
        "title": title, "title_en": title_en, "summary": summary, "summary_detail": detail,
        "category": cat, "category_ko": cat_ko, "source": source, "source_type": stype,
        "source_url": url, "credibility": credibility, "viral_signals": signals, "tags": tags,
        "viral_score": score, "viral_tier": t, "viral_emoji": emoji, "date": TODAY,
        "badge": badge, "source_verified": False, "title_original": title, "title_rewrite": title,
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
            news.append(art); added_news += 1
        else:
            research.append(art); added_research += 1

    news.sort(key=lambda x: x.get("viral_score", 0), reverse=True)
    research.sort(key=lambda x: x.get("viral_score", 0), reverse=True)

    data["news"] = news
    data["research"] = research

    meta = data.setdefault("meta", {})
    meta["last_updated"] = NOW.isoformat()
    meta["last_updated_kst"] = (
        f"{NOW.strftime('%Y-%m-%d %H:%M KST')} 아침 크롤 2차 "
        f"(트렌볼론신경독성·TRT뉘앙스·스테로이드거트·인슐린저혈당사·클렌부테롤심독성·여유증39%·펠리오시스간염·신장FSGS) "
        f"+{len(new_items)}건 (1차수집·미교차)"
    )
    all_scores = [a.get("viral_score", 0) for a in news + research]
    meta["total_articles"] = len(news) + len(research)
    meta["news_count"] = len(news)
    meta["research_count"] = len(research)
    meta["top_viral_score"] = max(all_scores) if all_scores else 0
    meta["avg_viral_score"] = round(sum(all_scores) / len(all_scores)) if all_scores else 0

    json.dump(data, open(ARTICLES_FILE, "w", encoding="utf-8"), ensure_ascii=False, indent=2)

    print(f"신규 추가: {len(new_items)}건 (news +{added_news}, research +{added_research})")
    print(f"중복 스킵: {dup}건")
    print(f"활성 합계: news {len(news)} + research {len(research)} = {len(news)+len(research)}")
    print("TOP5:")
    for a in sorted(new_items, key=lambda x: -x['viral_score'])[:5]:
        print(f"  {a['viral_emoji']} {a['viral_score']} {a['title']}")


if __name__ == "__main__":
    main()
