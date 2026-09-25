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
            {"kind": "cover", "kicker": "BLOOD WORK", "text": "‘안전하다’.\n*혈액검사*로 확인했다."},
            {"kind": "stat", "num": "29.5→125.6", "label": "간수치 ALT", "src": "JMIR"},
            {"kind": "stat", "num": "44.5→31.1", "label": "HDL", "src": "JMIR"},
            {"kind": "line", "text": "‘연구용’ 라벨은\n*당신*을 위한 게 아니다."},
            {"kind": "end", "text": "‘안전한 약물’은\n*마케팅 용어*다.", "cta": "저장."},
        ],
        "caption": ["SARM 사용 전→후 ALT 29.5→125.6", "출처: JMIR 1,700건"],
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
        (d / f"{i:02d}.png").write_bytes(b"")
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
    monkeypatch.setenv("DARK_IG_TOKEN", "t")
    monkeypatch.setenv("DARK_IG_USER_ID", "u")
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
    assert calls[0][2]["image_url"] == "https://ex.app/cardnews/x/00.png"
    assert dark_ledger.latest(led)["it"]["state"] == "posted"
    assert dark_publish.pending(q, led) == []          # 두 번 올리지 않는다


def test_publish_breaker_stops_on_repeat_error(tmp_path, monkeypatch):
    monkeypatch.setenv("DARK_IG_TOKEN", "t")
    monkeypatch.setenv("DARK_IG_USER_ID", "u")
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
