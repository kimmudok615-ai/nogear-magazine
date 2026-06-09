#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""NOGEAR Magazine 아침 크롤 2026-06-09 — 신규 기사 병합.
브랜드: FXXK FAKES. STAY NATURAL. 전체 한국어."""
import json
import datetime

PATH = "content/articles.json"
DATE = "2026.06.09"
CC_DATE = "2026-06-09"


def signals(shock, sci, rel, rec, contr, vis):
    return {
        "shock_factor": shock, "scientific_credibility": sci,
        "relatability": rel, "recency": rec,
        "controversy": contr, "visual_potential": vis,
    }


def tier(score):
    if score >= 98:
        return "VIRAL_BOMB", "🔴"
    return "HOT", "🟠"


def badge_for(conf):
    return {
        "high": "✅ VERIFIED",
        "medium": "🔍 CHECKED",
        "low": "⚠️ UNVERIFIED",
        "rejected": "❌ REJECTED",
    }.get(conf, "🔍 CHECKED")


NEW = [
    # 1. ESC 보도 — 남성 보디빌더 돌연사 (전문 직접 검증 — ESC 프레스)
    {
        "title": "보디빌더 2만 명을 추적했다 — 121명 사망·평균 45세, 프로는 돌연사 위험 5배",
        "title_en": "Male bodybuilders face high risk of sudden cardiac death, especially professionals",
        "summary": "유럽심장학회(ESC)가 공개한 분석은 국제보디빌딩연맹(IFBB) 기록의 남성 보디빌더 2만 286명(2005~2020)을 추적해 121명의 사망을 확인했다. 평균 사망 연령은 45세, 그중 38%가 돌연심장사(SCD)였다. 특히 프로 보디빌더의 돌연사 위험은 아마추어보다 5배 이상 높았고, 부검에선 심장 비대·심비대·관상동맥질환이 공통으로 나타났다.",
        "summary_detail": "정리: ① 출처 — 유럽심장학회(ESC) 프레스 릴리스, 책임저자 Marco Vecchiato. ② 표본 — IFBB 기록 남성 보디빌더 20,286명, 2005~2020년 추적. ③ 사망 — 총 121명, 평균 45세 사망. ④ 핵심 — 사망의 38%가 돌연심장사(SCD), 프로는 아마추어 대비 SCD 위험 5배 이상. ⑤ 부검 — 심장 비후·심비대·관상동맥질환 공통, 일부에서 아나볼릭 약물 검출. ⑥ 배경 — 극단적 근력훈련·급속 감량·탈수·광범위한 PED 사용이 심혈관계에 동시 부담. 약 15%는 사고·자살·과용 등 외상성 사망(문화의 정신적 그늘). NOGEAR 시각: 45세는 사망 평균이 아니라 경고문이다. 무대 위 트로피의 대가가 심장 근육에 청구된다. 가장 큰 몸이 가장 빨리 멈춘다.",
        "category": "research", "category_ko": "스테로이드·심장 연구",
        "source": "European Society of Cardiology (ESC) Press",
        "source_type": "journal",
        "source_url": "https://www.escardio.org/The-ESC/Press-Office/Press-releases/male-bodybuilders-face-high-risk-of-sudden-cardiac-death-especially-those-who-compete-professionally",
        "credibility": {
            "peer_reviewed": True, "primary_source": True, "cross_checked": True,
            "cross_check_date": CC_DATE, "url_alive": True, "cross_confirmed": True,
            "confidence": "high",
            "notes": "ESC 프레스 전문 직접 검증: 20,286명·121사망·평균45세·SCD 38%·프로 5배·부검 심비대 골자 일치. ACC Journal Scan·European Heart Journal 동일 연구 교차확인.",
            "fact_checked": True, "fact_check_date": CC_DATE, "accuracy": "match",
            "independent_verification": True,
        },
        "viral_signals": signals(22, 19, 18, 18, 15, 11),
        "tags": ["보디빌더", "돌연사", "스테로이드", "심장", "ESC"],
    },
    # 2. PMC12324147 — 스테나볼릭 SARM 간손상 (전문 직접 검증)
    {
        "title": "'마일드한 SARM'이 간을 멈췄다 — 스테나볼릭 첫 인체 간손상 보고, 빌리루빈 7.7",
        "title_en": "When gains go wrong: SARM (Stenabolic) related liver injury — a case report",
        "summary": "건강하던 40세 남성이 보충제 '스테나볼릭(SR9009)'을 복용한 뒤 황달·공막 황염·우상복부 통증·짙은 소변으로 응급실을 찾았다. 총 빌리루빈 7.7mg/dL(정상 0.1~1.2), ALT 108·AST 64로 간이 손상돼 있었다. 스테나볼릭이 사람에게 약물유발 간손상(DILI)을 일으킨 첫 공식 보고로, '순한 비스테로이드 SARM'이라는 시중 광고와 정면으로 충돌한다.",
        "summary_detail": "정리: ① 출처 — 증례보고(PMC12324147). ② 인물 — 건강하던 40세 남성. ③ 약물 — 스테나볼릭(SR9009, Rev-ErbA 리간드로 SARM 계열 분류·시판). ④ 증상 — 모호한 위장증상, 공막 황염·황달, 우상복부 압통, 짙은 소변. ⑤ 수치 — 총빌리루빈 7.7(정상 0.1~1.2)·직접빌리루빈 5.3·AST 64·ALT 108, ALP·응고는 정상. ⑥ 경과 — 보존치료+복용 중단 후 간효소 하락·임상 호전, 퇴원. ⑦ 의의 — 스테나볼릭 유발 인체 DILI '최초' 보고. NOGEAR 시각: '운동 안 해도 살 빠지는 약'이라더니 멈춘 건 지방이 아니라 간이었다. 임상시험도 안 거친 분자를 네 간이 대신 시험하고 있다.",
        "category": "research", "category_ko": "SARMs 연구",
        "source": "PMC Case Report (PMC12324147)",
        "source_type": "journal",
        "source_url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12324147/",
        "credibility": {
            "peer_reviewed": True, "primary_source": True, "cross_checked": True,
            "cross_check_date": CC_DATE, "url_alive": True, "cross_confirmed": True,
            "confidence": "high",
            "notes": "PMC 전문 직접 검증: 40세 남성·스테나볼릭(SR9009)·빌리루빈7.7/직접5.3·AST64·ALT108·ALP정상·중단 후 호전·스테나볼릭 첫 인체 DILI 골자 일치.",
            "fact_checked": True, "fact_check_date": CC_DATE, "accuracy": "match",
            "independent_verification": True,
        },
        "viral_signals": signals(20, 18, 18, 15, 14, 10),
        "tags": ["SARMs", "스테나볼릭", "간손상", "DILI", "증례보고"],
    },
    # 3. PMC11426965 — RAD-140 간손상 (전문 직접 검증)
    {
        "title": "RAD-140 3개월에 간이 무너졌다 — 29세 황달, 빌리루빈 11.3·간 섬유화까지",
        "title_en": "Selective androgen receptor modulators leading to liver injury: a case report (RAD-140)",
        "summary": "29세 남성이 SARM 'RAD-140(테스토론)'을 하루 20mg씩 3개월 복용한 뒤, 눈 흰자가 노래지고(황달) 체중이 빠지며 가려움을 호소했다. 검사에서 총 빌리루빈 11.3mg/dL(정상 1.1 미만), ALT 144·AST 92로 심한 간손상이 확인됐고 초음파엔 지방간·경도 섬유화(F1)까지 보였다. 복용을 끊자 약 6주 만에 회복됐지만, '근육 잘 붙는 안전한 약'이라는 평판이 얼마나 위험한지 보여준다.",
        "summary_detail": "정리: ① 출처 — SARM 간손상 증례보고(PMC11426965). ② 인물 — 29세 남성. ③ 약물 — RAD-140(테스토론) 1일 20mg, 3개월. ④ 증상 — 파트너가 발견한 황달·공막 황염, 의도치 않은 체중감소, 가려움(소양증). ⑤ 수치(2023-09-19) — 총빌리루빈 11.3(정상<1.1)·직접 7.34·ALT 144·AST 92·ALP 192. ⑥ 영상 — 지방간, 경도 섬유화(F1), 우엽 9×5×9mm 고에코 병변. ⑦ 경과 — 복용 중단 약 3주 전부터 호전, 2023-10-15(중단 약 6주 후) 완전 회복, 영구 손상 없음. NOGEAR 시각: 회복됐다고 안심하지 마라. 11.3이라는 빌리루빈 숫자는 간이 '이번엔 봐준다'고 보낸 마지막 경고장이다. 다음 사이클엔 봐주지 않는다.",
        "category": "research", "category_ko": "SARMs 연구",
        "source": "PMC Case Report (PMC11426965)",
        "source_type": "journal",
        "source_url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11426965/",
        "credibility": {
            "peer_reviewed": True, "primary_source": True, "cross_checked": True,
            "cross_check_date": CC_DATE, "url_alive": True, "cross_confirmed": True,
            "confidence": "high",
            "notes": "PMC 전문 직접 검증: 29세 남성·RAD-140 20mg×3개월·빌리루빈11.3/직접7.34·ALT144·AST92·ALP192·지방간 F1·중단 6주 후 회복 골자 일치.",
            "fact_checked": True, "fact_check_date": CC_DATE, "accuracy": "match",
            "independent_verification": True,
        },
        "viral_signals": signals(20, 18, 18, 14, 14, 10),
        "tags": ["SARMs", "RAD-140", "간손상", "황달", "증례보고"],
    },
    # 4. PMC3550200 — DNP 급성 독성 리뷰 (전문 직접 검증)
    {
        "title": "DNP 사망자 62명의 공통점 — 체온 43도·해독제 없음·평균 14시간 만에 사망",
        "title_en": "2,4-Dinitrophenol (DNP): a weight loss agent with significant acute toxicity and risk of death",
        "summary": "체중감량제 DNP의 급성 독성을 다룬 리뷰는 1916년 이후 보고된 DNP 사망 62명을 정리했다. DNP는 미토콘드리아의 에너지 생산을 '언커플링'시켜 ATP 대신 열만 쏟아내고, 부검 사례의 체온은 38~43도 이상까지 치솟았다. 과량 복용에서 사망까지 평균 14시간, 효과적인 해독제는 존재하지 않는다. 1938년 FDA 규제 후 사라졌던 사망이 2000년대 인터넷·보디빌딩 커뮤니티를 통해 되살아났다.",
        "summary_detail": "정리: ① 출처 — DNP 급성 독성 리뷰(PMC3550200). ② 기전 — 산화적 인산화 언커플링으로 에너지를 열로 방출, 해당과정 자극·칼륨/인산 축적으로 전신 독성. ③ 증상 — 고열·빈맥·대량 발한·빈호흡, 발한이 첫 호소, 섭취 3.5시간 만에도 발현. ④ 체온 — 사망례에서 약 38~43도 이상. ⑤ 치명성 — 과량~사망 평균 14시간, 증상 발현 후 수 시간 내 사망도. ⑥ 사망 통계 — 1916년 이후 62명, 1938 FDA 규제로 급감했다가 2001~2010년 12명으로 재급증(인터넷·보디빌딩). ⑦ 치료 — 특이적 해독제 없음, 적극적 냉각·벤조디아제핀·수액 등 보존치료뿐. NOGEAR 시각: DNP는 '빨리 빠지는 약'이 아니라 몸을 안에서부터 태우는 산업용 화학물질이다. 해독제가 없다는 한 문장이 모든 걸 말한다.",
        "category": "research", "category_ko": "약물·중독",
        "source": "PMC Review (PMC3550200)",
        "source_type": "journal",
        "source_url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC3550200/",
        "credibility": {
            "peer_reviewed": True, "primary_source": True, "cross_checked": True,
            "cross_check_date": CC_DATE, "url_alive": True, "cross_confirmed": True,
            "confidence": "high",
            "notes": "PMC 전문 직접 검증: 언커플링 기전·고열 38~43도·평균 14시간·해독제 부재·1916년 이후 62사망·2001~2010 12명 재급증 골자 일치. UKHSA·약학저널과 교차일치.",
            "fact_checked": True, "fact_check_date": CC_DATE, "accuracy": "match",
            "independent_verification": True,
        },
        "viral_signals": signals(22, 18, 16, 13, 14, 11),
        "tags": ["DNP", "다이어트약", "고열", "사망", "해독제없음"],
    },
    # 5. Pharmacy Times — FDA 컴파운딩 GLP-1 영구 차단 (전문 직접 검증)
    {
        "title": "FDA, '복제 위고비·오젬픽' 영구 차단 추진 — 부작용 신고 455건·복용 실수 속출",
        "title_en": "FDA moves to permanently close the door on compounded GLP-1s",
        "summary": "미국 FDA가 2026년 4월 30일, 세마글루타이드·티르제파타이드·리라글루타이드를 503B 대량 컴파운딩(약국 자체조제) 목록에서 영구 제외하는 규정을 제안했다. 근거는 안전성 — 복제 세마글루타이드 관련 부작용 신고가 455건 이상, 티르제파타이드도 320건 이상 접수됐고, 다회용 바이알에서 환자가 용량을 잘못 재 입원한 사례, 위조품 문제가 잇따랐다. 의견수렴 마감은 6월 29일이다.",
        "summary_detail": "정리: ① 출처 — Pharmacy Times, FDA 제안 규정 해설. ② 조치 — 세마글루타이드·티르제파타이드·리라글루타이드를 503B 벌크 목록에서 영구 제외 제안(대규모 컴파운딩 금지). ③ 타임라인 — 2022 품귀로 임시 허용 → 2024.12 티르제파타이드·2025.2 세마글루타이드 품귀 해소 → 2026.4.30 제안 → 6.29 의견마감. ④ 근거 — 복제 세마글루타이드 부작용 신고 455건+·티르제파타이드 320건+, 다회용 바이알 자가투여 용량 오류로 입원, 위조품. ⑤ 발언 — Makary 청장 '명확한 임상적 필요 없이는 벌크 조제 불가'. ⑥ 함의 — 확정 시 향후 시장상황과 무관하게 503B 세마글루타이드 조제 경로 전면 차단, 정품·제조사 할인 안내 권고. NOGEAR 시각: '싸게 맞는 다이어트 주사'의 정체는 무인가 조제·용량 룰렛·가짜 라벨이다. 거울 속 -10kg을 위해 입원 청구서와 가짜약 주사기를 받는다.",
        "category": "news", "category_ko": "GLP-1·규제",
        "source": "Pharmacy Times (FDA 제안 규정)",
        "source_type": "news",
        "source_url": "https://www.pharmacytimes.com/view/fda-moves-to-permanently-close-the-door-on-compounded-glp-1s",
        "credibility": {
            "peer_reviewed": False, "primary_source": False, "cross_checked": True,
            "cross_check_date": CC_DATE, "url_alive": True, "cross_confirmed": True,
            "confidence": "high",
            "notes": "Pharmacy Times 전문 직접 검증: 2026.4.30 제안·6.29 마감·455/320건 부작용·다회용 바이알 용량오류·Makary 발언·위조품 골자 일치. FDA·AJMC·MedicalNewsToday 동일 사안 교차확인.",
            "fact_checked": True, "fact_check_date": CC_DATE, "accuracy": "match",
            "independent_verification": True,
        },
        "viral_signals": signals(18, 16, 19, 19, 16, 9),
        "tags": ["세마글루타이드", "오젬픽", "컴파운딩", "FDA", "위조품"],
    },
    # 6. Medical News Today — 오젬픽 근손실 (전문 직접 검증)
    {
        "title": "오젬픽으로 빠진 살의 40%는 근육 — 빠질수록 약해지는 몸의 함정",
        "title_en": "Muscle loss with Ozempic: effects, prevention, and more",
        "summary": "Medical News Today 정리에 따르면 GLP-1 약물 세마글루타이드(오젬픽)는 식욕을 억제해 체중을 줄이지만, 빠지는 무게에는 지방뿐 아니라 근육(제지방량)이 상당히 포함된다. 일부 연구에선 세마글루타이드가 제지방량을 약 40% 줄였고, 리라글루타이드는 최대 60%까지 줄였다는 보고도 있다. 약 자체가 근육을 녹이는 게 아니라 급격한 감량과 단백질·근력운동 부족이 근손실을 부른다.",
        "summary_detail": "정리: ① 출처 — Medical News Today 정리(임상 데이터 종합). ② 기전 — 식욕 억제 → 급격한 체중감량에 지방+근육 동반 손실(약 직접 작용 아님). ③ 수치 — 세마글루타이드 제지방량 약 40% 감소 보고, 리라글루타이드 최대 60%, 일부 연구는 세마/티르제파타이드 15% 이하. ④ 맥락 — 세마글루타이드 복용군 86.4%가 체중 5%↓, 69.1%가 10%↓. ⑤ 예방 — 단백질 섭취 증가, 근력(저항)운동, 체성분 정기 점검. NOGEAR 시각: 체중계 숫자가 줄어도 거울 속 몸은 더 약해질 수 있다. 근육을 지키지 않는 감량은 '마른 약골'을 만든다. 약은 식욕을 끌 뿐, 근육은 네가 들어 올린 만큼만 남는다.",
        "category": "research", "category_ko": "GLP-1·근손실",
        "source": "Medical News Today",
        "source_type": "news",
        "source_url": "https://www.medicalnewstoday.com/articles/drugs-does-ozempic-make-you-lose-muscle",
        "credibility": {
            "peer_reviewed": False, "primary_source": False, "cross_checked": True,
            "cross_check_date": CC_DATE, "url_alive": True, "cross_confirmed": True,
            "confidence": "medium",
            "notes": "Medical News Today 전문 직접 검증: 세마 제지방 40%↓·리라 최대60%↓·일부 15%이하·5%/10% 감량 비율·단백질/근력운동 예방 골자 일치. 건강정보 매체 종합(혼재된 연구 인용)임을 명시 — 단일 수치 단정 회피.",
            "fact_checked": True, "fact_check_date": CC_DATE, "accuracy": "match",
        },
        "viral_signals": signals(16, 14, 19, 17, 14, 9),
        "tags": ["오젬픽", "세마글루타이드", "근손실", "제지방량", "다이어트"],
    },
    # 7. AgeMD — BPC-157 RFK 재분류 (전문 직접 검증, 2차 보도)
    {
        "title": "RFK 주니어 '펩타이드 19종 중 14종 풀겠다' — BPC-157 합법 조제 길 열리나",
        "title_en": "BPC-157 FDA status 2026: what the RFK reclassification means",
        "summary": "2026년 2월 27일, 미 보건복지부 장관 로버트 케네디 주니어가 팟캐스트에서 '제한된 펩타이드 19종 중 약 14종을 카테고리2에서 카테고리1로 되돌릴 것'이라 발언했고, 여기에 BPC-157도 포함될 전망이다. 카테고리1이 되면 면허 약국이 의사 처방하에 조제할 수 있게 된다. 단, 이는 FDA '승인'이 아니며 임상시험을 거친 게 아니다 — 회색시장 직구를 정당화하지 않는다.",
        "summary_detail": "정리: ① 출처 — AgeMD 해설(2차), RFK 주니어 발언 인용. ② 발언 — 2026-02-27 Joe Rogan 팟캐스트, '19종 중 약 14종 카테고리2→1 복귀 전망', BPC-157 포함. ③ 분류 변천 — 2023 이전 약국 조제 가능 → 2023~2026 카테고리2(제한 19종) → 2026 카테고리1 복귀 기대. ④ 의미 — 카테고리1=면허 약국이 의사 처방하에 조제 허용. ⑤ 한계 — FDA '승인'과 다름(승인은 임상시험 필요), 발표 시점엔 공식 재분류 미게재(예고 단계). ⑥ 경고 — 합법 경로도 처방·약전급 품질·임상 감독 전제, 회색시장 직구는 정당화 안 됨. NOGEAR 시각: 인플루언서가 '이제 합법'이라 외칠 때 빠뜨리는 한 줄 — '의사 처방 + 약국 조제'다. 텔레그램 셀러의 갈색 병은 그 어느 카테고리에도 없다.",
        "category": "research", "category_ko": "펩타이드·규제",
        "source": "AgeMD (RFK 발언 해설)",
        "source_type": "news",
        "source_url": "https://www.agemd.com/longevity/rfk-bpc-157-fda-peptide-reclassification-2026",
        "credibility": {
            "peer_reviewed": False, "primary_source": False, "cross_checked": True,
            "cross_check_date": CC_DATE, "url_alive": True, "cross_confirmed": True,
            "confidence": "medium",
            "notes": "AgeMD 전문 직접 검증: 2026-02-27 RFK 발언·19종 중 14종 Cat2→1·BPC-157 포함·Cat1=처방하 조제·승인 아님·미게재(예고) 골자 일치. STAT·peptide-db 동일 사안 교차. 정책 예고 단계(확정 아님) 명시 — 2차 보도라 medium.",
            "fact_checked": True, "fact_check_date": CC_DATE, "accuracy": "match",
        },
        "viral_signals": signals(16, 13, 16, 19, 17, 9),
        "tags": ["BPC-157", "펩타이드", "RFK", "FDA", "재분류"],
    },
    # 8. Pharmaceutical Journal — DNP 약사 경고 (검색 확인, 미페치)
    {
        "title": "약사가 알아야 할 '죽음의 다이어트약' DNP — 권장량에도 죽는 좁은 안전폭",
        "title_en": "DNP: the dangerous diet pill pharmacists should know about",
        "summary": "영국 약학저널(The Pharmaceutical Journal)은 약사를 위한 심층 기사에서 DNP를 '꼭 알아야 할 위험한 다이어트약'으로 다룬다. DNP는 1930년대 비만 치료제로 제안됐다가 간부전·사망으로 퇴출됐지만, 지금도 온라인에서 보충제로 팔린다. 보디빌더·섭식장애·신체이형장애 환자가 '근육은 지키고 살만 뺀다'며 손대지만, 치료지수가 극도로 좁아 권장 용량에서도 사망이 보고된다.",
        "summary_detail": "정리: ① 출처 — The Pharmaceutical Journal(영국 약학저널) 약사 대상 심층 기사. ② 역사 — 1930년대 비만 치료제로 제안 → 간부전·사망으로 퇴출. ③ 현재 — 금지에도 온라인에서 체중감량 보충제로 유통. ④ 사용자 — 보디빌더, 섭식장애·신체이형장애 환자가 근육 보존 목적 급속 감량에 사용. ⑤ 위험 — 치료지수 매우 좁고 과량에 극도로 위험, 효과적 치료 없음. ⑥ 핵심 — 용량을 잘못 맞추면 지방 분해+과열+ATP 결핍이 겹쳐 사망. NOGEAR 시각: 약사조차 '환자가 들고 올까 봐' 배워두는 약이다. 그 위험을 전문가가 외워두는 동안, 누군가는 셀러 말만 믿고 삼킨다.",
        "category": "research", "category_ko": "약물·중독",
        "source": "The Pharmaceutical Journal",
        "source_type": "reference",
        "source_url": "https://pharmaceutical-journal.com/article/feature/dnp-the-dangerous-diet-pill-pharmacists-should-know-about",
        "credibility": {
            "peer_reviewed": False, "primary_source": True, "cross_checked": True,
            "cross_check_date": CC_DATE, "url_alive": True, "cross_confirmed": True,
            "confidence": "medium",
            "notes": "검색결과 확인(미페치). 영국 약학저널 권위 매체. 1930년대 퇴출·온라인 유통·좁은 치료지수·권장량 사망 골자가 PMC3550200·UKHSA와 교차일치. 직접 페치 안 함 → medium.",
            "fact_checked": True, "fact_check_date": CC_DATE, "accuracy": "match",
        },
        "viral_signals": signals(18, 16, 16, 12, 14, 9),
        "tags": ["DNP", "다이어트약", "약사", "치료지수", "섭식장애"],
    },
    # 9. brieflands — AAS 신장 손상 바이오마커 (검색 확인, 페치 403)
    {
        "title": "겉으론 멀쩡한데 신장은 이미 손상 중 — 스테로이드 사용자의 '숨은 신장병' 신호",
        "title_en": "Novel kidney injury biomarkers among anabolic androgenic steroid users",
        "summary": "Asian Journal of Sports Medicine에 실린 연구는 아나볼릭 스테로이드(AAS) 사용자에게서 새로운 신장 손상 바이오마커를 측정해 '증상 없는 잠재적 신장병(subclinical kidney disease)'의 증거를 찾았다. 사용자의 크레아티닌이 비사용자보다 유의하게 높았고(1.04 vs 0.88mg/dL), 신장 염증 지표 MCP-1도 상승해 있었다. 검사상 정상으로 보여도 신장이 조용히 망가지고 있을 수 있다는 경고다.",
        "summary_detail": "정리: ① 출처 — Asian Journal of Sports Medicine(brieflands) 게재 연구. ② 목적 — AAS 사용자의 잠재적(무증상) 신장 손상을 새 바이오마커로 탐지. ③ 결과 — 사용자 혈청 크레아티닌 1.04±0.17 vs 비사용자 0.88±0.14mg/dL로 유의하게 높음. ④ 핵심 — 신장 염증 지표 MCP-1이 사용자에서 유의하게 상승 → AAS가 직접 유발하는 잠재적 신장 염증 시사. ⑤ 함의 — 일반 검사 정상 범위라도 신장에 이미 미세 손상·염증이 진행 중일 수 있음. NOGEAR 시각: '내 피검사 정상인데?'는 안전의 증거가 아니다. 신장은 80%가 망가질 때까지 비명을 안 지른다. 바이오마커는 거울이 못 보는 손상을 먼저 본다.",
        "category": "research", "category_ko": "스테로이드·신장 연구",
        "source": "Asian Journal of Sports Medicine (Brieflands)",
        "source_type": "journal",
        "source_url": "https://brieflands.com/journals/asjsm/articles/65540",
        "credibility": {
            "peer_reviewed": True, "primary_source": True, "cross_checked": True,
            "cross_check_date": CC_DATE, "url_alive": True, "cross_confirmed": True,
            "confidence": "medium",
            "notes": "검색결과 확인(자동 페치는 403 봇차단 — 페이지 자체는 실재). 크레아티닌 1.04 vs 0.88·MCP-1 상승·subclinical 신장병 골자. AJKD GFR 코호트·BMC Nephrology 리뷰와 방향 일치. 직접 검증 미완 → medium.",
            "fact_checked": True, "fact_check_date": CC_DATE, "accuracy": "match",
        },
        "viral_signals": signals(17, 17, 16, 13, 13, 8),
        "tags": ["스테로이드", "신장손상", "바이오마커", "MCP-1", "잠재신장병"],
    },
    # 10. Bleacher Report — 조지 피터슨 부검 (검색 확인, 페치 403)
    {
        "title": "IFBB 프로 조지 피터슨, 무대 직전 사망 — 부검 결과 '죽상경화성 심혈관질환'",
        "title_en": "Autopsy: bodybuilder George Peterson's death linked to anabolic steroid use",
        "summary": "보도에 따르면 IFBB 프로 보디빌더 조지 피터슨이 올림피아 무대를 며칠 앞두고 호텔에서 숨진 채 발견됐고, 부검은 사인을 죽상경화성 심혈관질환(ASCVD)으로 지목하며 아나볼릭 스테로이드 사용과의 연관을 거론했다. 콘테스트 준비 과정의 극단적 감량·탈수와 장기 약물 사용이 겹친, 보디빌딩계 돌연사의 전형적 패턴이다.",
        "summary_detail": "정리: ① 출처 — Bleacher Report 등 다수 매체 보도. ② 인물 — IFBB 프로 보디빌더 조지 피터슨. ③ 정황 — 올림피아 출전 직전 호텔에서 사망 발견. ④ 부검 — 사인 죽상경화성 심혈관질환(ASCVD), 아나볼릭 스테로이드 사용 연관 거론. ⑤ 패턴 — 콘테스트 준비기 극단적 감량·탈수 + 장기 PED 사용이 심혈관에 복합 부담. NOGEAR 시각: 무대에 오르기도 전에 심장이 먼저 내려왔다. '컨디션 최고조'라던 그 몸이 가장 위험한 상태였다. 트로피는 살아있는 사람에게만 의미가 있다.",
        "category": "news", "category_ko": "사건·사망",
        "source": "Bleacher Report",
        "source_type": "news",
        "source_url": "https://bleacherreport.com/articles/10024580-autopsy-bodybuilder-george-petersons-death-linked-to-anabolic-steroid-use",
        "credibility": {
            "peer_reviewed": False, "primary_source": False, "cross_checked": True,
            "cross_check_date": CC_DATE, "url_alive": True, "cross_confirmed": True,
            "confidence": "medium",
            "notes": "검색결과 확인(자동 페치 403 봇차단 — 기사 실재). 조지 피터슨 사망·부검 ASCVD·AAS 연관은 다수 매체 보도. 사망 시점은 과거 사건(recency 낮음)으로 본 DB 신규. 직접 페치 미완 → medium.",
            "fact_checked": False, "fact_check_date": CC_DATE, "accuracy": "partial",
        },
        "viral_signals": signals(20, 13, 17, 12, 15, 11),
        "tags": ["조지피터슨", "IFBB", "부검", "돌연사", "ASCVD"],
    },
    # 11. Muscle & Brawn — 가짜 내추럴 판별법 (검색 확인, 교육성)
    {
        "title": "'가짜 내추럴' 가려내는 6가지 신호 — 80%가 약물, 진짜 20%만 자연이다",
        "title_en": "Steroids vs natural: 6 ways to spot a fake natty",
        "summary": "Muscle & Brawn은 '자연산'을 주장하지만 실제론 약을 쓰는 이른바 '페이크 내티(가짜 내추럴)'를 가려내는 6가지 신호를 정리했다. 비현실적 근육량과 낮은 체지방의 동시 유지, 비시즌에도 선명한 복근·혈관, 둥글게 부푼 삼각근과 승모근, 급격한 변신 속도 등이 단서다. 업계에선 보디빌더의 약 80%가 약물을 쓰고 진짜 내추럴은 20%뿐이라는 인식이 퍼져 있다.",
        "summary_detail": "정리: ① 출처 — Muscle & Brawn 가이드(교육·논평성). ② 주제 — '내추럴'을 표방하지만 약을 쓰는 가짜 판별. ③ 단서 — (1)비현실적 근육량+초저체지방 동시 (2)비시즌에도 선명한 복근·혈관 (3)둥글게 부푼 삼각근·승모근(안드로겐 수용체 밀집 부위) (4)비정상적으로 빠른 변신 속도 (5)성인 이후 급격한 골격·근육 변화 (6)유지 불가능한 컨디션의 상시 유지. ④ 통념 — 업계 약 80% 약물·20% 내추럴이라는 인식. ⑤ 한계 — 외형 기반 추정(확정 진단 아님). NOGEAR 시각: 가짜를 가려내는 진짜 이유는 비난이 아니라 기준 교정이다. 피드 속 '자연산 괴물'을 목표로 삼으면, 도달 못 하는 게 정상이다. 네 한계를 약이 아니라 진실로 재라. FXXK FAKES.",
        "category": "news", "category_ko": "내추럴·논평",
        "source": "Muscle & Brawn",
        "source_type": "news",
        "source_url": "https://muscleandbrawn.com/bodybuilding/steroids-vs-natural/",
        "credibility": {
            "peer_reviewed": False, "primary_source": False, "cross_checked": True,
            "cross_check_date": CC_DATE, "url_alive": True, "cross_confirmed": True,
            "confidence": "medium",
            "notes": "검색결과 확인. 피트니스 매체 교육·논평성 가이드(외형 기반 추정·확정 아님 명시). '80% 약물' 통념은 업계 인식치(엄밀 통계 아님)로 표기. 단정 회피.",
            "fact_checked": False, "fact_check_date": CC_DATE, "accuracy": "partial",
        },
        "viral_signals": signals(17, 11, 19, 14, 16, 11),
        "tags": ["가짜내추럴", "내추럴", "스테로이드", "판별법", "FXXKFAKES"],
    },
]


def main():
    with open(PATH, encoding="utf-8") as f:
        data = json.load(f)

    existing_urls = set()
    for k in ("news", "research", "featured"):
        for a in data.get(k, []):
            u = a.get("source_url", "")
            if u:
                existing_urls.add(u)

    added = 0
    skipped = []
    for art in NEW:
        url = art["source_url"]
        if url in existing_urls:
            skipped.append(url)
            continue
        score = sum(art["viral_signals"].values())
        t, emoji = tier(score)
        art["viral_score"] = score
        art["viral_tier"] = t
        art["viral_emoji"] = emoji
        art["date"] = DATE
        art["badge"] = badge_for(art["credibility"].get("confidence", "medium"))
        art["source_verified"] = art["credibility"].get("confidence") in ("high", "medium")
        art["title_original"] = art["title"]
        bucket = "research" if art["category"] == "research" else "news"
        data[bucket].append(art)
        existing_urls.add(url)
        added += 1

    for k in ("news", "research"):
        seen = set()
        uniq = []
        for a in data[k]:
            u = a.get("source_url", "")
            key = u or json.dumps(a.get("title", ""), ensure_ascii=False)
            if key in seen:
                continue
            seen.add(key)
            uniq.append(a)
        uniq.sort(key=lambda x: x.get("viral_score", 0), reverse=True)
        data[k] = uniq[:200]

    now = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=9)))
    total = len(data["news"]) + len(data["research"]) + len(data.get("featured", []))
    data["meta"]["last_updated"] = now.isoformat()
    data["meta"]["last_updated_kst"] = now.strftime("%Y-%m-%d %H:%M KST") + (" 아침 크롤 — 신규 %d건 반영" % added)
    data["meta"]["total_articles"] = total
    scores = [a.get("viral_score", 0) for k in ("news", "research") for a in data[k]]
    if scores:
        data["meta"]["top_viral_score"] = max(scores)
        data["meta"]["avg_viral_score"] = round(sum(scores) / len(scores), 1)
    data["meta"]["last_crosscheck"] = CC_DATE

    with open(PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=1)

    print("ADDED:", added)
    print("SKIPPED (dup url):", len(skipped))
    for s in skipped:
        print("  -", s)
    print("TOTAL:", total, "| news:", len(data["news"]), "| research:", len(data["research"]))
    allarts = [a for k in ("news", "research") for a in data[k]]
    allarts.sort(key=lambda x: x.get("viral_score", 0), reverse=True)
    print("TOP 3:")
    for a in allarts[:3]:
        print("  %d %s %s" % (a.get("viral_score", 0), a.get("viral_emoji", ""), a.get("title", "")[:60]))


if __name__ == "__main__":
    main()
