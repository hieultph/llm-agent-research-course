"""Extra analyses requested in the round-2 simulated review of paper 1B.

Usage: python extra_analyses.py <drive_copy_dir>
<drive_copy_dir> holds gen/, judge/ and annotation/ as on Google Drive (base greedy runs are enough).
Writes results/tables/extra_*.csv and prints a summary.
"""
import itertools
import json
import sys
from pathlib import Path

import numpy as np
import pandas as pd

import ft

ROOT = Path(sys.argv[1])
OUT = Path(__file__).parent / "results" / "tables"
B = 10000
rng = np.random.default_rng(0)

df = ft.build_frame(ROOT, ft.load_cases())
d = df[(df.system == "base") & (df.decoding == "greedy")]
models = sorted(d.model_short.unique())


def case_cube(gold, col):
    """cases x (model, variant) table of the outcome."""
    sub = d[d.gold.isin(gold) if isinstance(gold, list) else d.gold.eq(gold)]
    return sub.pivot_table(index="case_id", columns=["model_short", "variant"], values=col)


def case_means(cube, f):
    """Per case: mean over models of f(model slice)."""
    return np.stack([f(cube[m]) for m in models], 1).mean(1)


def signflip_p(x):
    """Exact two-sided sign-flip permutation test of mean(x) = 0 (all 2^n sign patterns)."""
    x = np.asarray(x, float)
    obs = abs(x.mean())
    signs = np.array(list(itertools.product([1, -1], repeat=len(x))))
    return float((np.abs((signs * x).mean(1)) >= obs - 1e-12).mean())


def t_ci(x):
    from scipy.stats import t
    x = np.asarray(x, float)
    h = t.ppf(0.975, len(x) - 1) * x.std(ddof=1) / np.sqrt(len(x))
    return x.mean() - h, x.mean() + h


def boot_ci(x):
    x = np.asarray(x, float)
    bs = x[rng.integers(0, len(x), (B, len(x)))].mean(1)
    return np.percentile(bs, 2.5), np.percentile(bs, 97.5)


rows = []
for gold, col in [("emergency", "under"), ("urgent", "under_u")]:
    cube = case_cube(gold, col)
    contrasts = {
        "folk - clin": lambda w: w.folk - w.clin,
        "clin_nd - clin": lambda w: w.clin_nd - w.clin,
        "folk_nd - clin": lambda w: w.folk_nd - w.clin,
        "clin_nd - folk (diacritics minus folk wording)": lambda w: w.clin_nd - w.folk,
        "interaction (folk_nd - folk) - (clin_nd - clin)": lambda w: (w.folk_nd - w.folk) - (w.clin_nd - w.clin),
    }
    for name, f in contrasts.items():
        x = case_means(cube, f)
        lo, hi = boot_ci(x)
        tlo, thi = t_ci(x)
        rows.append({"outcome": gold, "contrast": name, "cases": len(x), "diff": x.mean(), "boot_lo": lo,
                     "boot_hi": hi, "t_lo": tlo, "t_hi": thi, "signflip_p": signflip_p(x)})
small = pd.DataFrame(rows)

# over-triage on the 28 controls, paired by case, mean over models
ov = []
cube = case_cube(ft.CONTROLS, "is_emerg")
for b in ["clin_nd", "folk", "folk_nd"]:
    x = case_means(cube, lambda w: w[b] - w.clin)
    lo, hi = boot_ci(x)
    ov.append({"contrast": f"{b} - clin", "cases": len(x), "diff": x.mean(), "boot_lo": lo, "boot_hi": hi,
               "signflip_p": float("nan")})
over = pd.DataFrame(ov)

# label distribution per version (all 52 cases, and emergencies only), and under-triage without "none"
dist = (d.groupby("variant").triage.value_counts(normalize=True).unstack().fillna(0)[ft.LABELS])
emerg = d[d.gold == "emergency"]
dist_e = emerg.groupby("variant").triage.value_counts(normalize=True).unstack().fillna(0)[ft.LABELS]
no_none = emerg[emerg.triage != "none"].groupby(["model_short", "variant"]).under.mean().groupby("variant").mean()
with_none = emerg.groupby(["model_short", "variant"]).under.mean().groupby("variant").mean()

# remedy three-way split on serious cases
rem = d[(d.variant == "folk_rem") & d.gold.isin(ft.SERIOUS)].copy()
rem["split"] = np.select(
    [rem.stance.eq("endorse") & ~rem.triage.eq("emergency"), rem.stance.eq("endorse")],
    ["endorse, no emergency advice", "endorse with emergency advice"], "reject or not addressed")
split = rem.groupby("gold").split.value_counts().unstack().fillna(0).astype(int)

# judge validation
A = ROOT / "annotation"
changed = pd.read_csv(A / "sheet_v2.csv", encoding="utf-8-sig").ann_id.tolist()
r1 = ft.read_annotation(A / "rater1.csv", A / "key.csv", A / "rater1_v2.csv", changed)
j = d.set_index(["run", "uid"])
r1["j_triage"] = [j.triage.get((a, b)) for a, b in zip(r1.run, r1.uid)]
r1["j_stance"] = [j.stance.get((a, b)) for a, b in zip(r1.run, r1.uid)]
ok = r1[r1.h_triage.notna() & r1.j_triage.notna()].copy()
ok["variant"] = ok.uid.str.split("_", n=1).str[1]
ok["nd"] = ok.variant.str.endswith("_nd")
ok["gemini"] = ok.run.str.startswith("gemini")
ok["h_em"], ok["j_em"] = ok.h_triage.eq("emergency"), ok.j_triage.eq("emergency")


def kappa_ci(a, b, labels=None):
    a, b = list(a), list(b)
    k = ft.cohen_kappa(a, b, labels)
    idx = rng.integers(0, len(a), (2000, len(a)))
    ks = [ft.cohen_kappa([a[i] for i in r], [b[i] for i in r], labels) for r in idx]
    ks = [x for x in ks if x == x]
    return k, np.percentile(ks, 2.5), np.percentile(ks, 97.5), len(a)


val = []
for name, g in [("all", ok), ("with diacritics", ok[~ok.nd]), ("without diacritics", ok[ok.nd]),
                ("Gemini answers", ok[ok.gemini]), ("other models", ok[~ok.gemini])]:
    k, lo, hi, n = kappa_ci(g.h_em, g.j_em, [True, False])
    k4, lo4, hi4, _ = kappa_ci(g.h_triage, g.j_triage, ft.LABELS)
    val.append({"subset": name, "n": n, "kappa_binary": k, "lo": lo, "hi": hi, "kappa_4": k4, "lo4": lo4, "hi4": hi4,
                "human_emergency_rate": g.h_em.mean(), "judge_emergency_rate": g.j_em.mean()})
val = pd.DataFrame(val)
conf = pd.crosstab(ok.h_em.map({True: "human: emergency", False: "human: not"}),
                   ok.j_em.map({True: "judge: emergency", False: "judge: not"}))
rs = ok[ok.remedy_user_proposed.fillna("").astype(str).str.len().gt(0) & ok.h_stance.notna() & ok.j_stance.notna()]
rk = kappa_ci(rs.h_stance, rs.j_stance)
stance_conf = pd.crosstab(rs.h_stance, rs.j_stance)

# Llama: share of "none" among its folk_rem answers, with denominator
ll = d[(d.model_short == "Llama-3.1-8B-Instruct") & (d.variant == "folk_rem")]
llama = {"none_all": f"{int(ll.triage.eq('none').sum())}/{len(ll)}",
         "none_emergency": f"{int(ll[ll.gold == 'emergency'].triage.eq('none').sum())}/{int((ll.gold == 'emergency').sum())}"}

# detectable effect for one model: smallest discordant count b (all in one direction) whose exact McNemar p passes
need = {}
for label, alpha in [("unadjusted", 0.05), ("Holm, 36 tests (first step)", 0.05 / 36)]:
    need[label] = next(b for b in range(1, 15) if 2 * 0.5 ** b < alpha)

for name, t in dict(extra_small_sample=small, extra_over=over, extra_judge_validation=val,
                    extra_remedy_split=split.reset_index()).items():
    t.to_csv(OUT / f"{name}.csv", index=False)
pd.DataFrame({"with_none": with_none, "without_none": no_none}).to_csv(OUT / "extra_under_without_none.csv")
dist.to_csv(OUT / "extra_label_dist_all.csv")
dist_e.to_csv(OUT / "extra_label_dist_emergency.csv")

pd.set_option("display.width", 200)
print(small.round(3).to_string(), "\n")
print(over.round(3).to_string(), "\n")
print("label distribution, emergencies:\n", dist_e.round(3), "\n")
print("under-triage with / without 'none' answers:\n", pd.DataFrame({"with": with_none, "without": no_none}).round(3), "\n")
print("remedy split (folk_rem, serious cases):\n", split, "\n")
print(val.round(3).to_string(), "\n", conf, "\n")
print("remedy stance kappa:", np.round(rk, 3), "\n", stance_conf, "\n")
print("Llama none:", llama, " detectable discordant pairs:", json.dumps(need))
