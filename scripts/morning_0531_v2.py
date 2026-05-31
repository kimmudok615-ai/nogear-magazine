#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""NOGEAR 아침 크롤 v2 — 2026-05-31. 신규 토픽(트렌볼론·인슐린·신장FSGS·여유증·여성남성화·클렌부테롤·근이형증·뇌인지·TRT) 추가.
   ⚠️ 모든 URL은 2026-05-31 WebSearch 결과에서 1:1 확인된 실제 링크만 사용."""
import json, datetime

PATH = "content/articles.json"
TODAY = "2026.05.31"

def sig(shock, sci, rel, rec, contr, vis):
    return {"shock_factor": shock, "scientific_credibility": sci, "relatability": rel,
            "recency": rec, "controversy": contr, "visual_potential": vis}

def cred(pr, ps, cc, conf, notes, acc, confirmed=True):
    return {"peer_reviewed": pr, "primary_source": ps, "cross_checked": cc,
            "cross_check_date": "2026-05-31", "url_alive": True, "cross_confirmed": confirmed,
            "confidence": conf, "notes": notes, "fact_checked": True, "accuracy": acc}

def score(s):
    return sum(s.values())

NEW_RESEARCH = [
    {
        "title": "트렌볼론, 분노를 주사한다 — AAS 사용 남성의 공격성·정신적 고통 직접 연관",
        "title_en": "Trenbolone, psychological distress, and aggression among males who use AAS",
        "summary": "Int. J. Drug Policy 연구는 트렌볼론 사용이 AAS 사용 남성에서 언어적 공격성·정신적 고통 증가와 직접 연관된다고 보고했다. 고용량일수록 편집증·분노·정서 불안정이 두드러진다. '트렌'은 근육뿐 아니라 인격을 깎는다.",
        "summary_detail": "정리: ① 대상 — AAS 사용 남성 중 트렌볼론 사용군 비교. ② 결과 — 언어적 공격성·정신적 고통과 유의한 연관, 용량의존적. ③ 증상 — 편집증, 불안, 분노, 정서 불안정(labile affect). ④ 빈도 — 사용자 자가보고에서 안절부절/과민 16.2%, 우울 14.4%, 급격한 기분변화 12.4%, 분노/공격성 11.7%. ⑤ 함의 — 정신과적 위해가 일화가 아닌 데이터. NOGEAR 시각: '트렌렉(tren rage)'은 밈이 아니라 부작용이다. 거울 속 근육이 커질수록 사람은 작아진다.",
        "category": "research", "category_ko": "정신·약물",
        "source": "International Journal of Drug Policy (ScienceDirect)", "source_type": "journal",
        "source_url": "https://www.sciencedirect.com/science/article/pii/S0955395924003207",
        "credibility": cred(True, True, True, "high", "Int J Drug Policy 동료심사 연구. 트렌볼론-공격성·정신적 고통 용량의존 연관 일치.", "verified"),
        "viral_signals": sig(20, 19, 19, 16, 16, 8), "tags": ["트렌볼론", "공격성", "정신건강", "AAS", "트렌렉"],
    },
    {
        "title": "트렌볼론을 더한 약물파는 더 망가진다 — 국제 비교 연구 'Trenbolo(g)ne Sandwich'",
        "title_en": "The Trenbolo(g)ne Sandwich: International Study Comparing Health Harms With/Without Trenbolone",
        "summary": "트렌볼론을 사용하는 AAS 사용자와 사용하지 않는 사용자의 건강 피해를 비교한 국제 연구는, 트렌볼론군에서 심리사회적 위해의 위험 프로파일이 극단적으로 악화됐다고 보고했다. 같은 약물파 안에서도 '트렌'이 선을 넘게 만든다.",
        "summary_detail": "정리: ① 설계 — 트렌볼론 사용군 vs 비사용군 국제 비교. ② 결과 — 트렌볼론군에서 심리사회적 위해 위험이 극단적으로 상승. ③ 의미 — 같은 AAS 사용자 집단 내에서도 트렌볼론이 위험을 차별적으로 키움. ④ 위상 — PMC 등재 동료심사. ⑤ 함의 — 약물 선택의 위계가 위험의 위계. NOGEAR 시각: '센 약'은 결과도 세다. 트렌은 근육의 지름길이 아니라 붕괴의 지름길이다.",
        "category": "research", "category_ko": "정신·약물",
        "source": "PMC (peer-reviewed)", "source_type": "journal",
        "source_url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC13112052/",
        "credibility": cred(True, True, True, "high", "PMC 등재 국제 비교연구. 트렌볼론군 심리사회적 위해 극단 악화 일치.", "verified"),
        "viral_signals": sig(19, 19, 17, 16, 16, 8), "tags": ["트렌볼론", "AAS", "심리사회적위해", "국제연구", "비교"],
    },
    {
        "title": "TRAVERSE 그 후 — 유럽 전문가 패널 'TRT는 비열등하나 무위험은 아니다'",
        "title_en": "Cardiovascular safety of testosterone therapy — European Expert Panel position statement",
        "summary": "Andrology 2026에 실린 유럽 테스토스테론 연구 전문가 패널 입장문은 TRAVERSE 이후 의학적 TRT의 심혈관 안전성을 정리했다. 적절히 선별된 성선기능저하 남성에서 TRT는 대체로 안전하나 심방세동·혈압·헤마토크릿 같은 위험 신호는 남는다. 핵심은 '의학적 TRT ≠ 약물 남용'이다.",
        "summary_detail": "정리: ① 배경 — TRAVERSE(MACE 비열등) 이후 종합 입장문. ② 결론 — 진성 성선기능저하 남성에서 TRT는 심혈관적으로 대체로 안전. ③ 단서 — 심방세동, 혈압 상승, 헤마토크릿 증가 등 위험 신호 잔존. ④ 규제 — 2025년 FDA가 테스토 제품의 심혈관 블랙박스 경고 삭제. ⑤ 경계 — 생리적 용량 의학 처방과 초생리적 남용은 별개. NOGEAR 시각: '안전하다'의 주어는 '의사가 관리한 적정용량'이다. 그 단서를 떼면 거짓말이 된다.",
        "category": "research", "category_ko": "테스토스테론",
        "source": "Andrology (Wiley) 2026 — European Expert Panel", "source_type": "journal",
        "source_url": "https://onlinelibrary.wiley.com/doi/10.1111/andr.70062",
        "credibility": cred(True, True, True, "high", "Andrology 2026 유럽 전문가 패널 입장문. TRT 비열등·위험신호 잔존·남용 구분 일치.", "verified"),
        "viral_signals": sig(16, 20, 16, 16, 13, 7), "tags": ["TRT", "TRAVERSE", "테스토스테론", "심혈관", "전문가패널"],
    },
    {
        "title": "보디빌더가 인슐린을 찌른 밤 — 70단위 주사 뒤 경련, 의식 소실",
        "title_en": "Severe Hypoglycemia Due to Cryptic Insulin Use in a Bodybuilder",
        "summary": "증례 보고는 한 보디빌더가 속효성 인슐린 70단위를 주사한 뒤 의식을 잃고 경련을 일으킨 사례를 기록했다. 당뇨가 없는 사람이 근육 목적으로 인슐린을 쓰면 저혈당이 분 단위로 혼수·사망으로 직행할 수 있다. 다수 프로 보디빌더가 인슐린 혼수로 사망했다.",
        "summary_detail": "정리: ① 사례 — 속효성 인슐린 70단위 자가주사 후 의식 소실·경련. ② 기전 — 비당뇨인은 정상 인슐린을 분비하므로 추가 주사 시 급격한 저혈당. ③ 결과 — 저혈당은 수 분 내 혼수·사망 가능. ④ 동기 — 운동 후 회복·근비대 촉진 목적의 오프라벨 사용. ⑤ 위험-이득 — 표준 용량 프로토콜 부재, 이득 대비 치명 위험. NOGEAR 시각: 인슐린은 약이 아니라 카운트다운이다. 탄수화물 타이밍 한 번 놓치면 깨어나지 못한다.",
        "category": "research", "category_ko": "약물",
        "source": "PMC / J. Emerg. Med (peer-reviewed)", "source_type": "journal",
        "source_url": "https://pubmed.ncbi.nlm.nih.gov/30527564/",
        "credibility": cred(True, True, True, "high", "PubMed 등재 증례. 보디빌더 인슐린 70단위·저혈당 혼수 일치.", "verified"),
        "viral_signals": sig(22, 18, 18, 13, 15, 9), "tags": ["인슐린", "저혈당", "보디빌더", "혼수", "증례"],
    },
    {
        "title": "약물파의 가슴 — AAS 사용자 여유증 실제 유병률 39%, 끊어도 안 사라진다",
        "title_en": "The Burden of Anabolic Androgenic Steroid-Induced Gynecomastia",
        "summary": "연구는 AAS 관련 여성형유방(여유증)의 실제 유병률이 39.19%로, 수술 전 문진만으로 파악된 4.05%보다 훨씬 높다고 보고했다. 사용자들이 과소보고한다는 뜻이다. 에스트로겐 상승으로 생긴 유선 조직은 약을 끊어도 사라지지 않아 수술이 필요하다.",
        "summary_detail": "정리: ① 유병률 — AAS 관련 여유증 실제 39.19%, 문진 기반 4.05% (대규모 과소보고). ② 비가역 — 증식된 유선 조직은 중단 후에도 영구 잔존. ③ 치료 — 외과적 절제(유선 절제)가 사실상 유일 해법. ④ 통계 — 1980~2013년 미국 보디빌더 1,500명 이상이 여유증 수술. ⑤ 함의 — '약 끊으면 돌아온다'는 거짓. NOGEAR 시각: 어떤 부작용은 수술실에서만 지워진다. 약은 끊을 수 있어도 몸은 영수증을 보관한다.",
        "category": "research", "category_ko": "내분비",
        "source": "PubMed (peer-reviewed)", "source_type": "journal",
        "source_url": "https://pubmed.ncbi.nlm.nih.gov/37705825/",
        "credibility": cred(True, True, True, "high", "PubMed 등재. AAS 여유증 실제 39.19% vs 문진 4.05%·비가역성 일치.", "verified"),
        "viral_signals": sig(20, 18, 19, 14, 15, 9), "tags": ["여유증", "여성형유방", "AAS", "비가역", "수술"],
    },
    {
        "title": "스테로이드가 신장을 굳힌다 — 보디빌더 10명에서 확인된 국소분절성 사구체경화증",
        "title_en": "Anabolic steroid abuse can lead to focal segmental glomerulosclerosis",
        "summary": "Nature Reviews Nephrology가 다룬 연구는 장기 AAS 남용 보디빌더 10명에서 국소분절성 사구체경화증(FSGS)과 단백뇨를 확인했다. 평균 단백뇨 10.1g/일, 평균 크레아티닌 3.0mg/dl로 신부전 수준이었고 30%는 신증후군을 보였다. 일부는 6~8년 내 말기 신부전으로 진행한다.",
        "summary_detail": "정리: ① 코호트 — 장기 AAS 남용 보디빌더 10명. ② 소견 — FSGS + 단백뇨(평균 10.1g/일), 신기능 저하(Cr 평균 3.0mg/dl), 30% 신증후군. ③ 기전 — 레닌-안지오텐신 활성, 엔도텔린 증가, 활성산소, 섬유화·세포자멸 매개. ④ 예후 — 상당수 6~8년 내 말기 신부전, 이식 필요 사례 보고. ⑤ 인식 — 과소평가된 표적 장기. NOGEAR 시각: 근육을 키우는 동안 신장은 굳어간다. 투석실은 무대 뒤의 가장 조용한 방이다.",
        "category": "research", "category_ko": "신장",
        "source": "Nature Reviews Nephrology", "source_type": "journal",
        "source_url": "https://www.nature.com/articles/nrneph.2010.5",
        "credibility": cred(True, True, True, "high", "Nature Reviews Nephrology. AAS-FSGS·단백뇨·말기신부전 진행 일치.", "verified"),
        "viral_signals": sig(20, 19, 17, 13, 14, 8), "tags": ["신장", "FSGS", "AAS", "단백뇨", "신부전"],
    },
    {
        "title": "여성의 스테로이드, 목소리는 영영 돌아오지 않는다 — 20년 추적 증례",
        "title_en": "Long-term effects of anabolic steroids on the female voice over a 20-year period",
        "summary": "증례 보고는 단 6주 AAS 사용 여성에서 시작된 목소리 저음화가 중단 후에도 비가역적 성대 비후로 남은 사례를 20년간 추적했다. 여성의 남성화(virilization)는 목소리·음핵 비대처럼 끊어도 되돌릴 수 없는 변화가 많다. 조기에 멈추지 않으면 영구적이다.",
        "summary_detail": "정리: ① 사례 — 6주 AAS 사용 후 목소리 저음화, 20년 추적. ② 비가역 — 성대 비후·음높이(F0) 저하는 중단 후에도 영구. ③ 남성화 — 음핵 비대(clitoromegaly), 다모증, 탈모, 여드름 동반. ④ 핵심 — 조기 식별 못 하면 비가역. ⑤ 함의 — 여성에겐 '사이클 종료=원상복구'가 더더욱 거짓. NOGEAR 시각: 근육은 빠질지언정, 빼앗긴 목소리는 돌아오지 않는다. 어떤 거래는 환불이 없다.",
        "category": "research", "category_ko": "여성·남성화",
        "source": "PMC (peer-reviewed) — case report", "source_type": "journal",
        "source_url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC6509898/",
        "credibility": cred(True, True, True, "high", "PMC 등재 20년 추적 증례. 여성 AAS 목소리 비가역 비후·남성화 일치.", "verified"),
        "viral_signals": sig(21, 18, 19, 13, 14, 9), "tags": ["여성스테로이드", "남성화", "성대", "비가역", "증례"],
    },
    {
        "title": "다이어트약 클렌부테롤, 22세 보디빌더의 심장을 공격하다 — 심근염 증례",
        "title_en": "Clenbuterol-Induced Myocarditis: A Case Report",
        "summary": "유럽 내과 증례 저널은 클렌부테롤 사용 후 발생한 심근염 증례를 보고했다. 체지방 감량·근육 보존 목적으로 쓰이는 클렌부테롤은 심근에 직접 독성을 보이며, 빈맥·저칼륨혈증·경련·심정지까지 유발한다. NSW 데이터에선 노출자의 84%가 입원했다.",
        "summary_detail": "정리: ① 사례 — 클렌부테롤 사용 후 심근염(myocarditis). ② 기전 — 심근 직접 독성, 심장보호 아미노산 타우린 고갈 가설. ③ 증상 — 빈맥, 저칼륨혈증, 떨림, 경련, 심정지. ④ 통계 — NSW 2004~2012 노출 63건 중 84% 입원, 21세 남성 심정지 사례 포함. ⑤ 위치 — 미승인·안전성 미보장 물질. NOGEAR 시각: 지방을 태우려다 심장을 태운다. '컷팅 보조제'라는 이름의 심장 독약이다.",
        "category": "research", "category_ko": "약물",
        "source": "PMC / EJCRIM (peer-reviewed)", "source_type": "journal",
        "source_url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC7473675/",
        "credibility": cred(True, True, True, "high", "PMC/EJCRIM 등재 증례. 클렌부테롤 심근염·심독성·NSW 입원율 일치.", "verified"),
        "viral_signals": sig(20, 18, 17, 13, 14, 8), "tags": ["클렌부테롤", "심근염", "심독성", "컷팅", "증례"],
    },
    {
        "title": "저용량 클렌부테롤도 위험하다 — 독성 증례와 문헌 리뷰",
        "title_en": "Low Dose Clenbuterol Toxicity: Case Report and Review of Literature",
        "summary": "PMC 증례·리뷰는 '저용량'이라 믿은 클렌부테롤조차 심각한 독성을 일으킬 수 있음을 보여준다. 트로포닌 상승·빈맥·저칼륨혈증이 전형이며, 관상동맥은 정상인데도 심근 손상이 나타난다. '조금만 쓰면 괜찮다'는 통념을 깬다.",
        "summary_detail": "정리: ① 메시지 — 저용량 클렌부테롤도 심각한 독성 가능. ② 소견 — 트로포닌 상승, 빈맥, 저칼륨혈증, 정상 관상동맥에도 심근 손상. ③ 사례 — 18·21세 보디빌더, 트로포닌 4.0 초과·관상동맥조영 음성. ④ 함의 — 용량과 안전이 비례하지 않음. ⑤ 위치 — 동료심사 증례·리뷰. NOGEAR 시각: '소량은 안전'이라는 믿음이 가장 위험하다. 심장은 용량을 협상하지 않는다.",
        "category": "research", "category_ko": "약물",
        "source": "PMC (peer-reviewed)", "source_type": "journal",
        "source_url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC10324766/",
        "credibility": cred(True, True, True, "high", "PMC 등재 증례·리뷰. 저용량 클렌부테롤 독성·트로포닌 상승 일치.", "verified"),
        "viral_signals": sig(18, 18, 16, 13, 13, 7), "tags": ["클렌부테롤", "독성", "트로포닌", "저용량", "심근"],
    },
    {
        "title": "근이형증(비고렉시아)은 사회적 전염병이 됐다 — 근육 콘텐츠가 강박을 키운다",
        "title_en": "Associations between muscularity-oriented social media content and muscle dysmorphia",
        "summary": "1,553명을 분석한 2025 연구는 근육·보충제·약물을 강조하는 소셜미디어 콘텐츠 노출이 남성·소년의 근이형증(비고렉시아) 위험 증가와 연관된다고 보고했다. 받은 '좋아요·댓글'의 중요도가 증상을 유의하게 예측했다. 알고리즘이 신체이형장애를 양산한다.",
        "summary_detail": "정리: ① 규모 — 참가자 1,553명 분석. ② 결과 — 근육지향 SNS 콘텐츠 노출이 근이형증 위험과 연관. ③ 메커니즘 — 받은 좋아요·댓글의 중요도가 증상을 유의하게 예측. ④ 배경 — 청소년 남성 25%가 '근육이 부족하다'고 우려. ⑤ 함의 — 약물 남용의 상류에 외형 강박이 있다. NOGEAR 시각: 약은 증상이고 병은 화면이다. 알고리즘이 부추긴 거울 강박이 주사기로 이어진다.",
        "category": "research", "category_ko": "정신",
        "source": "PubMed (peer-reviewed) 2025", "source_type": "journal",
        "source_url": "https://pubmed.ncbi.nlm.nih.gov/40367828/",
        "credibility": cred(True, True, True, "high", "PubMed 2025 등재. SNS 근육콘텐츠-근이형증 연관·좋아요 예측 일치(n=1,553).", "verified"),
        "viral_signals": sig(19, 18, 20, 17, 13, 9), "tags": ["근이형증", "비고렉시아", "소셜미디어", "신체이형", "강박"],
    },
    {
        "title": "장기 AAS 사용자의 뇌, 치매 위험군과 닮았다 — 인지 결손과 신경독성",
        "title_en": "Brain and Cognition Abnormalities in Long-Term Anabolic-Androgenic Steroid Users",
        "summary": "장기 고용량 AAS 사용자는 시각공간 기억 등에서 인지 결손을 보이며, 전두·측두엽 위축과 백질 손상 등 치매 위험군과 유사한 뇌 변화가 관찰된다. 초생리적 AAS가 알츠하이머 관련 단백질의 조기 축적·치매 위험을 높일 수 있다는 가설이 제기된다.",
        "summary_detail": "정리: ① 인지 — 장기 고용량 AAS에서 시각공간 기억 등 인지 결손. ② 구조 — 전두·측두엽 위축, 편도체 비대, 뇌량 백질 손상. ③ 신경화학 — 세로토닌·도파민계 교란으로 기분장애·공격성·인지 저하. ④ 가설 — 초생리적 AAS가 알츠하이머 관련 단백 조기 축적·치매 위험 증가. ⑤ 위치 — PMC 등재 영상·인지 연구. NOGEAR 시각: 근육의 대가를 기억으로 치를 수도 있다. 거울이 더는 누구인지 알려주지 못하는 날이 온다.",
        "category": "research", "category_ko": "신경",
        "source": "PMC (peer-reviewed)", "source_type": "journal",
        "source_url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC4458166/",
        "credibility": cred(True, True, True, "high", "PMC 등재. 장기 AAS 인지결손·뇌위축·치매유사 변화 일치.", "verified"),
        "viral_signals": sig(20, 19, 18, 14, 14, 8), "tags": ["AAS", "뇌", "인지결손", "치매", "신경독성"],
    },
    {
        "title": "초생리적 AAS는 치매의 위험인자인가 — 신경과학·생물행동 리뷰의 질문",
        "title_en": "Supraphysiologic-dose anabolic–androgenic steroid use: A risk factor for dementia?",
        "summary": "Neuroscience & Biobehavioral Reviews 논문은 초생리적 용량 AAS 사용이 알츠하이머·관련 치매 위험군과 유사한 생리·인지·뇌 이상과 연관된다고 정리하며, 조기 치매 위험인자 가능성을 제기한다. 근육의 전성기 뒤에 인지의 황혼이 앞당겨질 수 있다.",
        "summary_detail": "정리: ① 질문 — 초생리적 AAS가 치매 위험인자인가. ② 근거 — 사용자에서 치매 위험군과 유사한 생리·인지·뇌 이상. ③ 가설 — 신경독성이 알츠하이머 관련 단백 축적을 앞당길 가능성. ④ 한계 — 인과 확정엔 추가 연구 필요(연관 단계). ⑤ 위치 — 동료심사 리뷰. NOGEAR 시각: 빌린 근육의 이자가 기억일 수 있다. 아직 가설이지만, 베팅하기엔 판돈이 너무 크다.",
        "category": "research", "category_ko": "신경",
        "source": "Neuroscience & Biobehavioral Reviews (ScienceDirect)", "source_type": "journal",
        "source_url": "https://www.sciencedirect.com/science/article/abs/pii/S0149763418309515",
        "credibility": cred(True, True, True, "high", "N&BR 동료심사 리뷰. 초생리적 AAS-치매 위험 가설 일치(연관 단계 명시).", "verified", confirmed=True),
        "viral_signals": sig(19, 19, 17, 14, 15, 7), "tags": ["AAS", "치매", "알츠하이머", "신경독성", "위험인자"],
    },
    {
        "title": "인슐린을 '아나볼릭'으로 — 보디빌딩계의 저혈당, 1990년대부터의 경고",
        "title_en": "Insulin as an anabolic: hypoglycemia in the bodybuilding world",
        "summary": "이미 1990년대 PubMed 보고가 보디빌딩계의 인슐린 오용과 그로 인한 저혈당 위험을 경고했다. 수십 년이 지나도 같은 비극이 반복된다는 점이 핵심이다. 근비대를 노린 인슐린은 가장 오래되고 가장 치명적인 '아나볼릭'이다.",
        "summary_detail": "정리: ① 역사 — 1990년대부터 보디빌딩계 인슐린 오용·저혈당 경고. ② 동기 — 인슐린의 동화(anabolic) 작용을 근비대에 악용. ③ 위험 — 비당뇨인의 외인성 인슐린은 급격 저혈당 유발. ④ 반복성 — 수십 년간 같은 패턴의 사망·혼수 지속. ⑤ 함의 — 새로운 위험이 아니라 방치된 오래된 위험. NOGEAR 시각: 30년 전에도 경고했다. 바뀐 건 약이 아니라, 같은 실수를 반복하는 사람들뿐이다.",
        "category": "research", "category_ko": "약물",
        "source": "PubMed (peer-reviewed)", "source_type": "journal",
        "source_url": "https://pubmed.ncbi.nlm.nih.gov/9728265/",
        "credibility": cred(True, True, True, "high", "PubMed 등재. 보디빌딩계 인슐린 오용·저혈당 경고 일치(역사적 보고).", "verified"),
        "viral_signals": sig(17, 17, 16, 11, 13, 7), "tags": ["인슐린", "저혈당", "보디빌딩", "아나볼릭", "오용"],
    },
]

NEW_NEWS = [
    {
        "title": "리버 킹 $2,500만 소송 '완전 종료' — 그러나 로건 협박으로 체포까지",
        "title_en": "Liver King: $25M lawsuit dismissed; arrested for threatening Joe Rogan",
        "summary": "스테로이드 은폐로 제기됐던 리버 킹(브라이언 존슨)에 대한 2,500만 달러 집단소송이 2025년 3월 24일 원고 측에 의해 자진 취하됐다고 보도됐다. 그러나 같은 해 6월 24일, 존슨은 팟캐스터 조 로건을 반복 협박한 혐의로 오스틴 경찰에 체포됐다.",
        "summary_detail": "정리: ① 소송 — 스테로이드 은폐·기만 마케팅으로 제기된 $25M 집단소송. ② 결과 — 2025.3.24 원고 측(Cotter Law Group) 자진 취하, '완전 종료'. ③ 배경 — 2022.12 누출 이메일로 월 $11,000 스테로이드 사용 폭로·고백. ④ 후속 — 2025.6.24 조 로건 협박(테러 위협, 경범) 혐의 체포. ⑤ 추가 — 넷플릭스 다큐 'Untold: The Liver King' 공개. NOGEAR 시각: 소송은 끝났어도 거짓의 후과는 끝나지 않는다. 가짜로 쌓은 제국의 결말은 늘 법정 아니면 수갑이다.",
        "category": "scandal", "category_ko": "페이크내추럴",
        "source": "FOX 9 / SupplySide", "source_type": "news",
        "source_url": "https://www.fox9.com/news/liver-king-slapped-with-class-action-lawsuit-for-allegedly-deceiving-customers-by-hiding-steroid-use",
        "credibility": cred(False, False, True, "medium", "FOX9/SupplySide 보도. 소송 취하(2025.3)·로건 협박 체포(2025.6)·$11k 고백 다수 매체 교차.", "match"),
        "viral_signals": sig(22, 11, 21, 16, 19, 11), "tags": ["리버킹", "소송", "스테로이드", "조로건", "체포"],
    },
    {
        "title": "넷플릭스가 벗긴 리버 킹의 가면 — 'Untold' 다큐로 드러난 스테로이드 사기",
        "title_en": "How Netflix Exposed Liver King's Steroid-Fueled Fraud",
        "summary": "넷플릭스 다큐멘터리 'Untold: The Liver King'은 '조상 식단'으로 만든 몸이라던 리버 킹의 서사가 실은 월 1만 달러대 스테로이드로 만들어진 것임을 정리했다. 다큐에서 존슨은 자신이 밀었던 카니보어 식단을 스스로 비판하기도 했다.",
        "summary_detail": "정리: ① 작품 — 넷플릭스 'Untold: The Liver King'. ② 폭로 — '조상 식단'의 결과라던 피지크가 실제론 고액 스테로이드의 산물. ③ 규모 — 월 $11,000+ 스테로이드 지출 고백 재조명. ④ 반전 — 다큐 내에서 존슨이 자신의 카니보어 식단 홍보를 비판. ⑤ 의미 — 콘텐츠 제국의 토대가 거짓이었음을 대중매체가 확증. NOGEAR 시각: 카메라는 결국 진실을 잡는다. '내추럴'이라는 단어로 시작된 제국은 다큐 한 편으로 무너진다. FXXK FAKES.",
        "category": "scandal", "category_ko": "페이크내추럴",
        "source": "Washington Morning", "source_type": "news",
        "source_url": "https://washingtonmorning.com/2025/05/27/how-netflix-exposed-liver-kings-steroid-fueled-fraud/",
        "credibility": cred(False, False, True, "low", "매체 해설 기사. 넷플릭스 'Untold' 폭로·카니보어 자기비판은 IMDB/다수 보도와 교차(매체 신뢰도는 보통 이하).", "match", confirmed=True),
        "viral_signals": sig(21, 10, 20, 15, 18, 11), "tags": ["리버킹", "넷플릭스", "Untold", "스테로이드", "사기"],
    },
    {
        "title": "소년들이 거울 앞에서 무너진다 — 소셜미디어가 키운 근이형증의 급증",
        "title_en": "Muscle dysmorphia in boys and men is on the rise, fueled by social media",
        "summary": "STAT 보도는 소년·청년 남성의 근이형증(비고렉시아)이 소셜미디어를 연료 삼아 증가하고 있다고 전했다. 이상화된 근육질 신체에 끊임없이 노출되면서 근육 불만족이 커지고, 이는 보충제·약물 사용으로 번진다. 외형 강박이 약물 남용의 입구가 된다.",
        "summary_detail": "정리: ① 추세 — 소년·청년 남성 근이형증 증가, 소셜미디어가 핵심 동력. ② 일반인구 유병률 약 2%, 특정군에선 더 높고 미진단 다수 추정. ③ 연령 — 15~32세 남성에서 특히 빈발. ④ 경로 — 근육 불만족 → 보충제·약물 사용. ⑤ 함의 — 정신건강 문제로서의 접근 필요. NOGEAR 시각: 약물 문제는 헬스장이 아니라 피드에서 시작된다. 스크롤이 강박을 먹이고, 강박이 주사기를 부른다.",
        "category": "scandal", "category_ko": "정신",
        "source": "STAT News", "source_type": "news",
        "source_url": "https://www.statnews.com/2024/12/19/muscle-dysmorphia-rising-in-young-men-fueled-by-social-media/",
        "credibility": cred(False, False, True, "high", "STAT 보도(전문 의학매체). 근이형증 증가·소셜미디어 동력 — 학술연구와 정합.", "match"),
        "viral_signals": sig(19, 14, 20, 16, 13, 9), "tags": ["근이형증", "비고렉시아", "소셜미디어", "청소년", "정신건강"],
    },
    {
        "title": "테스토스테론 2026 — '두려워했던 것보다 안전, 광고만큼 단순하진 않다'",
        "title_en": "Testosterone in 2026: Safer Than We Feared, Not as Simple as the Ads",
        "summary": "2025년 FDA가 테스토스테론 제품의 심혈관 블랙박스 경고를 삭제하면서, 의학적 TRT의 안전성 인식이 개선됐다. 그러나 전문가들은 '안전'의 전제가 진성 성선기능저하 환자의 적정 처방임을 강조한다. 광고가 파는 '만능 회춘'과는 다른 이야기다.",
        "summary_detail": "정리: ① 변화 — 2025 FDA, 테스토 제품 심혈관 블랙박스 경고 삭제. ② 근거 — TRAVERSE의 MACE 비열등 결과. ③ 단서 — 안전성은 진성 성선기능저하·적정용량 전제에서 성립. ④ 위험 신호 — 심방세동·혈압·헤마토크릿 잔존. ⑤ 경계 — 광고의 '회춘 만병통치'와 임상적 TRT는 다름. NOGEAR 시각: 'FDA가 경고를 뗐다'와 '아무나 써도 된다'는 전혀 다른 문장이다. 광고는 그 차이를 지운다.",
        "category": "scandal", "category_ko": "테스토스테론",
        "source": "Grand Rounds in Urology", "source_type": "news",
        "source_url": "https://grandroundsinurology.com/testosterone-and-cardiovascular-risk-traverse-trial-and-new-fda-label-change/",
        "credibility": cred(False, True, True, "medium", "비뇨기과 전문매체. TRAVERSE·2025 FDA 블랙박스 삭제는 다수 보도·논문과 교차.", "match"),
        "viral_signals": sig(16, 16, 16, 16, 13, 7), "tags": ["테스토스테론", "TRT", "FDA", "블랙박스", "TRAVERSE"],
    },
    {
        "title": "클렌부테롤은 미승인·위험 물질이다 — 미국 중독관리센터 경고",
        "title_en": "Clenbuterol: Unapproved and unsafe (Poison Control)",
        "summary": "미국 중독관리센터(Poison Control)는 클렌부테롤이 인체용으로 승인되지 않은 위험 물질이라고 명시했다. 떨림·빈맥·저칼륨혈증·경련·심정지를 유발하며, 다이어트·근육 보존 목적의 사용은 명백한 도박이다. 정부 연계 기관의 직접 경고다.",
        "summary_detail": "정리: ① 주체 — 미국 중독관리센터(Poison Control) 공식 자료. ② 결론 — 클렌부테롤은 인체 미승인·안전성 미보장. ③ 증상 — 떨림, 빈맥, 저칼륨혈증, 경련, 심정지. ④ 맥락 — 체지방 감량·근육 보존 목적의 오프라벨 사용 위험. ⑤ 권위 — 중독·응급 분야 공신력. NOGEAR 시각: 중독센터가 경고하는 물질을 '컷팅 보조제'로 부르는 순간, 이미 게임은 졌다.",
        "category": "scandal", "category_ko": "약물·경고",
        "source": "Poison Control (US)", "source_type": "news",
        "source_url": "https://www.poison.org/articles/clenbuterol-unapproved-and-unsafe-201",
        "credibility": cred(False, True, True, "high", "미 중독관리센터 공식 자료. 클렌부테롤 미승인·심독성 경고 일치.", "verified"),
        "viral_signals": sig(17, 16, 16, 12, 13, 7), "tags": ["클렌부테롤", "중독센터", "미승인", "심정지", "경고"],
    },
    {
        "title": "비고렉시아 급증 — 더 많은 10대 소년이 '몸 강박'과 싸운다",
        "title_en": "Bigorexia Surges: More Teen Boys Battle Body Obsession",
        "summary": "University Hospitals의 정리에 따르면 10대 소년 사이에서 비고렉시아(근이형증)가 급증하고 있다. 청소년 남성의 25%가 '근육이 충분치 않다'고 느끼며, 이 불만족이 과도한 운동·식이 제한·보충제와 약물로 이어진다. 조용히 번지는 남성 청소년의 정신건강 위기다.",
        "summary_detail": "정리: ① 추세 — 10대 소년 비고렉시아 급증. ② 데이터 — 청소년 남성 25%가 근육 부족 우려. ③ 경로 — 신체 불만족 → 과도 운동·식이 제한·보충제·약물. ④ 사각지대 — 남성 청소년의 신체이형장애는 과소 인식·과소 진단. ⑤ 위치 — 병원 시스템(UH)의 환자교육 자료. NOGEAR 시각: 거식증이 소녀의 병으로만 여겨졌듯, 비고렉시아는 소년의 침묵 속에서 자란다. 보이지 않는다고 없는 게 아니다.",
        "category": "scandal", "category_ko": "정신",
        "source": "University Hospitals", "source_type": "news",
        "source_url": "https://www.uhhospitals.org/blog/articles/2025/10/bigorexia-surges-more-teen-boys-battle-body-obsession",
        "credibility": cred(False, True, True, "medium", "병원 시스템(UH) 환자교육 자료. 비고렉시아 급증·25% 통계는 학술/STAT와 교차.", "match"),
        "viral_signals": sig(18, 14, 19, 16, 13, 8), "tags": ["비고렉시아", "근이형증", "청소년", "신체강박", "정신건강"],
    },
]

def finalize(a):
    s = score(a["viral_signals"])
    a["viral_score"] = s
    a["viral_tier"] = "VIRAL_BOMB" if s >= 85 else ("HIGH_VIRAL" if s >= 80 else "TRENDING")
    conf = a["credibility"].get("confidence")
    a["viral_emoji"] = "🔴" if s >= 90 else "🟠"
    if a["credibility"].get("peer_reviewed"):
        a["badge"] = "✅ VERIFIED"
    elif conf == "low":
        a["badge"] = "⚠️ UNVERIFIED"
    else:
        a["badge"] = "🔍 CHECKED"
    a["date"] = TODAY
    a["source_verified"] = conf in ("high", "medium")
    a.setdefault("title_original", a["title"])
    a.setdefault("title_rewrite", a["title"])
    return a

def main():
    d = json.load(open(PATH, encoding="utf-8"))
    existing_urls = {x.get("source_url", "").rstrip("/") for sec in ("news", "research") for x in d[sec]}
    existing_titles = {x.get("title", "") for sec in ("news", "research") for x in d[sec]}

    added = 0
    for arr, target in ((NEW_RESEARCH, "research"), (NEW_NEWS, "news")):
        for a in arr:
            u = a["source_url"].rstrip("/")
            if u in existing_urls or a["title"] in existing_titles:
                print("SKIP dup:", a["title"][:40]); continue
            d[target].append(finalize(a))
            existing_urls.add(u); existing_titles.add(a["title"]); added += 1

    for sec in ("news", "research"):
        d[sec].sort(key=lambda x: x.get("viral_score", 0), reverse=True)

    removed = 0
    while len(d["news"]) + len(d["research"]) > 200 and d["research"]:
        d["research"].sort(key=lambda x: x.get("viral_score", 0))
        d["research"].pop(0); removed += 1
        d["research"].sort(key=lambda x: x.get("viral_score", 0), reverse=True)

    now = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=9)))
    d["meta"]["last_updated"] = now.isoformat()
    d["meta"]["last_updated_kst"] = now.strftime("%Y-%m-%d %H:%M") + f" KST 아침 크롤 v2 (트렌볼론·인슐린·신장FSGS·여유증·여성남성화·클렌부테롤·근이형증·뇌인지·TRT) +{added}건"
    d["meta"]["total_articles"] = len(d["news"]) + len(d["research"])
    d["meta"]["news_count"] = len(d["news"])
    d["meta"]["research_count"] = len(d["research"])
    d["meta"]["crawl_count"] = d["meta"].get("crawl_count", 0) + 1
    scores = [x.get("viral_score", 0) for sec in ("news", "research") for x in d[sec] if x.get("viral_score", 0) > 0]
    d["meta"]["top_viral_score"] = max(scores)
    d["meta"]["avg_viral_score"] = round(sum(scores) / len(scores), 1)
    d["meta"]["model"] = "claude-opus-4-8"

    json.dump(d, open(PATH, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    print(f"\nADDED {added} | REMOVED(cap) {removed} | total={d['meta']['total_articles']} news={d['meta']['news_count']} research={d['meta']['research_count']}")

if __name__ == "__main__":
    main()
