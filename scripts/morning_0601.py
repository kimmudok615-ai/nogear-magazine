#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""NOGEAR 아침 크롤 — 2026-06-01. 신규 기사 병합/중복제거/정렬/200 cap.
   ⚠️ 모든 URL은 2026-06-01 WebSearch 결과에서 1:1로 확인된 실제 링크만 사용.
   포커스: 펠리오시스(간), TRT붐, Enhanced Games, 위조 스테로이드 중금속,
           SARMs 간독성, 펩타이드 규제, 신장 FSGS, 라이버킹 소송."""
import json, datetime

PATH = "content/articles.json"
TODAY = "2026.06.01"
CHECK = "2026-06-01"


def sig(shock, sci, rel, rec, contr, vis):
    return {"shock_factor": shock, "scientific_credibility": sci, "relatability": rel,
            "recency": rec, "controversy": contr, "visual_potential": vis}


def cred(pr, ps, cc, conf, notes, acc, confirmed=True, alive=True):
    return {"peer_reviewed": pr, "primary_source": ps, "cross_checked": cc,
            "cross_check_date": CHECK, "url_alive": alive, "cross_confirmed": confirmed,
            "confidence": conf, "notes": notes, "fact_checked": True, "accuracy": acc}


def score(s):
    return sum(s.values())


# ============ RESEARCH ============
NEW_RESEARCH = [
    {
        "title": "스테로이드 쓰는 男 절반이 부작용 호소하면서도 병원엔 안 간다 — 노르웨이 대규모 조사",
        "title_en": "Health service engagement, side effects and concerns among men with anabolic-androgenic steroid use",
        "summary": "노르웨이 단면연구(PMC10071723)는 AAS를 쓰는 남성 다수가 여드름·고환 위축·성욕 변화·심계항진 등 부작용을 직접 보고하면서도, 낙인과 불신 탓에 의료기관을 찾지 않는다고 밝혔다. 부작용은 일상인데 치료 접근은 막혀 있다. 결국 위험은 음지에서 누적된다.",
        "summary_detail": "정리: ① 대상 — AAS를 사용하는 남성 대규모 단면조사(노르웨이). ② 자가보고 부작용 — 여드름, 고환 위축, 성욕·발기 변화, 심계항진·혈압 우려, 기분 변화. ③ 핵심 발견 — 부작용을 인지하면서도 상당수가 의료 서비스에 접근하지 않음. ④ 장벽 — 의료진의 지식 부족 우려, 낙인, 판단받을 것에 대한 두려움. ⑤ 함의 — 해악감소(harm reduction) 관점의 1차 진료 개입 필요성. NOGEAR 시각: 부작용을 느끼면서도 병원 문턱을 못 넘는다. 음지의 약은 음지의 합병증을 만든다 — 그게 설계다.",
        "category": "research", "category_ko": "역학·조사",
        "source": "PMC10071723 (Norwegian cross-sectional study)", "source_type": "journal",
        "source_url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10071723/",
        "credibility": cred(True, True, True, "high", "노르웨이 단면연구 PMC10071723. 자가보고 부작용·의료접근 회피·낙인 장벽 기술 일치.", "verified"),
        "viral_signals": sig(18, 19, 20, 14, 12, 6),
        "tags": ["AAS", "부작용", "의료접근", "노르웨이연구", "해악감소"],
    },
    {
        "title": "스테로이드가 간에 '피주머니'를 만든다 — 펠리오시스 간염, 터지면 즉사",
        "title_en": "Hepatic Peliosis and Hemorrhage after Anabolic Steroid Abuse",
        "summary": "AAS 남용은 간 실질에 혈액으로 찬 동공이 생기는 '펠리오시스 간염(peliosis hepatis)'을 유발한다. 이 낭종이 파열되면 치명적 복강 내 출혈로 즉사할 수 있다. 보디빌딩의 화학이 간을 스펀지처럼 만든다는 의학 케이스 보고가 반복적으로 쌓이고 있다.",
        "summary_detail": "정리: ① 병태 — 간 동양혈관(sinusoid) 확장으로 혈액이 고인 낭성 공간이 형성. ② 원인 — 안드로겐-아나볼릭 스테로이드 치료/남용과 강하게 연관. ③ 위험 — 낭종 파열 시 치명적 간 내·복강 내 출혈. ④ 회복성 — 약물 중단 시 부분적으로 가역적인 경우도 있으나 출혈은 응급. ⑤ 위치 — Thieme 등 동료심사 저널에 정식 케이스 등재. NOGEAR 시각: 보이지 않는 곳에서 간이 피주머니로 변한다. 무대 위 펌핑의 청구서는 수술대 위에서 날아온다.",
        "category": "research", "category_ko": "간·독성",
        "source": "Thieme / Hepatic Peliosis case (2024)", "source_type": "journal",
        "source_url": "https://www.thieme-connect.com/products/ejournals/abstract/10.1055/s-0044-1787963",
        "credibility": cred(True, True, True, "high", "Thieme 동료심사 케이스. AAS 남용 후 펠리오시스 간염·출혈 기술 일치. 파열 시 치명적 출혈 의학적 사실.", "verified"),
        "viral_signals": sig(24, 18, 16, 14, 11, 9),
        "tags": ["펠리오시스", "간출혈", "AAS", "간독성", "케이스보고"],
    },
    {
        "title": "27세 남성 간에서 25cm 종양 — 5년 스테로이드의 결과물 '간선종'",
        "title_en": "Peliosis Hepatis: A Vascular Tumor-Like Liver Lesion",
        "summary": "Annals of Internal Medicine 케이스에서, 5년간 AAS를 남용한 27세 남성이 상복부 통증으로 응급실을 찾았고 직경 25cm의 간선종(adenoma)에 펠리오시스가 동반된 것이 확인됐다. 양성 종양이지만 악성 전환·자발적 출혈·파열 위험이 높은 시한폭탄이다.",
        "summary_detail": "정리: ① 환자 — 5년 AAS 남용 이력의 27세 남성, 상복부 통증·구역으로 응급실 내원. ② 소견 — 직경 25cm 간세포선종(hepatocellular adenoma) + 펠리오시스 동반. ③ 위험 — 간선종은 악성 전환·자발적 출혈·파열 위험이 큰 양성 종양. ④ 맥락 — 안드로겐 연관 간종양(선종·간세포암)은 AAS의 잘 알려진 장기 합병증. ⑤ 출처 — ACP Annals of Internal Medicine 임상케이스. NOGEAR 시각: 25cm. 한 사람의 간 안에 자란 화학의 결정체다. 자연은 이런 종양을 청구서로 남기지 않는다.",
        "category": "research", "category_ko": "간·종양",
        "source": "Annals of Internal Medicine: Clinical Cases", "source_type": "journal",
        "source_url": "https://www.acpjournals.org/doi/10.7326/aimcc.2024.0078",
        "credibility": cred(True, True, True, "high", "ACP Annals 임상케이스. 27세·5년 AAS·25cm 간선종+펠리오시스 기술 일치.", "verified"),
        "viral_signals": sig(25, 17, 16, 13, 11, 10),
        "tags": ["간선종", "간종양", "AAS", "27세", "펠리오시스"],
    },
    {
        "title": "끊어도 또 자란다 — AAS가 만든 '재발성 간선종과 출혈'",
        "title_en": "Anabolic steroid abuse causing recurrent hepatic adenomas and hemorrhage",
        "summary": "PMC2731289 케이스 보고는 AAS 남용이 재발성 간세포선종과 반복 출혈을 일으킨 사례를 기록했다. 한 번 생긴 종양을 절제해도 사용 이력이 남긴 손상은 재발로 돌아온다. 간은 '리셋' 버튼이 없는 장기다.",
        "summary_detail": "정리: ① 사례 — AAS 남용에 따른 다발성·재발성 간세포선종. ② 합병증 — 종양 내 출혈 반복. ③ 의미 — 절제 후에도 재발 가능, 장기 추적 필요. ④ 기전 — 안드로겐이 간세포 증식을 자극, 선종 형성·혈관 취약성 증가. ⑤ 위치 — NIH PMC 등재 케이스. NOGEAR 시각: 잘라내도 다시 자란다. 약을 끊는 것과 흔적을 지우는 것은 다른 일이다.",
        "category": "research", "category_ko": "간·종양",
        "source": "PMC2731289", "source_type": "journal",
        "source_url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC2731289/",
        "credibility": cred(True, True, True, "high", "NIH PMC2731289 케이스. AAS 연관 재발성 간선종·출혈 기술 일치.", "verified"),
        "viral_signals": sig(22, 17, 16, 12, 10, 7),
        "tags": ["간선종", "재발", "간출혈", "AAS", "케이스보고"],
    },
    {
        "title": "LiverTox 공식 등재 — 안드로겐 스테로이드는 '간을 공격하는 약물'",
        "title_en": "Androgenic Steroids — LiverTox (NIH)",
        "summary": "NIH의 약물성 간손상 표준 데이터베이스 LiverTox(NBK548931)는 안드로겐 스테로이드를 담즙정체성 황달, 펠리오시스 간염, 간선종, 간세포암을 일으킬 수 있는 간독성 약물로 정식 등재하고 있다. '근육 보충제'가 아니라 간 질환 위험 인자라는 게 정부 레퍼런스의 결론이다.",
        "summary_detail": "정리: ① 위치 — NIH LiverTox 약물성 간손상(DILI) 표준 레퍼런스에 안드로겐 스테로이드 항목 등재. ② 위험 — 담즙정체성 황달, 펠리오시스 간염, 간세포선종, 간세포암. ③ 핵심 — 17-알파 알킬화 경구 스테로이드의 간독성이 특히 높음. ④ 의미 — 부작용이 일화가 아닌 정부 의학 데이터베이스 등재 사실. NOGEAR 시각: 정부가 만든 간독성 약물 목록에 이름이 올라 있다. 그게 진짜 '인증 배지'다.",
        "category": "research", "category_ko": "간·독성",
        "source": "LiverTox / NCBI Bookshelf NBK548931 (NIH)", "source_type": "journal",
        "source_url": "https://www.ncbi.nlm.nih.gov/books/NBK548931/",
        "credibility": cred(True, True, True, "high", "NIH LiverTox NBK548931. 안드로겐 스테로이드 간독성(담즙정체·펠리오시스·선종·간암) 등재 일치.", "verified"),
        "viral_signals": sig(20, 20, 15, 12, 9, 5),
        "tags": ["LiverTox", "간독성", "안드로겐", "간암", "NIH"],
    },
    {
        "title": "SARMs의 진짜 정체 — '안전한 스테로이드 대체'는 마케팅, 정체는 미승인 실험물질",
        "title_en": "Recreational Use of Selective Androgen Receptor Modulators",
        "summary": "US Pharmacist 리뷰는 SARMs(선택적 안드로겐 수용체 조절제)가 '부작용 없는 스테로이드 대체'로 팔리지만, 실제로는 어떤 규제당국도 인체 사용을 승인하지 않은 실험 단계 물질임을 명확히 한다. 테스토스테론 억제, 간손상, 지질 악화가 보고되는데도 보충제로 둔갑해 유통된다.",
        "summary_detail": "정리: ① 마케팅 vs 실제 — '근육만 키우고 부작용은 없다'는 주장 대 미승인 실험물질. ② 규제 — FDA 포함 어떤 당국도 인체 치료용으로 승인하지 않음(investigational only). ③ 보고된 부작용 — 내인성 테스토스테론 억제, 간효소(AST/ALT) 상승, HDL 감소. ④ 유통 — 불법적으로 보충제·연구용 화학물질로 위장 판매. ⑤ 함의 — '약한 스테로이드'가 아니라 '검증 안 된 약물'. NOGEAR 시각: 이름이 부드럽다고 안전한 게 아니다. SARMs의 'S'는 Safe가 아니다.",
        "category": "research", "category_ko": "SARMs",
        "source": "US Pharmacist", "source_type": "journal",
        "source_url": "https://www.uspharmacist.com/article/recreational-use-of-selective-androgen-receptor-modulators",
        "credibility": cred(False, True, True, "high", "US Pharmacist 임상 리뷰. SARMs 미승인·테스토스테론억제·간/지질 영향 기술 일치.", "verified"),
        "viral_signals": sig(19, 17, 18, 13, 12, 5),
        "tags": ["SARMs", "미승인", "마케팅", "간손상", "테스토스테론억제"],
    },
    {
        "title": "SARMs, LiverTox에도 올랐다 — 약물성 간손상(DILI) 공식 인자",
        "title_en": "Selective Androgen Receptor Modulators — LiverTox",
        "summary": "NIH LiverTox(NBK619971)는 SARMs를 약물성 간손상을 일으킬 수 있는 물질로 등재했다. 사용자 사이에서 황달·간효소 급등을 동반한 간손상 케이스가 보고됐고, 심근염·건파열까지 연관 사례가 누적되고 있다. '부작용 없는 SARMs'는 데이터로 반박된다.",
        "summary_detail": "정리: ① 등재 — NIH LiverTox에 SARMs 약물성 간손상(DILI) 항목 수록. ② 임상 — 담즙정체성 간손상·황달, AST/ALT 상승 케이스 보고. ③ 추가 위험 — 심근염(myocarditis), 건(腱) 파열 연관 사례. ④ 의미 — 'SARMs는 간에 안전'이라는 통념과 정면 배치. ⑤ 출처 — 정부 의학 레퍼런스. NOGEAR 시각: 간이 노랗게 변하고 나서야 'CHECKED'를 떠올린다. 그땐 늦다.",
        "category": "research", "category_ko": "SARMs",
        "source": "LiverTox / NCBI Bookshelf NBK619971 (NIH)", "source_type": "journal",
        "source_url": "https://www.ncbi.nlm.nih.gov/books/NBK619971/",
        "credibility": cred(True, True, True, "high", "NIH LiverTox NBK619971. SARMs DILI 등재·간손상 케이스 기술 일치.", "verified"),
        "viral_signals": sig(20, 19, 16, 13, 10, 5),
        "tags": ["SARMs", "LiverTox", "간손상", "황달", "DILI"],
    },
    {
        "title": "USADA 공식 입장 — SARMs는 금지약물, FDA 승인 제품은 '0개'",
        "title_en": "Selective Androgen Receptor Modulators (SARMs) — USADA",
        "summary": "미국반도핑기구(USADA)는 SARMs를 동화작용제(anabolic agents) 금지 분류로 명시하고, 인체 치료용으로 승인된 SARMs가 전 세계에 단 하나도 없다고 못 박는다. 보충제 라벨에 'SARM'이 적혀 있으면 그 자체로 불법·금지 신호다.",
        "summary_detail": "정리: ① 분류 — WADA/USADA 금지목록상 '동화작용제(Anabolic Agents)'. ② 승인 현황 — FDA 승인 SARMs 0개, 전부 investigational. ③ 도핑 — 운동선수 적발 시 자격정지 대상. ④ 라벨 함정 — 보충제에 SARM 표기 = 불법 성분 신호. ⑤ 출처 — USADA 공식 안내. NOGEAR 시각: 반도핑기구가 '약물'이라 부르는 걸 보충제 코너에서 산다. 라벨이 거짓말의 시작이다.",
        "category": "research", "category_ko": "SARMs",
        "source": "USADA", "source_type": "news",
        "source_url": "https://www.usada.org/spirit-of-sport/selective-androgen-receptor-modulators-sarms-prohibited-class-anabolic-agents/",
        "credibility": cred(False, True, True, "high", "USADA 공식. SARMs 금지분류·FDA 미승인(0개) 기술 일치.", "verified"),
        "viral_signals": sig(17, 16, 16, 13, 13, 5),
        "tags": ["SARMs", "USADA", "금지약물", "FDA미승인", "도핑"],
    },
    {
        "title": "보충제 속 숨은 SARMs, 고체분석으로 잡아낸다 — '미등록' 제품의 불편한 진실",
        "title_en": "Rapid detection of illegal SARMs in unregistered supplements",
        "summary": "PMC12205930 연구는 미등록 보충제에 불법으로 섞인 SARMs를 고체상 분석법 조합으로 신속 검출하는 방법을 제시했다. 라벨에 없는 SARMs가 '천연·합법 보충제'로 둔갑해 팔리고 있다는 증거다. 소비자는 자신이 뭘 먹는지조차 모른다.",
        "summary_detail": "정리: ① 문제 — 미등록(unregistered) 보충제에 라벨 미표기 SARMs 혼입. ② 기법 — 선택된 고체상 분석법 조합으로 신속 검출. ③ 의미 — 시중 '보충제'가 표기와 다른 약물 함유 가능. ④ 위험 — 소비자가 모르게 금지·미승인 약물 섭취 → 도핑·간독성 위험. ⑤ 출처 — NIH PMC 등재 분석화학 연구. NOGEAR 시각: 내가 먹는 게 단백질인지 약물인지 실험실이 알려준다. 라벨은 모른다.",
        "category": "research", "category_ko": "SARMs·검출",
        "source": "PMC12205930", "source_type": "journal",
        "source_url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC12205930/",
        "credibility": cred(True, True, True, "high", "NIH PMC12205930. 미등록 보충제 내 불법 SARMs 검출법 기술 일치.", "verified"),
        "viral_signals": sig(18, 18, 16, 13, 10, 5),
        "tags": ["SARMs", "보충제", "불법혼입", "검출", "라벨불일치"],
    },
    {
        "title": "세계 첫 '암시장 스테로이드 성분검사' 시작 — 음지의 바이알엔 뭐가 들었나",
        "title_en": "The world's first anabolic-androgenic steroid testing trial (Piatkowski, Addiction 2025)",
        "summary": "2025년 Addiction 저널에 실린 세계 최초 AAS 성분검사 시범사업(Piatkowski 등)은, 사용자가 익명으로 자신의 스테로이드를 검사 의뢰하게 했다. 분석 결과 상당수가 라벨과 다른 성분이거나 함량 불일치였다. 음지의 바이알이 '복불복'이라는 걸 데이터로 증명한 첫 사례다.",
        "summary_detail": "정리: ① 최초 — 세계 첫 커뮤니티 기반 AAS 화학분석 + 결과 환류 시범사업(2상 파일럿). ② 동기 — 사용자들은 성분 진위·함량·오염을 가장 우려. ③ 발견 — 제출 샘플의 일부가 예상과 다른 성분(예: 에난테이트 대신 사이피오네이트 치환) 또는 함량 불일치. ④ 의미 — 해악감소 관점의 약물검사 서비스 필요성. ⑤ 출처 — Wiley Addiction 동료심사. NOGEAR 시각: 자기가 찌르는 게 뭔지 검사실에 물어봐야 아는 세계. 그게 '게어'의 현실이다.",
        "category": "research", "category_ko": "암시장·검사",
        "source": "Addiction / Piatkowski 2025 (Wiley)", "source_type": "journal",
        "source_url": "https://onlinelibrary.wiley.com/doi/10.1111/add.70009",
        "credibility": cred(True, True, True, "high", "Wiley Addiction 2025 Piatkowski. 세계 첫 AAS 성분검사 시범사업·라벨 불일치 기술 일치. PMC12128565 동일연구.", "verified"),
        "viral_signals": sig(21, 19, 17, 16, 12, 6),
        "tags": ["암시장", "스테로이드검사", "성분불일치", "해악감소", "Addiction"],
    },
    {
        "title": "독으로 펌핑한다 — 암시장 스테로이드에서 납·비소·카드뮴 검출",
        "title_en": "Pumped up with poison: many anabolic steroids contain toxic metals",
        "summary": "The Conversation이 전한 호주 연구에 따르면, 암시장 스테로이드 다수가 표기 성분이 없거나 다른 성분으로 둔갑했고, 일부에서 납·비소·카드뮴 같은 중금속이 검출됐다. 박테리아 오염도 약 30% 제품에서 확인돼, 주사할 때마다 감염 위험을 떠안는 셈이다.",
        "summary_detail": "정리: ① 출처 — 호주 암시장 스테로이드 화학분석 연구를 The Conversation이 정리. ② 라벨 — 상당수가 라벨과 불일치하거나 기대 성분이 아예 없음. ③ 중금속 — 납(lead)·비소(arsenic)·카드뮴(cadmium) 검출. ④ 미생물 — 약 30% 제품에서 박테리아 오염 보고 → 주사 시 감염·농양 위험. ⑤ 종합 — 온라인/언더그라운드 제품의 상당 비율이 위조·오염·함량오류. NOGEAR 시각: 근육을 위해 중금속을 주사한다. '게어'는 약이 아니라 복권이다 — 그것도 독이 든.",
        "category": "research", "category_ko": "오염·중금속",
        "source": "The Conversation (Australia)", "source_type": "news",
        "source_url": "https://theconversation.com/pumped-up-with-poison-new-research-shows-many-anabolic-steroids-contain-toxic-metals-261470",
        "credibility": cred(False, True, True, "high", "The Conversation 호주 연구 보도. 라벨 불일치·납/비소/카드뮴·박테리아 오염 ~30% 기술 일치.", "verified"),
        "viral_signals": sig(24, 16, 18, 15, 12, 9),
        "tags": ["암시장", "중금속", "납비소카드뮴", "오염", "위조스테로이드"],
    },
    {
        "title": "BPC-157, 큰소리만 크고 증거는 빈약 — STAT의 냉정한 진단",
        "title_en": "BPC-157: The peptide with big claims and scant evidence (STAT)",
        "summary": "의학 매체 STAT(2026-02)은 인기 회복 펩타이드 BPC-157이 '만능 치유제'로 마케팅되지만 인체 임상 근거는 빈약하고 안전성·규제 의문이 크다고 보도했다. 동물·전임상 데이터를 인체 효능으로 비약하는 게 업계의 흔한 수법이다.",
        "summary_detail": "정리: ① 주장 — BPC-157은 힘줄·근육·장 치유 '만능 펩타이드'로 홍보. ② 현실 — 대부분 동물·전임상 데이터, 인체 무작위대조시험(RCT) 근거 빈약. ③ 안전성 — 장기 안전성·순도·제조 품질 미검증. ④ 규제 — 인체 치료용 승인 부재, 컴파운딩·연구용으로 회색지대 유통. ⑤ 출처 — STAT 탐사 보도(2026). NOGEAR 시각: 쥐에서 좋았다는 게 사람에게 좋다는 뜻은 아니다. 펩타이드 시장은 그 비약을 팔아 돈을 번다.",
        "category": "research", "category_ko": "펩타이드",
        "source": "STAT News 2026-02-03", "source_type": "news",
        "source_url": "https://www.statnews.com/2026/02/03/bpc-157-peptide-science-safety-regulatory-questions/",
        "credibility": cred(False, True, True, "high", "STAT 2026-02-03. BPC-157 인체 근거 빈약·안전성/규제 의문 보도 일치.", "verified"),
        "viral_signals": sig(19, 17, 17, 16, 12, 5),
        "tags": ["BPC-157", "펩타이드", "근거빈약", "STAT", "규제"],
    },
    {
        "title": "FDA, 7월에 BPC-157·TB-500 운명 결정 — 펩타이드 회색지대 끝나나",
        "title_en": "FDA Pharmacy Compounding Advisory Committee (July 23-24, 2026)",
        "summary": "FDA 약국 컴파운딩 자문위원회가 2026년 7월 23~24일 BPC-157, TB-500 등 펩타이드의 503A 벌크물질 목록 등재 여부를 논의한다. 결정에 따라 컴파운딩 약국을 통한 합법 유통 경로가 열리거나 완전히 막힌다. 펩타이드 시장의 분기점이다.",
        "summary_detail": "정리: ① 일정 — 2026년 7월 23~24일 FDA 약국 컴파운딩 자문위(PCAC) 회의. ② 안건 — BPC-157, TB-500 및 관련 벌크 약물물질의 503A Bulks List 등재 검토. ③ 의미 — 등재되면 컴파운딩 약국 합법 조제 가능, 거부되면 회색지대 차단. ④ 배경 — 펩타이드 인기 급증에 따른 규제 정비 수요. ⑤ 출처 — FDA 자문위원회 공식 일정. NOGEAR 시각: 정부가 '약인지 아닌지' 표결로 정하는 물질을 이미 수만 명이 몸에 넣고 있다. 순서가 거꾸로다.",
        "category": "research", "category_ko": "펩타이드·규제",
        "source": "FDA Advisory Committee Calendar", "source_type": "news",
        "source_url": "https://www.fda.gov/advisory-committees/advisory-committee-calendar/july-23-24-2026-meeting-pharmacy-compounding-advisory-committee-07232026",
        "credibility": cred(False, True, True, "high", "FDA 공식 일정. 2026-07-23~24 PCAC, BPC-157/TB-500 503A 벌크 검토 일치.", "verified"),
        "viral_signals": sig(18, 17, 15, 18, 11, 5),
        "tags": ["FDA", "BPC-157", "TB-500", "컴파운딩", "503A"],
    },
    {
        "title": "BPC-157 법적 지위 2026 정리 — '합법'이라 믿고 산 펩타이드의 진짜 상태",
        "title_en": "BPC-157 Legal Status & FDA Update (2026)",
        "summary": "2026년 BPC-157 법적 지위 정리에 따르면, 이 펩타이드는 FDA 승인 의약품이 아니며 컴파운딩 사용도 제한·검토 대상이다. '연구용(research only)'·'합법 회색지대'라는 판매 문구는 소비자를 안심시키는 마케팅에 가깝다.",
        "summary_detail": "정리: ① 지위 — FDA 승인 의약품 아님, 컴파운딩 가능성도 PCAC 검토에 묶임. ② 판매 문구 — 'research only', 'not for human consumption' 라벨로 책임 회피. ③ 현실 — 소비자는 인체 사용, 판매자는 면책. ④ 위험 — 순도·용량·출처 불확실. ⑤ 출처 — 펩타이드 법적지위 가이드(2026). NOGEAR 시각: '연구용'이라 적고 사람이 주사한다. 그 모순이 바로 회색지대의 본질이다.",
        "category": "research", "category_ko": "펩타이드·규제",
        "source": "The Peptide Guides (2026)", "source_type": "blog",
        "source_url": "https://thepeptideguides.com/guides/bpc-157-legal-status",
        "credibility": cred(False, False, True, "medium", "전문 가이드 매체. BPC-157 FDA 미승인·연구용 라벨 회색지대 기술 일치. 1차 규제문서는 FDA/STAT로 교차확인.", "checked"),
        "viral_signals": sig(16, 13, 16, 15, 11, 5),
        "tags": ["BPC-157", "법적지위", "연구용라벨", "회색지대", "FDA미승인"],
    },
    {
        "title": "BPC-157의 양날 — 혈관신생·산화질소 조절, 보호도 손상도 가능하다는 경고",
        "title_en": "BPC-157 Therapy: Targeting Angiogenesis and Nitric Oxide (Pharmaceuticals 2025 comment)",
        "summary": "PMC12567428 학술 코멘트는 BPC-157이 혈관신생(VEGFR2)과 산화질소(NO) 경로를 조절해 조직 보호 효과를 낼 수 있다고 보면서도, 같은 기전이 세포독성·손상으로 작용할 수 있는 양날임을 지적한다. '치유 펩타이드'의 작용기전이 곧 위험기전이기도 하다.",
        "summary_detail": "정리: ① 기전 — BPC-157은 VEGFR2 매개 혈관신생과 NO 시스템을 조절. ② 양면성 — 보호·치유 작용과 동시에 산화질소의 세포독성·손상 작용에도 관여 가능. ③ 핵심 주장 — '본질적 보호 기능을 유지·회복'하는 균형이 관건. ④ 함의 — 단순 '안전한 치유제'로 단정 불가, 맥락 의존적. ⑤ 출처 — MDPI Pharmaceuticals 2025 학술 코멘트(PMC). NOGEAR 시각: 같은 스위치가 살리기도 죽이기도 한다. 만능이라는 말이 가장 위험한 마케팅이다.",
        "category": "research", "category_ko": "펩타이드",
        "source": "Pharmaceuticals 2025 / PMC12567428", "source_type": "journal",
        "source_url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12567428/",
        "credibility": cred(True, True, True, "medium", "MDPI Pharmaceuticals 2025 학술 코멘트(PMC12567428). BPC-157 VEGFR2/NO 양면성 기술 일치. 코멘트 성격상 단일 1차근거 아님.", "checked"),
        "viral_signals": sig(17, 18, 15, 13, 11, 5),
        "tags": ["BPC-157", "혈관신생", "산화질소", "양날", "펩타이드"],
    },
    {
        "title": "오젬픽, 약빼고 근육도 뺀다 — 그리고 '오남용' 인구까지 등장",
        "title_en": "Ozempic/Semaglutide Injection Misuse — nationally representative sample (medRxiv)",
        "summary": "medRxiv에 공개된 미국 대표표본 연구는 세마글루타이드(오젬픽) 주사가 의학적 적응증 밖에서 오남용되고 있음을 보고했다. 체중과 함께 제지방(근육)이 빠지는 부작용이 알려졌는데도, 외모·체형 목적의 비처방 사용이 일정 비율로 존재한다.",
        "summary_detail": "정리: ① 데이터 — 미국 전국 대표표본 기반 세마글루타이드 주사 오남용 보고(medRxiv 프리프린트). ② 근육 — GLP-1 계열은 급격한 체중감소 시 제지방(근육) 손실 동반(임상서 최대 ~14% 제지방 감소 보고). ③ 오남용 — 적응증 밖·비처방 사용 인구 존재. ④ 맥락 — 'cutting' 목적 보디빌딩 커뮤니티 오프라벨 사용 확산. ⑤ 단계 — 프리프린트(동료심사 전), 해석 주의. NOGEAR 시각: 약으로 빼면 근육도 같이 빠진다. 숏컷의 대가는 늘 제지방으로 계산된다.",
        "category": "research", "category_ko": "GLP-1·오남용",
        "source": "medRxiv preprint (2025)", "source_type": "journal",
        "source_url": "https://www.medrxiv.org/content/10.64898/2025.12.25.25343021.full.pdf",
        "credibility": cred(False, True, True, "medium", "medRxiv 프리프린트(동료심사 전). 세마글루타이드 오남용 대표표본 보고. 제지방 손실은 임상 다출처 교차확인.", "checked"),
        "viral_signals": sig(20, 15, 19, 16, 12, 5),
        "tags": ["오젬픽", "세마글루타이드", "근손실", "오남용", "GLP-1"],
    },
    {
        "title": "티르제파타이드(마운자로)도 근육 깎는다 — 체중감량의 25%가 제지방",
        "title_en": "Effects of Tirzepatide on Skeletal Muscle Mass in Adults: A Systematic Review",
        "summary": "PMC12394919 체계적 검토는 티르제파타이드(마운자로) 치료 시 감량 체중의 약 25%가 제지방(근육)에서 빠진다고 정리했다. 지방을 주로 줄이지만 근육 손실도 분명히 동반된다. '약으로 빼면 근육은 지킨다'는 기대는 데이터로 절반만 맞다.",
        "summary_detail": "정리: ① 약물 — 티르제파타이드(GIP/GLP-1 이중작용제, 상품명 마운자로). ② 핵심 수치 — 임상에서 총 감량 체중의 약 25%가 제지방, 약 75%가 지방. ③ 비율 — 제지방 1kg 손실당 지방 2.9~6.1kg 감소(지방 우선 표적). ④ 단서 — 일부 체계적 검토는 상대적 제지방 보존을 보고, 결과 이질적. ⑤ 출처 — NIH PMC 체계적 검토. NOGEAR 시각: 지방을 더 많이 빼도, 근육은 분명히 같이 나간다. 저항운동·단백질 없이는 '마른 약골'이 남는다.",
        "category": "research", "category_ko": "GLP-1·근육",
        "source": "PMC12394919 (Systematic Review)", "source_type": "journal",
        "source_url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC12394919/",
        "credibility": cred(True, True, True, "high", "NIH PMC12394919 체계적 검토. 티르제파타이드 제지방 ~25% 손실·지방 우선 감소 기술 일치.", "verified"),
        "viral_signals": sig(19, 19, 18, 15, 10, 5),
        "tags": ["티르제파타이드", "마운자로", "제지방손실", "GLP-1", "체계적검토"],
    },
    {
        "title": "팔룸보이즘(HGH 거트)의 정체 — 성장호르몬+인슐린이 장기를 키운다",
        "title_en": "Palumboism AKA HGH Gut: A Potentially Fatal Side-Effect of HGH",
        "summary": "'버블 거트'로 불리는 팔룸보이즘은 HGH·인슐린·AAS 병용 보디빌더에게 나타나는 복부 팽만이다. HGH와 IGF-1이 내장 장기를 키우는 내장비대(visceromegaly)에, 인슐린이 내장지방을 더해 복벽을 밖으로 밀어낸다. 심근증으로 인한 심부전 사망 위험까지 있는 상태다.",
        "summary_detail": "정리: ① 정의 — 고도 보디빌더의 심한 복부 팽만('버블 거트'), 데이브 팔룸보의 이름에서 유래. ② 원인 — HGH·인슐린·AAS 병용. ③ 기전 — HGH/IGF-1이 내장 장기 성장(visceromegaly), 인슐린이 내장지방 증가 → 복벽 외측 압출. ④ 유사성 — 유발성 말단비대증(acromegaly)과 기전·외형 유사. ⑤ 치명성 — 심근증에 의한 심혈관 부전으로 사망 가능. NOGEAR 시각: 식스팩 위로 튀어나온 배. 그건 살이 아니라 커져버린 장기다. 무대 위 괴물성의 대가다.",
        "category": "research", "category_ko": "HGH·인슐린",
        "source": "Gilmore Health News", "source_type": "news",
        "source_url": "https://www.gilmorehealth.com/palumboism-a-potentially-fatal-side-effect-of-human-growth-hormone/",
        "credibility": cred(False, False, True, "medium", "Gilmore Health 보도 + 학술(PMC11578072 Abdominal Hypertrophy Syndrome) 교차확인. HGH/IGF-1 내장비대·인슐린 내장지방 기전 일치.", "checked"),
        "viral_signals": sig(23, 14, 18, 13, 12, 11),
        "tags": ["팔룸보이즘", "HGH거트", "버블거트", "인슐린", "내장비대"],
    },
    {
        "title": "근육 키우다 신장 망가진다 — 보디빌더 10명 중 9명서 'FSGS' 신장 흉터",
        "title_en": "Gym nephropathy: bodybuilding versus kidney damaging",
        "summary": "신장 전문 저널은 장기간 스테로이드를 쓴 보디빌더 다수에서 초점성 분절성 사구체경화증(FSGS)이라는 신장 흉터가 발견됐다고 정리한다. 고단백 식이와 만성 과여과, AAS가 겹쳐 신장을 과로시킨다. 단백뇨와 신기능 저하로 투석까지 갈 수 있다.",
        "summary_detail": "정리: ① 소견 — 컬럼비아 연구에서 장기 스테로이드 사용 보디빌더 10명 중 9명이 FSGS(초점성 분절성 사구체경화증). ② 기전 — 고단백 식이로 인한 질소노폐물 증가 → 신혈류·만성 과여과 → 사구체경화 가속, AAS가 가중. ③ 임상 — 단백뇨(평균 ~10g/일), 혈청 크레아티닌 상승, 일부 신증후군. ④ 중증도 — 고도비만 환자보다 더 심한 손상 양상. ⑤ 출처 — 이집트신장이식학회지 'gym nephropathy' 리뷰. NOGEAR 시각: 단백질 셰이크와 게어가 만나 신장을 갈아넣는다. 투석실은 헬스장 다음 정거장이 될 수 있다.",
        "category": "research", "category_ko": "신장",
        "source": "J. Egyptian Society of Nephrology and Transplantation", "source_type": "journal",
        "source_url": "https://journals.lww.com/esnt/fulltext/2019/19040/gym_nephropathy__bodybuilding_versus_kidney.4.aspx",
        "credibility": cred(True, True, True, "high", "신장학회지 리뷰. 보디빌더 FSGS·고단백/과여과 기전·단백뇨/크레아티닌 상승 기술 일치(컬럼비아 9/10 교차확인).", "verified"),
        "viral_signals": sig(22, 18, 18, 12, 10, 6),
        "tags": ["신장", "FSGS", "단백뇨", "고단백", "AAS"],
    },
    {
        "title": "보디빌더 급성 신손상 케이스 시리즈 — 스테로이드+보충제 조합의 신장 청구서",
        "title_en": "Acute kidney injury associated with androgenic steroids and nutritional supplements in bodybuilders",
        "summary": "Clinical Kidney Journal(옥스퍼드)에 실린 케이스 시리즈는 보디빌더에서 안드로겐 스테로이드와 보충제 병용이 급성 신손상(AKI)을 유발한 사례들을 보고했다. 단백질 보충제·이뇨·탈수·AAS가 겹치면 신장이 급격히 무너질 수 있다.",
        "summary_detail": "정리: ① 사례 — 보디빌더의 급성 신손상(AKI) 케이스 시리즈. ② 요인 — 안드로겐 스테로이드 + 고용량 단백질/보충제, 탈수·이뇨제 사용 동반. ③ 기전 — 신혈류 변화·횡문근융해·과여과·신독성 물질 부담. ④ 결과 — 일부는 회복, 일부는 만성 신질환으로 진행. ⑤ 출처 — Clinical Kidney Journal(Oxford). NOGEAR 시각: 무대 컨디셔닝을 위한 탈수·이뇨가 신장을 벼랑으로 민다. 콩팥은 펌핑을 모른다.",
        "category": "research", "category_ko": "신장",
        "source": "Clinical Kidney Journal (Oxford)", "source_type": "journal",
        "source_url": "https://academic.oup.com/ckj/article/8/4/415/337086",
        "credibility": cred(True, True, True, "high", "Oxford CKJ 케이스 시리즈. 보디빌더 AKI·스테로이드/보충제 병용 기술 일치.", "verified"),
        "viral_signals": sig(20, 18, 17, 12, 10, 5),
        "tags": ["급성신손상", "AKI", "보충제", "스테로이드", "신장"],
    },
    {
        "title": "장기 안드로겐 치료가 부른 다발성 간선종 — 재생불량성빈혈 치료의 그림자",
        "title_en": "Multiple hepatocellular adenomas associated with long-term androgenic steroids",
        "summary": "PMC7360229 케이스+문헌고찰은 재생불량성빈혈 치료를 위한 장기 안드로겐 스테로이드 투여가 다발성 간세포선종을 유발한 사례를 보고한다. 치료 목적의 합법적 사용에서도 장기 노출은 간종양 위험을 높인다. 용량×기간이 핵심 변수다.",
        "summary_detail": "정리: ① 사례 — 재생불량성빈혈(aplastic anemia)에 대한 장기 안드로겐 치료 후 다발성 간세포선종. ② 의미 — 남용뿐 아니라 치료적 장기 투여에서도 간종양 위험. ③ 변수 — 노출 용량·기간이 위험을 결정. ④ 위험 — 선종의 출혈·파열·악성 전환 가능성. ⑤ 출처 — NIH PMC 케이스+문헌고찰. NOGEAR 시각: '의사가 처방한 안드로겐'도 시간이 길면 간에 종양을 남긴다. 음지의 자가투여는 말할 것도 없다.",
        "category": "research", "category_ko": "간·종양",
        "source": "PMC7360229", "source_type": "journal",
        "source_url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC7360229/",
        "credibility": cred(True, True, True, "high", "NIH PMC7360229 케이스+리뷰. 장기 안드로겐 치료·다발성 간선종 기술 일치.", "verified"),
        "viral_signals": sig(19, 18, 15, 12, 10, 6),
        "tags": ["간선종", "안드로겐", "장기투여", "재생불량성빈혈", "간종양"],
    },
    {
        "title": "DNP, 치료약이 없는 다이어트 독약 — 체온 44도, 치사율 12%",
        "title_en": "Deadly DNP — UK Health Security Agency",
        "summary": "영국보건안전청(UKHSA)은 다이어트 약물 DNP(2,4-디니트로페놀)을 '해독제가 없는 독약'으로 경고한다. 미토콘드리아 산화적 인산화를 탈공역시켜 ATP 대신 열을 폭발시키고, 체온이 44도까지 치솟아 사망에 이른다. 2010~2020년 보고 과량 사례 치사율은 약 12%였다.",
        "summary_detail": "정리: ① 정체 — 1930년대 인체사용 금지된 산업용 화학물질, 온라인으로 부활한 다이어트 약. ② 기전 — 미토콘드리아 산화적 인산화 탈공역 → ATP 미생성·열 방출 폭증 → 통제불능 고체온(최대 ~44°C). ③ 치명성 — 해독제 없음, 과량 시 사망. ④ 통계 — 2010~2020년 독성센터 보고 과량 사례 치사율 ~11.9%, 전 세계 50명 이상 사망. ⑤ 위험 — 권장 용량에서도 사망 발생. NOGEAR 시각: 몸을 안에서부터 태우는 약. 다이어트 숏컷이 화장(火葬)이 되는 경로다.",
        "category": "research", "category_ko": "약물·DNP",
        "source": "UK Health Security Agency", "source_type": "news",
        "source_url": "https://ukhsa.blog.gov.uk/2018/08/13/deadly-dnp/",
        "credibility": cred(False, True, True, "high", "UKHSA 공식 블로그. DNP 탈공역·고체온·치사율 ~12%·해독제 부재 기술 일치(PMC 다출처 교차확인).", "verified"),
        "viral_signals": sig(25, 16, 17, 12, 11, 9),
        "tags": ["DNP", "다이어트약", "고체온", "치사율", "해독제없음"],
    },
]

# ============ NEWS ============
NEW_NEWS = [
    {
        "title": "'약물 허용' Enhanced Games 개막 — 그리스 수영선수, 세계기록 깨고 13억 잭팟",
        "title_en": "Enhanced Games results: Gkolomeev breaks world record for $1M bonus",
        "summary": "약물 사용을 허용한 'Enhanced Games'가 5월 24일 라스베이거스에서 열렸고, 그리스 수영선수 크리스티안 골로미프가 남자 50m 자유형에서 20.81초로 비강화 세계기록(20.88)을 넘어섰다. 우승 상금 25만 달러에 세계기록 보너스 100만 달러를 더해 약 13억원을 챙겼다. 단, 이 기록은 공인되지 않는다.",
        "summary_detail": "정리: ① 행사 — 5월 24일(일) 라스베이거스 Resorts World에서 약물 허용 'Enhanced Games' 개최, 약 24개 종목. ② 하이라이트 — 골로미프 50m 자유형 20.81초로 비강화 WR(20.88) 경신. ③ 상금 — 우승 25만 달러 + WR 보너스 100만 달러(수영서만 1회 지급). ④ 비공인 — 금지된 폴리우레탄 수영복·반도핑 통제 부재·비공인 대회로 World Aquatics 비준 거부. ⑤ 맥락 — 참가자 91% 테스토스테론, 79% HGH, 62% 자극제 사용 보고. NOGEAR 시각: 약을 풀면 기록은 깨진다. 그런데 그 기록은 아무도 인정하지 않는다 — 약이 만든 숫자엔 이름표가 없다.",
        "category": "scandal", "category_ko": "도핑·이벤트",
        "source": "Yahoo Sports 2026-05", "source_type": "news",
        "source_url": "https://sports.yahoo.com/olympics/article/enhanced-games-results-swimmer-kristian-gkolomeev-breaks-world-record-in-final-event-for-1m-bonus-fred-kerley-falls-short-235007088.html",
        "credibility": cred(False, False, True, "high", "Yahoo Sports 보도. 골로미프 20.81초·상금구조·비공인 기술 일치(LBC/JudgeMate 교차확인).", "match"),
        "viral_signals": sig(24, 12, 19, 20, 18, 10),
        "tags": ["EnhancedGames", "도핑허용", "세계기록", "골로미프", "라스베이거스"],
    },
    {
        "title": "Enhanced Games '세계기록'은 가짜다 — 공인 거부의 3가지 이유",
        "title_en": "Are the Enhanced Games Records Real? Ratification",
        "summary": "약물 허용 Enhanced Games에서 나온 '세계기록'은 어느 공식기구도 인정하지 않는다. 금지된 폴리우레탄 수영복, 반도핑 통제 전무, 비공인 대회라는 세 가지가 비준을 막는다. 숫자는 빨랐지만, 스포츠는 그것을 기록으로 세지 않는다.",
        "summary_detail": "정리: ① 쟁점 — Enhanced Games WR의 공식 인정 여부. ② 비준 거부 사유 — (1) 금지된 폴리우레탄 전신 수영복 착용, (2) 반도핑 검사·통제 부재, (3) 비공인(unsanctioned) 대회. ③ 기구 입장 — World Aquatics 비준 거부. ④ 반응 — USADA 트래비스 타이가트 '이윤이 원칙을 짓밟는 위험한 광대쇼', IOC '우리가 지키는 모든 것에 대한 배신'. ⑤ 의미 — 약·장비·무통제가 만든 기록의 공허함. NOGEAR 시각: 약으로 산 0.07초는 기록표에 오르지 못한다. 자연이 아닌 것은 결국 카운트되지 않는다.",
        "category": "scandal", "category_ko": "도핑·이벤트",
        "source": "JudgeMate / USADA·IOC 코멘트", "source_type": "news",
        "source_url": "https://www.judgemate.com/en/guides/are-enhanced-games-records-real",
        "credibility": cred(False, False, True, "medium", "JudgeMate 정리 + NPR 인용 USADA/IOC 코멘트 교차확인. 비준 거부 3사유·기구 입장 일치.", "match"),
        "viral_signals": sig(20, 12, 17, 18, 19, 8),
        "tags": ["EnhancedGames", "비공인기록", "WorldAquatics", "USADA", "도핑"],
    },
    {
        "title": "내셔널지오그래픽 경고 — 젊은 남성을 삼키는 '저(低)테스토스테론' 마케팅",
        "title_en": "Is there a 'low T' crisis? — National Geographic",
        "summary": "내셔널지오그래픽은 젊고 건강한 남성들이 의학적 결핍이 없는데도 TRT(테스토스테론 대체요법)에 빠져드는 현상을 경고했다. 지난 10년간 처방이 3배로 늘었고, 환자의 최대 1/4은 수치 검사 없이 시작했다. 너무 일찍 시작하면 자기 호르몬 생성이 꺼져 평생 약에 묶인다.",
        "summary_detail": "정리: ① 현상 — 건강한 젊은 남성의 TRT 수요 급증, '저테스토스테론 위기' 담론. ② 통계 — 지난 10년 TRT 처방 3배 증가, 정상 수치 남성에서도 증가, 환자 최대 25%는 사전 혈중검사 없이 시작. ③ 마케팅 — 피로·스트레스·성욕 저하 같은 일상 경험을 '결핍'으로 재프레이밍(시드니대 연구 인용). ④ 위험 — 조기 시작이 HPG 축을 억제해 내인성 생성 중단 → 평생 의존. ⑤ 출처 — National Geographic 헬스. NOGEAR 시각: 피곤한 걸 '저T'라 부르게 만드는 산업. 한 번 외부에서 넣으면, 몸은 만드는 법을 잊는다.",
        "category": "industry", "category_ko": "TRT·업계",
        "source": "National Geographic Health", "source_type": "news",
        "source_url": "https://www.nationalgeographic.com/health/article/why-testosterone-therapy-is-surging-among-young-men",
        "credibility": cred(False, True, True, "high", "Nat Geo 보도. TRT 처방 3배·25% 미검사·HPG 억제 의존 기술 일치(시드니대 연구 인용).", "match"),
        "viral_signals": sig(20, 15, 20, 16, 13, 6),
        "tags": ["TRT", "저테스토스테론", "젊은남성", "마케팅", "호르몬의존"],
    },
    {
        "title": "테스토스테론, 매너스피어의 '레드필 영약'이 되다 — 월 12만원에 처방되는 호르몬",
        "title_en": "Testosterone Is the Red-Pilled Elixir of the Manosphere (Inc.)",
        "summary": "Inc.은 테스토스테론이 온라인 '매너스피어'의 상징적 영약이 됐고, 기업들이 이를 주류 시장으로 끌어들이려 경쟁한다고 보도했다. 온라인 TRT 클리닉은 월 99~129달러에 처방을 내주고, Hims 같은 상장 헬스기업까지 주사형 테스토스테론 판매에 뛰어들었다.",
        "summary_detail": "정리: ① 현상 — 테스토스테론이 매너스피어의 '레드필 영약'으로 문화화. ② 산업화 — Hims(상장), Rugiet 등 텔레헬스 기업이 주사형 테스토스테론 시장 진입. ③ 가격 — 온라인 TRT 월 99~129달러, 재택 처방·랩검사 패키지. ④ 우려 — 의료 필요가 아닌 '느낌·퍼포먼스' 향상 목적 사용, 마케팅이 수요를 창출. ⑤ 출처 — Inc. 기획기사. NOGEAR 시각: 남성성을 병으로 만들고 약으로 판다. 영약이라 부르는 순간, 그건 비즈니스 모델이다.",
        "category": "industry", "category_ko": "TRT·업계",
        "source": "Inc. (Sam Blum)", "source_type": "news",
        "source_url": "https://www.inc.com/sam-blum/testosterone-is-the-red-pilled-elixir-of-the-manosphere-now-companies-are-eager-to-bring-it-mainstream/91288140",
        "credibility": cred(False, True, True, "medium", "Inc. 기획. Hims/Rugiet 진입·월 99~129달러·매너스피어 문화 기술 일치. 일부 비즈니스 전망 포함.", "match"),
        "viral_signals": sig(19, 12, 19, 16, 15, 6),
        "tags": ["테스토스테론", "매너스피어", "레드필", "온라인TRT", "Hims"],
    },
    {
        "title": "라이버킹, 스테로이드 숨긴 채 '날고기 신화' 팔았다 — 250억 집단소송",
        "title_en": "'Liver King' class action over hidden steroid use",
        "summary": "생간·생고환을 먹어 몸을 만들었다던 인플루언서 '라이버킹' 브라이언 존슨이, 스테로이드 사용을 숨긴 채 제품을 판매했다는 이유로 2,500만 달러(약 250억원) 집단소송에 휘말렸다. 그는 뒤늦게 스테로이드 사용을 인정했고, 별도로 2025년 넷플릭스 다큐의 주인공이 됐다.",
        "summary_detail": "정리: ① 인물 — '라이버킹' 브라이언 존슨, 날고기·내장식 다이어트로 거대 근육을 홍보. ② 소송 — 스테로이드 사용을 숨기고 제품을 판매했다며 뉴욕에서 2,500만 달러 집단소송 제기(원고 Christopher Altomare). ③ 핵심 주장 — 근육을 생내장 식단 덕으로 호도, 생고기·생고환 식단으로 식중독 유발 위험. ④ 진행 — 원소송은 이후 취하됨. ⑤ 후속 — 2025년 넷플릭스 다큐 'Untold: The Liver King', 같은 해 협박 혐의 체포. NOGEAR 시각: 신화의 재료는 생간이 아니라 주사기였다. FXXK FAKES — 가짜 내추럴의 교과서 사례다.",
        "category": "scandal", "category_ko": "위조내추럴",
        "source": "Top Class Actions / Rolling Stone", "source_type": "news",
        "source_url": "https://topclassactions.com/lawsuit-settlements/consumer-products/sporting-goods-equipment/liver-king-class-action-claims-fitness-influencer-hid-steroid-use-from-customers/",
        "credibility": cred(False, False, True, "high", "Top Class Actions/Rolling Stone/Yahoo 다출처. 2,500만달러 집단소송·스테로이드 은폐·원소송 취하·넷플릭스 다큐 기술 일치.", "match"),
        "viral_signals": sig(23, 11, 20, 15, 18, 9),
        "tags": ["라이버킹", "가짜내추럴", "집단소송", "스테로이드은폐", "FXXKFAKES"],
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
    d["meta"]["last_updated_kst"] = now.strftime("%Y-%m-%d %H:%M") + f" KST 아침 크롤 (펠리오시스간·TRT붐·EnhancedGames·중금속위조·SARMs간독성·펩타이드규제·신장FSGS·라이버킹) +{added}건"
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
