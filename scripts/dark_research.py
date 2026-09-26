#!/usr/bin/env python3
"""다크사이드 계정 소재 공급 — PubMed 최신 초록을 1차 근거로 쌓는다 (무료, 키 없음).

왜: 소재 원장(content/editorial/factchecks.json)이 2026-06-19 이후 멈췄다. 하루 2편이면 한 달 안에 바닥난다.
어떻게: NCBI E-utilities 로 최근 N일 논문을 찾아 초록을 그대로 저장한다.
       숫자는 초록에 있는 것만 쓸 수 있고(가드가 초록과 대조), LLM 은 번역·카피만 한다.
       요약본이 아니라 원문 초록이 근거이므로 accuracy="primary" 로 표시한다.
출력: content/dark/research.json  {"facts":[{title, notes, accuracy, source, pmid, checked_at, viral_score}]}

사용: python3 scripts/dark_research.py [--days 60] [--per 8]
"""
import argparse
import datetime as dt
import json
import re
import time
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "content" / "dark" / "research.json"
EUTILS = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils"

# 축별 검색어 — 인간 대상 연구 위주. 축 이름은 dark_picker.AXES 와 맞춘다.
QUERIES = {
    "drugs": '(anabolic androgenic steroids OR SARMs OR trenbolone OR "growth hormone" misuse) AND humans[MeSH]',
    "body_cost": '(anabolic steroids OR bodybuilders) AND (cardiomyopathy OR "sudden cardiac death" OR liver OR infertility OR mortality)',
    "hidden": '(dietary supplements) AND (adulterated OR adulteration OR contamination OR "undeclared")',
    "tactics": '("muscle dysmorphia" OR "fitness influencer" OR "social media" body image) AND (men OR males)',
    "sport": '(doping OR "performance-enhancing") AND (athletes OR prevalence) AND humans[MeSH]',
}
NUM = re.compile(r"\d[\d,]*(?:\.\d+)?")


def get(url, timeout=30):
    req = urllib.request.Request(url, headers={"User-Agent": "darkside-research/1.0"})
    with urllib.request.urlopen(req, timeout=timeout) as r:  # noqa: S310 — eutils 고정
        return r.read()


def search(query, days, retmax, fetch=get):
    q = urllib.parse.urlencode({"db": "pubmed", "term": query, "retmode": "json", "retmax": retmax,
                                "sort": "pub_date", "datetype": "pdat", "reldate": days})
    return json.loads(fetch(f"{EUTILS}/esearch.fcgi?{q}"))["esearchresult"].get("idlist", [])


def abstracts(pmids, fetch=get):
    if not pmids:
        return []
    q = urllib.parse.urlencode({"db": "pubmed", "id": ",".join(pmids), "retmode": "xml"})
    root = ET.fromstring(fetch(f"{EUTILS}/efetch.fcgi?{q}"))
    out = []
    for art in root.iter("PubmedArticle"):
        pmid = art.findtext(".//PMID")
        title = "".join(art.find(".//ArticleTitle").itertext()).strip() if art.find(".//ArticleTitle") is not None else ""
        abst = " ".join("".join(a.itertext()).strip() for a in art.iter("AbstractText"))
        journal = art.findtext(".//Journal/Title") or ""
        types = {t.text or "" for t in art.iter("PublicationType")}
        out.append({"pmid": pmid, "title": title, "abstract": abst, "journal": journal, "types": types})
    return out


def score(a):
    """볼 만한 정도 — 규모 큰 근거(메타분석·코호트)와 숫자가 많은 초록을 앞에."""
    s = 70
    if {"Meta-Analysis", "Systematic Review"} & a["types"]:
        s += 15
    if re.search(r"cohort|registry|nationwide|\d{3,}\s*(participants|patients|men|users|individuals)", a["abstract"], re.I):
        s += 8
    if {"Case Reports"} & a["types"]:
        s -= 10   # 개인 증례는 뒤로 (개인 사망 소재 회피와 같은 이유)
    s += min(7, len(NUM.findall(a["abstract"])) // 3)
    return s


def usable(a):
    return len(a["abstract"]) >= 400 and len(NUM.findall(a["abstract"])) >= 3 and "Retracted Publication" not in a["types"]


def collect(days=60, per=8, fetch=get, pause=0.4):
    today = dt.date.today().isoformat()
    facts = []
    for axis, q in QUERIES.items():
        try:
            ids = search(q, days, per, fetch)
            time.sleep(pause)  # NCBI 무키 한도(초당 3회) 지키기
            arts = abstracts(ids, fetch)
            time.sleep(pause)
        except Exception as e:  # noqa: BLE001 — 한 축이 실패해도 나머지는 쌓는다
            print(f"✗ {axis}: {type(e).__name__}: {e}")
            continue
        for a in filter(usable, arts):
            facts.append({
                "title": f"[{axis}] {a['title']}",
                "notes": f"{a['journal']} (PMID {a['pmid']}). 초록: {a['abstract']}",
                "accuracy": "primary",
                "source": f"https://pubmed.ncbi.nlm.nih.gov/{a['pmid']}/",
                "pmid": a["pmid"],
                "checked_at": today,
                "viral_score": score(a),
            })
    return facts


def merge(new, path=OUT):
    """PMID 기준으로 합친다. 기존 항목은 지우지 않는다."""
    old = json.loads(path.read_text(encoding="utf-8")).get("facts", []) if path.exists() else []
    seen = {f["pmid"] for f in old}
    added = [f for f in new if f["pmid"] not in seen]
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps({"updated": dt.date.today().isoformat(), "facts": old + added},
                               ensure_ascii=False, indent=1), encoding="utf-8")
    return len(added), len(old) + len(added)


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--days", type=int, default=60)
    ap.add_argument("--per", type=int, default=8)
    a = ap.parse_args()
    added, total = merge(collect(a.days, a.per))
    print(f"연구 소재 +{added} (총 {total}) → {OUT.relative_to(ROOT)}")
