#!/usr/bin/env python3
"""다크사이드 계정 자격증명 점검 — 읽기만 한다(키체인·launchd 는 건드리지 않는다).

9/26 첫 실행: 키체인의 계정 ID 칸에 설치 명령이 저장돼 게시가 실패했다.
계정 ID 는 토큰만 있으면 Graph API 로 찾을 수 있으므로, 잘못돼 있으면 **이번 실행에서만**
찾은 값을 쓴다. 저장소(키체인) 수정은 사람이 한다 — 자동으로 자격증명을 고쳐 쓰지 않는다.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import dark_publish  # noqa: E402


def discover_ig_id(token, call=dark_publish.http):
    """토큰만으로 인스타 비즈니스/크리에이터 계정 ID 를 찾는다. 못 찾으면 None."""
    g = dark_publish.GRAPH
    for path in ("me", "me/accounts"):
        try:
            d = call("GET", f"{g}/{path}", {"fields": "instagram_business_account", "access_token": token})
        except dark_publish.PublishError:
            continue
        for node in [d] + list(d.get("data", [])):
            iid = (node.get("instagram_business_account") or {}).get("id")
            if iid:
                return iid
    return None


def check_token(token, call=dark_publish.http):
    """→ (서버가 받아주나?, 사유)"""
    try:
        call("GET", f"{dark_publish.GRAPH}/me", {"fields": "id", "access_token": token})
        return True, "토큰 정상"
    except dark_publish.PublishError as e:
        return False, f"토큰을 서버가 거절 — 만료/취소, 새 토큰 필요: {str(e)[:120]}"
