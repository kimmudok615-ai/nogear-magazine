# 다크사이드 카드 — Canva 디자인 원본 (2026-09-27 결정: 디자인은 Canva)

- 템플릿(5장: 표지·숫자·목록·문장·마지막): https://www.canva.com/d/mbgif4Cj26a7Hbo  (보기: https://www.canva.com/d/Dq7CQIOnXiw6YRL)
- Canva 디자인 ID: `DAHWWfCrx5c`

## 흐름
1. 사람이 Canva 에서 템플릿을 고친다 (색·폰트·배치).
2. Claude 에게 «캔바 반영해줘» → Claude 가 Canva 디자인을 읽어 `design/tokens.json` 에 옮긴다.
3. 매일 08:30 맥 러너가 `git pull` 로 받아 그날 카드부터 자동 반영.

엔진(매일 생성·렌더)은 코드(`scripts/generate_dark_cardnews.py`)다 — Canva 연결은 Claude 대화 중에만 살아 있어서 무인 생성에는 쓰지 않는다.
