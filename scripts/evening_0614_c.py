#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""NOGEAR Magazine — 저녁 크롤 2026-06-14 (3차: 잔여 신규 출처 보강)"""
import importlib.util
from pathlib import Path

spec = importlib.util.spec_from_file_location("e1", Path(__file__).parent / "evening_0614.py")
e1 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(e1)
mk, s = e1.mk, e1.s

NEW = [
    mk("악력 약한 사람이 더 일찍 죽는다 — 17개국 14만 명 PURE 연구",
       "Grip Strength Predicts Death and Heart Disease: The PURE Study",
       "17개국 약 14만 명을 추적한 PURE 연구에서 악력은 전사망·심혈관사망의 강력한 예측인자였다. 악력 5kg 감소마다 전사망 위험이 16% 올랐고, 수축기 혈압보다 예측력이 컸다.",
       "정리: ① 규모 — 17개국 약 14만 명 전향적 추적(PURE). ② 결과 — 악력 5kg↓당 전사망 위험 16%↑. ③ 비교 — 수축기 혈압보다 강한 예측력. ④ 범위 — 심근경색·뇌졸중과도 역상관. ⑤ 의미 — 악력은 저렴하고 강력한 건강 선별 지표. NOGEAR 시각: 비싼 검사 대신 악력기 한 번. 근력은 거짓말하지 않는 바이탈이다.",
       "The Lancet / PURE", "https://www.thelancet.com/journals/lancet/article/PIIS0140-6736(14)62000-6/abstract",
       s(18, 19, 18, 13, 15, 11),
       ["악력", "사망률", "PURE", "심혈관", "근력"],
       "Lancet PURE 전향 연구. 17개국·악력 5kg↓ 사망 16%↑·혈압보다 강한 예측 골자 일치.", peer=True),

    mk("악력에도 '사망 위험 임계선'이 있다 — 용량-반응 메타분석",
       "Handgrip Strength Thresholds for All-Cause and Cardiovascular Mortality",
       "악력과 전사망·암·심혈관 사망의 관계를 용량-반응으로 본 메타분석이다. 일정 악력 수준 아래로 떨어지면 사망 위험이 가파르게 오르는 임계 구간이 존재했다.",
       "정리: ① 접근 — 악력-사망 용량-반응 체계적 메타분석. ② 발견 — 특정 악력 임계선 아래에서 위험 급증. ③ 범위 — 전사망·암·심혈관 사망 모두 해당. ④ 의미 — 단순 '높을수록 좋다'가 아니라 '최소선 확보'가 중요. ⑤ 적용 — 임계선 이상 근력 유지를 목표로. NOGEAR 시각: 근력엔 지켜야 할 바닥선이 있다. 그 선을 지키는 건 약이 아니라 운동이다.",
       "ScienceDirect / 용량-반응 메타분석", "https://www.sciencedirect.com/science/article/pii/S1568163722002203",
       s(16, 18, 16, 13, 15, 10),
       ["악력", "임계선", "사망률", "용량반응", "근력"],
       "ScienceDirect 용량-반응 메타분석. 악력 임계선 아래 사망 위험 급증 골자 일치.", peer=True),

    mk("카페인, 1시간 전 3~6mg/kg — 국제스포츠영양학회 공식 입장",
       "ISSN Position Stand: Caffeine and Exercise Performance",
       "국제스포츠영양학회(ISSN)의 공식 입장문은 카페인의 경기력 향상 효과를 폭넓게 인정한다. 핵심 권고는 운동 약 1시간 전 체중당 3~6mg. 무산소·유산소·지구력 전반에서 효과가 일관된다.",
       "정리: ① 권위 — ISSN 공식 포지션 스탠드. ② 권고 — 운동 1시간 전 3~6mg/kg. ③ 범위 — 무산소·유산소·지구력 전반 효과. ④ 개인차 — 유전자(대사 속도)·습관화에 따라 반응 차이. ⑤ 주의 — 늦은 시간 섭취는 수면 영향. NOGEAR 시각: 카페인은 가장 검증된 합법 보충제다. 약이 아니라 커피 한 잔의 과학이다.",
       "NIH PMC / ISSN 포지션", "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7777221/",
       s(15, 19, 18, 13, 13, 10),
       ["카페인", "ISSN", "경기력", "3to6mg", "보충제"],
       "ISSN 공식 포지션 스탠드. 1시간 전 3~6mg/kg·전 영역 효과·개인차 골자 일치.", peer=True),

    mk("여성의 전 생애와 크레아틴 — 생리·임신·폐경까지 확장되는 근거",
       "Creatine in Women's Health: A Lifespan Perspective",
       "크레아틴이 여성 건강에 미치는 영향을 전 생애 관점에서 정리한 리뷰다. 근력·뼈·기분·인지 전반에서 호르몬 변동기(생리·임신·폐경)에 특히 잠재적 이점이 제시된다.",
       "정리: ① 관점 — 여성의 전 생애(가임기~폐경) 크레아틴. ② 영역 — 근력·골 건강·기분·인지. ③ 호르몬 — 변동기에 크레아틴 대사가 이점 가능성. ④ 안전 — 권장량 내 일반적으로 안전. ⑤ 함의 — '남성 보충제' 프레임 탈피. NOGEAR 시각: 크레아틴을 둘러싼 가장 큰 가짜는 '여자에겐 필요 없다'는 말이다. 근거를 보라.",
       "NIH PMC / 여성 크레아틴", "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7998865/",
       s(16, 18, 18, 13, 15, 10),
       ["크레아틴", "여성건강", "전생애", "골건강", "호르몬"],
       "PMC 리뷰. 여성 전 생애 크레아틴·근력/골/인지·호르몬 변동기 이점 골자 일치.", peer=True),

    mk("크레아틴 신화 10가지, 과학으로 박살내기 — 물살·여성·로딩의 진실",
       "10 Creatine Myths Debunked by Science",
       "크레아틴을 둘러싼 10가지 신화를 과학으로 정리했다. '물살만 찐다', '여성에겐 부적합', '로딩이 필수다' 같은 통념 대부분이 근거가 약하거나 틀렸다. 가장 많이 연구된 보충제의 진짜 모습이다.",
       "정리: ① 물살 — 초기 수분 증가는 세포 내 수화, '살'과 다름. ② 여성 — 효과·안전성 모두 입증, 부적합 근거 없음. ③ 로딩 — 필수 아님, 매일 3~5g로도 포화 도달. ④ 사이클링 — 끊었다 먹을 필요 없음. ⑤ 정체성 — 가장 연구 많고 안전한 보충제. NOGEAR 시각: 헬스장 괴담의 9할은 크레아틴에 붙어 있다. 데이터로 걸러내면 남는 건 단순한 효과다.",
       "Jinfiniti / 크레아틴 신화", "https://www.jinfiniti.com/creatine-myths/",
       s(17, 16, 19, 13, 16, 11),
       ["크레아틴", "신화", "로딩", "물살", "디벙킹"],
       "Jinfiniti 해설. 물살/여성/로딩/사이클링 통념 반박 골자, 다수 근거와 정합.", primary=False),

    mk("존2 카디오, 장수의 황금티켓인가 페이스의 함정인가",
       "Zone 2 Cardio: Longevity's Golden Ticket or a Pacing Paradox?",
       "존2 카디오를 둘러싼 과대평가와 실제를 균형 있게 짚었다. 미토콘드리아·지방 대사 토대를 쌓는 가치는 분명하나, 정확한 강도 설정이 어렵고 단독으론 VO2max 상승에 한계가 있다.",
       "정리: ① 가치 — 존2는 미토콘드리아·모세혈관·지방 산화 토대 구축. ② 함정 — '존2 강도'를 정확히 맞추기 어려움(너무 빠르거나 느림). ③ 한계 — 단독으론 VO2max 상승 제한. ④ 해법 — 고강도 세션과 결합(폴라라이즈드). ⑤ 결론 — 만능 아닌 '기반 도구'. NOGEAR 시각: 유행어에 속지 말고 원리를 봐라. 존2는 토대일 뿐, 천장은 고강도가 올린다.",
       "Our Healtho / 존2 패러독스", "https://ourhealtho.com/zone-2-cardio-in-2026-longevitys-golden-ticket-or-a-pacing-paradox/",
       s(16, 14, 17, 16, 16, 11),
       ["존2", "장수", "VO2max", "페이스", "심폐"],
       "Our Healtho 종합. 존2 토대 가치·강도 설정 함정·단독 한계 골자 일치.", primary=False),

    mk("골격근은 어떻게 '기억'하는가 — 근육 기억의 세포 메커니즘 리뷰",
       "Skeletal Muscle Memory: The Cellular Mechanisms Review",
       "골격근 기억의 세포·분자 메커니즘을 종합한 리뷰다. 근핵 축적, 후성유전적 변화(DNA 메틸화), 위성세포의 역할이 과거 훈련 상태를 '기억'하게 만드는 핵심 기전으로 제시된다.",
       "정리: ① 주제 — 골격근 기억의 세포·분자 기전 종합. ② 근핵 — 비대 때 추가된 근핵의 잔존. ③ 후성유전 — DNA 메틸화 변화가 장기 전사 조절. ④ 위성세포 — 근핵 공급원으로서의 역할. ⑤ 함의 — 훈련의 흔적은 세포 수준에 새겨진다. NOGEAR 시각: 네 몸은 과거의 훈련을 세포에 새긴다. 한 번 제대로 만든 적응은 쉽게 지워지지 않는다.",
       "AJP-Cell Physiology / 리뷰", "https://journals.physiology.org/doi/pdf/10.1152/ajpcell.00099.2023",
       s(16, 18, 16, 13, 14, 11),
       ["근육기억", "후성유전", "DNA메틸화", "위성세포", "근핵"],
       "AJP-Cell 리뷰. 근핵·DNA 메틸화·위성세포 근육 기억 기전 골자 일치.", peer=True),

    mk("체중계 너머의 3가지 활력징후 — 더 활기차고 유능한 몸의 지표",
       "Beyond the Scale: 3 Vital Signs for a More Capable Body",
       "체중 숫자에 갇히지 말라는 제안이다. 더 오래·잘 사는 몸을 위해 추적해야 할 세 지표로 심폐체력(VO2max), 근력(악력 등), 이동성/근육량이 제시된다. 체중보다 기능이 건강을 말한다.",
       "정리: ① 문제 — 체중계 숫자는 건강을 충분히 못 담는다. ② 지표1 — 심폐체력(VO2max), 수명 예측. ③ 지표2 — 근력(악력 등), 사망·기능 예측. ④ 지표3 — 근육량·이동성, 노년 자립의 핵심. ⑤ 적용 — 체중 대신 이 셋을 추적. NOGEAR 시각: 몸무게에 집착하는 순간 본질을 놓친다. 강하고 움직이는 몸이 진짜 건강이다.",
       "Trusted Senior Specialists", "https://www.trustedseniorspecialists.com/trusted-senior-specialists-blog/track-these-3-big-metrics-to-live-better-longer",
       s(16, 14, 19, 14, 14, 11),
       ["활력징후", "VO2max", "근력", "근육량", "건강지표"],
       "TSS 종합. 체중 너머 심폐·근력·근육량/이동성 3지표 추적 골자 일치.", primary=False),
]


def main():
    e1.NEW = NEW
    e1.merge()


if __name__ == "__main__":
    main()
