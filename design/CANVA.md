# 다크사이드 카드 — Canva 디자인 원본 (2026-09-27 결정: 디자인은 Canva)

- 템플릿(5장: 표지·숫자·목록·문장·마지막): https://www.canva.com/d/mbgif4Cj26a7Hbo  (보기: https://www.canva.com/d/Dq7CQIOnXiw6YRL)
- Canva 디자인 ID: `DAHWWfCrx5c`

## 흐름
1. 사람이 Canva 에서 템플릿을 고친다 (색·폰트·배치).
2. Claude 에게 «캔바 반영해줘» → Claude 가 Canva 디자인을 읽어 `design/tokens.json` 에 옮긴다.
3. 매일 08:30 맥 러너가 `git pull` 로 받아 그날 카드부터 자동 반영.

엔진(매일 생성·렌더)은 코드(`scripts/generate_dark_cardnews.py`)다 — Canva 연결은 Claude 대화 중에만 살아 있어서 무인 생성에는 쓰지 않는다.

## 모든 에셋 Canva 축적 (2026-09-27)
- 매일 러너 끝에 `scripts/dark_canva_sync.py` 가 새 에셋만 Canva 폴더 **«NGR 다크사이드 에셋»** 에 올린다:
  카드 전장(표지·본문·끝) · 대안 표지 · 표지 모음(contact sheet) · 캐릭터 이미지. 이름: `<날짜>_<편>_<카드>.png`.
- 올린 기록 `data/canva_synced.json`(맥 로컬) — 같은 파일은 다시 안 올린다. 같은 오류 2번이면 그날 멈춤.
- 처음 한 번(사람): Canva 개발자 통합 만들기(권한 asset:write · folder:read · folder:write, 리디렉트
  `http://127.0.0.1:8765/callback`) → `bash ops/canva_connect.sh` (ID·시크릿 입력 → 브라우저 허용 → 밀린 에셋 올림).
- 컨트롤타워 «팀» 표의 «에셋 매니저» 줄이 올린 수·남은 수를 보여준다.
