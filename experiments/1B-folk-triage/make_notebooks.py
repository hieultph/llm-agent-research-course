"""Writes the two Colab notebooks from the cell lists below (stdlib only): python3 make_notebooks.py"""
import json
from pathlib import Path

HERE = Path(__file__).parent


def nb(cells):
    out = []
    for kind, src in cells:
        c = {"cell_type": kind, "metadata": {}, "source": src.strip("\n").splitlines(True)}
        if kind == "code":
            c.update(execution_count=None, outputs=[])
        out.append(c)
    return {"cells": out, "metadata": {"accelerator": "GPU", "colab": {"provenance": []},
                                       "kernelspec": {"display_name": "Python 3", "name": "python3"}},
            "nbformat": 4, "nbformat_minor": 5}


SETUP = r'''
import os, sys, json, subprocess
IN_COLAB = "google.colab" in sys.modules
if IN_COLAB:
    from google.colab import drive, userdata
    drive.mount("/content/drive")
    ROOT = "/content/drive/MyDrive/llm-research/1B-folk-triage"
    REPO = "/content/llm-agent-research-course"
    if os.path.exists(REPO):
        subprocess.run(["git", "-C", REPO, "pull", "-q"], check=True)
    else:
        subprocess.run(["git", "clone", "-q", "--depth", "1",
                        "https://github.com/hieultph/llm-agent-research-course", REPO], check=True)
    CODE = f"{REPO}/experiments/1B-folk-triage"
    def secret(k):
        try: return userdata.get(k)
        except Exception: return None
else:
    ROOT = os.environ.get("FT_ROOT", "outputs")
    CODE = os.environ.get("FT_CODE", ".")
    secret = os.environ.get
sys.path.insert(0, CODE)
import importlib, ft; importlib.reload(ft)
os.makedirs(ROOT, exist_ok=True)
CASES = ft.load_cases(f"{CODE}/data/cases.jsonl")
SYSTEMS = ft.system_prompts(ft.load_lexicon(f"{CODE}/data/folk_lexicon.csv"))
BY_UID = {c["uid"]: c for c in CASES}
print(len(CASES), "prompts ->", ROOT)
'''

GPU = [
    ("markdown", r'''
# 1B · Folk phrasing and diacritic loss → under-triage · notebook A (GPU: open models)

> **Tóm tắt (VI):** Notebook này cho các mô hình mở trả lời 260 câu hỏi (52 ca lấy từ hai bộ công khai × 5 cách kể: y khoa / dân gian × có dấu / không dấu, và bản dân gian kèm "tôi tính chữa dân gian …"), rồi lưu từng câu trả lời vào Drive (`MyDrive/llm-research/1B-folk-triage/gen/`). Nếu Colab ngắt giữa chừng, chạy lại từ đầu: những câu đã xong sẽ được bỏ qua.
>
> **Cách chạy:** Runtime → Change runtime type → **A100** (nhanh nhất, khoảng 1–1,5 giờ) hoặc **L4** (khoảng 2,5–3 giờ). Thêm secret `HF_TOKEN` (Colab → 🔑) để chạy Llama-3.1-8B; nếu không có, bước đó tự bỏ qua. Sau đó Runtime → **Run all**.
>
> Chạy xong thì mở notebook B (`1B_api_judge_analysis.ipynb`) để chấm và phân tích.

**Design.** Same case, same signs, only the wording changes: `clin`, `clin_nd` (diacritics stripped), `folk`, `folk_nd`, plus `folk_rem` (folk + "I plan to <folk remedy>, is that OK?"). 52 public vignettes (Levine et al. 2024; Ramaswamy et al. 2026) with their original labels: 14 emergency, 10 urgent (C/D), 28 soon/self-care controls; every case has a remedy. Neutral system prompt, greedy decoding, up to 2048 new tokens (the first run used 512; answers cut by that limit are regenerated in step 0).
'''),
    ("code", "!pip -q install -U transformers accelerate\n" + SETUP),
    ("code", r'''
import torch
VRAM = torch.cuda.get_device_properties(0).total_memory / 2**30
print(torch.cuda.get_device_name(0), f"{VRAM:.0f} GB")
BIG = VRAM > 30          # A100 / G4: larger batches
HF_TOKEN = secret("HF_TOKEN")

# hub id: batch size on L4 (doubled on A100). Small to large so cheap models finish first.
MODELS = {
    "Qwen/Qwen2.5-1.5B-Instruct": 32,
    "Qwen/Qwen2.5-3B-Instruct": 32,
    "arcee-ai/Arcee-VyLinh": 32,            # Vietnamese-adapted, Qwen2.5-3B base
    "Qwen/Qwen2.5-7B-Instruct": 16,
    "SeaLLMs/SeaLLMs-v3-7B-Chat": 16,       # Southeast-Asian-adapted, Qwen2 base
    "Qwen/Qwen3-8B": 16,                    # thinking disabled
    "meta-llama/Llama-3.1-8B-Instruct": 16, # gated: needs HF_TOKEN
}
MITIGATION_MODELS = ["Qwen/Qwen2.5-7B-Instruct", "SeaLLMs/SeaLLMs-v3-7B-Chat", "meta-llama/Llama-3.1-8B-Instruct"]
SAMPLING_MODELS = ["Qwen/Qwen2.5-7B-Instruct", "SeaLLMs/SeaLLMs-v3-7B-Chat"]
MAX_NEW = 2048
def bsz(bs):             # long answers: smaller batches so the KV cache fits (L4: 4-8, A100: 8-16)
    return max(4, bs * (2 if BIG else 1) // 4)
'''),
    ("markdown", r'''
## Step 0 · Redo answers cut by the old 512-token limit
Drops cut answers (and their judge labels) so steps 1–3 regenerate only those. The first call keeps a copy of the old files in `gen_v1/` and `judge_v1/`; notebook B uses it to find annotated answers that changed. Running this again is safe: answers that reach 2048 tokens (repetition loops) are kept.
'''),
    ("code", r'''
from pathlib import Path
for p in sorted(Path(ROOT, "gen").glob("*.jsonl")):
    if p.stem.startswith("gemini"): continue        # API runs are reset in notebook B
    n = ft.reset_incomplete(ROOT, p.stem, MAX_NEW)
    if n["gen"]: print(f"{p.stem}: redo {n['gen']} answers (dropped {n['judge']} judge labels)")
'''),
    ("markdown", "## Step 1 · Main run: every model, neutral prompt, greedy"),
    ("code", r'''
def gated_ok(m):
    return not m.startswith("meta-llama/") or bool(HF_TOKEN)

for m, bs in MODELS.items():
    if not gated_ok(m):
        print("skip (no HF_TOKEN):", m); continue
    ft.run_hf(m, CASES, SYSTEMS["base"], f"{ROOT}/gen/{ft.run_name(m)}.jsonl", system_key="base",
              batch_size=bsz(bs), max_new_tokens=MAX_NEW, hf_token=HF_TOKEN)
'''),
    ("code", r'''
# ✅ checks: every prompt answered once, few empty or truncated answers; show one stroke case per model
import pandas as pd
rows = []
for m in MODELS:
    g = ft.read_jsonl(f"{ROOT}/gen/{ft.run_name(m)}.jsonl")
    if not g: continue
    uids = [x["uid"] for x in g]
    rows.append({"model": m.split("/")[-1], "n": len(g), "unique": len(set(uids)),
                 "empty": sum(not x["response"] for x in g), "truncated": sum(x["truncated"] for x in g),
                 "median_tokens": pd.Series([x["n_tokens"] for x in g]).median()})
chk = pd.DataFrame(rows); display(chk)
assert (chk.n == len(CASES)).all() and (chk.unique == len(CASES)).all(), "❌ missing or duplicated answers: re-run step 1"
print("✅ all models answered all", len(CASES), "prompts")
for m in MODELS:
    g = {x["uid"]: x for x in ft.read_jsonl(f"{ROOT}/gen/{ft.run_name(m)}.jsonl")}
    if g:
        print(f"\n── {m}  E01_folk_nd\n", g["E01_folk_nd"]["response"][:500])
'''),
    ("markdown", r'''
## Step 2 · Mitigations (RQ4): generic safety line (m1) and folk-term glossary (m2)
Same prompts, different system prompt, on three 7–8B models. The glossary comes from `data/folk_lexicon.csv`.
'''),
    ("code", r'''
for k in ("m1", "m2"):
    print(f"── {k}: {SYSTEMS[k][:200]}…")
    for m in MITIGATION_MODELS:
        if not gated_ok(m): continue
        ft.run_hf(m, CASES, SYSTEMS[k], f"{ROOT}/gen/{ft.run_name(m, k)}.jsonl", system_key=k,
                  batch_size=bsz(MODELS[m]), max_new_tokens=MAX_NEW, hf_token=HF_TOKEN)
'''),
    ("markdown", "## Step 3 · Stability check: 5 samples at temperature 0.7 on two models"),
    ("code", r'''
for m in SAMPLING_MODELS:
    ft.run_hf(m, CASES, SYSTEMS["base"], f"{ROOT}/gen/{ft.run_name(m, 'base', 'sample5')}.jsonl", system_key="base",
              batch_size=max(4, MODELS[m] // 4) * (2 if BIG else 1), max_new_tokens=MAX_NEW, n_samples=5, seed=0)
print("✅ done. Runtime → Disconnect and delete runtime, then open notebook B.")
'''),
]

API = [
    ("markdown", r'''
# 1B · notebook B (CPU): Gemini models, LLM judge, human check, analysis

> **Tóm tắt (VI):** Không cần GPU (Runtime → CPU). Cần secret `GOOGLE_API_KEY` (Colab → 🔑, key Vertex/Agent Platform `AQ.…` hoặc key AI Studio `AIza…` đã nạp credit).
> 1. **Bước 1** cho 2 mô hình qua API trả lời 260 câu hỏi (chạy được trong lúc notebook A đang chạy).
> 2. **Bước 2** cho giám khảo LLM chấm mọi câu trả lời đang có trên Drive. Chạy lại bước này sau khi notebook A xong.
> 3. **Bước 3** tạo phiếu chấm tay `annotation/sheet.csv`. Bạn chấm cả 150 dòng, người thứ hai chấm các dòng đánh dấu `x`. Lưu thành `annotation/rater1.csv` và `annotation/rater2.csv` trên Drive.
> 4. **Bước 4–6** tính kappa, thống kê, vẽ hình, xuất bảng LaTeX và `conclusions.md`.
>
> Chạy lại toàn bộ notebook bao nhiêu lần cũng được: phần nào đã xong sẽ được bỏ qua.
'''),
    ("code", "!pip -q install requests pandas scipy matplotlib  # no -U: upgrading preloaded matplotlib breaks it until restart\n" + SETUP + r'''
os.environ["GOOGLE_API_KEY"] = secret("GOOGLE_API_KEY") or ""
assert os.environ["GOOGLE_API_KEY"], "❌ add the GOOGLE_API_KEY secret"
'''),
    ("code", r'''
API_MODELS = ["gemini-3.5-flash", "gemini-3.5-flash-lite"]  # Gemma 4 is not served on Vertex for this key
API_MITIGATION = ["gemini-3.5-flash-lite"]
JUDGE = "gemini-3.5-flash"      # validated against human labels in step 4
'''),
    ("code", r'''
# quick connectivity test (fails fast on a billing error)
print(ft.gemini_call(API_MODELS[0], CASES[0]["text"], system=SYSTEMS["base"], max_tokens=200)[0][:300])
'''),
    ("markdown", "## Step 1 · API models answer the 260 prompts (neutral prompt; m1/m2 on one model)"),
    ("code", r'''
# redo answers Gemini returned empty (RECITATION filter); retried up to 4 times, then excluded as missing
from pathlib import Path
for p in sorted(Path(ROOT, "gen").glob("gemini*.jsonl")):
    n = ft.reset_incomplete(ROOT, p.stem)
    if n["gen"]: print(f"{p.stem}: redo {n['gen']} answers (dropped {n['judge']} judge labels)")
for m in API_MODELS:
    ft.run_api(m, CASES, SYSTEMS["base"], f"{ROOT}/gen/{ft.run_name(m)}.jsonl")
for k in ("m1", "m2"):
    for m in API_MITIGATION:
        ft.run_api(m, CASES, SYSTEMS[k], f"{ROOT}/gen/{ft.run_name(m, k)}.jsonl", system_key=k)
'''),
    ("markdown", r'''
## Step 2 · LLM judge
The judge sees only the answer (and the proposed remedy for `folk_rem`), never the case, gold label or wording variant. It returns `triage` ∈ {emergency, soon, self_care, none}, the stance toward the remedy, and a quoted phrase as evidence.
'''),
    ("code", r'''
from pathlib import Path
print(ft.JUDGE_PROMPT)
for p in sorted(Path(ROOT, "gen").glob("*.jsonl")):
    print("judging", p.stem)
    ft.run_judge(JUDGE, str(p), f"{ROOT}/judge/{p.stem}.jsonl", BY_UID)
'''),
    ("code", r'''
import pandas as pd
df = ft.build_frame(ROOT, CASES)
n_gen, n_judged = len(df), df.triage.notna().sum()
print(f"{n_judged}/{n_gen} answers judged; runs: {df.run.nunique()}")
display(df.groupby("run").triage.value_counts().unstack(fill_value=0))
assert n_judged == n_gen, "❌ some answers are not judged yet: re-run step 2"
assert (df.triage == "parse_error").mean() < 0.01, "❌ judge output not parseable"
print("✅ all answers judged")
'''),
    ("markdown", r'''
## Step 3 · Human check of the judge
Creates `annotation/sheet.csv` (150 answers, stratified over models and variants, model and variant hidden).
Open it in Google Sheets. **Rater 1** (you) labels all rows; **rater 2** labels the rows marked `x` in column `rater2`. Use the same definitions as the judge prompt above. Download each as CSV to `annotation/rater1.csv` and `annotation/rater2.csv`.

If answers on the sheet were regenerated later (cut by the old 512-token limit, or empty), this step writes `annotation/sheet_v2.csv` with only those rows. Label them the same way and save as `annotation/rater1_v2.csv` and `annotation/rater2_v2.csv`. Labels of regenerated rows on the first sheet are not used.
'''),
    ("code", r'''
A = f"{ROOT}/annotation"; os.makedirs(A, exist_ok=True)
if not os.path.exists(f"{A}/sheet.csv"):
    ft.export_annotation(df, f"{A}/sheet.csv", f"{A}/key.csv", n=150, overlap=60)
print(pd.read_csv(f"{A}/sheet.csv").head(3).to_string()[:1500])
CHANGED = ft.changed_answers(ROOT, f"{A}/key.csv")
if CHANGED and not os.path.exists(f"{A}/sheet_v2.csv"):
    ft.export_annotation_update(ROOT, f"{A}/sheet.csv", f"{A}/key.csv", f"{A}/sheet_v2.csv")
if CHANGED:
    v2 = pd.read_csv(f"{A}/sheet_v2.csv")
    print(f"📝 {len(v2)} regenerated answers to label in sheet_v2.csv ({(v2.rater2 == 'x').sum()} also for rater 2):",
          ", ".join(v2.ann_id))
'''),
    ("markdown", "## Step 4 · Agreement: human–human and judge–human (Cohen's κ)"),
    ("code", r'''
KAPPA = {}
if os.path.exists(f"{A}/rater1.csv"):
    r1 = ft.read_annotation(f"{A}/rater1.csv", f"{A}/key.csv", f"{A}/rater1_v2.csv", CHANGED)
    j = df.set_index(["run", "uid"])
    r1["j_triage"] = [j.triage.get((a, b)) for a, b in zip(r1.run, r1.uid)]
    r1["j_stance"] = [j.stance.get((a, b)) for a, b in zip(r1.run, r1.uid)]
    ok = r1.h_triage.notna() & r1.j_triage.notna()
    print("unlabelled or missing:", ", ".join(r1.ann_id[~ok]) or "none")
    KAPPA["judge_vs_rater1_triage"] = ft.cohen_kappa(r1.h_triage[ok].tolist(), r1.j_triage[ok].tolist())
    KAPPA["judge_vs_rater1_triage_binary"] = ft.cohen_kappa((r1.h_triage[ok] == "emergency").tolist(),
                                                             (r1.j_triage[ok] == "emergency").tolist())
    rs = r1[ok & (r1.remedy_user_proposed.fillna("").str.len() > 0) & r1.h_stance.notna()]
    if len(rs):
        KAPPA["judge_vs_rater1_remedy"] = ft.cohen_kappa(rs.h_stance.tolist(), rs.j_stance.tolist())
    if os.path.exists(f"{A}/rater2.csv"):
        r2 = ft.read_annotation(f"{A}/rater2.csv", f"{A}/key.csv", f"{A}/rater2_v2.csv", CHANGED).set_index("ann_id")
        both = r1.set_index("ann_id").join(r2[["h_triage"]], rsuffix="_2").dropna(subset=["h_triage", "h_triage_2"])
        KAPPA["rater1_vs_rater2_triage"] = ft.cohen_kappa(both.h_triage.tolist(), both.h_triage_2.tolist())
        KAPPA["n_overlap"] = len(both)
    KAPPA["n_rater1"] = int(ok.sum())
    display(pd.crosstab(r1.h_triage[ok], r1.j_triage[ok], margins=True))
    print(json.dumps(KAPPA, indent=1))
    print("✅ judge usable" if KAPPA["judge_vs_rater1_triage_binary"] >= 0.7 else "⚠️ κ < 0.7: tighten the judge prompt")
else:
    print("⏳ waiting for annotation/rater1.csv")
'''),
    ("markdown", "## Step 5 · Results"),
    ("code", r'''
R = f"{ROOT}/results"; os.makedirs(f"{R}/tables", exist_ok=True)
rates = ft.rate_table(df); con = ft.contrast_table(df); pooled = ft.pooled_contrasts(df)
con_u = ft.contrast_table(df, gold="urgent"); pooled_u = ft.pooled_contrasts(df, gold="urgent")   # secondary: C/D cases
over = ft.over_contrasts(df); terms = ft.term_table(df)
rem = pd.concat([ft.remedy_table(df), ft.remedy_table(df, sourced_only=True)])
rem_sens = ft.remedy_sensitivity(df)                       # all remedies vs documented remedies only
conds = ft.condition_table(df); mit = ft.mitigation_table(df); samp = ft.sampling_table(df)
for name, t in dict(rates=rates, contrasts=con, pooled=pooled, contrasts_urgent=con_u, pooled_urgent=pooled_u,
                    over=over, remedy=rem, remedy_sensitivity=rem_sens, terms=terms,
                    conditions=conds, mitigation=mit, sampling=samp).items():
    t.to_csv(f"{R}/tables/{name}.csv", index=name == "conditions")
base = rates[(rates.system == "base") & (rates.decoding == "greedy")]
display(base.pivot(index="model", columns="variant", values="under").round(2))
display(base.pivot(index="model", columns="variant", values="under_u").round(2))
display(base.pivot(index="model", columns="variant", values="over").round(2))
display(pooled.round(3)); display(pooled_u.round(3)); display(con.round(3))
display(rem[rem.subset == "all"].round(2)); display(rem_sens.round(3))
'''),
    ("code", r'''
ft.fig_under_bars(rates, R); ft.fig_term_heatmap(terms, R); ft.fig_mitigation(mit, R)
display(conds.round(2)); display(mit.round(2)); display(samp.round(2))
'''),
    ("markdown", "## Step 6 · LaTeX tables and auto-written conclusions"),
    ("code", r'''
def pct(x): return f"{100 * x:.0f}"
def ci(r): return f"{100 * r['diff']:+.0f} [{100 * r['lo']:+.0f}, {100 * r['hi']:+.0f}]"
def star(p): return "" if p != p else ("$^{***}$" if p < .001 else "$^{**}$" if p < .01 else "$^{*}$" if p < .05 else "")

lines = [r"\begin{tabular}{lrrrrrlll}", r"\toprule",
         r"Model & clin & clin\_nd & folk & folk\_nd & rem & $\Delta$folk & $\Delta$nd & $\Delta$folk\_nd \\", r"\midrule"]
U = base.pivot(index="model", columns="variant", values="under")
for m in U.sort_values("clin").index:
    c = con[con.model == m].set_index("contrast")
    cell = lambda k: ci(c.loc[k]) + star(c.loc[k, "p_holm"]) if k in c.index else "--"
    lines.append(f"{m} & " + " & ".join(pct(U.loc[m, v]) for v in ft.VARIANTS) +
                 f" & {cell('folk - clin')} & {cell('clin_nd - clin')} & {cell('folk_nd - clin')} \\\\")
lines += [r"\midrule"]
P = pooled.set_index("contrast")
lines.append(r"Mean over models & \multicolumn{5}{c}{} & " +
             " & ".join(ci(P.loc[k]) for k in ["folk - clin", "clin_nd - clin", "folk_nd - clin"]) + r" \\")
lines += [r"\bottomrule", r"\end{tabular}"]
open(f"{R}/tables/main.tex", "w").write("\n".join(lines))

mt = [r"\begin{tabular}{llrrrrr}", r"\toprule", r"Model & Prompt & clin & folk & folk\_nd & gap & over \\", r"\midrule"]
for _, r in mit.sort_values(["model", "system"]).iterrows():
    mt.append(f"{r.model} & {r.system} & {pct(r.under_clin)} & {pct(r.under_folk)} & {pct(r.under_folk_nd)} & "
              f"{100 * r.gap_folk_nd:+.0f} & {pct(r.over_all)} \\\\")
mt += [r"\bottomrule", r"\end{tabular}"]
open(f"{R}/tables/mitigation.tex", "w").write("\n".join(mt))

summary = {"models": sorted(base.model.unique()), "kappa": KAPPA, "judge": JUDGE,
           "n_cases": df.groupby("gold").case_id.nunique().to_dict(),
           "pooled": pooled.round(4).to_dict("records"),
           "pooled_urgent": pooled_u.round(4).to_dict("records"),
           "under_by_variant_mean": base.groupby("variant").under.mean().round(4).to_dict(),
           "under_urgent_by_variant_mean": base.groupby("variant").under_u.mean().round(4).to_dict(),
           "over_by_variant_mean": base.groupby("variant").over.mean().round(4).to_dict(),
           "remedy": rem[rem.subset == "all"].round(4).to_dict("records"),
           "remedy_sensitivity": rem_sens.round(4).to_dict("records"),
           "holm_significant_urgent": con_u[(con_u.p_holm < .05)][["model", "contrast", "diff"]].round(3).to_dict("records"),
           "holm_significant": con[(con.p_holm < .05)][["model", "contrast", "diff"]].round(3).to_dict("records"),
           "top_terms": terms.head(8)[["term", "cases", "clin", "folk", "diff"]].round(3).to_dict("records")}
json.dump(summary, open(f"{R}/summary.json", "w"), ensure_ascii=False, indent=1)
print(open(f"{R}/tables/main.tex").read()); print(json.dumps(summary, ensure_ascii=False, indent=1)[:4000])
'''),
]

for name, cells in [("1B_generate_gpu.ipynb", GPU), ("1B_api_judge_analysis.ipynb", API)]:
    json.dump(nb(cells), open(HERE / name, "w"), ensure_ascii=False, indent=1)
    print("wrote", name)
