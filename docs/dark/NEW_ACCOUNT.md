# 계정 추가 · 컨트롤타워 (2026-09-27)

같은 공장(소재 → 카피 → 가드 → 바이럴 게이트 → 렌더 → 키트)으로 계정을 여러 개 돌린다.

## 컨트롤타워
- 화면: `tower/index.html` (매일 러너가 만들고 push → Vercel 주소 `/tower/`) · 기계용 `tower/status.json`
- 계정마다: 팔로워(7일 증감) · 오늘 편/목표 · 안 올린 편 · 누적 게시 · 보류 · 남은 소재 · 오늘 편 바이럴 점수 · 키트 · Canva 링크 · 마지막 실행
- 경보: 러너 26시간 무소식 · 오늘 목표 미달 · 남은 소재 6건 미만 · 안 올린 편이 목표의 2배 초과
- 측정 못 한 값은 `—` (0 아님). 화면 상단 생성 시각이 90분 넘게 지났으면 낡은 값.
- 수동 갱신: `python3 scripts/tower.py`

## 새 계정 추가 (3단계)
1. `scripts/generate_dark_cardnews.py` 의 `BRANDS` 에 브랜드 하나 추가 (handle·name·tag·avatar·motto·signoff·bio).
2. `config/accounts.json` 에 계정 추가 — **out_suffix · ledger · queue 는 다른 계정과 겹치면 안 된다**(테스트가 막는다).
   `axes` 로 다룰 축만 고른다(예: 약물 계정은 `["drugs","sport"]`).
3. `enabled: true` → 다음 08:30 러너부터 그 계정도 만들고 키트가 생긴다. 시험: `python3 scripts/dark_daily.py --account <id> --test --count 1`.

같이 쓰는 것: 팩트 원장·PubMed 소재·가드·바이럴 게이트·디자인 토큰.
따로 쓰는 것: 브랜드·축·원장(소재 재사용 판정)·출력 폴더·게시 시간.
자격증명(자동 게시를 켤 때만)은 파일에 두지 않는다.

## 에셋
- 카드·릴스·캡션: `cardnews/<날짜>_<out_suffix>/<편>/`
- 올릴 것: 그 날 폴더의 `POST_TODAY.md`
- 전체 색인(ngr): `cardnews/DARK_INDEX.md` · `content/dark/assets_index.json`
- 디자인: `design/tokens.json` (Canva 템플릿 반영은 «캔바 반영해줘»)
