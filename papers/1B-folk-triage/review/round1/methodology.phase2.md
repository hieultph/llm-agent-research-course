contract_role: methodology

## Dimension Scores

### D1: methodology_rigor
score: warn
trigger: "Methods that are sound in principle but under-reported or under-powered"

### D2: domain_accuracy
score: not_assessed

### D3: argumentative_coherence
score: warn
trigger: "Wording overstates the evidence in places"

### D4: cross_disciplinary_relevance
score: not_assessed

### D5: writing_and_structure
score: not_assessed

### D6: venue_fit_and_contribution
score: not_assessed

## Review Body

Reviewer identity: a biostatistician specialising in paired designs and LLM-as-judge evaluation. Calibration status: NOT_CALIBRATED. Vietnamese naturalness is outside my competence, so I did not judge it.

Summary. The core design suits the RQ1 and RQ2 questions. The same 52 physician-labelled cases are rewritten in five versions, so contrasts are paired within case. The diacritic manipulation is automatic and exact, and the controls guard against an "everyone to the ER" model. The primary outcome is stated. Per-model rates and paired differences are reported with intervals, and the authors say openly that single-model contrasts are underpowered with 14 emergencies. The pooled numbers I could check are internally consistent: the table means reproduce the abstract, and the meaning-check kappa, PABAK and AC1 reproduce from the stated 43/52 agreement with flags of 1 and 10. The pooled RQ1 and RQ2 effects on emergencies are therefore supported at the stated precision.

The weaknesses sit around this core:
- **RQ3 (remedy endorsement)** rests on a judge with only moderate human agreement, yet it is headlined in the abstract.
- **RQ4 (mitigation)** draws comparative conclusions from four models with no inferential statistics.
- **The per-condition analysis** is post hoc, with one case per condition. It is promoted to a contribution and to the conclusion.

Several smaller reporting gaps (judge validity by stratum, pooling weights, rerun variability, denominators, reproducibility identifiers) are easy to repair. Statistical-reporting judgement against the APA/CONSORT-style checklist in my remit: PARTLY_MEETS. Intervals and paired tests are present for RQ1/RQ2. They are absent for RQ3 rates and RQ4 contrasts, and there is no confusion matrix for the judge. Uncertainty: I recomputed proportions only. The bootstrap intervals and McNemar p-values cannot be checked without case-level data.

### S1: Within-case paired design with an exact diacritic manipulation
All five versions come from the same case, and the diacritic-free versions are produced deterministically. RQ2 is therefore a clean within-item manipulation, and the analysis respects the pairing.
**Evidence Anchor**: text: "All contrasts are paired by case."

### S2: Prespecified primary outcome with over-triage controls
Emergency under-triage is named as primary, urgent cases as secondary, and 28 soon/self-care controls measure over-triage. This blocks the trivial "always escalate" explanation and lets the paper show that the shift is toward less urgency overall.
**Evidence Anchor**: text: "Emergency under-triage is the primary outcome."

### S3: Per-model disaggregation with honest power framing
Per-model rates, paired differences with bootstrap CIs, exact McNemar with Holm correction, and an explicit statement that no single-model contrast survives correction. This avoids hiding heterogeneity behind the pooled mean.
**Evidence Anchor**: table: Table 3 (tab:main), per-model rows and Mean over models row

### S4: Judge blinded to case, gold label and version, and validated against blinded humans
The judge sees only the answer. Human labels were made without seeing model or version, and a second annotator overlapped on 60 answers. Binary emergency agreement of kappa 0.94 supports the primary outcome instrument.
**Evidence Anchor**: text: "never the case, the gold label or the version"

### S5: Sensitivity analyses on the weakest parts of the data
The pooled analysis was repeated without every pair flagged in the meaning check, and the remedy analysis on the documented-remedy subset. The primary effects held or grew. The urgent-case diacritic effects lost significance, and the paper reports this openly.
**Evidence Anchor**: text: "We repeated the pooled analysis without the ten cases whose clinical/folk pair was flagged by either rater"

### S6: Headline numbers reproduce from the tables
The abstract and Results means (22, 33, 48, 51 percent and the 11/25/29-point differences) reproduce from Table 3 as proportions of 126 model-case answers. The urgent, over-triage and remedy percentages are reachable at their implied denominators (receipts AR1 to AR5, AR7).
**Evidence Anchor**: text: "Folk wording raises the under-triage rate from 22\% to 33\% on average"

### W1: Remedy-endorsement results are headlined despite moderate judge validity and no intervals
The abstract reports unsafe endorsement in 10% of emergencies and up to half for one model (SeaLLMs, 7/14). The remedy-stance label was validated on only 32 answers, with judge-human kappa 0.50. That level leaves substantial misclassification, possibly model-dependent. No confidence intervals are given for endorsement rates, and none for the per-model 50% and 60% figures (n = 14 and n = 10). The Results and Limitations call these figures secondary or indicative, but the abstract presents them without that caveat. Remedy: give Wilson CIs for each rate, the remedy-stance confusion matrix, and a judge-corrected or human-only sensitivity estimate (or double-label all folk_rem answers on serious cases, 24 x 9 = 216). Either carry the kappa caveat into the abstract or remove the per-model claim from it.
**Severity**: Major
**Evidence Anchor**: text: "and in up to half for one model"
**Confidence**: 4 — agreement-statistic and small-proportion interval expertise

### W2: Mitigation conclusions have no inferential support
RQ4 claims rest on four models with one run each, and no CI or test is given:
- M1/M2 halve under-triage.
- The gap stays about 20 points.
- Over-triage rises 6 to 8 points.
- M2 gives no clear benefit over M1.

The per-model rows do not all move the same way. Under M1, Qwen2.5-7B folk under-triage rises from 29 to 43, and Gemini Flash-Lite folk rises from 0 to 14. Over-triage falls for Gemini Flash-Lite. Also, the base gap for these four models already averages about 20 points (50, 0, 21, 7). So the statement that the prompts "leave the gap" means the gap did not change at all. That should be said explicitly. Remedy: apply the same paired case-level bootstrap (prompt x version) used for RQ1/RQ2, report CIs for the under-triage change, the gap change and the over-triage change, and soften the abstract to match.
**Severity**: Major
**Evidence Anchor**: table: Table 4 (tab:mit), gap and over columns across base, m1, m2 rows
**Confidence**: 4 — paired-design inference expertise

### W3: Post hoc per-condition findings are promoted to a contribution and the conclusion
The claims that the trúng gió label "does not mislead" and that "conditions with less specific signs do" rest on the following:
- Each condition is typically a single case, so each rate is k/9 answers.
- The three conditions shown were chosen as "the largest shifts".
- No interval or test is given.

With one case per condition, condition is confounded with every other case feature (length, wording, source set). Selecting the largest shifts out of 14 also invites regression to the mean. E08, the trúng gió stroke case, is one of the two emergencies flagged in the meaning check. The Discussion then explains these differences by sign specificity, which is untested. Remedy: label this analysis exploratory, report all 14 conditions with intervals, and remove it from the contributions list and the conclusion, or temper it there.
**Severity**: Major
**Evidence Anchor**: text: "The best-known folk label (\vi{trúng gió} for stroke) does not mislead the models"
**Confidence**: 4 — small-sample and multiplicity expertise

### W4: Judge validation is reported only overall, not by version, model or prompt
The contrasts are threatened by differential misclassification more than by overall error:
- Agreement is not broken down by version (for example diacritic-free answers), by model, or for the Gemini Flash answers that the same-family judge scores.
- No confusion matrix is given.
- The 150-answer sample does not cover the M1/M2 or temperature-0.7 answers.
- The reference labeller is the first author, who knows the study hypotheses.

With kappa 0.94 this is unlikely to explain the 25-point diacritic effect. It could still affect the smaller 11-point folk effect and the near-zero Gemini rates. Remedy: report confusion matrices and agreement by version and by model family, and validate a stratified sample of mitigation answers.
**Severity**: Minor
**Evidence Anchor**: text: "Judge--human agreement on triage was $\kappa=0.90$ over the four labels and $\kappa=0.94$ for the binary emergency/not decision"
**Confidence**: 4 — LLM-as-judge validation expertise

### W5: The pooled estimate needs a stated estimand and a model-based check
The mean over models weights the nine models equally. Six of the nine are Qwen-derived (four Qwen models, Arcee-VyLinh built on Qwen2.5-3B, and SeaLLMs built on Qwen2), so the pooled effect mostly reflects one model lineage. Inference covers only these nine models, not "LLMs" generally. A percentile bootstrap over 14 clusters is also known to undercover. Remedy: state the estimand (an equal-weight average over this fixed model set). Add a mixed-effects logistic model with crossed random effects for case and model, or a BCa or cluster-wild interval, as a sensitivity check. Report the pooled effect excluding Qwen-lineage models.
**Severity**: Minor
**Evidence Anchor**: text: "The mean effect over models uses a case-level bootstrap that resamples cases for all models together"
**Confidence**: 4 — cluster bootstrap and GLMM expertise

### W6: The "do not compound" conclusion for RQ2 is not estimated
RQ2 asks whether the two effects compound. The answer rests on folk_nd being 3 points above clin_nd, with no interval for the interaction contrast (folk_nd - clin_nd - folk + clin). Remedy: report that contrast with its case-level bootstrap CI.
**Severity**: Minor
**Evidence Anchor**: text: "The two changes do not add up."
**Confidence**: 4 — factorial contrast expertise

### W7: Denominator of the over-triage column in Table 4 is unstated
SeaLLMs base over-triage is reported as 2%. No proportion of 28 control answers rounds to 2% (0/28 = 0%, 1/28 = 3.6%), so the cell must pool versions (for example 2/112), unlike the per-version over-triage in Section 5.2. This is not an error, but readers cannot reconstruct the cell (receipt AR6). Remedy: state the denominator and which versions are pooled.
**Severity**: Minor
**Evidence Anchor**: absence: Table 4 caption and RQ4 text — expected the number of answers behind each over-triage cell and which versions are pooled; checked Table 4 caption, RQ4 bullet list, Measures paragraph, Fig. 4 axis labels
**Confidence**: 4 — direct recomputation

### W8: Rerun variability is checked on two models only, without intervals
The sampling check covers two open models with majority vote and reports only folk_nd vs clin, with no CI and no estimate of within-prompt disagreement. The API models were run once at temperature 0, which is not guaranteed to be deterministic. Remedy: report the share of prompts whose majority label differs from the greedy label, give the paired difference with CI under sampling, and repeat a subset of the API calls.
**Severity**: Minor
**Evidence Anchor**: text: "With five samples at temperature 0.7 for Qwen2.5-7B and SeaLLMs, majority-vote under-triage kept the same direction"
**Confidence**: 3 — general decoding-robustness experience

### W9: The causal claim for folk wording is only partly identified
The folk version bundles lay vocabulary, register and a folk label. Only two controls carry lay wording without a label, so effects cannot be attributed to the folk label itself, which the Discussion does. The "same facts" premise rests on a meaning check with kappa 0.15. The raters used an LLM aid and differed in strictness, and two flagged cases were edited after rating without re-rating being reported. The flagged-pair sensitivity analysis mitigates this. Remedy: phrase the causal claim as applying to the bundled folk rewrite, and if feasible add a lay-wording-without-label version for emergencies.
**Severity**: Minor
**Evidence Anchor**: text: "Any change in the advice is then caused by the wording, not by missing information"
**Confidence**: 3 — design expertise; Vietnamese wording is outside my competence

### W10: Reproducibility identifiers are incomplete
The following are not given:
- model snapshot or revision identifiers (Hugging Face commit hashes, the Gemini version string), as API models change over time;
- the bootstrap seed;
- a statement that analysis code is released (the release statements list cases, lexicon, answers and labels).

Remedy: add these to Table 2 and the release statement.
**Severity**: Minor
**Evidence Anchor**: absence: Section 4 and Table 2 — expected model revision identifiers, bootstrap seed and an analysis-code release statement; checked Table 2 caption, Models and Prompting paragraphs, Statistics paragraph, Abstract and Conclusion release sentences
**Confidence**: 4 — reproducibility review experience

### W11: Non-answers are folded into under-triage without per-version reporting
"None" labels count as under-triage. This is defensible for safety, but it merges two mechanisms: lower urgency and failure to answer. Llama-3.1-8B's jump on folk_rem is driven by 35% none labels. Remedy: report none rates by model and version, and the main contrasts with none excluded.
**Severity**: Minor
**Evidence Anchor**: text: "answers labelled \emph{none} count as under-triage"
**Confidence**: 4 — outcome-definition expertise

### W12: The mechanism claim for diacritic loss rests on anecdotes
The claim that the emergency is lost in reading, before triage, is supported by two hand-picked answers. Remedy: frame it as a hypothesis. Alternatively, test it, for example by having the judge or annotators record whether the answer restates the key red-flag signs, compared by version.
**Severity**: Minor
**Evidence Anchor**: text: "The emergency is lost before any triage reasoning starts."
**Confidence**: 3 — inference-to-mechanism reasoning

Note on AR8. The reported smallest Holm-corrected p of 0.14 cannot be recomputed without the discordant counts. It is compatible with 9 one-directional discordant pairs (exact two-sided p = 2/512) multiplied by 36 tests, which would mean four contrasts per model including folk_rem. The Statistics paragraph should state the number of tests in the Holm family.

## Arithmetic Receipts

### AR1
procedure_id: grim
evidence_anchor: text: "They agreed on 43 of 52 pairs (83\%)"
reported_inputs: binary agree/disagree per pair; N = 52 pairs; reported proportion 83 percent; count 43
assumptions: unweighted proportion of 52 binary items; integer-percent precision as printed
derivation: 43/52 = 0.82692 = 82.69 percent
derived_value_or_range: 82.69 percent
comparison_rule: value must fall in the half-unit rounding interval of the reported integer percent
rounding_interval: [82.5, 83.5)
nearest_achievable: 42/52 = 80.77 percent; 43/52 = 82.69 percent; 44/52 = 84.62 percent
status: consistent

### AR2
procedure_id: grim
evidence_anchor: text: "models under-triaged 22\% of emergencies on average"
reported_inputs: binary under-triage per answer; 14 emergencies x 9 models = 126 answers (equal N per model so mean of per-model rates equals pooled proportion); reported 22 percent
assumptions: one answer per model-case (greedy decoding as stated); integer-percent precision
derivation: 28/126 = 0.22222 = 22.22 percent (per-model counts 0,0,1,2,3,3,5,6,8 from Table 3 clin column)
derived_value_or_range: 22.22 percent
comparison_rule: value must fall in the half-unit rounding interval of the reported integer percent
rounding_interval: [21.5, 22.5)
nearest_achievable: 27/126 = 21.43 percent; 28/126 = 22.22 percent; 29/126 = 23.02 percent
status: consistent

### AR3
procedure_id: grim
evidence_anchor: text: "and folk wording without diacritics to 51\%"
reported_inputs: binary under-triage per answer; N = 126 answers; reported 51 percent
assumptions: one answer per model-case; integer-percent precision
derivation: 64/126 = 0.50794 = 50.79 percent (per-model counts 1,1,9,8,6,10,5,13,11)
derived_value_or_range: 50.79 percent
comparison_rule: value must fall in the half-unit rounding interval of the reported integer percent
rounding_interval: [50.5, 51.5)
nearest_achievable: 63/126 = 50.00 percent; 64/126 = 50.79 percent; 65/126 = 51.59 percent
status: consistent

### AR4
procedure_id: grim
evidence_anchor: text: "clinical wording: 6\%"
reported_inputs: binary home-care-or-none per answer on urgent cases; 10 cases x 9 models = 90 answers; reported 6 percent
assumptions: one answer per model-case; integer-percent precision
derivation: 5/90 = 0.05556 = 5.56 percent
derived_value_or_range: 5.56 percent
comparison_rule: value must fall in the half-unit rounding interval of the reported integer percent
rounding_interval: [5.5, 6.5)
nearest_achievable: 4/90 = 4.44 percent; 5/90 = 5.56 percent; 6/90 = 6.67 percent
status: consistent

### AR5
procedure_id: grim
evidence_anchor: text: "It fell slightly, from 27\% (clinical) to 23\% (folk)"
reported_inputs: binary emergency label on controls; 28 controls x 9 models = 252 answers; reported 27 percent
assumptions: one answer per model-case; integer-percent precision
derivation: 68/252 = 0.26984 = 26.98 percent
derived_value_or_range: 26.98 percent (69/252 = 27.38 percent also qualifies)
comparison_rule: value must fall in the half-unit rounding interval of the reported integer percent
rounding_interval: [26.5, 27.5)
nearest_achievable: 68/252 = 26.98 percent; 69/252 = 27.38 percent
status: consistent

### AR6
procedure_id: grim
evidence_anchor: table: Table 4 (tab:mit), SeaLLMs-v3-7B-Chat base row, over column
reported_inputs: over-triage reported 2 percent; controls per model = 28; number of versions pooled not stated
assumptions: binary emergency label per answer; integer-percent precision; analytic N not licensed by the paper
derivation: with N = 28 attainable values are 0/28 = 0.00 and 1/28 = 3.57 percent, neither rounds to 2; with N = 112 (4 versions) 2/112 = 1.79 percent rounds to 2; with N = 140 (5 versions) 3/140 = 2.14 percent rounds to 2
derived_value_or_range: reachable only if N is at least about 50; per-version N = 28 unreachable
comparison_rule: value must fall in [1.5, 2.5) at the true analytic N
status: not_computable
not_computable_reason: analytic_n_ambiguous

### AR7
procedure_id: grim
evidence_anchor: text: "because 35\% of its remedy answers gave no usable advice"
reported_inputs: binary none label; Llama-3.1-8B folk_rem answers, one per case, N = 52; reported 35 percent
assumptions: every case has a remedy version as stated, so N = 52; integer-percent precision
derivation: 18/52 = 0.34615 = 34.62 percent
derived_value_or_range: 34.62 percent
comparison_rule: value must fall in the half-unit rounding interval of the reported integer percent
rounding_interval: [34.5, 35.5)
nearest_achievable: 17/52 = 32.69 percent; 18/52 = 34.62 percent; 19/52 = 36.54 percent
status: consistent

### AR8
procedure_id: p_from_test_statistic
evidence_anchor: text: "smallest corrected $p=0.14$"
reported_inputs: test family exact McNemar, Holm-corrected over all models x contrasts; corrected p = 0.14; discordant counts and family size not reported
assumptions: none beyond the stated exact McNemar and Holm procedure
derivation: exact and Holm-adjusted p require the discordant pair counts and the number of tests, neither reported; illustrative only, 9 one-directional discordant pairs give exact two-sided p = 2/512 = 0.0039, times 36 tests = 0.141, times 27 tests = 0.105
derived_value_or_range: not derived
comparison_rule: reported adjusted p must equal the Holm-adjusted exact binomial p at the reported precision
tail_convention: unstated
status: not_computable
not_computable_reason: nonstandard_p_procedure
