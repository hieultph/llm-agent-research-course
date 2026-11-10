## Contract Paraphrase

D1 (methodology_rigor, mandatory, owned by methodology). I read this as asking whether the design can actually answer the stated questions and whether the numbers can be trusted and reproduced. From a biostatistics standpoint that means: the unit of analysis is stated and the inference respects it (clustering of repeated outputs within index cases and models); uncertainty is reported with intervals that suit the sample size and dependence structure; confirmatory hypotheses are separated from exploratory analyses, with multiple-testing handling where several comparisons are made; any automated scoring instrument is validated against human judgement, with agreement reported as chance-corrected statistics and intervals; and enough material (prompts, configurations, seeds or sampling settings, scoring rubrics, data release terms) is provided for an independent group to rerun the pipeline.

D2 (domain_accuracy, mandatory, owned by domain). This dimension asks whether clinical and linguistic claims match current evidence and whether prior work is represented correctly. It is not mine to score; from the methodology side, I note only that the reference standard used for any accuracy measure depends on domain correctness, so a weak reference standard would weaken every downstream statistic I assess.

D3 (argumentative_coherence, mandatory, owned by da, methodology eligible). I read this as whether the conclusions follow from the evidence actually presented. My angle is the statistical link between results and claims: effect sizes and intervals are not over-read, subgroup or per-unit differences resting on very few cases are not presented as established, null or underpowered results are not read as evidence of no difference, and the numbers in text, tables and figures agree with each other.

D4 (cross_disciplinary_relevance, high, owned by perspective). This asks whether framing, definitions and implications are accessible and substantiated for readers in adjacent fields. Not mine to score; methodologically it overlaps only where terms such as accuracy, agreement or safety are defined operationally.

D5 (writing_and_structure, normal, owned by eic). This covers organisation, clarity, figure and table quality and venue conventions. Not mine to score, though figure-table-text consistency of reported numbers is something I check under D1 and D3.

D6 (venue_fit_and_contribution, mandatory, owned by eic). This asks whether the work fits the target venue and contributes something original and significant. Not mine to score; I make no venue-alignment claim because no target criteria are bound for this call.

## Scoring Plan

### D1: methodology_rigor
dimension_id: D1
what_to_look_for: Explicit unit of analysis and sample size per arm; intervals (e.g. Wilson for proportions, paired or cluster bootstrap for differences) that account for repeated outputs within index cases and models; pre-specified primary outcome versus exploratory analyses; multiple-comparison handling; human validation of any automated judge with chance-corrected agreement and intervals per label, plus disclosure of judge-model overlap with evaluated models; reference-standard construction; reproducibility artefacts (prompts, model versions, decoding settings, rubric, code and data availability with licence).
what_triggers_block: A headline comparison whose inference ignores clustering or pairing so that its interval or significance is materially misstated, or a primary outcome scored by an automated judge with no human validation of that label, or a key quantity that cannot be traced to a reported procedure.
what_triggers_warn: Methods that are defensible but incompletely reported, such as missing intervals on secondary results, moderate judge-human agreement on a secondary label without discussion of its effect, no correction across many exploratory comparisons, or reproducibility details that are partial but recoverable.
what_triggers_fatal: The design cannot answer its own research question, for example the reference standard or outcome definition is circular with the system being evaluated, or reported results cannot have been produced by the described procedure.

### D3: argumentative_coherence
dimension_id: D3
what_to_look_for: Whether each conclusion is backed by an estimate with stated uncertainty; whether subgroup claims rest on adequate numbers of independent cases; whether exploratory findings are labelled as such; whether non-significant or wide-interval results are described without implying equivalence; whether figures, tables and text report the same values.
what_triggers_block: A central claim depends on a subgroup or per-unit difference whose interval is compatible with no effect yet is stated as a finding, or text and table/figure values conflict for a number that carries a main conclusion.
what_triggers_warn: Hedged but still overconfident language on secondary or subgroup results, minor numeric mismatches between text and figures that do not change a conclusion, or limitations acknowledged but not reflected in the strength of the claims.
what_triggers_fatal: The main thesis is contradicted by the paper's own reported numbers, or rests entirely on an analysis that the paper itself shows to be invalid.

criteria_binding_unavailable

[CONTRACT-ACKNOWLEDGED]
