# Paper 1B figures: editable source

Each figure is an **SVG** file (an XML format) in `svg/`. The text stays as editable text.

**Ways to edit:**
- **Inkscape**: free; recommended.
- **draw.io / diagrams.net**: *File → Import* (imported as an image), or *Extras → Edit Diagram* to paste the SVG in.
- **Figma**: drag the file in.
- **A text editor**: change a word, a colour or a coordinate directly.

After editing, export to PDF for LaTeX:

```bash
uv venv .venv && uv pip install -r requirements.txt   # once
.venv/bin/python export.py                            # svg/*.svg -> ../latex/figures/*.pdf
```

| File | Kind | Source of the numbers | In the paper |
|---|---|---|---|
| `svg/fig_dataset.svg` | hand-drawn diagram | Section 3.1 | Fig. "Dataset construction" (§3.1) |
| `svg/fig_judge.svg` | hand-drawn diagram | Section 4, Appendix A | Fig. "From answer to measure" (§4) |
| `svg/fig_signs.svg` | hand-drawn diagram | keyword check on the Qwen3-8B answers for E05 (`gen/Qwen3-8B__base__greedy.jsonl` on Drive), judge labels | Fig. in §6 Discussion |
| `svg/fig_effects.svg` | chart | `results/tables/pooled.csv`, `pooled_urgent.csv` | §5.1–5.2 |
| `svg/fig_under_over.svg` | chart | `results/tables/rates.csv` | §5.2 |
| `svg/fig_remedy.svg` | chart | `results/tables/remedy.csv` | §5.3 |
| `svg/fig_conditions.svg` | chart | `results/tables/conditions.csv` | §5.4 |
| `svg/fig_mitigation.svg` | chart | `results/tables/mitigation.csv` | §5.5 |

**Charts:**
- `make_charts.py` draws the charts from the result tables in `experiments/1B-folk-triage/results/tables/`.
- When the results change, re-run `.venv/bin/python make_charts.py && .venv/bin/python export.py`.
- Re-running `make_charts.py` **overwrites** the chart SVGs, so any manual edits to a chart are lost. If you edit a chart by hand, stop running the script for that chart, or put the change into the script.

The hand-drawn diagrams (`fig_dataset`, `fig_judge`, `fig_signs`) are never overwritten by a script.

**Colours:** each version has a fixed colour across all charts: clin blue, clin_nd orange, folk aqua, folk_nd yellow, folk_rem pink. This palette passed the colour-blind check (dataviz `validate_palette.js`).
