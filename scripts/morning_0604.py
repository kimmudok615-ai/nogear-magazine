#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""NOGEAR Magazine — 2026-06-04 아침 크롤 빌더.
정직 모드: 신규 기사는 미검증(cross_confirmed=False)으로 저장. crosscheck 단계가 검증.
중복 = source_url 기준 스킵. viral_score = 6개 시그널 합. 내림차순 정렬, 최대 200 유지.
"""
import json
import os
from datetime import datetime, timezone, timedelta

KST = timezone(timedelta(hours=9))
TODAY = "2026.06.04"
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ARTICLES = os.path.join(ROOT, "content", "articles.json")


def tier(score):
    if score >= 90:
        return "VIRAL_BOMB", "🔴"
    if score >= 85:
        return "HIGH_VIRAL", "🟠"
    return "TRENDING", "🟠"


def cred(peer, primary, conf, notes):
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
#  url, peer, primary, conf, notes, [shock, sci, relat, recency, contro, visual], tags, title_rewrite)
RAW = [
    # ===== ENHANCED GAMES (2026.05.24 라스베이거스) =====
    (
        "'약물 올림픽' 인핸스드 게임 결과 — 22종목 중 세계기록 단 1개, 클린 선수가 우승 3개 쓸어담아",
        "Enhanced Games results: only 1 world record in 22 events, clean athletes won 3",
        "약물 사용을 전면 허용한 인핸스드 게임이 5월 24일 라스베이거스에서 열렸다. 5시간 22종목 동안 세계기록은 단 1개만 깨졌고, 오히려 약물을 쓰지 않은 '클린' 선수 3명이 우승을 가져갔다. 무제한 도핑이 인간 한계를 폭발시킬 거라던 주최 측의 서사는 무대 위에서 스스로 무너졌다.",
        "정리: ① 행사 — 인핸스드 게임, 2026년 5월 24일 라스베이거스, 도핑 검사 없음·의료 감독 하 PED 허용. ② 결과 — 22개 종목·5시간 중 세계기록은 단 1건. ③ 반전 — Fred Kerley(100m 9.97), Tristan Evelyn(여자 100m 11.25), Hunter Armstrong(50m 배영 24.21) 등 클린 선수 3명이 우승. ④ 함의 — '약물=무조건 더 빠르다'는 단순 등식이 실제 경기장에서 성립하지 않았다. ⑤ 맥락 — 약물은 회복·근량을 밀어올리지만 신경근 협응·기술·재능을 대체하지 못한다. NOGEAR 시각: 화학으로 채운 무대에서, 깨끗한 몸이 1등을 했다. 이게 올해 가장 통쾌한 헤드라인이다.",
        "scandal", "사건·업계", "Front Office Sports / GearJunkie 2026-05", "news",
        "https://frontofficesports.com/clean-athletes-stole-the-show-at-the-enhanced-games/",
        False, False, "high",
        "인핸스드 게임 5/24 라스베이거스 개최, 22종목 중 세계기록 1개, 클린 선수 3명 우승은 복수 매체 일치. 종목별 기록 수치는 cross-check 단계 재확인 필요.",
        [22, 12, 16, 20, 20, 14],
        ["인핸스드게임", "약물올림픽", "클린선수", "도핑", "라스베이거스"],
        "약물 다 허용한 무대에서 깨끗한 몸이 1등 했다 — 22종목 중 세계기록은 단 1개",
    ),
    (
        "그콜로메예프 50m 자유형 20.81 — 인핸스드 게임 유일한 '세계기록', $100만 보너스 챙겼지만 공인 안 돼",
        "Gkolomeev swims 50m free in 20.81 at Enhanced Games for $1M bonus — record not recognized",
        "그리스 수영선수 크리스티안 그콜로메예프가 인핸스드 게임에서 50m 자유형을 20.81초에 끊으며 공식 세계기록(20.88초)을 0.07초 앞당겼다. 100만 달러 보너스를 받았지만, 도핑 검사가 없는 대회라 이 기록은 공인되지 않는다. 약물로 만든 0.07초가 '진짜'냐는 논쟁이 다시 불붙었다.",
        "정리: ① 인물 — 크리스티안 그콜로메예프(그리스, 수영). ② 기록 — 50m 자유형 20.81초, 캐머런 매커보이의 공식 세계기록 20.88초를 0.07초 경신. ③ 보상 — 세계기록 보너스 100만 달러 수령. ④ 단서 — 인핸스드 게임은 WADA 비공인·도핑 검사 부재로 기록 인정 불가. ⑤ 약리 — PED는 회복·파워·체성분을 개선하나, 0.07초 단축이 약물 단독 효과인지 분리 불가능. NOGEAR 시각: 별표 달린 세계기록. 약통 옆에 세워둔 트로피는 트로피인가, 영수증인가.",
        "scandal", "사건·업계", "Yahoo Sports 2026-05", "news",
        "https://sports.yahoo.com/olympics/article/enhanced-games-results-swimmer-kristian-gkolomeev-breaks-world-record-in-final-event-for-1m-bonus-fred-kerley-falls-short-235007088.html",
        False, False, "high",
        "그콜로메예프 50m 자유형 20.81초·100만달러 보너스·비공인은 야후스포츠 보도. 종전 기록 보유자(매커보이 20.88) 수치 cross-check 필요.",
        [18, 11, 15, 20, 18, 14],
        ["그콜로메예프", "세계기록", "인핸스드게임", "수영", "비공인기록"],
        "별표 달린 세계기록 — 약물 허용 대회 50m 20.81초, $100만 받았지만 공인은 안 됨",
    ),
    (
        "인핸스드 게임 출전자 91%가 테스토스테론·79%가 성장호르몬 — '의사 처방'이라는 면죄부",
        "91% of Enhanced Games athletes used testosterone, 79% used HGH — under 'doctor's prescription'",
        "인핸스드 게임 출전 선수의 91%가 테스토스테론(또는 에스터)을, 79%가 성장호르몬을, 62%가 애더럴 등 각성제를 사용했다고 주최 측이 밝혔다. 'FDA 승인·의사 처방'을 안전장치로 내세웠지만, 초생리학적 용량의 만성 사용은 임상 처방과 전혀 다른 위험 프로파일을 갖는다. WADA·IOC·USADA가 일제히 '위험한 광대쇼'라 비난했다.",
        "정리: ① 사용률 — 테스토스테론 91%, HGH 79%, 각성제(애더럴 등) 62%. ② 주최 논리 — 모두 FDA 승인 약물·의사 처방·의료 감독. ③ 반론 — 경기력 향상 목적의 초생리학적 용량은 치료 용량과 위험이 다르다(심근비대·혈전·이상지질혈증·HPG축 억제). ④ 규제권 반응 — USADA CEO 타이가트 '이익을 원칙 위에 둔 위험한 광대쇼', IOC '우리가 지키는 모든 것에 대한 배신', WADA '미 당국이 중단시켜야'. ⑤ 함의 — '처방'이라는 단어가 만성 고용량 사용의 장기 위험을 지우지 못한다. NOGEAR 시각: 처방전은 알리바이가 아니다. 심장은 서류를 읽지 않는다.",
        "scandal", "사건·업계", "Wikipedia: 2026 Enhanced Games / NPR 2026-05", "news",
        "https://en.wikipedia.org/wiki/2026_Enhanced_Games",
        False, False, "medium",
        "사용률 91/79/62% 및 규제기관 비난 발언은 NPR·위키 정리 기반. 위키는 2차 출처로 cross-check 단계에서 1차(주최 발표) 확인 필요.",
        [20, 10, 14, 19, 20, 12],
        ["인핸스드게임", "테스토스테론", "성장호르몬", "도핑통계", "처방"],
        "출전자 91%가 테스토스테론 — '의사 처방'이라는 면죄부, 그러나 심장은 서류를 안 읽는다",
    ),
    (
        "하프토르 비요른손, 인핸스드 게임 데드리프트 475kg — '산'은 들었지만 화제는 약물이었다",
        "Hafthor Bjornsson deadlifts 475kg at Enhanced Games",
        "아이슬란드 스트롱맨 하프토르 비요른손이 인핸스드 게임 데드리프트에서 475kg을 들어올렸다. 압도적 퍼포먼스였지만, 약물 허용 대회라는 맥락이 모든 숫자에 별표를 붙였다. 무제한 도핑 환경에서의 '괴력'이 스포츠인지 약리 실험인지 묻는 목소리가 커졌다.",
        "정리: ① 인물 — 하프토르 비요른손(아이슬란드, 전 세계 최강자·왕좌의 게임 '산'). ② 기록 — 인핸스드 게임 데드리프트 475kg 우승. ③ 맥락 — 도핑 검사 없는 대회, 91%가 테스토스테론 사용 환경. ④ 쟁점 — 약물 허용 하의 최대근력 기록을 어떻게 해석할 것인가. ⑤ 약리 — 안드로겐·HGH·인슐린 조합은 근단면적·회복을 극대화하나 심혈관·연부조직 부하도 함께 키운다. NOGEAR 시각: 475kg은 진짜다. 문제는 그 옆에 뭐가 있었느냐다.",
        "scandal", "사건·업계", "GearJunkie / Front Office Sports 2026-05", "news",
        "https://gearjunkie.com/health-fitness/shocking-results-drug-olympics-enhanced-games",
        False, False, "medium",
        "비요른손 475kg 데드리프트 우승은 기어정키 보도. 정확한 중량·종목 조건 cross-check 필요.",
        [16, 9, 14, 18, 16, 15],
        ["하프토르비요른손", "데드리프트", "스트롱맨", "인핸스드게임", "475kg"],
        "'산'이 475kg을 들었다 — 그러나 화제가 된 건 무게가 아니라 약물이었다",
    ),
    # ===== TRENBOLONE 신경독성 =====
    (
        "트렌볼론, 뇌를 갉아먹는다 — 인간 사례보고 구조적 리뷰: 혈뇌장벽 통과·신경 위축",
        "Adverse effects of trenbolone: a structured review of human case reports",
        "보디빌딩계 '강심장' 약물 트렌볼론이 혈뇌장벽을 쉽게 통과해 뇌 피질을 손상시킨다는 인간 사례보고 구조적 리뷰가 나왔다. 신경 위축, NMDA 수용체 밀도 감소, 베타-아밀로이드 같은 신경독성 단백질 축적이 보고됐다. 기억력 저하·공격성·충동성으로 이어지는 기전이다.",
        "정리: ① 대상 — 트렌볼론 인간 부작용 사례보고 구조적 리뷰. ② 신경 기전 — 혈뇌장벽 통과 → 피질 무결성 손상 → 신경세포 위축, NMDA 수용체 밀도 감소, 베타-아밀로이드 축적. ③ 임상 양상 — 기억력 저하, 공격성, 충동성 등 인지·행동 결손. ④ 맥락 — 트렌볼론은 본래 가축 성장 촉진용 환경호르몬으로도 분류. ⑤ 함의 — 근육을 키우는 동안 뇌가 조용히 위축될 수 있다. NOGEAR 시각: '트렌 분노'는 밈이 아니라 신경병리다. 거울 속 근육이 커질 때, 거울을 보는 뇌가 줄어든다.",
        "research", "스테로이드 연구", "ResearchGate 구조적 리뷰", "research",
        "https://www.researchgate.net/publication/390366632_ADVERSE_EFFECTS_OF_TRENBOLONE_A_STRUCTURED_REVIEW_OF_CASE_REPORTS_IN_HUMANS",
        False, False, "medium",
        "트렌볼론 혈뇌장벽 통과·신경독성·베타아밀로이드 축적 주장은 리뷰 요약 기반. 동료심사 여부·원저 1차 데이터 cross-check 필요(ResearchGate 호스팅).",
        [20, 12, 15, 17, 18, 12],
        ["트렌볼론", "신경독성", "혈뇌장벽", "베타아밀로이드", "공격성"],
        "근육이 커지는 동안 뇌가 줄어든다 — 트렌볼론, 혈뇌장벽 뚫고 신경 갉아먹어",
    ),
    (
        "트렌볼론 쓸수록 더 공격적 — AAS 사용자 282명 연구: 용량 높을수록 언어폭력↑",
        "Trenbolone, psychological distress and aggression in 282 male AAS users",
        "AAS 사용 남성 282명을 분석한 연구에서, 트렌볼론 용량이 높을수록 언어적 공격성이 유의하게 증가했다. 연령·BMI를 보정해도 관계가 유지됐고, 현재 사용자의 33% 이상이 트렌볼론을 쓰고 있었다. '트렌 분노'에 처음으로 인간 용량-반응 데이터가 붙었다.",
        "정리: ① 표본 — AAS 사용 남성 282명, 현재 사용자 중 33%+ 가 트렌볼론 사용. ② 결과 — 트렌볼론 용량과 언어적 공격성 사이 유의한 양의 상관(연령·BMI 보정 후 유지). ③ 의의 — 동물 모델을 넘어 인간 용량-반응 신호 제시. ④ 한계 — 단면연구·자가보고 기반으로 인과 단정 불가. ⑤ 기전 — 안드로겐 수용체·세로토닌계·편도체 변화가 충동·공격 조절에 관여. NOGEAR 시각: '원래 성격'이라 둘러대지만, 데이터는 주사기에서 분노가 새어나온다고 말한다.",
        "research", "스테로이드 연구", "International Journal of Drug Policy 2024", "research",
        "https://www.sciencedirect.com/science/article/pii/S0955395924003207",
        False, False, "high",
        "282명·트렌볼론 용량-언어공격성 상관·33% 사용은 IJDP 게재 연구. 단면연구 한계 명시. cross-check 단계 원문 수치 확인 권장.",
        [19, 13, 16, 16, 19, 11],
        ["트렌볼론", "공격성", "AAS연구", "용량반응", "트렌분노"],
        "'트렌 분노'에 데이터가 붙었다 — 282명 연구, 용량 높을수록 언어폭력 증가",
    ),
    (
        "17β-트렌볼론, 스트레스 받으면 우울까지 — 혈뇌장벽 누수·신경염증으로 우울행동 악화",
        "17β-trenbolone drives depressive tendencies via BBB leakage and neuroinflammation",
        "2025년 동물 연구에서 17β-트렌볼론이 사회적 스트레스 조건에서 우울 유사 행동을 악화시키는 것으로 나타났다. 혈뇌장벽 누수, 신경염증, 세포외기질 매개 시냅스 기능장애가 기전으로 지목됐다. 트렌볼론이 공격성뿐 아니라 우울에도 관여할 수 있다는 신호다.",
        "정리: ① 모델 — 만성 사회패배 스트레스(CSDS) 유발 마우스. ② 결과 — 17β-트렌볼론이 골수 유래 MMP8을 증가시키고 사회적 위협에 대한 우울 경향을 강화. ③ 기전 — 혈뇌장벽 누수 → 신경염증 → 세포외기질 매개 시냅스 기능장애. ④ 함의 — 트렌볼론의 정신과적 영향이 공격성을 넘어 우울 스펙트럼까지 확장. ⑤ 한계 — 동물 모델, 인간 외삽 신중. NOGEAR 시각: 무대 위 자신감 뒤, 무대 뒤 어둠. 같은 분자가 둘 다 만든다.",
        "research", "스테로이드 연구", "Science of the Total Environment 2025", "research",
        "https://www.sciencedirect.com/science/article/abs/pii/S0013935125019851",
        False, False, "medium",
        "17β-트렌볼론·CSDS·MMP8·우울행동은 2025 동물연구 요약 기반. 동물 모델 한계. 저널·DOI cross-check 필요.",
        [17, 12, 14, 18, 16, 11],
        ["트렌볼론", "우울", "신경염증", "혈뇌장벽", "동물연구"],
        "트렌볼론은 분노만이 아니다 — 스트레스 받으면 우울행동까지, 뇌 염증이 매개",
    ),
    # ===== COUNTERFEIT / 위조 =====
    (
        "세계 최초 암시장 스테로이드 화학검사 시범사업 — 검사 샘플 13%가 '라벨과 다른 물질'",
        "World's first AAS testing trial: 13% of samples contained substances different from expected",
        "암시장 아나볼릭 스테로이드를 직접 화학분석한 세계 최초 시범사업 결과가 공개됐다. 호주 약물검사 서비스에서 분석된 AAS 샘플의 13%가 라벨과 다른 물질을 함유했다. 사용자가 '뭘 주사하는지' 자체를 모르는 현실이 데이터로 확인됐다.",
        "정리: ① 사업 — 화학분석+결과 공유+커뮤니티 피드백 2단계 파일럿(세계 최초 AAS 검사 시범). ② 표본 — 2024년 4/19~6/7 제출 32샘플 중 23개 분석. ③ 결과 — 분석 AAS 23개 중 13%가 예상과 다른 성분 검출. ④ 위험 — 라벨 오기·무성분·타성분·과소/과다 함량은 용량 통제를 불가능하게 만든다. ⑤ 추가 위험 — 무허가 실험실 제품은 미생물 품질관리 부재로 농양·괴사 위험. NOGEAR 시각: '믿을 만한 소스'라는 말은 신앙이지 데이터가 아니다. 바이알 안엔 뭐든 들어있을 수 있다.",
        "research", "스테로이드 연구", "Drug Testing and Analysis 2025 (PMC12128565)", "research",
        "https://pmc.ncbi.nlm.nih.gov/articles/PMC12128565/",
        True, True, "high",
        "세계 최초 AAS 검사 파일럿·23샘플·13% 불일치는 PMC 게재. 동료심사·1차 데이터. 표본 소수 한계 명시.",
        [18, 13, 16, 18, 16, 11],
        ["위조스테로이드", "약물검사", "암시장", "품질관리", "오염"],
        "'믿을 만한 소스'는 신앙이다 — 세계 첫 암시장 스테로이드 검사, 13%가 라벨과 다른 물질",
    ),
    (
        "암시장 스테로이드 36%가 위조 — 메타분석: 추가 37%는 '품질 미달'",
        "Fake AAS on the black market: meta-analysis finds 36% counterfeit",
        "암시장 아나볼릭 스테로이드를 다룬 체계적 문헌고찰·메타분석에서, 평균 36%가 위조품이고 추가 37%가 품질 미달로 추정됐다. 즉 시중 제품의 다수가 라벨대로가 아니다. 용량을 계산해 쓴다는 보디빌더의 전제 자체가 흔들린다.",
        "정리: ① 분석 — 암시장 위조 AAS 정성·정량 분석 결과의 체계적 고찰·메타분석. ② 추정치 — 위조 36%(95% CI 29–43), 품질 미달 추가 37%(95% CI 17–63). ③ 함의 — 라벨 신뢰 불가, 실제 투여 용량을 사용자가 알 수 없음. ④ 임상 위험 — 과다 함량 시 독성, 무성분 시 효과 없음·반복 투여 유도. ⑤ 맥락 — 클란데스틴 랩 제품은 멸균·정량 보증 없음. NOGEAR 시각: 숫자를 세며 사이클을 짠다? 그 숫자가 거짓일 확률이 1/3을 넘는다.",
        "research", "스테로이드 연구", "Systematic Review & Meta-analysis (PMC9288681)", "research",
        "https://pmc.ncbi.nlm.nih.gov/articles/PMC9288681/",
        True, True, "high",
        "위조 36%·품질미달 37% 추정치는 PMC 메타분석. CI 넓음(특히 품질미달) 명시. 동료심사·1차.",
        [17, 13, 15, 15, 16, 10],
        ["위조스테로이드", "메타분석", "암시장", "품질미달", "용량"],
        "시중 스테로이드 1/3 이상이 가짜 — 메타분석 36% 위조 + 37% 품질미달",
    ),
    (
        "보충제 속 불법 SARM, 고체상 분석으로 즉시 검출 — 무허가 제품 단속 새 무기",
        "Rapid detection of illegal SARMs in unregistered supplements",
        "무허가 보충제에 숨은 불법 SARM을 고체상 분석법 조합으로 신속 검출하는 연구가 발표됐다. '천연 보충제'를 표방한 제품에서 SARM이 검출되는 사례가 끊이지 않는 가운데, 규제·단속의 분석 도구가 진화하고 있다. 소비자는 라벨에 없는 약물을 모르고 먹을 수 있다.",
        "정리: ① 방법 — 선택된 고체상 분석법 조합으로 무허가 보충제 내 불법 SARM 신속 검출. ② 배경 — '천연·합법' 표방 보충제에 SARM이 비표시 혼입되는 사례. ③ 의의 — 빠른 스크리닝으로 단속·소비자 보호 가능. ④ 위험 — 소비자가 라벨에 없는 강력한 안드로겐 작용 물질을 모르고 섭취 → 간손상·테스토스테론 억제·도핑 양성. ⑤ 맥락 — SARM은 임상 데이터가 빈약하고 고용량 자가사용 위험 큼. NOGEAR 시각: '천연'이라 적힌 통 안에 약이 들었다. 라벨은 마케팅이지 성분표가 아니다.",
        "research", "스테로이드 연구", "Analytical study (PMC12205930)", "research",
        "https://pmc.ncbi.nlm.nih.gov/articles/PMC12205930/",
        True, True, "medium",
        "무허가 보충제 내 SARM 고체상 신속검출은 PMC 게재 분석연구. 방법론 중심. cross-check 단계 적용 범위 확인.",
        [15, 12, 14, 16, 15, 10],
        ["SARM", "보충제오염", "비표시혼입", "분석화학", "단속"],
        "'천연' 보충제 통 안에 약이 들었다 — 불법 SARM, 신속 검출 기술로 잡아낸다",
    ),
    # ===== TRT 클리닉 사기 =====
    (
        "게임데이 멘즈헬스 소송 — '필요 없는 남성에게 TRT 팔았다' 청구·집단소송·규제 진정 동시",
        "Gameday Men's Health lawsuit: billing fraud and deceptive TRT marketing alleged",
        "미국 TRT 체인 게임데이 멘즈헬스가 청구 사기, 기만적 테스토스테론 마케팅, 의료과실 의혹으로 소송에 휩싸였다. 의학적으로 TRT가 필요 없는 남성에게 위험을 축소하고 라이프스타일 광고로 권유했다는 주장이다. 개별 소송·집단소송·규제 진정이 2026년 현재 동시 진행 중이다.",
        "정리: ① 대상 — 게임데이 멘즈헬스(전국 다수 지점). ② 의혹 — 청구 사기, 기만적 TRT 마케팅, 부적절·미감독 처방, 무단 구독 등록. ③ 진행 — 개별 소송·집단소송·규제 진정 병행(2026 기준). ④ 산업 맥락 — TRT 클리닉 소비자 불만이 2021년 대비 60%+ 증가. ⑤ 위험 — 불필요한 외인성 테스토스테론은 적혈구증가·혈전·심혈관 위험·자체 생산 억제. NOGEAR 시각: '활력 회복' 광고 뒤엔 평생 주사 구독이 숨어 있다. 의료가 아니라 구독경제다.",
        "scandal", "사건·업계", "Lawfold 2026", "news",
        "https://lawfold.com/gameday-mens-health-lawsuit/",
        False, False, "medium",
        "게임데이 멘즈헬스 소송·청구사기·집단소송은 법률정보 사이트 보도. 1차 소장·법원 기록 cross-check 필요(법률 마케팅 사이트 출처 주의).",
        [16, 10, 16, 17, 18, 10],
        ["TRT", "게임데이멘즈헬스", "소송", "청구사기", "남성호르몬"],
        "'활력 회복' 광고의 정체는 평생 주사 구독 — 게임데이 TRT 클리닉 사기 소송",
    ),
    (
        "에이지리스 멘즈헬스, 메디케어·트라이케어 사기청구로 160만 달러 합의",
        "Ageless Men's Health pays $1.6M in False Claims Act settlement",
        "테네시 기반 TRT 클리닉 에이지리스 멘즈헬스가 메디케어·트라이케어에 의학적으로 불필요한 남성호르몬 치료를 사기 청구한 혐의로 160만 달러를 합의금으로 냈다. 미 보건복지부·법무부가 표적으로 삼은 사건이다. TRT 산업의 '과잉 처방' 구조가 공적 자금까지 갉아먹었다.",
        "정리: ① 대상 — 에이지리스 멘즈헬스(테네시). ② 혐의 — 의학적으로 불필요한 남성호르몬 치료를 메디케어·트라이케어에 사기 청구(허위청구법 위반). ③ 결과 — 160만 달러 합의. ④ 주체 — 미 HHS·DOJ. ⑤ 함의 — TRT 과잉 처방이 개인 건강을 넘어 공보험 재정 문제로 확장. NOGEAR 시각: 필요 없는 호르몬을 팔면 환자도 잃고 세금도 샌다. 합의금 160만 달러는 그 청구서다.",
        "scandal", "사건·업계", "Berger Montague 2026", "news",
        "https://bergermontague.com/testosterone-clinic-ageless-mens-health-pays-1-6-million-false-claims-act-settlement/",
        False, False, "high",
        "에이지리스 160만달러 허위청구법 합의·HHS/DOJ는 로펌 발표. 합의 금액·기관 cross-check 권장.",
        [15, 11, 14, 16, 17, 9],
        ["TRT", "에이지리스", "허위청구", "메디케어", "합의금"],
        "필요 없는 호르몬 팔면 세금도 샌다 — 에이지리스 TRT 클리닉 $160만 사기청구 합의",
    ),
    (
        "테스토스테론 처방 의사 상대 소송 25년치 분석 — 심장마비·뇌졸중·암 청구 급증",
        "Testosterone therapy lawsuits against prescribers: a 2000–2024 legal review",
        "2000~2024년 테스토스테론 치료 처방의를 상대로 한 소송을 분석한 법의학 리뷰가 나왔다. 심장마비·뇌졸중·암을 주장하는 청구가 늘고 있으며, '위험 고지 실패'가 핵심 쟁점이다. TRT의 의학적 정당성과 동의 절차가 법정에서 시험대에 올랐다.",
        "정리: ① 대상 — 2000~2024년 테스토스테론 처방의 상대 소송 사례 법적 리뷰. ② 청구 사유 — 심혈관 사건(심장마비·뇌졸중), 암, 위험 고지 실패. ③ 핵심 쟁점 — 적응증 없는 처방·불충분한 위험 설명·미흡한 모니터링. ④ 산업 맥락 — TRT 상업화·직접광고 확대와 소송 증가가 동행. ⑤ 임상 함의 — 처방 전 적응증 확인·심혈관 위험 평가·문서화된 동의 필요. NOGEAR 시각: 호르몬은 처방전 한 장으로 끝나지 않는다. 청구서는 몇 년 뒤 법정에서 날아온다.",
        "research", "스테로이드 연구", "PubMed legal case review 2024 (40753505)", "research",
        "https://pubmed.ncbi.nlm.nih.gov/40753505/",
        True, False, "medium",
        "2000-2024 TRT 처방의 소송 리뷰는 PubMed 색인. 법적 리뷰 성격(임상 RCT 아님) 명시. 원문 결론 cross-check 필요.",
        [14, 12, 13, 15, 16, 9],
        ["TRT", "소송", "위험고지", "심혈관", "법의학"],
        "TRT 처방, 몇 년 뒤 법정 청구서로 돌아온다 — 25년치 처방의 소송 분석",
    ),
    # ===== INSULIN =====
    (
        "보디빌더의 '숨은 인슐린' 중증 저혈당 사례 — 10분이면 코마, 가장 위험한 PED",
        "Severe hypoglycemia due to cryptic insulin use in a bodybuilder",
        "근성장 목적으로 인슐린을 쓴 보디빌더의 중증 저혈당 사례가 보고됐다. 인슐린은 비당뇨인에게 단 한 번의 용량 실수로 저혈당·코마·사망을 부를 수 있는, 보디빌딩에서 가장 위험한 약물로 꼽힌다. 치료 용량 10단위 대비 50단위 주사는 분 단위로 치명적일 수 있다.",
        "정리: ① 사례 — 인슐린을 아나볼릭 목적으로 사용한 보디빌더의 중증 저혈당(은폐된 인슐린 사용). ② 기전 — 외인성 인슐린이 혈당을 급격히 떨어뜨려 신경당결핍 → 혼란·의식소실·발작·코마. ③ 용량 위험 — 당뇨 치료 통상 ~10단위/일 대비 50단위 주사는 저혈당·코마·사망 유발 가능. ④ 시간 — 미처치 시 분 단위로 치명적. ⑤ 맥락 — 인슐린은 영양소 흡수·근글리코겐을 늘리지만 안전역이 극도로 좁다. NOGEAR 시각: 스테로이드는 몇 년에 걸쳐 죽인다. 인슐린은 그날 오후에 죽일 수 있다.",
        "research", "스테로이드 연구", "Am J Emerg Med (PubMed 30527564)", "research",
        "https://pubmed.ncbi.nlm.nih.gov/30527564/",
        True, True, "high",
        "보디빌더 은폐 인슐린 사용 중증 저혈당은 응급의학지 증례. 동료심사·1차. 용량 비교 수치는 일반 임상 상식과 일치.",
        [21, 13, 15, 15, 16, 11],
        ["인슐린", "저혈당", "코마", "PED", "증례보고"],
        "스테로이드는 몇 년에 걸쳐 죽이지만 인슐린은 그날 오후에 죽인다 — 보디빌더 중증 저혈당 증례",
    ),
    (
        "인슐린 남용, 도움인가 흉기인가 — 좁은 안전역·저혈당 사망의 해부학",
        "Insulin use and abuse in bodybuilding: helpful or lethal?",
        "보디빌딩계 인슐린 남용의 위험을 정리한 전문가 분석이다. 인슐린은 근육 영양소 흡수를 늘려 '동화'를 노리지만, 안전역이 극히 좁아 작은 실수가 치명적 저혈당으로 직결된다. 어지럼·혼란·극심한 피로·의식소실이 수 분 내 진행될 수 있다.",
        "정리: ① 사용 동기 — 인슐린의 동화 효과(글루코스·아미노산 근육 유입 촉진)로 근성장·회복 기대. ② 핵심 위험 — 극도로 좁은 치료-독성 간격, 용량 오류 시 중증 저혈당. ③ 증상 — 어지럼·혼란·피로·의식소실, 심하면 수 분 내 사망 가능. ④ 가중 요인 — 공복·운동·알코올·타 약물 병용이 저혈당 심화. ⑤ 함의 — '동화'를 얻으려다 가장 빠른 사망 경로를 연다. NOGEAR 시각: 인슐린은 약이 아니라 칼날 위 곡예다. 떨어지면 두 번 기회가 없다.",
        "research", "스테로이드 연구", "NFPT 전문가 분석", "research",
        "https://nfpt.com/the-lethal-risks-of-insulin-abuse/",
        False, False, "medium",
        "NFPT 인슐린 남용 위험 분석은 비동료심사 전문가 콘텐츠. 기전·증상은 임상 상식과 일치하나 1차 연구 아님(과거 크롤서 NFPT 中신뢰 분류 이력).",
        [16, 9, 14, 14, 15, 10],
        ["인슐린", "남용", "저혈당", "안전역", "동화작용"],
        "인슐린은 약이 아니라 칼날 위 곡예 — 떨어지면 두 번째 기회가 없다",
    ),
    # ===== HGH / PALUMBOISM =====
    (
        "복부비대증후군(팔룸보이즘) 병태생리 리뷰 — HGH·인슐린이 만든 '버블 거트'의 정체",
        "Abdominal Hypertrophy Syndrome: characteristics and potential pathophysiology",
        "팔룸보이즘(일명 HGH 거트·버블 거트)의 특징과 잠재적 병태생리를 정리한 문헌 리뷰가 나왔다. 성장호르몬·인슐린·아나볼릭 제제의 장기 사용이 마른 근육질 몸에 비정상적으로 부푼 복부를 만든다. 정확한 기전은 아직 규명되지 않았지만 심근병증으로 인한 심부전 가능성까지 지적된다.",
        "정리: ① 정의 — 복부비대증후군(스테로이드 거트/팔룸보이즘), 보디빌더에서 GH·인슐린·아나볼릭 장기 사용과 연관된 드문 상태. ② 양상 — 마른 근육질 체형에 비정상적으로 팽창한 복부. ③ 가설 기전 — GH 과다 → 장기(내장) 비대, 소화관 운동 저하, 복부 근육량 증가 복합. ④ 연구 상태 — 2024년 리뷰가 특징·병태생리 정리, 정확한 기전 미규명. ⑤ 위험 — 심근병증 → 심부전으로 치명적일 수 있음. NOGEAR 시각: 식스팩 위로 부푼 배. 그건 '벌크'가 아니라 장기가 커진 흔적이다.",
        "research", "스테로이드 연구", "Abdominal Hypertrophy Syndrome review (PubMed 39569303)", "research",
        "https://pubmed.ncbi.nlm.nih.gov/39569303/",
        True, False, "medium",
        "복부비대증후군 특징·병태생리 리뷰는 PubMed 색인 2024 리뷰. 기전은 가설 수준임을 명시. cross-check 단계 결론 확인.",
        [18, 12, 15, 15, 16, 14],
        ["팔룸보이즘", "HGH거트", "성장호르몬", "버블거트", "심근병증"],
        "식스팩 위 부푼 배는 '벌크'가 아니다 — 장기가 커진 흔적, 팔룸보이즘 병태생리 리뷰",
    ),
    (
        "팔룸보이즘은 치명적일 수 있다 — HGH 거트, 심근병증 통한 심부전 경로",
        "Palumboism aka HGH gut: a potentially fatal side-effect of HGH",
        "성장호르몬 남용의 부작용인 팔룸보이즘(HGH 거트)이 단순 외형 문제가 아니라 치명적일 수 있다는 분석이다. 데이브 팔룸보의 이름에서 유래한 이 상태는 마른 몸에 부푼 복부가 특징이다. 같은 HGH·인슐린 조합이 심근에도 작용해 심근병증·심부전으로 이어질 수 있다.",
        "정리: ① 명칭 유래 — 데이브 팔룸보(처음 뚜렷이 진단된 보디빌더). ② 양상 — 잦은 HGH+인슐린 사용으로 마른 근육질 체형에 비정상 팽창 복부. ③ 기전 — GH 과다가 소화계 운동 저하·내장 비대 유발. ④ 치명성 — 심근병증으로 인한 심혈관 부전 가능성. ⑤ 예방 — 본질적으로 GH 남용 중단이 유일한 근본 대응. NOGEAR 시각: 무대 위에서 배가 나온 '괴물'들. 그 배 안에서 심장도 함께 두꺼워지고 있다.",
        "research", "스테로이드 연구", "Gilmore Health News", "research",
        "https://www.gilmorehealth.com/palumboism-a-potentially-fatal-side-effect-of-human-growth-hormone/",
        False, False, "low",
        "팔룸보이즘 치명성·심근병증 연결은 건강매체 해설로 비동료심사. 외형 정의는 일반 합의, 사망 기전은 PubMed 39569303 등으로 보강 필요.",
        [16, 8, 14, 13, 15, 13],
        ["팔룸보이즘", "HGH거트", "심근병증", "성장호르몬", "심부전"],
        "무대 위 부푼 배 속에서 심장도 두꺼워진다 — 팔룸보이즘, 치명적일 수 있다",
    ),
    # ===== WOMEN / 비릴화 =====
    (
        "여성 스테로이드의 비가역적 대가 — 굵어진 목소리·체모·턱선은 되돌아오지 않는다",
        "Irreversible virilization: what women face from anabolic steroids",
        "여성의 아나볼릭 스테로이드 사용은 목소리 저음화, 얼굴 체모, 음핵 비대, 생리 변화 같은 비릴화(남성화)를 일으키며 상당수는 비가역적이다. 약을 끊어도 굵어진 성대와 변한 골격은 돌아오지 않는다. '여성용 약하다는 스테로이드'에도 안전한 선은 없다.",
        "정리: ① 증상 — 음성 저음화, 얼굴·몸 체모 증가, 음핵 비대, 생리 변화, 탈모. ② 비가역성 — 성대·골격·체모 변화는 중단 후에도 회복되지 않는 경우 다수. ③ 약물별 위험 — 아나바·윈스트롤 등은 비릴화 위험, 윈스트롤은 간손상도. ④ 기전 — 외인성 안드로겐이 안드로겐 수용체를 과활성화해 남성형 2차 성징 유발. ⑤ 함의 — '여성 친화적' 스테로이드라는 마케팅에도 안전 용량은 없다. NOGEAR 시각: 근육은 사이클이 끝나면 빠진다. 목소리는 평생 남는다. 거래가 공평하지 않다.",
        "research", "스테로이드 연구", "Women's experiences of AAS (PMC8632252)", "research",
        "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8632252/",
        True, False, "medium",
        "여성 AAS 비릴화·비가역성은 PMC 질적연구 및 임상 합의 기반. 개별 약물 위험 서술은 일반 임상지식. cross-check 단계 1차 인용 확인.",
        [17, 11, 16, 14, 16, 12],
        ["여성스테로이드", "비릴화", "남성화", "비가역성", "음성변화"],
        "근육은 사이클 끝나면 빠지지만 목소리는 평생 남는다 — 여성 스테로이드 비가역 비릴화",
    ),
    (
        "여성 AAS 사용, 젠더 관점에서 다시 보다 — '남성 데이터'로 만든 가이드의 사각지대",
        "Gendered perspectives on women's anabolic-androgenic steroid use",
        "여성의 아나볼릭 스테로이드 사용 실태를 젠더 관점에서 분석한 연구다. 기존 위해감소 전략이 남성 데이터에 기반해 여성 특유의 위험·경험을 놓친다는 지적이 핵심이다. 비릴화·생식 영향 등 여성 고유의 결과에 맞춘 접근이 필요하다는 결론이다.",
        "정리: ① 주제 — 여성 AAS 사용 실태·동기·경험의 젠더 분석. ② 문제의식 — 위해감소·임상 가이드가 대부분 남성 표본 기반 → 여성 위험 과소평가. ③ 여성 특이 위험 — 비릴화(다수 비가역), 생리·생식 영향, 사회적 낙인. ④ 제언 — 젠더 민감형 위해감소 접근(여성 특유 필요·경험 반영). ⑤ 맥락 — 여성 사용 증가에도 연구·임상 인프라는 남성 중심. NOGEAR 시각: 가이드라인이 남자만 보고 쓰였다. 그 사이 여성의 몸은 다른 청구서를 받는다.",
        "research", "스테로이드 연구", "Gendered perspectives on women's AAS (PMC10127974)", "research",
        "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10127974/",
        True, False, "medium",
        "여성 AAS 젠더 관점·위해감소 사각지대는 PMC 질적연구. 정성 분석 성격. cross-check 단계 결론 확인.",
        [14, 12, 15, 14, 15, 9],
        ["여성AAS", "젠더", "위해감소", "비릴화", "사각지대"],
        "가이드라인은 남자만 보고 쓰였다 — 여성의 몸은 다른 청구서를 받는다",
    ),
    # ===== ADOLESCENT =====
    (
        "청소년 스테로이드, 여전히 거기 있다 — 19세 이하 유병률 2.5%, 신체 불만족이 입구",
        "Adolescent steroid use persists: 2.5% prevalence in under-19s",
        "전 생애 AAS 사용 메타분석에서 19세 이하 청소년 유병률이 2.5%로 나타났다. 남성 청소년은 4~12%, 여성은 0.5~2% 범위로 보고된다. 신체 이미지 불만족, 보충제 오남용, 동반 약물 사용이 입구 역할을 한다는 점이 반복 확인됐다.",
        "정리: ① 유병률 — 생애 메타분석상 19세 이하 2.5%, 남성 청소년 4~12%·여성 0.5~2%. ② 위험 요인 — 신체 이미지 불만족, 근육강화 보충제 오용, 동반 물질 사용. ③ 지속성 — 중·고교·대학 연령 코호트에서 AAS 노출 지속 확인(최근 자료 업데이트). ④ 함의 — 성장기 노출은 골단 조기 폐쇄·호르몬축 교란 등 장기 영향 우려. ⑤ 예방 — 신체 이미지·보충제 문화 개입이 핵심. NOGEAR 시각: 어른들이 만든 '약 쓰는 몸'을 십대가 따라 그린다. 입구는 거울 앞 불만족이다.",
        "research", "스테로이드 연구", "Adolescent AAS attitudes (PMC10516554)", "research",
        "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10516554/",
        True, False, "medium",
        "청소년 AAS 유병률 2.5%·위험요인은 PMC 연구·메타분석 요약. 범위 수치는 복수 출처 종합. cross-check 단계 정확 수치 확인.",
        [15, 12, 16, 14, 15, 9],
        ["청소년", "스테로이드", "유병률", "신체이미지", "보충제"],
        "어른이 만든 '약 쓰는 몸'을 십대가 따라 그린다 — 19세 이하 유병률 2.5%",
    ),
    (
        "미국 8·10·12학년 스테로이드 사용 추세 — 1991년 이래 장기 통계가 말하는 것",
        "Steroid use prevalence among US 8th/10th/12th graders since 1991",
        "미국 8·10·12학년의 연간 스테로이드 사용 추세를 1991년부터 추적한 통계가 갱신됐다. 청소년 사용은 장기적으로 추적·관리되고 있으나, 신체 이미지 문화와 소셜미디어의 영향 속에 여전히 사회적 관심사로 남아 있다. 추세 데이터는 예방 정책의 기초가 된다.",
        "정리: ① 자료 — 미 8·10·12학년 통합 연간 스테로이드 사용 유병률(1991~2025 추적). ② 의의 — 장기 시계열로 청소년 사용 추이 모니터링 가능. ③ 맥락 — 신체 이미지·소셜미디어·보충제 마케팅이 태도에 영향. ④ 활용 — 추세 데이터가 예방·교육 정책 설계 근거. ⑤ 한계 — 자가보고 설문 기반으로 과소보고 가능. NOGEAR 시각: 숫자가 낮아 보여도 0이 아니다. 그리고 설문지는 거짓말을 자주 받는다.",
        "research", "스테로이드 연구", "Statista (Monitoring the Future 기반)", "research",
        "https://www.statista.com/statistics/696545/us-annual-prevalence-of-steroid-use-in-grades-8-10-12-since-1991/",
        False, False, "low",
        "스타티스타 통계 페이지(원자료 Monitoring the Future 추정). 구체 수치 비표시·2차 집계. 1차(MTF) 확인 필요. 페이월 가능.",
        [12, 9, 14, 13, 13, 9],
        ["청소년", "스테로이드", "유병률추세", "통계", "예방정책"],
        "낮아 보여도 0은 아니다 — 미국 8·10·12학년 스테로이드, 1991년부터의 장기 추세",
    ),
    # ===== 추가: 일반/심혈관/SARM 보강 =====
    (
        "전문 보디빌더 돌연심장사 위험 5배 이상 — 121명 사망·평균 45세, 38%가 심장사",
        "Professional bodybuilders face 5x+ risk of sudden cardiac death",
        "남성 보디빌더 사망을 분석한 연구에서 121명 사망, 평균 45.3세, 그중 38%가 돌연심장사로 나타났다. 전문 보디빌더의 돌연심장사 위험은 아마추어 대비 5배 이상 높았다. 스테로이드가 심근 벽을 두껍게 하고 적혈구를 늘려 고혈압·혈전·심장마비·대동맥 박리 위험을 키운다.",
        "정리: ① 표본 — 남성 보디빌더 사망 121건, 평균 45.3세. ② 결과 — 73건이 돌연사, 그중 46건(전체 38%)이 돌연심장사(SCD). ③ 위험비 — 전문 보디빌더 SCD 위험이 아마추어 대비 5배 이상. ④ 기전 — AAS가 적혈구↑·심근벽 비대 → 고혈압·혈전·심근경색·대동맥 박리. ⑤ 부검 소견 — 심장 비대·관상동맥질환 흔함. NOGEAR 시각: 무대 위 정점이 평균수명 45세로 끝난다. 트로피의 가격표가 심장에 붙어 있다.",
        "research", "스테로이드 연구", "European Heart Journal / ESC 2025", "research",
        "https://academic.oup.com/eurheartj/article/46/30/3006/8131432",
        True, True, "high",
        "보디빌더 121명·평균45.3세·SCD 38%·전문 5배는 EHJ 게재. 동료심사·1차. (DB에 동일 URL 존재 가능 — dedup이 스킵 처리).",
        [20, 14, 15, 14, 17, 11],
        ["돌연심장사", "보디빌더사망", "심근비대", "EHJ", "평균수명"],
        "정점이 평균 45세에 끝난다 — 전문 보디빌더 돌연심장사 위험 5배, 트로피 가격표는 심장에",
    ),
    (
        "세마글루타이드(오젬픽)로 빠지는 건 지방만이 아니다 — 체중감소의 39%가 '근육'",
        "Ozempic muscle loss: up to 39% of weight lost can be lean mass",
        "GLP-1 작용제 세마글루타이드(오젬픽)가 컷팅에 쓰이지만, 임상에서 제지방의 13.9%(약 6.9kg) 손실이 보고됐고 일부 연구에선 감량의 39%가 근육이었다. 식욕 억제로 칼로리 결핍은 쉬워지지만, 저항운동·단백질 없이는 근육이 함께 녹는다. '약으로 깎은 몸'의 숨은 비용이다.",
        "정리: ① 약물 — 세마글루타이드(오젬픽/위고비), GLP-1 작용제. ② 근손실 — 제지방 13.9%(≈6.9kg/15lb) 손실 보고, 일부 연구 감량의 39%가 근육. ③ 사용 동기 — 강력한 식욕 억제로 컷팅기 칼로리 결핍 용이. ④ 위험 — 저항운동·고단백 없이는 근량·근력 동반 감소, 벌크기엔 식욕 억제가 역효과. ⑤ 완화 — 저항운동+충분한 단백질·수분으로 근손실 최소화. NOGEAR 시각: 바늘 하나로 마른 몸을 사면, 청구서는 근육으로 결제된다.",
        "research", "스테로이드 연구", "Cleveland Clinic / U of Utah Health 2025", "research",
        "https://health.clevelandclinic.org/ozempic-muscle-loss",
        False, False, "medium",
        "세마글루타이드 제지방 13.9%·감량 39% 근육 수치는 임상해설·연구 인용. 수치 출처별 차이 큼, cross-check 단계 1차 시험 확인 권장.",
        [15, 11, 17, 16, 14, 11],
        ["세마글루타이드", "오젬픽", "근손실", "GLP-1", "컷팅"],
        "바늘로 마른 몸을 사면 청구서는 근육으로 결제된다 — 오젬픽 감량의 최대 39%가 근육",
    ),
]


def build():
    arts = []
    for r in RAW:
        (title, title_en, summary, detail, cat, cat_ko, src, stype, url,
         peer, primary, conf, notes, sig, tags, rewrite) = r
        score = sum(sig)
        t, emoji = tier(score)
        c, badge = cred(peer, primary, conf, notes)
        arts.append({
            "title": title,
            "title_en": title_en,
            "summary": summary,
            "summary_detail": detail,
            "category": cat,
            "category_ko": cat_ko,
            "source": src,
            "source_type": stype,
            "source_url": url,
            "credibility": c,
            "viral_signals": {
                "shock_factor": sig[0],
                "scientific_credibility": sig[1],
                "relatability": sig[2],
                "recency": sig[3],
                "controversy": sig[4],
                "visual_potential": sig[5],
            },
            "tags": tags,
            "viral_score": score,
            "viral_tier": t,
            "viral_emoji": emoji,
            "date": TODAY,
            "badge": badge,
            "source_verified": False,
            "title_original": title,
            "title_rewrite": rewrite,
        })
    return arts


def main():
    with open(ARTICLES, encoding="utf-8") as f:
        data = json.load(f)

    existing = data.get("news", []) + data.get("research", [])
    seen = {a.get("source_url") for a in existing}

    new_arts = build()
    fresh = [a for a in new_arts if a["source_url"] not in seen]
    skipped = len(new_arts) - len(fresh)

    # 신규를 카테고리별로 합치기: source_type == 'news' -> news, 'research' -> research
    merged = existing + fresh
    # source_url 기준 최종 dedup (첫 등장 우선)
    seen2 = set()
    dedup = []
    for a in merged:
        u = a.get("source_url")
        if u in seen2:
            continue
        seen2.add(u)
        dedup.append(a)

    # viral_score 내림차순 정렬
    dedup.sort(key=lambda a: a.get("viral_score", 0), reverse=True)

    # 최대 200 유지
    dedup = dedup[:200]

    # news/research 재분배 (원래 구조 유지)
    news = [a for a in dedup if a.get("source_type") == "news"]
    research = [a for a in dedup if a.get("source_type") != "news"]

    data["news"] = news
    data["research"] = research

    # meta 갱신
    now = datetime.now(KST)
    scores = [a.get("viral_score", 0) for a in dedup]
    meta = data.setdefault("meta", {})
    meta["last_updated"] = now.isoformat()
    meta["last_updated_kst"] = now.strftime(
        "%Y-%m-%d %H:%M KST") + f" 아침 크롤 — 인핸스드게임·트렌볼론신경독성·위조검사·TRT사기·인슐린·팔룸보이즘 신규 +{len(fresh)}건"
    meta["total_articles"] = len(dedup)
    meta["news_count"] = len(news)
    meta["crawl_count"] = meta.get("crawl_count", 0) + 1
    meta["model"] = "claude-opus-4-8"
    meta["top_viral_score"] = max(scores) if scores else 0
    meta["avg_viral_score"] = round(sum(scores) / len(scores)) if scores else 0

    with open(ARTICLES, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"신규 후보: {len(new_arts)}")
    print(f"중복 스킵: {skipped}")
    print(f"실제 추가: {len(fresh)}")
    print(f"총 기사 수: {len(dedup)} (news {len(news)} / research {len(research)})")
    print("TOP 3:")
    for a in dedup[:3]:
        print(f"  {a['viral_score']} {a['viral_emoji']} {a['title']}")
    print("신규 추가 목록:")
    for a in fresh:
        print(f"  +{a['viral_score']} {a['title']}")


if __name__ == "__main__":
    main()
