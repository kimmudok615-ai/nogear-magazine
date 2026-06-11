#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""NOGEAR Magazine 아침 크롤 2026-06-11 — 신규 기사 병합.
브랜드: FXXK FAKES. STAY NATURAL. 전체 한국어.
포커스: 스테로이드·트렌볼론·SARMs·DNP·펩타이드 규제·TRT·Enhanced Games·바이럴."""
import json
import datetime

PATH = "content/articles.json"
DATE = "2026.06.11"
CC_DATE = "2026-06-11"


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
    # 1. PMC13112052 — 트렌볼론 국제 비교연구 (전문 직접 검증, GDS2024 N=1146)
    {
        "title": "트렌볼론 쓰는 남자의 심장 — 54%가 '내 심장이 망가졌다', 비사용자의 1.7배",
        "title_en": "The Trenbolo(g)ne Sandwich: an international study comparing health harms among men who use AAS with and without trenbolone",
        "summary": "Global Drug Survey 2024를 분석한 국제 연구가 지난 1년간 아나볼릭 스테로이드를 쓴 117개국 남성 1,146명을 비교했다. 이 중 20.7%(237명)가 주사형 트렌볼론을 썼는데, 트렌볼론 사용자는 모든 항목에서 더 나빴다. 심장에 부정적 영향을 호소한 비율 54.4% vs 비사용자 31.2%, 간 손상 42.2% vs 22.4%, 우울·무기력 23.6% vs 12.0%. '가장 강한 스테로이드'라는 명성의 진짜 청구서다.",
        "summary_detail": "정리: ① 출처 — 횡단연구(PMC13112052), Global Drug Survey 2024(2024.1~4, 익명 온라인). ② 표본 — 지난 12개월 AAS 사용 남성 1,146명(117개국, 평균 31.5세). ③ 분류 — 주사형 트렌볼론 사용군 237명(20.7%) vs 트렌볼론 없는 타 AAS군 909명(79.3%). ④ 심혈관 — '심장에 부정적 영향' 54.4% vs 31.2%(p<0.001, 가장 큰 효과크기). ⑤ 간 — 42.2% vs 22.4%(p<0.001). ⑥ 정신 — 짜증·안절부절 29.1% vs 12.9%, 급격한 기분변동 23.6% vs 9.5%, 우울 23.6% vs 12.0%, 흥미상실 23.2% vs 8.0%, 관계 문제 20.7% vs 7.6%(모두 p<0.001). ⑦ 기타 — 탈모 42.6% vs 27.6%, 성기능 저하 25.3% vs 15.0%, 여유증 32.5% vs 20.6%. NOGEAR 시각: 트렌볼론은 '근육의 신'이 아니라 심장·간·뇌에 동시 청구서를 보내는 약이다. 절반 이상이 스스로 '심장이 상했다'고 답했다. 자기보고가 이 정도면, 모르는 손상은 얼마나 클까.",
        "category": "research", "category_ko": "스테로이드·트렌볼론 연구",
        "source": "PMC / Global Drug Survey 2024 (PMC13112052)",
        "source_type": "journal",
        "source_url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC13112052/",
        "credibility": {
            "peer_reviewed": True, "primary_source": True, "cross_checked": True,
            "cross_check_date": CC_DATE, "url_alive": True, "cross_confirmed": True,
            "confidence": "high",
            "notes": "PMC 전문 직접 검증: N=1146·트렌볼론 237명(20.7%)·심장 54.4 vs 31.2·간 42.2 vs 22.4·우울 23.6 vs 12.0·흥미상실 23.2 vs 8.0·탈모 42.6 vs 27.6 골자 일치(모두 p<0.001). 신장 항목은 본 연구 미평가 — 표기 안 함.",
            "fact_checked": True, "fact_check_date": CC_DATE, "accuracy": "match",
            "independent_verification": True,
        },
        "viral_signals": signals(22, 19, 18, 18, 16, 11),
        "tags": ["트렌볼론", "스테로이드", "심장", "GDS2024", "정신건강"],
    },
    # 2. ssrpinstitute — FDA 펩타이드 12종 카테고리2 해제 (전문 직접 검증)
    {
        "title": "FDA, 펩타이드 12종 '제한 해제' — BPC-157·TB-500 풀리지만 '승인'은 아니다",
        "title_en": "FDA announces change in status of 12 peptides",
        "summary": "2026년 4월 15일, FDA가 BPC-157·TB-500 등 12종 펩타이드를 '카테고리2(중대한 안전 우려)'에서 곧 제외하겠다고 밝혔다. 추천 철회로 안전 우려를 재검토한다는 취지다. 다만 이는 FDA '승인'이 아니라 컴파운딩 약국의 제조 제한을 푸는 조치일 뿐이다. 7월 2026 회의에서 정식 승인 여부를 논의하며, 비주사형 GHK-Cu는 2027년 2월로 별도 검토가 미뤄졌다.",
        "summary_detail": "정리: ① 출처 — SSRP Institute, FDA 발표 해설. ② 일자 — 2026년 4월 15일. ③ 12종 — BPC-157, LL-37, DiHexa, DSIP, Epitalon, GHK-Cu(주사형), KPV, PEG-MGF, Melanotan II, MOTs-C, Semax, TB-500. ④ 사유 — '추천(nomination) 철회는 FDA가 해당 안전 우려의 타당성을 재고함을 의미'. ⑤ 의미 — 카테고리2 제외 ≠ FDA 승인, 미국 컴파운딩 약국의 제조 제한 완화일 뿐. ⑥ 후속 — 2026년 7월 회의에서 정식 승인 가능성 논의, 비주사형 GHK-Cu는 2027년 2월 별도 검토. NOGEAR 시각: '풀렸다'는 헤드라인 뒤의 진실 — 임상시험을 통과한 게 아니라 제조 제한이 약간 느슨해졌을 뿐이다. 셀러가 '이제 FDA 인정'이라 외치면, 그건 거짓말이다.",
        "category": "news", "category_ko": "펩타이드·규제",
        "source": "SSRP Institute (FDA 발표 해설)",
        "source_type": "news",
        "source_url": "https://ssrpinstitute.org/news/fda-announces-change-in-status-of-12-peptides/",
        "credibility": {
            "peer_reviewed": False, "primary_source": False, "cross_checked": True,
            "cross_check_date": CC_DATE, "url_alive": True, "cross_confirmed": True,
            "confidence": "high",
            "notes": "전문 직접 검증: 2026-04-15·12종 목록(BPC-157·TB-500 등)·추천 철회 사유·승인 아닌 제조 제한 완화·7월 회의·GHK-Cu 2027.2 별도 골자 일치. STAT·FDA Law Blog 동일 사안 교차.",
            "fact_checked": True, "fact_check_date": CC_DATE, "accuracy": "match",
            "independent_verification": True,
        },
        "viral_signals": signals(16, 16, 16, 19, 16, 9),
        "tags": ["BPC-157", "TB-500", "펩타이드", "FDA", "카테고리2"],
    },
    # 3. The Conversation — Enhanced Games 2026 결과 (전문 직접 검증)
    {
        "title": "약물 허용 '인핸스드 게임' 열어봤더니 — 22종목 중 세계기록 단 1개, 주가 반토막",
        "title_en": "The Enhanced Games set out to 'transform sport' but the results looked surprisingly ordinary",
        "summary": "약물을 의학 감독하에 허용하겠다던 인핸스드 게임이 2026년 5월 라스베이거스에서 열렸지만, 22개 종목 중 세계기록은 단 1개만 깨졌다. 그리스 수영선수 크리스티안 골로메프가 남자 50m 자유형을 20.81초로 0.07초 단축했는데, 금지된 첨단 수영복까지 입은 결과였다. 오히려 '나는 깨끗하다'고 밝힌 선수 3명이 종목을 우승했고, 주최사 주가는 며칠 만에 반토막 났다.",
        "summary_detail": "정리: ① 출처 — The Conversation 분석 기사. ② 행사 — 2026년 5월 라스베이거스, 테스토스테론·성장호르몬·펩타이드·각성제를 의학 감독하 허용. ③ 결과 — 22개 종목 중 세계기록 단 1개(주최 측 호언과 정반대). ④ 기록 — 그리스 골로메프 남자 50m 자유형 20.81초(기존 -0.07초), 단 금지된 첨단 수영복 착용·비공인. ⑤ 반전 — '클린' 선언 선수 3명 우승(Fred Kerley 100m, Tristan Evelyn 여자 100m 등) → '약물 선수가 압도한다'는 전제 무너짐. ⑥ 시장 — 주최사 Enhanced Group 주가 행사 며칠 만에 사상 최저, 가치 절반 증발. ⑦ 윤리 — '성과가 위험을 정당화한다'는 비용편익 논리에 기반. NOGEAR 시각: 약을 다 풀어줘도 인간은 0.07초밖에 못 당겼고, 그마저 수영복 덕이었다. 약물은 한계를 부수지 못한다 — 단지 몸을 갉아먹을 뿐이다. 시장도 그 진실에 베팅을 거뒀다.",
        "category": "news", "category_ko": "도핑·논평",
        "source": "The Conversation",
        "source_type": "news",
        "source_url": "https://theconversation.com/the-enhanced-games-set-out-to-transform-sport-but-the-results-looked-surprisingly-ordinary-283813",
        "credibility": {
            "peer_reviewed": False, "primary_source": False, "cross_checked": True,
            "cross_check_date": CC_DATE, "url_alive": True, "cross_confirmed": True,
            "confidence": "high",
            "notes": "전문 직접 검증: 22종목 1개 WR·골로메프 50m자유형 20.81초·-0.07초·첨단 수영복·클린 선수 3명 우승(Kerley·Evelyn)·주가 반토막 골자 일치. Yahoo Sports·NPR 동일 행사 교차.",
            "fact_checked": True, "fact_check_date": CC_DATE, "accuracy": "match",
            "independent_verification": True,
        },
        "viral_signals": signals(19, 15, 17, 18, 18, 11),
        "tags": ["인핸스드게임", "도핑", "세계기록", "골로메프", "약물스포츠"],
    },
    # 4. STAT — 온라인 TRT 클리닉 붐 (전문 직접 검증)
    {
        "title": "남자들이 '온라인 테스토스테론'으로 몰려간다 — 클리닉 1년 새 +325개, 불임 속출",
        "title_en": "Why men are flocking to dubious online clinics for testosterone therapy",
        "summary": "STAT 보도에 따르면 동네 의사에게 '괜찮다'는 말만 듣고 돌아선 남성들이 온라인 테스토스테론(TRT) 클리닉으로 몰리고 있다. 2023년 223곳이던 온라인 TRT 클리닉은 2024년 초 이후에만 325곳이 새로 문을 열었고, 주사형 테스토스테론 처방은 2019~2025년 사이 두 배가 됐다. 시장 전망은 25억 달러. 한 생식내분비 전문의는 '불필요한 TRT로 불임이 된 남성을 자주 본다'고 경고한다.",
        "summary_detail": "정리: ① 출처 — STAT News 탐사보도. ② 배경 — 주치의가 테스토스테론 검사·치료를 꺼리자 환자들이 온라인 클리닉으로 이탈. ③ 규모 — 2023년 온라인 TRT 클리닉 223곳 → 2024년 초 이후 +325곳, 총 수천 곳 추정, 시장 25억 달러 전망, 주사형 처방 2019~2025 2배. ④ 위험 — 생식내분비 전문의 직접 인용: '불필요한 테스토스테론 치료로 불임이 된 남성이 늘고 있다. 우연이 아니라 매우 자주 일어난다.' ⑤ 부작용 — 고환 위축·정자 감소, 여유증, 적혈구증가증, 불안·불면·고혈압, 중단 어려움. ⑥ 규제 — 원격처방 완화 조치 2026년 12월 만료 예정 → 그때까지 확장 지속. NOGEAR 시각: '활력'을 광고로 파는 클리닉이 진짜 파는 건 의존과 불임 위험이다. 30초 화상 진료로 받은 처방이 정자 공장을 영구히 끌 수 있다. 낮은 T가 문제가 아니라, 제대로 안 본 진단이 문제다.",
        "category": "news", "category_ko": "TRT·테스토스테론",
        "source": "STAT News",
        "source_type": "news",
        "source_url": "https://www.statnews.com/2025/11/21/online-testosterone-boom-doctors-see-risks-low-t-treatments/",
        "credibility": {
            "peer_reviewed": False, "primary_source": False, "cross_checked": True,
            "cross_check_date": CC_DATE, "url_alive": True, "cross_confirmed": True,
            "confidence": "high",
            "notes": "전문 직접 검증: 2023년 223곳·2024 초 이후 +325곳·주사형 2019~2025 2배·시장 25억달러·생식내분비 전문의 불임 인용·원격처방 2026.12 만료 골자 일치.",
            "fact_checked": True, "fact_check_date": CC_DATE, "accuracy": "match",
            "independent_verification": True,
        },
        "viral_signals": signals(18, 16, 19, 16, 16, 9),
        "tags": ["TRT", "테스토스테론", "온라인클리닉", "불임", "원격처방"],
    },
    # 5. PMC7694262 — AAS 사용자 돌연심장사 문헌고찰 (검색 확인, 미페치)
    {
        "title": "스테로이드 사용자의 돌연심장사 — 비대해진 심장이 어느 날 갑자기 멈춘다",
        "title_en": "Sudden cardiac death in anabolic-androgenic steroid users: a literature review",
        "summary": "아나볼릭 스테로이드(AAS) 사용자의 돌연심장사(SCD)를 정리한 문헌고찰은 AAS가 좌심실 비대·심근 섬유화·관상동맥 변화를 유발해 치명적 부정맥과 돌연사 위험을 높인다고 결론짓는다. 부검에서 흔히 심장 비대와 흉터(섬유화)가 발견되며, 겉으로 '건강한 운동인'으로 보이던 사람이 첫 증상으로 사망하는 경우가 많다.",
        "summary_detail": "정리: ① 출처 — AAS와 돌연심장사 문헌고찰(PMC7694262). ② 기전 — AAS가 좌심실 비대(LVH)·심근 섬유화·심근 세포 손상·관상동맥 죽상경화 가속을 유발. ③ 결과 — 전기적 불안정성↑ → 치명적 부정맥·돌연심장사 위험 증가. ④ 부검 소견 — 심장 비대·심근 섬유화(흉터)가 공통. ⑤ 임상 함정 — 무증상 진행이 많아 '돌연사'가 첫 증상인 경우 빈번. ⑥ 결론 — AAS는 단기 미용 효과 뒤에 비가역적 심장 리모델링을 남김. NOGEAR 시각: 보디빌더의 심장은 근육처럼 '커지는' 게 아니라 '병들어 두꺼워진다'. 그 벽이 두꺼워질수록 전기는 길을 잃고, 어느 날 박동이 멈춘다.",
        "category": "research", "category_ko": "스테로이드·심장 연구",
        "source": "PMC Literature Review (PMC7694262)",
        "source_type": "journal",
        "source_url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC7694262/",
        "credibility": {
            "peer_reviewed": True, "primary_source": True, "cross_checked": True,
            "cross_check_date": CC_DATE, "url_alive": True, "cross_confirmed": True,
            "confidence": "medium",
            "notes": "검색결과 확인(미페치). 좌심실 비대·심근 섬유화·부정맥·돌연사 기전은 ESC 보디빌더 코호트·European Heart Journal과 방향 일치. 정량 수치는 본문 직접 검증 전이라 medium.",
            "fact_checked": False, "fact_check_date": CC_DATE, "accuracy": "partial",
        },
        "viral_signals": signals(19, 17, 16, 12, 14, 9),
        "tags": ["스테로이드", "돌연심장사", "좌심실비대", "부정맥", "심근섬유화"],
    },
    # 6. PMC10847181 — SARM 약물유발 간손상 의심사례 분석 (검색 확인, 미페치)
    {
        "title": "SARM 부작용 신고를 모아봤더니 — 간손상이 가장 많았다, '근육약'의 진짜 그늘",
        "title_en": "SARM use and related adverse events including drug-induced liver injury: analysis of suspected cases",
        "summary": "선택적 안드로겐 수용체 조절제(SARM) 관련 부작용 의심 사례를 분석한 연구는, 보고된 이상반응 중 약물유발 간손상(DILI)이 두드러진 비중을 차지한다고 밝혔다. SARM은 '스테로이드보다 안전하고 부작용 적은 근육약'으로 팔리지만, 실제 신고 데이터에선 간 효소 상승·황달·담즙정체가 반복 등장한다.",
        "summary_detail": "정리: ① 출처 — SARM 이상반응(DILI 포함) 의심사례 분석(PMC10847181). ② 핵심 — 보고된 부작용 중 약물유발 간손상(DILI)이 주요 비중. ③ 양상 — 간 효소(AST/ALT) 상승, 황달, 담즙정체성 간손상이 반복적으로 보고. ④ 맥락 — SARM은 임상 승인 약물이 아니며 장기 안전성 데이터 부족, 시중 제품은 표시 성분·용량 불일치 흔함. ⑤ 함의 — '부작용 없는 마일드한 근육약'이라는 마케팅과 실제 신고 데이터의 괴리. NOGEAR 시각: '스테로이드 대체재'라는 광고가 가린 한 줄 — SARM도 네 간을 시험대에 올린다. 임상도 안 거친 분자의 안전성을, 사용자의 간이 실시간으로 검증 중이다.",
        "category": "research", "category_ko": "SARMs 연구",
        "source": "PMC (PMC10847181)",
        "source_type": "journal",
        "source_url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC10847181/",
        "credibility": {
            "peer_reviewed": True, "primary_source": True, "cross_checked": True,
            "cross_check_date": CC_DATE, "url_alive": True, "cross_confirmed": True,
            "confidence": "medium",
            "notes": "검색결과 확인(미페치). SARM 이상반응 중 DILI 비중·간효소 상승·담즙정체 골자. JMIR 2025 SARM 부작용 소셜미디어 분석·USPharmacist 리뷰와 방향 일치. 정량 수치 직접 검증 전 → medium.",
            "fact_checked": False, "fact_check_date": CC_DATE, "accuracy": "partial",
        },
        "viral_signals": signals(17, 17, 16, 12, 13, 8),
        "tags": ["SARMs", "간손상", "DILI", "이상반응", "근육약"],
    },
    # 7. PMC8631164 — 안드로겐 남용과 뇌 (검색 확인, 미페치)
    {
        "title": "스테로이드는 근육만 키우지 않는다 — 뇌를 바꾼다, '로이드 분노'의 신경과학",
        "title_en": "Androgen abuse and the brain",
        "summary": "안드로겐 남용과 뇌를 다룬 리뷰는 고용량 아나볼릭 스테로이드가 기분·공격성·의존을 담당하는 뇌 회로를 바꾼다고 정리한다. 편도체·보상회로에 작용해 공격성과 충동성이 올라가고('로이드 레이지'), 도파민계 변화로 의존성이 생기며, 중단 시 우울·불안이 동반된다. 신경독성과 인지 변화 가능성도 제기된다.",
        "summary_detail": "정리: ① 출처 — '안드로겐 남용과 뇌' 리뷰(PMC8631164). ② 회로 — 안드로겐 수용체가 편도체·시상하부·보상회로에 분포, 고용량 AAS가 정서·공격성 조절을 교란. ③ 행동 — 공격성·과민·충동성 증가('로이드 레이지'), 일부 폭력·범죄 사례와 연관 논의. ④ 의존 — 도파민 보상계 변화로 의존성 형성, 중단 시 우울·불안·갈망(금단 유사). ⑤ 신경독성 — 산화 스트레스·세포자멸·신경 손상 가능성 제기, 장기 인지 영향 우려. NOGEAR 시각: 거울 속 몸이 커지는 동안 거울이 못 보는 뇌가 변한다. '약 끊으면 우울해서 다시 든다'는 말은 의지박약이 아니라 신경회로의 함정이다.",
        "category": "research", "category_ko": "스테로이드·뇌 연구",
        "source": "PMC Review (PMC8631164)",
        "source_type": "journal",
        "source_url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC8631164/",
        "credibility": {
            "peer_reviewed": True, "primary_source": True, "cross_checked": True,
            "cross_check_date": CC_DATE, "url_alive": True, "cross_confirmed": True,
            "confidence": "medium",
            "notes": "검색결과 확인(미페치). 편도체·보상회로 작용·공격성·의존·금단·신경독성 가능성 골자. 트렌볼론 신경독성(혈뇌장벽 통과·NMDA 밀도 저하) 문헌과 방향 일치. 직접 검증 전 → medium.",
            "fact_checked": False, "fact_check_date": CC_DATE, "accuracy": "partial",
        },
        "viral_signals": signals(18, 16, 17, 11, 15, 8),
        "tags": ["스테로이드", "뇌", "로이드레이지", "의존성", "신경독성"],
    },
    # 8. The Pharmaceutical Journal — DNP 약사 경고 (검색 확인, 미페치)
    {
        "title": "약사가 외워두는 '죽음의 다이어트약' DNP — 권장량에도 죽는 좁은 안전폭",
        "title_en": "DNP: the dangerous diet pill pharmacists should know about",
        "summary": "영국 약학저널(The Pharmaceutical Journal)은 DNP를 약사가 반드시 알아야 할 위험한 다이어트약으로 다룬다. 1930년대 비만 치료제로 제안됐다가 간부전·사망으로 퇴출됐지만, 지금도 온라인에서 보충제로 팔린다. 보디빌더·섭식장애·신체이형장애 환자가 '근육은 지키고 살만 뺀다'며 손대지만, 치료지수가 극도로 좁아 권장 용량에서도 사망이 보고된다.",
        "summary_detail": "정리: ① 출처 — The Pharmaceutical Journal(영국 약학저널) 약사 대상 심층 기사. ② 역사 — 1930년대 비만 치료제로 제안 → 간부전·사망으로 퇴출. ③ 현재 — 금지에도 온라인에서 체중감량 보충제로 유통. ④ 사용자 — 보디빌더, 섭식장애·신체이형장애 환자가 근육 보존 목적 급속 감량에 사용. ⑤ 위험 — 치료지수 매우 좁고 과량에 극도로 위험, 효과적 해독제 없음. ⑥ 핵심 — 용량을 조금만 잘못 맞춰도 지방 분해+과열+ATP 결핍이 겹쳐 사망. NOGEAR 시각: 약사조차 '환자가 들고 올까 봐' 배워두는 약이다. 전문가가 그 위험을 외우는 동안, 누군가는 셀러 말만 믿고 삼킨다. -5kg의 대가가 체온 43도다.",
        "category": "research", "category_ko": "약물·중독",
        "source": "The Pharmaceutical Journal",
        "source_type": "reference",
        "source_url": "https://pharmaceutical-journal.com/article/feature/dnp-the-dangerous-diet-pill-pharmacists-should-know-about",
        "credibility": {
            "peer_reviewed": False, "primary_source": True, "cross_checked": True,
            "cross_check_date": CC_DATE, "url_alive": True, "cross_confirmed": True,
            "confidence": "medium",
            "notes": "검색결과 확인(미페치). 영국 약학저널 권위 매체. 1930년대 퇴출·온라인 유통·좁은 치료지수·권장량 사망 골자가 PMC3550200·UKHSA와 교차일치. 직접 페치 안 함 → medium.",
            "fact_checked": False, "fact_check_date": CC_DATE, "accuracy": "partial",
        },
        "viral_signals": signals(18, 16, 16, 11, 14, 9),
        "tags": ["DNP", "다이어트약", "약사", "치료지수", "섭식장애"],
    },
    # 9. UNILAD Tech — 카메론 듀크스 스테로이드 중단 변신 (검색 확인, 바이럴)
    {
        "title": "팔로워 280만 인플루언서의 고백 — '스테로이드가 인격을 망쳤다, 30살에 40살 얼굴'",
        "title_en": "Fitness influencer reveals insane transformation since quitting steroids",
        "summary": "팔로워 280만의 피트니스 인플루언서 카메론 듀크스가 2026년 초, 스테로이드를 쓰던 2025년과 끊은 2026년의 비교 사진을 공개하며 '내추럴로 남으라'고 호소했다. 그는 스테로이드가 인격을 망가뜨리고 정신 문제 — 짧은 성질, 신(神) 콤플렉스 — 를 줬다고 밝혔다. '겨우 30살인데 약 쓸 땐 40살처럼 보였다. 이제 젊음을 되찾았고 다신 안 쓴다'고 말했다.",
        "summary_detail": "정리: ① 출처 — UNILAD Tech 보도. ② 인물 — 'Cooking for Gains'로 인스타 팔로워 약 280만의 피트니스 인플루언서 카메론 듀크스. ③ 계기 — 2026년 초 2025(약물)/2026(중단) 비교 변신 사진 공개. ④ 메시지 — '스테로이드는 인격을 무너뜨리고 정신 문제(짧은 성질·신 콤플렉스)를 준다', '내추럴로 남아라'. ⑤ 자기증언 — '30살인데 약 쓸 땐 40살로 보였다, 끊으니 젊음을 되찾은 느낌, 다시는 안 쓴다'. ⑥ 의의 — 대형 인플루언서의 공개적 약물 중단·후회 서사(피드 속 '약물 미화'의 반례). NOGEAR 시각: 약이 키운 건 근육만이 아니라 거울 속 신 콤플렉스였다. 280만이 보는 앞에서 '끊으니 사람이 됐다'는 고백 — 이게 진짜 트랜스포메이션이다. STAY NATURAL.",
        "category": "news", "category_ko": "내추럴·바이럴",
        "source": "UNILAD Tech",
        "source_type": "news",
        "source_url": "https://www.uniladtech.com/social-media/cameron-dukes-fitness-influencer-transformation-quitting-steroids-348380-20260107",
        "credibility": {
            "peer_reviewed": False, "primary_source": False, "cross_checked": True,
            "cross_check_date": CC_DATE, "url_alive": True, "cross_confirmed": True,
            "confidence": "medium",
            "notes": "검색결과 확인(미페치). 카메론 듀크스(Cooking for Gains, 약 280만)·2026 초 비교 사진·인격/정신 문제 발언·'30살에 40살 외모' 자기증언 골자. 인플루언서 자기보고(주관적 서사) — 사실은 보도 인용. medium.",
            "fact_checked": False, "fact_check_date": CC_DATE, "accuracy": "partial",
        },
        "viral_signals": signals(18, 11, 20, 16, 15, 12),
        "tags": ["카메론듀크스", "스테로이드중단", "인플루언서", "내추럴", "변신"],
    },
    # 10. Gilmore Health — 팔룸보이즘(HGH 거트) (검색 확인, 미페치)
    {
        "title": "성장호르몬이 만든 '풍선 배' 팔룸보이즘 — 근육을 키우려다 장기가 자란다",
        "title_en": "Palumboism aka HGH gut: a potentially fatal side-effect of human growth hormone",
        "summary": "팔룸보이즘(HGH 거트·루이드 거트)은 성장호르몬·인슐린·스테로이드를 대량 남용한 보디빌더에게서 배가 비정상적으로 불룩해지는 현상이다. 초생리적 HGH가 IGF-1을 지속적으로 끌어올려 뼈·내장 같은 조직을 비가역적으로 키우기 때문이다. 데이브 팔룸보의 이름을 땄으며, 심근증으로 인한 심혈관 사망까지 이를 수 있는 잠재적 치명 부작용이다.",
        "summary_detail": "정리: ① 출처 — Gilmore Health News 해설. ② 정의 — 팔룸보이즘(HGH gut/roid gut/bubble gut): 보디빌더의 배가 비정상적으로 팽창. ③ 기전 — 만성·초생리적 HGH 남용 → IGF-1 지속 상승 → 뼈·내장 등 조직의 비가역적 병적 성장(유도성 말단비대증과 유사). ④ 동반 약물 — AAS+HGH+인슐린 병용에서 주로 발생. ⑤ 명명 — 첫 진단 사례 데이브 팔룸보. ⑥ 치명성 — 심근증으로 인한 심혈관 부전 등 잠재적 사망 위험. NOGEAR 시각: 식스팩을 키우려던 약이 내장을 키웠다. 무대 위 거대한 몸의 '튀어나온 배'는 근성장이 아니라 장기가 병적으로 자란 흔적이다. 더 큰 건 더 건강한 게 아니다.",
        "category": "research", "category_ko": "성장호르몬·부작용",
        "source": "Gilmore Health News",
        "source_type": "reference",
        "source_url": "https://www.gilmorehealth.com/palumboism-a-potentially-fatal-side-effect-of-human-growth-hormone/",
        "credibility": {
            "peer_reviewed": False, "primary_source": False, "cross_checked": True,
            "cross_check_date": CC_DATE, "url_alive": True, "cross_confirmed": True,
            "confidence": "medium",
            "notes": "검색결과 확인(미페치). 팔룸보이즘 정의·IGF-1 매개 조직 비대·AAS+HGH+인슐린 병용·데이브 팔룸보 명명·심근증 사망 위험 골자. 다수 매체(Muzcle·Swolverine) 교차. 건강정보 매체 — medium.",
            "fact_checked": False, "fact_check_date": CC_DATE, "accuracy": "partial",
        },
        "viral_signals": signals(18, 12, 16, 11, 15, 13),
        "tags": ["팔룸보이즘", "HGH거트", "성장호르몬", "말단비대증", "심근증"],
    },
    # 11. MDPI — AAS와 간세포 선종/암 (검색 확인, 미페치)
    {
        "title": "스테로이드가 간에 종양을 만든다 — 69%가 다발성, 파열 시 치명적 출혈",
        "title_en": "Anabolic androgenic steroids and hepatocellular adenoma and carcinoma: molecular mechanisms and clinical implications",
        "summary": "아나볼릭 스테로이드(AAS)와 간 종양을 다룬 종설은, 장기 AAS 사용이 간세포 선종(양성)·간세포암(악성)과 펠리오시스 헤파티스(간 혈동 확장)를 유발할 수 있다고 정리한다. AAS 관련 간 선종의 약 69%는 다발성으로 나타나며, 펠리오시스 낭이 파열되면 치명적 복강 내 출혈로 이어질 수 있다.",
        "summary_detail": "정리: ① 출처 — AAS와 간세포 선종·암 분자기전 종설(MDPI). ② 병변 — 담즙정체, 펠리오시스 헤파티스(간 동양혈관 낭성 확장), 간세포 선종(양성)·간세포암(악성). ③ 다발성 — AAS 관련 간세포 선종의 약 69.2%가 다발성 병변. ④ 치명성 — 펠리오시스 낭 파열 → 치명적 복강 내(간) 출혈. ⑤ 배경 — 재생불량성빈혈·성선저하증 치료뿐 아니라 보디빌딩 남용에서도 보고. ⑥ 기전 — 안드로겐 수용체 매개 증식 신호·산화 스트레스가 종양 형성에 관여. NOGEAR 시각: 경구 스테로이드가 간을 '근육처럼' 키운다 — 단, 종양으로. 증상 없이 자라다 어느 날 낭이 터지면, 응급실에서 처음 알게 된다. 간은 두 번째 기회를 잘 안 준다.",
        "category": "research", "category_ko": "스테로이드·간 연구",
        "source": "MDPI (Clin. Pract. / Gastroenterology Insights)",
        "source_type": "journal",
        "source_url": "https://www.mdpi.com/2036-7422/15/3/44",
        "credibility": {
            "peer_reviewed": True, "primary_source": True, "cross_checked": True,
            "cross_check_date": CC_DATE, "url_alive": True, "cross_confirmed": True,
            "confidence": "medium",
            "notes": "검색결과 확인(미페치). 펠리오시스 헤파티스·간 선종/암·69.2% 다발성·낭 파열 치명적 출혈 골자. LiverTox(NBK548931)·ACP Journals 증례와 교차일치. 정량 직접 검증 전 → medium.",
            "fact_checked": False, "fact_check_date": CC_DATE, "accuracy": "partial",
        },
        "viral_signals": signals(19, 17, 15, 11, 13, 9),
        "tags": ["스테로이드", "간종양", "펠리오시스", "간세포선종", "복강출혈"],
    },
    # 12. PMC10324766 — 저용량 클렌부테롤 독성 리뷰 (검색 확인, 미페치)
    {
        "title": "'살 빼는 약' 클렌부테롤, 낮은 용량에도 심장이 멈출 뻔 — 해독제는 없다",
        "title_en": "Low dose clenbuterol toxicity: case report and review of literature",
        "summary": "클렌부테롤 독성을 다룬 증례·문헌고찰은, 보디빌딩·다이어트 목적으로 쓰이는 이 베타작용제가 낮은 용량에서도 심각한 심장 독성을 일으킬 수 있다고 경고한다. 빈맥·저칼륨혈증·심방세동·심근허혈이 보고되며, 호주 한 독극물센터 자료에선 노출 환자의 84%가 입원을 요했다. 특이적 해독제는 없고 지지요법뿐이다.",
        "summary_detail": "정리: ① 출처 — 저용량 클렌부테롤 독성 증례·문헌고찰(PMC10324766). ② 용도 — 베타-2 작용제, 동물용/일부 천식약이나 보디빌더·다이어터가 지방분해·근보존 목적 남용. ③ 독성 — 저용량에서도 빈맥·저칼륨혈증·심방세동·심근허혈·불안·발한. ④ 통계 — NSW 독극물정보센터 2004~2012 노출 63건, 2008년 3건→2012년 27건으로 급증, 84%가 입원 필요(주 사유 보디빌딩·체중감량). ⑤ 치료 — 특이적 해독제·역전제 없음, 지지요법(수액·칼륨 보정·베타차단 등)만. NOGEAR 시각: '한 알 정도야'가 통하지 않는 약이다. 심장을 채찍질해 지방을 태우는 원리이니, 채찍 맞는 건 결국 네 심장이다. 해독제가 없다는 한 문장을 기억하라.",
        "category": "research", "category_ko": "약물·중독",
        "source": "PMC Case Report & Review (PMC10324766)",
        "source_type": "journal",
        "source_url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC10324766/",
        "credibility": {
            "peer_reviewed": True, "primary_source": True, "cross_checked": True,
            "cross_check_date": CC_DATE, "url_alive": True, "cross_confirmed": True,
            "confidence": "medium",
            "notes": "검색결과 확인(미페치). 저용량 심장 독성·빈맥/저칼륨/심방세동·NSW 63건·84% 입원·해독제 부재 골자. JACC 보디빌더 클렌부테롤 증례·MedicalNewsToday와 교차. 직접 검증 전 → medium.",
            "fact_checked": False, "fact_check_date": CC_DATE, "accuracy": "partial",
        },
        "viral_signals": signals(18, 16, 16, 11, 13, 9),
        "tags": ["클렌부테롤", "심장독성", "저칼륨혈증", "다이어트약", "해독제없음"],
    },
    # 13. PMC10071723 — 노르웨이 AAS 사용 남성 단면조사 (검색 확인, 미페치)
    {
        "title": "스테로이드 쓰는데 병원엔 안 간다 — 부작용 겪고도 침묵하는 남성들",
        "title_en": "Health service engagement, side effects and concerns among men with anabolic-androgenic steroid use: a cross-sectional Norwegian study",
        "summary": "노르웨이에서 아나볼릭 스테로이드(AAS)를 쓰는 남성을 조사한 단면연구는, 다수가 부작용을 겪으면서도 의료 서비스에 거의 접촉하지 않는다는 사실을 드러냈다. 낙인·판단받는 두려움·의료진의 지식 부족 때문에 침묵하고, 그 사이 심혈관·호르몬·정신 부작용이 관리 없이 누적된다. AAS 사용을 '범죄'가 아닌 '공중보건' 문제로 다뤄야 한다는 근거다.",
        "summary_detail": "정리: ① 출처 — 노르웨이 AAS 사용 남성 단면조사(PMC10071723). ② 발견 — 사용자 상당수가 부작용을 경험하면서도 의료 접촉이 적음. ③ 장벽 — 낙인·판단 우려, 의료진의 AAS 지식 부족, 비밀유지 불안. ④ 우려 영역 — 심혈관·호르몬(성선저하)·정신건강·생식 관련 부작용. ⑤ 함의 — 처벌 중심 접근이 사용자를 음지로 밀어 위험을 키움 → 비낙인·해악감소(harm reduction) 기반 의료 필요. NOGEAR 시각: 가장 위험한 건 약 자체보다 '말 못 함'이다. 부작용을 느껴도 병원 대신 포럼에 묻는 순간, 손상은 관리되지 않고 쌓인다. 솔직함이 첫 번째 해독제다.",
        "category": "research", "category_ko": "스테로이드·공중보건",
        "source": "PMC Cross-sectional (Norway, PMC10071723)",
        "source_type": "journal",
        "source_url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10071723/",
        "credibility": {
            "peer_reviewed": True, "primary_source": True, "cross_checked": True,
            "cross_check_date": CC_DATE, "url_alive": True, "cross_confirmed": True,
            "confidence": "medium",
            "notes": "검색결과 확인(미페치). 의료 미접촉·낙인 장벽·부작용 침묵·harm reduction 필요 골자. 영국 AAS 1차진료 Delphi 합의(researchprotocols e65233)·harm reduction RCT(NCT07039539)와 방향 일치. 직접 검증 전 → medium.",
            "fact_checked": False, "fact_check_date": CC_DATE, "accuracy": "partial",
        },
        "viral_signals": signals(15, 16, 17, 12, 13, 7),
        "tags": ["스테로이드", "공중보건", "해악감소", "낙인", "노르웨이"],
    },
    # 14. FDA Law Blog — 펩타이드 컴파운딩 규제 (검색 확인, 미페치)
    {
        "title": "'펩타이드 랠리' 뒤의 진실 — 제한 풀려도 임상·품질 검증은 그대로 0",
        "title_en": "FDA's Pep(tide) Rally! What compounders and industry need to know",
        "summary": "FDA 규제 전문 로펌 블로그(FDA Law Blog)는 2026년 4월 펩타이드 카테고리2 해제를 '펩타이드 랠리'로 부르며, 업계의 열광과 달리 규제·법적 현실은 복잡하다고 짚는다. 제한 해제는 컴파운딩 약국의 제조 가능성을 열 뿐, 안전성·유효성을 입증한 임상시험이나 GMP 품질 검증을 대체하지 않는다. 7월 자문위 회의 결과에 따라 다시 뒤집힐 수도 있다.",
        "summary_detail": "정리: ① 출처 — FDA Law Blog(규제 전문 로펌, 2026.4 게시). ② 사안 — 2026년 4월 12종 펩타이드 카테고리2 해제를 둘러싼 컴파운딩 업계의 기대. ③ 핵심 경고 — 카테고리2 제외는 '제조 가능성'을 열 뿐, FDA 승인·임상 검증·GMP 품질 보증을 대체하지 않음. ④ 불확실성 — 503A 벌크 목록 정식 등재 여부는 7월 23~24 자문위(PCAC) 회의 결과에 좌우, 결과에 따라 재제한 가능. ⑤ 법적 함의 — 컴파운더는 여전히 처방·적응증·표시 규정 준수 필요. NOGEAR 시각: 인플루언서는 '랠리'라 외치지만 변호사는 '아직 아무것도 승인 안 됐다'고 적는다. 규제 완화 ≠ 안전 입증. 텔레그램 갈색 병은 이 모든 절차 바깥에 있다.",
        "category": "news", "category_ko": "펩타이드·규제",
        "source": "FDA Law Blog (Hyman, Phelps & McNamara)",
        "source_type": "reference",
        "source_url": "https://www.thefdalawblog.com/2026/04/fdas-peptide-rally-what-compounders-and-industry-need-to-know-post-1-of-2/",
        "credibility": {
            "peer_reviewed": False, "primary_source": True, "cross_checked": True,
            "cross_check_date": CC_DATE, "url_alive": True, "cross_confirmed": True,
            "confidence": "medium",
            "notes": "검색결과 확인(미페치). 규제 전문 로펌 블로그. 카테고리2 해제≠승인·7월 PCAC 회의·503A 등재 미확정·재제한 가능 골자가 SSRP Institute(직접검증)·Loti Labs와 교차일치. 직접 페치 전 → medium.",
            "fact_checked": False, "fact_check_date": CC_DATE, "accuracy": "partial",
        },
        "viral_signals": signals(15, 15, 15, 18, 16, 8),
        "tags": ["펩타이드", "컴파운딩", "FDA", "규제", "BPC-157"],
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
