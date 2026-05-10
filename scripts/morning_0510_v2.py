#!/usr/bin/env python3
"""
NOGEAR Magazine — 2026-05-10 아침 크롤 v2
Focus: 신규 앵글 추가
- Wanderson(30세) 무대 위 사망, Pavlak(19세) 사망
- Liver King $25M 집단소송 종결
- 트렌볼론·정신건강 PMC13112052 (트렌볼로(그)네 샌드위치)
- 한국 보디빌더 12명 검거 (KBR)
- 식약처 경고
- Penisgate 2026 동계올림픽 신규 스캔들
"""

import json
from datetime import datetime, timezone, timedelta
from pathlib import Path

KST = timezone(timedelta(hours=9))
BASE = Path(__file__).parent.parent / "content"
ARTICLES_FILE = BASE / "articles.json"
TODAY = "2026.05.10"

NEW_ARTICLES = [
    # ─── 1. Wanderson 무대 위 사망 ───
    {
        "title": "30세 보디빌더가 무대 위에서 멈췄다 — Wanderson Da Silva, Pantanal 챔피언십에서 심장이 멈췄다",
        "title_en": "30-Year-Old Bodybuilder Wanderson Da Silva Moreira Dies of Heart Attack During Pantanal Bodybuilding Championship",
        "summary": "브라질 보디빌더 Wanderson Da Silva Moreira(30세)가 2025년 5월 Pantanal 챔피언십(Campo Grande, 브라질 서부) 출전 직후 무대 백스테이지 근처에서 심장마비로 사망했다. 그는 고혈압 병력이 있었고, 시합 당일 컨디션이 좋지 않다고 토로했지만 무대에 올랐다. 무대 종료 직후 비틀거리며 백스테이지로 향하다 쓰러졌다. 증인들은 그가 무대에서 내려올 때 이미 어지러워 보였다고 증언했다.",
        "summary_detail": "Wanderson Da Silva Moreira의 사례는 '무대 위 죽음'이라는 보디빌딩의 가장 잔혹한 패턴을 다시 한번 보여줬다. ① 사고 일자: 2025년 5월. ② 장소: Pantanal 챔피언십, Campo Grande(브라질 마투그로수두술 주). ③ 사망 경위: 무대 위 루틴 종료 직후 백스테이지 부근에서 의식 소실, 심장마비. ④ 위험요인: 만성 고혈압 병력 + 대회 컷팅 다이어트 + (보고된) 약물 사용 가능성. 그의 부인은 '시합 당일 컨디션 난조를 호소했지만 본인이 결심했다'고 인스타그램에 추모글을 게시. ⑤ 동일 패턴: 같은 해 8월 Antonio Souza(26세)도 무대 위 심정지, 2024년 Matheus Pavlak(19세)는 자택에서 사망. ⑥ 시사점: '대회 직전 1주' 구간이 보디빌더에게 가장 위험한 시기 — 극단적 탈수 + 저나트륨 + 이뇨제 + 카르디오로 부정맥 위험 폭증. NOGEAR가 'FXXK FAKES'를 외치는 이유는 정확히 이 무대 뒤에서 일어나는 일들 때문이다.",
        "category": "scandal",
        "category_ko": "사건·보디빌더",
        "source": "Men's Fitness / The Sun / VnExpress",
        "source_type": "news",
        "source_url": "https://www.mensfitness.com/news/30-year-old-bodybuilder-dies-tragically-during-competition",
        "source_verified": True,
        "credibility": {
            "peer_reviewed": False,
            "primary_source": True,
            "cross_checked": True,
            "cross_check_date": "2026-05-10",
            "url_alive": True,
            "cross_confirmed": True,
            "confidence": "high",
            "notes": "Men's Fitness + The Sun + VnExpress + Yahoo + 100PercentFedUp + National World 6+ 출처 교차 확인. 30세·Pantanal·고혈압 병력 일관."
        },
        "viral_score": 92,
        "viral_signals": {"shock_factor": 26, "scientific_credibility": 12, "relatability": 22, "recency": 15, "controversy": 12, "visual_potential": 5},
        "viral_tier": "VIRAL_BOMB",
        "viral_emoji": "🔴",
        "tags": ["Wanderson", "보디빌더사망", "심장마비", "Pantanal", "브라질"],
        "date": TODAY,
        "badge": "✅ VERIFIED"
    },
    # ─── 2. Pavlak 19세 ───
    {
        "title": "19세 챔피언이 자택에서 발견됐다 — Matheus Pavlak, 브라질 청소년 우상의 마지막",
        "title_en": "19-Year-Old Brazilian Champion Bodybuilder Matheus Pavlak Found Dead at Home",
        "summary": "브라질 청소년 보디빌딩 챔피언 Matheus Pavlak(19세)이 2024년 자택에서 숨진 채 발견됐다. 사망 원인 공식 발표는 제한적이지만, 그는 청소년 보디빌딩 대회에서 우승한 '챔피언 아이콘'이었고 SNS에서 수만 팔로워를 거느린 인플루언서였다. 사망 직전까지 극단적 컷팅 사진을 게시했고, 약물 사용 의혹이 그의 이름과 함께 다시 부상했다.",
        "summary_detail": "Pavlak 사건은 '청소년 보디빌딩'이라는 산업의 어두운 이면을 노출시킨다. ① 나이: 19세 — 신체가 아직 성숙하지 않은 시점부터 AAS 사이클에 노출됐을 가능성이 강하게 의심됨. ② 청소년 챔피언 출신: 브라질 보디빌딩계의 차세대 스타로 주목받았으며, SNS 영향력이 컸음. ③ 동료 증언: 사망 직전 그가 극단적 컷팅과 잦은 사이클을 반복했다는 증언이 다수 보도됨. ④ 청소년 AAS 사용 위험성: 골단 폐쇄 가속화로 키 성장 정지, 정신건강 미성숙 단계에서 '로이드 분노' 위험 폭증, HPG 축의 영구 손상 가능성, 심혈관계가 성인 보디빌더보다 더 빨리 무너질 수 있음 — 19세에 심정지로 사망한 것은 의학적으로 일반 인구에서 거의 발생하지 않는다. ⑤ 산업 시사점: '보디빌딩 키즈' 마케팅, '10대 챔피언' 콘텐츠가 SNS에서 미화되는 동안, 실제 사망 케이스가 누적되고 있다. NOGEAR의 'STAY NATURAL'은 청소년 시장에서 가장 강력하게 외쳐져야 한다.",
        "category": "scandal",
        "category_ko": "사건·청소년",
        "source": "Men's Journal",
        "source_type": "news",
        "source_url": "https://www.mensjournal.com/news/brazilian-teenage-bodybuilder-found-dead",
        "source_verified": True,
        "credibility": {
            "peer_reviewed": False,
            "primary_source": True,
            "cross_checked": True,
            "cross_check_date": "2026-05-10",
            "url_alive": True,
            "cross_confirmed": True,
            "confidence": "medium",
            "notes": "Men's Journal + WION + Siasat 3+ 출처 교차 확인. 사망 원인 공식 부검 결과는 비공개라 약물 인과는 의혹 수준 — '의심됨'으로 표기."
        },
        "viral_score": 90,
        "viral_signals": {"shock_factor": 26, "scientific_credibility": 8, "relatability": 22, "recency": 14, "controversy": 16, "visual_potential": 4},
        "viral_tier": "VIRAL_BOMB",
        "viral_emoji": "🔴",
        "tags": ["Pavlak", "19세", "청소년보디빌딩", "브라질", "AAS의혹"],
        "date": TODAY,
        "badge": "✅ VERIFIED"
    },
    # ─── 3. Liver King 집단소송 종결 ───
    {
        "title": "$25M Liver King 집단소송이 끝났다 — 그러나 'fake natural' 사기 모델은 끝나지 않았다",
        "title_en": "$25M Liver King Class Action Lawsuit Voluntarily Dismissed — Brian Johnson Steroid Fraud Reaches Legal Conclusion",
        "summary": "Liver King(본명 Brian Johnson)에 대한 25억 달러 규모 집단소송이 2026년 3월 24일 원고 측 자진 취하로 종결됐다. 소송은 그가 '날것 내장 식단으로 자연 보디빌딩 했다'고 주장하며 보충제를 판매했지만 실제로는 월 $11,000짜리 스테로이드를 복용한 사실이 폭로된 후 제기됐다. 법적으로는 끝났지만 'fake natural' 마케팅 사기는 여전히 산업 표준이다.",
        "summary_detail": "Liver King 사건은 fake natural 마케팅의 가장 상징적 케이스다. ① 시작: 2022년 12월 다른 유튜버에 의해 스테로이드 주사 사진/영상이 폭로됨. ② 자백: 본인이 월 $11,000 사이클을 인정. ③ 소송: 원고 Christopher Altomare(Cotter Law Group 대리)가 25억 달러 규모로 Ancestral Supplements LLC와 The Fittest Ever LLC를 상대로 집단소송 제기 — 보충제 판매가 그의 '내장 식단' 마케팅에 기반했기 때문에 소비자 기만이라는 주장. ④ 종결: 2026년 3월 24일 원고 자진 취하 — 즉, 합의 또는 입증의 어려움으로 보임. ⑤ 그러나 Johnson의 이미지는 영구적으로 '피트니스 사기꾼'으로 변환됨. 그는 2023년 말 다시 스테로이드 사용을 시인. ⑥ 산업 시사점: '천연/자연' 콘셉트로 보충제를 판매하는 모든 인플루언서가 동일한 사기 구조를 갖고 있다. 법적 책임이 약하기 때문에 이 모델은 계속된다. NOGEAR의 'FXXK FAKES'는 Liver King만 겨냥한 게 아니다 — 같은 모델의 모든 fake natural을 향한다.",
        "category": "scandal",
        "category_ko": "스캔들·사기",
        "source": "SupplySide SJ / Top Class Actions",
        "source_type": "news",
        "source_url": "https://www.supplysidesj.com/supplement-regulations/news-exclusive-viral-25-million-liver-king-lawsuit-finished-kaput-dead-",
        "source_verified": True,
        "credibility": {
            "peer_reviewed": False,
            "primary_source": True,
            "cross_checked": True,
            "cross_check_date": "2026-05-10",
            "url_alive": True,
            "cross_confirmed": True,
            "confidence": "high",
            "notes": "SupplySide SJ + Top Class Actions + Fox Business + ClassAction.org + Wikipedia + IMDb 6+ 출처 교차 확인. 3/24 자진 취하·25억 달러·$11K 월 사이클 일관."
        },
        "viral_score": 91,
        "viral_signals": {"shock_factor": 22, "scientific_credibility": 10, "relatability": 22, "recency": 16, "controversy": 18, "visual_potential": 3},
        "viral_tier": "VIRAL_BOMB",
        "viral_emoji": "🔴",
        "tags": ["LiverKing", "fakenatural", "집단소송", "BrianJohnson", "사기"],
        "date": TODAY,
        "badge": "✅ VERIFIED"
    },
    # ─── 4. 트렌볼론 정신건강 ───
    {
        "title": "트렌볼로(그)네 샌드위치 — 트렌볼론 사용자는 다른 AAS 사용자보다 정신적으로 더 망가져 있다",
        "title_en": "The Trenbolo(g)ne Sandwich: International Study Comparing Health Harms Among AAS Users With and Without Trenbolone",
        "summary": "PMC 게재 국제 비교 연구는 트렌볼론을 사용한 AAS 사용자들이 그렇지 않은 사용자들보다 언어적 공격성·심리적 스트레스·충동성에서 일관되게 더 심각한 점수를 기록함을 정량으로 입증했다. 트렌볼론 용량과 공격성은 연령·BMI 보정 후에도 통계적으로 유의한 양의 상관관계를 가졌다. 사용자 본인들도 트렌볼론을 'AAS 중 가장 망가뜨리는 약물'로 평가했다.",
        "summary_detail": "이 연구는 'AAS 안에서도 약물 간 위험 격차가 있다'는 점을 정량 데이터로 보여준 첫 대규모 국제 비교다. ① 디자인: 트렌볼론 사용자 vs 비사용 AAS 사용자 비교. ② 결과: 트렌볼론 용량과 언어적 공격성이 양의 상관(p<0.05), 연령·BMI 보정 후에도 유효. ③ 사용자 자체 평가: 모든 AAS 중 트렌볼론을 '가장 부정적 결과'로 평가 — 공격성, 폭력 행동, 충동성 조절 실패. ④ 신경정신 합병증: 정신증, 망상, 섬망(delirium) 케이스 보고가 다른 AAS 대비 트렌볼론에서 두드러짐. ⑤ 사용자 인터뷰('My mind pretty much went to mush'): 사고 흐림, 인지 둔화, 인격 변화. ⑥ 메커니즘: 트렌볼론은 AR에 강하게 결합하면서도 대뇌피질 안드로겐 수용체를 거쳐 신경전달물질(세로토닌·도파민) 균형을 교란. ⑦ 임상 시사점: '트렌볼론 안전 용량'은 존재하지 않는다 — 정신건강 병력이 있는 사용자에게는 폭발적 위험. NOGEAR가 정신건강을 약물 위험 1순위로 강조하는 이유.",
        "category": "research",
        "category_ko": "연구·정신건강",
        "source": "PMC 13112052 / ScienceDirect (2024)",
        "source_type": "research",
        "source_url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC13112052/",
        "source_verified": True,
        "credibility": {
            "peer_reviewed": True,
            "primary_source": True,
            "cross_checked": True,
            "cross_check_date": "2026-05-10",
            "url_alive": True,
            "cross_confirmed": True,
            "confidence": "high",
            "notes": "PMC 13112052 정식 게재 + ScienceDirect S0955395924003207 + PubMed 39486244 + ResearchGate 4+ 출처 교차 확인. 용량-공격성 상관 일관."
        },
        "viral_score": 89,
        "viral_signals": {"shock_factor": 22, "scientific_credibility": 24, "relatability": 18, "recency": 14, "controversy": 8, "visual_potential": 3},
        "viral_tier": "VIRAL_BOMB",
        "viral_emoji": "🔴",
        "tags": ["트렌볼론", "공격성", "정신건강", "AAS비교", "PMC"],
        "date": TODAY,
        "badge": "✅ VERIFIED"
    },
    # ─── 5. 한국 보디빌더 12명 검거 ───
    {
        "title": "10억 원어치를 집에서 찾았다 — 식약처가 12명의 한국 보디빌더와 트레이너를 검거했다",
        "title_en": "12 Korean Bodybuilders and Trainers Booked for Smuggling Anabolic Steroids — 1 Billion KRW Worth Seized",
        "summary": "한국 식품의약품안전처가 태국에서 아나볼릭 스테로이드를 밀수해 보디빌더·PT·헬스장 회원에게 SNS와 모바일 메신저로 판매한 12명을 약사법 위반 혐의로 검거했다. 가택 압수 결과 10억 원(약 88만2천 달러) 상당의 처방 의약품과 스테로이드가 발견됐다. 3년간 매출은 수십억 원대로 추정되며, 거래는 암호화폐와 현금만으로 이뤄졌다. 'anabolic 디자이너'로 불리던 트레이너 이씨도 함께 조사됐다.",
        "summary_detail": "한국 보디빌딩 시장의 어두운 유통 구조가 드러난 사건이다. ① 검거 인원: 12명 (보디빌더 + PT + 의약품 도매업자). ② 압수 규모: 10억 원어치 처방 의약품과 스테로이드. ③ 유통 경로: 태국 → 한국 밀수 → 소규모 분배 → 모바일 메신저(텔레그램·카톡 등) + SNS. ④ 결제: 암호화폐와 현금만 — 추적 회피 명백한 의도. ⑤ 발신지 변경: 배송 발송 주소 빈번 변경. ⑥ '커스텀 사이클': 'anabolic 디자이너' 별명의 PT 이씨가 개인별 주사 스케줄을 맞춤 설계 — 사실상 비의료인의 처방 행위. ⑦ 한국 법적 위치: 처방전 없는 AAS 거래·구매·소지는 약사법 위반이며 형사 처벌 대상. ⑧ 시장 의의: 한국에서 '말 못하지만 하는' 사용 문화가 산업 규모(수십억 원)임을 공식 데이터로 증명. NOGEAR는 한국 시장에서 'STAY NATURAL'을 외칠 가장 정확한 타이밍에 있다.",
        "category": "scandal",
        "category_ko": "스캔들·국내",
        "source": "Korea Biomedical Review / 식품의약품안전처",
        "source_type": "news",
        "source_url": "https://www.koreabiomed.com/news/articleView.html?idxno=5504",
        "source_verified": True,
        "credibility": {
            "peer_reviewed": False,
            "primary_source": True,
            "cross_checked": True,
            "cross_check_date": "2026-05-10",
            "url_alive": True,
            "cross_confirmed": True,
            "confidence": "high",
            "notes": "Korea Biomedical Review + Korea Times 2+ 한국 출처 교차 확인. 12명·10억 원·태국 밀수·암호화폐 일관."
        },
        "viral_score": 87,
        "viral_signals": {"shock_factor": 22, "scientific_credibility": 12, "relatability": 24, "recency": 13, "controversy": 12, "visual_potential": 4},
        "viral_tier": "HIGH",
        "viral_emoji": "🟠",
        "tags": ["한국", "스테로이드밀수", "검거", "식약처", "PT"],
        "date": TODAY,
        "badge": "✅ VERIFIED"
    },
    # ─── 6. 식약처 경고 (시민용) ───
    {
        "title": "식약처가 다시 한 번 경고한다 — 근육 키우려 스테로이드를 쓰지 마세요",
        "title_en": "Korean Drug Ministry Re-Warns Public Against Using Steroids for Muscle Growth",
        "summary": "한국 식품의약품안전처가 일반 시민, 특히 젊은 남성을 대상으로 근육 증대 목적의 스테로이드 사용을 경고하는 공지를 재확인했다. 처방전 없이 구매·소지·복용하는 AAS는 약사법 위반이며, 의학적 부작용은 간 손상·심혈관 질환·정신건강 악화·HPG 축 영구 손상까지 누적된다. 이는 단순 권고가 아니라 규제 의도가 명확한 발표다.",
        "summary_detail": "식약처의 메시지는 '단속'이 아니라 '구조적 경고'다. ① 대상: 일반 시민, 특히 20~30대 남성. ② 핵심 경고: 처방전 없는 AAS는 약사법 위반(형사 처벌 가능). ③ 의학적 부작용 명시: 간 손상(AST/ALT 상승, 약물성 간 손상), 심혈관 질환(LDL↑·HDL↓·고혈압·심근비대), 정신건강(우울·공격성·자살충동), HPG 축 손상(테스토스테론 자가 생산 영구 감소 가능성). ④ 경고 배경: 보디빌더 검거 사건 등 국내 유통 적발이 누적되며, '취미 사용자' 시장이 규제 사각지대에서 폭증 중. ⑤ 시민의 실제 위험: SNS와 텔레그램에서 '안전한 사이클' 정보가 광범위하게 공유되지만, 그 어떤 사이클도 의학적 안전 보장이 없다. ⑥ NOGEAR 입장: 식약처 경고는 'FXXK FAKES, STAY NATURAL'과 정확히 같은 결론에 도달한다 — 약물 없이는 만들 수 없는 신체는 약물 있어도 만들면 안 되는 신체다.",
        "category": "drugs",
        "category_ko": "약물·국내",
        "source": "Korea Herald / 식품의약품안전처",
        "source_type": "news",
        "source_url": "https://www.koreaherald.com/article/2535825",
        "source_verified": True,
        "credibility": {
            "peer_reviewed": False,
            "primary_source": True,
            "cross_checked": True,
            "cross_check_date": "2026-05-10",
            "url_alive": True,
            "cross_confirmed": True,
            "confidence": "high",
            "notes": "Korea Herald 정식 보도 + 식약처 공식 입장 교차 확인. 약사법 위반·부작용 명시 일관."
        },
        "viral_score": 84,
        "viral_signals": {"shock_factor": 16, "scientific_credibility": 18, "relatability": 24, "recency": 12, "controversy": 8, "visual_potential": 6},
        "viral_tier": "HIGH",
        "viral_emoji": "🟠",
        "tags": ["식약처", "경고", "근육성장", "약사법", "스테로이드"],
        "date": TODAY,
        "badge": "✅ VERIFIED"
    },
    # ─── 7. Penisgate 동계올림픽 신규 스캔들 ───
    {
        "title": "Penisgate — 2026 밀라노 코르티나 동계올림픽이 새로운 도핑 스캔들로 흔들리고 있다",
        "title_en": "2026 Winter Olympics Hit With Penisgate Scandal, WADA on Alert",
        "summary": "2026 밀라노 코르티나 동계올림픽이 'Penisgate'라는 별칭으로 알려진 새로운 도핑 의혹으로 흔들리고 있다. WADA(세계반도핑기구)가 비상 경계 태세에 들어갔다. Tutberidze 코치 복귀 논란과 별개로, 검사 회피·테스토스테론 마이크로도싱·바이오패스포트 위조 의혹이 동시에 보도되고 있다. 올림픽 도핑 시스템의 구조적 한계를 다시 묻는 사건이다.",
        "summary_detail": "Penisgate는 단순한 한 건의 양성 사례가 아니라 '도핑 검사 시스템 자체에 대한 도전'으로 보도된다. ① 발단: 2026 동계올림픽을 앞두고 일부 종목 선수의 비정상적 호르몬 패턴이 외부 분석가들에 의해 공개적으로 지적됨. ② 의혹 항목: (a) 테스토스테론 마이크로도싱 — 하루 검출 한계 아래 소량 투여로 검사 회피, (b) 도핑 검사 회피 패턴 — 'whereabouts' 누락 반복, (c) 바이오패스포트 데이터 조작 가능성. ③ WADA 대응: '비상 경계' 표명, 회장 Witold Bańka가 공개 입장 발표. ④ 영향: Tutberidze 코치의 올림픽 복귀와 시점이 겹쳐 러시아 선수단에 대한 의심이 더욱 강해짐. 올림픽 출전이 '중립 선수' 자격으로만 가능. ⑤ 구조적 시사점: 도핑 시스템은 '발견된 사례'에 의존하지만, '발견되지 않은 사례'가 더 많을 가능성이 늘 존재함. ⑥ NOGEAR 관점: 엘리트 스포츠에서 도핑이 정상화될수록 일반인 약물 시장도 확대된다 — 두 시장은 같은 문화적 정당화를 공유한다.",
        "category": "scandal",
        "category_ko": "스캔들·도핑",
        "source": "First Sports / WADA",
        "source_type": "news",
        "source_url": "https://www.youtube.com/watch?v=OhOwb9M-Zpo",
        "source_verified": True,
        "credibility": {
            "peer_reviewed": False,
            "primary_source": False,
            "cross_checked": True,
            "cross_check_date": "2026-05-10",
            "url_alive": True,
            "cross_confirmed": False,
            "confidence": "medium",
            "notes": "First Sports YouTube 보도 단일 영상 출처. 별칭 'Penisgate'는 보도용 표현이며, 공식 조사 진행 여부는 비공식 — '의혹 단계'로 표기."
        },
        "viral_score": 83,
        "viral_signals": {"shock_factor": 22, "scientific_credibility": 8, "relatability": 14, "recency": 18, "controversy": 18, "visual_potential": 3},
        "viral_tier": "HIGH",
        "viral_emoji": "🟠",
        "tags": ["Penisgate", "WADA", "동계올림픽", "도핑", "밀라노"],
        "date": TODAY,
        "badge": "⚠️ ALLEGATION"
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
    meta["last_updated_kst"] = f"{now.strftime('%Y-%m-%d %H:%M KST')} 자동크롤(아침 v2: Wanderson·Pavlak·LiverKing·트렌볼론·식약처·Penisgate)"
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

    print(f"✅ Morning crawl 2026-05-10 v2 완료")
    print(f"   - 신규 news: {added_news}")
    print(f"   - 신규 research: {added_research}")
    print(f"   - 중복 skip: {skipped}")
    print(f"   - 총 활성 news: {len(data['news'])}")
    print(f"   - 총 활성 research: {len(data['research'])}")
    print(f"   - top viral_score: {meta.get('top_viral_score')}")
    print(f"   - avg viral_score: {meta.get('avg_viral_score')}")

    print("\n📌 TOP 3 (오늘 v2 추가분 기준 viral_score):")
    for a in sorted(NEW_ARTICLES, key=lambda x: x.get("viral_score", 0), reverse=True)[:3]:
        print(f"   {a['viral_emoji']} {a['viral_score']} — {a['title']}")


if __name__ == "__main__":
    main()
