"""다크사이드 계정 파이프라인 — 가드 7규칙 · 원장 · 소재 고르기 · 하루치 실행."""
import datetime as dt
import json
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))
import dark_copywriter  # noqa: E402
import dark_daily  # noqa: E402
import dark_guard  # noqa: E402
import dark_ledger  # noqa: E402
import dark_picker  # noqa: E402

FACT = {"title": "SARMs 혈액검사: ALT 29.5→125.6, HDL 44.5→31.1", "accuracy": "match",
        "notes": "JMIR 1,700건 자가보고. 테스토스테론 585.5→358.6.", "viral_score": 90}
FID = dark_guard.fact_id(FACT["title"])
FACTS = {
    FID: FACT,
    dark_guard.fact_id("보충제 500개 이상 FDA 적발"): {"title": "보충제 500개 이상 FDA 적발", "accuracy": "match",
                                                   "notes": "Harvard Health", "viral_score": 89},
    dark_guard.fact_id("DNP 사망률 11.9%"): {"title": "DNP 사망률 11.9%", "accuracy": "wrong", "notes": ""},
    dark_guard.fact_id("DNP 치사율 11.9% 확정"): {"title": "DNP 치사율 11.9% 확정", "accuracy": "match",
                                              "notes": "", "viral_score": 99},
    dark_guard.fact_id("잭슨 티펫 심장마비 사망"): {"title": "잭슨 티펫 심장마비 사망", "accuracy": "match",
                                              "notes": "", "viral_score": 98},
}


def good_series(**over):
    s = {
        "id": "drugs_x", "tag": "SARMs", "bg": "syringe.jpg", "fact_ids": [FID],
        "slides": [
            {"kind": "cover", "kicker": "BLOOD WORK", "text": "‘안전하다’던 약이\n*절대* 말 안 하는 3가지"},
            {"kind": "stat", "num": "29.5→125.6", "label": "간수치 ALT", "src": "JMIR"},
            {"kind": "stat", "num": "44.5→31.1", "label": "HDL", "src": "JMIR"},
            {"kind": "line", "text": "‘연구용’ 라벨은\n*당신*을 위한 게 아니다."},
            {"kind": "end", "text": "‘안전한 약물’은\n*마케팅 용어*다.", "cta": "저장."},
        ],
        "caption": ["SARM 사용 전→후 ALT 29.5→125.6", "출처: JMIR 1,700건", "이거 알고 있었나?"],
    }
    s.update(over)
    return s


# ── 가드 ─────────────────────────────────────────────
def test_guard_passes_clean_series():
    ok, why = dark_guard.check(good_series(), FACTS)
    assert ok, why


def test_guard_holds_invented_number():
    s = good_series()
    s["slides"][3]["text"] = "사용자의 73%가 후회한다."
    ok, why = dark_guard.check(s, FACTS)
    assert not ok and any("73" in w for w in why)


def test_guard_allows_small_integers():
    s = good_series()
    s["slides"][3]["text"] = "8주면 충분하다고 말한다."
    assert dark_guard.check(s, FACTS)[0]


@pytest.mark.parametrize("text", ["하루 20mg 이면 된다", "PCT 는 이렇게", "직구 사이트", "사이클 추천"])
def test_guard_holds_banned(text):
    s = good_series()
    s["slides"][3]["text"] = text
    assert not dark_guard.check(s, FACTS)[0]


def test_guard_holds_non_match_fact():
    s = good_series(fact_ids=[dark_guard.fact_id("DNP 사망률 11.9%")])
    s["slides"] = [s["slides"][0], s["slides"][3], s["slides"][4], s["slides"][3], s["slides"][3]]
    s["caption"] = []
    ok, why = dark_guard.check(s, FACTS)
    assert not ok and any("wrong" in w for w in why)


def test_guard_holds_unknown_fact_and_no_fact():
    assert not dark_guard.check(good_series(fact_ids=["deadbeef00"]), FACTS)[0]
    assert not dark_guard.check(good_series(fact_ids=[]), FACTS)[0]


def test_guard_holds_watched_name_allows_allowed_name():
    s = good_series()
    s["slides"][3]["text"] = "잭슨 티펫처럼"
    assert not dark_guard.check(s, FACTS)[0]
    s["slides"][3]["text"] = "리버 킹의 몸은 이야기였다"
    assert dark_guard.check(s, FACTS)[0]


def test_guard_holds_causal_death():
    s = good_series()
    s["slides"][3]["text"] = "스테로이드 때문에 그는 사망했다"
    assert not dark_guard.check(s, FACTS)[0]


def test_guard_mental_health_needs_109():
    s = good_series()
    s["slides"][3]["text"] = "자살 충동이 늘었다"
    assert not dark_guard.check(s, FACTS)[0]
    s["caption"].append("힘들면 109 (자살예방상담)")
    assert dark_guard.check(s, FACTS)[0]


def test_guard_structure():
    s = good_series()
    s["slides"] = s["slides"][:-1]
    assert not dark_guard.check(s, FACTS)[0]
    s = good_series()
    s["slides"][-1].pop("cta")
    assert not dark_guard.check(s, FACTS)[0]


# ── 원장 ─────────────────────────────────────────────
def test_ledger_roundtrip_and_reuse_window(tmp_path):
    p = tmp_path / "l.jsonl"
    dark_ledger.append("a", "picked", p, fact_ids=["f1"])
    dark_ledger.append("a", "queued", p)
    p.open("a").write("깨진 줄\n")
    assert dark_ledger.latest(p)["a"]["state"] == "queued"
    assert dark_ledger.used_fact_ids(path=p) == {"f1"}
    assert dark_ledger.used_fact_ids(path=p, today=dt.date.today() + dt.timedelta(days=31)) == set()
    with pytest.raises(ValueError):
        dark_ledger.append("a", "모름", p)


# ── 소재 고르기 ──────────────────────────────────────
def test_picker_skips_contested_names_and_duplicate_axes(tmp_path):
    picks = dark_picker.pick(count=5, facts=FACTS, ledger=tmp_path / "l.jsonl")
    titles = [p["fact"]["title"] for p in picks]
    assert "DNP 치사율 11.9% 확정" not in titles      # wrong 팩트와 같은 숫자
    assert "잭슨 티펫 심장마비 사망" not in titles     # 허용 밖 실명
    assert len({p["axis"] for p in picks}) == len(picks)
    assert FACT["title"] in titles


def test_picker_respects_ledger(tmp_path):
    p = tmp_path / "l.jsonl"
    dark_ledger.append("x", "picked", p, fact_ids=[FID])
    assert FID not in [c["fact_id"] for c in dark_picker.pick(5, FACTS, p)]


# ── 카피 파싱 ─────────────────────────────────────────
def test_extract_json_from_noisy_reply():
    reply = '생각중 <think>{"x":1}</think> 여기 {"tag":"T","slides":[{"kind":"cover"}],"caption":[]} 끝'
    assert dark_copywriter.extract_json(reply)["tag"] == "T"
    assert dark_copywriter.extract_json("JSON 없음") is None


def test_writer_falls_through_providers(monkeypatch):
    monkeypatch.delenv("DARK_LLM", raising=False)
    monkeypatch.setitem(dark_copywriter.PROVIDERS, "aside", lambda p: (_ for _ in ()).throw(RuntimeError("off")))
    monkeypatch.setitem(dark_copywriter.PROVIDERS, "local", lambda p: json.dumps({"tag": "T", "slides": [1]}))
    obj, model, errs = dark_copywriter.write(FACT)
    assert model == "local" and obj["tag"] == "T" and "aside" in errs[0]


def test_writer_returns_none_when_all_fail(monkeypatch):
    monkeypatch.setitem(dark_copywriter.PROVIDERS, "aside", lambda p: "")
    monkeypatch.setitem(dark_copywriter.PROVIDERS, "local", lambda p: "")
    obj, model, errs = dark_copywriter.write(FACT, order=["aside", "local"])
    assert obj is None and model is None and len(errs) == 2


# ── 하루치 ───────────────────────────────────────────
def test_daily_makes_count_and_skips_held(tmp_path, monkeypatch):
    monkeypatch.setattr(dark_daily.gen, "CARDNEWS", tmp_path / "cardnews")
    monkeypatch.setattr(dark_daily.gen, "ROOT", tmp_path)
    good = good_series()

    def writer(fact):
        if fact is FACT:
            return {"tag": "SARMs", "slides": good["slides"], "caption": good["caption"]}, "stub", []
        bad = [dict(x) for x in good["slides"]]
        bad[3] = {"kind": "line", "text": "직구 링크는 프로필에"}
        return {"tag": "X", "slides": bad, "caption": []}, "stub", []

    made, report = dark_daily.run(count=2, date="20990101", png=False, facts=FACTS,
                                  ledger=tmp_path / "l.jsonl", queue=tmp_path / "q.jsonl", writer=writer)
    assert len(made) == 1 and any("HOLD" in r for r in report)
    states = [r["state"] for r in dark_ledger.rows(tmp_path / "l.jsonl")]
    assert "held" in states and states.count("queued") == 1
    q = [json.loads(x) for x in (tmp_path / "q.jsonl").read_text().splitlines()]
    assert q[0]["auto_publish"] is True
    d = tmp_path / q[0]["dir"]
    assert (d / "00_cover.html").exists() and (d / "series.json").exists()


def test_picker_skips_individual_death_keeps_cohort():
    assert dark_picker.individual_death("열아홉, 심장이 먼저 멈췄다 — 브라질 보디빌더 돌연사")
    assert dark_picker.individual_death("22세 보디빌딩 인플루언서 사망")
    assert not dark_picker.individual_death("121명의 죽은 보디빌더 — 38%가 급성심장사")
    assert not dark_picker.individual_death("프로 보디빌더 급성심장사 위험 5배 — 연구")


def test_copy_failure_does_not_burn_fact(tmp_path):
    p = tmp_path / "l.jsonl"
    dark_ledger.append("a", "picked", p, fact_ids=["f1"])
    dark_ledger.append("a", "copy_failed", p)
    dark_ledger.append("b", "picked", p, fact_ids=["f2"])
    dark_ledger.append("b", "held", p)
    assert dark_ledger.used_fact_ids(path=p) == {"f2"}


def test_daily_stops_when_no_model(tmp_path):
    def dead(fact):
        return None, None, ["aside: ModuleNotFoundError", "local: URLError"]
    made, report = dark_daily.run(count=2, date="20990101", png=False, facts=FACTS,
                                  ledger=tmp_path / "l.jsonl", queue=tmp_path / "q.jsonl", writer=dead)
    assert made == [] and sum("카피 실패" in r for r in report) == 1


# ── 게시 ─────────────────────────────────────────────
import dark_publish  # noqa: E402


def _queued(tmp_path, n_png=3):
    d = tmp_path / "cardnews" / "x"
    d.mkdir(parents=True)
    for i in range(n_png):
        (d / f"{i:02d}_slide.png").write_bytes(b"")
    (d / "reel_card.png").write_bytes(b"")  # 캐러셀에 섞이면 안 된다
    (d / "caption.txt").write_text("캡션")
    led, q = tmp_path / "l.jsonl", tmp_path / "q.jsonl"
    dark_ledger.append("it", "queued", led)
    q.write_text(json.dumps({"id": "it", "dir": "cardnews/x", "auto_publish": True}) + "\n")
    return led, q


def test_publish_skips_without_credentials(tmp_path, monkeypatch):
    for k in ("DARK_IG_TOKEN", "DARK_IG_USER_ID", "DARK_PUBLIC_BASE"):
        monkeypatch.delenv(k, raising=False)
    monkeypatch.setattr(dark_publish, "ROOT", tmp_path)
    led, q = _queued(tmp_path)
    rep = dark_publish.run(queue=q, ledger=led, call=lambda *a, **k: pytest.fail("호출하면 안 됨"))
    assert "자격증명 없음" in rep[0]


def test_publish_carousel_flow_and_ledger(tmp_path, monkeypatch):
    monkeypatch.setenv("DARK_IG_TOKEN", "EAA" + "x" * 60)
    monkeypatch.setenv("DARK_IG_USER_ID", "17841400000000000")
    monkeypatch.setenv("DARK_PUBLIC_BASE", "https://ex.app/")
    monkeypatch.setattr(dark_publish, "ROOT", tmp_path)
    led, q = _queued(tmp_path)
    calls = []

    def call(method, url, params=None):
        calls.append((method, url, dict(params or {})))
        if url.endswith("/media") and params.get("is_carousel_item"):
            return {"id": f"c{len(calls)}"}
        if url.endswith("/media"):
            assert params["media_type"] == "CAROUSEL" and params["caption"] == "캡션"
            return {"id": "P"}
        if method == "GET":
            return {"status_code": "FINISHED"}
        return {"id": "MEDIA1"}

    rep = dark_publish.run(queue=q, ledger=led, call=call, wait=lambda urls: True)
    assert rep == ["✓ 게시 it → MEDIA1"]
    assert calls[0][2]["image_url"] == "https://ex.app/cardnews/x/00_slide.png"
    assert dark_ledger.latest(led)["it"]["state"] == "posted"
    assert dark_publish.pending(q, led) == []          # 두 번 올리지 않는다


def test_publish_breaker_stops_on_repeat_error(tmp_path, monkeypatch):
    monkeypatch.setenv("DARK_IG_TOKEN", "EAA" + "x" * 60)
    monkeypatch.setenv("DARK_IG_USER_ID", "17841400000000000")
    monkeypatch.setenv("DARK_PUBLIC_BASE", "https://ex.app")
    monkeypatch.setattr(dark_publish, "ROOT", tmp_path)
    led, q = _queued(tmp_path)
    dark_ledger.append("it2", "queued", led)
    q.open("a").write(json.dumps({"id": "it2", "dir": "cardnews/x", "auto_publish": True}) + "\n")
    dark_ledger.append("it3", "queued", led)
    q.open("a").write(json.dumps({"id": "it3", "dir": "cardnews/x", "auto_publish": True}) + "\n")

    def call(*a, **k):
        raise dark_publish.PublishError("HTTP 403: blocked")
    rep = dark_publish.run(max_items=3, queue=q, ledger=led, call=call, wait=lambda urls: True)
    assert any("중단" in r for r in rep) and sum(r.startswith("✗") for r in rep) == 2


def test_publish_rejects_bad_slide_count(tmp_path, monkeypatch):
    monkeypatch.setattr(dark_publish, "ROOT", tmp_path)
    _queued(tmp_path, n_png=1)
    with pytest.raises(dark_publish.PublishError):
        dark_publish.image_urls({"dir": "cardnews/x"}, "https://ex.app")


# ── 릴스 · 측정 ──────────────────────────────────────
import dark_measure  # noqa: E402
import dark_reel  # noqa: E402


def test_reel_thread_derived_from_slides_and_guarded():
    t = dark_reel.thread_of(good_series())
    assert t["title"].startswith("‘안전하다’") and "*" not in t["title"]
    assert t["items"][0] == "29.5→125.6 — 간수치 ALT"
    s = good_series(thread={"title": "훅", "items": ["사용자 73%가 후회"], "outro": "끝"})
    ok, why = dark_guard.check(s, FACTS)
    assert not ok and any("73" in w for w in why)          # 릴스 글도 가드가 본다


def test_reel_card_html_escapes_and_numbers():
    h = dark_reel.card_html(good_series(thread={"title": "<b>", "items": ["a", "b"], "outro": "o"}),
                            {"handle": "body.darkside", "avatar": ("D", "S")})
    assert "&lt;b&gt;" in h and h.count("<li>") == 2 and "body.darkside" in h


def test_reel_mp4_from_png(tmp_path):
    pytest.importorskip("imageio_ffmpeg")
    import subprocess
    png = tmp_path / "c.png"
    subprocess.run([dark_reel.ffmpeg(), "-loglevel", "error", "-f", "lavfi", "-i", "color=black:s=1080x1920",
                    "-frames:v", "1", str(png)], check=True)
    mp4 = dark_reel.to_mp4(png, tmp_path / "r.mp4", seconds=1)
    assert mp4.exists() and mp4.stat().st_size > 1000


def test_publish_reel_after_carousel(tmp_path, monkeypatch):
    monkeypatch.setenv("DARK_IG_TOKEN", "EAA" + "x" * 60)
    monkeypatch.setenv("DARK_IG_USER_ID", "17841400000000000")
    monkeypatch.setenv("DARK_PUBLIC_BASE", "https://ex.app")
    monkeypatch.setattr(dark_publish, "ROOT", tmp_path)
    led, q = _queued(tmp_path)
    q.write_text(json.dumps({"id": "it", "dir": "cardnews/x", "auto_publish": True,
                             "reel": "cardnews/x/reel.mp4"}) + "\n")
    seen = []

    def call(method, url, params=None):
        params = params or {}
        seen.append(params)
        if method == "GET":
            return {"status_code": "FINISHED"}
        if url.endswith("media_publish"):
            return {"id": "PUB_" + params["creation_id"]}
        if params.get("media_type") == "REELS":
            assert params["video_url"] == "https://ex.app/cardnews/x/reel.mp4"
            return {"id": "R"}
        return {"id": "P" if params.get("media_type") == "CAROUSEL" else "c"}

    rep = dark_publish.run(queue=q, ledger=led, call=call, wait=lambda u: True)
    assert "릴스 PUB_R" in rep[0]
    assert dark_ledger.latest(led)["it"]["reel_media_id"] == "PUB_R"


def test_measure_and_axis_weights(tmp_path, monkeypatch):
    led = tmp_path / "l.jsonl"
    old = (dt.datetime.now() - dt.timedelta(hours=50))
    for i, (axis, saved) in enumerate([("drugs", 30)] * 3 + [("hidden", 5)] * 3):
        dark_ledger.append(f"i{i}", "picked", led, axis=axis, fact_ids=[f"f{i}"])
        dark_ledger.append(f"i{i}", "posted", led, media_id=f"m{i}")
    # posted 시각을 50시간 전으로
    rows = [json.loads(x) for x in led.read_text().splitlines()]
    for r in rows:
        if r["state"] == "posted":
            r["at"] = old.isoformat(timespec="seconds")
    led.write_text("".join(json.dumps(r) + "\n" for r in rows))
    monkeypatch.setenv("DARK_IG_TOKEN", "EAA" + "x" * 60)
    saved_by = {f"m{i}": s for i, (_, s) in enumerate([("drugs", 30)] * 3 + [("hidden", 5)] * 3)}

    def call(method, url, params=None):
        mid = url.split("/")[-2]
        return {"data": [{"name": "reach", "values": [{"value": 1000}]},
                         {"name": "saved", "values": [{"value": saved_by[mid]}]}]}

    rep = dark_measure.run(ledger=led, call=call)
    assert len(rep) == 6 and dark_measure.due(led) == []
    w = dark_measure.axis_weights(led)
    assert w["drugs"] > 1 > w["hidden"]
    top = dark_picker.candidates(FACTS, weights={"hidden": 2.0})[0]
    assert top[2] == "hidden"                                 # 가중치가 순서를 바꾼다


def test_daily_test_mode_leaves_real_ledger_alone(tmp_path, monkeypatch):
    import subprocess
    root = Path(__file__).resolve().parent.parent
    before = (root / "data" / "dark_ledger.jsonl").read_text() if (root / "data" / "dark_ledger.jsonl").exists() else None
    env = dict(__import__("os").environ, DARK_LLM="local", NOGEAR_LOCAL_LLM_URL="http://127.0.0.1:9/none")
    r = subprocess.run([sys.executable, str(root / "scripts" / "dark_daily.py"), "--test", "--no-png", "--count", "1"],
                       capture_output=True, text=True, env=env, timeout=60)
    assert "시험 모드" in r.stdout
    after = (root / "data" / "dark_ledger.jsonl").read_text() if (root / "data" / "dark_ledger.jsonl").exists() else None
    assert before == after


def test_daily_test_mode_reaches_queue(monkeypatch, tmp_path):
    """--test 가 렌더·대기열까지 끝까지 간다 (9/25 맥: relative_to 로 죽었던 회귀)."""
    import runpy
    good = good_series()
    monkeypatch.setattr(dark_daily.dark_copywriter, "write",
                        lambda fact: ({"tag": "T", "slides": good["slides"], "caption": good["caption"]}, "stub", []))
    monkeypatch.setattr(dark_daily.dark_guard, "check", lambda s, f=None: (True, []))
    monkeypatch.setattr(sys, "argv", ["dark_daily.py", "--test", "--no-png", "--count", "1"])
    real_root = dark_daily.gen.ROOT
    with pytest.raises(SystemExit) as e:
        dark_daily.main()
    assert e.value.code == 0
    dark_daily.gen.ROOT = real_root
    dark_daily.gen.CARDNEWS = real_root / "cardnews"


# ── 소재 공급 · 성장 ─────────────────────────────────
import dark_research  # noqa: E402

EFETCH = b"""<PubmedArticleSet><PubmedArticle><MedlineCitation><PMID>40000001</PMID><Article>
<Journal><Title>Eur Heart J</Title></Journal><ArticleTitle>Anabolic steroid use and cardiomyopathy: a nationwide cohort</ArticleTitle>
<Abstract><AbstractText>We followed 1,189 male users and 11,890 controls for 10.2 years. Users had a hazard ratio of 8.9 for cardiomyopathy
and 3.0 for all-cause mortality. Findings persisted after adjustment for age, income and comorbidity across the entire follow-up period.
This nationwide registry study included all men sanctioned for AAS use in Danish fitness centres. Absolute risks remained low but clinically relevant.</AbstractText></Abstract>
<PublicationTypeList><PublicationType>Journal Article</PublicationType></PublicationTypeList></Article></MedlineCitation></PubmedArticle>
<PubmedArticle><MedlineCitation><PMID>40000002</PMID><Article><Journal><Title>X</Title></Journal>
<ArticleTitle>Short</ArticleTitle><Abstract><AbstractText>Too short 1 2.</AbstractText></Abstract></Article></MedlineCitation></PubmedArticle>
</PubmedArticleSet>"""


def fake_fetch(url):
    if "esearch" in url:
        return json.dumps({"esearchresult": {"idlist": ["40000001", "40000002"]}}).encode()
    return EFETCH


def test_research_collects_primary_facts_and_merges(tmp_path):
    facts = dark_research.collect(days=30, per=2, fetch=fake_fetch, pause=0)
    assert facts and all(f["accuracy"] == "primary" and f["pmid"] == "40000001" for f in facts)  # 짧은 초록 제외
    assert "1,189" in facts[0]["notes"] and facts[0]["title"].startswith("[")
    out = tmp_path / "r.json"
    assert dark_research.merge(facts, out)[0] >= 1
    assert dark_research.merge(facts, out)[0] == 0                 # 같은 PMID 는 다시 안 넣는다


def test_primary_fact_flows_through_picker_and_guard(tmp_path):
    f = dark_research.collect(days=30, per=1, fetch=lambda u: fake_fetch(u), pause=0)[0]
    fid = dark_guard.fact_id(f["title"])
    facts = {fid: f}
    c = dark_picker.candidates(facts)
    assert c and c[0][1] == fid and c[0][2] == f["title"][1:f["title"].index("]")]
    s = good_series(fact_ids=[fid])
    s["slides"] = [s["slides"][0], {"kind": "stat", "num": "8.9", "label": "심근병증 위험", "src": "Eur Heart J"},
                   {"kind": "stat", "num": "1,189", "label": "사용자", "src": "Eur Heart J"}, s["slides"][3], s["slides"][4]]
    s["caption"] = ["원문: https://pubmed.ncbi.nlm.nih.gov/40000001/"]
    assert dark_guard.check(s, facts)[0]
    s["slides"][1]["num"] = "12.5"
    assert not dark_guard.check(s, facts)[0]                        # 초록에 없는 숫자


def test_picker_skips_english_case_reports():
    assert dark_picker.individual_death("[drugs] Fatal case of SARM-induced liver failure")
    assert dark_picker.individual_death("[drugs] Trenbolone psychosis: a case report")


def test_publish_rejects_malformed_credentials(tmp_path, monkeypatch):
    monkeypatch.setenv("DARK_IG_TOKEN", "EAA" + "x" * 60)
    monkeypatch.setenv("DARK_IG_USER_ID", "cd ~/nogear-magazine && bash ops/install_mac.sh")   # 9/26 실제로 저장됐던 값
    monkeypatch.setenv("DARK_PUBLIC_BASE", "https://ex.app")
    monkeypatch.setattr(dark_publish, "ROOT", tmp_path)
    led, q = _queued(tmp_path)

    def no_account(method, url, params=None):
        assert url.endswith(("/me", "/me/accounts")), url     # 찾기 말고는 호출하지 않는다
        return {"data": []}
    rep = dark_publish.run(queue=q, ledger=led, call=no_account)
    assert "DARK_IG_USER_ID(숫자" in rep[0]


def test_publish_discovers_account_id_for_this_run_only(tmp_path, monkeypatch):
    import dark_heal
    monkeypatch.setenv("DARK_IG_TOKEN", "EAA" + "x" * 60)
    monkeypatch.setenv("DARK_IG_USER_ID", "cd ~/nogear-magazine")
    monkeypatch.setenv("DARK_PUBLIC_BASE", "https://ex.app")
    monkeypatch.setattr(dark_publish, "ROOT", tmp_path)
    led, q = _queued(tmp_path)
    urls = []

    def call(method, url, params=None):
        urls.append(url)
        if url.endswith("/me/accounts"):
            return {"data": [{"instagram_business_account": {"id": "17841499999999999"}}]}
        if url.endswith("/me"):
            return {}
        if method == "GET":
            return {"status_code": "FINISHED"}
        return {"id": "X"}
    rep = dark_publish.run(queue=q, ledger=led, call=call, wait=lambda u: True)
    assert rep[0].startswith("✓ 게시")
    assert any("/17841499999999999/media" in u for u in urls)
    assert __import__("os").environ["DARK_IG_USER_ID"] == "cd ~/nogear-magazine"   # 저장값은 안 바꾼다
    assert dark_heal.check_token("t", call=lambda *a, **k: {})[0]


def test_http_wraps_url_errors():
    with pytest.raises(dark_publish.PublishError):
        dark_publish.http("POST", "https://graph.facebook.com/v19.0/cd ~/x/media", {})


def test_assemble_adds_source_and_hashtags():
    f = {"title": "[drugs] X", "accuracy": "primary", "source": "https://pubmed.ncbi.nlm.nih.gov/1/"}
    s = dark_daily.assemble({"slides": [], "caption": ["훅"]},
                            {"fact_id": "a", "axis": "drugs", "fact": f, "bg": "x.jpg"})
    assert s["caption"][0] == "훅" and "원문: https://pubmed.ncbi.nlm.nih.gov/1/" in s["caption"]
    assert s["caption"][-1].startswith("#") and not any(ch.isdigit() for ch in s["caption"][-1])


def test_account_snapshot_delta(tmp_path, monkeypatch):
    monkeypatch.setenv("DARK_IG_TOKEN", "EAA" + "x" * 60)
    monkeypatch.setenv("DARK_IG_USER_ID", "17841400000000000")
    p = tmp_path / "acct.jsonl"
    n = iter([10, 17])
    call = lambda *a, **k: {"username": "ngr_magazine", "followers_count": next(n), "media_count": 3}
    assert "팔로워 10 ·" in dark_measure.account_snapshot(call, p)
    assert "팔로워 17 (+7)" in dark_measure.account_snapshot(call, p)


def test_publish_script_survives_bad_token(tmp_path):
    """9/27 실측: 토큰이 깨졌을 때 추적 스택으로 죽지 말고 한 줄 사유로 끝나야 한다."""
    import subprocess
    import textwrap
    root = Path(__file__).resolve().parent.parent
    code = textwrap.dedent(f"""
        import sys, runpy; sys.path.insert(0, {str(root / 'scripts')!r})
        import dark_publish as dp
        def bad(*a, **k): raise dp.PublishError('HTTP 400: Invalid OAuth access token')
        dp.http = bad
        import dark_heal
        print(dark_heal.discover_ig_id('x' * 60, bad), dark_heal.check_token('x' * 60, bad)[0])
    """)
    r = subprocess.run([sys.executable, "-c", code], capture_output=True, text=True, timeout=30)
    assert r.returncode == 0 and r.stdout.strip() == "None False", r.stderr


# ── 바이럴 규칙 ──────────────────────────────────────
def test_hook_score_prefers_viral_formulas():
    listicle = "헬스장이 절대 말 안 하는 3가지"
    hedge = "이 수치는 원인을 단정할 수 없다"
    plain = "보디빌더 사망 연구 결과"
    assert dark_daily.hook_score(listicle) > dark_daily.hook_score(plain) > dark_daily.hook_score(hedge)


def test_assemble_picks_best_hook_moves_hedges_and_adds_ctas():
    obj = {
        "hooks": ["보디빌더 사망 연구", "당신이 모르는 심장의 3가지 대가", "업계 이야기"],
        "comment_prompt": "이거 알고 있었나?",
        "slides": [
            {"kind": "cover", "text": "몸을 만드는 산업의 대가"},
            {"kind": "stat", "num": "38%", "label": "급성 심장사 비율", "src": "EHJ"},
            {"kind": "line", "text": "이 수치는 원인을 단정할 수 없다."},
            {"kind": "end", "text": "끝", "cta": "저장."},
        ],
        "caption": ["옛 훅", "본문"],
    }
    s = dark_daily.assemble(obj, {"fact_id": "a", "axis": "body_cost", "fact": {"title": "t"}, "bg": "x.jpg"})
    assert "3가지" in s["slides"][0]["text"] and "*" in s["slides"][0]["text"]
    assert all("단정할 수 없" not in str(x) for x in s["slides"])            # 본문에서 빠짐
    assert any(c.startswith("※ 이 수치는 원인을") for c in s["caption"])       # 캡션 끝으로
    assert s["caption"][0] == "당신이 모르는 심장의 3가지 대가"
    assert "이거 알고 있었나?" in s["caption"] and any("친구에게 보내라" in c for c in s["caption"])


# ── 디자인 토큰 · 에셋 색인 ──────────────────────────
import dark_assets  # noqa: E402
import dark_tokens  # noqa: E402


def test_tokens_override_colors_and_fonts_and_default_is_noop():
    css = "a{color:#C8141E;background:#050505;font-family:'Noto Serif KR'}@import url(family=Noto+Serif+KR)"
    assert dark_tokens.apply(css, {}) == css
    out = dark_tokens.apply(css, {"color": {"accent": "#00FF00"}, "font": {"serif": "Nanum Myeongjo"}})
    assert "#00FF00" in out and "'Nanum Myeongjo'" in out and "Nanum+Myeongjo" in out
    assert dark_tokens.apply(css, {"color": {"accent": "red;}</style><script>"}}) == css   # 형식 검사


def test_asset_index_reads_series_and_ledger(tmp_path):
    d = tmp_path / "cardnews" / "20990101_dark_auto" / "drugs_abc"
    d.mkdir(parents=True)
    (d / "series.json").write_text(json.dumps({"slides": [{"kind": "cover", "text": "당신이 *모르는*\n3가지"}],
                                               "caption": ["훅", "원문: https://pubmed.ncbi.nlm.nih.gov/1/"]}))
    (d / "00_cover.png").write_bytes(b"")
    (d / "reel.mp4").write_bytes(b"")
    led = tmp_path / "l.jsonl"
    dark_ledger.append("20990101_drugs_abc", "posted", led, media_id="M1")
    rows = dark_assets.scan(tmp_path, led)
    assert rows[0]["hook"] == "당신이 모르는 3가지" and rows[0]["status"] == "posted" and rows[0]["reel"]
    assert rows[0]["source"].endswith("/1/") and rows[0]["cards"] == 1
    j, m = dark_assets.write(rows, tmp_path)
    assert "게시 1" in m.read_text() and json.loads(j.read_text())[0]["media_id"] == "M1"


# ── 바이럴 구조 검사 ─────────────────────────────────
import dark_viral  # noqa: E402


def test_viral_gate_passes_benchmark_shape():
    pts, ok, notes = dark_viral.score(good_series())
    assert ok and pts >= 90, (pts, notes)


def test_viral_gate_fails_flat_series():
    flat = good_series()
    flat["slides"][0]["text"] = "보디빌딩 관련 연구를 정리했다"
    flat["slides"][1] = {"kind": "line", "text": "이 연구는 여러 한계가 있어 단정할 수 없다."}
    flat["slides"][-1]["cta"] = "끝."
    flat["caption"] = ["정리"]
    pts, ok, notes = dark_viral.score(flat)
    assert not ok and pts < 40
    assert any("2장" in n for n in notes) and any("면책" in n for n in notes)


@pytest.mark.parametrize("hook,expect", [
    ("헬스장이 목에 칼이 들어와도 말 안 하는 5가지", {"숫자 목록", "금지·경고", "숨은 진실"}),
    ("진짜 내추럴의 몸 특징 TOP 5", {"숫자 목록", "정체성 특징"}),
    ("약물 부작용 TOP 7, 1위는 충격", {"숫자 목록", "순위 반전"}),
])
def test_hook_formula_bank(hook, expect):
    _, forms = dark_viral.hook_points(hook)
    assert expect <= set(forms), forms


def test_daily_rewrites_once_on_viral_fail(tmp_path, monkeypatch):
    monkeypatch.setattr(dark_daily.gen, "CARDNEWS", tmp_path / "cardnews")
    monkeypatch.setattr(dark_daily.gen, "ROOT", tmp_path)
    good = good_series()
    flat = [dict(x) for x in good["slides"]]
    flat[0] = {"kind": "cover", "text": "연구 정리"}
    calls = []

    def writer(fact, feedback=None):
        calls.append(feedback)
        if fact is not FACT:
            return None, None, ["x: JSON 없음"]
        slides = good["slides"] if feedback else flat
        return {"tag": "T", "slides": slides, "caption": good["caption"]}, "stub", []

    made, report = dark_daily.run(count=1, date="20990101", png=False, facts=FACTS,
                                  ledger=tmp_path / "l.jsonl", queue=tmp_path / "q.jsonl", writer=writer)
    assert made and calls[0] is None and calls[1]                     # 두 번째 호출에 지적사항이 붙는다


# ── 계정 여러 개 · 컨트롤타워 (2026-09-27) ──────────────────────────
import dark_accounts  # noqa: E402
import dark_kit  # noqa: E402
import tower  # noqa: E402


def test_accounts_config_keeps_ngr_paths():
    ngr = dark_accounts.get("ngr")
    assert ngr["handle"] == "ngr_magazine" and ngr["out_suffix"] == "dark_auto"
    assert ngr["ledger"] == "data/dark_ledger.jsonl"          # 기존 원장 그대로 — 이력 안 끊김
    ids = [a["id"] for a in dark_accounts.load()]
    assert len(ids) == len(set(ids))
    for a in dark_accounts.load():                            # 계정끼리 원장·폴더가 섞이지 않게
        assert sum(b["out_suffix"] == a["out_suffix"] or b["ledger"] == a["ledger"]
                   for b in dark_accounts.load()) == 1
    with pytest.raises(KeyError):
        dark_accounts.get("없는계정")


def test_daily_account_suffix_and_axes(tmp_path, monkeypatch):
    monkeypatch.setattr(dark_daily.gen, "CARDNEWS", tmp_path / "cardnews")
    monkeypatch.setattr(dark_daily.gen, "ROOT", tmp_path)
    good = good_series()

    def writer(fact, feedback=None):
        return {"tag": "T", "slides": good["slides"], "caption": good["caption"]}, "stub", []

    axis = dark_picker.axis_of(FACT["title"])
    made, _ = dark_daily.run(count=2, date="20990101", png=False, facts=FACTS, ledger=tmp_path / "l.jsonl",
                             queue=tmp_path / "q.jsonl", writer=writer, suffix="acc2", axes_allowed=[axis])
    assert made and all(m.startswith(f"20990101_{axis}_") for m in made)   # 허용 축만
    assert (tmp_path / "cardnews" / "20990101_acc2").is_dir()
    assert not (tmp_path / "cardnews" / "20990101_dark_auto").exists()


def _fake_day(root, suffix="dark_auto", date="20990101"):
    d = root / "cardnews" / f"{date}_{suffix}" / "hidden_abc"
    d.mkdir(parents=True)
    (d / "series.json").write_text(json.dumps({**good_series(), "viral_score": 85}, ensure_ascii=False))
    (d / "caption.txt").write_text("훅 첫 줄\n본문", encoding="utf-8")
    for n in ("00_cover.png", "01_stat.png"):
        (d / n).write_bytes(b"")
    return d


def test_kit_uses_account_suffix_and_times(tmp_path):
    _fake_day(tmp_path, "acc2")
    kit, summary = dark_kit.build("20990101", root=tmp_path, base="https://x", suffix="acc2", times=["09:00"])
    text = kit.read_text(encoding="utf-8")
    assert "09:00" in text and "https://x/cardnews/20990101_acc2/hidden_abc/00_cover.png" in text
    assert "85" in text and "훅 첫 줄" in summary
    assert dark_kit.build("20990101", root=tmp_path, suffix="없음")[0] is None


def test_tower_status_and_alerts(tmp_path, monkeypatch):
    _fake_day(tmp_path)
    led = tmp_path / "data" / "dark_ledger.jsonl"
    for i in range(5):
        dark_ledger.append(f"x{i}", "queued", led)
    dark_ledger.append("20990101_hidden_abc", "posted", led, media_id="1")
    acc = {"id": "t", "handle": "t_acc", "enabled": True, "count": 2, "out_suffix": "dark_auto",
           "ledger": "data/dark_ledger.jsonl", "queue": "data/q.jsonl"}
    monkeypatch.setattr(tower, "_facts_left", lambda ledger, axes: 3)
    s = tower.account_status(acc, "20990101", root=tmp_path)
    assert s["posted"] == 1 and s["queued"] == 5 and len(s["today"]) == 1
    assert s["today"][0]["viral"] == 85 and s["today"][0]["cover"] == "00_cover.png"
    assert s["followers"] is None                                        # 측정 못 함 = None, 0 아님
    joined = " ".join(s["alerts"])
    assert "러너" in joined and "1/2" in joined and "소재 3" in joined and "5개 쌓임" in joined
    monkeypatch.setattr(tower.dark_accounts, "load", lambda: [acc])
    monkeypatch.setattr(tower, "ROOT", tmp_path)
    (tmp_path / "design").mkdir()
    (tmp_path / "design" / "tokens.json").write_text((Path(tower.__file__).parent.parent / "design" / "tokens.json")
                                                     .read_text(encoding="utf-8"), encoding="utf-8")
    tower.build("20990101", root=tmp_path)
    html_ = (tmp_path / "tower" / "index.html").read_text(encoding="utf-8")
    assert "@t_acc" in html_ and "00_cover.png" in html_
    assert json.loads((tmp_path / "tower" / "status.json").read_text())["accounts"][0]["id"] == "t"
