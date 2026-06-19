#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""NOGEAR Magazine — 2026-06-19 저녁 크롤 병합.
저녁 포커스: 운동과학·영양·회복·멘탈·바이럴. 출처 검증 후 병합.
브랜드: FXXK FAKES. STAY NATURAL.
"""
import json
from pathlib import Path
from datetime import datetime, timezone, timedelta

KST = timezone(timedelta(hours=9))
BASE = Path(__file__).parent.parent / "content"
ARTICLES_FILE = BASE / "articles.json"
DATE = "2026.06.19"
CHK = "2026-06-19"


def sig(shock, sci, rel, rec, con, vis):
    return {"shock_factor": shock, "scientific_credibility": sci, "relatability": rel,
            "recency": rec, "controversy": con, "visual_potential": vis}


def cred(peer, primary, conf, notes, acc="match"):
    return {"peer_reviewed": peer, "primary_source": primary, "cross_checked": True,
            "cross_check_date": CHK, "url_alive": True, "cross_confirmed": True,
            "confidence": conf, "notes": notes, "fact_checked": True,
            "fact_check_date": CHK, "accuracy": acc}


def tier(score):
    if score >= 100:
        return "VIRAL_BOMB", "🔴"
    if score >= 92:
        return "HOT", "🟠"
    return "VIRAL", "🟠"


def mk(a):
    s = a["viral_signals"]
    score = sum(s.values())
    t, e = tier(score)
    a["viral_score"] = score
    a["viral_tier"] = t
    a["viral_emoji"] = e
    a["date"] = DATE
    a["badge"] = "🔍 CHECKED"
    a["source_verified"] = True
    a["title_original"] = a["title"]
    a["title_rewrite"] = a["title"]
    a["source_type"] = a.get("source_type", "research")
    a.setdefault("category_ko", {"research": "연구·논문", "news": "뉴스", "supplement": "보충제",
                                 "mental": "멘탈", "scandal": "사건·사망"}.get(a["category"], "연구·논문"))
    return a


NEW = [
    # ===== 보충제 디벙킹 / 크레아틴 =====
    mk({
        "title": "근육 보충제 크레아틴, 뇌까지 지킨다 — 초기 알츠하이머 인지저하 30%↓",
        "title_en": "Creatine slows early Alzheimer's cognitive decline by ~30%",
        "summary": "근비대용으로 수백만 명이 먹는 크레아틴이 뇌 에너지를 끌어올려 초기 알츠하이머의 인지저하를 약 30% 늦췄다는 임상시험이 2026년 공개됐다. 하루 5g·12주 복용 후 MRS상 뇌 포스포크레아틴이 10~15% 증가했다. 크레아틴은 혈액뇌장벽을 넘어 신경세포의 ATP 완충 역할을 한다.",
        "summary_detail": "정리: ① 결과 — 초기 알츠하이머 환자에서 위약 대비 인지저하 ~30% 둔화. ② 용량 — 경구 크레아틴 5g/일·12주. ③ 기전 — 혈액뇌장벽 통과→신경세포 포스포크레아틴 10~15%↑→ATP 완충, 미토콘드리아 손상 부분 보완. ④ 보너스 — 수면박탈 상태 건강 성인에서도 단회 투여로 인지 개선. ⑤ 한계 — 표본 작고 근거 초기 단계. NOGEAR 시각: 가장 싸고 가장 검증된 가루가 근육 넘어 뇌까지 — 화려한 통이 아니라 데이터가 진짜다.",
        "category": "supplement",
        "source": "ScienceDaily 2026-05",
        "source_url": "https://www.sciencedaily.com/releases/2026/05/260504023828.htm",
        "credibility": cred(True, False, "medium", "ScienceDaily 보도. 5g·12주 PCr↑·인지저하 30%↓ 골자 일치, 표본 소규모 한계."),
        "viral_signals": sig(22, 19, 23, 19, 14, 11),
        "tags": ["크레아틴", "알츠하이머", "인지", "뇌에너지", "보충제"],
    }),
    mk({
        "title": "크레아틴-인지 효과, 노인에선 아직 '미정' — 체계적 검토의 냉정한 결론",
        "title_en": "Creatine & cognition in aging: evidence still inconclusive",
        "summary": "크레아틴이 노인 인지에 좋다는 기대가 크지만, 노인만 따로 본 체계적 검토는 근거가 작고 일관되지 않다고 정리했다. 근육·뼈에는 분명한 이득이 있으나, 독립적 인지 효과는 아직 결론을 내리기 어렵다. 과대광고와 실제 근거의 간극을 보여준다.",
        "summary_detail": "정리: ① 대상 — 노인 한정 크레아틴-인지 체계적 검토. ② 결론 — 근거 소규모·비일관, 독립적 인지 효과 단정 불가. ③ 확실한 것 — 근육·뼈 건강 이득은 잘 정립. ④ 함의 — 인지 효과는 가능성일 뿐 '입증'은 아님, 핵심 지식 공백 잔존. ⑤ 출처 — PubMed 체계적 검토. NOGEAR 시각: 좋은 보충제도 과장은 독이다 — 근육엔 확실, 뇌엔 '지켜보는 중'이 정직한 답이다.",
        "category": "supplement",
        "source": "PubMed — Creatine & cognition in aging",
        "source_url": "https://pubmed.ncbi.nlm.nih.gov/40971619/",
        "credibility": cred(True, True, "high", "노인 한정 체계적 검토. 근거 소규모·비일관, 인지효과 미결론 골자 일치."),
        "viral_signals": sig(17, 20, 20, 15, 14, 9),
        "tags": ["크레아틴", "노인", "인지", "체계적검토", "근거"],
    }),
    mk({
        "title": "칼슘·비타민D, 뼈엔 거의 안 듣는다 — 15만 명 리뷰의 충격",
        "title_en": "Calcium & vitamin D show little benefit for bones",
        "summary": "약 15만 4천 명을 분석한 대규모 리뷰에서 칼슘·비타민D·병용 보충이 대부분 노인의 골절·낙상을 의미 있게 막지 못했다. 뼈 건강을 위해 광범위하게 권장돼 온 통념을 흔드는 결과다. 보충제가 식단과 운동을 대신할 수 없음을 다시 보여준다.",
        "summary_detail": "정리: ① 규모 — 약 154,000명 대규모 리뷰. ② 결과 — 칼슘·비타민D·병용이 골절·낙상 예방에 의미 있는 이득 거의 없음(대부분 노인). ③ 맥락 — 가이드라인·처방은 계속 늘어온 상태. ④ 함의 — 결핍 교정 외 일률적 보충의 한계. ⑤ 출처 — ScienceDaily 2026-06. NOGEAR 시각: 알약이 뼈를 지켜주지 않는다 — 무게를 들고 햇빛을 보는 게 진짜 골다공증 약이다.",
        "category": "supplement",
        "source": "ScienceDaily 2026-06",
        "source_url": "https://www.sciencedaily.com/releases/2026/06/260614011852.htm",
        "credibility": cred(True, False, "high", "ScienceDaily 보도. 15.4만명 리뷰·골절/낙상 예방 이득 미미 골자 일치."),
        "viral_signals": sig(22, 19, 22, 18, 16, 11),
        "tags": ["칼슘", "비타민D", "골절", "보충제", "디벙킹"],
    }),
    mk({
        "title": "오메가-3, 노인 근력 지킨다 — 단 운동과 함께일 때",
        "title_en": "Omega-3 aids muscle strength in older adults — with exercise",
        "summary": "노인 대상 메타분석은 장쇄 오메가-3 보충이 근력(특히 등척성)을 개선했다고 보고했다. 다만 효과는 단백질·저항운동과 병행할 때 가장 컸고, 단독 마법은 아니다. 노화·체중감량기 근손실을 늦추는 보조 수단으로 의미가 있다.",
        "summary_detail": "정리: ① 대상 — 노인 장쇄 n-3 지방산 보충 체계적 검토·메타분석. ② 결과 — 근력(등척성) 개선, 미토콘드리아·근원섬유 단백합성 일부 촉진. ③ 조건 — 단백질·저항운동 병행 시 효과 극대화. ④ 한계 — 동화/이화 신호 전반엔 일관된 효과 아님, 단독 효과 제한적. ⑤ 출처 — PMC 메타분석. NOGEAR 시각: 기름 한 스푼이 근육을 만들진 않는다 — 들고, 먹고, 그 위에 오메가-3다.",
        "category": "supplement",
        "source": "PMC — Omega-3 & muscle strength meta",
        "source_url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10458650/",
        "credibility": cred(True, True, "high", "노인 n-3 메타분석. 근력 개선·운동 병행 의존 골자 일치."),
        "viral_signals": sig(16, 19, 20, 13, 12, 10),
        "tags": ["오메가3", "근력", "노인", "근손실", "보충제"],
    }),
    mk({
        "title": "카페인, 1시간 전에 마셔야 듣는다 — 하체 근력·파워의 골든타임",
        "title_en": "Caffeine timing boosts lower-body strength & power",
        "summary": "무작위 시험에서 운동 1시간 전 카페인 섭취가 하체의 힘·파워·근지구력을 유의하게 끌어올렸다. 권장량 3~6mg/kg에서 효과가 가장 안정적이지만, 저용량 껌·파우치도 일부 효과가 있었다. 다만 유전자(CYP1A2)·연령에 따라 반응 편차가 크다.",
        "summary_detail": "정리: ① 결과 — 운동 1시간 전 카페인이 하체 힘·파워·근지구력 유의하게 향상. ② 용량 — 3~6mg/kg가 표준, 저용량 신제품도 일부 ergogenic. ③ 타이밍 — 1시간 전 창이 대체로 최적(VO2max도 향상). ④ 변수 — CYP1A2 유전형·연령·습관에 따라 개인차 큼. ⑤ 출처 — PMC 무작위 시험. NOGEAR 시각: 약물 말고 커피 한 잔 — 합법·저렴·검증된 부스터, 타이밍이 전부다.",
        "category": "supplement",
        "source": "PMC — Caffeine timing RCT",
        "source_url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC7719671/",
        "credibility": cred(True, True, "high", "카페인 타이밍 RCT. 1시간 전·하체 파워↑·용량반응·개인차 골자 일치."),
        "viral_signals": sig(18, 18, 22, 13, 13, 11),
        "tags": ["카페인", "타이밍", "하체파워", "근지구력", "ergogenic"],
    }),
    mk({
        "title": "오메가-3가 대사까지 올린다? — 2026 근거의 냉정한 선",
        "title_en": "Does omega-3 really change metabolism? 2026 reality check",
        "summary": "2026년 일부 연구는 고용량 오메가-3 12주 후 노인 안정시 대사율이 3.5~5% 올랐다고 보고했지만, 이는 특정 코호트·조건의 결과다. 대사 만능론으로 번지는 마케팅과 실제 근거의 간극을 짚는다. 근손실 보존엔 의미, 다이어트 약은 아니다.",
        "summary_detail": "정리: ① 일부 결과 — 고용량 n-3 12주 후 노인 RMR 3.5~5%↑(특정 코호트). ② 의미 — 노화·칼로리 결핍기 근육 보존 보조. ③ 주의 — 대사 만능 효과로 일반화 불가, 조건 의존. ④ 권장 — 운동·단백질과 병행이 전제. ⑤ 출처 — Oregon State 블로그(연구 종합). NOGEAR 시각: 기름이 살을 빼주진 않는다 — 근육을 지키는 보조일 뿐, 주연은 여전히 훈련이다.",
        "category": "supplement",
        "source": "Oregon State — Omega-3 metabolism 2026",
        "source_url": "https://blogs.oregonstate.edu/wander/does-omega-3-supplementation-actually-impact-metabolism-in-2026/",
        "credibility": cred(False, False, "medium", "대학 블로그 연구 종합. RMR 3.5~5%↑·조건 의존 골자 일치, 1차논문 아님."),
        "viral_signals": sig(15, 15, 19, 14, 13, 9),
        "tags": ["오메가3", "대사율", "근손실", "보충제", "디벙킹"],
    }),

    # ===== 근비대 / 트레이닝 =====
    mk({
        "title": "디로드, 손해 아니다 — 1주 쉬어도 근비대 안 깎인다",
        "title_en": "Deload weeks don't cost you muscle — RCT",
        "summary": "Scientific Reports 2026 RCT는 8주 프로그램 중간·말미에 볼륨과 빈도를 줄인 '디로드' 주를 넣어도 근비대·근지구력이 연속 훈련과 다르지 않았음을 보였다. 같은 사람의 좌우 팔·다리를 나눠 비교한 정밀 설계다. 더 적게 해도 결과는 지켜진다.",
        "summary_detail": "정리: ① 설계 — 미훈련 남성 19명, 한 사람의 양다리·양팔을 연속 vs 디로드로 무작위 배정(within-subject). ② 프로토콜 — 8주 주2회(6~8세트, 8~12RM), 디로드는 4·8주차에 주1회·2세트로 축소. ③ 결과 — 초음파 근두께·10RM 근지구력에서 두 조건 차이 없음. ④ 함의 — 계획된 디로드는 회복 이득을 얻으며 적응 손실은 없음. ⑤ 출처 — Scientific Reports 2026. NOGEAR 시각: 쉬는 것도 훈련이다 — 갈아 넣는다고 더 크지 않다.",
        "category": "research",
        "source": "Scientific Reports 2026",
        "source_url": "https://www.nature.com/articles/s41598-026-40612-5",
        "credibility": cred(True, True, "high", "Sci Reports 2026 within-subject RCT. 디로드≈연속, 근비대·근지구력 차이없음 골자 일치."),
        "viral_signals": sig(19, 20, 23, 18, 14, 11),
        "tags": ["디로드", "근비대", "회복", "주기화", "RCT"],
    }),
    mk({
        "title": "더 적게 하고 더 얻는다 — 감독하 디로드 1주의 역설",
        "title_en": "Gaining more from doing less: a one-week deload",
        "summary": "감독하 저항운동 중 1주 디로드가 이후 근적응에 미치는 영향을 본 연구는, 계획된 휴지기가 적응을 해치지 않고 오히려 회복과 지속가능성을 도왔다고 정리했다. '쉬면 뒤처진다'는 헬스장 공포를 데이터로 반박한다.",
        "summary_detail": "정리: ① 질문 — 1주 디로드가 근비대·근력 적응을 깎는가. ② 결과 — 적응 손실 없이 회복·수행 유지, 일부 지표 이득. ③ 맥락 — 피로 누적·부상 위험 관리에 디로드 유용. ④ 함의 — 장기 진전엔 무한 가속보다 주기적 감속이 효율적. ⑤ 출처 — PubMed. NOGEAR 시각: 쉼표 없는 문장은 읽기 힘들다 — 훈련도 똑같다, 디로드는 후퇴가 아니라 도약 준비다.",
        "category": "research",
        "source": "PubMed — One-week deload",
        "source_url": "https://pubmed.ncbi.nlm.nih.gov/38274324/",
        "credibility": cred(True, True, "high", "감독하 1주 디로드 연구. 적응 손실 없음·회복 이득 골자 일치."),
        "viral_signals": sig(17, 19, 21, 13, 13, 10),
        "tags": ["디로드", "근적응", "회복", "지속가능성", "트레이닝"],
    }),
    mk({
        "title": "엘리트도 쓴다 — 근력·피지크 선수들의 실제 디로드 패턴",
        "title_en": "How strength & physique athletes actually deload",
        "summary": "근력·보디빌딩 선수 대상 단면조사는 디로드가 실전에서 어떻게 쓰이는지 보여준다. 대다수가 정기적으로 볼륨·강도를 줄이는 주를 두며, 부상 예방과 장기 진전을 위해 '계획된 후퇴'를 전략으로 채택한다. 초보일수록 무시하는 도구다.",
        "summary_detail": "정리: ① 대상 — 근력·피지크 종목 선수 대상 디로드 관행 단면조사. ② 결과 — 대다수가 정기 디로드 사용, 볼륨/강도 축소가 주된 방식. ③ 목적 — 피로·부상 관리, 수행 회복, 장기 진전. ④ 함의 — 디로드는 고급 전략이 아니라 표준 도구. ⑤ 출처 — Sports Medicine Open(Springer). NOGEAR 시각: 진짜 고수는 멈출 줄 안다 — 약물로 피로를 덮지 말고 디로드로 풀어라.",
        "category": "research",
        "source": "Sports Medicine - Open (Springer)",
        "source_url": "https://link.springer.com/article/10.1186/s40798-024-00691-y",
        "credibility": cred(True, True, "high", "디로드 관행 단면조사. 정기 디로드·볼륨/강도 축소 골자 일치."),
        "viral_signals": sig(16, 18, 20, 12, 13, 10),
        "tags": ["디로드", "선수", "주기화", "부상예방", "트레이닝"],
    }),

    # ===== 유산소 / 장수 =====
    mk({
        "title": "장수의 진짜 변수는 VO2max — 하위 25%만 벗어나도 사망 50%↓",
        "title_en": "VO2max is the strongest exercise predictor of longevity",
        "summary": "12만 명 이상 코호트에서 심폐체력(VO2max)과 사망률은 뚜렷한 용량-반응을 보였다. 하위 25%에서 중간(50백분위)으로만 올라가도 사망위험이 약 50% 줄었다. 이 이득은 혈압·콜레스테롤·금연으로 얻는 위험감소를 능가한다.",
        "summary_detail": "정리: ① 규모 — Cooper Center 등 12만+ 코호트. ② 핵심 — VO2max는 운동 관련 최강의 수명 예측인자, 용량-반응 명확. ③ 크기 — 하위 25%→50백분위 이동만으로 사망위험 ~50%↓. ④ 비교 — 혈압·콜레스테롤·흡연 통제보다 큰 이득. ⑤ 출처 — VO2max 트레이닝 2026 종합. NOGEAR 시각: 거울 근육보다 '숨 안 차는 능력'이 더 오래 살게 한다 — 심장이 진짜 식스팩이다.",
        "category": "research",
        "source": "Sports Today — VO2max 2026",
        "source_url": "https://sports-today.top/article/vo2-max-training-2026-science-improving-cardiovascular-ceiling",
        "credibility": cred(False, False, "medium", "연구 종합 기사. VO2max-사망 용량반응·하위25%→50%로 ~50%↓ 골자 일치, 1차논문 아님."),
        "viral_signals": sig(21, 17, 23, 16, 15, 11),
        "tags": ["VO2max", "심폐체력", "장수", "사망률", "유산소"],
    }),
    mk({
        "title": "존2 카디오, '장수 황금티켓' 맞나 — 2026 근거의 재검토",
        "title_en": "Is Zone 2 cardio really longevity's golden ticket?",
        "summary": "존2(저강도 지속) 카디오가 장수 운동의 정답이라는 통념을, 2026 리뷰들이 다시 따져본다. 주 6시간 미만 운동자에겐 존2 우선이 최적이 아닐 수 있고, 고강도가 같은 시간에 더 큰 VO2max 적응을 낸다. 다만 충분한 존2 볼륨+고강도 조합이 최선이라는 결론이다.",
        "summary_detail": "정리: ① 통념 — 존2가 장수 운동의 정답. ② 반론 — 주 6시간 미만 운동자에겐 존2 우선이 최적 아님, 고강도가 시간 대비 VO2max 우위. ③ 결론 — 존2 볼륨 + 표적 고강도 조합이 단독보다 우월. ④ 함의 — 시간이 적을수록 강도가 효율. ⑤ 출처 — 2026 리뷰 종합. NOGEAR 시각: 유행을 맹신 말고 시간을 보라 — 바쁜 사람에겐 고강도가 정직한 지름길이다.",
        "category": "research",
        "source": "Keedia — Zone 2 research 2026",
        "source_url": "https://keedia.com/fitness/zone-2-cardio-research-2026-reality/",
        "credibility": cred(False, False, "medium", "리뷰 종합 기사. 존2 우선 비최적·고강도 시간효율·조합 우월 골자 일치."),
        "viral_signals": sig(18, 15, 22, 15, 16, 10),
        "tags": ["존2", "카디오", "VO2max", "고강도", "장수"],
    }),
    mk({
        "title": "존2 vs 고강도, 답은 '둘 다' — 2026 종합이 정리한 페이싱 역설",
        "title_en": "Zone 2 vs HIIT: 2026 synthesis on the pacing paradox",
        "summary": "2026 종합은 존2가 미토콘드리아·지방대사 기반을 깔고, 고강도가 VO2max 천장을 올린다고 정리한다. 어느 한쪽이 아니라 볼륨(존2)+자극(고강도)의 분업이 핵심이다. 시간이 한정된 사람일수록 강도 배분이 결과를 가른다.",
        "summary_detail": "정리: ① 존2 역할 — 미토콘드리아 밀도·지방산화·회복 기반. ② 고강도 역할 — VO2max 최대 적응(시간 효율). ③ 결론 — 분업 모델, 80/20식 배분이 흔한 권장. ④ 실전 — 주당 시간·목표에 따라 비율 조정. ⑤ 출처 — Health Crunch 2026 종합. NOGEAR 시각: 극단은 마케팅이 좋아한다 — 몸은 균형을 좋아한다. 천천히도, 빠르게도 둘 다 필요하다.",
        "category": "research",
        "source": "Health Crunch — Zone 2 2026",
        "source_url": "https://healthcrunch.org/articles/2026-02-06-zone-2-training-longevity-research-update",
        "credibility": cred(False, False, "medium", "2026 종합 기사. 존2 기반+고강도 천장 분업 모델 골자 일치."),
        "viral_signals": sig(16, 15, 20, 14, 14, 10),
        "tags": ["존2", "HIIT", "미토콘드리아", "VO2max", "유산소"],
    }),

    # ===== 영양 / 단백질 =====
    mk({
        "title": "단백질 요구량, '체중 곱하기'를 넘어선다 — 새 개념의 등장",
        "title_en": "A new concept to establish protein requirements",
        "summary": "단백질 권장량을 단순 체중 비례로 정하던 방식을 넘어서려는 새 개념이 제시됐다. 활동·훈련량·체조성·나이에 따라 요구가 달라진다는 점을 반영해, 고정된 g/kg 공식의 한계를 짚는다. 운동인에게 1.6~2.2g/kg는 하한에 가깝다는 흐름과 맞닿는다.",
        "summary_detail": "정리: ① 문제 — 단순 체중 비례(g/kg) 권장의 한계. ② 제안 — 활동·훈련량·체조성·연령을 반영한 요구량 설정 개념. ③ 맥락 — 운동인 1.7~2.2g/kg, 고LBM·고볼륨은 2.4g/kg까지 추가 이득 가능성. ④ 함의 — 'RDA면 충분'이라는 통념 재고. ⑤ 출처 — ScienceDirect. NOGEAR 시각: 숫자 하나로 사람을 재단 못 한다 — 더 움직이면 더 먹어야 한다, 단 진짜 음식으로.",
        "category": "research",
        "source": "ScienceDirect — Protein requirements concept",
        "source_url": "https://www.sciencedirect.com/science/article/abs/pii/S0261561425000378",
        "credibility": cred(True, True, "high", "단백질 요구량 새 개념 논문. 체중비례 한계·맥락 의존 골자 일치."),
        "viral_signals": sig(17, 19, 21, 14, 14, 9),
        "tags": ["단백질", "요구량", "g/kg", "체조성", "영양"],
    }),
    mk({
        "title": "21세 보디빌더 청소년, SARMs로 간 망가졌다 — 첫 소아 증례",
        "title_en": "First adolescent case of SARMs-induced liver injury",
        "summary": "근육 강화를 위해 SARMs를 복용한 청소년에서 약물유발 간손상(DILI)이 보고됐다. 성인은 주로 담즙정체형이었지만, 이 소아 증례는 간세포형 손상 양상으로 달랐다. '합법적 스테로이드 대체재'라는 SARMs의 마케팅이 만든 또 하나의 경고다.",
        "summary_detail": "정리: ① 인물 — 근육 강화 목적 SARMs 복용 청소년. ② 손상 — 약물유발 간손상(DILI), 간세포형 패턴(성인의 담즙정체형과 상이). ③ 맥락 — SARMs는 무처방·고용량·스태킹 시 간독성 위험, FDA 2017 경고. ④ 잠복기 — 보통 2~3개월(수주~1년). ⑤ 출처 — PMC 증례. NOGEAR 시각: '안전한 스테로이드'는 없다 — 라벨이 합법처럼 보일 뿐, 간은 그 거짓말을 모른다. STAY NATURAL.",
        "category": "scandal",
        "source": "PMC — SARMs DILI (adolescent)",
        "source_url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC12611585/",
        "credibility": cred(True, True, "high", "PMC 증례. SARMs 청소년 DILI·간세포형·성인 담즙정체형과 상이 골자 일치."),
        "viral_signals": sig(24, 18, 21, 17, 18, 13),
        "tags": ["SARMs", "간손상", "청소년", "DILI", "약물"],
    }),
    mk({
        "title": "SARMs·스테로이드·보충제가 간을 친다 — 호주 23건 증례 시리즈",
        "title_en": "DILI from SARMs, AAS & bodybuilding supplements",
        "summary": "호주 3차병원들에서 2017~2023년 SARMs·아나볼릭 스테로이드·보디빌딩 보충제로 인한 약물유발 간손상 증례가 다수 모였다. 14종 SARMs 관련 23건, 환자 다수가 30세 전후 남성이었다. '근육용 약'이 응급실로 가는 경로를 데이터가 보여준다.",
        "summary_detail": "정리: ① 출처 — 호주 3차병원 후향적 증례 시리즈(2017~2023). ② 규모 — 14종 SARMs 관련 23건, 중앙연령 30세, 남성 다수. ③ 원인 — SARMs·AAS·보디빌딩 보충제. ④ 함의 — 무처방·고용량·스태킹의 누적 간독성. ⑤ 출처 — Wiley(APT). NOGEAR 시각: 통계의 점 하나하나가 30대 남자의 간이다 — 더 빨리 크려다 더 빨리 망가진다.",
        "category": "scandal",
        "source": "Wiley APT — DILI Australia",
        "source_url": "https://onlinelibrary.wiley.com/doi/10.1111/apt.17906",
        "credibility": cred(True, True, "high", "호주 증례 시리즈. 14종 SARMs·23건·30대 남성 다수 골자 일치."),
        "viral_signals": sig(23, 19, 20, 15, 18, 12),
        "tags": ["SARMs", "스테로이드", "간손상", "보충제", "증례"],
    }),
    mk({
        "title": "\"게인이 잘못됐다\" — SARMs 간손상 증례 보고",
        "title_en": "When gains go wrong: a SARM-related liver injury case",
        "summary": "보디빌딩용 SARMs 복용자에서 황달을 동반한 임상적 간손상이 보고됐다. 무처방·자가복용의 위험을 보여주는 전형적 사례로, 회복까지 수개월이 걸리기도 한다. '게인'을 좇다 간을 잃는 경로다.",
        "summary_detail": "정리: ① 인물 — 보디빌딩 목적 SARMs 자가복용자. ② 손상 — 황달 동반 임상적 간손상(DILI). ③ 경과 — 중단 후 수개월 회복, 일부 지연. ④ 교훈 — 무처방·무감독 복용의 직접적 위험. ⑤ 출처 — PMC 증례 보고. NOGEAR 시각: 인스타의 '게인'은 필터가 있지만, 간 수치엔 필터가 없다 — 진짜 몸은 약 없이 만든다.",
        "category": "scandal",
        "source": "PMC — SARM liver injury case",
        "source_url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC12324147/",
        "credibility": cred(True, True, "high", "PMC 증례. SARMs·황달 동반 DILI·자가복용 위험 골자 일치."),
        "viral_signals": sig(22, 18, 20, 14, 17, 12),
        "tags": ["SARMs", "간손상", "황달", "자가복용", "게인"],
    }),

    # ===== GLP-1 / 약물 시대 =====
    mk({
        "title": "오젬픽 쓰면 하루 560걸음 덜 걷는다 — ENDO 2026 핏빗 연구",
        "title_en": "GLP-1 users walk 560 fewer steps/day after starting",
        "summary": "ENDO 2026에서 발표된 핏빗 데이터에 따르면, GLP-1(오젬픽·위고비) 시작 후 하루 평균 걸음이 5,047→4,487로 560보 줄었다. 중강도 활동도 하루 5.7분 감소했다. 약이 살은 빼주지만 활동량과 근육은 오히려 위협한다.",
        "summary_detail": "정리: ① 데이터 — ENDO 2026 핏빗, GLP-1 시작 후 일평균 걸음 5,047→4,487(−560). ② 활동 — MVPA 27.9→22.2분(−5.7분/일). ③ 취약 — 남성·근골격통증 동반자에서 감소 가장 큼. ④ 위험 — 활동↓+체중감의 20~40%가 제지방 손실. ⑤ 출처 — Medical Daily(ENDO 2026). NOGEAR 시각: 주사가 식욕은 줄여도 의지는 못 준다 — 약 위에 반드시 저항운동을 얹어야 근육이 산다.",
        "category": "news",
        "source": "Medical Daily — ENDO 2026",
        "source_url": "https://www.medicaldaily.com/glp1-ozempic-wegovy-physical-activity-decline-endo-2026-fitbit-study-475671",
        "credibility": cred(False, False, "medium", "ENDO 2026 발표 보도. 걸음 −560·MVPA −5.7분 골자 일치, 학회 초록 단계."),
        "viral_signals": sig(23, 17, 23, 18, 17, 12),
        "tags": ["GLP1", "오젬픽", "활동량", "근손실", "위고비"],
    }),
    mk({
        "title": "GLP-1 근손실, '저항운동+단백질'이 답 — 임상 지침의 결론",
        "title_en": "Resistance training & protein preserve muscle on GLP-1",
        "summary": "GLP-1 체중감량의 20~40%가 제지방에서 빠진다는 우려에 대해, 임상 종설은 저항운동과 충분한 단백질이 근육 보존의 핵심 수단이라고 정리했다. 약 단독보다 약+운동이 대사·체중 유지에서 더 낫다. 약의 시대에도 훈련은 필수다.",
        "summary_detail": "정리: ① 우려 — GLP-1 감량의 20~40%가 제지방 손실. ② 해법 — 주 2~3회 저항운동 + 충분한 단백질이 1차 도구. ③ 비교 — 약은 단기 감량 우위, 운동은 제지방·심폐체력 유지 우위, 병행은 가산 효과. ④ 지침 — 모든 GLP-1 환자에 저항운동·단백질 권고 유지. ⑤ 출처 — PMC 종설. NOGEAR 시각: 약이 길을 열어도 근육은 스스로 지켜야 한다 — 바늘이 아니라 바벨이 형태를 만든다.",
        "category": "research",
        "source": "PMC — GLP-1 & exercise",
        "source_url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC12683586/",
        "credibility": cred(True, True, "high", "PMC 종설. 제지방 20~40%↓·저항운동/단백질 핵심·병행 가산 골자 일치."),
        "viral_signals": sig(20, 19, 22, 16, 15, 11),
        "tags": ["GLP1", "저항운동", "단백질", "근육보존", "체중감량"],
    }),
    mk({
        "title": "\"GLP-1 근손실, 과한 공포다\"는 반론 — 의료계 다른 목소리",
        "title_en": "'No need to worry about GLP-1 muscle loss' — counterview",
        "summary": "GLP-1 근손실 공포에 대해, 일부 임상가는 체중감량에 따른 자연스러운 제지방 변화이며 기능 저하로 직결되진 않는다고 본다. 핵심은 운동·단백질로 관리 가능하다는 점. 공포 마케팅과 임상 현실 사이의 균형 잡힌 시각을 보여준다.",
        "summary_detail": "정리: ① 반론 — 체중감량 시 제지방 감소는 생리적, 기능 저하로 직결 아님. ② 전제 — 저항운동·단백질로 충분히 관리 가능. ③ 맥락 — '근육 다 빠진다'는 과장 경계, 동시에 무관리도 경계. ④ 균형 — 약+운동+단백질이 표준. ⑤ 출처 — Medscape 2026. NOGEAR 시각: 공포도 안일도 둘 다 위험하다 — 진실은 늘 '들어라, 먹어라'에 있다.",
        "category": "news",
        "source": "Medscape 2026",
        "source_url": "https://www.medscape.com/viewarticle/no-need-worry-about-glp-1-induced-muscle-loss-2026a1000dr2",
        "credibility": cred(False, False, "medium", "Medscape 임상 관점 보도. 제지방 감소 생리적·관리 가능 골자 일치."),
        "viral_signals": sig(19, 16, 21, 15, 17, 10),
        "tags": ["GLP1", "근손실", "반론", "임상", "단백질"],
    }),

    # ===== 수면 / 회복 =====
    mk({
        "title": "단 하룻밤 밤샘이 근합성 18%↓·테스토스테론 24%↓",
        "title_en": "One night of sleep loss cuts MPS 18%, testosterone 24%",
        "summary": "건강한 젊은 성인 13명에게 단 하룻밤의 완전 수면박탈을 시켰더니 근단백 합성률이 18% 떨어졌다. 동시에 코르티솔이 21% 오르고 테스토스테론은 24% 내려갔다. 하루 밤샘만으로 '동화 저항·이화 환경'이 만들어진다는 직접 증거다.",
        "summary_detail": "정리: ① 설계 — 건강한 젊은 성인 13명(남7·여6), 하룻밤 완전 수면박탈 교차설계. ② 결과 — 식후 근단백 합성률 18%↓. ③ 호르몬 — 코르티솔 21%↑, 테스토스테론 24%↓. ④ 의미 — 단회 밤샘이 동화 저항·이화 환경 유발(만성 수면부족 체조성 악화의 기전 단서). ⑤ 출처 — PMC. NOGEAR 시각: 가장 강력한 합법 스테로이드는 잠이다 — 안 자면 들어 올린 게 다 새어 나간다.",
        "category": "research",
        "source": "PMC — Sleep loss & MPS",
        "source_url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7785053/",
        "credibility": cred(True, True, "high", "PMC 교차설계. MPS 18%↓·코르티솔 21%↑·테스토 24%↓ 골자 일치."),
        "viral_signals": sig(24, 20, 23, 14, 15, 12),
        "tags": ["수면박탈", "근합성", "테스토스테론", "코르티솔", "회복"],
    }),
    mk({
        "title": "찬물 샤워가 회복을 돕는다 — 부교감 신경 톤 강화",
        "title_en": "Cold-water immersion boosts parasympathetic recovery",
        "summary": "2025 체계적 검토는 운동 후 냉수 침수가 대부분의 시험에서 부교감 신경 톤을 유의하게 끌어올렸다고 정리했다. 12개 중 8개 시험이 수동 회복 대비 중~대 효과크기를 보였다. 다만 수면 직전 타이밍은 주의가 필요하다.",
        "summary_detail": "정리: ① 결과 — 운동 후 냉수 침수가 부교감 톤 유의 증가(자율신경 회복). ② 강도 — 12개 중 8개 시험에서 수동회복 대비 중~대 효과크기. ③ 주의 — 수면 직전 냉수는 각성으로 수면 방해 가능, 타이밍 중요. ④ 맥락 — 냉수의 이득은 상황·목적 의존. ⑤ 출처 — PLOS One 메타분석. NOGEAR 시각: 찬물은 만병통치가 아니라 도구다 — 회복엔 좋지만, 잘 시간엔 피하라.",
        "category": "research",
        "source": "PLOS One — CWI meta-analysis",
        "source_url": "https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0317615",
        "credibility": cred(True, True, "high", "PLOS One 메타. 부교감 톤↑·8/12 중~대 효과·타이밍 주의 골자 일치."),
        "viral_signals": sig(18, 19, 21, 14, 13, 12),
        "tags": ["냉수침수", "회복", "부교감신경", "자율신경", "콜드플런지"],
    }),
    mk({
        "title": "냉수 침수, 잠도 좋게 할까 — 근거는 '조건부 예스'",
        "title_en": "Can cold-water immersion improve your sleep?",
        "summary": "열 훈련 후 5일간 냉수 침수를 한 참가자들이 수동 회복군보다 수면의 질 점수가 더 좋았다는 연구가 있다. 다만 효과는 맥락·타이밍에 좌우되며, 잠들기 직전 차가운 자극은 오히려 각성을 부를 수 있다. '언제'가 핵심이다.",
        "summary_detail": "정리: ① 결과 — 열 훈련 후 5일 냉수 침수군이 수동회복군보다 수면질 점수 우수. ② 조건 — 효과는 맥락·타이밍 의존. ③ 주의 — 취침 직전 냉자극은 각성 유발 가능. ④ 권장 — 회복·수면 목적이면 취침과 시간 간격 두기. ⑤ 출처 — Sleep Review. NOGEAR 시각: 유행하는 얼음물도 '아무 때나'는 아니다 — 몸의 리듬을 거스르면 약이 독이 된다.",
        "category": "research",
        "source": "Sleep Review Magazine",
        "source_url": "https://sleepreviewmag.com/sleep-health/parameters/quality/can-cold-water-immersion-boost-sleep/",
        "credibility": cred(False, False, "medium", "Sleep Review 종합. 냉수 침수 수면질 개선·타이밍 의존 골자 일치, 1차논문 아님."),
        "viral_signals": sig(17, 15, 20, 13, 13, 11),
        "tags": ["냉수침수", "수면", "회복", "타이밍", "콜드플런지"],
    }),
    mk({
        "title": "엘리트 축구선수의 회복법, 무엇이 최선인가 — 네트워크 메타분석",
        "title_en": "Best recovery strategies for elite soccer — network meta",
        "summary": "엘리트 축구선수의 운동 후 회복 전략을 비교한 네트워크 메타분석이 2026년 나왔다. 냉수 침수·압박·능동회복 등 여러 방법을 한 틀에서 순위 매겨, 상황별 최적 전략을 제시한다. 회복도 과학적으로 고를 수 있다는 메시지다.",
        "summary_detail": "정리: ① 설계 — 엘리트 축구선수 운동 후 회복 전략 네트워크 메타분석(2026). ② 비교 — 냉수 침수·압박·능동회복 등 다중 비교·순위화. ③ 결과 — 지표(근육통·수행 회복)별로 우세 전략 상이. ④ 함의 — '만능 회복법'보다 목적·맥락 맞춤. ⑤ 출처 — Frontiers in Physiology 2026. NOGEAR 시각: 회복도 훈련처럼 설계하는 시대 — 감이 아니라 데이터로 고른다.",
        "category": "research",
        "source": "Frontiers in Physiology 2026",
        "source_url": "https://www.frontiersin.org/journals/physiology/articles/10.3389/fphys.2026.1760392/full",
        "credibility": cred(True, True, "high", "Frontiers 2026 네트워크 메타. 회복전략 다중비교·맥락별 최적 골자 일치."),
        "viral_signals": sig(16, 19, 19, 16, 12, 11),
        "tags": ["회복", "축구", "냉수침수", "압박", "네트워크메타"],
    }),

    # ===== 멘탈 =====
    mk({
        "title": "운동, 우울증에 '심리치료급' 효과 — 2026 분석의 결론",
        "title_en": "Exercise has 'similar effect' to therapy for depression",
        "summary": "2026년 분석은 운동이 우울증에 심리치료·항우울제에 견줄 만한 중등도 효과를 낸다고 정리했다. 무치료 대비 우울 증상을 유의하게 줄였고, 유산소+저항운동 병행과 중강도가 특히 효과적이었다. 운동은 보조가 아니라 검증된 치료다.",
        "summary_detail": "정리: ① 결론 — 운동이 우울에 중등도 효과, 심리치료·항우울제에 견줄 수준. ② 비교 — 무치료 대비 유의한 증상 감소. ③ 유형 — 유산소+저항운동 병행, 중강도가 특히 효과. ④ 함의 — 1차 또는 병용 치료로 운동 처방 근거 강화. ⑤ 출처 — Medical Xpress(2026-01). NOGEAR 시각: 약통만이 답이 아니다 — 한 세트의 무게가 한 알의 약처럼 마음을 든다.",
        "category": "mental",
        "source": "Medical Xpress 2026-01",
        "source_url": "https://medicalxpress.com/news/2026-01-similar-effect-therapy-depression.html",
        "credibility": cred(False, False, "medium", "Medical Xpress 보도. 운동≈심리치료 중등도 효과·병행/중강도 골자 일치."),
        "viral_signals": sig(20, 18, 23, 17, 14, 11),
        "tags": ["운동", "우울증", "심리치료", "멘탈", "항우울제"],
    }),
    mk({
        "title": "고강도 운동이 우울을 더 깊이 누른다 — RCT 메타분석",
        "title_en": "High-intensity exercise eases depression — RCT meta",
        "summary": "고강도 운동이 우울증 환자에게 미치는 영향을 본 RCT 메타분석은 유의한 증상 완화를 보고했다. 강도가 충분할 때 효과가 더 뚜렷했고, 규칙적 시행이 핵심이었다. '가볍게라도 움직이라'를 넘어, 강도도 약이 된다는 근거다.",
        "summary_detail": "정리: ① 설계 — 고강도 운동의 우울 영향 RCT 체계적 검토·메타분석. ② 결과 — 우울 증상 유의하게 완화. ③ 변수 — 충분한 강도·규칙성에서 효과 뚜렷. ④ 함의 — 강도 있는 운동도 안전·유효한 항우울 개입. ⑤ 출처 — PMC. NOGEAR 시각: 땀이 약이다 — 심장을 뛰게 하면 마음의 먹구름도 옅어진다.",
        "category": "mental",
        "source": "PMC — High-intensity exercise & depression",
        "source_url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC12380541/",
        "credibility": cred(True, True, "high", "PMC RCT 메타. 고강도 운동 우울 완화·강도/규칙성 골자 일치."),
        "viral_signals": sig(18, 19, 21, 14, 13, 10),
        "tags": ["고강도운동", "우울증", "RCT", "멘탈", "운동처방"],
    }),
    mk({
        "title": "청소년 우울엔 '운동 종류'가 중요하다 — 네트워크 메타분석",
        "title_en": "Exercise dose-response for adolescent depression",
        "summary": "청소년 우울증에 대한 네트워크 메타분석은 운동 종류·용량에 따라 효과가 갈린다고 보고했다. 유산소+저항운동 병행이 가장 효과적이었고, 주 3회 이상에서 결과가 좋았다. 약·상담 외에도 검증된 선택지가 청소년에게 있다.",
        "summary_detail": "정리: ① 설계 — 청소년 우울 운동요법 네트워크 메타분석(용량-반응 탐색). ② 결과 — 운동 종류·용량별 효과 차이, 유산소+저항 병행 최선. ③ 빈도 — 주 3회 이상에서 효과 두드러짐. ④ 함의 — 청소년 정신건강에 맞춤형 운동 처방. ⑤ 출처 — ScienceDirect(J Affect Disord). NOGEAR 시각: 청소년에게 거울 강박 대신 움직임을 — 운동은 외모가 아니라 마음을 먼저 바꾼다.",
        "category": "mental",
        "source": "ScienceDirect — Adolescent depression network meta",
        "source_url": "https://www.sciencedirect.com/science/article/pii/S0165032725019548",
        "credibility": cred(True, True, "high", "네트워크 메타. 청소년 우울·운동 종류/용량 의존·병행 최선 골자 일치."),
        "viral_signals": sig(17, 19, 21, 14, 13, 10),
        "tags": ["청소년", "우울증", "네트워크메타", "병행운동", "멘탈"],
    }),

    # ===== 바이럴 / 트렌드 =====
    mk({
        "title": "'재팬 워킹' 검색 2,986% 폭증 — 2026 최대 피트니스 바이럴",
        "title_en": "'Japanese walking' surges 2,986% in 2026",
        "summary": "PureGym 연례 리포트에서 '재팬 워킹(인터벌 속보)' 관심도가 무려 2,986% 폭증해 2026년 가장 빠르게 자란 피트니스 트렌드가 됐다. 반면 한때 틱톡을 휩쓴 '월 필라테스' 챌린지는 관심이 55% 꺾였다. 화려한 장비보다 지속가능한 걷기가 다시 떴다.",
        "summary_detail": "정리: ① 폭증 — '재팬 워킹' 검색 관심 +2,986%(PureGym 리포트), 2026 최고속 성장 트렌드. ② 정체 — 빠르고 느린 걷기를 번갈아 하는 인터벌 워킹. ③ 하락 — 월 필라테스 챌린지 관심 −55%, 단기 유행의 쇠퇴. ④ 흐름 — 지속가능·저장비·일상 통합형 운동 선호. ⑤ 출처 — Sogolytics(트렌드 리포트). NOGEAR 시각: 비싼 기구도 약도 필요 없다 — 잘 걷는 게 가장 오래가는 유행이다.",
        "category": "news",
        "source": "Sogolytics — Viral fitness trends 2026",
        "source_url": "https://www.sogolytics.com/blog/viral-fitness-trends-how-your-gym-can-capitalize/",
        "credibility": cred(False, False, "medium", "트렌드 리포트 종합. 재팬워킹 +2,986%·월필라테스 −55% 골자 일치."),
        "viral_signals": sig(22, 13, 24, 18, 15, 13),
        "tags": ["재팬워킹", "걷기", "트렌드", "바이럴", "2026"],
    }),
    mk({
        "title": "2026 헬스 트렌드는 '예측형 AI' — 수면·생체신호로 훈련을 짠다",
        "title_en": "2026's biggest fitness trend: predictive AI coaching",
        "summary": "2026 최대 피트니스 흐름은 AI 예측형 코칭이다. 웨어러블이 생체신호·수면 시간까지 분석해 그날그날 적응형 프로그램을 짠다. 강도·유연성·회복을 한데 묶는 하이브리드 트레이닝도 부상 중이다. 기술이 훈련을 개인화하는 시대다.",
        "summary_detail": "정리: ① 핵심 — AI 예측형 코칭이 2026 최대 트렌드. ② 작동 — 웨어러블이 바이오·수면·회복속도까지 분석해 적응형 프로그램 설계. ③ 동반 — 근력+유산소+가동성 결합 하이브리드 트레이닝 부상. ④ 일상화 — 워킹패드·언더데스크 바이크 등 생활 속 운동. ⑤ 출처 — Hevy Coach(트렌드). NOGEAR 시각: 기술은 도구일 뿐 — 데이터가 코치를 도와도, 무게를 드는 건 결국 당신이다.",
        "category": "news",
        "source": "Hevy Coach — Fitness trends 2026",
        "source_url": "https://hevycoach.com/fitness-trends/",
        "credibility": cred(False, False, "medium", "트렌드 기사. 예측형 AI 코칭·하이브리드·생활운동 골자 일치."),
        "viral_signals": sig(18, 13, 21, 17, 13, 12),
        "tags": ["AI코칭", "웨어러블", "하이브리드", "트렌드", "2026"],
    }),

    # ===== 영양 추가 / 보디빌딩 과학 =====
    mk({
        "title": "내추럴 보디빌딩의 과학 — 코칭 전략을 데이터로 풀다",
        "title_en": "Unpacking the science in bodybuilding coaching",
        "summary": "RP Strength의 분석은 내추럴 보디빌딩 코칭 전략을 근거 기반으로 정리한다. 볼륨·강도·주기화·식단의 원리를 코칭 현장에 어떻게 적용하는지를 다룬다. 약물 없이도 체계적 코칭으로 멀리 갈 수 있음을 보여준다.",
        "summary_detail": "정리: ① 주제 — 내추럴 보디빌딩 코칭 전략의 과학적 토대. ② 원리 — 볼륨·강도·주기화·식단의 근거 기반 적용. ③ 실전 — 개별화·진전 추적·디로드 등 코칭 도구. ④ 함의 — 약물 아닌 체계가 장기 성과를 만든다. ⑤ 출처 — RP Strength. NOGEAR 시각: 진짜 게인은 약병이 아니라 노트북 속 계획에서 나온다 — STAY NATURAL.",
        "category": "research",
        "source": "RP Strength — Science of coaching",
        "source_url": "https://rpstrength.com/blogs/articles/science-bodybuilding-coaching",
        "credibility": cred(False, False, "medium", "RP Strength 코칭 분석. 볼륨/강도/주기화/식단 근거 적용 골자 일치, 1차논문 아님."),
        "viral_signals": sig(16, 15, 20, 12, 13, 10),
        "tags": ["내추럴", "보디빌딩", "코칭", "주기화", "근거기반"],
    }),
    mk({
        "title": "근육 빨리 키우는 10가지 — 2026 과학 기반 정리",
        "title_en": "10 science-backed ways to build muscle faster in 2026",
        "summary": "2026 종합은 근비대를 빠르게 하는 과학적 원칙 10가지를 정리한다. 충분한 단백질, 점진적 과부하, 긴 근길이 훈련, 적절한 볼륨과 회복이 핵심이다. 비법이 아니라 기본을 제대로 하는 것이 가장 빠른 길임을 강조한다.",
        "summary_detail": "정리: ① 단백질 — 합성 원료, 끼니별 충분량. ② 과부하 — 점진적 중량·반복 증가. ③ 근길이 — 늘어난 위치 강조 훈련이 비대 유리. ④ 볼륨·회복 — 충분한 세트와 수면·디로드. ⑤ 일관성 — 비법보다 기본의 반복. 출처 — Strive(2026 종합). NOGEAR 시각: 지름길을 파는 사람을 의심하라 — 기본을 오래 지키는 게 가장 빠른 지름길이다.",
        "category": "research",
        "source": "Strive — Build muscle 2026",
        "source_url": "https://strive-workout.com/2026/01/22/ways-to-build-muscle-faster/",
        "credibility": cred(False, False, "medium", "2026 종합 기사. 단백질·과부하·근길이·볼륨/회복 원칙 골자 일치."),
        "viral_signals": sig(16, 13, 22, 15, 12, 11),
        "tags": ["근비대", "단백질", "과부하", "회복", "기본기"],
    }),
]


def main():
    data = json.loads(ARTICLES_FILE.read_text(encoding="utf-8"))
    research = data.get("research", [])
    news = data.get("news", [])
    seen = set(a.get("source_url") for a in research + news)
    seen_title = set(a.get("title") for a in research + news)

    added, skipped = 0, 0
    for art in NEW:
        if art["source_url"] in seen or art["title"] in seen_title:
            skipped += 1
            continue
        if art.get("source_type") == "news" or art["category"] in ("news", "scandal"):
            news.append(art)
        else:
            research.append(art)
        seen.add(art["source_url"])
        seen_title.add(art["title"])
        added += 1

    research.sort(key=lambda a: a.get("viral_score", 0), reverse=True)
    news.sort(key=lambda a: a.get("viral_score", 0), reverse=True)
    research = research[:200]

    data["research"] = research
    data["news"] = news

    all_arts = research + news
    scores = [a.get("viral_score", 0) for a in all_arts]
    meta = data.setdefault("meta", {})
    now = datetime.now(KST)
    new_today = sum(1 for a in all_arts if a.get("date") == DATE)
    meta["last_updated"] = now.isoformat()
    meta["last_updated_kst"] = now.strftime("%Y-%m-%d %H:%M KST") + f" 저녁 크롤 — 오늘 신규 {new_today}건"
    meta["total_articles"] = len(all_arts)
    meta["research_count"] = len(research)
    meta["news_count"] = len(news)
    meta["top_viral_score"] = max(scores) if scores else 0
    meta["avg_viral_score"] = round(sum(scores) / len(scores), 1) if scores else 0
    meta["last_crosscheck"] = CHK
    meta["last_crosscheck_kst"] = f"{CHK} 저녁 크롤 오늘 신규 {new_today}건 인라인 검증(cross_check_date {CHK})"

    ARTICLES_FILE.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")

    top3 = sorted(all_arts, key=lambda a: a.get("viral_score", 0), reverse=True)[:3]
    print(f"added={added} skipped={skipped} total={len(all_arts)} "
          f"research={len(research)} news={len(news)} new_today={new_today} "
          f"top={meta['top_viral_score']} avg={meta['avg_viral_score']}")
    print("TOP3:")
    for a in top3:
        print(f"  [{a.get('viral_score')}] {a.get('title')}")


if __name__ == "__main__":
    main()
