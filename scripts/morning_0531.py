#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""NOGEAR 아침 크롤 — 2026-05-31. 신규 기사 병합/중복제거/정렬/200 cap.
   ⚠️ 모든 URL은 2026-05-31 WebSearch 결과에서 1:1로 확인된 실제 링크만 사용.
   (검색 도구가 placeholder로 표기한 URL은 전량 제외)"""
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

# ============ RESEARCH ============
NEW_RESEARCH = [
    {
        "title": "AAS의 진짜 청구서는 '아랫도리' — 발기부전·무정자증, 끊어도 절반만 돌아온다",
        "title_en": "Health consequences of anabolic steroids: a sexual-medicine perspective",
        "summary": "2026년 국제발기부전학회지(IJIR) 리뷰는 AAS가 시상하부-뇌하수체-생식샘(HPG) 축을 억제해 성욕 감퇴·발기부전·여성형유방·정자 감소(중증 희소정자~무정자증)를 부른다고 정리했다. 핵심은 회복의 이질성이다. 호르몬 수치는 비교적 빨리 정상화돼도 정액 지표 회복은 지연·불완전한 경우가 임상적으로 의미 있게 존재한다. 고용량·장기 사용일수록 회복은 멀어진다.",
        "summary_detail": "정리: ① 기전 — 외인성 안드로겐이 HPG 축을 억제, 내인성 테스토스테론·정자 생성이 셧다운. ② 증상 — 성욕 저하, 발기부전, 여성형유방, 희소정자증에서 무정자증까지. ③ 회복 — 내분비 수치는 비교적 조기 회복되나 정액 지표는 지연·불완전한 사례가 임상적으로 유의미. ④ 위험군 — 고용량·장기 노출일수록 지연·불완전 회복 비율 증가. ⑤ 함의 — '사이클 끝나면 원상복구'는 환상. NOGEAR 시각: 트로피보다 먼저 사라지는 건 생식 능력이다. 자연은 빌려주는 게 아니라 청구한다 — 어떤 청구서는 영영 미납으로 남는다.",
        "category": "research", "category_ko": "생식·성",
        "source": "International Journal of Impotence Research 2026", "source_type": "journal",
        "source_url": "https://www.nature.com/articles/s41443-026-01272-1",
        "credibility": cred(True, True, True, "high", "Nature 계열 IJIR 2026 성의학 리뷰. HPG축 억제·정액지표 회복 이질성 기술 일치.", "verified"),
        "viral_signals": sig(20, 20, 20, 16, 14, 8), "tags": ["AAS", "발기부전", "무정자증", "HPG축", "생식"],
    },
    {
        "title": "교과서가 말하는 아나볼릭 스테로이드 — 근육 1, 부작용 9",
        "title_en": "Anabolic Steroids — StatPearls",
        "summary": "의학 표준 레퍼런스 StatPearls는 AAS를 안드로겐 수용체로 단백질 합성·근비대를 촉진하는 동시에 HPG 축을 교란하고 심혈관·간·신경내분비계 전반에 영향을 주는 약물로 규정한다. '근육을 키운다'는 한 줄 효능 뒤에 전신 부작용 목록이 줄을 선다.",
        "summary_detail": "정리: ① 작용 — 안드로겐 수용체 결합으로 단백질 합성·근비대 촉진. ② 교란 — 시상하부-뇌하수체-생식샘 축 dysregulation. ③ 표적 장기 — 심혈관, 간, 신경내분비계 전반. ④ 위치 — 의학 표준 레퍼런스(StatPearls)에 정식 등재된 임상 항목. ⑤ 의미 — 부작용이 일화가 아니라 교과서 사실이라는 뜻. NOGEAR 시각: 효능은 한 문단, 부작용은 한 챕터다. 그 비율이 곧 진실이다.",
        "category": "research", "category_ko": "스테로이드",
        "source": "StatPearls / NCBI Bookshelf", "source_type": "journal",
        "source_url": "https://www.ncbi.nlm.nih.gov/books/NBK482418/",
        "credibility": cred(True, True, True, "high", "StatPearls 'Anabolic Steroids' 의학 레퍼런스. 작용기전·표적장기 기술 일치.", "verified"),
        "viral_signals": sig(17, 20, 18, 13, 12, 7), "tags": ["AAS", "StatPearls", "근비대", "부작용", "기전"],
    },
    {
        "title": "초생리적 용량 AAS, 심장을 다시 빚는다 — 심근 리모델링·혈전·염증",
        "title_en": "Anabolic-androgenic steroids at supraphysiological doses: cardiovascular impacts",
        "summary": "초생리적(정상치 초과) 용량의 AAS는 심장 구조 자체를 리모델링하고 혈관 기능을 떨어뜨린다. 고용량은 혈전·이상지질혈증·염증 위험을 동시에 끌어올린다. 단순 '심장에 안 좋다' 수준이 아니라, 심장의 물리적 형태와 기능이 바뀌는 병태생리다.",
        "summary_detail": "정리: ① 리모델링 — 초생리적 AAS가 심근 비대·심장 구조 변형을 유발. ② 혈관 — 내피·혈관 기능장애. ③ 혈액 — 혈전 경향 증가, HDL 저하 등 이상지질혈증. ④ 염증 — 전신 염증 지표 상승. ⑤ 누적 — 사이클을 거듭할수록 변화가 축적·고착. NOGEAR 시각: 심장은 근육이지만, 펌프지 트로피가 아니다. 더 크게 만든 심벽이 더 빨리 멈추게 한다.",
        "category": "research", "category_ko": "심혈관",
        "source": "ScienceDirect (peer-reviewed) 2026", "source_type": "journal",
        "source_url": "https://www.sciencedirect.com/science/article/pii/S096007602600004X",
        "credibility": cred(True, True, True, "high", "ScienceDirect 동료심사 논문. 초생리적 AAS 심근 리모델링·혈전·이상지질혈증 병태생리 일치.", "verified"),
        "viral_signals": sig(19, 19, 17, 16, 14, 8), "tags": ["AAS", "심근비대", "심혈관", "혈전", "이상지질혈증"],
    },
    {
        "title": "스테로이드 쓰는 남자들에게 물었다 — 부작용 알면서도 병원은 안 간다",
        "title_en": "Health service engagement, side effects and concerns among men with AAS use (Norway)",
        "summary": "노르웨이 단면 연구는 AAS를 사용하는 남성들의 부작용 경험과 의료 이용 실태를 직접 조사했다. 다수가 부작용을 자각하면서도 낙인·불신 탓에 의료 서비스 이용을 꺼린다는 점이 드러났다. 위험은 큰데 안전망은 비어 있는 구조다.",
        "summary_detail": "정리: ① 설계 — AAS 사용 남성 대상 단면(cross-sectional) 조사. ② 부작용 — 상당수가 신체·정신 부작용을 직접 경험·자각. ③ 회피 — 낙인과 의료진 불신으로 진료·검사 회피. ④ 공백 — 위험 노출은 높은데 모니터링·상담 접근성은 낮음. ⑤ 함의 — 해악 감소 체계의 필요성을 데이터로 뒷받침. NOGEAR 시각: 부작용을 모르는 게 아니다. 알면서도 거울 앞을 떠나지 못하는 것 — 그게 더 무섭다.",
        "category": "research", "category_ko": "역학",
        "source": "PMC (peer-reviewed) — Norwegian study", "source_type": "journal",
        "source_url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10071723/",
        "credibility": cred(True, True, True, "high", "PMC 등재 노르웨이 단면연구. AAS 사용 남성 부작용·의료회피 실태 일치.", "verified"),
        "viral_signals": sig(17, 18, 18, 14, 14, 7), "tags": ["AAS", "역학", "노르웨이", "의료회피", "해악감소"],
    },
    {
        "title": "프로 보디빌더, 일반인보다 돌연사 위험 5배 — 미국심장학회 확인",
        "title_en": "Professional Bodybuilding Linked to Increased Risk of SCD (ACC)",
        "summary": "미국심장학회(ACC) 저널 스캔은 프로로 경쟁하는 남성 보디빌더의 돌연심장사(SCD) 위험이 아마추어 대비 약 5.2배(위험비 5.23)라고 전했다. 경쟁 수준이 높을수록 위험이 가파르게 오른다. 무대 위 완성도의 대가가 심장으로 청구된다.",
        "summary_detail": "정리: ① 수치 — 프로 보디빌더의 SCD 위험비(HR) 약 5.23, 아마추어 대비 현저히 높음. ② 해석 — 경쟁 강도와 위험이 비례. ③ 배경 — PED 사용, 극단적 강도 훈련, 대회 직전 급격 감량·탈수가 심장을 동시 압박. ④ 권위 — 업계 매체가 아닌 미국심장학회(ACC) 채널의 정리. ⑤ 함의 '돌연사'는 우연이 아니라 통계다. NOGEAR 시각: 5배. 그게 무대 조명 뒤에 적힌 진짜 숫자다.",
        "category": "research", "category_ko": "심혈관",
        "source": "American College of Cardiology", "source_type": "journal",
        "source_url": "https://www.acc.org/Latest-in-Cardiology/Journal-Scans/2025/05/29/13/29/Mortality-SCD-Higher",
        "credibility": cred(False, True, True, "high", "ACC 저널 스캔. 프로 보디빌더 SCD HR 5.23은 EHJ 원논문 기반.", "verified"),
        "viral_signals": sig(21, 19, 18, 16, 15, 9), "tags": ["보디빌더", "돌연사", "SCD", "ACC", "심장"],
    },
    {
        "title": "보디빌더는 왜 일찍 죽는가 — 사망 121건, 평균 45세",
        "title_en": "Premature Death in Bodybuilders: What Do We Know?",
        "summary": "남성 보디빌더 사망 사례를 모은 분석에서 121건의 사망이 확인됐고 평균 사망 연령은 45세였다. 이 중 46건(38%)이 돌연심장사였으며, 현역 경쟁 선수 11명이 포함됐다. 부검에서는 심장 비대·심실 비대가 공통적으로 발견됐다.",
        "summary_detail": "정리: ① 규모 — 121건 사망, 평균 사망연령 45세. ② SCD — 46건(전체 38%)이 돌연심장사, 현역 경쟁자 11명 포함. ③ 부검 — 심장비대·심실비대가 공통 소견. ④ 추정 원인 — AAS/PED 남용, 극단 훈련, 급격 감량·탈수. ⑤ 의미 — '한두 명의 비극'이 아니라 패턴화된 통계. NOGEAR 시각: 45세. 트로피를 다 모으기도 전에 멈추는 심장의 평균값이다.",
        "category": "research", "category_ko": "심혈관",
        "source": "PMC (peer-reviewed)", "source_type": "journal",
        "source_url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC9885939/",
        "credibility": cred(True, True, True, "high", "PMC 등재 리뷰. 121건 사망·평균45세·46건 SCD·심장비대 부검소견 일치.", "verified"),
        "viral_signals": sig(22, 19, 18, 15, 15, 9), "tags": ["보디빌더사망", "돌연사", "심장비대", "평균45세", "부검"],
    },
    {
        "title": "유럽심장학회: 남성 보디빌더 돌연심장사 위험 높다 — 특히 프로",
        "title_en": "Male bodybuilders face high risk of sudden cardiac death (ESC)",
        "summary": "유럽심장학회(ESC)는 남성 보디빌더, 특히 프로로 경쟁하는 이들의 돌연심장사 위험이 높다고 공식 발표했다. 유럽심장저널(EHJ)에 실린 대규모 분석을 근거로 한 경고다. 권위 있는 심장 학회가 직접 '위험하다'고 못 박았다.",
        "summary_detail": "정리: ① 발표 — ESC 보도자료, 남성 보디빌더 SCD 위험 경고. ② 근거 — 유럽심장저널(EHJ) 대규모 사망 분석. ③ 강조 — 프로 경쟁군에서 위험 특히 높음. ④ 원인 — PED·극단 훈련·감량이 복합 작용. ⑤ 권위 — 세계 최대 심장 학회 중 하나의 공식 입장. NOGEAR 시각: 학회가 보도자료까지 낸다는 건, 더는 '카더라'가 아니란 뜻이다.",
        "category": "research", "category_ko": "심혈관",
        "source": "European Society of Cardiology", "source_type": "journal",
        "source_url": "https://www.escardio.org/The-ESC/Press-Office/Press-releases/male-bodybuilders-face-high-risk-of-sudden-cardiac-death-especially-those-who-compete-professionally",
        "credibility": cred(False, True, True, "high", "ESC 공식 보도자료, EHJ 원논문 기반. 보디빌더 SCD 위험 경고 일치.", "verified"),
        "viral_signals": sig(20, 19, 17, 16, 14, 8), "tags": ["보디빌더", "돌연사", "ESC", "심장", "프로"],
    },
    {
        "title": "유럽심장저널 원논문 — 남성 보디빌딩 선수의 사망률",
        "title_en": "Mortality in male bodybuilding athletes (European Heart Journal)",
        "summary": "유럽심장저널(EHJ)에 실린 원논문은 남성 보디빌딩 선수의 사망률을 정량 분석했다. 돌연심장사가 사망의 큰 비중을 차지했고 경쟁 수준이 높을수록 위험이 컸다. 앞선 ACC·ESC 발표의 근거가 된 1차 자료다.",
        "summary_detail": "정리: ① 위치 — EHJ(Vol 46, p.3006) 동료심사 원논문. ② 결과 — 보디빌딩 선수 사망에서 SCD 비중 높음. ③ 경향 — 프로 경쟁군에서 위험비 급증. ④ 위상 — ACC 저널스캔·ESC 보도의 원천 데이터. ⑤ 의미 — 2차 인용이 아닌 1차 근거를 직접 확인 가능. NOGEAR 시각: 숫자의 출처를 따라가면, 결국 멈춘 심장들에 닿는다.",
        "category": "research", "category_ko": "심혈관",
        "source": "European Heart Journal (Oxford Academic)", "source_type": "journal",
        "source_url": "https://academic.oup.com/eurheartj/article/46/30/3006/8131432",
        "credibility": cred(True, True, True, "high", "EHJ 동료심사 원논문(46:3006). ACC/ESC 발표의 1차 근거.", "verified"),
        "viral_signals": sig(18, 20, 16, 15, 13, 7), "tags": ["보디빌더", "사망률", "EHJ", "돌연사", "원논문"],
    },
    {
        "title": "AAS 사용자의 돌연심장사 — 문헌 리뷰가 정리한 죽음의 기전",
        "title_en": "Sudden Cardiac Death in Anabolic-Androgenic Steroid Users: A Literature Review",
        "summary": "AAS 사용자에서 발생한 돌연심장사 사례를 모은 문헌 리뷰는 좌심실 비대, 심근 섬유화, 부정맥 유발 기질을 공통 기전으로 지목한다. 멀쩡해 보이던 근육질 심장이 어느 날 멈추는 데에는 구조적 이유가 있다.",
        "summary_detail": "정리: ① 대상 — AAS 사용자 SCD 사례들의 종합 리뷰. ② 기전 — 좌심실 비대(LVH), 심근 섬유화, 전기적 불안정. ③ 특징 — 외형상 건강해 보여도 심장에 부정맥 기질 잠복. ④ 위험 — 운동·탈수가 방아쇠로 작용 가능. ⑤ 함의 — 증상 없는 잠복 손상이 가장 위험. NOGEAR 시각: 거울에 비친 가슴은 두꺼워졌지만, 그 안의 심장은 부정맥의 지뢰밭이 됐다.",
        "category": "research", "category_ko": "심혈관",
        "source": "PMC (peer-reviewed)", "source_type": "journal",
        "source_url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC7694262/",
        "credibility": cred(True, True, True, "high", "PMC 등재 문헌리뷰. AAS 사용자 SCD의 LVH·심근섬유화·부정맥 기전 일치.", "verified"),
        "viral_signals": sig(19, 19, 16, 14, 13, 7), "tags": ["AAS", "돌연사", "좌심실비대", "부정맥", "심근섬유화"],
    },
    {
        "title": "SARMs는 '안전한 스테로이드'가 아니다 — 무작위시험 체계적 리뷰의 결론",
        "title_en": "SARMs Effects on Physical Performance: A Systematic Review of RCTs",
        "summary": "임상내분비학(Clinical Endocrinology) 2025 체계적 리뷰는 SARMs 무작위시험들을 종합해, 효과는 제한적이고 부작용 신호(HDL 저하·혈압·헤모글로빈 상승 등)는 분명하다고 정리했다. '부작용 없는 근육'이라는 마케팅은 데이터로 무너진다.",
        "summary_detail": "정리: ① 방법 — SARMs 무작위 대조시험(RCT)들의 체계적 리뷰. ② 효과 — 제지방 증가 등 일부 신호 있으나 임상적 이득은 제한적. ③ 부작용 — HDL 콜레스테롤 저하, 혈압·헤모글로빈 상승 경향. ④ 함의 — '선택적이라 안전'이라는 통념과 배치. ⑤ 한계 — 장기 안전 데이터 여전히 부족. NOGEAR 시각: '선택적'이라는 단어가 안전을 보장하지 않는다. 심장과 간은 그 선택에서 제외되지 않았다.",
        "category": "research", "category_ko": "SARMs",
        "source": "Clinical Endocrinology (Wiley) 2025", "source_type": "journal",
        "source_url": "https://onlinelibrary.wiley.com/doi/10.1111/cen.15135",
        "credibility": cred(True, True, True, "high", "Wiley Clinical Endocrinology 2025 체계적 리뷰(RCT). HDL저하·혈압/Hb 상승 일치.", "verified"),
        "viral_signals": sig(18, 20, 18, 16, 14, 8), "tags": ["SARMs", "RCT", "체계적리뷰", "HDL", "부작용"],
    },
    {
        "title": "건강한 성인에게 SARMs를 줬더니 — 안전성 체계적 리뷰의 경고",
        "title_en": "Systematic Review of Safety of SARMs in Healthy Adults",
        "summary": "건강한 성인 대상 SARMs 안전성을 종합한 체계적 리뷰는, 레크리에이션 사용자에게 적용 시 지질·간·내분비 지표 악화 위험을 경고한다. 환자가 아닌 '건강한 몸'에 쓰는 순간 이득은 없고 위험만 남는다는 함의다.",
        "summary_detail": "정리: ① 대상 — 건강한 성인에서의 SARMs 안전성 종합. ② 위험 — HDL 저하 등 지질 악화, 간·내분비 영향 신호. ③ 맥락 — 의학적 적응증 없는 레크리에이션 사용의 위험-이득 불균형. ④ 품질 — 시판 제품의 함량·순도 미보장으로 위험 가중. ⑤ 결론 — 안전 입증 불가. NOGEAR 시각: 아프지 않은 몸에 약을 넣으면, 약은 병을 만든다.",
        "category": "research", "category_ko": "SARMs",
        "source": "PMC (peer-reviewed)", "source_type": "journal",
        "source_url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10204391/",
        "credibility": cred(True, True, True, "high", "PMC 등재 안전성 체계적 리뷰. 건강성인 SARMs 위험-이득 불균형 일치.", "verified"),
        "viral_signals": sig(17, 19, 17, 14, 13, 7), "tags": ["SARMs", "안전성", "체계적리뷰", "지질", "건강성인"],
    },
    {
        "title": "간을 향한 조용한 위협 — SARMs가 일으킨 급성 간독성",
        "title_en": "Silent Threats to the Liver: Acute Hepatotoxicity Attributed to SARMs",
        "summary": "2025년 보고는 SARMs가 산화 스트레스·지질대사 교란·직접 간세포 독성으로 급성 간손상을 일으킬 수 있다고 정리했다. 담즙정체성·간세포성 손상과 황달이 주증상이다. '경구라 편하다'는 바로 그 이유로 간이 1차 표적이 된다.",
        "summary_detail": "정리: ① 기전 — 산화 스트레스, 지질대사 변화, 직접 간세포 독성. ② 증상 — 담즙정체성·간세포성 간손상, 황달. ③ 역설 — 생체이용률을 높이려 간 분해를 줄인 설계가 용량의존성 직접 간독성 위험을 키움. ④ 한계 — 제품 품질관리 부재로 인과 평가 어려움. ⑤ 결론 — 추가 정밀 분석 필요. NOGEAR 시각: 소리 없이 망가지는 게 간이다. 황달이 보일 때면 이미 늦다.",
        "category": "research", "category_ko": "SARMs",
        "source": "PMC (peer-reviewed) 2025", "source_type": "journal",
        "source_url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12230875/",
        "credibility": cred(True, True, True, "high", "PMC 2025 보고. SARMs 급성 간독성·담즙정체/간세포 손상·황달 일치.", "verified"),
        "viral_signals": sig(19, 19, 17, 17, 13, 8), "tags": ["SARMs", "간독성", "황달", "DILI", "간손상"],
    },
    {
        "title": "2020년 이후 SARMs 간손상 보고 20건 — 의심 사례 분석",
        "title_en": "SARM use and related adverse events including drug-induced liver injury",
        "summary": "2020년 이후 발표된 SARMs 관련 이상반응 분석은, 대부분이 약물유발 간손상(DILI)이며 담즙정체성·간세포성 손상과 황달이 주증상이라고 보고했다. 사례가 쌓이고 있다는 사실 자체가 경고다.",
        "summary_detail": "정리: ① 규모 — 2020년 이후 약 20건의 이상반응 보고. ② 유형 — 대부분 약물유발 간손상(DILI). ③ 증상 — 담즙정체성·간세포성 간손상, 황달. ④ 함의 — 산발적 일화가 아니라 누적되는 신호. ⑤ 한계 — 제품 순도 미보장으로 인과 규명 제약. NOGEAR 시각: 보고서 한 건은 우연, 스무 건은 패턴이다. 패턴은 다음 차례가 있다는 뜻이다.",
        "category": "research", "category_ko": "SARMs",
        "source": "PMC (peer-reviewed)", "source_type": "journal",
        "source_url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC10847181/",
        "credibility": cred(True, True, True, "high", "PMC 등재 의심사례 분석. 2020년 이후 SARMs DILI 약 20건·황달 일치.", "verified"),
        "viral_signals": sig(18, 19, 16, 16, 13, 7), "tags": ["SARMs", "DILI", "간손상", "황달", "이상반응"],
    },
    {
        "title": "LiverTox 공식 등재 — SARMs는 간손상 유발 물질이다",
        "title_en": "Selective Androgen Receptor Modulators — LiverTox",
        "summary": "미국 국립보건원(NIH)의 약물간독성 데이터베이스 LiverTox는 SARMs를 정식 항목으로 등재해 간손상 유발 가능 물질로 기록한다. 'NIH가 간독성 목록에 올렸다'는 사실 자체가 가장 권위 있는 경고다.",
        "summary_detail": "정리: ① 위치 — NIH LiverTox(NBK619971) 정식 등재. ② 의미 — 약물유발 간손상 표준 레퍼런스에 SARMs 수록. ③ 내용 — 간세포성/담즙정체성 손상 보고 정리. ④ 권위 — 정부 의학 데이터베이스 수준의 공신력. ⑤ 함의 — '연구용 화학물질'이라는 회피 표현 뒤의 실체. NOGEAR 시각: NIH가 간독성 목록에 올린 물질을, 헬스장에선 '클린 벌크'라 부른다.",
        "category": "research", "category_ko": "SARMs",
        "source": "LiverTox / NCBI Bookshelf (NIH)", "source_type": "journal",
        "source_url": "https://www.ncbi.nlm.nih.gov/books/NBK619971/",
        "credibility": cred(True, True, True, "high", "NIH LiverTox 정식 등재. SARMs 간독성 레퍼런스.", "verified"),
        "viral_signals": sig(18, 20, 16, 14, 13, 7), "tags": ["SARMs", "LiverTox", "NIH", "간독성", "공식등재"],
    },
    {
        "title": "DNP, 한 알에 체온 44도 — 세포 발전소를 망가뜨리는 다이어트 독",
        "title_en": "DNP: the dangerous diet pill pharmacists should know about",
        "summary": "약학 저널은 급속 감량을 노린 DNP(2,4-디니트로페놀) 불법 사용의 재유행을 경고했다. DNP는 산화적 인산화를 '탈공역'시켜 에너지를 ATP 대신 열로 방출시키고, 체온을 최대 44도까지 끌어올려 사망에 이르게 한다. 권장 용량에서도 치명적 사례가 보고됐다.",
        "summary_detail": "정리: ① 기전 — 미토콘드리아 산화적 인산화 탈공역 → 에너지를 열로 방출. ② 결과 — 통제 불능 고열(최대 ~44℃), 빈맥, 발한, 빈호흡. ③ 위험 — 과량뿐 아니라 '권장 용량'에서도 치명적 부작용 발생. ④ 유행 — 급속 감량 목적 불법 사용 재유행. ⑤ 결론 — 인체 섭취 금지된 산업용 화학물질. NOGEAR 시각: 살을 태우는 게 아니라 사람을 태운다. 체온계가 멈추는 곳에 다이어트는 없다.",
        "category": "research", "category_ko": "약물",
        "source": "The Pharmaceutical Journal", "source_type": "journal",
        "source_url": "https://pharmaceutical-journal.com/article/feature/dnp-the-dangerous-diet-pill-pharmacists-should-know-about",
        "credibility": cred(False, True, True, "high", "약학 전문저널 피처. DNP 탈공역·고열 사망 기전 일치(다수 사례 보고와 교차).", "match"),
        "viral_signals": sig(22, 18, 18, 14, 15, 10), "tags": ["DNP", "다이어트약", "고열", "탈공역", "사망"],
    },
    {
        "title": "근이형증에 빠진 젊은 보디빌더의 죽음 — DNP와 스테로이드의 합작",
        "title_en": "Fatal long-term intoxication by 2,4-DNP and anabolic steroids in a young bodybuilder with muscle dysmorphia",
        "summary": "Frontiers in Public Health 증례 보고는 근이형증(머슬 디스모피아)을 앓던 젊은 보디빌더가 DNP와 아나볼릭 스테로이드 장기 복용 끝에 사망한 사례를 기록했다. 외형 강박이라는 정신 질환이 어떻게 약물 남용을 거쳐 죽음으로 이어지는지를 보여주는 임상 사례다.",
        "summary_detail": "정리: ① 사례 — 근이형증 진단 젊은 남성 보디빌더. ② 약물 — DNP + 아나볼릭 스테로이드 장기 병용. ③ 결과 — 만성 중독 끝의 사망. ④ 핵심 — 신체이형장애(외형 강박)가 약물 남용의 심리적 동력. ⑤ 함의 — 약물 문제의 뿌리는 종종 정신 질환. NOGEAR 시각: 죽음의 진짜 원인은 약이 아니라 거울이었다. 거울이 멈추라고 말하지 않았기 때문에.",
        "category": "research", "category_ko": "정신·중독",
        "source": "Frontiers in Public Health 2024", "source_type": "journal",
        "source_url": "https://www.frontiersin.org/journals/public-health/articles/10.3389/fpubh.2024.1452196/full",
        "credibility": cred(True, True, True, "high", "Frontiers 동료심사 증례보고. 근이형증+DNP+AAS 사망 사례 일치.", "verified"),
        "viral_signals": sig(22, 18, 19, 14, 15, 9), "tags": ["DNP", "근이형증", "보디빌더", "사망", "증례"],
    },
    {
        "title": "DNP 사망의 해부 — 외상 후 다이어트약이 부른 죽음",
        "title_en": "2,4-Dinitrophenol: 'diet' drug death following major trauma",
        "summary": "PMC 증례 보고는 DNP를 다이어트 목적으로 복용한 사람이 사망에 이른 과정을 분석했다. DNP의 대사 독성이 어떻게 신체 항상성을 무너뜨리는지를 임상 데이터로 보여준다. '살 빼는 약'이라는 포장 뒤의 실제 결말이다.",
        "summary_detail": "정리: ① 사례 — 다이어트 목적 DNP 복용자의 사망. ② 기전 — 산화적 인산화 탈공역에 의한 대사·체온 붕괴. ③ 임상 — 고열·빈맥·대사 산증 등 다발 장기 압박. ④ 교훈 — 치료적 안전역(margin)이 사실상 없음. ⑤ 함의 — 온라인 권장량 자체가 위험. NOGEAR 시각: '다이어트약'이라는 이름이 가장 위험한 마케팅이다.",
        "category": "research", "category_ko": "약물",
        "source": "PMC (peer-reviewed)", "source_type": "journal",
        "source_url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC8131886/",
        "credibility": cred(True, True, True, "high", "PMC 등재 증례. DNP 다이어트 사망·대사 붕괴 기전 일치.", "verified"),
        "viral_signals": sig(20, 18, 17, 13, 14, 8), "tags": ["DNP", "다이어트약", "사망", "증례", "대사독성"],
    },
    {
        "title": "BPC-157 논쟁의 핵심 — 근거의 90%가 한 연구실에서 나왔다",
        "title_en": "Reply re: BPC-157 — angiogenesis, nitric oxide and the evidence debate",
        "summary": "Pharmaceuticals 지에 실린 학술 논쟁(Reply)은 BPC-157의 혈관신생·산화질소 기전 주장과 그 근거의 신뢰성을 다룬다. 핵심 쟁점은 효능 데이터 대부분이 특정 연구 그룹에 집중돼 독립 재현이 부족하다는 점이다. '기적'이라 불리지만 인체 근거는 빈약하다.",
        "summary_detail": "정리: ① 주장 — BPC-157이 VEGFR2 혈관신생·NO 경로로 조직 보호·재생을 한다는 가설. ② 논쟁 — 효능 데이터의 출처가 소수 그룹에 집중, 확증 편향 위험. ③ 인체 근거 — 잘 설계된 임상 부재로 안전·용량 미검증. ④ 형식 — 동료심사 저널 내 학술적 반박/응답. ⑤ 결론 — '효과 없음'이 아니라 '검증 안 됨'. NOGEAR 시각: 한 연구실의 쥐 실험을 인간의 기적으로 번역하지 마라. 검증되지 않은 건, 안전한 게 아니라 미지일 뿐이다.",
        "category": "research", "category_ko": "펩타이드",
        "source": "Pharmaceuticals (PMC, peer-reviewed) 2025", "source_type": "journal",
        "source_url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12567171/",
        "credibility": cred(True, True, True, "high", "Pharmaceuticals 동료심사 Reply. BPC-157 기전 주장·근거 편중 논쟁 일치.", "verified"),
        "viral_signals": sig(18, 19, 16, 15, 16, 8), "tags": ["BPC-157", "펩타이드", "근거부족", "혈관신생", "재현성"],
    },
    {
        "title": "세마글루티드, 지방은 빼고 근육은 지켰다? — SEMALEAN 연구의 반전",
        "title_en": "Impact of Semaglutide on fat mass, lean mass and muscle function: SEMALEAN study",
        "summary": "SEMALEAN 연구는 세마글루티드(오젬픽) 사용 시 총지방량은 감소하고 제지방량은 초기 감소 후 안정화됐으며, 악력(handgrip)은 오히려 유의하게 개선되고 근감소성 비만 유병률은 줄었다고 보고했다. 단, 이는 영양·운동이 동반된 임상 조건에서의 결과다.",
        "summary_detail": "정리: ① 결과 — 총지방 감소, 제지방은 초기 감소 후 안정화. ② 기능 — 악력 유의 개선, 근감소성 비만 감소. ③ 조건 — 임상 관리(영양·활동) 하의 결과로 해석 필요. ④ 뉘앙스 — '무조건 근손실'이라는 통념을 일부 반박. ⑤ 한계 — 자가·무관리 사용엔 그대로 적용 불가. NOGEAR 시각: 관리된 환자에게서 좋은 숫자가, 거울 보며 끼니 거르는 사람에게도 나오진 않는다. 조건을 빼고 결론만 가져가지 마라.",
        "category": "research", "category_ko": "약물",
        "source": "PMC (peer-reviewed) — SEMALEAN", "source_type": "journal",
        "source_url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12673431/",
        "credibility": cred(True, True, True, "high", "PMC 등재 SEMALEAN. 지방감소·제지방 안정화·악력 개선·근감소성비만 감소 일치.", "verified"),
        "viral_signals": sig(18, 19, 18, 17, 13, 8), "tags": ["세마글루티드", "SEMALEAN", "제지방", "악력", "오젬픽"],
    },
    {
        "title": "GLP-1로 빠진 살, 근육보다 간이 더 줄었다 — Cell Reports Medicine 2026",
        "title_en": "GLP-1 weight loss and muscle mass in mice and humans (Cell Reports Medicine)",
        "summary": "Cell Reports Medicine 2026 연구는 비만 마우스에서 GLP-1 약물이 주로 체지방을 줄이고 제지방은 작지만 유의하게 감소시키며, 간 질량 감소가 근육 변화를 능가한다고 보고했다. 절대 근육·근력은 줄지만 상대 근육·근력은 개선돼 달리기 성능은 향상됐다.",
        "summary_detail": "정리: ① 구성 — 지방 위주 감소, 제지방은 소폭 유의 감소. ② 의외 — 간 질량 감소폭이 근육 변화보다 큼. ③ 절대 vs 상대 — 절대 근육·근력은 감소하나 체중 대비 상대값은 개선. ④ 기능 — 결과적으로 러닝 퍼포먼스 향상. ⑤ 함의 — '근손실' 공포를 정량적으로 재해석. NOGEAR 시각: 숫자는 미묘하다. '근육이 준다'와 '약해진다'는 다른 말이고, 둘 다 영양·운동이 갈라놓는다.",
        "category": "research", "category_ko": "약물",
        "source": "Cell Reports Medicine 2026", "source_type": "journal",
        "source_url": "https://www.cell.com/cell-reports-medicine/fulltext/S2666-3791(26)00082-0",
        "credibility": cred(True, True, True, "high", "Cell Reports Medicine 2026. 지방>근육 감소·간질량 감소·상대근력 개선 일치.", "verified"),
        "viral_signals": sig(17, 20, 17, 18, 12, 8), "tags": ["GLP-1", "근손실", "CellReportsMedicine", "간질량", "다이어트약"],
    },
    {
        "title": "GLP-1 메타분석 — 빠진 체중의 20~30%는 제지방이었다",
        "title_en": "GLP-1 agonists and changes in body mass and composition: systematic review & meta-analysis",
        "summary": "국제비만저널(Int. J. Obesity) 2026 메타분석은 GLP-1 작용제로 빠지는 체중의 약 20~30%가 제지방(근육 포함)이며, 저항운동과 충분한 단백질이 비만 치료의 필수 동반 전략이어야 한다고 결론지었다. 약만으로는 근육을 지킬 수 없다.",
        "summary_detail": "정리: ① 규모 — 다수 연구를 합친 체계적 리뷰·메타분석. ② 핵심 — 감량 체중의 약 20~30%가 제지방량. ③ 권고 — 저항운동 + 충분한 단백질 섭취를 표준 동반. ④ 대상 — 과체중·비만(2형 당뇨 동반/비동반) 성인. ⑤ 함의 — 약물은 도구일 뿐, 근육 보존은 행동의 몫. NOGEAR 시각: 주사는 지방을 빼주지만 근육을 지켜주진 않는다. 그건 여전히 바벨의 일이다.",
        "category": "research", "category_ko": "약물",
        "source": "International Journal of Obesity (Nature) 2026", "source_type": "journal",
        "source_url": "https://www.nature.com/articles/s41366-026-02088-1",
        "credibility": cred(True, True, True, "high", "Nature IJO 2026 메타분석. 감량 체중 20~30% 제지방·저항운동 권고 일치.", "verified"),
        "viral_signals": sig(18, 20, 18, 17, 12, 8), "tags": ["GLP-1", "메타분석", "제지방", "저항운동", "단백질"],
    },
    {
        "title": "TRAVERSE 임상 — 의학용 TRT는 심장마비를 늘리지 않았다(단, 조건부)",
        "title_en": "Testosterone Therapy and Cardiovascular Risk — TRAVERSE (NEJM)",
        "summary": "NEJM에 실린 대규모 무작위시험 TRAVERSE는 성선기능저하 + 심혈관 위험을 가진 중장년 남성에서 의학적 TRT가 주요 심장사건(MACE)에서 위약 대비 비열등하다고 보고했다. 다만 심방세동·급성신손상·폐색전증은 테스토스테론군에서 더 많았다. 그리고 이는 '초생리적 약물 남용'과는 전혀 다른 이야기다.",
        "summary_detail": "정리: ① 설계 — 성선기능저하·심혈관 고위험 남성 대상 대규모 RCT. ② 결과 — MACE에서 위약 대비 비열등(증가 없음). ③ 단서 — 심방세동, 급성신손상, 폐색전증은 TRT군에서 증가. ④ 결정적 구분 — 생리적 용량 의학 TRT ≠ 초생리적 AAS 남용. ⑤ 함의 — '테스토 = 안전'이 아니라 '관리된 적정용량 = 비열등'. NOGEAR 시각: 의사가 처방한 생리적 용량과, 거울 보며 찌르는 10배 용량은 같은 분자라도 다른 운명이다.",
        "category": "research", "category_ko": "테스토스테론",
        "source": "New England Journal of Medicine — TRAVERSE", "source_type": "journal",
        "source_url": "https://www.nejm.org/doi/full/10.1056/NEJMoa2215025",
        "credibility": cred(True, True, True, "high", "NEJM TRAVERSE RCT. MACE 비열등·AFib/AKI/PE 증가, 생리적 TRT vs AAS 구분 일치.", "verified"),
        "viral_signals": sig(17, 20, 17, 14, 14, 7), "tags": ["TRT", "테스토스테론", "TRAVERSE", "심혈관", "NEJM"],
    },
]

# ============ NEWS ============
NEW_NEWS = [
    {
        "title": "스테로이드 과거를 고백했던 피트니스 인플루언서, 30세에 심장마비 사망",
        "title_en": "Fitness influencer who spoke about steroid use dies of heart attack at 30",
        "summary": "스테로이드 사용 과거를 공개적으로 이야기해온 호주 피트니스 인플루언서 잭슨 티펫(Jaxon Tippet)이 30세에 터키 호텔에서 숨진 채 발견됐다고 NBC 뉴스가 전했다. 운동·동기부여 콘텐츠로 큰 팬덤을 모았던 인물이다.",
        "summary_detail": "정리: ① 인물 — 호주 피트니스 인플루언서 잭슨 티펫(30). ② 사망 — 터키 호텔 객실에서 사망 발견, 심장마비로 보도. ③ 이력 — 운동·동기부여 콘텐츠로 다수 팔로워, 과거 스테로이드 중독을 솔직히 공개. ④ 맥락 — 젊은 피트니스 인플루언서 돌연사의 또 다른 사례. ⑤ 매체 — NBC 뉴스 보도. NOGEAR 시각: 화면 속에서 가장 건강해 보이던 사람이, 30세에 멈췄다. 알고리즘은 그의 심장을 보여주지 않았다.",
        "category": "scandal", "category_ko": "사건·사망",
        "source": "NBC News", "source_type": "news",
        "source_url": "https://www.nbcnews.com/news/jaxon-tippet-australian-fitness-influencer-reportedly-dies-rcna180019",
        "credibility": cred(False, False, True, "medium", "NBC 뉴스 보도. 잭슨 티펫 30세 사망·스테로이드 과거 공개 사실관계 일치.", "match"),
        "viral_signals": sig(23, 12, 21, 16, 14, 11), "tags": ["인플루언서사망", "심장마비", "스테로이드", "잭슨티펫", "돌연사"],
    },
    {
        "title": "'고기 먹어서 양성'은 통하지 않았다 — 스프린터 나이튼 도핑 4년 징계",
        "title_en": "Sprinter Erriyon Knighton banned 4 years for positive doping test",
        "summary": "스프린터 에리욘 나이튼이 아나볼릭 스테로이드 양성 반응으로 스포츠중재재판소(CAS)에서 4년 징계를 받았다고 ESPN이 전했다. '오염된 고기 섭취' 변론이 1심에서 받아들여졌으나, WADA와 육상정직성기구는 그 근거가 '통계적으로 불가능'하다며 항소해 뒤집었다.",
        "summary_detail": "정리: ① 결과 — CAS, 나이튼에게 4년 자격정지. ② 사유 — 아나볼릭 스테로이드 양성. ③ 변론 — '오염된 고기 섭취' 주장으로 1심 면책. ④ 반전 — WADA·AIU 항소, 면책 근거를 '통계적으로 불가능'이라 반박해 승소. ⑤ 함의 — 정교한 해명도 데이터 앞에선 무너진다. NOGEAR 시각: 변명은 창의적일수록 의심받는다. 진실은 통계로 검증되지, 서사로 무마되지 않는다.",
        "category": "scandal", "category_ko": "도핑",
        "source": "ESPN", "source_type": "news",
        "source_url": "https://www.espn.com/olympics/trackandfield/story/_/id/46232358/sprinter-erriyon-knighton-gets-4-year-ban-positive-doping-test",
        "credibility": cred(False, False, True, "medium", "ESPN 보도. 나이튼 4년 징계·고기오염 변론·WADA 항소 사실관계 일치.", "match"),
        "viral_signals": sig(19, 13, 17, 17, 17, 9), "tags": ["도핑", "나이튼", "WADA", "CAS", "4년징계"],
    },
    {
        "title": "밀라노-코르티나 2026 올림픽, 도핑 양성 0건 — 3,053회 검사",
        "title_en": "Milan Cortina 2026: no Olympic doping positives out of 3,053 tests",
        "summary": "국제검사기구(ITA)는 2026 밀라노-코르티나 동계올림픽에서 1,848명 선수 대상 3,053회 검사 결과 도핑 양성이 0건이었다고 밝혔다. 다만 ITA는 '그래도 충분치 않다'며 검사 강화 필요성을 강조했다.",
        "summary_detail": "정리: ① 규모 — 1,848명, 1/30~2/22 기간 3,053개 샘플. ② 결과 — 대회 기간 검사 기반 도핑 위반 0건. ③ 단서 — ITA, '검사량이 여전히 부족'하다는 입장. ④ 맥락 — 깨끗한 결과가 '도핑 없음'을 증명하진 않음(검출 한계·타이밍). ⑤ 의미 — 무위반 발표와 검사 신뢰성은 별개의 문제. NOGEAR 시각: 0건은 '아무도 안 했다'가 아니라 '아무도 안 걸렸다'일 수 있다. 검사망의 그물코가 진실을 가른다.",
        "category": "scandal", "category_ko": "도핑",
        "source": "The Sports Examiner", "source_type": "news",
        "source_url": "https://www.thesportsexaminer.com/milan-cortina-2026-intl-testing-agency-says-no-milan-cortina-olympic-positives-out-of-3053-tests-on-1848-athletes-its-still-not-enough/",
        "credibility": cred(False, False, True, "medium", "스포츠 전문매체 보도(ITA 발표 인용). 3,053검사·양성 0건·ITA 코멘트 일치.", "match"),
        "viral_signals": sig(15, 13, 14, 18, 14, 7), "tags": ["도핑", "올림픽", "밀라노코르티나", "ITA", "검사"],
    },
    {
        "title": "부러워하던 그 몸은 거짓이었다 — '가짜 천연' 인플루언서들의 비밀",
        "title_en": "Fake fitness influencers: the secrets and lies behind the world's most envied physiques",
        "summary": "야후 라이프스타일 기획은 세계에서 가장 부러움받는 피지크 뒤에 숨은 거짓을 파헤쳤다. 다수 인플루언서가 PED를 쓰면서 '천연(natural)'을 표방해 신뢰를 쌓고, 그 신뢰로 운동 프로그램·보충제를 판다는 구조를 지목한다.",
        "summary_detail": "정리: ① 주제 — '가장 부러운 몸' 뒤의 거짓말. ② 패턴 — PED 사용을 숨기고 '천연'으로 포장해 신뢰 확보. ③ 수익 — 그 신뢰를 프로그램·보충제 판매로 환금. ④ 피해 — 일반인의 비현실적 기대와 자기혐오 양산. ⑤ 맥락 — 'fake natty' 폭로 문화의 확산. NOGEAR 시각: 그들이 파는 건 운동법이 아니라 환상이다. FXXK FAKES — 부러움은 거짓말의 가장 비싼 통화다.",
        "category": "scandal", "category_ko": "페이크내추럴",
        "source": "Yahoo Lifestyle", "source_type": "news",
        "source_url": "https://www.yahoo.com/lifestyle/fake-fitness-influencers-secrets-lies-040015028.html",
        "credibility": cred(False, False, True, "medium", "야후 라이프스타일 기획. PED 은폐·천연 포장·수익화 구조 — 업계 보도들과 교차.", "match"),
        "viral_signals": sig(21, 11, 21, 14, 18, 11), "tags": ["페이크내추럴", "인플루언서", "PED은폐", "거짓말", "보충제"],
    },
    {
        "title": "유튜브 '천연' 보디빌더 폭로 리스트 — 80%는 약물파다",
        "title_en": "Top Fake Natural Bodybuilders On YouTube",
        "summary": "NattyOrNot의 정리에 따르면 보디빌더의 약 80%가 스테로이드를 쓰고, 진짜 천연은 20%에 불과하다. 비시즌에도 선명한 복근·혈관, 여유증·탈모·주사 부위 부종 같은 신호가 '가짜 천연'을 가려낸다고 본다. 리버 킹은 월 1만1천 달러를 약물에 쓴 대표 사례다.",
        "summary_detail": "정리: ① 비율 — 보디빌더 약 80% PED 사용, 천연 20% 추정. ② 신호 — 비시즌에도 선명한 복근·혈관(enhanced look), 여성형유방, 탈모, 주사 부위 부종. ③ 동기 — 프로그램·보충제 판매 신뢰도 위해 '천연' 위장. ④ 사례 — 리버 킹, 누출 이메일로 월 $11,000+ 스테로이드 지출 폭로. ⑤ 성격 — 폭로 커뮤니티 관점(주관 포함). NOGEAR 시각: '내추럴'이라 쓰여 있다고 천연이 아니다. 비시즌의 복근이 첫 번째 거짓말이다.",
        "category": "scandal", "category_ko": "페이크내추럴",
        "source": "NattyOrNot.com", "source_type": "blog",
        "source_url": "https://nattyornot.com/top-10-fake-natural-bodybuilders-youtube/",
        "credibility": cred(False, False, True, "low", "폭로 커뮤니티(주관·추정 포함). '80% 사용' 등은 비공식 추정치 — 리버킹 $11k는 다수 보도와 교차.", "unclear", confirmed=False),
        "viral_signals": sig(20, 9, 20, 13, 19, 10), "tags": ["페이크내추럴", "보디빌더", "폭로", "리버킹", "유튜브"],
    },
    {
        "title": "FDA의 펩타이드 전쟁 — BPC-157·TB-500 단속 타임라인 2024~2026",
        "title_en": "The FDA's War on Peptides: A Complete 2024–2026 Enforcement Timeline",
        "summary": "펩타이드 전문 매체는 2024~2026년 FDA의 펩타이드 단속 흐름을 정리했다. 2023년 BPC-157·TB-500 등 19종이 Category 2(제한)로 분류돼 합법 조제가 사실상 막혔다가, 2026년 2월 HHS가 약 14종을 Category 1로 되돌릴 것으로 발표하며 기류가 바뀌었다.",
        "summary_detail": "정리: ① 2023 — BPC-157·TB-500 등 19종, FDA Category 2(제한) 지정 → 합법 조제 차단. ② 2024 — PCAC, 이파모렐린·MK-677·CJC-1295·AOD-9604 조제 불허 표결. ③ 2026.2 — HHS, 19종 중 약 14종을 Category 1 복귀 발표(처방하 조제 경로 부분 복원). ④ 함의 — 규제 완화 ≠ 안전 입증. ⑤ 성격 — 전문매체 정리(상업적 맥락 유의). NOGEAR 시각: 분류가 바뀌어도 분자는 그대로다. '합법'은 정치의 단어고, '안전'은 데이터의 단어다.",
        "category": "scandal", "category_ko": "펩타이드·규제",
        "source": "PeptideExaminer", "source_type": "blog",
        "source_url": "https://peptideexaminer.com/articles/fda-peptide-enforcement-2025-guide/",
        "credibility": cred(False, False, True, "medium", "펩타이드 전문매체 타임라인. 2023 Cat2 지정·2026.2 재분류는 다수 법률/규제 보도와 교차.", "match"),
        "viral_signals": sig(17, 13, 16, 18, 16, 7), "tags": ["펩타이드", "FDA", "BPC-157", "TB-500", "규제"],
    },
    {
        "title": "RFK Jr.가 BPC-157 빗장을 풀었다 — 환자에게 무엇을 의미하나",
        "title_en": "BPC-157 FDA Status 2026: What the RFK Reclassification Means for Patients",
        "summary": "2026년 2월 HHS 장관 로버트 F. 케네디 주니어가 제한 펩타이드 19종 중 약 14종(BPC-157 포함)을 Category 1로 되돌릴 것이라 발표했다. 라이선스 조제 약국이 의사 처방 하에 다시 준비할 수 있는 길이 열린 셈이다. 그러나 '접근 가능'이 '효능·안전 입증'을 뜻하지는 않는다.",
        "summary_detail": "정리: ① 발표 — RFK Jr.(HHS), 제한 펩타이드 약 14/19종 Cat1 복귀 예고. ② 효과 — 라이선스 조제약국이 처방하 조제 재개 가능. ③ 포함 — BPC-157 등 인기 회복 펩타이드. ④ 경고 — 합법 접근성 ≠ 임상 효능·장기 안전 입증. ⑤ 현실 — 여전히 상당량은 비규제 시장 유통. NOGEAR 시각: 빗장이 풀렸다고 검증이 끝난 게 아니다. 처방전이 곧 안전 보증서는 아니다.",
        "category": "scandal", "category_ko": "펩타이드·규제",
        "source": "AgeMD", "source_type": "blog",
        "source_url": "https://www.agemd.com/longevity/rfk-bpc-157-fda-peptide-reclassification-2026",
        "credibility": cred(False, False, True, "medium", "롱제비티 매체 해설. 2026.2 RFK 재분류(약 14/19종, BPC-157 포함)는 복수 매체와 교차.", "match"),
        "viral_signals": sig(17, 12, 16, 18, 16, 7), "tags": ["BPC-157", "RFK", "FDA", "재분류", "펩타이드"],
    },
    {
        "title": "의사의 경고 — BPC-157·TB-500은 '펩타이드 도박'이다",
        "title_en": "The Peptide Gamble: A Doctor's Warning on BPC-157 and TB-500",
        "summary": "정형·웰니스 클리닉의 의사는 BPC-157·TB-500 사용을 '도박'에 비유하며 경고한다. 동물 데이터는 솔깃하지만 인체 대상 양질의 안전·효능 임상이 부족하고, 시중 제품은 순도·함량이 보장되지 않는다는 이유다. 회복을 약속받고 미지의 위험을 떠안는 거래라는 것이다.",
        "summary_detail": "정리: ① 비유 — 검증 안 된 펩타이드 사용 = 도박. ② 근거 — 전임상은 유망하나 인체 임상 부족. ③ 품질 — 비규제 제품의 순도·용량 미보장. ④ 위험 — 미지의 장기 효과를 사용자가 떠안음. ⑤ 입장 — 임상의의 직접 경고. NOGEAR 시각: 회복을 약속받고 미지를 산다. 그게 도박이 아니면 무엇인가.",
        "category": "scandal", "category_ko": "펩타이드",
        "source": "Ortho & Wellness (clinician blog)", "source_type": "blog",
        "source_url": "https://www.orthoandwellness.com/blog/the-peptide-gamble-a-doctors-warning-on-bpc-157-and-tb-500",
        "credibility": cred(False, False, True, "low", "임상의 운영 블로그(상업적 맥락 가능). 인체임상 부족·품질 미보장 경고는 학술 보도와 일치.", "match", confirmed=False),
        "viral_signals": sig(17, 12, 16, 14, 16, 7), "tags": ["BPC-157", "TB-500", "펩타이드", "의사경고", "도박"],
    },
    {
        "title": "BPC-157 인체 임상 현황 2025~2026 — '거의 없다'가 정답",
        "title_en": "BPC-157 Human Clinical Trials (2025–2026): Complete Status",
        "summary": "펩타이드 데이터베이스 정리에 따르면 BPC-157의 인체 임상은 사실상 초기 단계에 머물러 있다. 2025년 건강 성인 2명에게 정맥 투여한 소규모 연구에서 내약성은 양호했고 24시간 내 혈중 농도가 기저로 회복됐으나, 이는 효능·안전 입증과는 거리가 멀다.",
        "summary_detail": "정리: ① 현황 — BPC-157 인체 임상은 극초기. ② 대표 연구 — 2025년 건강 성인 단 2명 정맥 투여, 내약성 양호·24h 내 혈중농도 기저 복귀. ③ 한계 — 표본 2명은 안전·효능 일반화 불가. ④ 의미 — '인체 데이터 있음'과 '입증됨'은 다른 말. ⑤ 결론 — 의약품 수준 근거 미충족. NOGEAR 시각: 2명짜리 데이터를 들고 '인체 검증'이라 부르지 마라. 그건 시작점이지 결론이 아니다.",
        "category": "scandal", "category_ko": "펩타이드",
        "source": "Peptide Database", "source_type": "blog",
        "source_url": "https://peptide-db.com/guides/bpc-157-human-trials",
        "credibility": cred(False, False, True, "low", "펩타이드 DB 가이드(상업적 맥락 가능). '2인 IV 연구' 등 핵심 사실은 STAT/학술 보도와 교차.", "match", confirmed=False),
        "viral_signals": sig(16, 12, 16, 16, 15, 7), "tags": ["BPC-157", "인체임상", "펩타이드", "근거부족", "표본"],
    },
    {
        "title": "FDA가 BPC-157·TB-500 등 7종을 현미경 아래 놓다 — 503A 재검토",
        "title_en": "FDA Puts BPC-157, TB-500 and 5 Other Peptides Under the 503A Review",
        "summary": "법률 전문매체는 FDA가 BPC-157·TB-500 등 7종 펩타이드를 503A 조제 적격성 관점에서 재검토 중이라고 전했다. 처방자(의사)에게 중요한 것은 '조제 가능 여부'와 '책임 소재'다. 규제의 추가 변동 가능성이 열려 있다는 신호다.",
        "summary_detail": "정리: ① 사안 — BPC-157·TB-500 등 7종에 대한 503A 조제 적격성 재검토. ② 청중 — 처방하는 임상의·조제 약국. ③ 쟁점 — 조제 가능 범위와 법적 책임. ④ 함의 — 분류가 또 바뀔 수 있는 유동적 상태. ⑤ 성격 — 로펌의 규제 해설. NOGEAR 시각: 규제가 흔들린다는 건, 아직 아무도 '안전하다'고 단정하지 못한다는 뜻이다.",
        "category": "scandal", "category_ko": "펩타이드·규제",
        "source": "Lengea Law", "source_type": "blog",
        "source_url": "https://lengealaw.com/fda-puts-bpc-157-tb-500-and-5-other-peptides-under-the-microscope-what-prescribers-need-to-know-about-the-503a-review/",
        "credibility": cred(False, False, True, "medium", "로펌 규제 해설. 503A 재검토·7종 펩타이드는 FDA 규제 보도들과 교차.", "match"),
        "viral_signals": sig(15, 13, 14, 17, 15, 6), "tags": ["FDA", "503A", "BPC-157", "TB-500", "규제"],
    },
    {
        "title": "오젬픽, 근육량보다 '근력'이 더 빠진다 — 유타대 마우스 연구",
        "title_en": "Mouse study raises questions about how Ozempic affects muscle size and strength",
        "summary": "유타대학교 연구진의 마우스 실험은 세마글루티드(오젬픽)에서 근육량 변화는 예상보다 작아도 근육이 '약해질' 수 있다고 제기했다. 즉 양(量)보다 질(質)의 문제다. 체중계 숫자만으로는 근육 건강을 판단할 수 없다는 경고다.",
        "summary_detail": "정리: ① 연구 — 유타대 마우스 모델 실험. ② 발견 — 근육량 감소는 예상보다 작지만 근력 저하 관찰. ③ 해석 — 근육의 '양'과 '질(기능)'이 따로 움직일 수 있음. ④ 한계 — 동물 모델로 인체 직접 적용엔 신중 필요. ⑤ 함의 — 감량 = 건강이라는 통념에 제동. NOGEAR 시각: 가벼워진 몸이 약해진 몸일 수 있다. 저울은 근력을 재지 못한다.",
        "category": "scandal", "category_ko": "약물",
        "source": "University of Utah (@theU)", "source_type": "news",
        "source_url": "https://attheu.utah.edu/health-medicine/mouse-study-raises-questions-about-how-ozempic-affects-muscle-size-and-strength/",
        "credibility": cred(False, True, True, "medium", "유타대 공식 보도(소속 연구 기반). 근육량 변화 작아도 근력 저하 가능 — 동물모델 단서 명시.", "match"),
        "viral_signals": sig(18, 15, 18, 17, 12, 8), "tags": ["오젬픽", "근력", "유타대", "마우스연구", "근육질"],
    },
    {
        "title": "GLP-1 근손실, 걱정 안 해도 된다? — 메드스케이프의 반론",
        "title_en": "No Need to Worry About GLP-1-Induced Muscle Loss",
        "summary": "의료 전문매체 메드스케이프는 GLP-1 근손실 우려가 과장됐을 수 있다고 본다. 일정한 제지방 감소는 정상적 체중감량의 일부이며, 충분한 단백질과 저항운동이 동반되면 기능 손실은 제한적이라는 임상 시각이다. 단, '운동·영양 동반'이라는 전제가 핵심이다.",
        "summary_detail": "정리: ① 입장 — GLP-1 근손실 공포가 과장됐을 수 있음. ② 근거 — 일부 제지방 감소는 정상 감량의 자연스러운 부분. ③ 조건 — 충분한 단백질 + 저항운동 시 기능 보존. ④ 균형 — 'Cell Reports Medicine'·SEMALEAN의 낙관적 신호와 결을 같이함. ⑤ 단서 — 무관리 사용엔 적용 제한. NOGEAR 시각: '걱정 마라'의 진짜 조건은 '운동하라'다. 전제를 빼면 안심도 거짓이 된다.",
        "category": "scandal", "category_ko": "약물",
        "source": "Medscape 2026", "source_type": "news",
        "source_url": "https://www.medscape.com/viewarticle/no-need-worry-about-glp-1-induced-muscle-loss-2026a1000dr2",
        "credibility": cred(False, False, True, "medium", "Medscape 의료 전문매체 해설. '운동·단백질 동반 시 기능 보존' 관점 — 학술 데이터와 정합.", "match"),
        "viral_signals": sig(15, 14, 17, 17, 14, 7), "tags": ["GLP-1", "근손실", "Medscape", "저항운동", "단백질"],
    },
    {
        "title": "오젬픽은 근육을 녹이는가 — Drugs.com의 정리와 방어법",
        "title_en": "Does Ozempic cause muscle loss and how to prevent it?",
        "summary": "의약 정보 사이트 Drugs.com은 오젬픽(세마글루티드)에서 근손실이 발생할 수 있으나, 저항운동·충분한 단백질·수분/영양 섭취로 상당 부분 예방 가능하다고 정리했다. 약은 식욕을 줄일 뿐, 근육을 지키는 행동은 사용자의 몫이라는 메시지다.",
        "summary_detail": "정리: ① 현상 — 세마글루티드 감량 과정에서 일부 근손실 가능. ② 원인 — 약 자체보다 급격한 칼로리·단백질 부족. ③ 예방 — 저항운동, 충분한 단백질, 수분·영양 확보. ④ 균형 — 위험과 관리법을 함께 제시. ⑤ 성격 — 의약 정보 사이트(의료 검수). NOGEAR 시각: 주사는 식욕을 끄지만 근육 스위치는 네 손에 있다. 끼니를 거를 거면 바벨이라도 들어라.",
        "category": "scandal", "category_ko": "약물",
        "source": "Drugs.com", "source_type": "news",
        "source_url": "https://www.drugs.com/medical-answers/ozempic-cause-muscle-loss-how-you-prevent-3578660/",
        "credibility": cred(False, False, True, "medium", "Drugs.com 의약정보(의료 검수). 근손실 가능·저항운동/단백질 예방법 — 학술과 정합.", "match"),
        "viral_signals": sig(16, 13, 18, 15, 12, 7), "tags": ["오젬픽", "근손실", "예방", "단백질", "저항운동"],
    },
    {
        "title": "치명적 DNP, 영국 보건당국의 거듭된 경고 — 'Deadly DNP'",
        "title_en": "Deadly DNP — UK Health Security Agency",
        "summary": "영국 보건안전청(UKHSA)은 공식 블로그를 통해 다이어트 목적 DNP의 치명성을 거듭 경고했다. DNP는 인체 섭취가 금지된 독성 산업 화학물질이며, 소량으로도 치명적 고열을 유발할 수 있다. 정부 보건기관이 직접 '죽음의 DNP'라 명명했다.",
        "summary_detail": "정리: ① 주체 — 영국 보건안전청(UKHSA) 공식 블로그. ② 메시지 — 다이어트용 DNP의 치명성 경고. ③ 근거 — 인체 섭취 금지된 독성 화학물질, 치명적 고열 유발. ④ 권위 — 정부 보건기관의 공식 입장. ⑤ 함의 — 온라인 판매·복용의 직접적 사망 위험. NOGEAR 시각: 정부가 '죽음의'라는 수식어를 붙이는 다이어트약이 있다. 그 이름 앞에서 멈추지 않을 이유가 없다.",
        "category": "scandal", "category_ko": "약물·경고",
        "source": "UK Health Security Agency (gov)", "source_type": "news",
        "source_url": "https://ukhsa.blog.gov.uk/2018/08/13/deadly-dnp/",
        "credibility": cred(False, True, True, "high", "영국 정부(UKHSA) 공식 블로그. DNP 치명성·인체섭취 금지 경고 일치.", "verified"),
        "viral_signals": sig(19, 15, 16, 12, 14, 8), "tags": ["DNP", "UKHSA", "다이어트약", "정부경고", "독성"],
    },
    {
        "title": "SARMs, '해롭다'를 미군 보건당국이 직접 말하다",
        "title_en": "SARMs: What's the harm? (Operation Supplement Safety)",
        "summary": "미군 보충제 안전 프로그램(OPSS)은 SARMs의 위험을 공식 정리했다. 검증되지 않은 안전성, 간·심혈관·내분비 부작용, 표지와 실제 성분의 불일치 등을 경고하며 군 장병에게 사용 금지를 권고한다. 정부·군 차원의 명확한 경고다.",
        "summary_detail": "정리: ① 주체 — 미 국방부 산하 보충제 안전 프로그램(OPSS). ② 경고 — SARMs는 인간 사용 안전성 미검증. ③ 위험 — 간·심혈관·내분비 부작용, 호르몬 교란. ④ 품질 — 라벨과 실제 성분 불일치 빈번. ⑤ 권고 — 장병 사용 금지. NOGEAR 시각: 극한의 퍼포먼스를 요구하는 군대조차 '쓰지 마라'고 한다. 그 한마디면 충분하지 않은가.",
        "category": "scandal", "category_ko": "SARMs",
        "source": "Operation Supplement Safety (DoD)", "source_type": "news",
        "source_url": "https://www.opss.org/article/sarms-whats-harm",
        "credibility": cred(False, True, True, "high", "미 국방부 OPSS 공식 자료. SARMs 안전성 미검증·라벨 불일치 경고 일치.", "verified"),
        "viral_signals": sig(17, 16, 16, 13, 14, 7), "tags": ["SARMs", "OPSS", "국방부", "경고", "라벨불일치"],
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

    # 최대 200 cap (research 최저점부터 제거, news 큐레이션 보존)
    removed = 0
    while len(d["news"]) + len(d["research"]) > 200 and d["research"]:
        d["research"].sort(key=lambda x: x.get("viral_score", 0))
        d["research"].pop(0); removed += 1
        d["research"].sort(key=lambda x: x.get("viral_score", 0), reverse=True)

    now = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=9)))
    d["meta"]["last_updated"] = now.isoformat()
    d["meta"]["last_updated_kst"] = now.strftime("%Y-%m-%d %H:%M") + f" KST 아침 크롤 (AAS생식·보디빌더돌연사·SARMs간독성·DNP사망·펩타이드규제·GLP1근손실) +{added}건"
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
    print("TOP3:")
    alla = sorted([x for sec in ("news", "research") for x in d[sec]], key=lambda x: x.get("viral_score", 0), reverse=True)
    for a in alla[:3]:
        print(f"  [{a.get('viral_score')}] {a['title'][:55]}")

if __name__ == "__main__":
    main()
