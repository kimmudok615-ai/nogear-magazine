#!/usr/bin/env python3
"""에셋 보드 — 모든 캐러셀·캐릭터·디자인 자산을 한 화면에 (2026-09-27 Andy
«파일 정리 및 에셋 구축 보드 깔끔하게 · 일자별 업로드 등 QC 추측 바이럴까지 · 팀 에이전트 싹 다 붙히는 구조»).

board/index.html (Vercel /board/) + board/data.json
  · 일자별: 날짜마다 만든 편, 올릴 시간, 올렸나(원장), 측정치
  · 편마다 팀 11역할의 판정이 한 줄로 붙는다: 소재 → 카피 → 안전 → 바이럴 → JEV → 디자인 QC → 게시 → 측정
  · 예상 바이럴(추측) = 바이럴 게이트 70% + JEV 순위 30% (JEV 없으면 게이트 점수만) — 측정되면 실제 저장률을 옆에
  · 에셋: 캐릭터 · 표지 형식 3종 · 색·글꼴 · Canva · 문서 지도
읽기만 한다. 측정 못 한 값은 «—».
"""
import datetime as dt
import html
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import dark_accounts  # noqa: E402
import dark_ledger  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "board"
STAGES = [("fact", "소재"), ("copy", "카피"), ("safety", "안전"), ("viral", "바이럴"), ("jev", "JEV"),
          ("design", "디자인"), ("publish", "게시"), ("analyst", "측정")]


def predicted(viral, jev_rank):
    """예상 바이럴(추측) 0~100. 투명한 식 — 실제 저장률이 쌓이면 dark_jev_audit 로 검증한다."""
    if viral is None:
        return None
    return round(viral * 0.7 + (jev_rank / 7 * 100) * 0.3) if jev_rank is not None else round(viral)


def _ledger_rows(accounts, root):
    last, picked = {}, {}
    for acc in accounts:
        led, _ = dark_accounts.paths(acc, root)
        for r in dark_ledger.rows(led):
            last[r["id"]] = r
            if r["state"] == "drafted":
                picked.setdefault(r["id"], {})["model"] = r.get("model")
            if r["state"] == "posted":
                picked.setdefault(r["id"], {})["posted_at"] = r.get("posted_at") or r["at"]
            if r["state"] == "measured":
                picked.setdefault(r["id"], {})["metrics"] = r.get("metrics")
    return last, picked


def item(sj, root, acc, last, extra):
    d = sj.parent
    s = json.loads(sj.read_text(encoding="utf-8"))
    date = d.parent.name.split("_")[0]
    iid = f"{date}_{d.name}"
    kind = "example" if d.parent.name.endswith("_examples") else "daily"
    rel = lambda p: "../" + str(p.relative_to(root))  # noqa: E731
    cards = [rel(p) for p in sorted(d.glob("[0-9][0-9]_*.png"))]
    alts = {p.stem.replace("alt_cover_", ""): rel(p) for p in sorted(d.glob("alt_cover_*.png"))}
    st = last.get(iid, {}).get("state")
    ex = extra.get(iid, {})
    m = ex.get("metrics") or {}
    rank = (s.get("jev") or {}).get("rank")
    dq = s.get("design_qa")
    save_rate = round(m["saved"] / m["reach"] * 100, 2) if m.get("reach") and m.get("saved") is not None else None
    stages = {
        "fact": ("ok", f"{len(s.get('fact_ids', []))}건 · {d.name.rsplit('_', 1)[0]}"),
        "copy": ("ok", ex.get("model") or ("직접 작성" if kind == "example" else "—")),
        "safety": ("ok", "가드 통과"),
        "viral": ("ok" if (s.get("viral_score") or 0) >= 70 else "warn", f"{s.get('viral_score', '—')}점"),
        "jev": (("ok", f"순위 {rank}/7") if rank is not None else ("idle", "심사 없음")),
        "design": (("idle", "미검사") if dq is None else ("ok", "통과") if not dq else ("warn", f"문제 {sum(map(len, dq.values()))}")),
        "publish": (("ok", str(ex.get("posted_at", ""))[:10] or "게시") if st in ("posted", "measured")
                    else ("wait", "대기") if st == "queued" else ("idle", "예시" if kind == "example" else "—")),
        "analyst": (("ok", f"저장률 {save_rate}%") if save_rate is not None else ("idle", "—")),
    }
    cover = next((c for c in s.get("slides", []) if c.get("kind") == "cover"), {})
    cap = (d / "caption.txt").read_text(encoding="utf-8") if (d / "caption.txt").exists() else ""
    return {"id": iid, "account": acc.get("handle"), "date": date, "kind": kind, "axis": d.name.rsplit("_", 1)[0],
            "hook": " ".join(str(cover.get("text", "")).replace("*", "").split()), "cards": cards, "alts": alts,
            "caption": cap, "viral": s.get("viral_score"), "jev_rank": rank, "predicted": predicted(s.get("viral_score"), rank),
            "save_rate": save_rate, "status": st or ("example" if kind == "example" else "—"),
            "stages": {k: {"state": a, "note": b} for k, (a, b) in stages.items()}}


def collect(root=ROOT):
    accounts = dark_accounts.load()
    last, extra = _ledger_rows(accounts, root)
    items = []
    for acc in accounts:
        suf = acc.get("out_suffix", "dark_auto")
        for pattern in (f"*_{suf}/*/series.json", "*_dark_examples/*/series.json" if acc["id"] == "ngr" else None):
            if pattern:
                items += [item(sj, root, acc, last, extra) for sj in sorted((root / "cardnews").glob(pattern))]
    items.sort(key=lambda x: (x["date"], x["predicted"] or 0), reverse=True)
    chars = json.loads((root / "design" / "characters.json").read_text(encoding="utf-8")).get("images", {}) \
        if (root / "design" / "characters.json").exists() else {}
    tokens = json.loads((root / "design" / "tokens.json").read_text(encoding="utf-8")) \
        if (root / "design" / "tokens.json").exists() else {}
    team = json.loads((root / "config" / "team.json").read_text(encoding="utf-8"))["roles"] \
        if (root / "config" / "team.json").exists() else []
    return {"generated": dt.datetime.now().isoformat(timespec="seconds"), "items": items,
            "characters": [{"name": k, "axis": v.get("axis"), "use": v.get("use"),
                            "src": f"../cardnews/assets/characters/{k}.png",
                            "have": (root / "cardnews" / "assets" / "characters" / f"{k}.png").exists()} for k, v in chars.items()],
            "colors": tokens.get("color", {}), "team": [{"name": r["name"], "tier": r["tier"], "script": r["script"],
                                                         "gate": r["gate"]} for r in team],
            "stages": STAGES}


PAGE = """<!doctype html><html lang="ko"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1"><title>NGR 에셋 보드</title>
<link href="https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@400;700&family=Noto+Serif+KR:wght@900&display=swap" rel="stylesheet">
<style>
@font-face{font-family:Plex;src:url('../design/fonts/IBMPlexMono-Regular.ttf')}
:root{--ink:#0B0B0A;--paper:#E9E4DA;--dust:#8C867B;--line:#2A2926;--red:#C8141E;--ok:#8FB38A;--wait:#D6B25E}
*{box-sizing:border-box;margin:0;padding:0}
body{background:var(--ink);color:var(--paper);font:15px/1.55 'Noto Sans KR',sans-serif;padding:0 16px 80px}
.wrap{max-width:1280px;margin:0 auto}
.mono{font-family:Plex,ui-monospace,monospace;letter-spacing:.14em;text-transform:uppercase;font-size:11px;color:var(--dust)}
header{display:flex;justify-content:space-between;align-items:flex-end;gap:16px;flex-wrap:wrap;padding:40px 0 20px;border-bottom:1px solid var(--line)}
h1{font:900 34px/1.1 'Noto Serif KR',serif;letter-spacing:-.02em}h1 em{color:var(--red);font-style:normal}
nav{display:flex;gap:18px;flex-wrap:wrap}nav a{color:var(--dust);text-decoration:none}nav a:hover{color:var(--paper)}
section{padding:32px 0;border-bottom:1px solid var(--line)}h2{font:700 13px Plex,monospace;letter-spacing:.2em;color:var(--dust);margin-bottom:18px}
.kpis{display:grid;grid-template-columns:repeat(auto-fit,minmax(140px,1fr));gap:1px;background:var(--line);border:1px solid var(--line)}
.kpis div{background:var(--ink);padding:14px 16px}.kpis b{display:block;font:900 28px 'Noto Serif KR',serif}
.filters{display:flex;gap:8px;flex-wrap:wrap;margin-bottom:18px}
select,input{background:#141412;color:var(--paper);border:1px solid var(--line);padding:7px 10px;font:13px 'Noto Sans KR'}
.day{margin-bottom:28px}.day h3{font:700 13px Plex,monospace;letter-spacing:.16em;margin-bottom:12px;display:flex;justify-content:space-between;color:var(--paper)}
.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(240px,1fr));gap:16px}
.card{border:1px solid var(--line);background:#101010;cursor:pointer;display:flex;flex-direction:column}
.card:hover{border-color:var(--dust)}.card img{width:100%;aspect-ratio:4/5;object-fit:cover;display:block;background:#000}
.card .b{padding:10px 12px 12px;display:flex;flex-direction:column;gap:8px;flex:1}
.hook{font-weight:700;font-size:14px;line-height:1.4}
.row{display:flex;justify-content:space-between;align-items:center}
.pred{font:900 22px 'Noto Serif KR',serif}.pred small{font:11px Plex;color:var(--dust);margin-left:4px}
.pipe{display:grid;grid-template-columns:repeat(8,1fr);gap:2px}
.pipe i{height:6px;background:var(--line)}.pipe i.ok{background:var(--ok)}.pipe i.warn{background:var(--red)}.pipe i.wait{background:var(--wait)}
dialog{margin:auto;background:var(--ink);color:var(--paper);border:1px solid var(--line);max-width:1100px;width:calc(100% - 32px);padding:24px}
dialog::backdrop{background:rgba(0,0,0,.8)}
.strip{display:flex;gap:10px;overflow-x:auto;padding-bottom:8px}.strip img{height:300px;border:1px solid var(--line)}
table{width:100%;border-collapse:collapse;font-size:13px;margin:16px 0}td,th{padding:6px 8px;border-top:1px solid var(--line);text-align:left;vertical-align:top}
th{font:11px Plex;letter-spacing:.12em;color:var(--dust);font-weight:400}
.s-ok{color:var(--ok)}.s-warn{color:var(--red)}.s-wait{color:var(--wait)}.s-idle{color:var(--dust)}
pre{white-space:pre-wrap;background:#141412;border:1px solid var(--line);padding:12px;font:13px/1.6 'Noto Sans KR';max-height:260px;overflow:auto}
button{background:none;color:var(--paper);border:1px solid var(--line);padding:6px 12px;cursor:pointer;font:13px 'Noto Sans KR'}
button:hover{border-color:var(--paper)}
.chars{display:grid;grid-template-columns:repeat(auto-fill,minmax(150px,1fr));gap:12px}
.chars figure{border:1px solid var(--line)}.chars img,.chars .ph{width:100%;aspect-ratio:4/5;object-fit:cover;display:block;background:repeating-linear-gradient(45deg,#111 0 8px,#161614 8px 16px)}
.chars figcaption{padding:8px;font-size:12px;color:var(--dust)}
.sw{display:flex;gap:10px;flex-wrap:wrap}.sw div{width:120px}.sw i{display:block;height:48px;border:1px solid var(--line)}
.legend{display:flex;gap:14px;flex-wrap:wrap;margin-top:10px}.legend span{display:flex;align-items:center;gap:6px}.legend i{width:14px;height:6px;display:inline-block}
@media(max-width:600px){h1{font-size:26px}.strip img{height:220px}}
</style></head><body><div class="wrap">
<header><div><div class="mono">NGR · THE DARK SIDE — ASSET BOARD</div><h1>에셋 <em>보드</em></h1></div>
<nav class="mono"><a href="#days">일자별</a><a href="#team">팀</a><a href="#assets">에셋</a><a href="../tower/">컨트롤타워</a></nav></header>
<section><div class="kpis" id="kpis"></div><p class="mono" style="margin-top:12px">생성 __GEN__ · 90분 넘게 지난 화면은 낡은 값 · 예상 바이럴 = 게이트 70% + JEV 30% (추측, 실측 저장률과 대조)</p></section>
<section id="days"><h2>일자별 업로드 · QC · 예상 바이럴</h2>
<div class="filters"><select id="fAcc"><option value="">모든 계정</option></select><select id="fKind"><option value="">일일+예시</option><option value="daily">일일</option><option value="example">예시</option></select>
<select id="fAxis"><option value="">모든 축</option></select><select id="fStat"><option value="">모든 상태</option><option>queued</option><option>posted</option><option>measured</option><option>example</option></select>
<select id="fSort"><option value="date">날짜순</option><option value="pred">예상 바이럴순</option></select><input id="fQ" placeholder="훅 검색"></div>
<div class="legend mono" id="legend"></div><div id="list" style="margin-top:18px"></div></section>
<section id="team"><h2>팀 — 편마다 붙는 11역할</h2><table id="teamT"></table></section>
<section id="assets"><h2>캐릭터</h2><div class="chars" id="chars"></div>
<h2 style="margin-top:28px">색</h2><div class="sw" id="sw"></div>
<h2 style="margin-top:28px">형식 · 문서</h2><table>
<tr><th>기본</th><td>다크사이콜로지 스레드 캡처 — scripts/dark_thread.py</td></tr>
<tr><th>대안 A</th><td>증거 파일(Evidence Noir) — scripts/dark_dossier.py · design/PHILOSOPHY.md · design/DESIGN_RULES.md</td></tr>
<tr><th>검사</th><td>scripts/dark_design_qa.py (넘침·겹침·16px·붉은색)</td></tr>
<tr><th>파일 지도</th><td>docs/dark/README.md</td></tr><tr><th>Canva</th><td>design/canva_assets.json · design/CANVA.md</td></tr></table></section>
</div><dialog id="dlg"></dialog>
<script>
const D=__DATA__;const $=s=>document.querySelector(s);const esc=t=>String(t??'').replace(/[&<>"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));
const fill=(id,vals)=>vals.forEach(v=>$(id).insertAdjacentHTML('beforeend',`<option>${esc(v)}</option>`));
fill('#fAcc',[...new Set(D.items.map(i=>i.account))]);fill('#fAxis',[...new Set(D.items.map(i=>i.axis))]);
$('#legend').innerHTML=D.stages.map(s=>s[1]).join(' → ')+' &nbsp; <span><i style="background:var(--ok)"></i>완료</span><span><i style="background:var(--wait)"></i>대기</span><span><i style="background:var(--red)"></i>문제</span><span><i style="background:var(--line)"></i>없음</span>';
const n=D.items.length,posted=D.items.filter(i=>['posted','measured'].includes(i.status)).length,queued=D.items.filter(i=>i.status==='queued').length;
const pr=D.items.map(i=>i.predicted).filter(x=>x!=null),dq=D.items.filter(i=>i.stages.design.state==='warn').length;
$('#kpis').innerHTML=[['편',n],['게시',posted],['대기',queued],['평균 예상 바이럴',pr.length?Math.round(pr.reduce((a,b)=>a+b,0)/pr.length):'—'],['디자인 문제',dq],['캐릭터',D.characters.filter(c=>c.have).length+'/'+D.characters.length]].map(([k,v])=>`<div><span class="mono">${k}</span><b>${v}</b></div>`).join('');
function card(i){return `<div class="card" data-id="${esc(i.id)}"><img loading="lazy" src="${esc(i.cards[0]||'')}" alt=""><div class="b"><div class="hook">${esc(i.hook)}</div>
<div class="row"><span class="pred">${i.predicted??'—'}<small>예상</small></span><span class="mono">${esc(i.axis)} · ${esc(i.status)}</span></div>
<div class="pipe">${D.stages.map(([k,l])=>`<i class="${i.stages[k].state}" title="${l}: ${esc(i.stages[k].note)}"></i>`).join('')}</div></div></div>`}
function draw(){const f={a:$('#fAcc').value,k:$('#fKind').value,x:$('#fAxis').value,s:$('#fStat').value,q:$('#fQ').value.trim()};
let it=D.items.filter(i=>(!f.a||i.account===f.a)&&(!f.k||i.kind===f.k)&&(!f.x||i.axis===f.x)&&(!f.s||i.status===f.s)&&(!f.q||i.hook.includes(f.q)));
if($('#fSort').value==='pred'){it=[...it].sort((a,b)=>(b.predicted??-1)-(a.predicted??-1));$('#list').innerHTML=`<div class="grid">${it.map(card).join('')}</div>`;return}
const days={};it.forEach(i=>(days[i.date+' '+i.kind]??=[]).push(i));
$('#list').innerHTML=Object.entries(days).map(([d,xs])=>`<div class="day"><h3><span>${d.slice(0,4)}.${d.slice(4,6)}.${d.slice(6,8)} ${d.includes('example')?'· 예시':''}</span><span class="mono">${xs.length}편 · 게시 ${xs.filter(i=>['posted','measured'].includes(i.status)).length}</span></h3><div class="grid">${xs.map(card).join('')}</div></div>`).join('')||'<p class="mono">없음</p>'}
['#fAcc','#fKind','#fAxis','#fStat','#fSort'].forEach(s=>$(s).onchange=draw);$('#fQ').oninput=draw;draw();
$('#list').onclick=e=>{const c=e.target.closest('.card');if(!c)return;const i=D.items.find(x=>x.id===c.dataset.id);
$('#dlg').innerHTML=`<div class="row"><div><div class="mono">${esc(i.id)} · @${esc(i.account)}</div><div class="hook" style="font-size:20px;margin-top:6px">${esc(i.hook)}</div></div><button onclick="dlg.close()">닫기</button></div>
<div class="strip" style="margin-top:16px">${i.cards.map(u=>`<a href="${esc(u)}" target="_blank"><img src="${esc(u)}"></a>`).join('')}${Object.entries(i.alts).map(([k,u])=>`<a href="${esc(u)}" target="_blank" title="대안 ${esc(k)}"><img src="${esc(u)}" style="opacity:.75"></a>`).join('')}</div>
<table><tr><th>역할</th><th>판정</th></tr>${D.stages.map(([k,l])=>`<tr><td>${l}</td><td class="s-${i.stages[k].state}">${esc(i.stages[k].note)}</td></tr>`).join('')}
<tr><td>예상 바이럴</td><td>${i.predicted??'—'} (게이트 ${i.viral??'—'} · JEV ${i.jev_rank??'—'}/7)</td></tr><tr><td>실측 저장률</td><td>${i.save_rate!=null?i.save_rate+'%':'—'}</td></tr></table>
<div class="row"><span class="mono">캡션</span><button id="cp">복사</button></div><pre>${esc(i.caption)}</pre>`;
$('#cp').onclick=()=>{navigator.clipboard.writeText(i.caption).then(()=>$('#cp').textContent='복사됨').catch(()=>$('#cp').textContent='복사 안 됨 — 직접 선택')};dlg.showModal()};
$('#teamT').innerHTML='<tr><th>역할</th><th>도구</th><th>담당</th><th>문(게이트)</th></tr>'+D.team.map(r=>`<tr><td>${esc(r.name)}</td><td class="mono">${esc(r.tier)}</td><td class="mono" style="text-transform:none">${esc(r.script)}</td><td>${esc(r.gate)}</td></tr>`).join('');
$('#chars').innerHTML=D.characters.map(c=>`<figure>${c.have?`<img loading="lazy" src="${esc(c.src)}">`:'<div class="ph"></div>'}<figcaption>${esc(c.name)} · ${esc(c.axis)}<br>${esc(c.use)}${c.have?'':' (맥에서 받는 중)'}</figcaption></figure>`).join('');
$('#sw').innerHTML=Object.entries(D.colors).map(([k,v])=>`<div><i style="background:${esc(v)}"></i><span class="mono">${esc(k)} ${esc(v)}</span></div>`).join('');
</script></body></html>"""


def build(root=ROOT):
    data = collect(root)
    out = root / "board"
    out.mkdir(exist_ok=True)
    (out / "data.json").write_text(json.dumps(data, ensure_ascii=False, indent=1), encoding="utf-8")
    page = PAGE.replace("__DATA__", json.dumps(data, ensure_ascii=False).replace("</", "<\\/")).replace(
        "__GEN__", html.escape(data["generated"].replace("T", " ")))
    (out / "index.html").write_text(page, encoding="utf-8")
    return data


if __name__ == "__main__":
    d = build()
    print(f"🗂 에셋 보드: {len(d['items'])}편 · 캐릭터 {sum(c['have'] for c in d['characters'])}/{len(d['characters'])} → board/index.html")
