contract_role: methodology

## Dimension Scores

### D1: methodology_rigor
score: warn
trigger: "Methods that are defensible but incompletely reported"

### D2: domain_accuracy
score: not_assessed

### D3: argumentative_coherence
score: warn
trigger: "Hedged but still overconfident language on secondary or subgroup results"

### D4: cross_disciplinary_relevance
score: not_assessed

### D5: writing_and_structure
score: not_assessed

### D6: venue_fit_and_contribution
score: not_assessed

## Review Body

Reviewer identity: biostatistician (diagnostic accuracy, agreement statistics, paired and clustered resampling, LLM-as-judge validation). I do not assess Vietnamese language or clinical nuance.

Overall, the design is sound for its purpose. Each case is its own control in a 2x2 within-case design (wording x diacritics), with a remedy arm and non-urgent controls that let over-triage be measured. The primary outcome is named in advance and the judge is blinded to case, version and gold label. The authors are mostly candid that per-model results are underpowered. I recomputed the headline numbers from Table 2 and they reproduce. Column means are 22.1, 33.4, 47.8 and 50.8%. Pooled counts are 28, 42, 60 and 64 of 126. Differences are +11.1, +25.4 and +28.6 points. The 6/9 and 8/9 sign counts match Table 2 and Fig. 7. The four Wilson intervals in the remedy section reproduce, as do the mitigation means in Fig. 11 (29/14/14, 48/34/32 and 24/30/32), the meaning-check kappa of 0.15, PABAK of 0.65 and AC1 of 0.79 (2x2 table: 1 both, 0 and 9 discordant, 42 neither), and the Fig. 9 remedy totals (13+23 = 36 unsafe; 49/216 endorse; 132/216 reject). The Holm-adjusted minimum p of 0.14 also fits an exact McNemar with 9:0 discordant pairs multiplied by 36. The issues below concern how much the inference can carry, not arithmetic errors. The exception is W6, a text-figure conflict.

The D1 warn reflects several methods that are defensible but incompletely reported or validated: small-cluster inference (W1), judge validation without uncertainty or stratification (W2), no paraphrase control (W3) and reproducibility details (W13). None reaches the block level I set in Phase 1. The headline inference does respect pairing by case, and the primary label was validated against humans. The D3 warn reflects claims that go beyond their intervals, namely the interaction (W4), per-model and adaptation claims (W5) and remedy endorsement (W7), plus one discussion claim the authors' own heat map contradicts (W6). None of these overturns the pooled main result.

### S1: Paired factorial design with over-triage controls
**Evidence Anchor**: text: "Without controls, a model that sends everyone to the emergency room would look perfect."

Holding the facts fixed and varying only wording and diacritics, with 28 controls, separates a shift in operating point from a loss of discrimination. That is exactly what the over-triage analysis then exploits.

### S2: Judge blinded to everything except the answer
**Evidence Anchor**: text: "never the case, the gold label or the version"

This blinds the judge to the gold label, the most dangerous leakage path for an LLM judge. The guideline and judge prompt are given verbatim.

### S3: Honest framing of per-model power
**Evidence Anchor**: text: "The evidence therefore rests on the mean over models."

The paper states that no per-model contrast survives Holm and places the weight on the pooled estimate. It labels the per-condition analysis exploratory and the mitigation study descriptive.

### S4: Sensitivity analyses targeted at the obvious threats
**Evidence Anchor**: text: "We repeated the pooled analysis without the ten cases whose clinical/folk pair was flagged by either rater"

The paper also repeats the remedy analysis on the documented subset and draws stochastic samples for two models. It reports the urgent-case diacritic effects losing significance instead of hiding that result.

### S5: Internal numerical consistency of the main table
**Evidence Anchor**: table: Table 2 (tab:main), row "Mean over models" and the four version columns

Every pooled number in the abstract, results and conclusion reproduces from the per-model rows, as does every value plotted in Figs. 7, 8, 9 and 11.

### S6: Appropriate agreement statistics for a skewed table
**Evidence Anchor**: text: "prevalence-adjusted measures were higher"

Reporting PABAK and AC1 alongside a kappa depressed by prevalence is correct practice, and the values reproduce.

### W1: Pooled confidence intervals rest on a percentile bootstrap over 14 clusters
**Severity**: Major
**Evidence Anchor**: text: "The mean effect over models uses a case-level bootstrap that resamples cases for all models together."
**Confidence**: 4 — small-sample resampling inference

Every confirmatory claim (+11 [4, 18], +25 [13, 37], +29 [20, 37]) is a percentile bootstrap over 14 emergency cases. With so few clusters and discrete outcomes, percentile intervals are known to undercover, because the bootstrap variance is biased downward by about (n-1)/n and the resampling distribution is lumpy. The lower bound of 4 for the folk effect is therefore the number most at risk. Two analyses would show whether the conclusions depend on this choice. One is an exact sign-flip permutation test on the 14 case-level mean differences, which needs only 2^14 relabellings. The other is a t-interval or BCa interval on those same 14 values, or a crossed random-effects logistic model with case and model random effects. The paper should also state that inference is conditional on these nine models (models are fixed, not sampled), so "on average" means over this model set, not over LLMs.

### W2: Judge validation lacks intervals, a confusion matrix, and stratification by diacritic status and model family
**Severity**: Major
**Evidence Anchor**: text: "Judge--human agreement on triage was $\kappa=0.90$ over the four labels and $\kappa=0.94$ for the binary emergency/not decision."
**Confidence**: 4 — LLM-as-judge validation in clinical NLP

The paper's main effect is a contrast between versions, so what matters is whether the judge errs differently across versions. Overall kappa cannot show that. Answers to unaccented prompts are likely to be partly unaccented or degraded themselves, and the judge prompt explicitly anticipates this. If the judge misses emergency advice in such text more often, part of the diacritic effect is measurement error. The judge is also Gemini 3.5 Flash, which is one of the two evaluated models with near-zero under-triage. Blinding to the answer's source does not remove style familiarity. Please report the following:
- the 2x2 judge-human confusion matrix for emergency vs not, with a CI for kappa;
- agreement separately for with- and without-diacritic versions, and for Gemini vs non-Gemini answers;
- the human-labelled under-triage contrast on the 150-answer sample next to the judge-labelled one.

The primary human annotator is the first author, who was blind to model and version but not to the hypothesis. Unaccented answers may also reveal their version to the reader.

### W3: No neutral-paraphrase control, so folk-specific attribution is not identified
**Severity**: Major
**Evidence Anchor**: text: "Any change in the advice is then caused by the wording, not by missing information."
**Confidence**: 3 — design inference; acknowledged by the authors in Limitations

Greedy small models flip under any rewording. Table 2 shows this directly for Qwen2.5-7B: a +0 folk_nd effect with a CI of [-43, +36] implies many cases flipping in both directions. When baseline under-triage is low, symmetric perturbation noise alone pushes under-triage upward, toward the model's marginal rate. The observed fall in over-triage argues against pure noise, which is a real point in the authors' favour. Still, the folk effect cannot be separated from a generic paraphrase effect without a clinical-paraphrase arm. The Introduction's causal sentence should be narrowed, either to "the rewording, including register and dialect" or by adding that control. The Limitations already concede the point. The Introduction and abstract do not.

### W4: The interaction claimed under RQ2 is never estimated with uncertainty
**Severity**: Major
**Evidence Anchor**: text: "The two changes do not add up."
**Confidence**: 4 — factorial contrasts in paired designs

RQ2 asks whether the effects compound, and the abstract and conclusion state that missing diacritics "cause most of the harm". Two quantities settle this. One is the interaction, (folk_nd - clin_nd) - (folk - clin), which is about -8 points from the pooled counts (36 - 14 - 32 = -10 of 126). The other is the paired difference between the diacritic effect and the folk effect (about +14 points). Neither has a reported CI. Both are available from the same case-level bootstrap and should be reported before "do not add up" and "most of the harm" are stated as findings. "Causes" should also be softened to "accounts for".

### W5: Per-model and adaptation claims over-read 14-case intervals
**Severity**: Major
**Evidence Anchor**: text: "language adaptation did not make the model more robust to unaccented input"
**Confidence**: 4 — subgroup inference

The paper rightly says no per-model contrast survives correction. The Discussion and abstract still draw model-level conclusions:
- "the effects concentrate in small open models";
- Gemini "barely affected";
- "Qwen2.5-7B showed no effect", where Table 2's Δfolk_nd is +0 with a CI of [-43, +36] (absence of evidence, not evidence of absence);
- a conclusion about language adaptation from a single pair evaluated on 14 cases.

No model-by-version heterogeneity test is reported. The Gemini models sit at a 0% floor on clin, so their effects can only be zero or positive, and one of them is the judge (W2). Gemini Flash-Lite's low under-triage partly reflects a more cautious operating point, which the authors do note. These statements should be recast as descriptive, with per-model intervals shown in the text. If heterogeneity is claimed, a model x version interaction test (e.g. random slopes) should support it.

### W6: Discussion claim about folk wording for liver failure and DKA conflicts with the condition heat map
**Severity**: Major
**Evidence Anchor**: figure: Fig. 10 (fig:conditions), rows "Liver failure (paracetamol)" and "Diabetic ketoacidosis"
**Confidence**: 5 — direct read-off of the figure

The Discussion states that folk wording "mattered more" for paracetamol liver failure and DKA. In the figure, liver failure is 22% in both clin and folk, and lower in folk_nd (56%) than in clin_nd (78%). DKA is 56% in both clin and folk. The only folk-associated rise for DKA appears in folk_nd vs clin_nd (89 vs 56, i.e. 3 of 9 answers). These are the very cases offered as examples of folk-wording harm. The figure shows a diacritic effect, and for liver failure the folk effect runs the other way. The sentence should be corrected, or replaced by conditions where clin-to-folk does rise (e.g. meningitis 11 to 44, heart failure 0 to 33). Even then, each cell rests on nine non-independent answers from one case.

### W7: The unsafe-endorsement headline depends on a weakly validated label, and its intervals omit both clustering and misclassification
**Severity**: Major
**Evidence Anchor**: text: "in 7 of 14 emergencies for one model"
**Confidence**: 4 — misclassification and agreement statistics

Remedy stance has kappa = 0.50 on 32 answers. The CI for that kappa is wide, roughly 0.2 to 0.8 at this n, and is not reported. Unsafe endorsement combines this weak label with the triage label, so its error compounds both. The Wilson intervals (which reproduce) assume independent answers and perfect labelling, and the authors acknowledge only the first. The abstract and Contribution 2 headline a per-model count ("7 of 14") from this label. Report the kappa CI, the confusion matrix for stance, and a bound on unsafe endorsement under the observed judge-human disagreement. Alternatively, report human-labelled unsafe endorsement for the two highlighted models (at most 24 answers each). The per-model count should move out of the abstract unless it is human-verified.

### W8: The stated detectable effect does not match the chosen multiplicity correction
**Severity**: Minor
**Evidence Anchor**: text: "a single model's difference must be large (about 30 points or more) to be detected"
**Confidence**: 4 — exact McNemar power

With Holm over 36 tests, the smallest raw p must fall below 0.05/36 ≈ 0.0014. An exact McNemar with all discordant pairs in one direction needs at least 11 of 14 (2 x 0.5^11 ≈ 0.001), which is about 79 points. "About 30 points" holds only before correction. The per-model test set is therefore near-powerless by design, and the paper should say so. The paper should also say whether the three pooled primary contrasts (and the urgent outcome) are treated as a family. The folk effect's [4, 18] interval would probably survive a three-way adjustment, but this is not stated.

### W9: Zero-width bootstrap intervals at the floor imply false certainty
**Severity**: Minor
**Evidence Anchor**: table: Table 2 (tab:main), Gemini rows "+0 [+0, +0]"
**Confidence**: 4 — resampling at boundaries

When no case is discordant, the percentile bootstrap returns [0, 0]. That describes the sample, not the uncertainty: 0/14 vs 0/14 is compatible with a true difference of several points. Mark these cells as degenerate, or use an exact or Newcombe-type interval for paired proportions.

### W10: "Less urgent overall" rests on an over-triage change reported without an interval
**Severity**: Minor
**Evidence Anchor**: text: "The models therefore did not compensate by becoming more cautious."
**Confidence**: 3 — paired proportions

The fall from 27% to 21% (-6, range -21 to 0) supports the paper's interpretive claim that both groups shift toward less urgency. It has no paired CI over the 28 control cases, and should get one, as the emergency contrasts do.

### W11: The mitigation gap was already about 20 points at baseline
**Severity**: Minor
**Evidence Anchor**: text: "Neither prompt closed the gap between the two versions."
**Confidence**: 4 — direct recomputation from Table 3

From Table 3, the four-model base means are 28.5% (clin) and 48.25% (folk_nd), a gap of 19.75 points. With M1 and M2 the gaps are 19.75 and 17.75. The mitigations therefore shifted both versions down roughly in parallel and left the gap essentially unchanged, a stronger and clearer statement than "did not close". The abstract's "lowered under-triage" should carry the paper's own descriptive qualifier (one greedy run, four models, no CI).

### W12: Per-condition analysis described as one case per condition, but asthma has two
**Severity**: Minor
**Evidence Anchor**: text: "each condition has one case (nine answers per version)"
**Confidence**: 5 — direct read-off

The figure caption says that asthma has two cases (18 answers), which the results text omits. Align the two.

### W13: Reproducibility identifiers incomplete
**Severity**: Minor
**Evidence Anchor**: absence: Experimental Setup and release statements — expected analysis code, Hugging Face model revision hashes, Gemini model version identifiers and bootstrap seed; checked abstract, Table 1 caption, Prompting and decoding, Statistics, Ethics Statement, Conclusion
**Confidence**: 4 — reproducibility audit

The release covers cases, lexicon, answers and labels. Code is not mentioned. Hosted model aliases can change behind the same name, so the exact identifiers and run dates matter.

### W14: Denominator of the Llama "no usable advice" share is not stated
**Severity**: Minor
**Evidence Anchor**: text: "because 35\% of its remedy answers gave no usable advice"
**Confidence**: 3 — denominator check

35% is reachable from all 52 remedy answers (18/52) but not from 14 emergencies or 24 serious cases. State the denominator, because the sentence explains an emergency-only rise from 43% to 86%.

## Arithmetic Receipts

### AR1
procedure_id: grim
evidence_anchor: text: "models under-triaged 22\% of emergencies on average"
reported_inputs: under-triage 22% (clin, mean over 9 models), binary outcome, 14 emergency cases per model, N=126 answers, integer-percent precision
assumptions: each model answered all 14 emergencies (paper states 2,340 answers = 260 prompts x 9 models), so the equal-weight model mean equals the pooled k/126
derivation: k/126 in [0.215, 0.225) gives k in [27.09, 28.35), so k=28; Table 2 clin column counts 0+0+1+2+3+3+5+6+8=28
derived_value_or_range: 28/126 = 22.22%
rounding_interval: [21.5, 22.5)
nearest_achievable: 27/126 = 21.43%, 28/126 = 22.22%, 29/126 = 23.02%
comparison_rule: reported integer percent must equal the rounding of some attainable k/126
status: consistent

### AR2
procedure_id: grim
evidence_anchor: text: "and folk wording without diacritics to 51\% (+29 [20, 37]; higher in 8 of 9 models)"
reported_inputs: under-triage 51% (folk_nd, mean over 9 models), binary outcome, N=126 answers, integer-percent precision
assumptions: complete 14 x 9 design as stated by the paper
derivation: k/126 in [0.505, 0.515) gives k in [63.63, 64.89), so k=64; Table 2 folk_nd column counts 1+1+9+8+6+10+5+13+11=64
derived_value_or_range: 64/126 = 50.79%
rounding_interval: [50.5, 51.5)
nearest_achievable: 63/126 = 50.00%, 64/126 = 50.79%, 65/126 = 51.59%
comparison_rule: reported integer percent must equal the rounding of some attainable k/126
status: consistent

### AR3
procedure_id: grim
evidence_anchor: text: "rose from 6\% (clinical) to 19\% (folk)"
reported_inputs: urgent-case self-care or none share 19% (folk), 10 urgent cases x 9 models, N=90, integer-percent precision
assumptions: complete 10 x 9 design as stated by the paper
derivation: k/90 in [0.185, 0.195) gives k in [16.65, 17.55), so k=17
derived_value_or_range: 17/90 = 18.89%
rounding_interval: [18.5, 19.5)
nearest_achievable: 16/90 = 17.78%, 17/90 = 18.89%, 18/90 = 20.00%
comparison_rule: reported integer percent must equal the rounding of some attainable k/90
status: consistent

### AR4
procedure_id: grim
evidence_anchor: text: "occurred in 10\% of emergency answers (13/126, Wilson 95\% CI [6, 17])"
reported_inputs: unsafe endorsement 10%, count 13, N=126, integer-percent precision
assumptions: N=126 as stated in the text
derivation: 13/126 = 0.1032, which lies in [0.095, 0.105)
derived_value_or_range: 13/126 = 10.32%
rounding_interval: [9.5, 10.5)
nearest_achievable: 12/126 = 9.52%, 13/126 = 10.32%, 14/126 = 11.11%
comparison_rule: reported integer percent must equal the rounding of the reported count over N
status: consistent

### AR5
procedure_id: grim
evidence_anchor: text: "They endorsed remedies less often on serious cases (23\%) than on controls (44\%)"
reported_inputs: endorse share 23% on serious cases, 24 serious cases x 9 models, N=216, integer-percent precision
assumptions: complete 24 x 9 folk_rem answers as stated by the paper
derivation: k/216 in [0.225, 0.235) gives k in [48.6, 50.76), so k is 49 or 50; Fig. 9 bars sum to about 49
derived_value_or_range: 49/216 = 22.69% or 50/216 = 23.15%
rounding_interval: [22.5, 23.5)
nearest_achievable: 48/216 = 22.22%, 49/216 = 22.69%, 50/216 = 23.15%, 51/216 = 23.61%
comparison_rule: reported integer percent must equal the rounding of some attainable k/216
status: consistent

### AR6
procedure_id: grim
evidence_anchor: table: Table 3 (tab:mit), row "Llama-3.1-8B-Instruct m2", column "over"
reported_inputs: over-triage 45%, n=112 per row as stated in the caption, integer-percent precision
assumptions: n=112 = 28 controls x 4 versions as stated in the caption
derivation: k/112 in [0.445, 0.455) gives k in [49.84, 50.96), so k=50
derived_value_or_range: 50/112 = 44.64%
rounding_interval: [44.5, 45.5)
nearest_achievable: 49/112 = 43.75%, 50/112 = 44.64%, 51/112 = 45.54%
comparison_rule: reported integer percent must equal the rounding of some attainable k/112
status: consistent

### AR7
procedure_id: grim
evidence_anchor: text: "Llama-3.1-8B is the exception: its under-triage rose from 43\% to 86\%"
reported_inputs: share labelled none 35% for Llama-3.1-8B folk_rem answers, denominator not stated
assumptions: none licensed; the candidate denominators 14, 24 and 52 are all compatible with the text
derivation: 18/52 = 34.6% reaches 35%; no k/14 or k/24 rounds to 35%; the paper does not state which denominator applies
derived_value_or_range: reachable only if N=52; undetermined otherwise
comparison_rule: reported integer percent must equal the rounding of some attainable k/N for the paper's analytic N
status: not_computable
not_computable_reason: analytic_n_ambiguous

### AR8
procedure_id: p_from_test_statistic
evidence_anchor: text: "no single-model contrast survives Holm correction (smallest corrected $p=0.14$)"
reported_inputs: exact McNemar test, Holm adjustment over 36 tests, smallest adjusted p 0.14; no discordant counts or test statistic reported
tail_convention: unstated
assumptions: none beyond the stated test family and correction
derivation: exact binomial McNemar with Holm adjustment is outside the bounded procedure, and the discordant-pair counts are not reported
derived_value_or_range: not derived within the bounded procedure
comparison_rule: recomputed p from a reported statistic and df compared at reported precision
status: not_computable
not_computable_reason: nonstandard_p_procedure
