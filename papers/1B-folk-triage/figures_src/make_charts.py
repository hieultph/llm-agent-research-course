"""Draw the result charts of paper 1B as editable SVG (text stays text).

Reads the result tables in experiments/1B-folk-triage/results/tables and writes
svg/fig_*.svg. Run export.py afterwards to get the PDFs used by LaTeX.
"""
from pathlib import Path

import matplotlib
import matplotlib.pyplot as plt
import pandas as pd

matplotlib.use("Agg")
HERE = Path(__file__).resolve().parent
TABLES = HERE.parents[2] / "experiments" / "1B-folk-triage" / "results" / "tables"
OUT = HERE / "svg"

plt.rcParams.update({
    "svg.fonttype": "none",          # keep text as <text>, editable in Inkscape / draw.io
    "font.family": "DejaVu Sans",
    "font.size": 7.5,
    "axes.titlesize": 8,
    "axes.spines.top": False,
    "axes.spines.right": False,
    "axes.edgecolor": "#8a8a85",
    "axes.labelcolor": "#33332f",
    "xtick.color": "#55554f",
    "ytick.color": "#55554f",
    "axes.grid": False,
})

# Fixed categorical order (validated palette, light mode). Colour follows the version.
VERSION_COLOR = {"clin": "#2a78d6", "clin_nd": "#eb6834", "folk": "#1baf7a",
                 "folk_nd": "#eda100", "folk_rem": "#e87ba4"}
INK, MUTED, GRID = "#33332f", "#8a8a85", "#e4e3df"
WIDTH = 4.8  # inches, LNCS text width


def save(fig, name):
    fig.savefig(OUT / f"{name}.svg", bbox_inches="tight", pad_inches=0.02)
    plt.close(fig)


def fig_effects():
    """Pooled paired differences with 95% case-level bootstrap CI."""
    em = pd.read_csv(TABLES / "pooled.csv")
    ur = pd.read_csv(TABLES / "pooled_urgent.csv")
    labels = {"folk - clin": "folk − clin", "clin_nd - clin": "clin_nd − clin",
              "folk_nd - clin": "folk_nd − clin", "folk_rem - folk": "folk_rem − folk"}
    colors = {"folk - clin": VERSION_COLOR["folk"], "clin_nd - clin": VERSION_COLOR["clin_nd"],
              "folk_nd - clin": VERSION_COLOR["folk_nd"], "folk_rem - folk": VERSION_COLOR["folk_rem"]}
    fig, axes = plt.subplots(1, 2, figsize=(WIDTH, 1.55), sharey=True)
    for ax, df, title in [(axes[0], em, "Emergencies (14 cases)"), (axes[1], ur, "Urgent cases (10 cases)")]:
        df = df.set_index("contrast").loc[list(labels)]
        ys = range(len(df))[::-1]
        ax.axvline(0, color=MUTED, lw=0.8)
        for y, (c, r) in zip(ys, df.iterrows()):
            ax.plot([100 * r.lo, 100 * r.hi], [y, y], color=colors[c], lw=2, solid_capstyle="round")
            ax.plot(100 * r["diff"], y, "o", ms=5, color=colors[c], mec="white", mew=1)
            ax.text(41, y, f"{100 * r['diff']:+.0f}  ({int(r.models_positive)}/9)", va="center",
                    ha="left", fontsize=7, color=INK)
        ax.set_yticks(list(ys), [labels[c] for c in df.index])
        ax.set_xlim(-20, 40)
        ax.set_xticks([-20, 0, 20, 40])
        ax.set_title(title, loc="left", color=INK)
        ax.set_xlabel("Change in under-triage (points)")
    axes[1].tick_params(left=False)
    fig.subplots_adjust(wspace=0.55)
    save(fig, "fig_effects")


def fig_under_over():
    """Mean over the nine models: under-triage of emergencies and over-triage of controls by version."""
    r = pd.read_csv(TABLES / "rates.csv")
    r = r[(r.system == "base") & (r.decoding == "greedy")]
    m = r.groupby("variant")[["under", "over"]].mean() * 100
    fig, axes = plt.subplots(1, 2, figsize=(WIDTH, 1.7))
    # (a) 2x2 interaction: x = diacritics, one line per wording
    ax = axes[0]
    for wording, (a, b) in {"clinical": ("clin", "clin_nd"), "folk": ("folk", "folk_nd")}.items():
        ys = [m.loc[a, "under"], m.loc[b, "under"]]
        ax.plot([0, 1], ys, "-o", color=VERSION_COLOR[a], lw=2, ms=5, mec="white", mew=1)
        ax.text(1.06, ys[1] + (2.5 if wording == "folk" else -2.5), f"{wording} {ys[1]:.0f}%", va="center", fontsize=7, color=INK)
        for x, y in zip([0, 1], ys):
            ax.text(x - 0.06 if x == 0 else x + 0.06, y, f"{y:.0f}%", ha="right" if x == 0 else "left",
                    va="center", fontsize=6.5, color=MUTED) if x == 0 else None
    ax.set_xticks([0, 1], ["with diacritics", "without"])
    ax.set_xlim(-0.35, 1.6)
    ax.set_ylim(0, 60)
    ax.set_ylabel("Under-triage of emergencies (%)")
    ax.set_title("(a) Under-triage", loc="left", color=INK)
    # (b) over-triage on the 28 controls
    ax = axes[1]
    order = ["clin", "clin_nd", "folk", "folk_nd", "folk_rem"]
    for i, v in enumerate(order):
        ax.bar(i, m.loc[v, "over"], width=0.6, color=VERSION_COLOR[v], edgecolor="white", lw=1)
        ax.text(i, m.loc[v, "over"] + 1, f"{m.loc[v, 'over']:.0f}", ha="center", va="bottom", fontsize=6.5, color=INK)
    ax.set_xticks(range(len(order)), order, rotation=30, ha="right")
    ax.set_ylim(0, 60)
    ax.set_ylabel("Over-triage of controls (%)")
    ax.set_title("(b) Over-triage", loc="left", color=INK)
    fig.subplots_adjust(wspace=0.45)
    save(fig, "fig_under_over")


def fig_remedy():
    """Remedy stance on the 24 serious cases (emergency + urgent), per model."""
    d = pd.read_csv(TABLES / "remedy.csv")
    d = d[(d.subset == "all") & d.gold.isin(["emergency", "urgent"])].copy()
    for c in ["endorse", "reject", "not_addressed", "unsafe_endorse"]:
        d[c] = d[c] * d.n
    g = d.groupby("model")[["n", "endorse", "reject", "not_addressed", "unsafe_endorse"]].sum()
    g = g.sort_values("unsafe_endorse")
    short = lambda s: s.replace("-Instruct", "").replace("-v3-7B-Chat", "").replace("gemini-3.5-", "Gemini ")
    stance = [("reject", "#2a78d6", "reject"), ("endorse", "#eb6834", "endorse"),
              ("not_addressed", "#c3c2b7", "not addressed")]
    fig, ax = plt.subplots(figsize=(WIDTH, 2.0))
    for i, (model, r) in enumerate(g.iterrows()):
        left = 0
        for col, color, _ in stance:
            w = r[col]
            ax.barh(i, w, left=left, height=0.62, color=color, edgecolor="white", lw=1)
            left += w
        ax.text(24.6, i, f"{int(round(r.unsafe_endorse))}", va="center", ha="left", fontsize=7, color=INK)
    ax.text(24.6, len(g) - 0.3, "unsafe", va="bottom", ha="left", fontsize=6.5, color=MUTED)
    ax.set_yticks(range(len(g)), [short(m) for m in g.index])
    ax.set_xlim(0, 24)
    ax.set_xticks([0, 6, 12, 18, 24])
    ax.set_xlabel("Answers on the 24 emergency and urgent cases")
    handles = [plt.Rectangle((0, 0), 1, 1, color=c) for _, c, _ in stance]
    ax.legend(handles, [l for *_, l in stance], ncol=3, frameon=False, fontsize=7,
              loc="lower left", bbox_to_anchor=(0, 1.0), handlelength=1.2)
    save(fig, "fig_remedy")


def fig_conditions():
    """Exploratory: under-triage per emergency condition (mean over models) by version."""
    c = pd.read_csv(TABLES / "conditions.csv")
    c = c.replace({"condition": {"Heart attack": "Myocardial infarction", "DKA": "Diabetic ketoacidosis",
                                 "Liver failure": "Liver failure (paracetamol)",
                                 "Rocky Mountain Spotted Fever": "Rocky Mountain spotted fever"}})
    cols = ["clin", "clin_nd", "folk", "folk_nd", "folk_rem"]
    c = c.sort_values("folk_nd", ascending=True)
    vals = c[cols].to_numpy() * 100
    fig, ax = plt.subplots(figsize=(WIDTH, 2.7))
    im = ax.imshow(vals, cmap="Blues", vmin=0, vmax=100, aspect="auto")
    for i in range(vals.shape[0]):
        for j in range(vals.shape[1]):
            v = vals[i, j]
            ax.text(j, i, f"{v:.0f}", ha="center", va="center", fontsize=6.5,
                    color="white" if v >= 55 else INK)
    ax.set_xticks(range(len(cols)), cols)
    ax.xaxis.tick_top()
    labels = [f"{n}" + (" (2 cases)" if k > 1 else "") for n, k in zip(c.condition, c.cases)]
    ax.set_yticks(range(len(c)), labels)
    ax.tick_params(length=0)
    for s in ax.spines.values():
        s.set_visible(False)
    ax.set_xticks([x - 0.5 for x in range(1, len(cols))], minor=True)
    ax.set_yticks([y - 0.5 for y in range(1, len(c))], minor=True)
    ax.grid(which="minor", color="white", lw=1.5)
    cb = fig.colorbar(im, ax=ax, fraction=0.04, pad=0.02)
    cb.set_label("Under-triage (% of answers)", fontsize=7)
    cb.outline.set_visible(False)
    cb.ax.tick_params(labelsize=6.5)
    save(fig, "fig_conditions")


def fig_mitigation():
    """Mean over the four mitigation models: under-triage (clin, folk_nd) and over-triage per prompt."""
    t = pd.read_csv(TABLES / "mitigation.csv")
    m = t.groupby("system")[["under_clin", "under_folk_nd", "over_all"]].mean().loc[["base", "m1", "m2"]] * 100
    x = [0, 1, 2]
    fig, axes = plt.subplots(1, 2, figsize=(WIDTH, 1.6), sharey=True)
    ax = axes[0]
    for col, v, name in [("under_clin", "clin", "clin"), ("under_folk_nd", "folk_nd", "folk_nd")]:
        ax.plot(x, m[col], "-o", color=VERSION_COLOR[v], lw=2, ms=5, mec="white", mew=1)
        ax.text(2.12, m[col].iloc[-1], name, va="center", fontsize=7, color=INK)
    ax.set_title("(a) Under-triage of emergencies", loc="left", color=INK)
    ax2 = axes[1]
    ax2.plot(x, m["over_all"], "-o", color=MUTED, lw=2, ms=5, mec="white", mew=1)
    ax2.set_title("(b) Over-triage of controls", loc="left", color=INK)
    for a in axes:
        a.set_xticks(x, ["base", "M1", "M2"])
        a.set_xlim(-0.3, 2.6)
        a.set_ylim(0, 60)
    axes[0].set_ylabel("% (mean of 4 models)")
    for i, v in enumerate(m["over_all"]):
        ax2.text(i, v + 3, f"{v:.0f}", ha="center", fontsize=6.5, color=INK)
    for col in ["under_clin", "under_folk_nd"]:
        for i, v in enumerate(m[col]):
            axes[0].text(i, v + 3, f"{v:.0f}", ha="center", fontsize=6.5, color=INK)
    save(fig, "fig_mitigation")


if __name__ == "__main__":
    OUT.mkdir(exist_ok=True)
    for f in [fig_effects, fig_under_over, fig_remedy, fig_conditions, fig_mitigation]:
        f()
        print("wrote", f.__name__)
