# 1A pilot — diacritic noise vs. accuracy

> [!summary] Tóm tắt (VI)
> Thí nghiệm thử cho ý tưởng 1A trên Colab, kết quả lưu vào Google Drive.
> **v1** (mô hình 1.5B) cho thấy Qwen2.5 giảm từ 0.72 xuống 0.35 khi bỏ hết dấu, nhưng một nửa số mô hình chạy chưa đúng.
> **v2** sửa lỗi đó, dùng mô hình 4–8B và thêm phân tích theo từng câu. Chạy v2 trên L4 khoảng 1–1,5 giờ, 3–5 CU.

Idea: [[phase-1-ideas]] (1A)

| Notebook | Models | Results on Drive | Open |
|---|---|---|---|
| [1A_pilot_v2.ipynb](1A_pilot_v2.ipynb) — **use this** | 7 open 4–8B models (+3 gated) | `MyDrive/llm-research/1A-pilot-v2/` | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/hieultph/llm-agent-research-course/blob/main/experiments/1A-pilot/1A_pilot_v2.ipynb) |
| [1A_pilot.ipynb](1A_pilot.ipynb) — v1, kept with its outputs | 6 models, 1.5–2.7B | `MyDrive/llm-research/1A-pilot/` | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/hieultph/llm-agent-research-course/blob/main/experiments/1A-pilot/1A_pilot.ipynb) |

## Run it on Colab

1. Click the badge above.
2. **Runtime → Change runtime type → L4 GPU**. The notebook already asks for L4, but check.
3. Optional, for the gated models (Llama-3.1, Vistral, Aya): accept each model's licence on Hugging Face, then add your token as `HF_TOKEN` in Colab's 🔑 **Secrets** panel.
4. **Runtime → Run all**. Allow Google Drive access when asked.
5. When it finishes: **Runtime → Disconnect and delete runtime**.

If Colab disconnects, run all again. Models already saved in `preds/` are skipped. A model that fails to load is listed and skipped, not a crash.

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
- **v2** ran end to end on CPU with two tiny models and one model name that does not exist (to test the skip path), on 18 items. The prefill fix was checked separately on SeaLLMs-v3-1.5B, 30 items. v2 has not run yet with the 4–8B models on GPU.
