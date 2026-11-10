contract_role: da
## Dimension Scores

### D1: methodology_rigor
score: not_assessed

### D2: domain_accuracy
score: not_assessed

### D3: argumentative_coherence
score: warn
trigger: "Secondary claims overreach the evidence, some alternative explanations or limitations are under-discussed"

### D4: cross_disciplinary_relevance
score: not_assessed

### D5: writing_and_structure
score: not_assessed

### D6: venue_fit_and_contribution
score: not_assessed

## Review Body

Calibration status: `NOT_CALIBRATED` (seat report; panel topology not known at seat time). Unbound call: no venue-alignment claim is made.

**What the paper does well.** The paired design (same case, five tellings) is the right shape for the question, the headline numbers are internally consistent (I re-derived the pooled means in Table 2 from the per-model rows: 22/33/48/51 and +11/+25/+29 all reproduce from counts out of 126), the controls make over-triage visible, and the limitations section concedes most design weaknesses openly. The diacritic-loss effect (+25, CI [13, 37], positive in most models, robust to sampling and to dropping flagged pairs on emergencies) is the paper's most solid result, and I do not challenge that the harmful direction is real.

**Why D3 is warn, not block.** The core thesis as worded in the abstract (folk wording and, much more, missing diacritics raise emergency under-triage on average across these nine models, without a compensating rise in over-triage) follows from the reported evidence. The coherence problems sit in the interpretive layer built on top of it: what the folk effect is attributed to, the per-condition and trúng gió conclusions that the title and conclusion lean on, the "less urgent overall" reading, and the sycophancy framing of RQ3. Each can be repaired by narrowing claims or adding analyses of data the authors already hold; none, in my reading, overturns the core result, so no CRITICAL is raised.

**Strongest counter-argument.** A sceptic would say the paper has shown that small open models read unaccented and non-standard Vietnamese poorly, and little more. The largest effect is diacritic stripping, a script-level degradation already known to hurt NLP systems; the authors' own qualitative reading is that models "fail to read" the signs, which is a comprehension failure, not a triage behaviour specific to folk illness. The folk-wording effect (+11) is smaller, positive in only 6 of 9 models, reversed in Qwen3-8B, not significant for any single model, and bundles three things the design cannot separate: a folk label, lay register, and Southern dialect vocabulary. With no neutral clinical paraphrase as a control, the sceptic can attribute the whole +11 to distance from the source-like clinical text, which is the register the models were most likely tuned on. The one case built around the folk concept that motivates the paper (trúng gió for stroke) shows no misleading effect, and that case was itself flagged in the meaning check. The per-condition story ("less specific signs") is post hoc on one case per condition and draws partly on no-diacritic cells. The remedy result, framed as sycophancy, does not move triage at all on average, and its unsafe-endorsement count is dominated by models that already under-triage the folk version. The two commercial models, the ones a Vietnamese user is most likely to meet, are barely affected. On this reading, the defensible contribution is a careful robustness probe of small open models to unaccented Vietnamese health questions with a reusable paired set; the folk-illness framing in the title, introduction and conclusion is not what the evidence carries.

**Ignored alternative explanations.** (1) Register and lexical-frequency distance rather than folk-illness semantics as the driver of the folk effect (see M1). (2) Generation degradation (more *none*, off-topic or garbled answers on unaccented input) as the driver of both rising under-triage and falling over-triage (see M4). (3) Pre-existing under-triage rather than deference to the user as the source of unsafe endorsement (see M5). (4) Ceiling effects in the weakest models (e.g. 86 to 93 percent under-triage) as the reason the two perturbations "do not add up" (m2 below).

**Missing stakeholder perspectives.** No clinician reviewed the Vietnamese versions, and both native raters are Southern; I note these only as absent voices (owned by other seats).

**Unexamined premise.** The paper assumes the clinical Vietnamese translation is the neutral reference point. It is the version closest to the English source and to medical register; treating it as "zero" makes any departure look like harm, which is the premise behind M1.

**MINOR issues** (each with typed anchor and confidence).
- m1. The Discussion heading asserts a mechanism that the following text calls a hypothesis from two examples, and the mitigation result is offered as fitting it although a persistent ~20-point gap is consistent with almost any mechanism. Anchor: text: Discussion "Diacritic loss: the model misreads the signs." and "The hypothesis fits the mitigation result". Confidence: 4 (direct reading of the section).
- m2. Sub-additivity is asserted without an interaction estimate or CI, and the weakest models sit near ceiling (Qwen2.5-1.5B 93 percent on clin_nd), which mechanically suppresses any added folk effect. Anchor: text: Results RQ1-RQ2 "The two changes do not add up." Confidence: 4 (arithmetic on Table 2).
- m3. The introduction claims advice changes are "not by missing information", but the paper itself describes diacritic removal as removing lexical information and later explains the effect as models failing to read the signs. Anchor: text: Introduction "Any change in the advice is then caused by the wording, not by missing information." and "which removes much of the lexical information LLMs rely on". Confidence: 4 (internal comparison of two passages).
- m4. The abstract headlines the most extreme of nine models on the label with the weakest judge validity (kappa 0.50 on 32 answers), which the results section itself calls secondary. Anchor: text: Abstract "and in 7 of 14 emergencies for one model". Confidence: 3 (selection concern; per-model n is small).
- m5. On the urgent secondary outcome, both diacritic effects vanish when flagged pairs are removed, yet the urgent-case results paragraph reports them unqualified. Anchor: text: Robustness, flagged pairs "The diacritic effects were no longer distinguishable from zero". Confidence: 4 (direct reading).
- m6. The pooled "on average" figure is a property of the chosen model mix (seven small open models, two commercial ones barely affected; folk effect reversed in Qwen3-8B), so the headline should be stated as the mean over this panel. Anchor: text: Results "Folk wording raised this to 33\% (+11 points, 95\% CI [4, 18]; higher in 6 of 9 models)." Confidence: 3 (framing judgement).

#### CRITICAL
| # | Dimension | Issue Description | Evidence Anchor | Confidence | Field-Norm Boundary | Evidence-Crossing Rationale |
|---|-----------|-------------------|-----------------|------------|---------------------|-----------------------------|

#### MAJOR
| # | Dimension | Issue Description | Evidence Anchor | Confidence | Field-Norm Boundary | Evidence-Crossing Rationale |
|---|-----------|-------------------|-----------------|------------|---------------------|-----------------------------|
| M1 | D3 | The folk effect is presented as an effect of folk telling, but the folk version bundles a folk label, lay register and Southern vocabulary, and there is no neutral paraphrase control. The +11 points cannot be attributed to folk-illness content over generic distance from the source-like clinical text; the title and introduction frame it as the former. Repair: narrow the claim to "lay/folk rewording", or add a neutral paraphrase arm. | text: Introduction "We hold the case and its signs fixed and change only the telling." and Limitations "Any paraphrase may move small greedy-decoded models; we have no neutral clinical-paraphrase control." | 4 (design described explicitly in Sections 3 and 7) | n/a (severity rests on the paper's own causal claim, not a field norm) | n/a |
| M2 | D3 | The Conclusion states as a finding that folk labels such as trúng gió were not the main problem, and Contribution 3 states it as a result, but it rests on one stroke case (nine answers per version), labelled exploratory in Results, and that case (E08) is one of the pairs flagged in the meaning check. A single case cannot support a general statement about the best-known folk label. Repair: present it as a single-case observation. | text: Conclusion "The main problem was not folk labels such as \vi{trúng gió}." and Results "each condition has one case (nine answers per version)" | 4 (counts stated in Sections 5.4 and 5.6) | n/a | n/a |
| M3 | D3 | The Discussion attributes per-condition harm to folk wording on less specific signs, but the supporting Results numbers are drawn from no-diacritic cells (meningitis on clin_nd, DKA on folk_nd), and folk-only per-condition figures are not reported. The "less specific signs" mechanism is post hoc and mixes the two perturbations. Repair: report folk vs clin per condition separately, or drop the attribution. | text: Discussion "Folk wording mattered more where the signs are less specific, such as liver failure told as \vi{bị cảm} (``a cold'')" and Results "meningitis rose from 11\% (clinical) to 78\% (clinical, no diacritics)" | 4 (cross-reading of Sections 5.4 and 6) | n/a | n/a |
| M4 | D3 | "Less urgent overall" assumes models give milder advice, but *none* answers count as under-triage and never as over-triage, so more degenerate or off-topic output on unaccented input would raise under-triage and lower over-triage mechanically. The rate of *none* labels by version is not reported (only for Llama on folk_rem). Repair: report the label distribution per version and recompute both rates excluding *none*. | text: Discussion "Lay or unaccented text made the advice less urgent across the board, as if such users had milder problems." and Measures "(answers labelled \emph{none} count as under-triage)" | 3 (alternative is plausible; direction unknown without the breakdown) | n/a | n/a |
| M5 | D3 | RQ3 is framed as sycophancy, but adding the remedy did not change under-triage on average, and unsafe endorsement requires no emergency advice, which the same models already withhold on the folk version (SeaLLMs 86 percent under-triage on folk, then 7 of 14 unsafe endorsements). Unsafe endorsement is therefore largely downstream of existing under-triage, not deference to the user. Repair: report endorsement conditional on the model's folk-version triage, or drop the sycophancy framing. | text: Dataset "which separates real sycophancy from a habit of rejecting all folk medicine." and Results "Adding a remedy and asking ``is that OK?'' did not change under-triage on average" | 3 (inference from Table 2 rows and Section 5.3) | n/a | n/a |

