# 1A paper — outline

> [!summary] Tóm tắt (VI)
> Dàn ý bài báo 1A, viết từ kết quả v4, v4 follow-up, v5, v5 follow-up và v6 (xem [README của pilot](../../experiments/1A-pilot/README.md#results-v4--follow-up--v5--v6)). Bản thảo đầy đủ ở [draft.md](draft.md).
> - **Thông điệp chính:** mất dấu làm LLM mở tiếng Việt mất khoảng một nửa phần năng lực trên mức ngẫu nhiên. Kết quả không phụ thuộc prompt, mô hình lớn hơn mất ít hơn, và lời nhắc trong prompt không giúp gì. Khôi phục dấu bằng một bộ khôi phục riêng lấy lại khoảng 60%, nhưng không giúp trên bình luận vốn được gõ không dấu.
> - **Khác với arXiv 2610.31422:** bài đó đo 4 "decision model" khoảng 300M tham số với một mức nhiễu. Bài này đo 19 LLM sinh văn bản (1,5–14B), có đường liều–đáp ứng, phân tích tokenizer và độ bất ngờ, so sánh cách giảm thiểu, và thêm dữ liệu không dấu tự nhiên.
> - **Phải ghi là hạn chế:** tập không dấu tự nhiên nhỏ, cơ chế của Δ broken chưa rõ, mô hình lớn nhất 14B, chỉ có một bộ khôi phục dấu.
> - **Còn phải làm trước khi nộp:** kiểm chứng các trích dẫn đánh dấu `[TODO verify]`, đọc bài ViSoBERT để xác nhận phần nói về bỏ dấu, chọn hội nghị, chuyển sang LaTeX.

**Working title:** *Reading Without Diacritics: How Open LLMs Lose, and Partly Recover, Vietnamese Understanding When Tone Marks Disappear*

**Format:** ACL-style long paper, 8 pages + limitations + appendix. Venue to decide (see the end of this file).

## One-sentence claim

Removing diacritics costs open LLMs about half of their above-chance accuracy on Vietnamese tasks, regardless of the prompt. Larger models lose less. Telling the model the text is unaccented does nothing, while a separate diacritic restorer recovers about 60% of the loss on synthetic text, but not on text people actually typed without marks.

## Contributions

1. **Measurement.** 19 open instruction-tuned LLMs (1.5–14B, 8 families, including 3 Vietnamese-adapted) × 5 tasks × 7 noise conditions, with a validity gate fixed before any noisy result was seen.
2. **Dose-response and comparison with teen code.** Monotone loss in the share of stripped words (97% of valid pairs with 3 seeds). Teen code looks harmless only because it changes few words; at an equal dose it does similar damage.
3. **Robustness of the finding.** Four prompt templates (incl. English instructions) give the same drop and the same model ranking.
4. **Scale.** −0.086 normalised drop per doubling of parameters, continuing to 14B.
5. **Mechanism evidence.** On the same noisy item, the model that finds it more surprising (ΔNLL) errs more, also within one tokenizer. Tokenizer fragmentation does not explain the loss. The broken-syllable change has a robust *negative* sign that we report as open.
6. **Mitigation.** Prompt hint vs automatic restoration on the same pairs, plus a test on naturally unaccented comments where restoration does not help.
7. **Release:** noise suite, notebooks with built-in checks, per-item debug files.

## Section plan (page budget)

| § | Section | Pages | Content | Source |
|---|---|---|---|---|
| 1 | Introduction | 1 | Unaccented Vietnamese is common (chat, search, old keyboards). Two questions people ask: how much do LLMs lose, and does it help to restore or to warn the model? Contributions list | — |
| 2 | Related work | 0.75 | Vietnamese robustness (2610.31422, ViSoBERT, dialect study), diacritics and tokenization, diacritic restoration, synthetic vs natural noise, evaluation methodology | §Related work below |
| 3 | Setup | 1.5 | Tasks and items, noise conditions, models, prompting and scoring (letter answers, prefill, batch calibration), validity gate, metrics, statistics | v4 protocol table |
| 4 | How much is lost (RQ1) | 1.25 | Strip drop per task, dose-response, seeds, teen code at equal dose, label collapse, robustness to scoring choices, **prompt templates** | v4, F1, F3, F5, v5 seeds, v6-A |
| 5 | Who is robust (RQ2) | 0.75 | Size trend incl. 14B, within-family tests, Vietnamese-adapted models (not significant), Qwen2.5 vs SeaLLMs same tokenizer | v4, F2, v6-B |
| 6 | Why (RQ3) | 1 | Same-item FE model: ΔNLL, ambiguity, Δtokens, Δbroken; same-tokenizer subset; Δbroken sign checks (G2) incl. phi-4 | v4, F4, F6, G2, v6-B |
| 7 | Can it be fixed? (RQ4) | 1 | Hint vs restoration; restoration per task and per 14B model; restorer accuracy on informal text (G1); natural unaccented ViHSD | v5, G1, v6-A, v6-C |
| 8 | Discussion | 0.5 | What to tell practitioners; synthetic vs natural gap | — |
| 9 | Limitations, ethics | 0.5 | See below | — |

## Figures and tables for the main text

| # | What | From |
|---|---|---|
| Fig 1 | Dose-response (a) and strip vs teen code vs mixed (b) | `fig05_effect` + `figF3_teencode_dose` (merge: x = share of words changed) |
| Fig 2 | Forest plot of strip drop per (model, task) | `fig06_forest_strip`, add the 14B models |
| Fig 3 | Drop vs size per family, 1.5–14B | `fig15_size_and_tokenizers` (a) |
| Fig 4 | Item-level FE coefficients + binned ΔNLL vs flips | `fig09_mechanism` |
| Fig 5 | Hint vs restoration recovery per task | `fig14_hint_vs_restoration` |
| Tab 1 | Tasks, classes, items, % syllables with diacritics | v4 step 1, `fig01_data` |
| Tab 2 | Models: family, size, adapted?, tokenizer, clean acc. | v4 setup + v6 |
| Tab 3 | Strip drop and restoration recovery per task | README v4 RQ1 + v5 restoration table |
| Tab 4 | Prompt templates: mean drop, CI, Spearman | v6-A |
| Tab 5 | Natural unaccented ViHSD | v6-C |

**Appendix:** validity gate per pair (`fig04_validity`), prediction shift and label collapse (`fig10_prediction_shift`, `figF1_collapse`), tokenizer statistics (`fig03_tokenizers`), seed stability (`fig12_seed_stability`), restoration error analysis (`figG1_restoration_errors`), Δbroken checks (`figG2_broken`), adapted vs general (`figF2_adapted`), the four prompt templates verbatim, teen-code table, full per-pair numbers.

## Related work: what to say about each

- **Ha et al. 2026, arXiv 2610.31422** (closest). Four zero-shot "decision models" (JEV via API; LAYA 322M, GLiNER2.5-multi-Decide 287M, Quyet-1.0-Small 328M) on 13 Vietnamese classification settings. Diacritic removal is the most damaging perturbation: −9.51 to −15.47 mean macro-F1, worse than teencode (≤ 1.1) and typos (≤ 4.5); a decrease in 47 of 48 model-setting comparisons. LLM numbers are copied from Thin et al. 2024, not re-run under noise.
  - *What they do not do* (checked in their text): partial removal / dose-response, restoration as mitigation, prompt variation (only label-description language EN/VI/EN+VI), model size, tokenizer analysis, naturally unaccented text, generative LLMs under noise.
  - *How we differ:* generative LLMs 1.5–14B; dose-response; per-item mechanism; mitigation; natural text. *How we agree:* diacritic removal ≫ teencode. We add that this ranking partly reflects dose (F3); their teencode changes 2.1% of characters vs 18.3% for no-accents, consistent with that reading.
  - Overlap of datasets: UIT-VSFC, UIT-VSMEC, ViHSD. Our numbers are not directly comparable (accuracy/normalised drop vs macro-F1; different models).
- **Nguyen et al. 2023, ViSoBERT (EMNLP).** Cited by 2610.31422 as reporting degradation under diacritic removal. `[TODO verify]` read the ViSoBERT paper and state exactly what they test before citing that claim.
- **Dialect robustness, arXiv 2608.10414.** Regional dialect variation, not diacritics. `[TODO verify]` authors and venue.
- **"Don't Touch My Diacritics", arXiv 2410.24140.** Position paper on diacritic handling and tokenization. `[TODO verify]` authors.
- **Tokenizer fairness and fertility:** Rust et al. 2021 (ACL, "How good is your tokenizer?"); Petrov et al. 2023 (NeurIPS, tokenizer unfairness across languages). Our result: fertility change does not explain the loss.
- **Synthetic vs natural noise:** Belinkov & Bisk 2018 (ICLR). Motivates §7's natural-text test. ViLexNorm (Nguyen et al. 2024, EACL) for unaccented and non-standard Vietnamese social-media text.
- **Diacritic restoration for Vietnamese:** the restorer we use (`peterhung/vietnamese-accent-marker-xlm-roberta`, XLM-R large token classifier). `[TODO]` cite 1–2 published Vietnamese restoration papers and one benchmark.
- **Evaluation method:** batch calibration (Zhou et al. 2024, ICLR); CheckList (Ribeiro et al. 2020) and TextFlint (Wang et al. 2021) as perturbation-testing frameworks; SailCompass (arXiv 2412.01186) for SEA LLM evaluation robustness `[TODO verify]`.

## Limitations to state

- Natural unaccented set: 226 items, unbalanced; CIs wide. Cannot separate "weak restorer on informal text" from "models already read habitual unaccented writing".
- Largest model is 14B; no closed or very large models.
- One restorer; its word accuracy is 75–93% (mean 83.4%, below our pre-set 85% target).
- Δbroken mechanism unexplained; we do not claim broken syllables cause the loss.
- Single-token letter answers with a label-blind prefill: this measures understanding, not free-form generation. Free-generation agreement ≥ 0.7 is gated, but generation tasks are not covered.
- Teen-code table is small and hand-written.
- 6 of 80 v4 pairs excluded by the gate (results barely change when kept, F5).

## Before submission

- [ ] Verify every `[TODO verify]` citation; read ViSoBERT's diacritic experiment.
- [ ] Regenerate Fig 1 (merged dose plot) and Fig 2 (forest with the 14B models) from Drive.
- [ ] Pull per-task item counts and % diacritic syllables into Tab 1 from v4 `tables/`.
- [ ] Fill the Δtokens coefficient sign and size from v4 `tables/` (README has only p).
- [ ] Ask a second native speaker to check the teen-code table.
- [ ] Release: clean the notebooks into a repo, upload noisy items (check dataset licences: UIT datasets need a request form).
- [ ] Choose venue. Candidates: PACLIC, KSE, SoICT (fast, regional), or an ACL-family Findings / workshop on multilingual or low-resource NLP. Decide before converting to the venue's LaTeX template.
