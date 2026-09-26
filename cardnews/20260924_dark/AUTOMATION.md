# 다크사이드 계정 — 자동화 설계안 (v2, 2026-09-24)

목표: 단독 계정 @ngr_magazine (크리에이터)에 **매일 캐러셀 2편**을 사람 손 없이 내보낸다.
원칙: 사실은 원장에서만 · 판단은 코드→JEV→LLM 순 · 외부 게시는 항상 승인 뒤.

## 1. 흐름 (입력 → 처리 → 출력 → 승인게이트)

| # | 단계 | 입력 | 처리 (담당) | 출력 | 게이트 |
|---|---|---|---|---|---|
| 1 | 소재 고르기 | `content/editorial/factchecks.json`, 주간 피처, `social-plan.json` | `dark_topic_picker.py` (코드): accuracy=`match` 만, 최근 30일 안 쓴 것, 시리즈 5축 순환 | 후보 3건 | 자동 |
| 2 | 안전 등급 | 후보 fact | `judgment_chain.judge()` 새 레인 `dark_topic_safety` (🟢/🟡/🔴) — **섀도우로 시작** | 등급 | 🔴 → 탈락, 🟡 → 승인카드에 표시 |
| 3 | 기획·카피 | 🟢/🟡 fact + 포맷 규칙(README) | ChatGPT Luna(생성) → 어려운 것만 Sol. Claude 는 폴백 | `content/dark/series/<id>.json` (현 `SERIES` 스키마) | 자동 |
| 4 | 가드 | series JSON | `dark_guard.py` (코드, 결정적) — 아래 §3 | PASS / HOLD + 사유 | HOLD 면 멈춤 |
| 5 | 비주얼 | 커버·릴스 프롬프트 | Higgsfield GPT Image 2.5(커버 4:5, 릴스 프레임 9:16) → Kling 3.0 pro 5s 무음 | `higgsfield/manifest.json` + 파일 | 주간 크레딧 상한 |
| 6 | 렌더 | series JSON + 이미지 | `generate_dark_cardnews.py --series <json>` | 카드 PNG, caption, meta | 자동 |
| 7 | 승인 | 미리보기·팩트근거·캡션 | 텔레그램 승인 카드 (`apply_approvals.py` 패턴) | approved / rejected + 수정요청 | **Andy 1탭** |
| 8 | 게시 | 승인된 묶음 | P2: 수동 업로드 / P3: Graph API 예약 게시 | 게시 ID | 승인 없으면 불가 |
| 9 | 측정 | 게시 ID | `reels_tracker.py`·`aside_ig_posts.py` 방식 | 저장·공유·도달 | — |
| 10 | 학습 | 측정치 | 훅 유형·시리즈별 저장률 → picker 가중치 | `data/dark_learning.json` | 자동 |

## 2. 원장 — `data/dark_ledger.jsonl` (append-only)
한 줄 = 한 콘텐츠의 상태 변화.
`picked → graded → drafted → guarded → visual → rendered → awaiting_approval → approved → posted → measured`
- 필드: `id, series, fact_ids[], state, at, owner, cost{hf_credits, llm_usd}, hold_reason`
- 같은 fact 재사용 금지는 원장으로 판정. 멈춘 건(>48h) 자동 재실행하지 않고 stale 로 표시.

## 3. 가드 규칙 (`dark_guard.py`, LLM 없이)
1. 슬라이드의 **모든 숫자**가 연결된 fact 의 제목/노트에 존재 → 없으면 HOLD.
2. fact 의 accuracy 가 `wrong`/`unclear` → HOLD. `partial` 은 노트의 정정 문구를 따랐는지 확인.
3. 금지어: 용량 단위(mg/ml/IU/주당), 사이클·PCT·스택·구매·직구·추천 제품명 → HOLD.
4. 실명: 화이트리스트(본인 공개 인정 + 주요 매체) 밖의 인명 → HOLD.
5. 마지막 장 `kind=end` 이고 방어/출구 문장 있음.
6. 정신건강 수치가 있으면 도움 문구 필수.
7. 사망 사례에 인과 단정 표현(“~때문에 죽었다”) → HOLD.

## 4. 비용 (현재 단가 기준)
| 항목 | 단가 | 주간(3+3) |
|---|---|---|
| 커버 이미지 GPT Image 2.5 high 2k | 2.75 cr | 8.25 |
| 릴스 프레임 + Kling 3.0 pro 5s | 10.25 cr | 30.75 |
| 합계 | | **≈ 39 cr/주 (≈ 170 cr/월)** |
| 카피 생성 | ChatGPT 구독 내 | 0 |
| 안전 등급 | JEV/로컬 LLM | ≈ 0 |
제안 상한: **주 60 크레딧** (재생성 여유 포함). 넘으면 멈추고 보고.

## 5. 단계별 도입
- **P1 — 로컬 코드 (승인 불필요, 바로 가능)**
  생성기를 series JSON 입력으로 분리 · `dark_guard.py` · 원장 · picker · 테스트(가드 7규칙, 숫자 대조, 원장 상태 전이).
- **P2 — 반자동 (승인 필요)**
  JEV 레인 `dark_topic_safety` 섀도우 추가 · Higgsfield 주간 상한 · 로컬 러너에 하루 1회 편입(새 스케줄) · 텔레그램 승인 카드 · 게시는 사람이 업로드.
- **P3 — 자동 게시 (별도 승인)**
  새 계정 개설·비즈니스 전환 · Meta Graph API 토큰(자격증명) · 승인된 묶음만 예약 게시.

## 6. 결정 (2026-09-24 Andy)
- NOGEAR 브랜드 빼고 단독 계정으로 시작 (`--brand neutral`, NOGEAR 판은 `--brand nogear`)
- 매일 캐러셀 2편부터 (릴스는 뒤로)
- 카피는 로컬 GPT 우선: aside Codex Luna → 맥미니 qwen3:8b → 둘 다 실패면 그날 멈춤(유료 대체 없음)
- **승인 없이 자동 게시** → `dark_guard.py` 가 유일한 문. HOLD 는 고치지 않고 버린다.

## P1 구현 (완료)
| 파일 | 역할 |
|---|---|
| `scripts/dark_picker.py` | match 팩트만 · 30일 재사용 금지 · 허용 밖 실명/개인 사망 기사/다투는 숫자 제외 · 축 중복 없이 |
| `scripts/dark_copywriter.py` | 팩트 → 캐러셀 JSON (aside Luna → 로컬 LLM) |
| `scripts/dark_guard.py` | 가드 7규칙 |
| `scripts/dark_ledger.py` | 원장 `data/dark_ledger.jsonl` (모델 꺼짐·렌더 실패는 팩트를 태우지 않음) |
| `scripts/dark_daily.py` | 하루치 실행 → `cardnews/<날짜>_dark_auto/` + 게시 대기열 `data/dark_publish_queue.jsonl` |
| `ops/com.darkside.daily.plist` | 매일 08:30 launchd 템플릿 (맥에서 설치) |
| `tests/test_dark_pipeline.py` | 가드·원장·picker·카피 파싱·하루치 |

## 아직 없는 것
- 인스타 업로드(대기열 → 게시): 계정 개설 + Meta 토큰 필요
- 하루치 커버 이미지는 스톡 5장 순환 (Higgsfield 자동 생성은 스크립트용 API 필요)

## (이전) Andy 결정 필요
1. 계정 개설과 핸들(`@nogear.dark` 안)
2. 빈도 — 주 3+3 안 / 다른 안
3. Higgsfield 주간 상한 — 60 크레딧 안
4. 게시 방식 — P2 수동으로 시작 → 4주 뒤 P3 판단 안
5. GitHub 권한 연결(현재 push 403) — 자동화 코드가 올라가야 러너가 돈다

## 7. 멈춤 조건
- 가드 HOLD 3회 연속, 크레딧 상한 도달, 승인 48시간 무응답, 게시 후 신고/제재 신호 → 파이프라인 정지 + 보고(사유·쓴 범위·다음 조치).

## 연결 지도 (2026-09-25) — 새로 짓지 않고 이미 있는 것을 쓴다
| 단계 | 쓰는 것 | 비용 | 상태 |
|---|---|---|---|
| 소재 | `content/editorial/factchecks.json` (매거진 팩트체크 원장) | 0 | ✅ 연결 |
| 카피 | aside → Codex Luna (ChatGPT 구독) · 맥미니 ollama qwen3:8b | 0 | ✅ 코드 연결 · 맥에서 첫 실행 확인 필요 |
| 가드 | `dark_guard.py` | 0 | ✅ |
| 카드 렌더 | Playwright + 크로미움 (맥 로컬) | 0 | ✅ |
| 이미지 호스팅 | 매거진 Vercel 배포 (`vercel.json` 에 `cardnews/**/*.png` 추가) | 0 | ✅ PR 병합 후 |
| 게시 | Instagram Graph API 콘텐츠 게시 (`dark_publish.py`) | 0 | ⏳ 새 계정 자격증명 필요 |
| 보고 | 노기어 텔레그램 봇 (`dark_notify.py`, `.env.cafe24` 재사용) | 0 | ✅ |
| 스케줄 | 맥 launchd `ops/com.darkside.daily.plist` → `ops/dark_daily.sh` | 0 | ⏳ 맥에서 설치 |
| 커버 이미지(선택) | Higgsfield GPT Image 2.5 (크레딧) · Canva 무료 | 2.75cr/장 | 수동 |

### Andy 가 직접 해야 하는 것 (계정·자격증명은 대신 못 만든다)
1. 인스타 새 계정 개설 → 프로페셔널(크리에이터/비즈니스) 전환
2. 페이스북 페이지 하나 만들고 그 계정과 연결
3. developers.facebook.com 에서 앱 생성(무료) → 권한 `instagram_basic`, `instagram_content_publish`, `pages_show_list`
4. 장기 토큰 발급 → 계정 ID 조회 (방법은 노기어 `scripts/instagram_sync.py` 머리말과 같다)
5. 맥 셸 환경에 `DARK_IG_TOKEN`, `DARK_IG_USER_ID` 등록 (노기어 본계정 `INSTAGRAM_*` 와 이름이 다르다 — 섞이지 않게)
6. 이 PR 병합 → 맥 `~/nogear-magazine` 을 main 으로 → plist 설치

## 성장 자동화 (2026-09-26)
| 무엇 | 어떻게 | 파일 |
|---|---|---|
| 소재 자가 보충 | 매일 아침 PubMed 최근 60일 초록을 축별로 수집 → `accuracy=primary`. 숫자는 초록에 있는 것만 통과(가드) | `scripts/dark_research.py` → `content/dark/research.json` |
| 게시 시간 분산 | 08:30 생성+1편, 19:30 나머지 1편 (하루 두 번 노출) | `ops/com.darkside.daily.plist`, `ops/dark_daily.sh [daily\|publish]` |
| 캡션 | 원문 링크(PubMed) + 축별 해시태그 5개 | `dark_daily.assemble` |
| 학습 | 48시간 뒤 저장률 → 축 가중치 (기존) + 팔로워·게시물 수 일일 스냅샷 | `dark_measure.py` → `data/dark_account.jsonl` |
| 원격 확인 | 매 실행 보고를 `ops/status/last_run_{daily,publish}.txt` 로 push | `ops/dark_daily.sh` |
| 자격증명 검사 | 계정 ID 숫자·토큰 형식이 아니면 게시 시도 전에 멈춤 (9/26 첫 실행 원인) | `dark_publish.config`, `install_mac.sh` |

하지 않는 것: 댓글·DM 자동 답장, 팔로우/좋아요 자동화(계정 제재 위험·외부 메시지), 유료 광고.
