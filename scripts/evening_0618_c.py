#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""NOGEAR Magazine — 2026-06-18 저녁 크롤 3차 병합 (장수·멘탈·디벙킹 보강).
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
    mk({
        "title": "60세 이상 여성, 근력이 곧 생존 — 악력 상위 25%는 사망위험 35%↓",
        "title_en": "Muscle strength predicts mortality in women 63–99",
        "summary": "63~99세 여성 5,472명을 가속도계로 활동량까지 보정해 추적한 JAMA Network Open 연구에서, 악력 상위 25% 여성은 하위 25%보다 사망 위험이 35% 낮았다. 활동량 권고를 못 채운 여성에서도 근력은 독립적으로 생존과 연결됐다. '얼마나 움직이나'를 넘어 '얼마나 강한가'가 수명을 갈랐다.",
        "summary_detail": "정리: ① 대상 — 여성 5,472명(63~99세), 1주일 착용 가속도계로 활동·좌식 보정. ② 결과 — 악력 상위 25%는 하위 25% 대비 사망위험 35%↓(활동·심폐체력 보정 후에도). ③ 추가 — 의자 일어서기 시간 등 근력 검사도 사망과 연관. ④ 의미 — 활동 권고 미달자에서도 근력은 독립 보호 인자. ⑤ 출처 — JAMA Network Open(2026). NOGEAR 시각: 나이 들수록 거울이 아니라 근력이 목숨값이다 — 들 수 있는 몸이 오래 산다.",
        "category": "research",
        "source": "JAMA Network Open 2026",
        "source_url": "https://jamanetwork.com/journals/jamanetworkopen/fullarticle/2845052",
        "credibility": cred(True, True, "high", "JAMA Netw Open 5,472명. 악력 상위25% 사망 35%↓·활동 보정 골자 일치."),
        "viral_signals": sig(22, 21, 23, 16, 14, 12),
        "tags": ["근력", "악력", "여성", "사망률", "장수"],
    }),
    mk({
        "title": "하루 1분의 '폭발', 수명을 늘린다 — VILPA의 과학",
        "title_en": "1 minute of vigorous bursts a day lowers mortality (VILPA)",
        "summary": "운동을 따로 안 해도, 일상 속 짧고 강한 움직임(VILPA)만으로 사망 위험이 낮아진다는 분석이 나왔다. 하루 중앙값 1.1분, 보통 10초 이내의 '에너지 폭발' 5~6회를 한 사람이 전혀 안 한 사람보다 약 7년간 더 잘 버텼다. 빠른 오르막 걷기, 버스 잡으려 뛰기, 짐 들고 계단 오르기가 곧 운동이었다.",
        "summary_detail": "정리: ① 개념 — VILPA(일상 속 격렬 간헐 신체활동): 빠른 오르막·계단·짐 운반 등. ② 용량 — 하루 중앙값 1.1분, 10초 내외 폭발 5~6회. ③ 결과 — 약 7년 추적서 무(無) 대비 사망 위험↓. ④ 함의 — 헬스장 없이도 '강도'를 일상에 끼워 넣으면 이득. ⑤ 출처 — ScienceDaily(2026-04). NOGEAR 시각: 시간 없다는 핑계의 반박 — 하루 1분의 진심이 수명을 산다.",
        "category": "research",
        "source": "ScienceDaily — VILPA 2026",
        "source_url": "https://www.sciencedaily.com/releases/2026/04/260426012305.htm",
        "credibility": cred(True, True, "high", "VILPA 보도(2026-04). 1.1분/일·10초 폭발 5~6회·사망↓ 골자 일치."),
        "viral_signals": sig(22, 18, 24, 17, 13, 12),
        "tags": ["VILPA", "고강도", "수명", "일상활동", "장수"],
    }),
    mk({
        "title": "같은 운동만 반복? '다양성'이 더 오래 살게 한다 — 11만명 30년 추적",
        "title_en": "Variety of activity, not just more, lowers mortality",
        "summary": "하버드 공중보건대가 11만 명 이상을 30년 추적한 결과, 같은 운동을 더 많이 하기보다 여러 종류의 신체활동을 섞는 쪽이 사망 위험을 더 낮췄다. 유산소·근력·유연성·일상활동을 고루 갖춘 사람이 더 길게 버텼다. '한 우물'보다 '여러 자극'이 장수에 유리했다.",
        "summary_detail": "정리: ① 규모 — 하버드 T.H. Chan, 11만명+·30년 추적. ② 발견 — 활동의 '다양성'이 단순 '양'보다 사망 위험 추가 감소와 연관. ③ 함의 — 유산소+근력+유연성+일상 움직임의 조합이 유리. ④ 맥락 — 근력 스위트스폿·VILPA 연구와 결을 같이함. ⑤ 출처 — AMA 보도(Harvard 연구). NOGEAR 시각: 몸은 단조로움을 싫어한다 — 섞어서 움직여라, 오래 살고 싶다면.",
        "category": "research",
        "source": "American Medical Association — Harvard study",
        "source_url": "https://www.ama-assn.org/public-health/prevention-wellness/massive-study-uncovers-how-much-exercise-needed-live-longer",
        "credibility": cred(True, True, "high", "하버드 11만명 30년 AMA 보도. 활동 다양성-사망↓ 골자 일치."),
        "viral_signals": sig(19, 18, 22, 16, 14, 11),
        "tags": ["운동다양성", "수명", "하버드", "장수", "복합운동"],
    }),
    mk({
        "title": "아이들의 우울에도 운동이 듣는다 — 주 3회 초과가 최적",
        "title_en": "Exercise treats depression in children & adolescents",
        "summary": "어린이·청소년 우울증을 다룬 무작위대조시험들의 체계적 검토·메타분석은, 운동 개입이 유의한 치료 효과를 낸다고 결론지었다. 효과는 주 3회를 초과할 때 가장 컸다. 성장기 정신건강에도 '몸을 움직이는 처방'이 통한다는 근거다.",
        "summary_detail": "정리: ① 대상 — 어린이·청소년 우울 RCT 체계적 검토·메타분석. ② 결과 — 운동의 유의한 치료 효과. ③ 용량 — 주 3회 초과에서 최적 결과. ④ 함의 — 약물·상담 외 1차 보조로 운동 처방 근거. ⑤ 출처 — PMC 게재 메타분석. NOGEAR 시각: 스크린에 갇힌 세대에게 가장 필요한 처방은 운동장이다.",
        "category": "mental",
        "source": "PMC — Exercise for youth depression",
        "source_url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC12624221/",
        "credibility": cred(True, True, "high", "어린이·청소년 우울 RCT 메타분석. 유의 효과·주3회 초과 최적 골자 일치."),
        "viral_signals": sig(18, 19, 22, 15, 13, 11),
        "tags": ["어린이", "청소년", "우울증", "운동치료", "멘탈"],
    }),
    mk({
        "title": "찬물과 호흡법, 몸과 마음을 바꾼다 — 반(半)무작위 대조시험",
        "title_en": "Breathwork + cold immersion: psychophysiological effects",
        "summary": "Scientific Reports에 실린 반무작위 대조시험은 호흡법과 냉수 침수를 결합한 개입의 심리·생리 효과를 측정했다. 스트레스 반응·기분 지표에서 변화가 관찰됐다. 빔호프류 '찬물+호흡' 루틴이 유행을 넘어 통제된 실험대에 오른 사례다.",
        "summary_detail": "정리: ① 설계 — 호흡법+냉수 침수 결합 개입의 반무작위 대조시험. ② 측정 — 심리·생리(스트레스 반응·기분) 지표. ③ 결과 — 개입군에서 변화 관찰(효과·한계 병기). ④ 맥락 — 빔호프식 루틴의 과학적 검증 흐름. ⑤ 출처 — Scientific Reports(2025). NOGEAR 시각: 유행을 따르기 전에 데이터를 보라 — 찬물도 '근거 있는 도구'가 될 수 있다.",
        "category": "research",
        "source": "Scientific Reports 2025",
        "source_url": "https://www.nature.com/articles/s41598-025-29187-9",
        "credibility": cred(True, True, "medium", "Sci Rep 반무작위 시험. 호흡+냉수 침수 심리생리 효과 측정 골자 일치, 표본 한계."),
        "viral_signals": sig(18, 17, 21, 15, 14, 12),
        "tags": ["냉수침수", "호흡법", "빔호프", "스트레스", "회복"],
    }),
    mk({
        "title": "'과학이 틀렸던' 보충제 7가지 — 한때의 정설이 뒤집힌 목록",
        "title_en": "7 supplements science got wrong",
        "summary": "한때 '과학적'이라 추천됐다가 후속 연구로 평가가 뒤집힌 보충제 7가지가 정리됐다. 초기 소규모·관찰 결과가 큰 RCT에서 무너진 사례들이다. 보충제 과학은 고정된 진리가 아니라 갱신되는 과정 — 어제의 정답이 오늘의 오답이 된다.",
        "summary_detail": "정리: ① 주제 — 과거 '근거 있다'던 보충제 7종의 평가 반전. ② 패턴 — 소규모·관찰 호의적 결과가 대규모 RCT에서 약화·반박. ③ 교훈 — 보충제 근거는 갱신되는 과정, 단일 연구로 단정 금지. ④ 태도 — '최신 메타 + 인체 RCT' 기준으로 재평가. ⑤ 출처 — SuppCo Science Corner 58. NOGEAR 시각: 과학을 신앙처럼 굳히지 마라 — 의심하고, 갱신하고, 정직하게 따라가라.",
        "category": "supplement",
        "source": "SuppCo — Science Corner 58",
        "source_url": "https://supp.co/articles/science-corner-58-plot-twist-seven-supplements-science-got-wrong",
        "credibility": cred(False, False, "medium", "보충제 평가 반전 정리. 소규모→대규모 RCT 반박 패턴 골자 일치, 1차논문 아님."),
        "viral_signals": sig(20, 14, 22, 15, 18, 11),
        "tags": ["보충제", "과학갱신", "RCT", "디벙킹", "근거"],
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
