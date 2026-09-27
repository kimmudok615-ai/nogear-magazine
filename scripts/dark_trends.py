#!/usr/bin/env python3
"""헬스 커뮤니티·뉴스 화제 수집 — «지금 헬창들이 떠드는 것»을 소재 고르기와 훅 말투에 반영한다.
(2026-09-27 Andy: «헬창 관련 뉴스, reddit, dc인사이드 등등도 긁어와도 좋을듯»)

🔴 여기서 나오는 건 **화제 신호**다. 사실 근거가 아니다.
   숫자·주장은 여전히 팩트 원장·PubMed 초록에서만 나온다(가드). 커뮤니티 글은 «무엇이 뜨거운가»만 알려준다.

소스 (하루 한 번, 소스마다 요청 1번, 무료·키 없음)
  · Reddit      — 서브레딧 주간 인기글 RSS (r/nattyorjuice, r/moreplatesmoredates …)
  · DC인사이드   — 헬스 갤러리 개념글 목록 (robots.txt 가 막으면 건너뛴다)
  · 뉴스         — Google 뉴스 RSS (한국어 검색어)
  · X           — 무료 API 가 없다(유료 Basic 월 $200). 비용 승인 전에는 안 붙인다.

저장
  · content/dark/trends.json   (커밋됨) 어휘 목록에 있는 **낱말 빈도·축 점수만**. 글 제목·닉네임·링크 없음.
  · data/dark_trends_raw.json  (맥 로컬만, gitignore) 제목 원문 — 사람이 훑어볼 때만.
쓰는 곳
  · dark_daily: 뜨거운 축·낱말이 걸린 팩트를 먼저 고른다(최대 1.5배)
  · dark_copywriter: «요즘 커뮤니티에서 도는 말»을 훅 말투 힌트로 (금지어는 빼고)

사용: python3 scripts/dark_trends.py
"""
import datetime as dt
import html
import json
import re
import sys
import urllib.parse
import urllib.request
import urllib.robotparser
import xml.etree.ElementTree as ET
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "content" / "dark" / "trends.json"
RAW = ROOT / "data" / "dark_trends_raw.json"
UA = "Mozilla/5.0 (compatible; ngr-magazine-trends/1.0; daily topic research)"

REDDIT = ["nattyorjuice", "moreplatesmoredates", "bodybuilding", "Supplements", "Fitness"]
DC_GALLERIES = [("health", "board")]  # (갤러리 id, board|mgallery/board) — 헬스 갤러리. 늘릴 땐 여기만.
NEWS_QUERIES = ["스테로이드 헬스", "보디빌더 사망", "보충제 적발", "위고비 부작용", "내추럴 헬스 유튜버"]

# 어휘 목록 — (보여줄 말, 정규식, 축, 훅 힌트로 써도 되나)
# 여기에 있는 낱말만 센다. 목록 밖의 말(사람 이름 등)은 아예 저장하지 않는다.
TERMS = [
    ("로이더", r"로이더|roid", "drugs", True),
    ("약투", r"약투|약쟁이|약물\s*투여", "drugs", True),
    ("스테로이드", r"스테로이드|steroid|\bAAS\b|juice", "drugs", True),
    ("SARMs", r"SARMs?|사름", "drugs", True),
    ("트렌", r"트렌볼론|\btren\b", "drugs", True),
    ("TRT", r"\bTRT\b|테스토스테론|testosterone", "drugs", True),
    ("성장호르몬", r"성장호르몬|\bHGH\b|growth hormone", "drugs", True),
    ("펩타이드", r"펩타이드|peptide|BPC", "drugs", True),
    ("위고비·오젬픽", r"위고비|오젬픽|마운자로|ozempic|wegovy|semaglutide|tirzepatide|GLP-?1", "drugs", True),
    ("DNP", r"\bDNP\b", "drugs", True),
    ("내추럴", r"내추럴|내츄럴|natty", "tactics", True),
    ("가짜 내추럴", r"(가짜|페이크|페)\s*내[추츄]럴|fake natty|페내", "tactics", True),
    ("유튜버·인플루언서", r"유튜버|인플루언서|influencer|youtuber", "tactics", True),
    ("비고렉시아", r"비고렉시아|근이형|bigorexia|body dysmorphia", "tactics", True),
    ("심장", r"심장|심근|심정지|cardiac|heart attack|heart failure", "body_cost", True),
    ("급사", r"급사|돌연사|사망|숨져|died|death", "body_cost", False),  # 개인 사망은 소재 신호로만
    ("간수치", r"간수치|간 수치|liver|\bALT\b|\bAST\b", "body_cost", True),
    ("혈압", r"혈압|blood pressure|hypertension", "body_cost", True),
    ("탈모", r"탈모|hair loss|hairline", "body_cost", True),
    ("여유증", r"여유증|gyno", "body_cost", True),
    ("불임", r"불임|정자|fertility|sperm", "body_cost", True),
    ("정신·분노", r"분노|우울|불안|roid rage|depress|anxiety", "body_cost", True),
    ("보충제", r"보충제|supplement", "hidden", True),
    ("크레아틴", r"크레아틴|creatine", "hidden", True),
    ("부스터", r"부스터|프리워크|pre-?workout", "hidden", True),
    ("식약처·FDA", r"식약처|FDA|적발|회수|recall|adulterat", "hidden", True),
    ("도핑", r"도핑|doping|WADA|USADA|KADA", "sport", True),
    ("인핸스드 게임", r"인핸스드|enhanced games", "sport", True),
]


def _get(url, timeout=15):
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept-Language": "ko,en;q=0.8"})
    with urllib.request.urlopen(req, timeout=timeout) as r:  # noqa: S310 — 고정된 공개 주소만
        return r.read().decode("utf-8", errors="replace")


def _local(tag):
    return tag.rsplit("}", 1)[-1]


def parse_feed(text):
    """RSS 2.0 / Atom → 제목 목록."""
    root = ET.fromstring(text)
    return [html.unescape(e.text or "").strip() for e in root.iter() if _local(e.tag) == "title"
            and (e.text or "").strip()][1:]  # 첫 제목은 피드 자체 이름


DC_ROW = re.compile(r'<tr[^>]*class="[^"]*ub-content[^"]*"[^>]*>(.*?)</tr>', re.S)
DC_TIT = re.compile(r'<td[^>]*class="[^"]*gall_tit[^"]*"[^>]*>.*?<a[^>]*>(?:<em[^>]*></em>)?(.*?)</a>', re.S)
DC_NUM = re.compile(r'<td[^>]*class="[^"]*gall_(count|recommend)[^"]*"[^>]*>\s*([\d,]+)', re.S)


def parse_dc(text):
    """DC인사이드 목록 HTML → [(제목, 조회, 추천)]. 공지(추천·조회 없음)·닉네임은 버린다."""
    out = []
    for row in DC_ROW.findall(text):
        t = DC_TIT.search(row)
        nums = {k: int(v.replace(",", "")) for k, v in DC_NUM.findall(row)}
        if not t or "count" not in nums:
            continue
        title = html.unescape(re.sub(r"<[^>]+>", "", t.group(1))).strip()
        if title:
            out.append((title, nums.get("count", 0), nums.get("recommend", 0)))
    return out


def allowed(url, get=_get):
    """robots.txt 가 이 주소를 막으면 False — 막힌 곳은 긁지 않는다. robots 를 못 읽으면 보수적으로 False."""
    p = urllib.parse.urlparse(url)
    rp = urllib.robotparser.RobotFileParser()
    try:
        rp.parse(get(f"{p.scheme}://{p.netloc}/robots.txt").splitlines())
    except Exception:  # noqa: BLE001
        return False
    return rp.can_fetch(UA, url)


def collect(get=_get):
    """→ (소스별 {title 목록}, 소스별 상태)"""
    titles, status = {}, {}

    def run(name, fn):
        try:
            got = fn()
            titles[name] = got
            status[name] = f"{len(got)}건" if got else "0건 — 구조 바뀜/빈 목록 확인"
        except Exception as e:  # noqa: BLE001 — 한 소스가 죽어도 나머지는 돈다
            titles[name] = []
            status[name] = f"실패 {type(e).__name__}: {str(e)[:80]}"

    for sub in REDDIT:
        run(f"reddit/{sub}", lambda s=sub: parse_feed(get(f"https://www.reddit.com/r/{s}/top/.rss?t=week")))
    for gid, kind in DC_GALLERIES:
        url = f"https://gall.dcinside.com/{kind}/lists/?id={gid}&exception_mode=recommend"

        def dc(u=url):
            if not allowed(u, get):
                raise PermissionError("robots.txt 가 막음 — 건너뜀")
            return [t for t, _, _ in parse_dc(get(u))]
        run(f"dc/{gid}", dc)
    for q in NEWS_QUERIES:
        u = "https://news.google.com/rss/search?" + urllib.parse.urlencode(
            {"q": f"{q} when:7d", "hl": "ko", "gl": "KR", "ceid": "KR:ko"})
        run(f"news/{q}", lambda u=u: parse_feed(get(u)))
    status["x"] = "안 붙임 — 무료 API 없음(유료 승인 필요)"
    return titles, status


def score(titles):
    """→ (낱말 빈도, 축 점수 0~1). 글 한 건에 같은 낱말은 한 번만 센다."""
    counts = {}
    for ts in titles.values():
        for t in ts:
            for label, pat, _, _ in TERMS:
                if re.search(pat, t, re.I):
                    counts[label] = counts.get(label, 0) + 1
    axis = {}
    for label, _, ax, _ in TERMS:
        axis[ax] = axis.get(ax, 0) + counts.get(label, 0)
    top = max(axis.values() or [0])
    return dict(sorted(counts.items(), key=lambda x: -x[1])), {a: round(v / top, 2) if top else 0 for a, v in axis.items()}


def build(get=_get, out=OUT, raw=RAW, now=None):
    now = now or dt.datetime.now()
    titles, status = collect(get)
    terms, axes = score(titles)
    data = {"generated": now.isoformat(timespec="seconds"), "sources": status,
            "total_titles": sum(map(len, titles.values())), "terms": terms, "axes": axes}
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(data, ensure_ascii=False, indent=1), encoding="utf-8")
    raw.parent.mkdir(parents=True, exist_ok=True)
    raw.write_text(json.dumps({"generated": data["generated"], "titles": titles}, ensure_ascii=False, indent=1),
                   encoding="utf-8")
    return data


# ── 다른 스크립트가 쓰는 쪽 ─────────────────────────────────────
def load(path=OUT, max_age_h=72):
    """3일 넘은 화제는 쓰지 않는다(낡은 신호를 최신인 척 쓰지 않게)."""
    try:
        d = json.loads(path.read_text(encoding="utf-8"))
        age = dt.datetime.now() - dt.datetime.fromisoformat(d["generated"])
        return d if age.total_seconds() <= max_age_h * 3600 else None
    except Exception:  # noqa: BLE001
        return None


def boost(fact, trends, cap=1.5):
    """팩트 → 배수(1.0~cap). 뜨거운 축 + 제목에 걸린 뜨거운 낱말."""
    if not trends:
        return 1.0
    import dark_picker
    title = f"{fact.get('title', '')} {fact.get('notes', '')[:300]}"
    b = 1.0 + 0.25 * trends.get("axes", {}).get(dark_picker.axis_of(fact.get("title", "")) or "", 0)
    hot = list(trends.get("terms", {}))[:8]
    hits = sum(1 for label, pat, _, _ in TERMS if label in hot and re.search(pat, title, re.I))
    return round(min(cap, b + 0.1 * hits), 2)


def hint(trends, n=6):
    """훅 말투 힌트 — 금지어·개인 사망 신호는 뺀다. 없으면 빈 문자열."""
    if not trends:
        return ""
    import dark_guard
    ok = {label for label, _, _, safe in TERMS if safe}
    words = [w for w in trends.get("terms", {}) if w in ok
             and not any(re.search(p, w) for p in dark_guard.BANNED)][:n]
    return ("요즘 헬스 커뮤니티(레딧·DC 헬스갤·뉴스)에서 많이 도는 말: " + ", ".join(words)
            + ". 사실과 숫자는 FACT 에서만, 이 말들은 표지 훅의 말투·단어 선택에만 참고.") if words else ""


if __name__ == "__main__":
    sys.path.insert(0, str(Path(__file__).resolve().parent))
    d = build()
    print(f"🔥 화제 수집 {d['total_titles']}건 · 상위: "
          + ", ".join(f"{k} {v}" for k, v in list(d["terms"].items())[:6]))
    print("   소스: " + " · ".join(f"{k} {v}" for k, v in d["sources"].items()))
