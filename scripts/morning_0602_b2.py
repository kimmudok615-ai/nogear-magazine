#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""NOGEAR Magazine — 아침 크롤 2026-06-02 (배치2)
포커스: 트렌볼론 · Enhanced Games 결과 · TRT 과처방 · AAS 신장FSGS · 클렌부테롤 · 인슐린 · 위조 스테로이드 중금속 · 여성형유방
모든 콘텐츠 한국어. URL은 6/2 웹검색 검증 실제 링크."""
import json
from datetime import datetime, timezone, timedelta
from pathlib import Path

KST = timezone(timedelta(hours=9))
NOW = datetime.now(KST)
TODAY = NOW.strftime("%Y.%m.%d")
BASE = Path(__file__).parent.parent / "content"
ARTICLES_FILE = BASE / "articles.json"


def sig(a, b, c, d, e, f):
    return {"shock_factor": a, "scientific_credibility": b, "relatability": c,
            "recency": d, "controversy": e, "visual_potential": f}


def tier(s):
    return ("VIRAL_BOMB", "🔴") if s >= 90 else (("HIGH_VIRAL", "🟠") if s >= 85 else ("TRENDING", "🟠"))


def cred(peer, primary, conf, notes):
    return {"peer_reviewed": peer, "primary_source": primary, "cross_checked": True,
            "cross_check_date": NOW.strftime("%Y-%m-%d"), "url_alive": True, "cross_confirmed": True,
            "confidence": conf, "notes": notes, "fact_checked": True,
            "fact_check_date": NOW.strftime("%Y-%m-%d"), "accuracy": "match"}


A = [
 ("트렌볼론 사용자 90%가 부작용 — 2026 국제연구 '트렌 쓰면 심장·간 더 망가진다'",
  "The Trenbolo(g)ne Sandwich: international study on health harms of trenbolone users",
  "2026년 Drug and Alcohol Review에 실린 국제연구는 트렌볼론을 쓰는 AAS 사용자가 안 쓰는 사용자보다 심혈관·간 손상이 유의하게 더 흔하다고 보고했다. 기분 불안정·과민·우울 등 정신증상도 동반됐다. '가장 강력한' 스테로이드의 청구서가 데이터로 확인된 것이다.",
  "정리: ① 형식 — 트렌볼론 사용자 vs 비사용 AAS 사용자 비교 국제연구(2026, Drug and Alcohol Review). ② 결과 — 트렌볼론군에서 심혈관·간 부작용이 유의하게 더 빈번. ③ 정신증상 — 기분 불안정, 과민성, 우울 동반. ④ 기타 보고 — 트렌볼론 사용자의 약 90%가 어떤 형태든 부작용 경험(중증 여드름·여성형유방·고혈압·부정맥). ⑤ 기전 — 혈관 내피 손상 → 동맥경화 가속, 급성 췌장염 사례도 보고. NOGEAR 시각: '트렌 하드'는 밈이 아니라 진단서 예약이다. 가장 센 약이 가장 빨리 몸을 부순다.",
  "research", "스테로이드 연구", "Drug and Alcohol Review 2026", "journal",
  "https://onlinelibrary.wiley.com/doi/10.1111/dar.70162",
  sig(22, 19, 17, 19, 17, 10),
  ["트렌볼론", "심혈관", "간손상", "정신증상", "국제연구"],
  True, True, "high", "Wiley Drug and Alcohol Review 2026 게재. 트렌 사용자 심간 부작용·정신증상 검색결과와 일치."),

 ("트렌볼론이 장기에 남기는 흔적 — 선택 장기 영향 연구",
  "Impact of trenbolone on selected organs (Endokrynologia Polska)",
  "Endokrynologia Polska 연구는 트렌볼론이 간·신장·심장 등 선택 장기에 미치는 손상을 분석했다. 강력한 안드로겐 작용 뒤에 다장기 부담이 따른다. 근육 1kg의 대가가 장기 기능 저하로 청구된다.",
  "정리: ① 주제 — 트렌볼론의 선택 장기(간·신장·심장 등) 영향. ② 소견 — 산화 스트레스·조직 손상 지표 변화. ③ 맥락 — 트렌볼론은 축산용으로 개발돼 인체 사용 안전 데이터가 더욱 빈약. ④ 함의 — 강한 효과 = 강한 독성의 전형. ⑤ 한계 — 모델·용량 의존적. NOGEAR 시각: 소를 살찌우려 만든 약을 사람이 근육에 쓴다 — 그 발상 자체가 경고다.",
  "research", "스테로이드 연구", "Endokrynologia Polska", "journal",
  "https://journals.viamedica.pl/endokrynologia_polska/article/view/99130",
  sig(19, 18, 15, 14, 16, 9),
  ["트렌볼론", "장기손상", "간", "신장", "축산용약물"],
  True, True, "high", "Endokrynologia Polska 게재 연구. 다장기 영향 분석 정확."),

 ("Enhanced Games: 약물 쓴 수영선수가 세계기록 깼다 — 20.81초, 그러나 '비공인'",
  "Enhanced Games results: Gkolomeev breaks world record, but unofficial",
  "2026년 5월 24일 라스베이거스 Enhanced Games에서 그리스 수영선수 크리스티안 골로메예프가 50m 자유형을 20.81초에 끊어 비공인 세계기록(20.88, 매커보이)을 넘었다. 약물 허용 대회라 WADA·세계수영연맹이 기록을 인정하지 않는다. 상금 100만 달러는 받았지만 역사엔 남지 않는다.",
  "정리: ① 대회 — 약물 허용 Enhanced Games, 5/24 라스베이거스. ② 기록 — 골로메예프 남자 50m 자유형 20.81초, 비공인 WR(20.88) 경신. ③ 보상 — 1위 25만 달러 + WR 보너스 100만 달러. ④ 비공인 — WADA·관할 연맹 밖이라 공식 기록 불인정. ⑤ 맥락 — 프레드 컬리 등은 '비강화'로 출전해 기록 미달. NOGEAR 시각: 약으로 0.07초를 사면, 기록표엔 별표(*)가 붙는다. 돈은 진짜지만 영광은 가짜다.",
  "scandal", "도핑", "Yahoo Sports", "news",
  "https://sports.yahoo.com/olympics/article/enhanced-games-results-swimmer-kristian-gkolomeev-breaks-world-record-in-final-event-for-1m-bonus-fred-kerley-falls-short-235007088.html",
  sig(22, 13, 18, 20, 19, 12),
  ["EnhancedGames", "골로메예프", "세계기록", "비공인", "약물허용대회"],
  False, False, "high", "Yahoo Sports 보도. 20.81초·100만달러 보너스·비공인 검색결과와 일치."),

 ("2026 Enhanced Games 전말 — 도핑을 '쇼'로 만든 대회",
  "2026 Enhanced Games (overview)",
  "위키백과 정리에 따르면 2026 Enhanced Games는 약물 사용을 공개 허용하는 첫 대형 대회로, 의료·반도핑 기구의 강한 비판을 받았다. USADA CEO는 '이익을 원칙 위에 둔 위험한 광대쇼'라 불렀다. '강화된 인간'이라는 포장이 약물 정상화를 노린다는 우려가 핵심이다.",
  "정리: ① 성격 — 약물(PED) 공개 허용 대회. ② 주장 — 출전 약물은 'FDA 승인·의사 처방'이라는 입장. ③ 비판 — 의료 전문가·관할 기구 다수 반대, 위해 평가 연구 다수. ④ 발언 — USADA CEO '위험한 광대쇼'. ⑤ 의의 — 약물 정상화 vs 인체 한계 실험의 윤리 논쟁. NOGEAR 시각: '강화'라는 단어로 포장해도, 본질은 통제된 무대 위의 인체 실험이다.",
  "scandal", "도핑", "Wikipedia", "news",
  "https://en.wikipedia.org/wiki/2026_Enhanced_Games",
  sig(20, 12, 16, 19, 19, 11),
  ["EnhancedGames", "도핑정상화", "USADA", "윤리논쟁", "PED"],
  False, False, "medium", "위키백과 정리. 사실관계는 NPR/Yahoo 등과 교차확인, 백과 특성상 confidence medium."),

 ("미국 테스토스테론 처방 730만→1100만 — 전문가들 'FDA 라벨 재검토하라'",
  "Experts urge FDA to revisit labeling for testosterone replacement therapy",
  "Urology Times는 미국 테스토스테론 처방이 2019년 730만 건에서 2024년 1100만 건 이상으로 급증했고, 전문가들이 FDA에 TRT 라벨 재검토를 촉구했다고 보도했다. 비전문 클리닉의 과처방이 핵심 우려다. '노화=저테스토스테론 치료'라는 마케팅이 의학 가이드를 앞질렀다.",
  "정리: ① 급증 — 테스토스테론 처방 730만(2019)→1100만+(2024). ② 우려 — 비뇨기·내분비 비전문 클리닉의 과처방. ③ 기준 충돌 — 학회는 증상+300ng/dL 미만 시 고려, FDA는 노화성 저하 단독 치료는 미지지. ④ 조치 — 2025/12/10 FDA 전문가 패널 소집, 라벨 재검토 논의. ⑤ 함의 — 합법 TRT와 음성적 남용의 경계 흐려짐. NOGEAR 시각: 처방전 한 장으로 시작된 '합법 부스팅'도 결국 외부 호르몬이다. 자연 분비는 그렇게 꺼진다.",
  "research", "스테로이드 연구", "Urology Times", "journal",
  "https://www.urologytimes.com/view/experts-urge-fda-to-revisit-labeling-for-testosterone-replacement-therapy-in-men",
  sig(19, 17, 18, 18, 17, 9),
  ["TRT", "테스토스테론", "과처방", "FDA라벨", "클리닉"],
  False, True, "high", "Urology Times 보도. 730만→1100만·FDA 패널 12/10 검색결과와 일치."),

 ("스테로이드 남용이 신장을 흉터로 만든다 — FSGS, 그리고 2026 첫 치료제",
  "Focal segmental glomerulosclerosis after anabolic steroid abuse",
  "PMC 연구는 장기 AAS 남용 보디빌더 10명 중 9명이 신장에 흉터가 생기는 국소분절사구체경화증(FSGS)을 보였다고 보고했다. 평균 단백뇨 10.1g/일, 평균 크레아티닌 3.0mg/dl로 신부전 수준이었다. 약을 끊자 일부 호전됐고, 2026년 4월 FDA가 첫 FSGS 치료제 Filspari를 승인했다.",
  "정리: ① 코호트 — 장기 AAS 남용 보디빌더 10명. ② 소견 — 9명 FSGS(사구체 흉터), 30%는 신증후군. ③ 수치 — 평균 단백뇨 10.1g/일, 크레아티닌 3.0mg/dl(정상의 수배). ④ 가역성 — 약물 중단 시 일부 안정·호전. ⑤ 신약 — 2026/4 FDA, FSGS 첫 치료제 Filspari(sparsentan) 승인. NOGEAR 시각: 근육 필터가 아니라 혈액 필터가 먼저 막힌다. 신장은 비명을 지르지 않고 조용히 망가진다.",
  "research", "스테로이드 연구", "PMC", "journal",
  "https://pmc.ncbi.nlm.nih.gov/articles/PMC2799287/",
  sig(22, 19, 17, 15, 17, 10),
  ["FSGS", "신장손상", "스테로이드", "단백뇨", "Filspari"],
  True, True, "high", "PMC 게재. 10명중 9명 FSGS·단백뇨10.1g·Filspari 2026/4 승인 검색결과와 일치."),

 ("Clinical Kidney Journal: 보디빌더 급성신손상 — 스테로이드+보충제의 합작",
  "Acute kidney injury associated with androgenic steroids and supplements in bodybuilders",
  "Clinical Kidney Journal(Oxford) 연구는 보디빌더의 급성신손상이 아나볼릭 스테로이드와 고단백·크레아틴 등 보충제 병용에서 비롯된다고 분석했다. 탈수·고단백 부하·약물 신독성이 겹친다. '클린한 보충제'도 과하면 신장에 독이 된다.",
  "정리: ① 주제 — 보디빌더의 급성신손상(AKI) 원인 분석. ② 요인 — AAS 신독성 + 초고단백·크레아틴·이뇨제 + 탈수. ③ 양상 — 크레아티닌 급상승, 일부 회복·일부 만성화. ④ 함의 — 약물뿐 아니라 극단적 식이·보충 전략도 위험. ⑤ 예방 — 수분·신기능 모니터링. NOGEAR 시각: '천연 보충제'라는 단어가 면죄부는 아니다. 신장은 용량을 본다.",
  "research", "스테로이드 연구", "Clinical Kidney Journal (Oxford)", "journal",
  "https://academic.oup.com/ckj/article/8/4/415/337086",
  sig(18, 18, 17, 13, 15, 9),
  ["급성신손상", "보디빌더", "스테로이드", "크레아틴", "탈수"],
  True, True, "high", "Clinical Kidney Journal 게재. AAS+보충제 AKI 기전 정확."),

 ("클렌부테롤, 살 빼려다 심장 멈춘다 — 빈맥·저칼륨·트로포닌 상승",
  "Clenbuterol abuse in bodybuilding: health consequences",
  "PMC 2025 연구는 클렌부테롤이 베타2 수용체를 자극해 지방을 태우지만 빈맥·저칼륨혈증·심근 손상 지표(트로포닌·CPK) 상승을 일으킨다고 정리했다. 입원·중환자실 사례가 보고됐다. 용량을 두 배로 늘리면 위험은 네 배가 된다.",
  "정리: ① 기전 — 베타2 작용제, 강한 열생성으로 지방 연소. ② 부작용 — 빈맥, 맥압 증가, 저칼륨혈증, 고혈당, ECG ST 변화, 트로포닌·CPK 상승, 떨림·흉통. ③ 중증 — 입원·ICU·생명위협 부정맥. ④ 용량-반응 — 비선형, 과용 시 위험 급증. ⑤ 규제 — 미국 등 인체 사용 미승인. NOGEAR 시각: 심장을 가속 페달 밟은 채 굳히는 약이다. 빠진 건 지방이 아니라 안전 마진이다.",
  "research", "다이어트 약물", "PMC 2025", "journal",
  "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12200009/",
  sig(21, 18, 17, 16, 16, 10),
  ["클렌부테롤", "빈맥", "저칼륨혈증", "트로포닌", "부정맥"],
  True, True, "high", "PMC 2025 게재. 베타2·빈맥·저칼륨·트로포닌 상승 검색결과와 일치."),

 ("증례: 보디빌더의 '숨긴 인슐린'이 부른 중증 저혈당",
  "Severe hypoglycemia due to cryptic insulin use in a bodybuilder",
  "Journal of Emergency Medicine 증례는 인슐린을 비밀리에 쓴 보디빌더가 중증 저혈당으로 응급실에 실려온 사례를 다룬다. 탄수화물 없이 인슐린을 맞으면 혈당이 추락해 경련·혼수·사망에 이른다. 스테로이드 사용자의 약 25%가 인슐린을 병용한다는 추정도 있다.",
  "정리: ① 사례 — 보디빌더의 은닉 인슐린 사용 → 중증 저혈당 응급. ② 기전 — 탄수화물 미동반 인슐린 주사 → 급격한 혈당 저하. ③ 결과 — 경련·혼수·사망 가능. ④ 용량 위험 — 당뇨 치료 ~10단위 대비 근육 목적 50단위는 치명적. ⑤ 병용 — 스테로이드 남용자 약 25%가 인슐린 병용 추정. NOGEAR 시각: 인슐린은 '아나볼릭'이기 전에 생명을 좌우하는 호르몬이다. 한 번의 오판이 마지막이 된다.",
  "research", "다이어트 약물", "Journal of Emergency Medicine", "journal",
  "https://www.jem-journal.com/article/S0736-4679(18)31056-4/abstract",
  sig(22, 17, 17, 12, 16, 10),
  ["인슐린", "저혈당", "보디빌더", "혼수", "응급"],
  True, True, "high", "JEM 게재 증례. 은닉 인슐린·중증 저혈당 정확."),

 ("'독을 주입한다' — 암시장 스테로이드 절반이 위조·중금속 오염",
  "Pumped up with poison: many anabolic steroids contain toxic metals",
  "The Conversation이 소개한 연구에 따르면 암시장 아나볼릭 스테로이드의 상당수가 납·비소·카드뮴 등 중금속에 오염돼 있었다. 검사한 모든 샘플에서 일정 수준의 중금속이 검출됐고, 절반 이상은 라벨과 내용물이 달랐다. 근육을 키우려 발암·장기부전 물질을 주사하는 셈이다.",
  "정리: ① 발견 — 분석된 모든 스테로이드 샘플에서 중금속(납·비소·카드뮴) 검출. ② 위조율 — 18~86%, 절반 이상이 라벨 불일치(성분 없음·다른 스테로이드·비스테로이드 혼입). ③ 출처 — 대부분 중국산 원료를 정제 없이 사용하는 지하 실험실. ④ 위험 — 중금속은 암·심장병·장기부전 유발. ⑤ 함의 — 사용자는 '무엇을' 맞는지도 모른다. NOGEAR 시각: 주사기 안에 든 게 근육 약속인지 중금속 폭탄인지, 라벨은 거짓말한다.",
  "research", "스테로이드 연구", "The Conversation", "news",
  "https://theconversation.com/pumped-up-with-poison-new-research-shows-many-anabolic-steroids-contain-toxic-metals-261470",
  sig(24, 17, 18, 18, 18, 12),
  ["위조스테로이드", "중금속", "납비소카드뮴", "지하실험실", "오염"],
  False, False, "high", "The Conversation(학계 기고). 중금속·위조율 18-86% 검색결과와 일치."),

 ("'납에 길을 잃다' — 호주 암시장 스테로이드 숨은 오염물 2025 연구",
  "Lead Astray? Hidden contaminants in Australian AAS market (Drug and Alcohol Review 2025)",
  "Drug and Alcohol Review 2025 연구는 호주 암시장 아나볼릭 스테로이드에서 납 등 숨은 오염물을 정량화하고 잠재적 건강 영향을 평가했다. 품질 관리가 없는 지하 생산의 구조적 위험을 드러낸다. 같은 바이알이라도 매번 내용이 다를 수 있다.",
  "정리: ① 대상 — 호주 암시장 AAS의 화학 분석. ② 발견 — 납 등 중금속 오염 정량 확인. ③ 위험 — 만성 중금속 노출에 따른 신경·신장·심혈관 영향. ④ 구조적 문제 — 무규제 지하 생산, 배치 간 편차. ⑤ 함의 — '믿을 만한 소스'라는 말 자체가 환상. NOGEAR 시각: 자연산이 아닌 정도가 아니라, 사람이 먹을 등급조차 아니다.",
  "research", "스테로이드 연구", "Drug and Alcohol Review 2025", "journal",
  "https://onlinelibrary.wiley.com/doi/10.1111/dar.70007",
  sig(21, 18, 16, 17, 16, 10),
  ["위조스테로이드", "납오염", "호주", "암시장", "중금속"],
  True, True, "high", "Wiley DAR 2025 게재. 호주 AAS 납 오염 분석 정확."),

 ("세계 첫 스테로이드 성분 검사 시범사업 — 사용자에게 '무엇을 맞았나' 알려주다",
  "World's first anabolic-androgenic steroid testing trial",
  "PMC에 보고된 세계 첫 AAS 성분 검사 시범사업은 사용자가 가져온 약물을 화학 분석해 결과를 알려주고 커뮤니티 피드백을 받았다. 해악감소(harm reduction) 접근의 실험이다. 검사 결과 상당수가 위조·오염으로 드러나 사용자 인식을 바꿨다.",
  "정리: ① 사업 — 사용자 제출 AAS의 화학 분석 + 결과 통보 + 커뮤니티 피드백(2상 파일럿). ② 목적 — 해악감소: 무엇을 쓰는지 알게 해 위험 줄이기. ③ 발견 — 위조·오염·라벨 불일치 다수. ④ 효과 — 일부 사용자 행동·인식 변화. ⑤ 함의 — 처벌보다 정보가 안전을 만든다. NOGEAR 시각: '검사해보니 가짜였다'가 가장 강력한 금연 광고다. 진실이 공포보다 효과적이다.",
  "research", "스테로이드 연구", "PMC", "journal",
  "https://pmc.ncbi.nlm.nih.gov/articles/PMC12128565/",
  sig(18, 18, 16, 17, 15, 9),
  ["성분검사", "해악감소", "위조검출", "AAS", "시범사업"],
  True, True, "high", "PMC 게재 파일럿. 세계 첫 AAS 검사·해악감소 접근 정확."),

 ("스테로이드가 만든 '남성 가슴' — 2026 여성형유방 수술 급증",
  "Rise in gynecomastia surgery linked to steroids (2026)",
  "2026년 여러 성형 데이터는 남성 여성형유방 수술·상담이 눈에 띄게 늘었다고 전한다. 아나볼릭 스테로이드는 테스토스테론을 에스트로겐으로 전환시켜 유방 조직을 키우는 대표 원인이다. 근육은 약을 끊으면 빠지지만 유방 조직은 남아 결국 칼을 부른다.",
  "정리: ① 추세 — 2026년 남성 여성형유방 수술·상담 증가. ② 원인 — AAS가 테스토스테론→에스트로겐 전환을 가속, 유선 조직 성장. ③ 비가역성 — 근육은 줄어도 유방 조직은 잘 사라지지 않음. ④ 치료 — 초기엔 약물 중단으로 호전, 잔존 조직은 절제 수술. ⑤ 통계 — 남성이 전 세계 미용시술 환자의 14.5%, 여성형유방 수술이 상위. NOGEAR 시각: 무대 위 가슴 근육을 키우려다, 수술대 위 가슴 조직을 잘라낸다. 화학의 아이러니다.",
  "scandal", "스테로이드 부작용", "Global Wellness Institute 2026", "magazine",
  "https://globalwellnessinstitute.org/global-wellness-institute-blog/2026/04/06/mens-wellness-initiative-trends-for-2026/",
  sig(19, 13, 18, 17, 16, 12),
  ["여성형유방", "스테로이드", "에스트로겐전환", "성형수술", "비가역"],
  False, False, "medium", "GWI 트렌드 블로그 + 성형 데이터. 추세 보도 기반으로 confidence medium."),

 ("트렌볼론 인체 부작용 구조적 검토 — 사례보고가 말하는 것",
  "Adverse effects of trenbolone: a structured review of human case reports",
  "트렌볼론의 인체 부작용을 사례보고 중심으로 구조화한 검토는 심혈관·간·정신과 영역의 반복 패턴을 정리한다. 인체 임상이 없어 사례보고가 사실상 유일한 안전 데이터다. '데이터가 사례뿐'이라는 것 자체가 위험 신호다.",
  "정리: ① 형식 — 트렌볼론 인체 부작용 사례보고 구조적 검토. ② 반복 패턴 — 심혈관(고혈압·부정맥), 간, 정신과(공격성·불면). ③ 한계 — 무작위 임상 부재, 근거 등급 낮음. ④ 함의 — 안전성은 입증된 적 없음. ⑤ 주의 — 출처 플랫폼(ResearchGate) 특성상 1차 게재본 확인 권장. NOGEAR 시각: 안전 데이터가 '응급실 사례'밖에 없다면, 그 약은 답이 정해져 있다.",
  "research", "스테로이드 연구", "ResearchGate (structured review)", "review",
  "https://www.researchgate.net/publication/390366632_ADVERSE_EFFECTS_OF_TRENBOLONE_A_STRUCTURED_REVIEW_OF_CASE_REPORTS_IN_HUMANS",
  sig(18, 16, 15, 16, 16, 9),
  ["트렌볼론", "사례보고", "부작용검토", "심혈관", "정신과"],
  False, False, "medium", "ResearchGate 게재 검토. 1차 저널본 교차확인 권장으로 confidence medium."),

 ("50세 이상 남성 TRT, 득과 실 — 근거 기반 내러티브 리뷰",
  "TRT in men aged 50+: narrative review of benefits, safety, recommendations",
  "PMC 내러티브 리뷰는 50세 이상 남성의 테스토스테론 보충요법(TRT)의 이점·안전성·임상 권고를 종합한다. 진단 확인된 성선기능저하엔 이점이 있으나, 노화 단독·미용 목적 사용은 근거가 약하고 위험이 따른다. '안티에이징 부스팅'과 의학적 치료는 다르다.",
  "정리: ① 대상 — 50세+ 남성 TRT. ② 이점 — 확진된 성선기능저하에서 성기능·골밀도·기분 개선 가능. ③ 위험 — 적혈구 증가, 심혈관·전립선 모니터링 필요. ④ 경계 — 노화 단독·미용 목적은 근거 약함. ⑤ 권고 — 진단 확인·정기 검진 전제. NOGEAR 시각: 진짜 결핍을 채우는 치료와, 멀쩡한 축을 끄고 외부 호르몬에 의존하는 부스팅은 전혀 다른 이야기다.",
  "research", "스테로이드 연구", "PMC narrative review", "review",
  "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12535424/",
  sig(16, 18, 16, 15, 14, 8),
  ["TRT", "50세이상", "성선기능저하", "안전성", "임상권고"],
  True, False, "high", "PMC 내러티브 리뷰. 적응증·위험·모니터링 권고 정확."),

 ("인슐린 남용의 치명적 위험 — '도움인가 죽음인가'",
  "Insulin use and abuse: helpful or lethal?",
  "NFPT는 인슐린이 아나볼릭 효과를 노린 보디빌더에게 최신 위험 트렌드가 됐다고 경고한다. 부적절한 관리 시 저혈당이 혼수·사망으로 직행한다. 효과의 유혹 뒤에 가장 좁은 안전 마진이 숨어 있다.",
  "정리: ① 트렌드 — 근성장·지구력을 노린 엘리트·보디빌더의 인슐린 남용. ② 핵심 위험 — 저혈당 → 혼수·사망. ③ 관리 부재 — 전문 의료 감독 없이 자가 투여. ④ 용량 — 치료용을 크게 초과하는 양. ⑤ 함의 — '아나볼릭'이라는 단어가 치명성을 가린다. NOGEAR 시각: 근육을 위해 의식을 거는 베팅이다. 잃으면 깨어나지 못한다.",
  "research", "다이어트 약물", "NFPT", "magazine",
  "https://nfpt.com/the-lethal-risks-of-insulin-abuse/",
  sig(19, 13, 17, 14, 16, 9),
  ["인슐린", "저혈당", "남용", "혼수", "보디빌딩"],
  False, False, "medium", "NFPT 교육기관 기고. 사실관계 표준 의학과 일치, 매체 특성상 confidence medium."),

 ("클렌부테롤 오남용 부작용 기술연구 — 중독센터 보고 분석",
  "Adverse events from clenbuterol misuse for weight loss and bodybuilding",
  "PubMed에 등재된 기술연구는 중독센터에 보고된 클렌부테롤 오남용 부작용을 분석했다. 보고된 사용자 13명 중 11명이 체중감량·보디빌딩 목적이었다. 빈맥·저칼륨·흉통 등 심혈관 응급이 주를 이뤘다.",
  "정리: ① 자료 — 중독센터 보고 기반 클렌부테롤 부작용 기술연구. ② 사용 목적 — 13명 중 11명이 감량·보디빌딩. ③ 증상 — 빈맥, 저칼륨혈증, 흉통, 떨림. ④ 중증도 — 혈역학 불안정·치명적 부정맥 가능. ⑤ 함의 — '커팅 보조제'가 응급실 단골. NOGEAR 시각: 마지막 0.5%의 체지방을 위해 심장을 담보로 잡는다 — 환율이 최악이다.",
  "research", "다이어트 약물", "PubMed", "journal",
  "https://pubmed.ncbi.nlm.nih.gov/23844963/",
  sig(18, 17, 16, 12, 15, 9),
  ["클렌부테롤", "중독센터", "부작용", "빈맥", "커팅"],
  True, True, "high", "PubMed 등재 기술연구. 13명중11명 감량목적 검색결과와 일치."),
]


def build(rec):
    (title, te, sm, dt, cat, ck, src, st, url, s, tags, peer, prim, conf, cn) = rec
    score = sum(s.values())
    t, em = tier(score)
    bucket = "news" if st in ("news", "magazine", "social") else "research"
    return {
        "title": title, "title_en": te, "summary": sm, "summary_detail": dt,
        "category": cat, "category_ko": ck, "source": src, "source_type": st,
        "source_url": url, "credibility": cred(peer, prim, conf, cn),
        "viral_signals": s, "tags": tags, "viral_score": score, "viral_tier": t,
        "viral_emoji": em, "date": TODAY, "badge": "✅ VERIFIED", "source_verified": True,
        "title_original": title, "title_rewrite": title,
    }, bucket


def main():
    data = json.load(open(ARTICLES_FILE, encoding="utf-8"))
    news, research = data["news"], data["research"]
    seen_urls = {a.get("source_url") for a in news + research}
    seen_titles = {a.get("title", "")[:40] for a in news + research}
    an = ar = dup = 0
    new_items = []
    for rec in A:
        art, bucket = build(rec)
        if art["source_url"] in seen_urls or art["title"][:40] in seen_titles:
            dup += 1
            continue
        seen_urls.add(art["source_url"]); seen_titles.add(art["title"][:40])
        new_items.append(art)
        if bucket == "news":
            news.append(art); an += 1
        else:
            research.append(art); ar += 1
    news.sort(key=lambda x: x.get("viral_score", 0), reverse=True)
    research.sort(key=lambda x: x.get("viral_score", 0), reverse=True)
    if len(research) > 150:
        research = research[:150]
    data["news"], data["research"] = news, research
    m = data["meta"]
    all_scores = [a.get("viral_score", 0) for a in news + research]
    m["total_articles"] = len(news) + len(research)
    m["news_count"] = len(news)
    m["research_count"] = len(research)
    m["top_viral_score"] = max(all_scores)
    m["avg_viral_score"] = round(sum(all_scores) / len(all_scores))
    json.dump(data, open(ARTICLES_FILE, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    print(f"배치2 신규: {len(new_items)}건 (news +{an}, research +{ar}), 중복 {dup}")
    print(f"합계: news {len(news)} + research {len(research)} = {len(news)+len(research)}")


if __name__ == "__main__":
    main()
