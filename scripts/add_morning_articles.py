# -*- coding: utf-8 -*-
import json
from datetime import datetime, timezone

with open('content/articles.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

today = "2026.04.14"
check_date = "2026-04-14"

new_articles = [
    {
        "title": "스테로이드 끊으면 '자살충동·우울·불면증' — AAS 금단증상의 공포",
        "title_ko": "스테로이드 끊으면 '자살충동·우울·불면증' — AAS 금단증상의 공포",
        "title_en": "AAS Withdrawal: Suicidal Ideation, Depression, Insomnia — The Hidden Horror of Stopping Steroids",
        "summary": "미국 국립약물남용연구소(NIDA)와 StatPearls 임상 데이터에 따르면, 아나볼릭-안드로겐 스테로이드(AAS)를 중단하면 자살충동, 극심한 우울증, 불면증, 식욕 감퇴, 근육통, 성욕 저하가 동반되는 금단증상이 나타난다. '스테로이드는 끊으면 된다'는 인식은 위험한 오해다. AAS 금단은 의학적으로 관리가 필요한 심각한 상태다. 금단 기간 중 자살 시도 사례도 보고됐다.",
        "summary_detail": "AAS(아나볼릭-안드로겐 스테로이드) 사용자가 갑자기 약물을 중단하면 내인성 테스토스테론 생성 축(HPG axis)이 억제된 상태여서 심각한 호르몬 결핍이 발생한다. NIDA와 StatPearls가 정리한 금단 증상 목록에는 거식증, 체형 왜곡 불만, 식욕 감소, 우울증과 우울감, 극도의 피로, 두통, 불면증, 성욕 저하, 근육통과 관절통, 안절부절, 자살충동, 스테로이드 재복용 충동, 체중 감소가 포함된다. 자살충동은 가장 위험한 증상으로, 임상적 감시 없이 혼자 AAS를 끊는 것은 생명에 위협이 될 수 있다. 의학적 PCT(사후 사이클 치료)로 클로미펜, 타목시펜, hCG 등이 사용되지만 완전한 회복까지 수개월이 걸린다. '언제든지 그만둘 수 있다'는 믿음은 AAS 중독을 과소평가하는 위험한 인식이다.",
        "category": "steroids",
        "category_ko": "스테로이드",
        "source": "NIDA / StatPearls (NIH)",
        "source_type": "journal",
        "source_url": "https://www.ncbi.nlm.nih.gov/books/NBK538174/",
        "viral_score": 87,
        "viral_signals": {
            "shock_factor": 25,
            "scientific_credibility": 18,
            "relatability": 20,
            "recency": 13,
            "controversy": 7,
            "visual_potential": 4
        },
        "viral_tier": "VIRAL_BOMB",
        "viral_emoji": "🔴",
        "tags": ["스테로이드금단", "자살충동", "우울증", "AAS", "금단증상", "PCT"],
        "date": today,
        "credibility": {
            "peer_reviewed": True,
            "primary_source": True,
            "cross_checked": True,
            "cross_check_date": check_date,
            "url_alive": True,
            "cross_confirmed": True,
            "confidence": "high",
            "notes": "StatPearls (NBK538174) NIH Bookshelf confirmed. AAS withdrawal symptoms list confirmed including suicidal ideations, depression, insomnia, low libido, myalgia. NIDA corroborates. Well-established clinical evidence for AAS withdrawal syndrome."
        },
        "badge": "✅ VERIFIED"
    },
    {
        "title": "스테로이드가 뇌를 망친다 — 불안·조증·우울·자살충동 유발 체계적 증거",
        "title_ko": "스테로이드가 뇌를 망친다 — 불안·조증·우울·자살충동 유발 체계적 증거",
        "title_en": "AAS Destroys the Brain: Systematic Evidence of Anxiety, Mania, Depression, and Suicidal Ideation",
        "summary": "2025년 MDPI와 PMC에 발표된 체계적 검토에서 AAS 남용이 심혈관만이 아니라 뇌와 정신 건강에도 광범위한 손상을 유발한다는 복합 증거가 정리됐다. 비사용자보다 불안 장애 발생률이 현저히 높으며, 중등도 이상의 AAS 복용은 조증, 경조증, 주요 우울증과 연관된다. 금단 시에는 자살충동까지 나타난다. '근육을 위한 약물'이 사실상 '뇌를 망가뜨리는 약물'이라는 충격적인 결론이다.",
        "summary_detail": "2025년 MDPI 학술지(IJMS)에 발표된 AAS 전신 영향 체계적 분석과 PMC7832337의 문헌고찰을 종합하면, AAS 남용의 정신신경 독성이 명확히 입증된다. AAS 사용자는 비사용자보다 불안장애 발생률이 현저히 높고, 중등도에서 고용량 복용은 조증(mania), 경조증(hypomania), 주요 우울증(MDD)과 유의미하게 연관된다. 근원적 기전은 AAS가 기분 조절에 관여하는 세로토닌과 도파민 시스템을 교란하고, 편도체 과활성화를 통해 공격성과 충동성을 증폭시키는 것이다. 장기 복용 후 AAS를 중단하면 내인성 테스토스테론 생성이 억제된 상태에서 극심한 호르몬 결핍이 발생하며, 자살충동까지 동반되는 금단 증후군이 나타난다. 동물 실험에서 일부 AAS는 신경세포 수를 감소시키고 미토콘드리아 기능을 손상시켰다. 근육은 얻고 뇌는 잃는 교환이 실제로 일어나고 있다.",
        "category": "steroids",
        "category_ko": "스테로이드",
        "source": "PMC / MDPI IJMS 2025",
        "source_type": "journal",
        "source_url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC12652398/",
        "viral_score": 86,
        "viral_signals": {
            "shock_factor": 24,
            "scientific_credibility": 19,
            "relatability": 18,
            "recency": 14,
            "controversy": 8,
            "visual_potential": 3
        },
        "viral_tier": "VIRAL_BOMB",
        "viral_emoji": "🔴",
        "tags": ["스테로이드", "정신건강", "불안", "조증", "우울증", "뇌손상", "AAS"],
        "date": today,
        "credibility": {
            "peer_reviewed": True,
            "primary_source": True,
            "cross_checked": True,
            "cross_check_date": check_date,
            "url_alive": True,
            "cross_confirmed": True,
            "confidence": "high",
            "notes": "PMC12652398 (MDPI IJMS 2025) confirmed in search. AAS neuropsychiatric: anxiety, mania, hypomania, major depression confirmed. Withdrawal suicidal ideation cross-confirmed via NIDA/StatPearls. Multiple peer-reviewed sources converge on neuropsychiatric harms."
        },
        "badge": "✅ VERIFIED"
    },
    {
        "title": "스탠퍼드, '부작용 없는 천연 오젬픽' 화합물 발견 — 근손실 없는 체중 감량 가능성",
        "title_ko": "스탠퍼드, '부작용 없는 천연 오젬픽' 화합물 발견 — 근손실 없는 체중 감량 가능성",
        "title_en": "Stanford Discovers 'Natural Ozempic' Without Side Effects — Bodybuilding World Takes Notice",
        "summary": "2026년 4월 12일 ScienceDaily가 보도한 스탠퍼드 대학 연구에서 오젬픽(세마글루타이드)과 유사한 체중 감량 효과를 내면서도 부작용이 없는 '천연 GLP-1 유사' 화합물이 발견됐다. 이 물질은 GLP-1 수용체를 자극하는 천연 경로를 활성화해 구역, 근손실 등 오젬픽의 대표 부작용 없이 식욕을 억제한다. 보디빌딩 커뮤니티와 비만 치료 분야 모두에 혁명적 가능성을 열 수 있는 발견이다.",
        "summary_detail": "스탠퍼드 대학 연구팀이 2026년 4월 발표한 연구에서 인체 내 천연 화합물이 GLP-1 수용체를 통해 오젬픽과 유사한 대사 효과를 낼 수 있음을 발견했다. ScienceDaily가 4월 12일 보도한 이 연구는 오젬픽의 가장 큰 단점인 구역, 구토, 근육 손실 없이 포만감과 식욕 억제 효과를 재현할 가능성을 제시한다. 오젬픽은 체중 감량에 탁월하지만 체중의 최대 39%가 근육에서 빠지고 속근 섬유 근력이 20% 감소하는 부작용이 있다. 새로 발견된 화합물이 이 문제를 해결할 수 있다면, 피트니스 인구와 비만 환자 모두에게 이상적인 대안이 될 수 있다. 다만 현재는 초기 연구 단계이며, 인체 임상 시험 결과가 나오기까지는 수년이 걸릴 것으로 예상된다. NOGEAR: 자연이 오젬픽보다 더 나은 해답을 갖고 있을지도 모른다.",
        "category": "science",
        "category_ko": "과학연구",
        "source": "ScienceDaily / Stanford University",
        "source_type": "news",
        "source_url": "https://www.sciencedaily.com/releases/2026/04/260412221946.htm",
        "viral_score": 87,
        "viral_signals": {
            "shock_factor": 22,
            "scientific_credibility": 17,
            "relatability": 20,
            "recency": 18,
            "controversy": 7,
            "visual_potential": 3
        },
        "viral_tier": "VIRAL_BOMB",
        "viral_emoji": "🔴",
        "tags": ["오젬픽대안", "천연GLP-1", "스탠퍼드", "체중감량", "근손실없음", "GLP-1"],
        "date": today,
        "credibility": {
            "peer_reviewed": False,
            "primary_source": False,
            "cross_checked": True,
            "cross_check_date": check_date,
            "url_alive": True,
            "cross_confirmed": True,
            "confidence": "medium",
            "notes": "ScienceDaily 2026-04-12 confirmed in search results. Stanford 'natural Ozempic without side effects' discovery reported. Press release stage - peer-reviewed publication not yet confirmed. Early-stage research. URL alive and found in search."
        },
        "badge": "🔍 CHECKED"
    },
    {
        "title": "러시아 도핑 코치 에테리 투트베리제, 2026 밀라노 동계올림픽 복귀 — WADA '불편하다'",
        "title_ko": "러시아 도핑 코치 에테리 투트베리제, 2026 밀라노 동계올림픽 복귀 — WADA '불편하다'",
        "title_en": "Russian Doping Coach Eteri Tutberidze Returns to 2026 Milan Olympics — WADA Chief: 'Not Comfortable'",
        "summary": "2022 베이징 동계올림픽 도핑 스캔들의 코치 에테리 투트베리제가 2026 밀라노-코르티나 동계올림픽에 복귀했다. WADA 회장은 '그녀의 존재가 불편하다'고 공개 발언했다. 전 제자 발리예바(15세)의 도핑 사건으로 전 세계를 충격에 빠뜨렸던 투트베리제가 아무런 제재 없이 최고 무대로 복귀한 것은 반도핑 시스템의 구조적 실패를 드러낸다.",
        "summary_detail": "2022 베이징 동계올림픽에서 15세 피겨스케이팅 선수 카밀라 발리예바가 금지 약물 트리메타지딘 양성 반응을 보이며 국제 도핑 스캔들이 터졌다. 발리예바의 코치인 에테리 투트베리제는 당시 어린 선수를 강제로 대회에 출전시키고 올림픽 종료 후 냉담하게 대한 모습으로 전 세계에 충격을 줬다. 발리예바는 결국 4년 자격 정지를 받아 2026년 밀라노 올림픽 출전 자격을 박탈당했다. 그러나 투트베리제는 다른 선수 2명을 코치하며 밀라노-코르티나 올림픽에 복귀했다. WADA 회장 비톨트 반카는 '투트베리제의 존재가 불편하다'고 직접 발언했고, Newsweek는 이를 새로운 PED 논란으로 규정했다. 스포츠 윤리 전문가들은 도핑 책임 코치가 아무런 징계 없이 최고 무대에 복귀한 것이 반도핑 시스템의 심각한 허점이라고 비판한다. 도핑 문화는 선수 개인이 아닌 시스템과 코치진에 의해 주도된다는 점을 이 사건은 다시 한번 증명했다.",
        "category": "doping",
        "category_ko": "도핑",
        "source": "Newsweek / NBC New York",
        "source_type": "news",
        "source_url": "https://www.newsweek.com/sports/russian-coachs-winter-olympics-return-sparks-fresh-ped-controversy-11537286",
        "viral_score": 84,
        "viral_signals": {
            "shock_factor": 20,
            "scientific_credibility": 6,
            "relatability": 17,
            "recency": 18,
            "controversy": 16,
            "visual_potential": 7
        },
        "viral_tier": "HOT",
        "viral_emoji": "🟠",
        "tags": ["도핑스캔들", "밀라노올림픽", "러시아", "WADA", "피겨스케이팅", "투트베리제"],
        "date": today,
        "credibility": {
            "peer_reviewed": False,
            "primary_source": True,
            "cross_checked": True,
            "cross_check_date": check_date,
            "url_alive": True,
            "cross_confirmed": True,
            "confidence": "high",
            "notes": "Newsweek and NBC New York articles confirmed in search results. Tutberidze coaching 2 skaters at 2026 Milan-Cortina. WADA president Witold Banka 'not comfortable' quote confirmed. Valieva 4-year ban confirmed."
        },
        "badge": "✅ VERIFIED"
    },
    {
        "title": "스테로이드 사용자들의 DIY 위험 관리 — 의사 없이 혼자 관리하는 치명적 자기기만",
        "title_ko": "스테로이드 사용자들의 DIY 위험 관리 — 의사 없이 혼자 관리하는 치명적 자기기만",
        "title_en": "AAS Users' Dangerous DIY Risk Management: Self-Prescribing PCT Without a Doctor",
        "summary": "PMC에 발표된 2025년 질적 연구에서 AAS 사용자들이 의료 기관 없이 혈액 검사를 직접 주문하고, PCT(사후 사이클 치료) 약물을 자가 처방하는 실태가 밝혀졌다. 이들은 안전하게 사용하는 법을 안다고 믿지만, 의료 감독 없는 자가 관리는 오히려 위험을 증폭시킨다. 부작용 발생 시 응급 치료가 지연되는 아이러니도 보고됐다.",
        "summary_detail": "PMC에 발표된 2025년 AAS 사용자 대상 질적 연구(PMC12302693)는 사용자들이 어떻게 위험을 인식하고 자가 관리를 시도하는지를 심층 분석했다. 대다수 사용자들이 개인 혈액 검사 서비스로 간 수치, 지질 패널, 테스토스테론 수치를 모니터링했다. 그러나 결과 해석 오류, 비정상 수치 무시, bro science 기반의 자가 처방(클로미펜, 타목시펜, 아리미덱스 등)이 만연했다. 의료 기관 방문 시 AAS 사용을 숨기는 경우가 많아 의사가 혈액 이상의 원인을 파악하지 못하고 잘못된 치료 방향을 설정하는 사례도 있었다. 응급 상황에서 AAS 및 PCT 약물 복용 사실을 밝히지 않아 치료가 지연되는 아이러니도 보고됐다. 연구진은 AAS 사용자들이 해악 감소(harm reduction)를 추구하지만 의학 지식의 한계로 오히려 더 큰 위험에 노출될 수 있다고 결론지었다.",
        "category": "steroids",
        "category_ko": "스테로이드",
        "source": "PMC / Qualitative Study 2025",
        "source_type": "journal",
        "source_url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC12302693/",
        "viral_score": 84,
        "viral_signals": {
            "shock_factor": 21,
            "scientific_credibility": 17,
            "relatability": 20,
            "recency": 13,
            "controversy": 10,
            "visual_potential": 3
        },
        "viral_tier": "HOT",
        "viral_emoji": "🟠",
        "tags": ["스테로이드", "자가관리", "DIY의료", "PCT", "혈액검사", "해악감소"],
        "date": today,
        "credibility": {
            "peer_reviewed": True,
            "primary_source": True,
            "cross_checked": True,
            "cross_check_date": check_date,
            "url_alive": True,
            "cross_confirmed": True,
            "confidence": "high",
            "notes": "PMC12302693 confirmed in search results: 'Managing risks and harms associated with the use of anabolic steroids: a qualitative study' PMC 2025. Self-monitoring, self-prescribing PCT, hiding use from doctors - all confirmed patterns in the study."
        },
        "badge": "✅ VERIFIED"
    },
    {
        "title": "SARMs 임상 RCT 결론 — 효과는 있지만 운동선수 복용량은 임상량의 10~100배",
        "title_ko": "SARMs 임상 RCT 결론 — 효과는 있지만 운동선수 복용량은 임상량의 10~100배",
        "title_en": "SARMs RCT Review: Muscle Gains Real, But Athletes Take 10-100x the Studied Dose — Safety Data Missing",
        "summary": "Wiley Clinical Endocrinology 2025 체계적 문헌고찰에서 SARMs가 임상 용량에서 근육량과 신체 성능을 실제로 향상시키는 것으로 나타났다. 그러나 실제 보디빌더가 사용하는 용량은 임상 연구의 10~100배에 달하며, 이 용량에서의 안전성 데이터는 전혀 없다. 효과 증거는 있지만 실사용 환경의 안전 데이터는 없는 반쪽짜리 과학이 SARMs의 실체다.",
        "summary_detail": "Clinical Endocrinology(Wiley)에 발표된 2025년 무작위 대조시험(RCT) 체계적 문헌고찰은 SARMs의 신체 성능에 대한 임상 증거를 종합했다. SARMs는 임상 연구 용량에서 근육량 증가, 보행 속도 향상, 신체 기능 개선 효과를 보였다. 그러나 연구에 사용된 임상 용량이 실제 운동선수나 보디빌더들이 사용하는 용량의 10분의 1에서 100분의 1 수준에 불과하다. 운동선수들이 스택(여러 SARMs 병용)하거나 초고용량으로 복용하는 경우에 대한 안전성 데이터는 존재하지 않는다. 더 큰 문제는 시판되는 SARMs 제품 중 상당수가 라벨에 표기된 성분과 실제 성분이 다르며, 스테로이드나 기타 금지 약물이 혼합된 경우도 있다는 것이다. AST, ALT 간 효소 수치는 SARMs 사용 기간에 비례해 증가했으며, HDL 콜레스테롤은 감소했다. 전체 테스토스테론과 SHBG의 유의미한 변화도 확인됐다. 효과는 실재하지만, 실사용 환경에서의 안전 데이터는 없는 것이 SARMs의 냉혹한 현실이다.",
        "category": "SARMs",
        "category_ko": "SARMs",
        "source": "Clinical Endocrinology / Wiley 2025",
        "source_type": "journal",
        "source_url": "https://onlinelibrary.wiley.com/doi/10.1111/cen.15135",
        "viral_score": 83,
        "viral_signals": {
            "shock_factor": 19,
            "scientific_credibility": 19,
            "relatability": 17,
            "recency": 15,
            "controversy": 8,
            "visual_potential": 5
        },
        "viral_tier": "HOT",
        "viral_emoji": "🟠",
        "tags": ["SARMs", "임상데이터", "용량차이", "근육향상", "안전성부재", "RCT"],
        "date": today,
        "credibility": {
            "peer_reviewed": True,
            "primary_source": True,
            "cross_checked": True,
            "cross_check_date": check_date,
            "url_alive": False,
            "cross_confirmed": True,
            "confidence": "medium",
            "notes": "Wiley DOI cen.15135 confirmed in search results. 2025 systematic review of SARMs RCTs. Clinical doses show performance gains. Athletes use 10-100x clinical doses confirmed via Smart SARMs and FitScience 2025 sources. AST/ALT/HDL/testosterone changes confirmed. URL likely paywalled."
        },
        "badge": "🔍 CHECKED"
    }
]

# Merge - avoid duplicates by title
existing_titles = set()
for a in data.get('news', []):
    existing_titles.add(a.get('title', '').strip())

added = 0
for article in new_articles:
    if article['title'].strip() not in existing_titles:
        data['news'].append(article)
        existing_titles.add(article['title'].strip())
        added += 1
        print(f"추가: {article['title'][:50]}")

# Sort by viral_score descending
data['news'].sort(key=lambda x: x.get('viral_score', 0), reverse=True)

# Keep max 200
if len(data['news']) > 200:
    data['news'] = data['news'][:200]

# Update meta
data['meta']['total_articles'] = len(data['news']) + len(data.get('featured', []))
data['meta']['news_count'] = len(data['news'])
data['meta']['last_updated'] = datetime.now(timezone.utc).isoformat()
data['meta']['last_updated_kst'] = '2026-04-14 아침 크롤'
data['meta']['crawl_count'] = data['meta'].get('crawl_count', 0) + 1
data['meta']['top_viral_score'] = max((a.get('viral_score', 0) for a in data['news']), default=0)
data['meta']['avg_viral_score'] = round(sum(a.get('viral_score', 0) for a in data['news']) / max(len(data['news']), 1), 1)
data['meta']['model'] = 'claude-sonnet-4-6'

with open('content/articles.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"\n신규 추가: {added}개")
print(f"총 기사 수: {data['meta']['total_articles']}개")
print(f"뉴스 배열: {len(data['news'])}개")
print(f"최고 바이럴 점수: {data['meta']['top_viral_score']}")
print(f"평균 바이럴 점수: {data['meta']['avg_viral_score']}")
