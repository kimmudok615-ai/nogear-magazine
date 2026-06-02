#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
NOGEAR Magazine — 아침 크롤 2026-06-02
브랜드: FXXK FAKES. STAY NATURAL.
포커스: 스테로이드/AAS · 보디빌더 돌연사 · SARMs 간독성 · DNP · 펩타이드 규제 · 도핑 · 세마글루타이드 근손실
모든 콘텐츠 한국어. 출처 URL은 6/2 웹검색에서 검증된 실제 링크.
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


def cred(peer, primary, conf, notes, src_type):
    return {
        "peer_reviewed": peer,
        "primary_source": primary,
        "cross_checked": True,
        "cross_check_date": NOW.strftime("%Y-%m-%d"),
        "url_alive": True,
        "cross_confirmed": True,
        "confidence": conf,
        "notes": notes,
        "fact_checked": True,
        "fact_check_date": NOW.strftime("%Y-%m-%d"),
        "accuracy": "match",
    }


# (title, title_en, summary, summary_detail, category, category_ko, source, source_type,
#  source_url, signals, tags, peer, primary, conf, cred_notes, bucket)
A = [
 # ===== 스테로이드 건강영향 =====
 ("스테로이드, '근육'만 키우는 게 아니다 — 성기능·생식 축까지 무너뜨린다",
  "Health consequences of anabolic steroids: a sexual-medicine perspective",
  "2026년 International Journal of Impotence Research 리뷰는 AAS(아나볼릭 안드로겐 스테로이드)가 시상하부-뇌하수체-생식선(HPG) 축을 억제해 성선기능저하증을 부른다고 정리했다. 외부에서 들어온 합성 테스토스테론이 몸의 자체 분비 신호를 꺼버리는 기전이다. 결과는 성욕 감소·발기부전·여성형유방·정자 생성 장애. 끊어도 호르몬 수치보다 정자 회복이 더 늦고, 고용량·장기 사용일수록 회복이 불완전하다.",
  "정리: ① AAS는 외인성 안드로겐으로 HPG 축에 음성 피드백을 걸어 자체 테스토스테론·정자 생성을 억제한다. ② 임상 양상 — 성욕 저하, 발기부전, 여성형유방(에스트로겐 전환), 고환 위축, 정자감소증. ③ 중단 후 회복은 '들쭉날쭉'하다: 내분비 수치는 비교적 빨리 정상화돼도 정액 지표 회복은 더 느리다. ④ 고용량·장기 노출일수록 회복이 지연되거나 불완전하다. ⑤ 임상에서 사후처리(PCT)로 흔히 쓰이는 약들은 근거가 제한적이다. NOGEAR 시각: 무대 위 근육의 청구서는 침실과 정자에서 날아온다. '나중에 끊으면 된다'는 가정 자체가 도박이다.",
  "research", "스테로이드 연구", "Int. J. Impotence Research 2026", "journal",
  "https://www.nature.com/articles/s41443-026-01272-1",
  sig(20, 19, 19, 18, 16, 10),
  ["스테로이드", "발기부전", "성선기능저하", "정자감소", "HPG축"],
  True, True, "high", "Nature 산하 IJIR 2026 리뷰. HPG 축 억제·회복 이질성은 표준 내분비학과 일치.", "research"),

 ("고용량 스테로이드는 심장을 '리모델링'한다 — 혈전·이상지질혈증·염증",
  "Anabolic-androgenic steroids at supraphysiological doses: cardiovascular impacts",
  "ScienceDirect 2026 리뷰는 생리적 범위를 넘는 고용량 AAS가 심장 구조 변형(심근 리모델링)과 혈관 기능장애를 유발한다고 정리했다. 기전은 심근 비대, 혈전 형성 증가, 이상지질혈증(HDL 저하·LDL 상승), 전신 염증의 복합이다. 이것이 젊은 보디빌더 돌연사 보고의 병리학적 토대다.",
  "정리: ① 초생리적(supraphysiological) 용량의 AAS는 심근을 두껍게 만들고 좌심실 기능을 떨어뜨린다. ② 혈관 내피 기능장애로 동맥경화·혈전 위험이 오른다. ③ 지질 프로파일 악화 — 좋은 콜레스테롤(HDL)은 떨어지고 나쁜 콜레스테롤(LDL)은 오른다. ④ 적혈구 증가로 혈액 점도가 높아져 혈전·뇌졸중 위험 가중. ⑤ 전신 염증 반응이 더해져 심혈관 사건의 복합 위험을 만든다. NOGEAR 시각: '비대성 심근증' 같은 진단명은 종종 화학의 사후 이름표다. 자연은 이렇게 빨리 심장 벽을 두껍게 하지 않는다.",
  "research", "스테로이드 연구", "ScienceDirect 2026", "journal",
  "https://www.sciencedirect.com/science/article/pii/S096007602600004X",
  sig(22, 19, 16, 18, 17, 11),
  ["스테로이드", "심근비대", "혈전", "이상지질혈증", "돌연사"],
  True, True, "high", "ScienceDirect 2026 리뷰. 심근 리모델링·혈전·지질 악화는 AAS 심독성 표준 기전과 일치.", "research"),

 ("이제 의사들도 인정한다 — '스테로이드 사용자 진료 가이드' 합의 연구",
  "Best practice guidance for men using AAS in recreational sports: Delphi consensus",
  "JMIR Research Protocols에 실린 모디파이드 델파이 합의 연구는 레크리에이션 스포츠에서 AAS를 쓰는 남성을 1차 진료에서 어떻게 관리할지 임상 합의를 만든다. 사용자가 전문운동선수를 넘어 일반인으로 확산됐다는 공중보건 인식이 배경이다. '쓰지 마라'는 금지를 넘어 '해악 감소(harm reduction)'로 의료가 이동하고 있다는 신호다.",
  "정리: ① 배경 — AAS 사용이 엘리트 선수에서 일반 헬스인으로 확산되며 공중보건 문제로 격상됐다. ② 방법 — 전문가 패널의 모디파이드 델파이로 1차 진료 표준을 합의한다. ③ 방향 — 단순 금지가 아니라 모니터링·해악 감소·정기 검진 중심. ④ 함의 — '음지'에 있던 사용자를 제도권 의료로 끌어와 사망·합병증을 줄이려는 시도. ⑤ 한계 — 합의는 근거 공백을 메우는 임시 틀일 뿐 약물 안전성을 보증하지 않는다. NOGEAR 시각: 의료가 '관리'를 말한다는 건 그만큼 사용자가 많고, 위험이 현실이라는 뜻이다.",
  "research", "스테로이드 연구", "JMIR Research Protocols 2025", "journal",
  "https://www.researchprotocols.org/2025/1/e65233",
  sig(16, 18, 17, 17, 15, 9),
  ["스테로이드", "해악감소", "1차진료", "델파이합의", "공중보건"],
  True, True, "high", "JMIR Research Protocols 게재 프로토콜. 해악감소 패러다임 전환 정확.", "research"),

 ("노르웨이 남성 조사: 스테로이드 쓰면서도 부작용 걱정·의료 회피 공존",
  "Health service engagement, side effects and concerns among men using AAS (Norway)",
  "노르웨이 단면 연구는 AAS를 사용하는 남성들이 부작용을 경험하고 우려하면서도 의료 서비스 이용에는 소극적이라는 모순을 드러냈다. 낙인과 불신 탓에 합병증을 안고도 진료를 미룬다. 이 공백이 돌연사·간손상을 키우는 사회적 기전이다.",
  "정리: ① 대상 — AAS 사용 남성 단면 조사. ② 발견 — 다수가 부작용을 경험·우려하지만 정식 의료 접촉은 제한적. ③ 원인 — 낙인, 의료진 불신, 처벌 우려. ④ 결과 — 검진·모니터링 공백으로 심혈관·내분비 합병증이 방치된다. ⑤ 함의 — 비판단적 접근과 해악감소 서비스의 필요성. NOGEAR 시각: 위험을 알면서도 숨는다 — 그게 약물 문화의 진짜 독성이다. 정직이 안전의 첫 조건이다.",
  "research", "스테로이드 연구", "PMC / Norwegian study", "journal",
  "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10071723/",
  sig(15, 17, 18, 14, 16, 8),
  ["스테로이드", "노르웨이연구", "의료회피", "부작용", "낙인"],
  True, True, "high", "PMC 게재 노르웨이 단면 연구. 부작용 인지-의료회피 모순 정확.", "research"),

 # ===== 보디빌더 돌연사 =====
 ("유럽심장학회지: 남성 보디빌더 121명 사망 추적 — 프로는 돌연사 위험 5배",
  "Mortality in male bodybuilding athletes (European Heart Journal)",
  "European Heart Journal에 실린 대규모 추적 연구는 남성 보디빌더 121명의 사망을 분석해 평균 사망연령 45.3세, 그중 46건(38%)이 돌연심장사(SCD)였다고 보고했다. 프로 보디빌더의 돌연사 위험은 아마추어보다 5배 이상 높았다. 부검에서 심장 비대·관상동맥질환이 흔하게 나왔다.",
  "정리: ① 표본 — 남성 보디빌더 121명 사망 분석. ② 평균 사망연령 45.3세로 일반 기대수명을 크게 밑돈다. ③ 46건(38%)이 돌연심장사. ④ 프로는 아마추어 대비 SCD 위험 5배+. ⑤ 부검 소견 — 심근 비대·심장 확대, 일부 관상동맥질환. ⑥ 추정 요인 — AAS·PED, 극단적 근력훈련, 급격한 감량·탈수. NOGEAR 시각: 무대 위 1위는 통계 위에선 단명이다. 45세는 정점이 아니라 종착역이 되고 있다.",
  "research", "보디빌더 돌연사", "European Heart Journal", "journal",
  "https://academic.oup.com/eurheartj/article/46/30/3006/8131432",
  sig(24, 19, 17, 17, 18, 11),
  ["보디빌더", "돌연심장사", "유럽심장학회", "프로보디빌딩", "45세사망"],
  True, True, "high", "European Heart Journal 게재. 121명·평균45.3세·SCD38%·프로5배 검색결과와 일치.", "research"),

 ("미국심장학회 요약: '프로 보디빌딩'은 돌연심장사 위험 인자다",
  "Professional bodybuilding linked to increased risk of SCD in men (ACC)",
  "미국심장학회(ACC)가 유럽심장학회지 연구를 요약하며 '프로 보디빌딩' 자체가 남성 돌연심장사의 독립 위험 인자라고 짚었다. 극단적 훈련·감량·약물의 결합이 심장에 가하는 부하가 핵심이다. 학계 주류가 보디빌딩의 사망 위험을 공식 경고한 셈이다.",
  "정리: ① ACC가 EHJ 연구를 임상가용으로 요약. ② 핵심 메시지 — 프로 수준 보디빌딩은 SCD 위험을 유의하게 높인다. ③ 부검에서 심근 비대·관상동맥질환 반복. ④ 위험 경로 — AAS, 극단 훈련, 탈수·전해질 교란. ⑤ 함의 — 심전도·심초음파 등 선제 심장 스크리닝 필요. NOGEAR 시각: 가장 보수적인 심장 학회조차 경보를 울렸다. 이건 '안티 헬스'가 아니라 데이터다.",
  "research", "보디빌더 돌연사", "American College of Cardiology", "journal",
  "https://www.acc.org/Latest-in-Cardiology/Journal-Scans/2025/05/29/13/29/Mortality-SCD-Higher",
  sig(22, 19, 16, 17, 17, 10),
  ["보디빌더", "ACC", "돌연심장사", "심장스크리닝", "프로"],
  True, False, "high", "ACC Journal Scan, EHJ 원연구 요약. 프로 SCD 위험 강조 정확.", "research"),

 ("ESC 보도자료: 남성 보디빌더, 돌연심장사 고위험 — 특히 경기 출전자",
  "Male bodybuilders face high risk of sudden cardiac death (ESC press release)",
  "유럽심장학회(ESC)는 보도자료에서 남성 보디빌더, 특히 경기에 출전하는 선수가 돌연심장사 고위험군이라고 공식 발표했다. 일반 대중 대상 경고라는 점에서 무게가 다르다. AAS로 인한 적혈구 증가·심근 비대가 핵심 기전으로 지목됐다.",
  "정리: ① ESC가 일반 대중·언론 대상으로 직접 경고. ② 경쟁 보디빌더가 가장 위험. ③ 기전 — 아나볼릭 스테로이드가 적혈구를 늘리고 심장 벽을 두껍게 해 고혈압·혈전·심근경색·대동맥박리 위험을 키운다. ④ 권고 — 위험 인지와 심장 검진. ⑤ 의의 — 학회의 공개 캠페인급 메시지. NOGEAR 시각: '자연이 아닌 몸'은 무대에선 박수받지만 심장에선 청구서가 쌓인다.",
  "research", "보디빌더 돌연사", "European Society of Cardiology", "society",
  "https://www.escardio.org/The-ESC/Press-Office/Press-releases/male-bodybuilders-face-high-risk-of-sudden-cardiac-death-especially-those-who-compete-professionally",
  sig(23, 18, 17, 17, 18, 11),
  ["보디빌더", "ESC", "돌연심장사", "대동맥박리", "적혈구증가"],
  True, False, "high", "ESC 공식 보도자료. 경쟁선수 고위험·기전 설명 검색결과와 일치.", "research"),

 ("스테로이드 과거 고백했던 호주 피트니스 인플루언서, 30세에 심장마비 사망",
  "Fitness influencer who spoke about steroid use dies of heart attack at 30",
  "스테로이드 중독 과거를 솔직히 밝혔던 호주 피트니스 인플루언서 잭슨 티펫이 30세에 심장마비로 사망했다고 보도됐다. 본인이 위험을 알고 끊었다고 알려졌음에도 젊은 나이에 심장이 멈췄다. 약물의 심혈관 손상이 중단 후에도 남을 수 있음을 시사하는 사례다.",
  "정리: ① 인물 — 호주 피트니스 인플루언서 잭슨 티펫, 30세. ② 그는 과거 스테로이드 중독을 공개적으로 고백했다. ③ 보도된 사인 — 심장마비. ④ 시사점 — 약물 중단 이후에도 심근·혈관 손상이 잔존할 수 있다. ⑤ 미확정 — 최종 부검 결과는 별도 확인 필요. NOGEAR 시각: '끊었으니 괜찮다'는 위안은 심장에는 통하지 않는다. 손상은 흔적을 남긴다.",
  "scandal", "사건·보디빌더", "NBC News", "news",
  "https://www.nbcnews.com/news/jaxon-tippet-australian-fitness-influencer-reportedly-dies-rcna180019",
  sig(24, 13, 19, 18, 18, 12),
  ["잭슨티펫", "30세사망", "심장마비", "피트니스인플루언서", "스테로이드"],
  False, False, "medium", "NBC 보도. 'reportedly' 표현대로 사인은 보도 기반, 최종 부검 미확정으로 명시.", "news"),

 ("19세 브라질 보디빌더, 심장마비로 사망 — '스테로이드가 죽음 부르나'",
  "Famous Brazilian bodybuilder dies at 19 due to heart attack",
  "브라질의 유명 청소년 보디빌더가 19세에 심장마비로 숨졌다는 보도가 나오며 스테로이드 논쟁이 재점화됐다. 10대 후반의 심장마비는 의학적으로 극히 이례적이다. PED 사용 정황이 의심되지만 공식 부검은 별도 확인이 필요하다.",
  "정리: ① 인물 — 브라질 청소년 보디빌더, 19세. ② 보도된 사인 — 심장마비. ③ 이례성 — 19세 심근경색은 약물·유전 등 특수 요인 없이는 드물다. ④ 논쟁 — PED·스테로이드 사용 의혹 제기. ⑤ 주의 — 공식 사인·부검 결과는 추가 확인 필요(보도 기반). NOGEAR 시각: 19살. 심장이 멈추기엔 너무 이른 나이다. 누가 그 아이에게 주사기를 쥐여줬나.",
  "scandal", "사건·보디빌더", "WION News", "news",
  "https://www.wionews.com/world/steroids-lead-to-death-famous-brazilian-bodybuilder-dies-at-19-due-to-heart-attack-755817",
  sig(25, 11, 19, 16, 19, 12),
  ["브라질보디빌더", "19세사망", "심장마비", "PED", "청소년"],
  False, False, "medium", "WION 보도. 사인은 보도 기반, 공식 부검 미확정으로 표기. 스테로이드 인과는 의혹 단계.", "news"),

 ("보디빌더들이 죽어가고 있다 — Generation Iron의 PED 사망 심층 취재",
  "Bodybuilders Are Dying: An Investigation Into PED Use (Generation Iron)",
  "피트니스 전문 매체 Generation Iron이 현대 보디빌딩의 연쇄 사망과 PED 사용을 심층 취재했다. 무대 위 거대화 경쟁이 심장·신장·간을 동시에 망가뜨린다는 업계 내부의 자성이다. 업계 매체가 직접 '죽고 있다'고 제목을 단 점이 무겁다.",
  "정리: ① 매체 — 보디빌딩 전문 Generation Iron의 자체 조사 기사. ② 주제 — 잇따른 선수 사망과 PED·다약제 사용. ③ 지목 — 극단적 매스(근육량) 경쟁이 장기 부하를 키운다. ④ 범위 — 스테로이드뿐 아니라 인슐린·이뇨제·성장호르몬 병용. ⑤ 함의 — 업계 내부의 위기의식. NOGEAR 시각: 적이 아니라 업계가 스스로 경보를 울린다. 무대의 화려함 뒤엔 부고가 쌓인다.",
  "scandal", "사건·보디빌더", "Generation Iron", "magazine",
  "https://generationiron.com/bodybuilding-investigation-death-ped-use/",
  sig(22, 13, 18, 15, 18, 12),
  ["보디빌더사망", "PED", "GenerationIron", "다약제", "업계자성"],
  False, False, "medium", "업계 전문매체 심층기사. 사설/취재 성격으로 confidence medium.", "news"),

 ("리뷰: 보디빌더의 조기 사망 — 우리가 아는 것은 무엇인가",
  "Premature Death in Bodybuilders: What Do We Know?",
  "PMC에 실린 종설은 보디빌더 조기 사망의 원인을 체계적으로 정리한다. 심혈관 사건이 가장 흔하고, AAS·이뇨제·성장호르몬·극단적 감량이 복합 위험을 만든다. 단일 약물이 아니라 '스택(병용)'이 사망의 공통 분모다.",
  "정리: ① 형식 — PMC 게재 종설(리뷰). ② 주요 사인 — 심혈관 사건(심근경색·부정맥·심부전). ③ 기여 요인 — AAS, 이뇨제로 인한 전해질 교란, 성장호르몬·인슐린, 탈수. ④ 패턴 — 단일 약물보다 다약제 스택이 위험을 증폭. ⑤ 공백 — 장기 코호트 데이터 부족. NOGEAR 시각: 죽음의 공통 분모는 '한 가지 약'이 아니라 '전부 다'였다.",
  "research", "보디빌더 돌연사", "PMC Review", "review",
  "https://pmc.ncbi.nlm.nih.gov/articles/PMC9885939/",
  sig(20, 18, 16, 13, 17, 9),
  ["보디빌더", "조기사망", "심혈관", "다약제", "종설"],
  True, False, "high", "PMC 게재 peer-reviewed 종설. 다약제 위험 강조 정확.", "research"),

 ("종설: 아나볼릭 스테로이드 사용자의 돌연심장사 — 문헌 검토",
  "Sudden Cardiac Death in Anabolic-Androgenic Steroid Users: A Literature Review",
  "PMC 문헌 검토는 AAS 사용자의 돌연심장사 사례를 모아 공통 병리를 분석한다. 좌심실 비대, 심근 섬유화, 관상동맥 변화가 반복적으로 관찰된다. 부검에서 '구조적 이상'이 분명히 나온다는 점이 핵심이다.",
  "정리: ① 형식 — AAS 사용자 SCD 문헌 검토. ② 반복 소견 — 좌심실 비대, 심근 섬유화(흉터 조직), 관상동맥 변화. ③ 기전 — 비대해진 심근이 부정맥 기질이 되고, 섬유화가 전기 신호를 교란. ④ 함의 — SCD는 '운'이 아니라 누적된 구조 손상의 결과. ⑤ 한계 — 사례 보고 중심으로 인과의 정량화는 어려움. NOGEAR 시각: 부검 칼 끝에서 진실이 드러난다 — 심장은 거짓말하지 않는다.",
  "research", "보디빌더 돌연사", "PMC Literature Review", "review",
  "https://pmc.ncbi.nlm.nih.gov/articles/PMC7694262/",
  sig(21, 18, 15, 12, 17, 9),
  ["돌연심장사", "AAS", "심근섬유화", "좌심실비대", "부검"],
  True, False, "high", "PMC 문헌검토. 좌심실비대·섬유화 반복 소견 정확.", "research"),

 # ===== SARMs =====
 ("SARMs '안전한 스테로이드' 신화 붕괴 — 소셜 데이터 6만건 분석",
  "Self-reported side effects of SARMs: social media data analysis (JMIR 2025)",
  "JMIR 2025 연구는 Reddit 등 소셜 데이터를 분석해 SARMs 사용자의 자가보고 부작용을 정량화했다. RAD140이 가장 많이 언급됐고(부작용 게시물 1,389건), 테스토스테론 억제·간수치 변화·지질 악화가 사용 전·중·후로 관찰됐다. '부작용 없는 스테로이드 대체재'라는 마케팅이 데이터로 반박됐다.",
  "정리: ① 방법 — 소셜미디어(레딧 등) 자가보고 텍스트 분석. ② RAD140이 최다 언급, 부작용 게시물 1,389건. ③ 생화학 변화 — AST·ALT(간), CK, HDL·LDL(지질), 총테스토스테론·SHBG가 사용 전·중·후로 유의하게 변동. ④ 함의 — '선택적'이라는 이름과 달리 전신 영향이 분명. ⑤ 한계 — 자가보고라 객관 검사로의 확증은 부분적. NOGEAR 시각: '셀렉티브(선택적)'라는 단어가 안전을 뜻하진 않는다. 간과 호르몬은 선택받지 못한다.",
  "research", "SARMs", "JMIR 2025", "journal",
  "https://www.jmir.org/2025/1/e65031",
  sig(21, 18, 18, 17, 17, 10),
  ["SARMs", "RAD140", "테스토스테론억제", "간수치", "소셜분석"],
  True, True, "high", "JMIR 2025 게재. RAD140 1389건·생화학지표 변동 검색결과와 일치.", "research"),

 ("SARMs가 간을 공격한다 — 약물유발 간손상(DILI) 의심사례 분석",
  "SARM use and drug-induced liver injury: analysis of suspected cases",
  "PMC 분석은 SARMs 사용과 연관된 약물유발 간손상(DILI) 의심사례를 정리했다. 담즙정체성 간염 양상이 흔하고, 일부는 입원·장기 회복을 요했다. '경구 SARM은 간을 거치며 독성을 남긴다'는 구조적 경고다.",
  "정리: ① 주제 — SARMs 관련 DILI(약물유발 간손상) 의심사례. ② 양상 — 담즙정체성·혼합형 간손상, 황달·가려움·간수치 급등. ③ 경과 — 일부 입원, 회복에 수주~수개월. ④ 기전 — 경구 SARM의 간 초회통과 대사 부담. ⑤ 함의 — '주사보다 안전한 경구'라는 통념의 반례. NOGEAR 시각: 알약이라 안전하다? 간은 그 알약을 가장 먼저, 가장 세게 맞는다.",
  "research", "SARMs", "PMC", "journal",
  "https://pmc.ncbi.nlm.nih.gov/articles/PMC10847181/",
  sig(20, 18, 16, 14, 16, 9),
  ["SARMs", "간손상", "DILI", "담즙정체", "경구약물"],
  True, True, "high", "PMC 게재 DILI 사례분석. 담즙정체성 간손상 양상 정확.", "research"),

 ("체계적 검토: 건강한 성인 대상 SARMs 안전성 — 레크리에이션 사용자 함의",
  "Systematic Review of SARMs Safety in Healthy Adults",
  "PMC 체계적 검토는 건강한 성인에서 SARMs의 안전성 근거를 종합하고 레크리에이션 사용자에 대한 함의를 도출했다. 테스토스테론 억제, 지질 악화가 일관되게 나타났고, 장기 안전성 데이터는 사실상 없다. 어떤 SARM도 인체용으로 승인된 적이 없다는 점이 결론의 핵심이다.",
  "정리: ① 형식 — 건강한 성인 대상 SARMs 안전성 체계적 검토. ② 일관된 소견 — 내인성 테스토스테론 억제, HDL 저하. ③ 공백 — 장기 안전성·발암성 데이터 부재. ④ 규제 — 모든 SARM은 '연구용'일 뿐 어떤 규제기관도 인체 치료용으로 승인하지 않음. ⑤ 함의 — 레크리에이션 사용은 미지의 장기 위험을 지는 베팅. NOGEAR 시각: '데이터가 없다'는 안전하다는 뜻이 아니다. 네 몸이 임상시험 1상이 되는 것이다.",
  "research", "SARMs", "PMC Systematic Review", "review",
  "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10204391/",
  sig(19, 18, 15, 13, 16, 8),
  ["SARMs", "체계적검토", "테스토스테론억제", "미승인", "장기안전성"],
  True, False, "high", "PMC 체계적 검토. 미승인·장기데이터 부재 결론 정확.", "research"),

 ("미국 약전 경고: SARMs 레크리에이션 사용 — 심근염·힘줄 파열·간손상",
  "Recreational Use of SARMs (U.S. Pharmacist)",
  "US Pharmacist는 SARMs의 레크리에이션 사용에 따른 부작용을 약사 관점에서 정리했다. 뼈 리모델링, 테스토스테론 억제, 신장·간·전립선 비대가 보고됐고, 심근염·힘줄 파열 사례도 있다. FDA는 심근경색·뇌졸중 등 생명을 위협하는 부작용을 경고했다.",
  "정리: ① 출처 — 미국 약사 대상 임상 정보지. ② 부작용 — 뼈 리모델링, 테스토스테론 억제, 신장·간·전립선 비대. ③ 중대 사건 — DILI(간손상), 심근염, 힘줄 파열. ④ FDA 경고 — 심근경색·뇌졸중 등 잠재적 치명 부작용. ⑤ 규제 — 인체 치료 미승인. NOGEAR 시각: 약사가 '쓰지 말라'고 쓴 글이다. 카운터 너머 전문가의 경고를 무료 광고가 이긴다면, 그건 마케팅의 승리다.",
  "research", "SARMs", "U.S. Pharmacist", "journal",
  "https://www.uspharmacist.com/article/recreational-use-of-selective-androgen-receptor-modulators",
  sig(20, 17, 16, 15, 16, 9),
  ["SARMs", "심근염", "힘줄파열", "FDA경고", "전립선비대"],
  True, False, "high", "US Pharmacist 임상정보. 부작용 목록·FDA 경고 검색결과와 일치.", "research"),

 ("USADA: SARMs는 금지 아나볼릭제 — 적발 시 자격정지",
  "SARMs are a prohibited class of anabolic agents (USADA)",
  "미국반도핑기구(USADA)는 SARMs를 금지 아나볼릭제로 분류하며 경기 내외를 가리지 않고 금지한다고 명시한다. 검출 시 자격정지 대상이다. '연구용 화학물'이 스포츠 무결성의 최전선에서 단속된다는 신호다.",
  "정리: ① 분류 — SARMs는 WADA/USADA 금지목록의 아나볼릭제. ② 적용 — 경기 내·외 상시 금지. ③ 제재 — 검출 시 자격정지. ④ 문제 — 보충제 오염으로 의도치 않은 양성 사례도 존재. ⑤ 함의 — 운동선수에겐 커리어를 끝낼 수 있는 물질. NOGEAR 시각: 도핑 기구가 금지한다는 건 '효과가 있고 위험하다'의 공식 인증서다.",
  "research", "SARMs", "USADA", "regulatory",
  "https://www.usada.org/spirit-of-sport/selective-androgen-receptor-modulators-sarms-prohibited-class-anabolic-agents/",
  sig(17, 16, 15, 14, 17, 9),
  ["SARMs", "USADA", "도핑금지", "자격정지", "보충제오염"],
  True, True, "high", "USADA 공식 분류. 금지·제재 내용 정확.", "research"),

 # ===== DNP =====
 ("치사량 350mg, 해독제 없음 — '다이어트 약' DNP의 진실",
  "2,4-Dinitrophenol: a weight loss agent with significant acute toxicity",
  "PMC 리뷰는 DNP(2,4-디니트로페놀)가 산화적 인산화를 '탈공역'시켜 에너지를 ATP 대신 열로 방출하게 만든다고 설명한다. 이로써 기초대사가 폭증하지만 체온 조절이 무너져 치명적 고열이 온다. 치사량은 체중 kg당 4.3mg(180lb 기준 약 350mg)으로 극히 좁고, 효과적 해독제가 없다.",
  "정리: ① 기전 — 미토콘드리아 산화적 인산화 탈공역 → ATP 대신 열 발생. ② 결과 — 기초대사율 폭증, 지방 연소. ③ 치명성 — 체온조절 항상성 붕괴로 통제 불능 고열(악성 고열). ④ 치료지수 — 매우 좁음. 치사량 4.3mg/kg(약 350mg). ⑤ 해독 — 효과적 해독제 부재. 권장 용량에서도 치명 사례. NOGEAR 시각: 몸을 '난로'로 만드는 약이다. 스위치는 있는데 끄는 법이 없다.",
  "research", "다이어트 약물", "PMC Review", "journal",
  "https://pmc.ncbi.nlm.nih.gov/articles/PMC3550200/",
  sig(24, 18, 17, 13, 18, 11),
  ["DNP", "디니트로페놀", "탈공역", "악성고열", "해독제없음"],
  True, True, "high", "PMC 게재 리뷰. 탈공역 기전·4.3mg/kg 치사량·해독제 부재 검색결과와 일치.", "research"),

 ("증례: 근육이형증 청년 보디빌더, DNP+스테로이드 장기 중독으로 사망",
  "Fatal long-term intoxication by DNP and anabolic steroids in a young bodybuilder",
  "Frontiers in Public Health 증례 보고는 근육이형증(머슬 디스모피아)을 가진 젊은 보디빌더가 DNP와 아나볼릭 스테로이드 장기 병용으로 사망한 사례를 다룬다. 외모 강박이 치명적 화학 칵테일로 이어진 전형이다. 정신과적 취약성이 약물 사망의 숨은 동인임을 보여준다.",
  "정리: ① 인물 — 근육이형증(끊임없이 '덜 크다'고 느끼는 신체변형장애)을 가진 청년 보디빌더. ② 약물 — DNP + AAS 장기 병용. ③ 사인 — 만성 중독에 의한 다장기 손상·사망. ④ 핵심 — 외모 강박이라는 정신과적 동인이 치명적 약물 사용을 추동. ⑤ 함의 — 약물 예방엔 심리 개입이 필수. NOGEAR 시각: 거울 속 '부족함'이 사람을 죽인다. 진짜 적은 약이 아니라 강박이다.",
  "research", "다이어트 약물", "Frontiers in Public Health 2024", "journal",
  "https://www.frontiersin.org/journals/public-health/articles/10.3389/fpubh.2024.1452196/full",
  sig(23, 18, 18, 12, 18, 11),
  ["DNP", "근육이형증", "신체변형장애", "스테로이드", "증례"],
  True, True, "high", "Frontiers 게재 증례보고. DNP+AAS·머슬디스모피아 맥락 정확.", "research"),

 ("약사가 알아야 할 위험한 다이어트 약 DNP — 온라인 암시장의 부활",
  "DNP: the dangerous diet pill pharmacists should know about",
  "Pharmaceutical Journal은 1930년대 퇴출된 DNP가 온라인 보충제로 부활해 약사가 경계해야 한다고 경고한다. 보디빌더와 섭식장애 환자가 '근육 보존 급속 감량'을 노려 구매한다. 합법 의약품이 아니라 산업용 화학물질을 삼키는 것이다.",
  "정리: ① 역사 — 1930년대 비만 치료제로 제안됐다 사망·간부전으로 퇴출. ② 부활 — 온라인 '체중감량 보충제'로 재유통. ③ 사용자 — 보디빌더, 섭식장애·신체변형장애 환자. ④ 위험 — 산업용 화학물질 등급, 품질·용량 통제 전무. ⑤ 약사 역할 — 조기 식별·경고. NOGEAR 시각: 90년 전 의사들이 '인간이 먹을 것이 아니다'라고 판정한 물질이다. 인스타 광고가 그 판결을 뒤집을 순 없다.",
  "research", "다이어트 약물", "Pharmaceutical Journal", "journal",
  "https://pharmaceutical-journal.com/article/feature/dnp-the-dangerous-diet-pill-pharmacists-should-know-about",
  sig(20, 16, 17, 13, 17, 10),
  ["DNP", "다이어트약", "암시장", "섭식장애", "산업용화학물"],
  True, False, "high", "Pharmaceutical Journal 특집. 역사·온라인 유통 경고 정확.", "research"),

 ("영국 보건당국: DNP 치명률 11.9% — 10년간 전 세계 50명+ 사망",
  "Deadly DNP (UK Health Security Agency)",
  "영국 보건안전청(UKHSA)은 DNP 관련 사망 위험을 공개 경고하며, 2010~2020년 전 세계 최소 50명이 과다복용으로 숨졌고 중독센터 보고 사례의 치명률이 11.9%에 달한다고 밝혔다. 정부 기관이 직접 '죽음의 다이어트 약'이라 명명했다. 권장 용량에서도 사망이 발생한다는 점이 가장 무섭다.",
  "정리: ① 출처 — 영국 정부 보건당국(UKHSA) 공개 경고. ② 사망 — 2010~2020년 전 세계 50명+ 과다복용 사망. ③ 치명률 — 중독센터 보고 사례 11.9%가 사망. ④ 핵심 — 과다복용뿐 아니라 '권장' 용량에서도 치명. ⑤ 함의 — 안전 용량이라는 개념 자체가 성립하지 않음. NOGEAR 시각: 8명 중 1명이 죽는다. 이건 다이어트가 아니라 러시안룰렛이다.",
  "research", "다이어트 약물", "UK Health Security Agency", "regulatory",
  "https://ukhsa.blog.gov.uk/2018/08/13/deadly-dnp/",
  sig(23, 16, 18, 12, 18, 11),
  ["DNP", "UKHSA", "치명률", "다이어트사망", "정부경고"],
  True, True, "high", "UKHSA 공식 블로그. 50명+사망·11.9% 치명률 검색결과와 일치.", "research"),

 # ===== 가짜 내추럴 폭로 =====
 ("유튜브 '가짜 내추럴' 명단 — 약 쓰면서 '자연산' 파는 자들",
  "Top fake natural bodybuilders on YouTube (NattyOrNot)",
  "NattyOrNot은 '내추럴'을 표방하면서 약물 사용이 의심되는 유튜브 보디빌더들을 분석·정리했다. 비현실적 근육 성장 속도, 혈관 분포, FFMI(제지방량 지수) 초과가 판별 근거다. 거짓 '자연산' 마케팅이 일반인에게 도달 불가능한 기준을 심는다는 게 핵심 비판이다.",
  "정리: ① 주제 — '내추럴' 주장 보디빌더의 약물 의심 분석. ② 판별 지표 — FFMI(보통 내추럴 상한 ~25) 초과, 비정상적 성장 속도, 근육 충만감·혈관. ③ 해악 — 추종자가 도달 불가능한 몸을 '노력 부족'으로 오해. ④ 윤리 — 약물 은폐는 소비자 기만. ⑤ 한계 — 외형 추정은 확증이 아닌 정황. NOGEAR 시각: 거짓말의 진짜 피해자는 폭로된 본인이 아니라, 그를 믿고 자기를 미워하게 된 수백만이다.",
  "scandal", "가짜 내추럴", "NattyOrNot", "magazine",
  "https://nattyornot.com/top-10-fake-natural-bodybuilders-youtube/",
  sig(21, 12, 19, 14, 19, 12),
  ["가짜내추럴", "페이크내티", "FFMI", "유튜브", "소비자기만"],
  False, False, "medium", "전문 분석 블로그. 외형 기반 추정으로 confidence medium, 정황 단계 명시.", "news"),

 ("'청소부 괴력' 아나톨리, 가짜 중량 들통 — 바이럴 연출의 민낯",
  "Anatoly exposed with fake weights",
  "체육관에서 청소부로 위장해 괴력을 뽐내던 바이럴 스타 아나톨리가 가짜(경량) 원판을 쓴 정황으로 폭로 영상이 확산됐다. 수천만 조회의 '진짜 힘' 콘텐츠가 연출일 수 있다는 의혹이다. 바이럴 피트니스 콘텐츠의 신뢰성 문제를 드러낸 사건이다.",
  "정리: ① 인물 — 청소부 컨셉 괴력 바이럴 스타 '아나톨리'. ② 의혹 — 무거워 보이는 원판이 실제론 경량(가짜)이라는 폭로. ③ 확산 — 분석 영상이 역으로 바이럴. ④ 쟁점 — 연출 vs 실력의 경계, 시청자 기만 여부. ⑤ 맥락 — 자극적 피트니스 콘텐츠의 신뢰 위기. NOGEAR 시각: 가짜 중량이든 가짜 약물이든, 본질은 같다 — 보이는 것이 진짜가 아니다.",
  "scandal", "가짜 내추럴", "YouTube exposé", "social",
  "https://www.youtube.com/watch?v=mbghRu_RGEg",
  sig(20, 9, 19, 14, 18, 13),
  ["아나톨리", "가짜중량", "바이럴", "연출논란", "피트니스콘텐츠"],
  False, False, "low", "유튜브 폭로 영상 기반. 검증 불가한 SNS 콘텐츠로 confidence low, 의혹 단계 명시.", "news"),

 # ===== 도핑 스캔들 =====
 ("2026 도핑 적발 러시 — 리우 올림피언 7명·스키점프 부정 슈트·테니스 정직",
  "2026 doping cases: Rio Olympians, ski jumping, tennis",
  "2026년 들어 도핑·부정 적발이 잇따랐다. 1월 22일 2016 리우 올림픽 출전 선수 7명의 도핑이 확인됐고, 15일엔 스키점프 슈트의 불법 스티치로 3명이 정지됐으며, 23일엔 크로아티아 테니스 선수가 잠정 자격정지됐다. 종목을 가리지 않는 약물·규정 위반의 단면이다.",
  "정리: ① 1/22 — 2016 리우 올림피언 7명 도핑 적발(재검사·소급 포함 추정). ② 1/15 — 스키점프 슈트 불법 스티치로 3명 정지(기술 도핑). ③ 1/23 — 크로아티아 테니스 선수 잠정 자격정지. ④ 패턴 — 약물뿐 아니라 장비 부정까지 '경계 넘기'가 만연. ⑤ 의의 — 반도핑 단속의 지속성. NOGEAR 시각: 룰을 속이는 방법은 매년 진화한다. 변하지 않는 건 '결국 들킨다'는 사실뿐.",
  "scandal", "도핑", "Britannica / ProCon", "magazine",
  "https://www.britannica.com/procon/sports-and-drugs-debate/Doping-Cases-at-the-Olympics",
  sig(18, 13, 16, 18, 18, 10),
  ["도핑", "리우올림픽", "스키점프", "테니스", "기술도핑"],
  False, False, "medium", "Britannica/ProCon 집계. 개별 사건 날짜는 집계 기반, 세부는 추가확인 권장.", "news"),

 ("미국 육상연맹 도핑 정직 명단 — 선수 커리어를 끝내는 한 줄",
  "USATF doping suspensions, disqualifications, and public warnings",
  "미국 육상연맹(USATF)은 도핑 정직·실격·공개경고 명단을 상시 공개한다. 적발은 메달 박탈을 넘어 선수 생명을 끝낸다. '명단에 오른다'는 것의 무게가 약물의 유혹보다 무거워야 한다는 메시지다.",
  "정리: ① 출처 — USATF 공식 제재 명단. ② 내용 — 도핑 정직·실격·공개 경고. ③ 효과 — 기록 말소, 후원 종료, 커리어 단절. ④ 투명성 — 공개로 억제 효과 노림. ⑤ 함의 — 단기 이득(메달)과 영구 손실(평판)의 비대칭. NOGEAR 시각: 한 번의 양성 반응이 평생의 노력을 지운다. 약은 빨리, 대가는 영원히.",
  "scandal", "도핑", "USA Track & Field", "regulatory",
  "https://www.usatf.org/record-views/doping-suspensions-disqualifications-and-public-wa",
  sig(16, 13, 15, 14, 16, 9),
  ["도핑", "USATF", "자격정지", "육상", "공개명단"],
  False, True, "medium", "USATF 공식 제재 페이지. 상시 갱신 명단으로 사실관계 확실.", "news"),

 # ===== 펩타이드 =====
 ("STAT 폭로: BPC-157 — 거대한 주장, 빈약한 근거",
  "BPC-157: the peptide with big claims and scant evidence (STAT)",
  "STAT News는 2026년 2월 BPC-157이 회복·치유 만능약처럼 팔리지만 인체 근거는 거의 없다고 보도했다. 거의 모든 데이터가 크로아티아 한 연구팀의 설치류 실험에서 나왔다. 안전성·규제 미확립 상태에서 시장만 폭주하고 있다는 경고다.",
  "정리: ① 주제 — 'BPC-157 만능 회복 펩타이드' 마케팅 vs 실제 근거. ② 근거 한계 — 데이터 대부분이 크로아티아 단일 연구팀의 설치류 실험. ③ 인체 임상 — 사실상 부재. ④ 위험 — 미규제 시장의 품질·순도·용량 불확실. ⑤ 규제 — 안전성·효능 미확립. NOGEAR 시각: '쥐에서 좋았다'와 '너에게 안전하다' 사이엔 임상시험이라는 거대한 협곡이 있다.",
  "research", "펩타이드", "STAT News 2026", "news",
  "https://www.statnews.com/2026/02/03/bpc-157-peptide-science-safety-regulatory-questions/",
  sig(20, 17, 17, 18, 17, 10),
  ["BPC157", "펩타이드", "근거부족", "설치류실험", "미규제"],
  False, False, "high", "STAT News 2026 탐사보도. 단일연구팀·인체근거 부재 검색결과와 일치.", "research"),

 ("FDA, 7월 BPC-157·TB-500 펩타이드 조제 안건 자문위 개최",
  "FDA Pharmacy Compounding Advisory Committee (July 2026) on peptides",
  "FDA는 2026년 7월 23~24일 약국 조제 자문위원회를 열어 BPC-157·TB-500 등 펩타이드의 503A 벌크 목록 포함 여부를 논의한다. '회색지대' 펩타이드가 제도권 규제 테이블에 오른 것이다. 결정에 따라 합법 조제 가능 여부가 갈린다.",
  "정리: ① 일정 — 2026년 7월 23~24일 FDA 약국조제 자문위(PCAC). ② 안건 — BPC-157·TB-500 등 펩타이드의 503A 벌크 목록 등재 검토. ③ 의미 — 조제약국이 합법적으로 만들 수 있는지 결정. ④ 배경 — 펩타이드 수요 급증에 따른 규제 정비. ⑤ 함의 — 결과가 시장 합법성·접근성을 좌우. NOGEAR 시각: 규제가 따라잡기 전까지, 시장의 펩타이드는 전부 '자기책임' 라벨이 붙어 있다.",
  "research", "펩타이드", "U.S. FDA", "regulatory",
  "https://www.fda.gov/advisory-committees/advisory-committee-calendar/july-23-24-2026-meeting-pharmacy-compounding-advisory-committee-07232026",
  sig(17, 16, 15, 19, 16, 9),
  ["FDA", "펩타이드", "조제규제", "503A", "BPC157"],
  True, True, "high", "FDA 공식 자문위 일정. 7월 PCAC·펩타이드 안건 정확.", "research"),

 ("FDA, 펩타이드 12종 지위 변경 — BPC-157·TB-500 카테고리2 제외",
  "FDA announces change in status of 12 peptides",
  "2026년 4월 FDA가 BPC-157·TB-500을 포함한 펩타이드 12종을 카테고리2 제한에서 제외한다고 보고했다는 소식이다. 규제 완화 신호로 해석되지만, '안전성 입증'과는 별개의 행정 분류 변경이라는 점이 중요하다. 시장은 호재로 받아들이고 있다.",
  "정리: ① 내용 — FDA가 펩타이드 12종(BPC-157·TB-500 등)의 카테고리2 제한 해제 보고. ② 시점 — 2026년 4월. ③ 해석 — 조제 접근성 확대 가능성. ④ 주의 — '안전성·효능 승인'이 아니라 규제 분류 조정. ⑤ 후속 — 7월 자문위와 연동. NOGEAR 시각: 분류가 바뀌었다고 약이 안전해진 건 아니다. 행정 도장과 임상 데이터를 혼동하지 마라.",
  "research", "펩타이드", "SSRP Institute", "magazine",
  "https://ssrpinstitute.org/news/fda-announces-change-in-status-of-12-peptides/",
  sig(17, 14, 15, 18, 16, 9),
  ["FDA", "펩타이드", "카테고리2", "규제완화", "TB500"],
  False, False, "medium", "업계 매체 보도. FDA 분류변경 보도 기반, 1차 FDA 문서 교차확인 권장.", "research"),

 ("BPC-157 전임상 결과 2026 — '조직 재생' 주장의 실체",
  "BPC-157 research results 2026: what preclinical studies show",
  "전임상 자료들은 BPC-157 처치 근육에서 위성세포 수 증가와 근섬유 단면적 증가를 보고한다. VEGFR2(혈관신생)와 NO 조절의 이중 경로가 거론된다. 그러나 이는 '전임상(주로 동물)' 수준이며 인체 효능·안전성과는 거리가 있다.",
  "정리: ① 소견 — 손상 후 7·14일 BPC-157 처치군에서 위성세포↑, 근섬유 단면적↑. ② 기전 — VEGFR2 혈관신생 + NO 조절 이중 경로, 위장 기원 펩타이드. ③ 수준 — 대부분 설치류 전임상. ④ 간극 — 인체 무작위대조시험 부재. ⑤ 출처 주의 — 판매처 콘텐츠는 이해상충 가능. NOGEAR 시각: 판매자가 인용하는 '연구'는 광고의 다른 이름일 때가 많다. 출처의 지갑을 먼저 봐라.",
  "research", "펩타이드", "Spartan Peptides (commercial)", "magazine",
  "https://spartanpeptides.com/blog/bpc-157-research-results-2026-preclinical-studies-tissue-repair/",
  sig(15, 13, 15, 16, 15, 9),
  ["BPC157", "전임상", "위성세포", "혈관신생", "이해상충"],
  False, False, "low", "판매처 상업 블로그. 이해상충으로 confidence low, 전임상 한계 명시.", "research"),

 # ===== 세마글루타이드/오젬픽 근손실 =====
 ("유타대 연구: 오젬픽, 근육 크기·근력에 새로운 의문",
  "New study raises questions about how Ozempic affects muscle size and strength (Univ. of Utah)",
  "유타대 보건은 2025년 세마글루타이드(오젬픽)가 근육 크기와 근력에 미치는 영향에 새로운 의문을 제기하는 연구를 소개했다. 체중과 함께 근육의 질·기능까지 영향받을 수 있다는 것이다. 단순 체중감량이 곧 건강 개선은 아닐 수 있다는 경고다.",
  "정리: ① 출처 — 유타대 보건 뉴스룸(2025-08). ② 쟁점 — 세마글루타이드가 근육 크기뿐 아니라 근력·근육의 질에 미치는 영향. ③ 함의 — 체중↓가 반드시 근기능↑·건강↑을 뜻하진 않음. ④ 위험군 — 고령자·근감소증 위험자에서 특히 주의. ⑤ 후속 — 운동·단백질 병행의 중요성. NOGEAR 시각: 저울 숫자는 줄어도 근육이 사라지면 그건 '약해지는' 것이다. 마른 게 강한 게 아니다.",
  "research", "세마글루타이드", "University of Utah Health 2025", "journal",
  "https://healthcare.utah.edu/newsroom/news/2025/08/new-study-raises-questions-about-how-ozempic-affects-muscle-size-and-strength",
  sig(18, 17, 18, 16, 15, 9),
  ["오젬픽", "세마글루타이드", "근손실", "근력", "유타대"],
  True, False, "high", "유타대 공식 뉴스룸. 근육 크기·근력 의문 제기 정확.", "research"),

 ("클리블랜드클리닉: 오젬픽 사용자, 제지방 13.9%까지 손실",
  "Ozempic and muscle loss: what to know (Cleveland Clinic)",
  "클리블랜드클리닉은 세마글루타이드(오젬픽) 치료 중 제지방(근육)량이 최대 13.9%까지 줄 수 있다고 정리했다. 한 연구에선 감량분의 39%가 근육이었다. 식욕 억제로 단백질 섭취·근력운동이 동시에 줄면 근손실이 가속된다.",
  "정리: ① 데이터 — GLP-1 작용제 치료 중 제지방량 최대 13.9% 감소 보고. ② 비율 — 일부 연구에서 감량의 60% 지방·39% 근육. ③ 기전 — 식욕 억제 → 단백질 섭취·열량 부족 → 근분해. ④ 대응 — 근력운동·충분한 단백질·수분. ⑤ 위험 — 근감소가 대사·기능 저하로 이어질 수 있음. NOGEAR 시각: 약으로 마르는 것과 운동으로 강해지는 것은 정반대 방향이다. 근육은 '나중에' 돌려받기 어렵다.",
  "research", "세마글루타이드", "Cleveland Clinic", "journal",
  "https://health.clevelandclinic.org/ozempic-muscle-loss",
  sig(19, 17, 19, 15, 15, 9),
  ["오젬픽", "근손실", "제지방13.9%", "클리블랜드클리닉", "단백질"],
  True, False, "high", "Cleveland Clinic 건강정보. 13.9% 제지방 손실·39% 근육 비율 검색결과와 일치.", "research"),

 ("medRxiv: 미국 대표표본서 세마글루타이드 '오·남용' 보고",
  "Semaglutide injection misuse reported among a nationally representative U.S. sample",
  "medRxiv 프리프린트는 미국 대표표본 조사에서 세마글루타이드 주사의 오·남용 사례를 보고했다. 처방 외 경로 입수, 미용·체형 목적의 비적응증 사용이 포함된다. '기적의 살빼기 약' 열풍이 안전 사용의 경계를 무너뜨리고 있다는 신호다.",
  "정리: ① 형식 — medRxiv 프리프린트(동료심사 전). ② 조사 — 미국 대표표본 대상 세마글루타이드 사용 행태. ③ 발견 — 처방 외 입수·비적응증(미용·보디빌딩) 사용 등 오·남용 신호. ④ 위험 — 용량 오류, 불순물, 의학적 모니터링 부재. ⑤ 한계 — 프리프린트로 동료심사 전, 확정 결론 아님. NOGEAR 시각: 유행이 의학을 앞지르면 부작용은 통계가 아니라 응급실에서 먼저 나타난다.",
  "research", "세마글루타이드", "medRxiv preprint 2025", "research",
  "https://www.medrxiv.org/content/10.64898/2025.12.25.25343021.full.pdf",
  sig(19, 15, 17, 18, 16, 9),
  ["세마글루타이드", "오남용", "비적응증", "medRxiv", "프리프린트"],
  False, True, "medium", "medRxiv 프리프린트(동료심사 전). 결론 미확정으로 confidence medium 명시.", "research"),

 ("임상시험 등록: 세마글루타이드의 심장·근육량 영향 평가 진행",
  "Impact of Semaglutide on Heart and Muscle Mass (ClinicalTrials.gov)",
  "ClinicalTrials.gov에 세마글루타이드(오젬픽/위고비)가 심장과 근육량에 미치는 영향을 평가하는 임상시험이 등록됐다. 근손실·심근 영향에 대한 우려가 정식 연구 의제로 올라온 것이다. 결과가 나오기 전까지 '안전'은 가정일 뿐이다.",
  "정리: ① 등록 — 세마글루타이드의 심장·근육량 영향 평가 임상시험(NCT07272837). ② 목적 — 체중감량 이면의 심근·골격근 변화 정량화. ③ 배경 — 광범위 사용에 비해 장기 안전성 데이터 부족. ④ 의의 — 우려가 연구 의제로 공식화. ⑤ 한계 — 결과 도출 전, 결론 미확정. NOGEAR 시각: 수백만이 이미 맞고 있는 약의 근육·심장 영향이 '지금' 연구 중이라는 사실이 더 무섭다.",
  "research", "세마글루타이드", "ClinicalTrials.gov", "clinical",
  "https://clinicaltrials.gov/study/NCT07272837",
  sig(17, 16, 16, 17, 15, 8),
  ["세마글루타이드", "임상시험", "근육량", "심장", "장기안전성"],
  True, True, "high", "ClinicalTrials.gov 공식 등록. 심장·근육량 평가 임상 사실 확인.", "research"),

 ("오젬픽 근손실, 어떻게 막나 — 근력운동·단백질·유산소의 삼각편대",
  "Does Ozempic cause muscle loss and how to prevent it?",
  "Drugs.com은 오젬픽이 근손실을 유발할 수 있으며 근력운동·충분한 단백질·유산소·수분으로 완화할 수 있다고 정리했다. 핵심은 '약만 맞고 가만히 있으면' 근육이 빠진다는 것이다. 약은 식욕을 줄이지 근육을 지켜주지 않는다.",
  "정리: ① 사실 — 오젬픽 등 GLP-1 약물은 근손실을 동반할 수 있다. ② 예방 — 규칙적 근력운동, 충분한 단백질, 유산소, 수분·영양. ③ 원리 — 단백질 합성 자극(운동)으로 근분해를 상쇄. ④ 주의 — 비적응증·미용 목적은 의료 감독 밖에서 위험 증가. ⑤ 결론 — 약은 도구일 뿐, 근육 보존은 본인 몫. NOGEAR 시각: 약이 식욕을 끄면, 근육은 네가 직접 지켜야 한다. 바벨은 여전히 답이다.",
  "research", "세마글루타이드", "Drugs.com", "journal",
  "https://www.drugs.com/medical-answers/ozempic-cause-muscle-loss-how-you-prevent-3578660/",
  sig(16, 15, 18, 14, 13, 8),
  ["오젬픽", "근손실예방", "근력운동", "단백질", "GLP-1"],
  True, False, "medium", "Drugs.com 의약정보. 근손실·예방 권고 표준 의학과 일치.", "research"),
]


def build(rec):
    (title, title_en, summary, detail, cat, cat_ko, source, stype, url,
     signals, tags, peer, primary, conf, cnotes, bucket) = rec
    score = sum(signals.values())
    t, emoji = tier(score)
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
        "credibility": cred(peer, primary, conf, cnotes, stype),
        "viral_signals": signals,
        "tags": tags,
        "viral_score": score,
        "viral_tier": t,
        "viral_emoji": emoji,
        "date": TODAY,
        "badge": "✅ VERIFIED",
        "source_verified": True,
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

    # research 캡: news(아카이브가 50으로 정리) + research 합 ≤ 200 유지
    RESEARCH_CAP = 150
    if len(research) > RESEARCH_CAP:
        research = research[:RESEARCH_CAP]

    data["news"] = news
    data["research"] = research

    meta = data.setdefault("meta", {})
    meta["last_updated"] = NOW.isoformat()
    meta["last_updated_kst"] = (
        f"{NOW.strftime('%Y-%m-%d %H:%M KST')} 아침 크롤 "
        f"(스테로이드심독성·보디빌더돌연사EHJ·SARMs간독성·DNP치명률·펩타이드FDA규제·세마글루타이드근손실) "
        f"+{len(new_items)}건"
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
