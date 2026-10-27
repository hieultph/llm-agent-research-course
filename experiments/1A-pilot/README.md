# 1A pilot — diacritic noise vs. accuracy

> [!summary] Tóm tắt (VI)
> Thí nghiệm thử cho ý tưởng 1A trên Colab, kết quả lưu vào Google Drive.
> **v1** (mô hình 1.5B) cho thấy Qwen2.5 giảm từ 0.72 xuống 0.35 khi bỏ hết dấu, nhưng một nửa số mô hình chạy chưa đúng.
> **v2** sửa lỗi đó, dùng mô hình 4–8B và thêm phân tích theo từng câu.
> **v2.1** sửa lỗi nhãn của Phi, kiểm soát độ dài câu, chạy 15 mô hình (1.5–8B, 5 họ có nhiều cỡ) trên 5 bộ dữ liệu. Khoảng 5–7 giờ trên L4 (15–20 CU), chạy được thành nhiều phiên.
> **v2.2** không chạy mô hình: kiểm tra lại dữ liệu và output của v2.1, sửa các phân tích còn yếu, và vẽ hình/bảng cho bài báo. Chạy trên CPU, khoảng 5 phút.
> **v3** sửa 3 điểm v2.2 tìm ra:
> - chấm lại Qwen3 và bloomz theo định dạng trả lời chúng thích (chọn định dạng mà không nhìn nhãn đúng);
> - VinaLLaMA-2.7b dùng chung template ChatML với bản 7b;
> - NLL của ViMMRC chỉ tính trên câu hỏi + đáp án.
>
> Chạy khoảng 2–3 giờ trên L4, sau đó chạy notebook phân tích v3 trên CPU.
>
> **v4 — bản chuẩn, nên dùng bản này.** Làm lại từ đầu dựa trên mọi lỗi của v1–v3, trong một notebook chạy từng bước:
> - mỗi bước có kiểm tra tự động; notebook dừng lại nếu có kiểm tra thất bại;
> - trả lời trắc nghiệm bằng một chữ cái (một token, được kiểm tra trên từng mô hình);
> - định dạng trả lời và hiệu chỉnh lấy từ tập dev riêng; dùng đúng chat format của từng mô hình;
> - NLL lấy từ cùng lượt chạy;
> - cổng hợp lệ được chốt trước khi xem kết quả nhiễu;
> - có CI bootstrap và hiệu chỉnh Holm;
> - xuất 10 hình, các bảng LaTeX và phần kết luận tự sinh.
>
> Chạy khoảng 3–4 giờ trên L4.

Idea: [[phase-1-ideas]] (1A)

| Notebook | Models | Results on Drive | Open |
|---|---|---|---|
| [1A_pilot_v4.ipynb](1A_pilot_v4.ipynb) — **use this: clean, step-by-step, GPU then CPU** | 15 open 1.5–8B models (+ Llama-3.2-3B with the `HF_TOKEN` secret) × 5 tasks | `MyDrive/llm-research/1A-pilot-v4/` (figures, LaTeX tables, `conclusions.md`) | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/hieultph/llm-agent-research-course/blob/main/experiments/1A-pilot/1A_pilot_v4.ipynb) |
| [1A_pilot_v3.ipynb](1A_pilot_v3.ipynb) — superseded by v4 | re-scores Qwen3 ×3, bloomz ×3, VinaLLaMA-2.7b; adds ViMMRC question + options NLL for all 16 | `MyDrive/llm-research/1A-pilot-v3/` (same layout as v2.1) | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/hieultph/llm-agent-research-course/blob/main/experiments/1A-pilot/1A_pilot_v3.ipynb) |
| [1A_pilot_v3_analysis.ipynb](1A_pilot_v3_analysis.ipynb) — **CPU, run second** | the v2.2 analysis on the v3 results | `MyDrive/llm-research/1A-pilot-v3-analysis/` | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/hieultph/llm-agent-research-course/blob/main/experiments/1A-pilot/1A_pilot_v3_analysis.ipynb) |
| [1A_pilot_v2.2_analysis.ipynb](1A_pilot_v2.2_analysis.ipynb) — **analysis of v2.1, CPU only** | reads v2.1 | `MyDrive/llm-research/1A-pilot-v2.2/` (figures as PNG + PDF, tables as CSV + LaTeX) | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/hieultph/llm-agent-research-course/blob/main/experiments/1A-pilot/1A_pilot_v2.2_analysis.ipynb) |
| [1A_pilot_v2.1.ipynb](1A_pilot_v2.1.ipynb) — superseded by v4 | 15 open 1.5–8B models (+4 gated) × 5 tasks | `MyDrive/llm-research/1A-pilot-v2.1/` | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/hieultph/llm-agent-research-course/blob/main/experiments/1A-pilot/1A_pilot_v2.1.ipynb) |
| [1A_pilot_v2.ipynb](1A_pilot_v2.ipynb) — kept with its outputs | 7 open 4–8B models, VSFC only | `MyDrive/llm-research/1A-pilot-v2/` | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/hieultph/llm-agent-research-course/blob/main/experiments/1A-pilot/1A_pilot_v2.ipynb) |
| [1A_pilot.ipynb](1A_pilot.ipynb) — v1, kept with its outputs | 6 models, 1.5–2.7B | `MyDrive/llm-research/1A-pilot/` | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/hieultph/llm-agent-research-course/blob/main/experiments/1A-pilot/1A_pilot.ipynb) |

## Run it on Colab

1. Click the badge above.
2. **Runtime → Change runtime type → L4 GPU**. The notebook already asks for L4, but check.
3. Optional, for the gated models (Llama-3.1, Vistral, Aya): accept each model's licence on Hugging Face, then add your token as `HF_TOKEN` in Colab's 🔑 **Secrets** panel.
4. **Runtime → Run all**. Allow Google Drive access when asked.
5. When it finishes: **Runtime → Disconnect and delete runtime**.

If Colab disconnects, run all again. Models already saved in `preds/` are skipped. A model that fails to load is listed and skipped, not a crash.

## v4: the clean protocol

Each design choice fixes a problem found in v1–v3. The full table is at the top of the notebook.

| Step | What it does | What stops the run |
|---|---|---|
| 1. Data | Dev = validation split, test = test split. NFC; duplicates, conflicting labels, items under 3 syllables and items with no diacritic are removed. Balanced sample per class | Dev/test overlap; unbalanced test |
| 2. Noise | 7 conditions on the input fields only | `strip` leaves a diacritic; `partial*` changes anything besides diacritics; noise is not deterministic |
| 3. Prompts (CPU) | Each model's documented chat format (ChatML for VinaLLaMA-2.7b, plain for bloomz). Options are A/B/C…. Tokenizer stats are computed on the tokens inside the real prompt | An answer letter is not one distinct token; the prompt exceeds the context |
| 4. Models (GPU) | Answer prefill chosen on dev (label-blind). Calibration prior from clean dev. One forward pass gives both the answer and the per-field NLL. A free-generation check runs on 40+40 items | — |
| 5. Audit | Files complete and reproducible. **Validity gate** fixed in advance: letter mass ≥ 0.5, generation agreement ≥ 0.7, clean-accuracy CI above chance | Any integrity failure |
| 6–9. Analysis | RQ1 effect (dose-response, teen code, robustness to scoring choices); RQ2 size within family (Holm) and Vietnamese-adapted models; RQ3 tokenizer vs exposure (same-item two-way FE, same-tokenizer test, ambiguity); prediction shift | — |
| 10. Conclusions | `conclusions.md` is generated from the numbers, with a *Limitations* list | — |

Figures `fig01`–`fig10` are saved as PNG and PDF with captions in `figures/captions.csv`. Tables are in `tables/` (CSV and LaTeX).

## What v3 changes

| v2.2 finding | v3 |
|---|---|
| Qwen3 and bloomz put < 50% of their probability on the label words in 19 (model, task) pairs. Qwen3 answers in markdown; bloomz answers empty or in English | **Answer format chosen per (model, task), label-blind.** Four candidate formats are scored on 40 clean items; the one with the highest median label mass wins: `v21`, `start` (no prefill, optional `**`), `q_last` (instruction after the input, as in bloomz's xP3 training), `q_last_en` (also English label words). `v21` is kept unless another beats it by ≥ 0.02 |
| `vinallama-2.7b-chat` has no chat template, so it got a plain prompt while the 7b got ChatML | The 2.7b uses the **7b's ChatML template**. `<|im_start|>` is a single token in its vocabulary |
| ViMMRC ΔNLL was mostly the article (~83% of the syllables) | **`nll_qo`**: NLL of question + options only, for all 16 models |

Everything else is unchanged: same items (checked against the v2.1 file), calibration and tokenizer stats. Unchanged predictions are copied from v2.1. Label variants are scored as continuations of a cached prompt, which gives the same numbers as v2.1's from-scratch scoring (within 1e-5) at a fraction of the cost.

The v3 notebook ends with these tables:
- the format chosen for each (model, task);
- a check that the `v21` candidate reproduces v2.1's stored label mass;
- before/after values for the 7 changed models: accuracy, label mass, tier and strip `norm_drop`;
- ViMMRC perplexity ratios on the whole item vs on question + options.

## What v2.2 found (audit and corrected analysis of the v2.1 run)

**The benchmark is sound.**

- **Items:** the rebuilt items match the ones the run used, 9135/9135.
- **Prediction files:** all 80 (model, task) files are complete. The stored predictions and label mass can be recomputed from the stored log-probs. Every model saw the same items with the same labels.
- **Noise:**
  - Partial removal hits its nominal rate (0.25 / 0.50 / 0.75, ±0.003).
  - `strip` leaves no diacritic.
  - Partial and strip change nothing except diacritics.
- **Reused v2 VSFC files:** the label tokens are identical to v2.1's for the 6 reused models (300/300), so reuse was valid.
- **Label mass under `strip`:** it barely moves (|Δ| ≤ 0.1, except bloomz-1b7). The drop is a change of judgement, not of answer format.

| Question | Result |
|---|---|
| Size of the effect | Mean normalised drop under `strip` (reliable pairs): VSFC 0.57, VSMEC 0.56, XNLI 0.52, ViHSD 0.41, ViMMRC 0.36. Teen code ≤ 0.10. |
| Does calibration hide part of it? | Slightly. Calibrating noisy items with the **clean** prior (what a deployed system knows) gives 0.64 / 0.58 / 0.56 / 0.43 / 0.38. Under `strip`, raw predictions shift toward *tiêu cực* (VSFC), *mâu thuẫn* (XNLI) and *khác* (VSMEC). |
| Tokenizer or exposure? (model level) | Within each condition, Δfertility has ρ ≈ 0 with the drop, and log perplexity ratio has ρ 0.29–0.45. In OLS with condition and task fixed effects: perplexity ratio +0.12 per SD (p < 0.001), Δfertility n.s., Δbroken n.s. |
| Tokenizer or exposure? (same noisy item) | With item × condition fixed effects, the model that finds the noisy item more surprising flips more: **+2.2 pp per SD of ΔNLL** (all models, p < 0.001), +3.7 pp on reliable pairs. It holds within one tokenizer (Qwen2.5 / Qwen3 / SeaLLMs: +2.4 pp) and in 4 of 5 tasks (not ViHSD). Δtokens and Δbroken are n.s. everywhere. **This is the cleanest test in the pilot.** |
| Tokenizer or exposure? (pooled logit) | Without item fixed effects the picture is unstable. Δtokens and Δbroken are collinear (r = 0.86) and take opposite signs, so do not report that model as the main result. |
| Lexical ambiguity | Among partial/strip items, stripped words with more accented readings predict flips (+0.09 per SD, p = 0.003). |
| Scale within a family | Larger is more robust on VSFC for Qwen2.5, Qwen3 and SeaLLMs (all CIs exclude 0), and for Qwen2.5 on ViHSD. Most other task × family differences have CIs that include 0. VinaLLaMA 2.7→7B is never more robust, and is significantly worse on VSMEC. |
| Qwen2.5-3B vs Llama-3.2-3B | Llama loses more on VSFC (+0.44) and XNLI (+0.60), both CIs excluding 0, at a similar Δfertility. Null on the other 3 tasks. |
| Real noise in ViHSD | **Null** once the label is controlled for (originally unaccented vs fully accented comments: logit −0.30, p = 0.17). Do not claim it. |
| Agreement across models | Models only weakly agree on *which* items flip (mean r = 0.25). |

**Caveats that remain** (need a GPU run, v3):

- **Low label mass:** Qwen3 and bloomz carry little probability on the labels on several tasks. Their results are shown with a † ("gated" tier), not dropped.
- **Prompt format confound:** VinaLLaMA-2.7b-chat ships **without a chat template**, so it got a plain prompt, while VinaLLaMA-7b-chat got ChatML. This confounds the VinaLLaMA size comparison.
- **Prediction collapse:** 16 reliable (model, task, condition) cells still put > 60% of calibrated predictions on one label. Examples: Llama-3.2-3B on VSFC under noise, and Qwen2.5-3B on XNLI.
- **ViMMRC NLL** is still computed over the whole article.

## What v2 taught us (and what v2.1 changes)

| v2 finding | v2.1 change |
|---|---|
| All 7 models passed the gate; normalised drop under `strip` ranged from 0.17 (Qwen3-8B) to 0.68–0.70 (VinaLLaMA, bloomz). | Same method, so v2 and v2.1 VSFC numbers are comparable. VSFC predictions are **reused from v2** (items verified identical: 2100/2100 rows), except Phi-3.5. |
| Phi and Mistral get *fewer* tokens when diacritics are stripped (fertility 2.9 → 1.8), yet they drop most: evidence against "fragmentation causes the drop". Model level: Δfertility ρ ≈ 0, perplexity ratio ρ = 0.50. Item level: ΔNLL predicts flips (+0.22, p < 0.001), Δtokens does not. | Tested again on 5 tasks and 15 models. |
| Phi-3.5 label mass 0%: " tiêu cực" tokenized alone gets an extra `'▁'` token. | **Labels tokenized in context** (prompt + label, minus prompt). |
| "Broken syllables" had a negative coefficient (−0.36), suspected length confound. | **log(length)** added to every item-level regression. |
| One size per family. | **5 families with 2–3 sizes** (Qwen2.5 1.5/3/7B, Qwen3 1.7/4/8B, SeaLLMs 1.5/7B, VinaLLaMA 2.7/7B, bloomz 1.7/3/7B): size effects with the tokenizer held fixed. |
| One task. | **5 tasks**: VSFC (sentiment), VSMEC (7 emotions), ViHSD (hate speech; only 68% of the original syllables carry diacritics, vs ~86% in edited text), XNLI-vi (inference), ViMMRC (reading comprehension, scored in one forward pass). |
| Qwen3 (1.6%) and bloomz (5%) put little probability on the labels. | Item-level model repeated on pairs with label mass ≥ 50% only. |

## What v1 taught us (and what v2 changes)

| v1 finding | v2 change |
|---|---|
| Qwen2.5-1.5B: 0.72 → 0.35 (strip), VinaLLaMA-2.7B: 0.63 → 0.41. The drop is smooth, with no cliff. | Same noise levels kept, so v1 and v2 are comparable. |
| SeaLLMs at chance. **Cause:** it answers correctly but in its own words ("Nhãn: tiêu cực", "Phân loại … là tiêu cực"), so only 22% of its probability fell on the labels at the first answer token. | **Answer prefilled with "Nhãn:"**. On 30 items: label mass 22% → 97%, accuracy 0.33 → 0.77. |
| Content-free calibration collapsed Qwen3 to one class (raw 0.67 → 0.34). | **Batch calibration** (Zhou et al. 2024): subtract the mean label distribution over the items of each condition. |
| 3 of 6 models at chance, so floor effects inflated the correlation (ρ≈0.62). | 4–8B models, a **sanity gate** (clean accuracy ≥ 0.45), and a **normalised drop** = drop ÷ (clean − ⅓). |
| Teen code changed almost nothing. | Larger table, plus **`mixed`** = teen code, then strip 50%. |
| Qwen2.5, Qwen3 and SeaLLMs share one tokenizer: a natural control for "tokenizer vs exposure". | Kept on purpose at 7–8B. Mistral-7B vs Vistral-7B adds a second pair if you have `HF_TOKEN`. |
| ~30 model × condition points are too few. | **Item-level logistic regression**: flip ~ Δtokens + broken syllables + ΔNLL, with model and condition fixed effects and SEs clustered by item. |

## What v2 produces (in `MyDrive/llm-research/1A-pilot-v2/`)

| File | Contents |
|---|---|
| `noisy_items.csv` | 300 UIT-VSFC test items (100 per class) × 7 conditions |
| `tokenizer_items.csv` / `tokenizer_stats.csv` | tokens, broken syllables and byte fragments per item, and aggregated per model × condition |
| `preds/<model>.csv` | per-item label log-probs, label mass, raw and batch-calibrated predictions, sentence NLL |
| `diagnostics.csv` | 6 free (greedy) answers per model: what the model actually says |
| `summary.csv` | accuracy, macro-F1, drop with 95% bootstrap CI, normalised drop, perplexity ratio, Δ tokenizer stats |
| `item_level.csv` | one row per (model, item, noisy condition) that was correct when clean, with its predictors |
| `pilot_v2_plots.png` | accuracy by condition; normalised drop vs Δfertility; normalised drop vs perplexity ratio |

## Design choices to remember for the paper

- **Label scoring after a prefilled "Nhãn:"**, summing both casings ("tiêu cực" / "Tiêu cực"). No answer parsing.
- **Batch calibration** is the main prediction; raw predictions are kept as `pred_raw`. Report both.
- **Noise only on the input sentence**: the instruction and labels stay clean.
- **Per-syllable normalisation uses the clean sentence**, so teen code abbreviations do not look artificially cheap.
- **Partial removal** strips an exact share of the syllables that *carry* diacritics.
- The teen code table is still small and needs your check as a native speaker.

## Tested

- **v1** ran on Colab L4 with 6 models (results above).
- **v2** ran on Colab L4 with 7 models, VSFC (results above).
- **v2.1** was smoke-tested on CPU with tiny models and 2 items per class:
  - **All sections ran on all 5 tasks:** Qwen2.5-0.5B (BPE, chat template) and bloomz-560m (no chat template).
  - **The label fix works:** TinyLlama (SentencePiece, like Phi) gets 79% label mass on VSFC; Phi got 0% in v2. It was stopped after 2 tasks because it is slow on CPU.
  - **Reuse and skip paths work:** v2 reuse was tested with a simulated v2 folder, and a nonexistent model name is skipped cleanly.
  - **VSFC items are identical to v2 at full size** (2100/2100 rows).
  - **Memory:** the first smoke run ran out of RAM on ViMMRC. Scoring now uses chunked log-probabilities (same values within 1.4e-6) and a 4096-token budget.
- **v2.1** then ran on Colab L4 with 16 models (outputs are in the notebook).
- **v2.2** was tested locally on synthetic predictions with real tokenizer stats, then ran on Colab CPU on the real v2.1 results with no errors (outputs are in the notebook).
- **v3** was tested on CPU, end to end, with tiny random-weight models that use each model's real tokenizer and architecture (16 models, all 5 tasks, full size), on a synthetic v2.1 folder:
  - **Cached scoring is exact:** label scores from the cached prompt equal scoring (prompt + label) from scratch within 1e-5, for the Qwen3, Bloom and Llama architectures.
  - **Every path ran:** the format probe, re-scoring, ChatML for VinaLLaMA-2.7b (`<|im_start|>` = one token), NLL-only models, and a gated model without a token (copied without `nll_qo`; the analysis says so and leaves it out).
  - **The analysis notebook** then ran on that output with no errors.
  - **Not yet run on a GPU with the real models.** Which format wins for Qwen3 and bloomz will only be known from that run.
- **v4** was tested end to end on CPU on full-size real data, with 16 tiny random-weight models that use each model's real tokenizer, chat template and architecture (4 items per class):
  - **All checks pass,** including single-token answer letters for all 16 real tokenizers and every chat template copying the message verbatim.
  - **The validity gate stops bad results:** the integrity check stopped the run on a false alarm, which was then fixed.
  - **The analysis steps were exercised:** synthetic answers with a known signal were used for this, and all 10 figures and the conclusions were produced.
  - **It has not yet run on a GPU with the real models.**
