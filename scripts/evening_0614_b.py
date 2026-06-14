#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""NOGEAR Magazine — 저녁 크롤 2026-06-14 (2차: 크레아틴/심폐/회복/멘탈/바이럴 신규 출처)"""
import importlib.util
from pathlib import Path

spec = importlib.util.spec_from_file_location("e1", Path(__file__).parent / "evening_0614.py")
e1 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(e1)
mk, s = e1.mk, e1.s

NEW = [
    # ===== 크레아틴 (영양/보충제 재평가) =====
    mk("크레아틴이 폐경기 여성의 인지·기분을 살린다 — 첫 임상의 충격",
       "Creatine HCl Eases Cognitive and Physical Menopause Symptoms",
       "갱년기·폐경기 여성 36명을 대상으로 한 첫 무작위 이중맹검 임상에서, 크레아틴 HCl이 인지·반응속도·기분을 개선했다. 하루 750mg·1500mg의 저용량으로도 효과가 나타나 여성 건강 연구의 전환점으로 평가된다.",
       "정리: ① 설계 — 갱년기·폐경기 여성 36명, 이중맹검 RCT(저용량 750/1500mg HCl, HCl+CEE, 위약, 8주). ② 결과 — 인지·반응속도·기분 개선. ③ 의의 — 폐경기 여성 대상 저용량 크레아틴 첫 임상. ④ 맥락 — 크레아틴은 근육뿐 아니라 뇌 에너지 대사에 작용. ⑤ 한계 — 소규모, 추가 검증 필요. NOGEAR 시각: 크레아틴은 '남자 헬창 보충제'라는 편견이 가장 큰 가짜다. 근거가 향하는 곳을 보라.",
       "Nutraceutical Business Review", "https://nutraceuticalbusinessreview.com/creatine-hcl-ease-cognitive-physical-menopause-symptoms",
       s(19, 18, 19, 17, 16, 12),
       ["크레아틴", "폐경기", "여성건강", "인지", "기분"],
       "NBR 보도 + JANA 게재 RCT(36명). 저용량 HCl 인지·기분 개선 골자 일치.", peer=False, primary=False),

    mk("폐경기 여성 크레아틴 임상의 원문 — 750mg 저용량의 가능성",
       "CONCRET-MENOPA: Creatine HCl and Cognition in Menopausal Women (RCT)",
       "폐경기·갱년기 여성을 대상으로 8주간 크레아틴 HCl·에틸에스터 보충이 인지·임상 지표·뇌 크레아틴 수치에 미치는 영향을 본 무작위 임상의 원 논문이다. 저용량 전략의 임상적 가능성을 처음으로 검증했다.",
       "정리: ① 대상 — 갱년기·폐경기 여성, 8주 RCT. ② 개입 — 크레아틴 HCl, 에틸에스터, 위약 비교. ③ 측정 — 인지·임상 결과·뇌 크레아틴 농도. ④ 발견 — 저용량에서도 인지·기분 개선 신호. ⑤ 함의 — 여성 전 생애 크레아틴 활용 근거 축적. NOGEAR 시각: '얼마나 많이'가 아니라 '누구에게 어떻게'. 보충제는 맞는 사람에게 맞는 양일 때 무기가 된다.",
       "PubMed / CONCRET-MENOPA", "https://pubmed.ncbi.nlm.nih.gov/40854087/",
       s(16, 19, 17, 16, 14, 10),
       ["크레아틴", "폐경기", "임상시험", "저용량", "뇌건강"],
       "PubMed 원문(CONCRET-MENOPA RCT). 폐경기 여성 인지·뇌 크레아틴 측정 골자 일치.", peer=True),

    mk("크레아틴과 노화 뇌 — 6개 중 5개 연구가 '인지 개선' 손들었다",
       "Creatine and Cognition in Aging: A Systematic Review",
       "고령자 대상 크레아틴-인지 연구를 묶은 체계적 문헌고찰에서, 6개 중 5개(83%) 연구가 긍정적 연관을 보고했다. 특히 기억·주의 영역, 질환자·여성·체중 큰 사람에게서 이점이 두드러졌다.",
       "정리: ① 범위 — 고령자 크레아틴-인지 체계적 고찰. ② 결과 — 6개 중 5개(83%) 긍정 연관. ③ 영역 — 기억·주의에서 특히. ④ 하위그룹 — 질환자·18~60세·여성·고체중에서 더 유리. ⑤ 함의 — 체중 기반 상대 용량 전략 제안. NOGEAR 시각: 근육 키우려 먹던 크레아틴이 뇌까지 챙긴다. 단, 만병통치가 아니라 '근거가 쌓이는 중'이다.",
       "Oxford / Nutrition Reviews", "https://academic.oup.com/nutritionreviews/article/84/2/333/8253584",
       s(16, 19, 17, 15, 14, 10),
       ["크레아틴", "노화", "인지", "체계적고찰", "기억"],
       "Nutrition Reviews 체계적 고찰. 6중 5개 긍정·기억/주의·하위그룹 이점 골자 일치.", peer=True),

    mk("크레아틴이 탈모를 부른다? — 단 하나의 2009년 연구가 만든 괴담",
       "Does Creatine Cause Hair Loss? Debunking the DHT Myth",
       "'크레아틴이 탈모를 유발한다'는 공포는 2009년 단일 소규모 연구에서 비롯됐다. 일시적 DHT 상승이 관찰됐을 뿐, 이후 더 크고 견고한 시험들은 직접적 탈모 연관을 찾지 못했다. 괴담은 데이터로 반박됐다.",
       "정리: ① 출처 — 2009년 소규모 연구의 일시적 DHT 상승. ② 한계 — 표본 작고 후속 재현 안 됨. ③ 후속 — 더 큰 시험들에서 직접적 탈모 연관 없음. ④ 신장 괴담 — '크레아티닌' 상승과 혼동, 건강한 성인에선 신장 손상 근거 없음. ⑤ 단서 — 기존 신질환자는 사용 자제. NOGEAR 시각: 단일 연구 하나로 공포를 사지 마라. FXXK FAKES는 가짜 뉴스에도 적용된다.",
       "Ubie / DHT 괴담 반박", "https://ubiehealth.com/doctors-note/creatine-hair-loss-myth-2026-debunk-dht-evidence-751q2",
       s(18, 16, 19, 15, 18, 11),
       ["크레아틴", "탈모괴담", "DHT", "신장", "디벙킹"],
       "Ubie 의학 해설. 2009 단일연구 기원·후속 반박·크레아티닌 혼동 골자 일치.", primary=False),

    mk("크레아틴 한 알이 밤샘의 뇌를 구한다 — 단일 고용량의 과학",
       "Single-Dose Creatine Reverses Sleep-Deprivation Cognitive Decline",
       "율리히 연구소 실험에서 크레아틴 단일 고용량(0.35g/kg)이 수면박탈로 떨어진 인지·처리속도를 일시적으로 끌어올렸다. 뇌의 인산·ATP·pH 변화를 되돌리는 기전으로, 밤샘 상태의 뇌 대사를 일부 복구했다.",
       "정리: ① 설계 — 21시간 수면박탈 중 크레아틴 0.35g/kg 단회 투여. ② 측정 — 투여 후 3·5.5·7.5시간 인지검사 + 뇌 인산대사. ③ 결과 — ATP·신경 크레아틴 상승, pH 저하 방지, 인지·처리속도 개선. ④ 기전 — 수면박탈이 만든 세포 스트레스가 크레아틴 흡수를 촉진. ⑤ 단서 — 일시적 효과, 만성 사용과 별개. NOGEAR 시각: 밤샘은 여전히 나쁘다. 다만 뇌가 위기일 때 크레아틴이 응급 연료가 될 수 있다는 것.",
       "Scientific Reports / 율리히", "https://www.nature.com/articles/s41598-024-54249-9",
       s(19, 19, 18, 15, 15, 12),
       ["크레아틴", "수면박탈", "인지", "뇌대사", "ATP"],
       "Sci Reports + 율리히 발표. 0.35g/kg 단회·인지/처리속도 개선·인산대사 변화 골자 일치.", peer=True),

    mk("저용량 크레아틴 0.2g/kg, 밤샘 인지 12% 끌어올렸다",
       "Single-Dose Creatine May Support Cognition in Sleep Deprivation",
       "후속 연구는 더 낮은 단일 용량(0.2g/kg)으로도 21시간 수면박탈 동안 인지 수행이 약 12% 개선됨을 보였다. 수면박탈이 뇌의 크레아틴 흡수를 늘리는 '세포 스트레스'가 핵심 조건이다.",
       "정리: ① 용량 — 단일 0.2g/kg(앞선 0.35g/kg보다 낮음). ② 결과 — 21시간 수면박탈 중 인지 약 12% 개선. ③ 조건 — 세포 스트레스 상태가 크레아틴 흡수를 촉진. ④ 의미 — 응급 상황(밤샘·교대근무)에서 활용 가능성. ⑤ 주의 — 수면 자체의 대체재는 아님. NOGEAR 시각: 크레아틴은 잠을 대신하지 못한다. 진짜 회복은 베개 위에서 온다.",
       "NutraIngredients", "https://www.nutraingredients.com/Article/2026/04/21/single-dose-creatine-may-support-cognition-in-sleep-deprivation-study/",
       s(17, 17, 18, 17, 15, 11),
       ["크레아틴", "저용량", "수면박탈", "인지", "교대근무"],
       "NutraIngredients 보도. 0.2g/kg 단회·인지 ~12% 개선·세포 스트레스 흡수 골자 일치.", primary=False),

    # ===== 심폐 / 장수 =====
    mk("VO2max는 수명의 가장 강력한 예측인자다 — 12만 명 코호트의 결론",
       "VO2 Max Is the Strongest Exercise Predictor of Longevity",
       "쿠퍼센터 12만 명 추적을 비롯한 대형 코호트에서 심폐체력(VO2max)과 전사망률 사이에 뚜렷한 용량-반응 관계가 확인됐다. VO2max는 운동 관련 지표 중 수명을 가장 강하게 예측한다.",
       "정리: ① 데이터 — 쿠퍼센터 등 12만 명+ 코호트. ② 발견 — VO2max ↑일수록 전사망률 ↓, 명확한 용량-반응. ③ 위상 — 운동 관련 최강의 장수 예측인자. ④ 방법 — 존2 유산소가 기반, 고강도 인터벌이 상승 가속. ⑤ 적용 — 심폐체력을 '바꿀 수 있는 활력징후'로 관리. NOGEAR 시각: 체중계보다 VO2max를 봐라. 오래 잘 사는 몸의 진짜 지표다.",
       "Health Crunch / 존2 연구", "https://healthcrunch.org/articles/2026-02-06-zone-2-training-longevity-research-update",
       s(18, 17, 18, 16, 14, 12),
       ["VO2max", "심폐체력", "장수", "존2", "코호트"],
       "Health Crunch + 쿠퍼센터 코호트. VO2max-사망률 용량반응·최강 예측인자 골자 일치.", primary=False),

    mk("존2냐 고강도냐 — 2026 결론은 '둘 다, 폴라라이즈드'",
       "Zone 2 vs HIIT in 2026: Polarized Training Wins",
       "2026 연구 합의는 명확하다. 시간이 부족하면 고강도가 효율적이고, 존2는 그 토대를 쌓는다. 엘리트가 쓰는 '폴라라이즈드(존2 다량 + 고강도 소량)' 모델이 VO2max 향상에 단독 방식보다 우월하다.",
       "정리: ① 효율 — 주 6시간 미만이면 고강도가 시간 대비 VO2max 이득 큼. ② 토대 — 존2가 모세혈관·미토콘드리아·혈장량 기반 구축. ③ 최적 — 존2 다량 + 고강도 소량의 폴라라이즈드. ④ 결과 — 단독 방식보다 VO2max 향상 우월. ⑤ 적용 — 대부분 저강도, 일부 고강도로 양극화. NOGEAR 시각: '존2가 답'도, 'HIIT가 답'도 아니다. 섞을 줄 아는 사람이 오래, 멀리 간다.",
       "keedia / 존2 리얼리티", "https://keedia.com/fitness/zone-2-cardio-research-2026-reality/",
       s(16, 16, 18, 16, 16, 11),
       ["존2", "HIIT", "폴라라이즈드", "VO2max", "심폐"],
       "keedia 종합. 시간효율 고강도·존2 토대·폴라라이즈드 우월 골자 일치.", primary=False),

    mk("악력이 혈압보다 죽음을 잘 예측한다 — 300만 명 메타분석",
       "Grip Strength Predicts Mortality Better Than Blood Pressure",
       "42개 연구·300만 명 메타분석에서 악력은 전사망률의 독립적 예측인자였고, 악력 5kg 감소마다 사망 위험이 16% 높아졌다. 악력은 수축기 혈압보다 사망을 더 잘 예측하는 단순·저비용 지표다.",
       "정리: ① 규모 — 42개 연구·300만 명+ 메타분석. ② 수치 — 악력 5kg↓당 전사망 위험비 1.16. ③ 비교 — 수축기 혈압보다 강한 예측력. ④ 범위 — 심혈관·뇌졸중·심근경색과도 역상관. ⑤ 장점 — 측정 간단·저렴한 위험 선별 도구. NOGEAR 시각: 비싼 검사보다 악력기 한 번. 근력은 건강의 가장 정직한 바이탈이다. 약 없이도 키울 수 있다.",
       "Scientific Reports / NHANES", "https://www.nature.com/articles/s41598-024-80487-y",
       s(19, 18, 18, 14, 16, 12),
       ["악력", "사망률", "근력", "바이오마커", "메타분석"],
       "Sci Reports NHANES 분석 + 메타분석. 악력 5kg↓ HR 1.16·혈압보다 강한 예측 골자 일치.", peer=True),

    # ===== 회복 / 카페인 타이밍 =====
    mk("저녁 운동 전 카페인, 경기력은 올리고 수면은 갉아먹는다",
       "Pre-Evening-Training Caffeine: Performance Up, Sleep Down",
       "오후 늦게·저녁 훈련 전 카페인 섭취가 수면에 미치는 영향을 본 메타분석이다. 카페인은 경기력을 높이지만, 늦은 시간 섭취는 잠들기·수면의 질을 분명히 해친다. 효과와 비용이 함께 온다.",
       "정리: ① 효과 — 운동 1시간 전 3~6mg/kg 카페인은 경기력 향상. ② 비용 — 늦은 시간 섭취는 수면 잠복기·질 저하. ③ 트레이드오프 — 같은 카페인이 활성↑·수면↓을 동시에. ④ 적용 — 저녁 훈련자는 용량·시점 조절 필수. ⑤ 대안 — 늦은 고강도엔 카페인 최소화. NOGEAR 시각: 회복을 갉아먹는 PR은 가짜 PR이다. 잠을 지키는 게 다음 운동을 위한 투자다.",
       "NIH PMC / 카페인·수면 메타분석", "https://pmc.ncbi.nlm.nih.gov/articles/PMC12473705/",
       s(17, 18, 18, 15, 15, 11),
       ["카페인", "수면", "경기력", "타이밍", "회복"],
       "PMC 체계적 메타분석. 늦은 카페인 경기력↑·수면 잠복기/질↓ 트레이드오프 골자 일치.", peer=True),

    mk("카페인 용량·타이밍이 수면을 정확히 얼마나 망치는가 — 100명 교차 임상",
       "Dose and Timing of Caffeine on Sleep: A Randomized Crossover Trial",
       "100mg·400mg 카페인을 취침 12·8·4시간 전에 투여한 무작위 교차 임상이다. 늦게, 많이 마실수록 수면 손상이 컸다. 카페인의 수면 영향은 '얼마나'와 '언제'의 함수임을 정량적으로 보여준다.",
       "정리: ① 설계 — 카페인 100/400mg을 취침 12/8/4시간 전 투여, 교차. ② 결과 — 늦은 시점·높은 용량일수록 수면 악화. ③ 정량 — 용량·타이밍이 수면 지표를 체계적으로 변화. ④ 실전 — 같은 한 잔도 시간대에 따라 영향 다름. ⑤ 권고 — 오후 늦은 카페인은 줄이거나 끊기. NOGEAR 시각: 커피를 끊으란 게 아니다. '언제'를 바꾸면 수면을 지키면서도 카페인을 쓸 수 있다.",
       "Oxford / SLEEP", "https://academic.oup.com/sleep/article/48/4/zsae230/7815486",
       s(16, 19, 17, 15, 14, 10),
       ["카페인", "수면", "용량타이밍", "교차임상", "커피"],
       "Oxford SLEEP RCT. 100/400mg·12/8/4시간 전·늦고 많을수록 수면 악화 골자 일치.", peer=True),

    mk("수면 부족한 선수, 카페인이 무너진 경기력을 되살린다",
       "Caffeine Restores Performance in Sleep-Restricted Athletes",
       "수면이 제한된 남자 대학 축구선수에서 카페인 보충이 무산소·유산소 수행 저하를 상당 부분 상쇄했다. 1시간 전 3~6mg/kg 카페인이 급성 수면 부족의 경기력 손실을 방어한다.",
       "정리: ① 대상 — 수면 제한 남자 대학 축구선수. ② 개입 — 운동 1시간 전 3~6mg/kg 카페인. ③ 결과 — 무산소·유산소 수행 저하를 상쇄. ④ 의미 — 급성 수면 부족 상황의 응급 카드. ⑤ 단서 — 만성 수면 부족의 해법은 아님, 수면 회복이 우선. NOGEAR 시각: 카페인은 부족한 잠의 임시 처방이지 치료가 아니다. 근본은 잠이다.",
       "Frontiers in Physiology", "https://www.frontiersin.org/journals/physiology/articles/10.3389/fphys.2025.1561695/full",
       s(16, 17, 17, 15, 14, 10),
       ["카페인", "수면부족", "경기력", "축구", "회복"],
       "Frontiers 연구. 수면제한 선수·카페인 무산소/유산소 수행 상쇄 골자 일치.", peer=True),

    # ===== 운동과학 / 근육 기억 =====
    mk("근육은 기억한다 — '근핵 영구성'이 증명한 다시 커지는 능력",
       "Muscle Memory Is Real: Myonuclear Permanence in Humans",
       "근육이 과거의 비대 상태를 '기억'한다는 근육 기억 현상이 사람에서 확인됐다. 처음 근비대 때 더해진 근핵(myonuclei)이 휴식기에도 남아, 재훈련 시 더 빠른 성장을 가능케 한다는 근핵 영구성 가설이다.",
       "정리: ① 현상 — 한 번 키운 근육은 detraining 후에도 더 빨리 회복. ② 기전 — 초기 비대 때 추가된 근핵이 영구적으로 잔존. ③ 효과 — 재훈련 시 향상된 전사 반응. ④ 단서 — 인체에서 근핵 잔존 확인, 단 재성장 이점 크기는 논쟁 중. ⑤ 함의 — 운동 공백이 곧 원점은 아니다. NOGEAR 시각: 쉬었다고 좌절 마라. 네 근육은 지난 노력을 기억한다. 다시 시작하면 더 빠르다.",
       "The Journal of Physiology / Wiley", "https://physoc.onlinelibrary.wiley.com/doi/10.1113/JP285675",
       s(19, 18, 19, 14, 15, 12),
       ["근육기억", "근핵", "재훈련", "근비대", "detraining"],
       "J Physiology 2024 인체 연구. 근핵 영구성·재훈련 전사 반응·이점 크기 논쟁 골자 일치.", peer=True),

    mk("근핵은 정말 영원한가 — 인간·동물 연구를 묶은 메타분석의 신중한 답",
       "Myonuclear Permanence in Muscle Memory: A Meta-Analysis",
       "근육 기억의 핵심인 근핵 영구성을 인간·동물 연구로 묶은 체계적 메타분석이다. 다수 연구가 근핵 잔존을 지지하나, 일부는 detraining 중 손실을 보고해 결론은 아직 신중해야 한다.",
       "정리: ① 범위 — 인간·동물 근핵 영구성 메타분석. ② 다수 — 근핵이 비훈련기에도 잔존한다는 근거. ③ 반론 — 일부 연구는 근핵 손실 보고. ④ 상태 — 증거 혼재, 단정 이르다. ⑤ 함의 — '한 번 키우면 영원'은 매력적이나 과학은 진행형. NOGEAR 시각: 과학은 단정하지 않는다. 확실한 건, 꾸준함이 만든 적응은 쉽게 사라지지 않는다는 것.",
       "NIH PMC / 근핵 메타분석", "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9530508/",
       s(16, 18, 16, 13, 16, 10),
       ["근핵", "근육기억", "메타분석", "영구성", "detraining"],
       "PMC 체계적 메타분석. 근핵 잔존 다수 지지·일부 손실 보고·결론 신중 골자 일치.", peer=True),

    # ===== 바이럴 / 트렌드 추가 =====
    mk("운동 트렌드, 거품과 본질 — 떠오르는 9가지와 사라지는 것들",
       "9 Fitness Trends to Watch in 2026 and Beyond",
       "2026 이후 주목할 운동 트렌드 9가지를 정리했다. 측정 기반 트레이닝, 회복 중심, 근력·장수 결합이 본질로 자리 잡는 한편, 자극적 단발 챌린지는 빠르게 소비되고 사라진다.",
       "정리: ① 부상 — 데이터/웨어러블 기반, 회복 중시, 근력·장수 결합, 하이브리드 카디오. ② 본질화 — 측정·개별화·지속 가능성이 핵심 축. ③ 소멸 — 자극적 단발 챌린지는 단명. ④ 공통 — 효과·근거가 트렌드 수명을 결정. ⑤ 적용 — 유행을 '근거' 필터로 거르기. NOGEAR 시각: 떴다 지는 챌린지 말고, 평생 갈 습관을 골라라. 거품은 빠지고 기본만 남는다.",
       "Hevy Coach / 트렌드", "https://hevycoach.com/fitness-trends/",
       s(15, 14, 17, 16, 14, 11),
       ["운동트렌드", "웨어러블", "회복", "근력장수", "하이브리드"],
       "Hevy Coach 트렌드 종합. 데이터/회복/근력·장수 본질화·챌린지 단명 골자 일치.", primary=False),

    mk("VO2max를 '심혈관 천장'으로 올리는 법 — 2026 트레이닝 과학",
       "VO2 Max Training in 2026: Raising Your Cardiovascular Ceiling",
       "VO2max를 개인의 '심혈관 천장'으로 보고, 이를 끌어올리는 2026 트레이닝 과학을 정리했다. 고강도 인터벌이 천장을 빠르게 올리고, 존2 볼륨이 그 천장을 떠받친다. 나이가 들수록 의도적 관리가 필요하다.",
       "정리: ① 개념 — VO2max = 개인 심혈관 능력의 천장. ② 상승 — 고강도 인터벌이 천장을 빠르게 올림. ③ 토대 — 존2 볼륨이 천장 유지·확장 지원. ④ 노화 — 40대 이후 자연 하락, 의도적 훈련 필요. ⑤ 결합 — 근력만으론 부족, 심폐를 더해야 진짜 장수. NOGEAR 시각: 근육만 키우고 심폐를 버리면 반쪽이다. 천장을 올려야 오래 잘 산다.",
       "Sports Today / VO2max", "https://sports-today.top/article/vo2-max-training-2026-science-improving-cardiovascular-ceiling",
       s(16, 15, 17, 16, 14, 11),
       ["VO2max", "고강도인터벌", "존2", "심폐천장", "노화"],
       "Sports Today 종합. VO2max 천장·HIIT 상승·존2 토대·노화 관리 골자 일치.", primary=False),

    mk("'40대 이후엔 근력만으론 부족하다' — 진짜 장수에 필요한 카디오",
       "After 40, Lifting Alone Isn't Enough: The Cardio You Actually Need",
       "40대 이후 진짜 장수를 위해선 근력만으론 부족하다는 것이 2026 합의다. VO2max·존2·고강도를 결합한 심폐 훈련을 더해야 사망률·기능 저하를 함께 막을 수 있다.",
       "정리: ① 주장 — 40대 이후 근력 단독은 장수에 불충분. ② 보완 — VO2max 중심 심폐 훈련 필수. ③ 구성 — 존2 기반 + 고강도 소량. ④ 효과 — 사망률↓ + 기능·이동성 유지. ⑤ 적용 — 주간 루틴에 카디오를 의무 편성. NOGEAR 시각: 거울 속 근육과 오래 사는 몸은 다르다. 둘 다 가지려면 심장을 단련하라.",
       "Legendary Life Podcast", "https://www.legendarylifepodcast.com/your-2026-body-blueprint-part-4-why-lifting-alone-isnt-enough-after-40-and-what-you-need-to-add-for-real-longevity/",
       s(16, 14, 18, 15, 15, 11),
       ["40대", "장수", "카디오", "근력", "VO2max"],
       "Legendary Life 종합. 40대+ 근력 단독 불충분·심폐 결합 필요 골자 일치.", primary=False),
]


def main():
    e1.NEW = NEW
    e1.merge()


if __name__ == "__main__":
    main()
