#!/usr/bin/env python3
"""모든 에셋을 Canva 에 쌓는다 — 2026-09-27 Andy «모든 에셋 캔바에 축적».

매일 러너 끝에 돈다: 렌더된 카드(표지·본문·대안 표지)·캐릭터 이미지·표지 모음을
Canva 계정의 «NGR 다크사이드 에셋» 폴더에 올린다. 이미 올린 건 다시 안 올린다(data/canva_synced.json).
Canva Connect API(무료) — asset-uploads + folders. 같은 파일은 이름으로 찾기 쉽게: <날짜>_<편>_<카드>.png

자격증명(파일·저장소에 두지 않는다 — 처음 한 번 사람이):
  1) canva.com/developers → 통합 만들기 → 권한 asset:write · folder:read · folder:write
     리디렉트 URL: http://127.0.0.1:8765/callback
  2) 맥 키체인에 CANVA_CLIENT_ID · CANVA_CLIENT_SECRET (service=darkside) — ops/install_mac.sh 와 같은 방식
  3) python3 scripts/dark_canva_sync.py --auth   (브라우저에서 한 번 허용 → 새로고침 토큰 저장)
새로고침 토큰은 Canva 가 쓸 때마다 바꿔 주므로 data/.canva_token.json(권한 600, gitignore)에 이어 적는다.
자격증명이 없으면 아무것도 안 올리고 한 줄 보고만 한다(하루치는 안 멈춘다).

사용: python3 scripts/dark_canva_sync.py [--max 150] [--dry-run] | --auth
"""
import argparse
import base64
import datetime as dt
import hashlib
import json
import os
import secrets
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
API = "https://api.canva.com/rest/v1"
LEDGER = ROOT / "data" / "canva_synced.json"
TOKEN = ROOT / "data" / ".canva_token.json"
FOLDER_NAME = "NGR 다크사이드 에셋"
REDIRECT = "http://127.0.0.1:8765/callback"
SCOPES = "asset:write folder:read folder:write"
PAUSE = 2.2  # 업로드 한도(분당 30건 수준) 아래로


class CanvaError(RuntimeError):
    pass


def http(method, url, headers=None, data=None, timeout=60):
    req = urllib.request.Request(url, data=data, method=method, headers=headers or {})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:  # noqa: S310 — api.canva.com 고정
            body = r.read().decode()
            return json.loads(body) if body else {}
    except urllib.error.HTTPError as e:
        raise CanvaError(f"HTTP {e.code}: {e.read().decode(errors='replace')[:200]}") from e
    except Exception as e:  # noqa: BLE001
        raise CanvaError(f"{type(e).__name__}: {str(e)[:160]}") from e


def assets(root=ROOT):
    """올릴 파일 목록 → [(Canva 이름, 경로)]. 카드 PNG·대안 표지·표지 모음·캐릭터."""
    out = []
    for d in sorted((root / "cardnews").glob("*_dark_*/*/")):
        day = d.parent.name.split("_")[0]
        for p in sorted(d.glob("*.png")):
            out.append((f"{day}_{d.name}_{p.stem}.png", p))
    for p in sorted((root / "cardnews").glob("*_dark_*/contact_sheet.png")):
        out.append((f"{p.parent.name}_contact_sheet.png", p))
    for p in sorted((root / "cardnews" / "assets" / "characters").glob("*.png")):
        out.append((f"character_{p.stem}.png", p))
    return out


def _load(path, default):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception:  # noqa: BLE001
        return default


def _save(path, obj, private=False):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, ensure_ascii=False, indent=1), encoding="utf-8")
    if private:
        os.chmod(path, 0o600)


def _basic(cid, secret):
    return "Basic " + base64.b64encode(f"{cid}:{secret}".encode()).decode()


def access_token(call=http, token_path=TOKEN):
    """키체인(환경변수)의 CLIENT_ID/SECRET + 저장된 새로고침 토큰 → 접근 토큰. 없으면 None."""
    cid, sec = os.getenv("CANVA_CLIENT_ID", "").strip(), os.getenv("CANVA_CLIENT_SECRET", "").strip()
    tok = _load(token_path, {})
    if not (cid and sec and tok.get("refresh_token")):
        return None
    r = call("POST", f"{API}/oauth/token",
             {"Authorization": _basic(cid, sec), "Content-Type": "application/x-www-form-urlencoded"},
             urllib.parse.urlencode({"grant_type": "refresh_token", "refresh_token": tok["refresh_token"]}).encode())
    _save(token_path, {"refresh_token": r.get("refresh_token", tok["refresh_token"]),
                       "at": dt.datetime.now().isoformat(timespec="seconds")}, private=True)
    return r["access_token"]


def folder_id(tok, ledger, call=http):
    if ledger.get("folder_id"):
        return ledger["folder_id"]
    r = call("POST", f"{API}/folders", {"Authorization": f"Bearer {tok}", "Content-Type": "application/json"},
             json.dumps({"name": FOLDER_NAME, "parent_folder_id": "root"}).encode())
    ledger["folder_id"] = r["folder"]["id"]
    return ledger["folder_id"]


def upload(tok, name, path, call=http, sleep=time.sleep):
    meta = json.dumps({"name_base64": base64.b64encode(name.encode()).decode()})
    r = call("POST", f"{API}/asset-uploads", {"Authorization": f"Bearer {tok}", "Content-Type": "application/octet-stream",
                                               "Asset-Upload-Metadata": meta}, path.read_bytes())
    job = r["job"]
    for _ in range(20):
        if job.get("status") == "success":
            return job["asset"]["id"]
        if job.get("status") == "failed":
            raise CanvaError(f"업로드 실패: {job.get('error', {}).get('message', '?')}")
        sleep(1.5)
        job = call("GET", f"{API}/asset-uploads/{job['id']}", {"Authorization": f"Bearer {tok}"})["job"]
    raise CanvaError("업로드 시간 초과")


def run(max_items=150, dry=False, root=ROOT, ledger_path=LEDGER, call=http, sleep=time.sleep, token=None):
    ledger = _load(ledger_path, {"synced": {}})
    todo = [(n, p) for n, p in assets(root) if n not in ledger["synced"]][:max_items]
    if not todo:
        return ["Canva: 새 에셋 없음"]
    if dry:
        return [f"Canva (dry): 올릴 것 {len(todo)}개 — 예) {todo[0][0]}"]
    try:
        tok = token or access_token(call)
    except CanvaError as e:
        return [f"Canva 동기화 안 함 — 토큰 갱신 실패(다시 --auth): {e}"]
    if not tok:
        return [f"Canva 동기화 안 함 — 자격증명 없음 (대기 {len(todo)}개). scripts/dark_canva_sync.py 머리말 1~3단계"]
    fid = folder_id(tok, ledger, call)
    done, fails = 0, []
    for name, p in todo:
        try:
            aid = upload(tok, name, p, call, sleep)
            call("POST", f"{API}/folders/move", {"Authorization": f"Bearer {tok}", "Content-Type": "application/json"},
                 json.dumps({"to_folder_id": fid, "item_id": aid}).encode())
            ledger["synced"][name] = {"asset_id": aid, "at": dt.datetime.now().isoformat(timespec="seconds")}
            done += 1
        except CanvaError as e:
            fails.append(f"{name}: {e}")
            if len(fails) >= 2 and fails[-1].split(": ", 1)[1][:40] == fails[-2].split(": ", 1)[1][:40]:
                break  # 같은 오류 2번 연속이면 멈춘다
        _save(ledger_path, ledger)
        sleep(PAUSE)
    _save(ledger_path, ledger)
    left = len([n for n, _ in assets(root) if n not in ledger["synced"]])
    return [f"🎨 Canva «{FOLDER_NAME}» 에 {done}개 올림 · 남은 것 {left}" + (f" · 실패 {len(fails)}: {fails[-1][:120]}" if fails else "")]


def auth():
    """처음 한 번 — 브라우저 허용 → 코드 → 새로고침 토큰 저장 (PKCE)."""
    import http.server
    import webbrowser
    cid, sec = os.getenv("CANVA_CLIENT_ID", "").strip(), os.getenv("CANVA_CLIENT_SECRET", "").strip()
    if not (cid and sec):
        sys.exit("CANVA_CLIENT_ID / CANVA_CLIENT_SECRET 이 없다 (키체인 service=darkside)")
    verifier = secrets.token_urlsafe(64)
    challenge = base64.urlsafe_b64encode(hashlib.sha256(verifier.encode()).digest()).rstrip(b"=").decode()
    state = secrets.token_urlsafe(16)
    url = "https://www.canva.com/api/oauth/authorize?" + urllib.parse.urlencode({
        "response_type": "code", "client_id": cid, "redirect_uri": REDIRECT, "scope": SCOPES,
        "code_challenge": challenge, "code_challenge_method": "S256", "state": state})
    got = {}

    class H(http.server.BaseHTTPRequestHandler):
        def do_GET(self):  # noqa: N802
            q = urllib.parse.parse_qs(urllib.parse.urlparse(self.path).query)
            got.update({k: v[0] for k, v in q.items()})
            self.send_response(200)
            self.end_headers()
            self.wfile.write("Canva 연결 완료 — 창을 닫아도 된다".encode())

        def log_message(self, *a):
            pass

    print("브라우저에서 허용:", url)
    webbrowser.open(url)
    http.server.HTTPServer(("127.0.0.1", 8765), H).handle_request()
    if got.get("state") != state or "code" not in got:
        sys.exit(f"허용 실패: {got}")
    r = http("POST", f"{API}/oauth/token",
             {"Authorization": _basic(cid, sec), "Content-Type": "application/x-www-form-urlencoded"},
             urllib.parse.urlencode({"grant_type": "authorization_code", "code": got["code"],
                                     "code_verifier": verifier, "redirect_uri": REDIRECT}).encode())
    _save(TOKEN, {"refresh_token": r["refresh_token"], "at": dt.datetime.now().isoformat(timespec="seconds")}, private=True)
    print("✓ Canva 연결됨 — 매일 러너가 에셋을 올린다")


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--max", type=int, default=150)
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--auth", action="store_true")
    a = ap.parse_args()
    if a.auth:
        auth()
    else:
        print("\n".join(run(a.max, a.dry_run)))
