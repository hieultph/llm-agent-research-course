# 1A pilot — diacritic noise vs. accuracy

> [!summary] Tóm tắt (VI)
> Thí nghiệm thử đầu tiên cho ý tưởng 1A, chạy trên Colab (L4, khoảng 30–45 phút, 2–3 CU). Kết quả lưu vào Google Drive.

Notebook: [1A_pilot.ipynb](1A_pilot.ipynb) · Idea: [[phase-1-ideas]] (1A)

## Run it on Colab

1. Open the notebook straight from GitHub: [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/hieultph/llm-agent-research-course/blob/main/experiments/1A-pilot/1A_pilot.ipynb)
   The repo is private, so the first time, Colab asks you to authorize GitHub. If the link fails: Colab → **File → Open notebook → GitHub** tab → tick **Include private repos** → pick the notebook.
2. **Runtime → Change runtime type → L4 GPU** (T4 also works, slower).
3. Optional, for Gemma and Llama: accept each model's licence on Hugging Face, then add your token as `HF_TOKEN` in Colab's 🔑 **Secrets** panel.
4. **Runtime → Run all**. Allow Google Drive access when asked.
5. When it finishes: **Runtime → Disconnect and delete runtime**.

If Colab disconnects, run all again. Models already saved in `preds/` are skipped.

## What it produces (in `MyDrive/llm-research/1A-pilot/`)

| File | Contents |
|---|---|
| `noisy_items.csv` | 300 UIT-VSFC test items (100 per class) × 6 noise conditions |
| `tokenizer_stats.csv` | fertility, broken-syllable rate, byte-fragment rate per model × condition |
| `preds/<model>.csv` | per-item label log-probs, raw and calibrated predictions, sentence NLL |
| `summary.csv` | accuracy, macro-F1, drop with 95% bootstrap CI, perplexity ratio, Δ tokenizer stats |
| `pilot_plots.png` | accuracy by condition; drop vs Δfertility; drop vs perplexity ratio |

## Design choices to remember for the paper

- **Label scoring, not generation**: each label's log-probability after the prompt, summing both casings ("tiêu cực" / "Tiêu cực").
- **Contextual calibration** (Zhao et al. 2021) is the main prediction, because small models prefer one label regardless of input. Qwen2.5-0.5B answered "Tiêu cực" to everything in testing. Raw predictions are kept as `pred_raw`.
- **Noise only on the input sentence**: the instruction and labels stay clean.
- **Per-syllable normalisation uses the clean sentence**, so teen code abbreviations do not look artificially cheap.
- **Partial removal** strips an exact share of the syllables that *carry* diacritics.
- The teen code table is small and still needs your check as a native speaker.

## Tested

The full notebook ran end to end on CPU with two small models (Qwen2.5-0.5B, bloomz-560m) on 18 items. It has not been run yet with the six pilot models on GPU.
