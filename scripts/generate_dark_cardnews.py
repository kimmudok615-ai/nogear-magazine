#!/usr/bin/env python3
"""
NOGEAR DARK — 다크사이콜로지 계정 포맷을 레퍼런스로 한 캐러셀 생성기.

형식만 빌린다: 검은 배경 · 세리프 · 한 장 한 문장 · 번호 목록 · 반전 → 방어법.
내용은 content/editorial/factchecks.json 에서 match/확인된 수치만 쓴다.
조종자는 «사람» 이 아니라 «산업·알고리즘·성분표» 로 둔다(실명 단정 금지).

출력: cardnews/<날짜>_dark/<시리즈>/NN_*.html·png, caption.txt, meta.json
      cardnews/<날짜>_dark/profile.html·png (계정 프로필/그리드 미리보기)

사용: python3 scripts/generate_dark_cardnews.py [--date 20260924] [--no-png]
"""
import argparse
import html
import json
import os
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CARDNEWS = ROOT / "cardnews"

ACCOUNT = {
    "handle": "nogear.dark",
    "name": "몸의 다크사이드 | NOGEAR",
    "bio": [
        "당신의 몸을 조종하는 산업을 해부한다.",
        "가짜 몸 · 숨은 성분 · 되돌릴 수 없는 것들",
        "모든 숫자엔 출처가 있다. 용량·구매법은 없다.",
        "FXXK FAKES. STAY NATURAL. ↓",
    ],
    "link": "nogear magazine",
    "highlights": ["DARK TACTICS", "비가역", "성분표", "SARMs", "무대 뒤"],
}

# ── 시리즈 정의 ────────────────────────────────────────────
# slide kinds: cover · line · item · stat · end
# 문장 안 *강조* → 붉은 강조어
SERIES = [
    {
        "id": "A_dark_tactics",
        "tag": "DARK TACTICS",
        "bg": "body.jpg",
        "slides": [
            {"kind": "cover", "kicker": "DARK TACTICS · 5",
             "text": "그들은 당신의 근육이 아니라\n*불안*을 판다."},
            {"kind": "line", "text": "가짜 몸은 근육으로 설득하지 않는다.\n*심리*로 설득한다.",
             "sub": "알아차리는 순간, 기법은 힘을 잃는다."},
            {"kind": "item", "no": "01", "title": "앵커링",
             "text": "‘12주 만에’ 같은 불가능한 기준을 먼저 보여준다.\n그 뒤로 당신의 진전은 *실패*처럼 보인다."},
            {"kind": "item", "no": "02", "title": "사회적 증거",
             "text": "모두가 그 몸인 것처럼 느끼게 만든다.\n당신의 피드가 *표본*이 된다."},
            {"kind": "item", "no": "03", "title": "기원 신화",
             "text": "‘조상 식단’, ‘유전자’, ‘노력’.\n몸에 *이야기*를 붙인다."},
            {"kind": "item", "no": "04", "title": "해결책 판매",
             "text": "불안이 생긴 자리에\n*링크*가 놓인다."},
            {"kind": "item", "no": "05", "title": "다음 단계",
             "text": "보충제로 안 되면\n‘진짜 방법’이 따로 있다고 *속삭인다*."},
            {"kind": "stat", "num": "$11,000",
             "label": "‘조상 식단’으로 만들었다던 몸 —\n실제로는 월 1만 1천 달러대 스테로이드 지출",
             "src": "Yahoo Lifestyle 보도(유출 이메일 기반) · 본인 공개 인정 사례"},
            {"kind": "line", "text": "당신이 약한 게 아니다.\n*설계된 것*이다."},
            {"kind": "end", "text": "오늘 피드에서\n이 5가지를 찾아봐라.",
             "cta": "저장해라. 다음에 속기 전에."},
        ],
        "caption": [
            "그들은 당신의 근육이 아니라 불안을 판다.",
            "",
            "가짜 몸이 쓰는 5가지 다크 기법",
            "01 앵커링 · 02 사회적 증거 · 03 기원 신화 · 04 해결책 판매 · 05 다음 단계",
            "",
            "알아차리는 순간 기법은 힘을 잃는다.",
            "📌 저장해두고, 오늘 피드에서 하나씩 찾아보세요.",
            "",
            "출처: Yahoo Lifestyle(Liver King 월 $11,000 지출 보도, 유출 이메일 기반)",
        ],
        "facts": ["Liver King $11,000/월 — factchecks: partial(Yahoo 원문 확인, Netflix 출처엔 없음) → 출처를 Yahoo로 표기"],
    },
    {
        "id": "B_irreversible",
        "tag": "IRREVERSIBLE",
        "bg": "heart.jpg",
        "slides": [
            {"kind": "cover", "kicker": "THE PRICE",
             "text": "약은 끊을 수 있다.\n몸은 *되돌릴 수 없다*."},
            {"kind": "line", "text": "사이클은 몇 주.\n청구서는 *몇 년* 뒤에 온다."},
            {"kind": "stat", "num": "+12.43",
             "label": "AAS 사용 시 수축기 혈압 평균 상승(mmHg)\n이완기는 +8.09",
             "src": "PubMed PMID 39945139 메타분석"},
            {"kind": "stat", "num": "8.9×",
             "label": "스테로이드 사용자의\n심근병증 위험",
             "src": "Circulation · 덴마크 코호트(aHR 8.90)"},
            {"kind": "stat", "num": "20×",
             "label": "여성 프로 보디빌더의 급성심장사 위험\n(아마추어 대비)",
             "src": "European Heart Journal 2025 · ESC 보도자료"},
            {"kind": "line", "text": "심장은 근육이다.\n그리고 *기억*한다."},
            {"kind": "stat", "num": "10개월",
             "label": "약 없이 12주 운동으로\n되돌린 단백체 노화",
             "src": "npj Aging 2026 (PMID 41449222)"},
            {"kind": "end", "text": "몸은 빌리는 게 아니다.\n*갚을 방법*이 없다.",
             "cta": "저장. 다음 사이클 전에 다시 보기."},
        ],
        "caption": [
            "약은 끊을 수 있다. 몸은 되돌릴 수 없다.",
            "",
            "· 수축기 혈압 평균 +12.43 mmHg (PMID 39945139)",
            "· 심근병증 위험 8.9배 (Circulation, 덴마크 코호트)",
            "· 여성 프로 보디빌더 급성심장사 20배 (EHJ 2025)",
            "",
            "그리고 반대편 데이터 — 약 없이 12주 운동, 단백체 노화 10개월 역전 (npj Aging 2026)",
            "",
            "📌 저장하세요. STAY NATURAL.",
        ],
        "facts": [
            "+12.43/+8.09 mmHg — factchecks: 혈압 수치 정확 일치",
            "심근병증 aHR 8.90 — factchecks: Circulation 확인(국가는 덴마크, ‘40%’ 표현 금지)",
            "여성 프로 SCD 20배 — factchecks: ESC 보도자료 확인",
            "12주 운동 단백체 노화 10개월 — factchecks: match",
        ],
    },
    {
        "id": "C_hidden_ingredients",
        "tag": "HIDDEN LABEL",
        "bg": "pills.jpg",
        "slides": [
            {"kind": "cover", "kicker": "HIDDEN LABEL",
             "text": "당신이 산 건\n보충제가 *아니었을* 수도 있다."},
            {"kind": "stat", "num": "500+",
             "label": "의약품 성분이 섞여 나온\n보충제 수",
             "src": "FDA 적발 데이터 · Harvard Health"},
            {"kind": "line", "text": "가장 많이 걸린 곳:\n체중감량 · 근육 · *정력*.",
             "sub": "당신이 ‘효과가 빠르다’고 느꼈던 바로 그 분야."},
            {"kind": "line", "text": "성분표에 없으니\n먹는 사람은 *모른다*.",
             "sub": "이것이 가장 조용한 다크 기법이다."},
            {"kind": "item", "no": "01", "title": "방어법",
             "text": "제3자 인증 마크를 확인한다.\n라벨이 아니라 *검사*를 믿는다."},
            {"kind": "item", "no": "02", "title": "방어법",
             "text": "‘처방약급 효과’, ‘즉각 변화’.\n이 문구가 보이면 *의심*한다."},
            {"kind": "end", "text": "몸에 들어가는 건\n라벨이 아니라 *성분*이다.",
             "cta": "저장. 장바구니 담기 전에."},
        ],
        "caption": [
            "당신이 산 건 보충제가 아니었을 수도 있다.",
            "",
            "FDA가 적발한, 의약품 성분이 섞인 보충제 500개 이상.",
            "체중감량 · 보디빌딩 · 성기능 분야에 집중.",
            "",
            "방어법: 제3자 인증 확인 / ‘처방약급 효과’ 문구 경계",
            "",
            "출처: Harvard Health (FDA 데이터)",
            "📌 저장. 장바구니 담기 전에.",
        ],
        "facts": ["보충제 500개 이상 의약품 오염 — factchecks: match(Harvard Health 원문 확인)"],
    },
    {
        "id": "D_sarms_bloodwork",
        "tag": "SARMs",
        "bg": "syringe.jpg",
        "slides": [
            {"kind": "cover", "kicker": "BLOOD WORK",
             "text": "‘스테로이드보다 안전하다’.\n*혈액검사*로 확인했다."},
            {"kind": "stat", "num": "29.5→125.6",
             "label": "간수치 ALT\n(SARM 사용 전 → 후)",
             "src": "JMIR · 사용자 자가보고 1,700건+ 분석"},
            {"kind": "stat", "num": "44.5→31.1",
             "label": "좋은 콜레스테롤 HDL", "src": "JMIR"},
            {"kind": "stat", "num": "585→358",
             "label": "테스토스테론\n근육을 키우려다 호르몬이 줄었다", "src": "JMIR"},
            {"kind": "line", "text": "FDA 경고:\n간 손상 · 불임 · *정신증*.",
             "sub": "그리고 SNS에서 청소년·청년을 겨냥하고 있다."},
            {"kind": "line", "text": "‘연구용’이라는 라벨은\n*당신*을 위한 게 아니다."},
            {"kind": "end", "text": "‘안전한 약물’은\n*마케팅 용어*다.",
             "cta": "저장. 그리고 동생에게 보내라."},
        ],
        "caption": [
            "‘스테로이드보다 안전하다’ — 혈액검사로 확인했다.",
            "",
            "SARM 사용 전 → 후",
            "· ALT(간수치) 29.5 → 125.6",
            "· HDL 44.5 → 31.1",
            "· 테스토스테론 585 → 358",
            "",
            "FDA: 간 손상 · 불임 · 정신증, 청소년·청년 타깃팅 경고",
            "",
            "출처: JMIR(사용자 자가보고 분석), 미국 FDA",
            "📌 저장하고, 헬스 시작한 동생에게 보내주세요.",
        ],
        "facts": [
            "ALT/HDL/T 수치 — factchecks: JMIR match",
            "FDA SARMs 청소년 경고 — factchecks: match",
            "RAD-140 42세 황달 케이스는 JMIR에 없음(partial) → 사용 금지",
        ],
    },
    {
        "id": "E_stage_42",
        "tag": "BEHIND THE STAGE",
        "bg": "skull.jpg",
        "slides": [
            {"kind": "cover", "kicker": "BEHIND THE STAGE",
             "text": "그들의 평균 사망 나이는\n*42.2세*였다."},
            {"kind": "stat", "num": "20,286",
             "label": "보디빌더를 8년간 추적한 연구", "src": "European Heart Journal"},
            {"kind": "stat", "num": "38%",
             "label": "사망자 중\n급성심장사의 비율", "src": "European Heart Journal"},
            {"kind": "stat", "num": "5.23×",
             "label": "프로 선수의 급성심장사 위험\n(아마추어 대비)", "src": "European Heart Journal (HR 5.23)"},
            {"kind": "line", "text": "조명은 꺼진다.\n심장은 그 무게를 *기억*한다."},
            {"kind": "line", "text": "무대에 서는 걸 비난하는 게 아니다.\n무대까지 가는 *방법*을 묻는 것이다."},
            {"kind": "end", "text": "오래 가는 몸을\n*선택*한다.",
             "cta": "저장. 무대 뒤를 기억하자."},
        ],
        "caption": [
            "그들의 평균 사망 나이는 42.2세였다.",
            "",
            "보디빌더 20,286명 · 8년 추적",
            "· 사망자의 38%가 급성심장사",
            "· 프로는 아마추어보다 급성심장사 위험 5.23배",
            "",
            "무대를 비난하는 게 아니다. 무대까지 가는 방법을 묻는 것이다.",
            "",
            "출처: European Heart Journal",
            "📌 저장. STAY NATURAL.",
        ],
        "facts": ["20,286명·38%·HR 5.23·평균 42.2세 — factchecks: EHJ match (‘일반인 대비’ 아님, ‘아마추어 대비’)"],
    },
]

REELS = """# NOGEAR DARK — 릴스 카피 6종 (15~25초)

원칙: 0~2초 화면 텍스트 훅 → 본문 3문장 → 방어/출구로 끝. 수치는 factchecks.json 확인분만.

## ① 가짜 내추럴
- 0~2초 텍스트: **"그는 내추럴이라고 했다."**
- 본문: 조상 식단. 유전자. 노력. 전부 이야기였다. 보도된 진짜 재료는 월 1만 1천 달러어치 약이었다. 속은 건 당신 잘못이 아니다 — 속게 만든 게 기술이다.
- 엔딩: FXXK FAKES. 다음 편 — 가짜 몸이 쓰는 5가지 기법.
- 캡션: 당신이 비교하던 그 몸, 진짜였을까? (출처: Yahoo Lifestyle 보도)

## ② 되돌릴 수 없는 것
- 0~2초: **"끊으면 돌아온다고? 아니."**
- 본문: 혈압 평균 +12. 심근병증 위험 8.9배. 약은 몇 주, 청구서는 몇 년 뒤.
- 엔딩: 몸은 할부가 안 된다. STAY NATURAL.

## ③ 거울
- 0~2초: **"거울 속 당신은 작지 않다."**
- 본문: 매일 운동하는데도 작아 보인다면, 문제는 몸이 아니라 피드일 수 있다. 비교 대상이 가짜면 기준도 가짜다.
- 엔딩: 피드를 바꿔라. 힘들면 전문가와 이야기하자 — 그건 약한 게 아니다.

## ④ 성분표에 없는 성분
- 0~2초: **"성분표에 없는 성분."**
- 본문: FDA가 보충제 500개 이상에서 의약품 성분을 찾아냈다. 체중감량, 근육, 정력 보충제. 당신은 약을 먹고 있었을 수도 있다.
- 엔딩: 라벨 말고 인증 마크를 봐라.

## ⑤ SARMs
- 0~2초: **"‘안전한 스테로이드’라더니."**
- 본문: 사용 뒤 간수치는 4배 넘게, 테스토스테론은 40% 가까이 떨어졌다. FDA는 이 약이 SNS에서 청소년을 노린다고 경고했다.
- 엔딩: ‘안전한 약물’은 마케팅 용어다.

## ⑥ 트렌볼론
- 0~2초: **"‘내 머리가 죽이 됐다.’"** (연구 참여자 직접 인용)
- 본문: 트렌볼론 사용자 16명 인터뷰 — 극단적 공격성, 충동 조절 문제.
- 엔딩: 근육보다 먼저 바뀌는 게 있다.
- ⚠️ ‘뇌세포 손상’은 이 연구에서 측정하지 않았다 → 쓰지 않는다.

## 쓰지 않는 소재 (factchecks wrong/unclear)
- DNP ‘10명 중 1명 사망’(수치 오류) · 특정인 사망을 스테로이드 때문이라고 단정
- ‘스테로이드 청년 40% 심장병’(실제 8.9배) · 오젬픽 근력 20%(쥐 실험)
- RAD-140 42세 황달 케이스(인용 논문에 없음) · ‘운동=항우울제 동등’(→ ‘심리치료와 비슷’)
"""

GUIDE = """# NOGEAR DARK — 계정 운영 가이드

다크사이콜로지 계정은 **형식 레퍼런스**다. 내용은 NOGEAR 팩트체크 원장 기준.

## 빌린 형식
검은 배경 · 세리프 · 한 장 한 문장 · 번호 목록 · 붉은 강조어 1개 · 반전 → 방어법 → 저장 CTA

## 선 (바이럴은 되고 논란은 안 되게)
| 🟢 OK | 🟡 조심 | 🔴 금지 |
|---|---|---|
| 기전·혈액검사·부검 소견 | 실명: 본인 공개 인정 + 주요 매체 보도만 | 용량·사이클·PCT·구매 경로 |
| FDA·WADA 공식 경고 | 사망 사례: 인과 단정 금지 | ‘○○는 약쟁이’ 추측 폭로 |
| 보충제 오염 등 구조 | 회색지대(Enhanced Games·펩타이드)는 양쪽 | 사용자 조롱·체형 비하 |
| 약 없이 되는 데이터 | 정신건강 수치 → 도움 문구 동반 | 공포만 남기는 엔딩 |

조종자는 **사람이 아니라 산업·알고리즘·성분표**.

## 게시 전 체크
- [ ] 슬라이드의 모든 수치가 각 시리즈 meta.json `facts` 에 있다
- [ ] 마지막 장이 방어법/출구다
- [ ] 실명이 있으면 공개 인정 근거가 있다
- [ ] 게시는 Andy 승인 후 (승인 게이트)
"""

CSS = """
@import url('https://fonts.googleapis.com/css2?family=Noto+Serif+KR:wght@400;700;900&family=Noto+Sans+KR:wght@400;700&family=Cormorant+Garamond:ital,wght@0,600;1,500&display=swap');
*{margin:0;padding:0;box-sizing:border-box}
body{width:1080px;height:1350px;background:#050505;font-variant-numeric:lining-nums;color:#EDEAE4;font-family:'Noto Serif KR',serif;overflow:hidden;position:relative;word-break:keep-all}
.bg{position:absolute;inset:0;background-size:cover;background-position:center;filter:grayscale(100%) contrast(1.3) brightness(.55);opacity:.7}
.shade{position:absolute;inset:0;background:linear-gradient(180deg,rgba(5,5,5,.35) 0%,rgba(5,5,5,.55) 35%,rgba(5,5,5,.92) 75%,#050505 100%)}
.grain{position:absolute;inset:0;background-image:radial-gradient(rgba(255,255,255,.035) 1px,transparent 1px);background-size:3px 3px}
.frame{position:absolute;inset:40px;border:1px solid rgba(237,234,228,.12)}
.top{position:absolute;top:72px;left:88px;right:88px;display:flex;justify-content:space-between;font-family:'Cormorant Garamond',serif;font-size:26px;letter-spacing:6px;color:#8a857c}
.top .k{color:#B3121B}
.wrap{position:absolute;left:88px;right:88px;top:0;bottom:0;display:flex;flex-direction:column;justify-content:center}
em{font-style:normal;color:#C8141E}
.cover .hook{font-size:84px;font-weight:900;line-height:1.28;letter-spacing:-2px;white-space:pre-line}
.cover .rule{width:120px;height:3px;background:#C8141E;margin:0 0 48px}
.line .t{font-size:70px;font-weight:700;line-height:1.38;letter-spacing:-1.5px;white-space:pre-line}
.line .s,.item .s{margin-top:44px;font-family:'Noto Sans KR';font-size:30px;color:#8a857c;line-height:1.6}
.item .no{font-family:'Cormorant Garamond',serif;font-style:italic;font-size:220px;color:#C8141E;line-height:.9;opacity:.9}
.item .ti{font-family:'Noto Sans KR';font-weight:700;font-size:30px;letter-spacing:8px;color:#8a857c;margin:24px 0 36px}
.item .t{font-size:62px;font-weight:700;line-height:1.42;letter-spacing:-1.2px;white-space:pre-line}
.stat .n{font-family:'Cormorant Garamond',serif;font-weight:600;font-size:200px;line-height:1;color:#C8141E;letter-spacing:-4px;white-space:nowrap}
.stat .n.long{font-size:150px}
.stat .l{margin-top:48px;font-size:54px;font-weight:700;line-height:1.45;white-space:pre-line}
.stat .src{margin-top:56px;padding-top:24px;border-top:1px solid rgba(237,234,228,.15);font-family:'Noto Sans KR';font-size:24px;color:#6f6a62;letter-spacing:1px}
.end .t{font-size:78px;font-weight:900;line-height:1.35;letter-spacing:-2px;white-space:pre-line}
.end .cta{margin-top:64px;font-family:'Noto Sans KR';font-weight:700;font-size:32px;color:#EDEAE4;display:flex;align-items:center;gap:20px}
.end .cta svg{width:40px;height:40px}
.end .motto{margin-top:28px;font-family:'Cormorant Garamond',serif;font-size:30px;letter-spacing:8px;color:#B3121B}
.bottom{position:absolute;bottom:72px;left:88px;right:88px;display:flex;justify-content:space-between;font-family:'Cormorant Garamond',serif;font-size:24px;letter-spacing:5px;color:#5c5850}
.bottom .h{color:#8a857c}
"""


def fmt(text):
    """이스케이프 후 *강조* → <em>."""
    return re.sub(r"\*(.+?)\*", r"<em>\1</em>", html.escape(text))


def slide_html(series, s, idx, total, img_rel):
    kind = s["kind"]
    bg = f'<div class="bg" style="background-image:url(\'{img_rel}\')"></div>' if kind in ("cover", "end") else ""
    if kind == "cover":
        body = f'<div class="rule"></div><div class="hook">{fmt(s["text"])}</div>'
    elif kind == "line":
        body = f'<div class="t">{fmt(s["text"])}</div>' + (f'<div class="s">{fmt(s["sub"])}</div>' if s.get("sub") else "")
    elif kind == "item":
        body = (f'<div class="no">{s["no"]}</div><div class="ti">{html.escape(s["title"])}</div>'
                f'<div class="t">{fmt(s["text"])}</div>')
    elif kind == "stat":
        cls = "n long" if len(s["num"]) > 7 else "n"
        body = (f'<div class="{cls}">{html.escape(s["num"])}</div><div class="l">{fmt(s["label"])}</div>'
                f'<div class="src">SOURCE · {html.escape(s["src"])}</div>')
    else:  # end
        save = ('<svg viewBox="0 0 24 24" fill="none" stroke="#C8141E" stroke-width="2">'
                '<path d="M6 3h12v18l-6-4-6 4z"/></svg>')
        body = (f'<div class="t">{fmt(s["text"])}</div><div class="cta">{save}{html.escape(s["cta"])}</div>'
                f'<div class="motto">FXXK FAKES · STAY NATURAL</div>')
    right = "SWIPE →" if kind == "cover" else f"{idx:02d} / {total - 1:02d}"
    kicker = s.get("kicker", series["tag"])
    return f"""<!DOCTYPE html><html><head><meta charset="utf-8"><style>{CSS}</style></head>
<body class="{kind}">{bg}<div class="shade"></div><div class="grain"></div><div class="frame"></div>
<div class="top"><span class="k">{html.escape(kicker)}</span><span>NOGEAR · DARK</span></div>
<div class="wrap">{body}</div>
<div class="bottom"><span class="h">@{ACCOUNT['handle']}</span><span>{right}</span></div>
</body></html>"""


def profile_html(covers):
    tiles = "".join(f'<div class="tile" style="background-image:url(\'{c}\')"></div>' for c in covers)
    hl = "".join(f'<div class="hl"><div class="c">{html.escape(h[:1])}</div><span>{html.escape(h)}</span></div>'
                 for h in ACCOUNT["highlights"])
    bio = "<br>".join(html.escape(b) for b in ACCOUNT["bio"])
    return f"""<!DOCTYPE html><html><head><meta charset="utf-8"><style>
@import url('https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@400;700&family=Cormorant+Garamond:wght@600&display=swap');
*{{margin:0;padding:0;box-sizing:border-box}}
body{{width:1080px;background:#000;color:#f5f5f5;font-family:'Noto Sans KR',sans-serif}}
.head{{display:flex;align-items:center;gap:64px;padding:64px 48px 32px}}
.av{{width:200px;height:200px;border-radius:50%;background:#050505;border:3px solid #C8141E;display:flex;align-items:center;justify-content:center;font-family:'Cormorant Garamond';font-size:64px;letter-spacing:2px;color:#EDEAE4}}
.av b{{color:#C8141E}}
.handle{{font-size:40px;font-weight:700;margin-bottom:24px}}
.stats{{display:flex;gap:56px;font-size:28px;color:#aaa}} .stats b{{color:#fff;display:block;font-size:34px}}
.bio{{padding:0 48px 32px;font-size:28px;line-height:1.6}} .bio .nm{{font-weight:700}} .bio .ln{{color:#e0e0ff}}
.hls{{display:flex;gap:36px;padding:8px 48px 40px}}
.hl{{display:flex;flex-direction:column;align-items:center;gap:12px;font-size:20px;color:#ddd}}
.hl .c{{width:120px;height:120px;border-radius:50%;border:2px solid #333;background:#0b0b0b;display:flex;align-items:center;justify-content:center;font-family:'Cormorant Garamond';font-size:48px;color:#C8141E}}
.grid{{display:grid;grid-template-columns:repeat(3,1fr);gap:4px;border-top:1px solid #222;padding-top:4px}}
.tile{{aspect-ratio:4/5;background-size:cover;background-position:center}}
</style></head><body>
<div class="head"><div class="av"><b>N</b>D</div><div>
<div class="handle">{ACCOUNT['handle']}</div>
<div class="stats"><div><b>{len(covers)}</b>게시물</div><div><b>—</b>팔로워</div><div><b>—</b>팔로잉</div></div></div></div>
<div class="bio"><div class="nm">{html.escape(ACCOUNT['name'])}</div>{bio}<div class="ln">🔗 {html.escape(ACCOUNT['link'])}</div></div>
<div class="hls">{hl}</div>
<div class="grid">{tiles}</div>
</body></html>"""


def render(pairs, viewport_h=1350, full_page=False):
    from playwright.sync_api import sync_playwright
    with sync_playwright() as p:
        # 프록시 환경(원격 세션)에서도 웹폰트가 로드되도록 HTTPS_PROXY 를 넘긴다
        proxy = os.environ.get("HTTPS_PROXY") or os.environ.get("https_proxy")
        opts = {"proxy": {"server": proxy}} if proxy else {}
        try:
            browser = p.chromium.launch(**opts)
        except Exception:  # 번들 브라우저 버전 불일치 시 시스템 chromium
            browser = p.chromium.launch(executable_path=os.environ.get("CHROMIUM_PATH", "/opt/pw-browsers/chromium"), **opts)
        page = browser.new_page(viewport={"width": 1080, "height": viewport_h})
        if proxy:
            # 브라우저가 프록시 CA 를 못 믿는 환경: 폰트 요청만 requests(시스템 CA 사용)로 대신 받는다
            import requests

            def via_requests(route):
                r = requests.get(route.request.url, headers={"User-Agent": route.request.headers.get("user-agent", "")}, timeout=30)
                route.fulfill(status=r.status_code, body=r.content,
                              headers={"content-type": r.headers.get("content-type", ""), "access-control-allow-origin": "*"})

            page.route(re.compile(r"https://fonts\.(googleapis|gstatic)\.com/.*"), via_requests)
        for src, dst in pairs:
            page.goto(f"file://{src.resolve()}")
            page.wait_for_load_state("networkidle")
            page.evaluate("document.fonts.ready")
            page.wait_for_timeout(300)
            page.screenshot(path=str(dst), full_page=full_page)
        browser.close()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--date", default="20260924")
    ap.add_argument("--no-png", action="store_true")
    args = ap.parse_args()

    out = CARDNEWS / f"{args.date}_dark"
    out.mkdir(parents=True, exist_ok=True)
    pairs, covers = [], []

    for series in SERIES:
        d = out / series["id"]
        d.mkdir(exist_ok=True)
        # Higgsfield(GPT Image 2.5) 커버가 받아져 있으면 우선 사용, 없으면 기존 스톡 이미지
        hf = out / "higgsfield" / f"cover_{series['id'][0]}.png"
        img_rel = f"../higgsfield/{hf.name}" if hf.exists() else f"../../assets/{series['bg']}"
        total = len(series["slides"])
        names = []
        for i, s in enumerate(series["slides"]):
            name = f"{i:02d}_{s['kind']}.html"
            (d / name).write_text(slide_html(series, s, i, total, img_rel), encoding="utf-8")
            pairs.append((d / name, d / name.replace(".html", ".png")))
            names.append(name)
        covers.append(f"{series['id']}/{names[0].replace('.html', '.png')}")
        (d / "caption.txt").write_text("\n".join(series["caption"]) + "\n", encoding="utf-8")
        meta = {
            "version": "dark_v1",
            "account": "@" + ACCOUNT["handle"],
            "series": series["id"],
            "card_count": total,
            "cards": names,
            "facts": series["facts"],
            "fact_source": "content/editorial/factchecks.json",
            "publish": "승인 전 게시 금지",
        }
        (d / "meta.json").write_text(json.dumps(meta, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    (out / "reels.md").write_text(REELS, encoding="utf-8")
    (out / "README.md").write_text(GUIDE, encoding="utf-8")
    (out / "profile.html").write_text(profile_html(covers), encoding="utf-8")

    if not args.no_png:
        render(pairs)
        render([(out / "profile.html", out / "profile.png")], viewport_h=800, full_page=True)
    print(f"✅ {out.relative_to(ROOT)} — {len(SERIES)}개 시리즈 · {len(pairs)}장")


if __name__ == "__main__":
    main()
