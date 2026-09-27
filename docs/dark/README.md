# 다크사이드 파일 지도 — 여기서 시작

한 화면으로 보기: **에셋 보드 `board/index.html`** (Vercel `/board/`) · **컨트롤타워 `tower/index.html`** (`/tower/`).
둘 다 매일 08:30 러너가 새로 만든다. 손으로 고치지 않는다.

## 폴더
| 폴더 | 무엇 | 누가 쓰나 |
|---|---|---|
| `cardnews/<날짜>_dark_auto/<편>/` | 매일 만든 캐러셀(카드 PNG·캡션·series.json·대안 표지·릴스) + 그날 `POST_TODAY.md` | 러너 |
| `cardnews/<날짜>_dark_examples/<편>/` | 기획·예시 묶음 렌더 결과 + `EXAMPLES.md` · 표지 모음 | `dark_batch.py` |
| `cardnews/20260924_dark/` | 첫 수작업 세트 A~E·벤치마크 원본 (보관) | — |
| `cardnews/assets/` | 스톡 배경 · `characters/` 캐릭터 이미지(맥에서 받음) | 러너 |
| `content/dark/` | 연구 소재 `research.json` · 화제 `trends.json` · 예시 원고 `examples/` · 검증 `jev_audit.json` | 러너·사람 |
| `design/` | 철학 `PHILOSOPHY.md` · 규칙 `DESIGN_RULES.md` · 색 `tokens.json` · 글꼴 `fonts/` · 캐릭터 `characters.json` · Canva `CANVA.md`·`canva_assets.json` | 사람 |
| `config/` | 계정 `accounts.json` · 팀 `team.json` | 사람 |
| `docs/dark/` | 분석 · 매거진 방향 · 팀 · 계정 추가 · 이 지도 | 사람 |
| `ops/` | 러너 `dark_daily.sh` · 설치 `install_mac.sh` · Canva 연결 `canva_connect.sh` · 원격 보고 `status/` | 사람(설치)·러너 |
| `board/` · `tower/` | 에셋 보드 · 컨트롤타워 (생성물) | 러너 |
| `data/` (저장소 밖, 맥 로컬) | 원장 · 대기열 · Canva 기록 · 토큰 | 러너 |

## 스크립트 — 팀 역할별 (`config/team.json` 순서)
| 역할 | 스크립트 |
|---|---|
| 편집장(주인) | `dark_daily.py` |
| 화제 리서처 | `dark_trends.py` |
| 팩트 리서처 | `dark_research.py` |
| 소재 기획 | `dark_picker.py` |
| 카피라이터 | `dark_copywriter.py` |
| 안전 검수 | `dark_guard.py` |
| 바이럴 심사 | `dark_viral.py` |
| JEV 심사위원 | `dark_jev.py` (→ 노기어 `judgment_chain`) |
| 디자이너 | `generate_dark_cardnews.py` + `dark_thread.py`(기본) · `dark_dossier.py`(대안) · `dark_design_qa.py`(검사) · `dark_reel.py` · `dark_characters.py` |
| 게시 매니저 | `dark_kit.py` (게시는 사람) · `dark_publish.py`(자동 게시, 꺼짐) |
| 에셋 매니저 | `dark_board.py` · `dark_assets.py` · `dark_canva_sync.py` |
| 성과 분석가 | `dark_measure.py` · `dark_jev_audit.py` |
| 컨트롤타워 | `tower.py` · `dark_team.py` |
| 공용 | `dark_ledger.py` · `dark_accounts.py` · `dark_tokens.py` · `dark_notify.py` · `dark_heal.py` · `dark_batch.py` |

## 한 편의 흐름 (에셋 보드의 8칸 막대)
소재 → 카피 → 안전 → 바이럴 → JEV → 디자인 QC → 게시 → 측정.
막대 색: 초록 완료 · 노랑 대기 · 빨강 문제 · 회색 없음. 편을 누르면 카드 전장·대안 표지·역할별 판정·캡션 복사.

**예상 바이럴(추측)** = 바이럴 게이트 점수 × 0.7 + JEV 순위(7점 만점) × 0.3. JEV 가 없으면 게이트 점수만.
게시 48시간 뒤 실측 저장률이 옆에 붙고, `dark_jev_audit.py` 가 추측이 맞았는지 잰다.
