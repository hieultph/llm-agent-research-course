# Reading Without Diacritics: How Open LLMs Lose, and Partly Recover, Vietnamese Understanding When Tone Marks Disappear

> [!summary] Tóm tắt (VI)
> Bản thảo đầu tiên, viết bằng tiếng Anh để chuyển sang LaTeX sau. Mọi con số lấy từ [README của pilot](../../experiments/1A-pilot/README.md#results-v4--follow-up--v5--v6) (v4–v6). Dàn ý, danh sách hình/bảng và các việc còn lại ở [outline.md](outline.md).
> - `[TODO]` đánh dấu chỗ còn thiếu số liệu hoặc trích dẫn chưa kiểm chứng.
> - `[FIG n]` / `[TAB n]` là chỗ đặt hình và bảng.

*Draft 1, 2026-10-29. Authors and affiliations TBD.*

## Abstract

Vietnamese is often typed without diacritics, yet the marks carry tone and vowel identity, so "ban" can be *bạn* (friend), *bán* (sell) or *bàn* (table). We measure how much open large language models lose when diacritics disappear, why, and what helps. We evaluate 19 instruction-tuned models (1.5–14B parameters, 8 families, 3 Vietnamese-adapted) on five tasks: sentiment, emotion, hate speech, natural language inference and reading comprehension. We use seven noise conditions and a validity gate fixed before any noisy result was seen. Removing all diacritics costs a model 41–67% of its above-chance accuracy, depending on the task, and the loss grows monotonically with the share of stripped words. The effect is the same under four prompt templates, including English instructions (Spearman ≥ 0.95 between model rankings). Larger models lose less: −0.086 normalised drop per doubling of parameters, a trend that continues to 14B. On the same noisy item, the model that finds the input more surprising errs more, including among models that share a tokenizer, whereas the change in tokenizer fragmentation does not explain the loss. Telling the model that the text may lack diacritics recovers nothing (−1%). Restoring the diacritics with a separate XLM-R-based restorer before prompting recovers 60%. However, on 226 comments their authors actually typed without diacritics, restoration does not help (+0.01 balanced accuracy, 95% CI [−0.02, 0.04]). We release the noise suite, the notebooks with their built-in checks, and per-item predictions.

## 1 Introduction

Vietnamese writes tone and vowel quality with diacritics. Six tones and several modified vowels mean that one unaccented string can stand for many words: *ban* can be *bạn, bán, bàn, bản, bận, băn…*. Readers resolve this from context, and many people type without diacritics in chat, comments and search, on keyboards without a Vietnamese input method, or simply out of habit. A model deployed on Vietnamese user text will see this input.

Recent work shows that diacritic removal is the most damaging perturbation for zero-shot Vietnamese classifiers, ahead of teen code and typos (Ha et al., 2026). That study measures small specialised "decision models" at a single noise level. Practitioners now mostly use open generative LLMs, and three questions remain open for them:

1. **How much** do open LLMs lose, and does the answer depend on the prompt, the amount of noise, or the model size?
2. **Why** do they lose it: because the tokenizer splits unaccented text into odd pieces, or because the model has seen less unaccented text and finds it surprising?
3. **What helps**: telling the model, or restoring the diacritics first? Does a fix measured on synthetic noise carry over to text people actually typed without marks?

We answer these with 19 open models (1.5–14B) on five Vietnamese tasks. Our contributions:

- A **controlled measurement** with full and partial (25/50/75%) diacritic removal, teen code and their mix, scored with single-token answers and a pre-registered validity gate (§3–4).
- Evidence that the loss is **robust to the prompt**, **monotone in the dose**, and **shrinks with model size** up to 14B (§4–5).
- A **same-item analysis** pointing to model surprise rather than tokenizer fragmentation, plus a robust but unexplained negative effect of broken syllables that we report as open (§6).
- A **direct comparison of mitigations** on the same pairs: a prompt hint does nothing and automatic restoration recovers 60% of the loss on synthetic noise, but not on naturally unaccented comments (§7).

## 2 Related work

**Vietnamese robustness.** Closest to us, Ha et al. (2026) test four zero-shot decision models (JEV, an API model; and LAYA, GLiNER2.5-multi-Decide and Quyet-1.0-Small, 287–328M parameters) on 13 Vietnamese classification settings. Their mean macro-F1 drops by 9.5–15.5 points under diacritic removal, against ≤ 1.1 for teen code and ≤ 4.5 for typos, with a decrease in 47 of 48 model-setting comparisons. Their LLM results come from earlier clean-input experiments (Thin et al., 2024) and are not re-run under noise. They do not vary the amount of removal, the model size or the prompt beyond the language of the label descriptions. They also do not analyse tokenization, test restoration, or use naturally unaccented text. We cover these for generative LLMs and agree with their main ranking. We add one qualification: teen code looks harmless partly because it changes few words (§4.3). In their own statistics, teen code edits 2.1% of characters and diacritic removal 18.3%. ViSoBERT (Nguyen et al., 2023) is reported to degrade under diacritic removal `[TODO verify: read their experiment and state it exactly]`. A recent study of regional dialects (arXiv 2608.10414) `[TODO verify authors]` finds accuracy drops for Vietnamese LLMs but does not test diacritics.

**Diacritics and tokenization.** Tokenizers trained mostly on English split non-Latin and diacritic-heavy scripts into more tokens. This raises cost and has been linked to weaker performance (Rust et al., 2021; Petrov et al., 2023). A position paper argues that diacritic stripping in preprocessing harms models (arXiv 2410.24140) `[TODO verify authors]`. We test the tokenizer explanation directly and find that the change in fragmentation does not predict the loss once item and model are held fixed (§6).

**Diacritic restoration.** Restoring Vietnamese diacritics is a well-studied sequence labelling task `[TODO cite 1–2 Vietnamese restoration papers]`. We use an openly released XLM-R-large token classifier as an off-the-shelf restorer and evaluate it as a preprocessing defence for LLMs, which we have not seen done.

**Synthetic vs natural noise.** Models robust to synthetic noise need not be robust to natural noise, and vice versa (Belinkov and Bisk, 2018). Vietnamese social-media text mixes unaccented words, slang and abbreviations (Nguyen et al., 2024, ViLexNorm). We therefore test restoration on comments their authors typed without diacritics, not only on stripped text.

**Evaluation methodology.** We follow perturbation-testing practice (Ribeiro et al., 2020; Wang et al., 2021). Batch calibration (Zhou et al., 2024) removes label bias, and paired bootstrap CIs with Holm correction support the comparisons.

## 3 Setup

### 3.1 Tasks and items

`[TAB 1]` Five public tasks; test items come from the test split and dev items (format choice, calibration) from the validation split. We apply NFC normalisation, remove duplicates, conflicting labels, items under three syllables and items with no diacritic, and sample a balanced number per class.

| Task | Type | Classes | Test items |
|---|---|---|---|
| UIT-VSFC | student feedback sentiment | 3 | 450 |
| UIT-VSMEC | social-media emotion | 7 | 245 |
| ViHSD | social-media hate speech | 3 | 450 |
| XNLI (vi) | natural language inference | 3 | 450 |
| ViMMRC | multiple-choice reading comprehension | 4 | 240 |

In total there are 1,835 test items. Noise is applied to the input fields only: the instruction and the options stay clean.

### 3.2 Noise conditions

- `clean`: the original text.
- `partial25/50/75`: an exact share of the syllables that carry diacritics is stripped, for 3 random seeds.
- `strip`: all diacritics are removed (NFD, drop combining marks, map đ → d).
- `teencode`: a hand-written substitution table (*không → ko*, *được → dc*, …). It changes 6–12% of words.
- `mixed`: teen code, then 50% stripping.

Automatic checks stop the run if `strip` leaves a diacritic, if `partial` changes anything besides diacritics, or if the noise is not deterministic.

### 3.3 Models

`[TAB 2]` 19 instruction-tuned models:

- Qwen2.5 1.5/3/7/14B;
- Qwen3 1.7/4/8/14B;
- SeaLLMs-v3 1.5/7B (Vietnamese/SEA-adapted, Qwen2.5 tokenizer);
- VinaLLaMA 2.7/7B (Vietnamese-adapted);
- bloomz 1.7/3/7.1B;
- Phi-3.5-mini (3.8B) and phi-4 (14B);
- Mistral-7B-Instruct-v0.3;
- Llama-3.2-3B-Instruct.

Several families have more than one size with the same tokenizer, which allows size comparisons with the tokenizer held fixed. The 14B models ran on an A100 80 GB and the rest on an L4.

### 3.4 Prompting and scoring

Each model uses its documented chat format. Options are given as letters (A, B, C…) and the answer is prefilled with "Đáp án:". We check per model that each answer letter is one distinct token, and read the model's probability over the letters in one forward pass. The same pass gives the per-field negative log-likelihood (NLL) used in §6. Predictions use batch calibration with the prior estimated on clean dev items. Raw predictions are kept and lead to the same conclusions (§4.4).

### 3.5 Validity gate

Before looking at any noisy result, we fixed a gate that a (model, task) pair must pass to be analysed:

- median probability mass on the option letters ≥ 0.5;
- agreement between a free greedy answer and the scored answer ≥ 0.7 (on 40 clean + 40 stripped items);
- clean accuracy ≥ chance + 0.10, with the lower bound of its 95% CI above chance.

For the original 16 models, 74 of 80 pairs pass. All 6 failures are near-chance clean accuracy (5 on ViHSD, 1 on XNLI). The three 14B models pass on all five tasks (89 valid pairs in total).

### 3.6 Metrics and statistics

The **normalised drop** is (acc_clean − acc_cond) / (acc_clean − chance). It is 0 for no loss and 1 for a fall to chance. Restoration **recovery** is (acc_restored − acc_strip) / (acc_clean − acc_strip), computed when the strip loss exceeds 0.05. All CIs are 95% paired bootstrap over items (B = 2000, shared resamples across conditions), and multiple within-family tests use Holm correction. Regressions use fixed effects as stated and cluster standard errors by item (§6) or by model (§5).

## 4 How much is lost?

### 4.1 Full removal

`[FIG 2]` `[TAB 3]` Under `strip`, the mean normalised drop over valid models is:

| Task | Normalised drop [95% CI] | Valid models |
|---|---|---|
| VSFC | 0.67 [0.61, 0.74] | 16 |
| VSMEC | 0.66 [0.55, 0.76] | 16 |
| XNLI | 0.56 [0.45, 0.64] | 15 |
| ViHSD | 0.53 [0.44, 0.63] | 11 |
| ViMMRC | 0.41 [0.36, 0.46] | 16 |

A model typically loses between two fifths and two thirds of what it knows above chance. ViMMRC loses least. We expect long passages to give more context to resolve ambiguous words, but have not tested this.

### 4.2 Dose-response

`[FIG 1a]` Accuracy falls monotonically with the share of stripped syllables in 86% of valid pairs with one noise seed. With accuracies averaged over three seeds, it falls monotonically in 97%. The normalised drop differs by 0.048 between seeds on average (max 0.121). There is no threshold: every additional stripped word costs accuracy.

### 4.3 Teen code is light, not harmless

`[FIG 1b]` Teen code alone costs only 0.06 normalised drop. However, our teen-code table changes just 6–12% of words. At that same dose, partial diacritic removal does similar damage: VSFC 0.10 vs 0.06, XNLI 0.11 vs 0.12. The common conclusion that teen code is harmless, also visible in Ha et al. (2026), should therefore be read as "teen code, as usually generated, changes few words".

### 4.4 The loss does not depend on the prompt or the scoring

`[TAB 4]` We re-ran the clean and stripped conditions with three more templates: a Vietnamese paraphrase, English instructions with Vietnamese input, and v4's template plus a sentence warning that the text may lack diacritics. On the 85 pairs valid under all four templates, the results are:

| Template | Mean normalised drop [95% CI] | Spearman with v4 ranking |
|---|---|---|
| v4 | 0.52 [0.48, 0.55] | — |
| Vietnamese paraphrase | 0.52 [0.49, 0.56] | 0.96 |
| English instructions | 0.55 [0.51, 0.58] | 0.95 |
| v4 + hint | 0.52 [0.48, 0.56] | 0.98 |

Only one task × template cell differs significantly from v4: XNLI with English instructions (+0.07). Across scoring choices (raw vs calibrated, clean vs per-condition prior), the strip drop stays between 0.53 and 0.71. Keeping the six gated-out pairs changes little (ViHSD 0.53 → 0.59).

### 4.5 What the errors look like

Under `strip`, predictions drift toward one label in 19 of 74 valid pairs. On VSFC, seven models shift toward *negative*. Letter mass barely moves, so the models still answer in the expected format. The errors come from a change of judgement, not from formatting failures. `[APPENDIX: fig10, figF1]`

## 5 Who is robust?

`[FIG 3]` **Size.** We regress the strip drop on log2(parameters) with task and family fixed effects, clustering by model. The drop shrinks by 0.090 per doubling for the 16 models ≤ 8B. With the three 14B models it shrinks by 0.086 [−0.103, −0.069] per doubling (p = 9.5e-23; 19 models, 89 pairs). The 14B models lose 0.24 (Qwen3-14B), 0.30 (Qwen2.5-14B) and 0.44 (phi-4) on average. Size helps, but even the best 14B model still loses about a quarter of its above-chance accuracy. Pairwise within-family tests are less powerful: only 5 of 22 survive Holm correction among ≤ 8B models.

**Vietnamese adaptation does not buy robustness.** With size and task controlled, the three adapted models lose 0.16 [−0.02, 0.34] *more* than general models (p = 0.086; exact permutation p = 0.091). With the tokenizer held fixed, SeaLLMs-v3 loses more than Qwen2.5 in 8 of 9 matched comparisons. Only VSFC (1.5B and 7B) survives Holm correction. A plausible reading is that Vietnamese continued pretraining uses edited, fully accented text, which makes unaccented input relatively more surprising (consistent with §6: adapted models show larger ΔNLL, 2.96 vs 1.71). This is not significant, and we do not claim it.

## 6 Why: surprise, not fragmentation

`[FIG 4]` We fit an item-level model of errors. For each noisy item that a model answered correctly when clean, we predict whether it now errs. The model has item × condition and model fixed effects, so it compares models *on the same noisy item*, with SEs clustered by item. Predictors are standardised:

| Predictor (per SD) | Effect on error | p |
|---|---|---|
| ΔNLL of the input | +1.8 pp | 2.5e-5 |
| ΔNLL, models sharing one tokenizer | +3.5 pp | 1.8e-8 |
| Lexical ambiguity of stripped words (bits) | +2.0 pp | 1.6e-5 |
| Δ tokens per syllable | `[TODO sign, size]` | 3.9e-4 |
| Δ broken syllables | −3.9 pp | 9.3e-6 |

**Surprise predicts errors.** The model that finds a stripped item more surprising, relative to its clean version, is more likely to get it wrong. This holds within the Qwen2.5/Qwen3/SeaLLMs group, which shares one tokenizer, so the effect cannot come from tokenization differences. Items whose stripped words have many possible accented readings are also harder.

**Fragmentation does not explain the loss.** At the model level, the change in tokens per syllable is uncorrelated with the drop. Phi-3.5 and Mistral even get *fewer* tokens after stripping and still lose heavily.

**An unexplained negative effect.** More broken syllables after stripping go with *fewer* errors. We checked that this is not an artefact:
- **Collinearity:** corr(Δtokens, Δbroken) = 0.87 but VIF ≈ 4, and the sign holds when Δbroken is entered alone (−1.6 pp, p = 1.4e-4).
- **Baseline tokenization:** it survives controlling for the clean break rate (−3.8 pp, p = 1.4e-5).
- **Subsamples:** it is negative in all 14 leave-one-tokenizer-group and leave-one-family-out refits (−4.6 to −2.3 pp) and under another definition (−4.1 pp).

Tokenizers differ in direction. Phi-3.5, Mistral and phi-4 split 80–90% of clean syllables and fewer after stripping (phi-4: 0.81 → 0.50); all others split more. We report this as an open finding and make no causal claim about broken syllables.

## 7 Can it be fixed?

### 7.1 A prompt hint does nothing

`[FIG 5]` Adding "the text may be written without diacritics" to the prompt changes clean and stripped accuracy by less than one point on every task. It recovers −1% of the lost accuracy on average, and no task's CI excludes zero in its favour.

### 7.2 Restoring diacritics recovers most of the loss

We restore the stripped text with an off-the-shelf XLM-R-large token classifier (`peterhung/vietnamese-accent-marker-xlm-roberta`, Apache-2.0), using 120-word windows, and re-score.

| Task | Words restored correctly | Drop, strip | Drop, restored | Recovery [95% CI] |
|---|---|---|---|---|
| VSFC | 92.5% | 0.67 | 0.12 | 0.77 [0.68, 0.85] |
| XNLI | 92.0% | 0.56 | 0.10 | 0.73 [0.62, 0.87] |
| VSMEC | 76.2% | 0.66 | 0.23 | 0.64 [0.50, 0.78] |
| ViMMRC | 81.2% | 0.41 | 0.15 | 0.55 [0.40, 0.67] |
| ViHSD | 75.1% | 0.53 | 0.24 | 0.52 [0.32, 0.66] |

Restoration recovers 64% of the loss on average (60% on the pairs of §4.4, 49–71% per task), and the remaining drop is 0.17 instead of 0.57. The benefit follows the restorer's accuracy. It is weaker on the two social-media tasks, and this is not because their originals already lack marks: words written unaccented in the original, slang and foreign words make up only 4.5–5.7% of their words, and excluding them barely changes restoration accuracy. The restorer is simply weaker on informal text. Its benefit also shrinks for stronger models: it recovers 23% (Qwen2.5-14B), 42% (Qwen3-14B) and 50% (phi-4), since these models lose less to begin with, restoration errors weigh relatively more `[TODO check: compare acc_restored with acc_clean for the 14B models]`.

### 7.3 Naturally unaccented text

`[TAB 5]` Synthetic stripping removes every mark from text that was written with them. Real users who type without diacritics may write differently. We took ViHSD test comments with no diacritic at all that their authors wrote that way. We kept those where the restorer changes at least 20% of words, which leaves 226 comments; the restorer adds diacritics to 70% of their words. Over 14 valid models, restoration changes balanced accuracy by +0.01 [−0.02, 0.04]. The same models gain +0.055 on synthetic ViHSD items. Only VinaLLaMA-7B gains significantly (+0.17), and no model loses significantly.

Two explanations fit and this set cannot separate them. Either the restorer is weak on informal writing (§7.2), or models already read habitual unaccented writing reasonably well. The set is small and unbalanced (mostly the *clean* class), so per-model CIs are wide. We therefore present this as a caution, not a negative result: gains measured on synthetic stripping should not be assumed for real unaccented input.

## 8 Discussion

For practitioners:

1. **Expect a large loss.** Unaccented input can cost half of a model's task ability, and prompt engineering, including telling the model, will not fix it.
2. **Use a larger model** if you can: the loss falls steadily with size, though not to zero at 14B.
3. **Restoring diacritics is cheap and helps on stripped formal text**, but check it on your own users' text before relying on it.

For research, the gap between synthetic and natural unaccented text is the main open question. It needs a larger, balanced corpus of naturally unaccented text with labels, and a restorer trained on informal writing. The surprise result also suggests a training-side fix: adding unaccented text to continued pretraining should lower ΔNLL, and §6 predicts that this would lower the loss.

## 9 Limitations

- **Scale.** Our largest models have 14B parameters, and we test no closed models. The size trend may flatten beyond 14B.
- **One restorer.** Its mean word accuracy (83.4%) is below the 85% target we set in advance. A better restorer would recover more.
- **Natural text.** The naturally unaccented set has 226 items from one task.
- **Answer format.** We score single-letter answers, which measures understanding rather than generation. Free-generation agreement is gated, but generation tasks such as summarisation are not covered.
- **Teen code.** The table is small and hand-written, and has not yet been checked by a second native speaker.
- **Mechanism.** The negative broken-syllable effect is unexplained.
- **Exclusions.** The validity gate excludes 6 of 80 original pairs. Including them barely changes the results.

## Ethics statement

We use public research datasets under their licences. ViHSD contains offensive content. We show no examples beyond what is needed. Our noisy versions are derived from the datasets and will be released only where the original licence allows it `[TODO check UIT licences]`.

## References `[TODO verify all; convert to BibTeX]`

- Belinkov, Y. and Bisk, Y. 2018. Synthetic and natural noise both break neural machine translation. ICLR.
- Ha, P. H., Phuc, N. X., Quy, N. N., Tran, T. T., Triet, N. M., and Thin, D. V. 2026. How well do decision models transfer to Vietnamese? An empirical study of text classification. arXiv:2610.31422.
- Nguyen, N., Phan, T., Nguyen, D., and Nguyen, K. 2023. ViSoBERT: a pre-trained language model for Vietnamese social media text processing. EMNLP, 5191–5207.
- Nguyen, T., Le, T., and Nguyen, K. 2024. ViLexNorm: a lexical normalization corpus for Vietnamese social media text. EACL, 1421–1437.
- Petrov, A., La Malfa, E., Torr, P., and Bibi, A. 2023. Language model tokenizers introduce unfairness between languages. NeurIPS.
- Ribeiro, M. T., Wu, T., Guestrin, C., and Singh, S. 2020. Beyond accuracy: behavioral testing of NLP models with CheckList. ACL, 4902–4912.
- Rust, P., Pfeiffer, J., Vulić, I., Ruder, S., and Gurevych, I. 2021. How good is your tokenizer? On the monolingual performance of multilingual language models. ACL.
- Thin, D. V. et al. 2024. PACLIC 38, 181–192. `[TODO full title]`
- Wang, X. et al. 2021. TextFlint: unified multilingual robustness evaluation toolkit for natural language processing. ACL-IJCNLP demos, 347–355.
- Zhou, H. et al. 2024. Batch calibration: rethinking calibration for in-context learning and prompt engineering. ICLR.
- Dataset papers: UIT-VSFC (Nguyen et al., 2018), UIT-VSMEC (Ho et al., 2019), ViHSD (Luu et al., 2021), XNLI (Conneau et al., 2018), ViMMRC (Nguyen et al., 2020) `[TODO full entries]`.
- Models: Qwen2.5, Qwen3, SeaLLMs-v3, VinaLLaMA, BLOOMZ, Phi-3.5, phi-4, Mistral, Llama-3.2 `[TODO technical reports]`.
- arXiv 2608.10414 (dialect robustness) and arXiv 2410.24140 (diacritics position paper) `[TODO authors]`.
