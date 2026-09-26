#!/usr/bin/env python3
"""다크사이드 계정 게시 — 대기열 → 인스타 캐러셀 (Instagram Graph API, 무료).

이미 있는 것을 쓴다
  · 이미지 호스팅 = 이 저장소의 Vercel 배포 (cardnews/**/*.png 가 공개 URL 이 된다)
  · 게시 = Graph API 콘텐츠 게시 (노기어 instagram_sync.py 와 같은 v19.0)
  · 보고 = 노기어 텔레그램 봇 (TELEGRAM_BOT_TOKEN / TELEGRAM_CHAT_ID)

🔴 노기어 본계정으로 새지 않게 자격증명 이름을 따로 쓴다:
     DARK_IG_TOKEN     새 계정의 장기 토큰
     DARK_IG_USER_ID   새 계정의 Instagram 비즈니스 계정 ID
     DARK_PUBLIC_BASE  Vercel 주소 (예: https://nogear-magazine.vercel.app)
   셋 중 하나라도 없으면 아무것도 올리지 않고 끝난다.
🔴 같은 오류가 2번 연속이면 그날은 멈춘다 (차단기 — 같은 403 을 9,398번 받은 적이 있다).

사용: python3 scripts/dark_publish.py [--max 2] [--dry-run]
"""
import argparse
import json
import os
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import dark_ledger  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
QUEUE = ROOT / "data" / "dark_publish_queue.jsonl"
GRAPH = "https://graph.facebook.com/v19.0"


class PublishError(RuntimeError):
    pass


def http(method, url, params=None, timeout=30):
    data = urllib.parse.urlencode(params or {}).encode() if method == "POST" else None
    if method == "GET" and params:
        url += "?" + urllib.parse.urlencode(params)
    req = urllib.request.Request(url, data=data, method=method)
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:  # noqa: S310 — graph.facebook.com 고정
            return json.loads(r.read().decode())
    except urllib.error.HTTPError as e:
        body = e.read().decode(errors="replace")[:300]
        raise PublishError(f"HTTP {e.code}: {body}") from e
    except Exception as e:  # noqa: BLE001 — URL·네트워크 오류도 차단기가 세게 한다(추적 없이 죽지 않게)
        raise PublishError(f"{type(e).__name__}: {str(e)[:200]}") from e


def config(call=None):
    c = {k: os.getenv(k, "").strip() for k in ("DARK_IG_TOKEN", "DARK_IG_USER_ID", "DARK_PUBLIC_BASE")}
    # 계정 ID 가 숫자가 아니면 토큰으로 찾아 이번 실행에만 쓴다(키체인은 안 바꾼다 — dark_heal 참고)
    if call and c["DARK_IG_TOKEN"] and not c["DARK_IG_USER_ID"].isdigit():
        import dark_heal
        found = dark_heal.discover_ig_id(c["DARK_IG_TOKEN"], call)
        if found:
            print(f"계정 ID 형식 오류 → 토큰으로 찾은 {found} 로 이번 실행 진행 (키체인 값은 그대로)")
            c["DARK_IG_USER_ID"] = found
    missing = [k for k, v in c.items() if not v]
    # 9/26 첫 실행: 계정 ID 칸에 설치 명령이 저장돼 URL 이 깨졌다 → 모양부터 본다
    if c["DARK_IG_USER_ID"] and not c["DARK_IG_USER_ID"].isdigit():
        missing.append("DARK_IG_USER_ID(숫자여야 함 — 17841…)")
    if c["DARK_IG_TOKEN"] and (len(c["DARK_IG_TOKEN"]) < 50 or " " in c["DARK_IG_TOKEN"]):
        missing.append("DARK_IG_TOKEN(형식 이상 — 긴 토큰 문자열이어야 함)")
    return c, missing


def image_urls(item, base):
    d = ROOT / item["dir"]
    pngs = sorted(p.name for p in d.glob("[0-9][0-9]_*.png"))  # reel_card.png 제외
    if not 2 <= len(pngs) <= 10:
        raise PublishError(f"캐러셀 장수 {len(pngs)} (2~10)")
    return [f"{base.rstrip('/')}/{item['dir']}/{n}" for n in pngs]


def wait_public(urls, tries=20, delay=15, get=None):
    """Vercel 배포가 끝나 첫·끝 이미지가 열릴 때까지 기다린다."""
    get = get or (lambda u: urllib.request.urlopen(urllib.request.Request(u, method="HEAD"), timeout=15).status)  # noqa: S310
    for _ in range(tries):
        try:
            if all(get(u) == 200 for u in (urls[0], urls[-1])):
                return True
        except Exception:  # noqa: BLE001 — 아직 배포 전
            pass
        time.sleep(delay)
    return False


def publish_carousel(urls, caption, cfg, call=http, sleep=time.sleep):
    uid, tok = cfg["DARK_IG_USER_ID"], cfg["DARK_IG_TOKEN"]
    children = [call("POST", f"{GRAPH}/{uid}/media",
                     {"image_url": u, "is_carousel_item": "true", "access_token": tok})["id"] for u in urls]
    parent = call("POST", f"{GRAPH}/{uid}/media",
                  {"media_type": "CAROUSEL", "children": ",".join(children), "caption": caption,
                   "access_token": tok})["id"]
    for _ in range(12):  # 컨테이너 준비 대기 (최대 약 1분)
        st = call("GET", f"{GRAPH}/{parent}", {"fields": "status_code", "access_token": tok}).get("status_code")
        if st == "FINISHED":
            break
        if st == "ERROR":
            raise PublishError("컨테이너 ERROR")
        sleep(5)
    return call("POST", f"{GRAPH}/{uid}/media_publish", {"creation_id": parent, "access_token": tok})["id"]


def publish_reel(video_url, caption, cfg, call=http, sleep=time.sleep):
    uid, tok = cfg["DARK_IG_USER_ID"], cfg["DARK_IG_TOKEN"]
    cid = call("POST", f"{GRAPH}/{uid}/media",
               {"media_type": "REELS", "video_url": video_url, "caption": caption,
                "share_to_feed": "true", "access_token": tok})["id"]
    for _ in range(40):  # 영상 처리 대기 (최대 약 3분)
        st = call("GET", f"{GRAPH}/{cid}", {"fields": "status_code", "access_token": tok}).get("status_code")
        if st == "FINISHED":
            break
        if st == "ERROR":
            raise PublishError("릴스 컨테이너 ERROR")
        sleep(5)
    else:
        raise PublishError("릴스 처리 시간 초과")
    return call("POST", f"{GRAPH}/{uid}/media_publish", {"creation_id": cid, "access_token": tok})["id"]


def pending(queue=QUEUE, ledger=dark_ledger.LEDGER):
    if not queue.exists():
        return []
    last = dark_ledger.latest(ledger)
    items = [json.loads(x) for x in queue.read_text(encoding="utf-8").splitlines() if x.strip()]
    return [i for i in items if i.get("auto_publish") and last.get(i["id"], {}).get("state") == "queued"]


def run(max_items=2, dry=False, queue=QUEUE, ledger=dark_ledger.LEDGER, call=http, wait=wait_public):
    todo = pending(queue, ledger)[:max_items]
    cfg, missing = config(call=None if (dry or not todo) else call)
    if not todo:
        return ["대기열 비어 있음"]
    if missing and not dry:
        return [f"게시 안 함 — 자격증명 없음: {', '.join(missing)}"]
    report, last_err = [], None
    for item in todo:
        try:
            urls = image_urls(item, cfg["DARK_PUBLIC_BASE"] or "https://example.invalid")
            caption = (ROOT / item["dir"] / "caption.txt").read_text(encoding="utf-8").strip()
            if dry:
                report.append(f"(dry) {item['id']} · {len(urls)}장")
                continue
            if not wait(urls):
                raise PublishError("이미지가 아직 공개 URL 에 없음 (Vercel 배포 확인)")
            media_id = publish_carousel(urls, caption, cfg, call=call)
            extra = {}
            if item.get("reel") and os.getenv("DARK_PUBLISH_REELS", "1") != "0":
                reel_url = f"{cfg['DARK_PUBLIC_BASE'].rstrip('/')}/{item['reel']}"
                try:
                    extra["reel_media_id"] = publish_reel(reel_url, caption, cfg, call=call)
                except PublishError as e:  # 릴스 실패가 캐러셀 기록을 지우지 않게
                    report.append(f"△ {item['id']} 릴스 실패: {e}")
            dark_ledger.append(item["id"], "posted", ledger, media_id=media_id, **extra)
            report.append(f"✓ 게시 {item['id']} → {media_id}" + (f" + 릴스 {extra['reel_media_id']}" if extra else ""))
            last_err = None
        except PublishError as e:
            report.append(f"✗ {item['id']}: {e}")
            if last_err == str(e)[:60]:
                report.append("■ 같은 오류 2번 연속 — 오늘 게시 중단")
                break
            last_err = str(e)[:60]
    return report


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--max", type=int, default=2)
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()
    print("\n".join(run(a.max, a.dry_run)))


if __name__ == "__main__":
    main()
