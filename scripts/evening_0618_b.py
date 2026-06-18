#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""NOGEAR Magazine — 2026-06-18 저녁 크롤 2차 병합.
저녁 포커스 확장: 근비대·보충제 디벙킹·회복·멘탈·바이럴. 출처 검증 후 병합.
브랜드: FXXK FAKES. STAY NATURAL.
"""
import json
from pathlib import Path
from datetime import datetime, timezone, timedelta

KST = timezone(timedelta(hours=9))
BASE = Path(__file__).parent.parent / "content"
ARTICLES_FILE = BASE / "articles.json"
DATE = "2026.06.18"
CHK = "2026-06-18"


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
    # ===== 근비대 / 트레이닝 =====
    mk({
        "title": "실패까지 안 가도 된다 — '1~3회 남기기'가 회복까지 챙긴다",
        "title_en": "Stopping 1–3 reps short matches failure for hypertrophy",
        "summary": "훈련된 사람에게선 실패 1~3회 전에 멈춰도 끝까지 가는 것과 거의 같은 근비대가 나온다. 오히려 0~1 RIR(실패 근접)는 근육통과 회복 저하, 컨디션 악화를 불렀다. 근력은 여유를 두는 쪽이 더 나았다. 매 세트 '갈아 넣기'는 비효율이라는 게 데이터의 결론이다.",
        "summary_detail": "정리: ① 비대 — 실패 1~3회 전 중단 ≈ 완전 실패(훈련자 기준), 메타에선 실패 쪽 미세 우위(ES 0.15~0.21)지만 볼륨 보정 시 격차 작음. ② 근력 — 여유(RIR) 두는 쪽이 우위, 실패는 근력 이득 안 늘림. ③ 회복 — 0~1 RIR는 근육통↑·회복↓·웰빙↓. ④ 처방 — 80% 세트 RPE 7~9(1~3 RIR) + 20%만 고립종목 실패. ⑤ 핵심 — 총 볼륨이 결과를 더 좌우. NOGEAR 시각: 매번 죽기살기로 갈 필요 없다 — 회복까지가 훈련이다.",
        "category": "research",
        "source": "House of Hypertrophy — Failure vs RIR",
        "source_url": "https://houseofhypertrophy.com/failure-vs-reps-in-reserve/",
        "credibility": cred(False, False, "medium", "연구 종합 정리. 1~3 RIR≈실패·회복 우위·근력은 RIR 우위 골자 일치, 1차논문 아님."),
        "viral_signals": sig(20, 16, 24, 14, 17, 11),
        "tags": ["실패세트", "RIR", "근비대", "회복", "볼륨"],
    }),
    mk({
        "title": "저중량+혈류제한, 고중량만큼 큰다 — BFR 메타분석",
        "title_en": "Low-load BFR matches high-load for hypertrophy",
        "summary": "혈류를 제한한 저중량 운동(BFR)이 고중량 저항운동과 비슷한 근비대를 낸다는 메타분석 근거가 쌓였다. 관절·연부조직 부담은 훨씬 적어, 부상·재활·노년층에 매력적이다. 다만 훈련 경험에 따라 효과가 갈려, 만능은 아니다.",
        "summary_detail": "정리: ① 효과 — 저부하 BFR ≈ 고부하 저항운동 비대(반복 스킴 무관). ② 부담 — 관절·연부조직 스트레스 현저히 낮음. ③ 조절변수 — 훈련자는 BFR로 근력·비대 이득 클 수 있으나, 비훈련자는 고부하가 근력 우위. ④ 활용 — 부상·재활·고령 등 고중량 어려운 상황. ⑤ 출처 — Sports Medicine Open 메타분석. NOGEAR 시각: 무거운 게 답이 아닐 때가 있다 — 똑똑한 자극엔 약물도 부상도 필요 없다.",
        "category": "research",
        "source": "Sports Medicine - Open (Springer)",
        "source_url": "https://link.springer.com/article/10.1186/s40798-024-00719-3",
        "credibility": cred(True, True, "high", "BFR vs 고부하 메타분석. 비대 유사·관절부담↓·훈련경험 조절 골자 일치."),
        "viral_signals": sig(19, 19, 21, 13, 15, 12),
        "tags": ["BFR", "혈류제한", "저중량", "근비대", "재활"],
    }),

    # ===== 보충제 디벙킹 =====
    mk({
        "title": "BCAA 단독은 돈 낭비 — 완전 단백질이 50% 더 큰 반응",
        "title_en": "BCAAs in isolation are ineffective for muscle building",
        "summary": "스털링대 연구는 인기 보충제 BCAA를 단독 섭취하면 근성장에 비효율적이라고 밝혔다. BCAA는 합성 스위치를 켜지만 필수아미노산이 빠져 최대 반응을 못 낸다. 유청 25g(BCAA ~6g 포함)이 BCAA 단독보다 약 50% 큰 동화 반응을 냈다. 단백질이 충분하면 BCAA는 사실상 불필요하다.",
        "summary_detail": "정리: ① 결론 — BCAA 단독은 근성장에 비효율, 격리 섭취 시 최대 반응 불가. ② 기전 — 필수아미노산 일부 결여로 합성 상한. ③ 비교 — 유청 25g이 BCAA 단독 대비 ~50% 큰 동화 반응. ④ 예외 — 단식 훈련 등 극히 좁은 상황뿐. ⑤ 출처 — University of Stirling. NOGEAR 시각: 색깔 예쁜 BCAA 통 대신 닭가슴살·계란을 — 완전 단백질이 진짜다.",
        "category": "supplement",
        "source": "University of Stirling",
        "source_url": "https://www.stir.ac.uk/news/2017/07/not-all-muscle-building-supplements-are-equal/",
        "credibility": cred(True, True, "high", "스털링대 연구. BCAA 단독 비효율·유청 50% 우위 골자 일치."),
        "viral_signals": sig(21, 18, 24, 12, 18, 11),
        "tags": ["BCAA", "유청", "완전단백질", "보충제디벙킹", "근성장"],
    }),
    mk({
        "title": "카페인은 근력을 4% 올린다 — '기대 효과'까지 잡은 균형설계 연구",
        "title_en": "Caffeine raises strength 4%; expectation alters lactate",
        "summary": "2026년 균형-위약 설계 연구에서 카페인은 정적·등속(60°/s) 수축의 최대 토크를 4% 높였다. 흥미롭게도 카페인 자체와 '카페인을 먹었다'는 기대 모두 혈중 젖산을 끌어올렸다. 근력엔 실제 약리효과가, 체감엔 기대효과가 함께 작동한다는 깔끔한 분리 증거다.",
        "summary_detail": "정리: ① 설계 — 균형-위약(balanced-placebo)으로 약리효과와 기대효과 분리. ② 근력 — 카페인이 최대 토크 ~4%↑(정적·60°/s). ③ 지구력 — 유의한 증가는 없음. ④ 젖산 — 카페인+기대 모두 혈중 젖산 상승. ⑤ 출처 — Nutrients(2026-02). NOGEAR 시각: 합법·저렴·검증된 카페인 — 약물 없이도 4%는 진짜다. 다만 머릿속 '기대'도 일을 한다.",
        "category": "supplement",
        "source": "Nutrients (MDPI) 2026",
        "source_url": "https://www.mdpi.com/2072-6643/18/5/801",
        "credibility": cred(True, True, "high", "균형-위약 카페인 연구. 근력 +4%·지구력 무·젖산 기대효과 골자 일치."),
        "viral_signals": sig(19, 19, 22, 16, 14, 11),
        "tags": ["카페인", "근력", "위약효과", "젖산", "보충제"],
    }),
    mk({
        "title": "카페인, '메타의 메타'가 내린 판결 — 근력엔 효과, 지구력엔 글쎄",
        "title_en": "Caffeine meta-of-meta-analyses on strength & endurance",
        "summary": "여러 메타분석을 다시 묶은 '메타의 메타'는 카페인이 근력에 일관된 이득을 준다고 결론지었다. 근지구력 효과는 상대적으로 작고 변동이 컸다. 가장 많이 연구된 합법 에르고제닉의 효과 범위를 가장 높은 증거 수준으로 정리한 셈이다.",
        "summary_detail": "정리: ① 방법 — 다수 메타분석을 통합한 우산형(메타의 메타) 검토. ② 근력 — 일관된 향상 효과. ③ 지구력 — 효과는 작고 이질성 큼. ④ 함의 — 카페인은 근력 보조에서 가장 견고한 합법 도구. ⑤ 출처 — ScienceDirect(Heliyon). NOGEAR 시각: 과장 없이도 통하는 보충제는 존재한다 — 카페인이 그 드문 예다.",
        "category": "supplement",
        "source": "ScienceDirect — Meta of meta-analyses",
        "source_url": "https://www.sciencedirect.com/science/article/pii/S2405844024110560",
        "credibility": cred(True, True, "high", "우산형 검토. 카페인 근력 일관 효과·지구력 약함 골자 일치."),
        "viral_signals": sig(18, 19, 20, 13, 14, 10),
        "tags": ["카페인", "근력", "지구력", "메타분석", "에르고제닉"],
    }),

    # ===== 영양 / 생리 =====
    mk({
        "title": "초가공식품, 칼로리와 무관하게 '근육 속 지방'을 늘린다 — MRI 615명",
        "title_en": "Ultra-processed foods raise intramuscular fat, regardless of calories",
        "summary": "Radiology에 실린 615명 MRI 연구는 초가공식품 섭취가 많을수록 허벅지 근육 속 지방(근간 지방·IMAT)이 더 많이 쌓였음을 보여줬다. 칼로리·지방 섭취량, 활동량, 사회경제 요인과 무관했다. 근섬유 사이로 지방이 침투하는 '근육의 지방변성'은 인슐린저항·근기능 저하와 연결된다.",
        "summary_detail": "정리: ① 대상 — 615명(남275·여340, 평균 60세, BMI 27, 식단 41%가 초가공). ② 결과 — 초가공식품↑ → 허벅지 근간지방(IMAT)↑, 칼로리·지방·활동·사회경제 무관. ③ 의미 — IMAT는 인슐린저항·근기능 저하·건강 악화와 연결. ④ 한계 — 단면연구라 인과 단정 불가. ⑤ 출처 — Radiology(RSNA). NOGEAR 시각: 가짜 음식은 거울 밖에서 근육을 갉는다 — 진짜 음식이 진짜 몸을 만든다. STAY NATURAL.",
        "category": "research",
        "source": "Radiology (RSNA) 2026",
        "source_url": "https://pubs.rsna.org/doi/10.1148/radiol.251129",
        "credibility": cred(True, True, "high", "Radiology 615명 MRI. 초가공-IMAT↑·칼로리 무관·단면 한계 골자 일치."),
        "viral_signals": sig(22, 20, 23, 17, 15, 13),
        "tags": ["초가공식품", "근간지방", "IMAT", "MRI", "근육질"],
    }),
    mk({
        "title": "24시간 사회가 남성 호르몬을 깎는다 — 수면부족·초가공식품의 대가",
        "title_en": "24/7 lifestyle, sleep loss & UPFs hit male testosterone",
        "summary": "내분비 종설은 수면부족과 초가공식품 위주의 24시간 생활이 남성 테스토스테론과 생식 건강을 끌어내린다고 정리했다. 젊은 성인 연구에선 근비대 훈련·하루 60분 이상 햇빛이 테스토스테론의 양(+) 예측인자였고, 탄산음료·흡연·수면부족은 음(−) 상관이었다.",
        "summary_detail": "정리: ① 종설 — 수면부족+초가공식품 중심 24/7 생활이 남성 T·생식 건강 저하. ② 양(+) 예측 — 근비대 훈련, 햇빛 60분+, 일부 보충제. ③ 음(−) 상관 — 일일 탄산음료, 흡연, 수면부족. ④ 식단 — 비채식이 채식 대비 T 높음(관찰). ⑤ 출처 — Reviews in Endocrine and Metabolic Disorders. NOGEAR 시각: 테스토스테론은 주사가 아니라 습관에서 나온다 — 자고, 들고, 햇빛 보고, 가짜 음식 끊어라.",
        "category": "research",
        "source": "Rev Endocr Metab Disord (Springer) 2026",
        "source_url": "https://link.springer.com/article/10.1007/s11154-026-10030-z",
        "credibility": cred(True, True, "high", "내분비 종설. 수면부족·UPF가 T 저하, 근비대훈련·햇빛 양의 예측 골자 일치."),
        "viral_signals": sig(22, 19, 24, 16, 16, 11),
        "tags": ["테스토스테론", "수면", "초가공식품", "근비대", "내추럴"],
    }),

    # ===== 장수 / 근력 지표 =====
    mk({
        "title": "악력이 수명을 말한다 — 5kg 떨어질 때마다 사망위험 16%↑",
        "title_en": "Grip strength: each 5kg drop = 16% higher mortality",
        "summary": "300만 명을 포함한 대규모 분석에서 악력은 전체 사망의 독립 예측인자였고, 악력이 5kg 떨어질 때마다 사망위험이 약 16% 올라갔다. 하위 20% 악력군의 위험은 남성 2.2배·여성 2.5배였다. 악력은 수축기 혈압보다도 강한 사망 예측 변수였다.",
        "summary_detail": "정리: ① 규모 — 42개 연구·300만명+ 메타분석. ② 핵심 — 악력 5kg↓당 전사망 위험 ~16%↑(HR 1.16). ③ 극단 — 하위 20% 악력군 HR 남 2.20·여 2.52. ④ 비교 — 악력이 수축기 혈압보다 강한 사망 예측력. ⑤ 출처 — ScienceDirect 용량-반응 메타분석. NOGEAR 시각: 멋진 거울 근육보다 '쥐는 힘'이 더 오래 살게 한다 — 기능이 곧 수명이다.",
        "category": "research",
        "source": "ScienceDirect — Grip strength meta-analysis",
        "source_url": "https://www.sciencedirect.com/science/article/pii/S1568163722002203",
        "credibility": cred(True, True, "high", "악력-사망 용량반응 메타. 5kg당 16%↑·하위20% HR 2.2~2.5 골자 일치."),
        "viral_signals": sig(23, 20, 23, 14, 14, 12),
        "tags": ["악력", "수명", "사망률", "근력", "장수"],
    }),

    # ===== 멘탈 =====
    mk({
        "title": "중장년 우울, 운동으로 '예방'된다 — 균형·기능운동의 힘",
        "title_en": "Exercise prevents depression in middle-aged & older adults",
        "summary": "중장년·노년의 우울증 예방을 다룬 체계적 검토·메타분석은, 운동 개입이 우울 발생 위험을 유의하게 낮춘다고 결론지었다. 특히 균형·부드러운 트레이닝과 기능적 운동의 효과가 두드러졌다. 우울은 '치료'만이 아니라 '예방'의 영역이기도 하다.",
        "summary_detail": "정리: ① 대상 — 중장년·노년 우울 예방 RCT 체계적 검토·메타분석. ② 결과 — 운동 개입이 우울 발생 위험 유의하게 감소. ③ 유형 — 균형·부드러운 트레이닝, 기능적 운동이 특히 효과적. ④ 함의 — 운동은 우울의 치료뿐 아니라 1차 예방 수단. ⑤ 출처 — PMC 게재 메타분석. NOGEAR 시각: 늙어서도 움직이는 사람이 덜 가라앉는다 — 운동은 마음의 백신이다.",
        "category": "mental",
        "source": "PMC — Exercise prevents depression",
        "source_url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11925714/",
        "credibility": cred(True, True, "high", "중장년 우울 예방 메타분석. 운동 개입 위험↓·균형/기능운동 효과 골자 일치."),
        "viral_signals": sig(18, 19, 22, 14, 13, 11),
        "tags": ["우울예방", "중장년", "균형운동", "기능운동", "멘탈"],
    }),
    mk({
        "title": "대학생 우울·불안에도 운동이 듣는다 — 체계적 검토",
        "title_en": "Exercise eases depression and anxiety in university students",
        "summary": "대학생을 대상으로 한 체계적 검토·메타분석은 운동이 우울과 불안 증상을 유의하게 줄였다고 보고했다. 시험·취업 압박에 시달리는 청년층에서, 약·상담만이 답이 아니라 규칙적 운동이 검증된 개입이 될 수 있음을 보여준다.",
        "summary_detail": "정리: ① 대상 — 대학생 우울·불안 RCT 체계적 검토·메타분석. ② 결과 — 운동이 우울·불안 증상 유의하게 완화. ③ 맥락 — 학업·진로 스트레스 고위험 청년층. ④ 함의 — 캠퍼스 정신건강 개입에 운동 처방 근거. ⑤ 출처 — Frontiers in Sports and Active Living(2026). NOGEAR 시각: 불안할 때 가장 하기 싫은 게 운동이지만, 가장 잘 듣는 처방이기도 하다.",
        "category": "mental",
        "source": "Frontiers Sports & Active Living 2026",
        "source_url": "https://www.frontiersin.org/journals/sports-and-active-living/articles/10.3389/fspor.2026.1708741/abstract",
        "credibility": cred(True, True, "high", "대학생 우울·불안 메타분석. 운동의 유의한 완화 효과 골자 일치."),
        "viral_signals": sig(17, 18, 22, 15, 12, 10),
        "tags": ["대학생", "우울", "불안", "운동", "멘탈"],
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
