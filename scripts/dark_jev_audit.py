#!/usr/bin/env python3
"""JEV 심사 검증 — «JEV 가 강하다고 한 편이 실제로 더 저장됐나?»

노기어 규칙(CLAUDE.md «일치율을 믿기 전에»): 승격은 evidenceVerdict == real_evidence 인 문항만.
여기서 real_evidence = 게시 48시간 뒤 실제 저장률로 답이 갈리는 문항이다.
  · 답마다 편수·평균 저장률(저장/도달)·평균 공유율
  · 코드 답 vs 확정 답 일치율 — 단, 한쪽 답이 하나뿐이면(상수) «잣대 아님» 으로 표시
  · 문항 판정: 표본(답마다 3편 이상) 모자라면 insufficient, 좋은 답 저장률이 나쁜 답보다
    1.3배 이상이면 real_evidence, 아니면 no_signal
출력: content/dark/jev_audit.json (커밋 — 숫자만, 문구 없음)
승격(productionRoutingFromJev)은 여기서 하지 않는다. Andy 승인 사항이다.
"""
import datetime as dt
import json
import statistics
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import dark_ledger  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "content" / "dark" / "jev_audit.json"
MIN_N = 3
GOOD = {"hook_strength": ("strong", "weak"), "save_value": ("high", "low"),
        "list_hook_present": ("true", "false"), "promise_kept": ("true", "false"),
        "tone_fit": ("street_direct", "academic")}


def joined(ledger=dark_ledger.LEDGER):
    jev, met = {}, {}
    for r in dark_ledger.rows(ledger):
        if r.get("jev"):
            jev[r["id"]] = r["jev"]
        if r["state"] == "measured" and r.get("metrics"):
            met[r["id"]] = r["metrics"]
    return [(jev[i], met[i]) for i in jev if i in met]


def _rate(m, k):
    reach = m.get("reach") or 0
    return (m.get(k) or 0) / reach if reach else None


def audit(ledger=dark_ledger.LEDGER, now=None):
    rows = joined(ledger)
    out = {"generated": (now or dt.datetime.now()).isoformat(timespec="seconds"), "measured": len(rows),
           "questions": {}}
    for q in sorted({k for j, _ in rows for k in j if not k.startswith("_")}):
        by, agree, code_vals = {}, [], set()
        for j, m in rows:
            ans, status = (j.get(q) or [None, None])[:2]
            code = (j.get("_code") or {}).get(q)
            if code:
                code_vals.add(code)
            if status == "decided" and ans:
                s = _rate(m, "saved")
                if s is not None:
                    by.setdefault(ans, []).append((s, _rate(m, "shares") or 0))
                if code:
                    agree.append(code == ans)
        stats = {a: {"n": len(v), "saveRate": round(statistics.mean(x for x, _ in v), 4),
                     "shareRate": round(statistics.mean(y for _, y in v), 4)} for a, v in by.items()}
        verdict = "insufficient"
        good, bad = GOOD.get(q, (None, None))
        if good in stats and bad in stats and min(stats[good]["n"], stats[bad]["n"]) >= MIN_N:
            gs, bs = stats[good]["saveRate"], stats[bad]["saveRate"]
            verdict = "real_evidence" if gs > 0 and (bs == 0 or gs / bs >= 1.3) else "no_signal"
        out["questions"][q] = {
            "answers": stats, "evidenceVerdict": verdict,
            "codeAgreement": round(sum(agree) / len(agree), 2) if agree else None,
            "yardstick": "constant_code" if len(code_vals) == 1 else ("code" if code_vals else "none"),
        }
    return out


if __name__ == "__main__":
    a = audit()
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(a, ensure_ascii=False, indent=1), encoding="utf-8")
    ready = [q for q, v in a["questions"].items() if v["evidenceVerdict"] == "real_evidence"]
    print(f"🧪 JEV 심사 검증: 측정된 편 {a['measured']} · 근거 확인 문항 {ready or '아직 없음'}")
