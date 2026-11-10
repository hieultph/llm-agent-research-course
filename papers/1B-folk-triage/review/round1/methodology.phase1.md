## Contract Paraphrase

D1 (methodology_rigor, mandatory, owned by methodology): I read this as asking whether the design can actually answer the stated research questions at the stated level of confidence. From a methodology standpoint that means the unit of analysis is defined and counted correctly; paired or clustered structure is respected in the inference; uncertainty is reported with intervals and the method that produced them; multiple comparisons are acknowledged and handled; any automated labelling instrument is validated against human judgement with an agreement statistic; decoding settings, reruns and data handling are documented; and the materials released would let another team reproduce the numbers.

D2 (domain_accuracy, mandatory, owned by domain): Domain claims must agree with current evidence in the field, prior work must be represented faithfully, and terminology and reported results from other studies must be correct. My only methodological interest here is whether reference standards and outcome definitions borrowed from the domain are applied as their sources define them; the judgement belongs to the domain seat.

D3 (argumentative_coherence, mandatory, owned by da, methodology eligible): The central thesis has to hang together and follow from the evidence presented, without fallacies that undermine it. My methodological angle is the inferential link between results and claims: whether the strength of each conclusion matches the strength of the statistical evidence, whether causal or general wording outruns what the design permits, and whether null or contrary results are reported as honestly as supportive ones.

D4 (cross_disciplinary_relevance, high, owned by perspective): Framing, definitions and implications should be understandable to readers in neighbouring fields, and any claim that crosses disciplinary lines should be backed up. From a methods view, this includes defining the outcome measures and statistics clearly enough for a non-specialist to interpret them.

D5 (writing_and_structure, normal, owned by eic): The manuscript should be well organised and clearly written, with tables and figures that are accurate and readable, and it should follow venue conventions. Methodologically, tables and figures should show the denominators, intervals and conditions needed to interpret them.

D6 (venue_fit_and_contribution, mandatory, owned by eic): The work should suit the target venue and make an original, significant contribution for its readers. A methods reviewer cares that the claimed contribution is one the evidence can carry, but this judgement rests with the editor seat.

## Scoring Plan

### D1: methodology_rigor
dimension_id: D1
what_to_look_for: Explicit unit of analysis and counts per condition; inference that respects pairing and clustering (paired tests such as McNemar or exact tests, cluster or item-level bootstrap intervals); effect sizes with confidence intervals; a power or precision statement suited to the number of independent items; a stated correction or framing for multiple contrasts; justification for any pooling across models or conditions, plus per-model breakdowns; validation of any automated or LLM judge against blinded human labels with chance-corrected agreement and confusion matrices; documented decoding parameters, rerun or seed variability, handling of refusals, truncations and API failures; prespecified versus post hoc subset and robustness analyses clearly distinguished; released prompts, items, code and outputs sufficient for reproduction.
what_triggers_block: A headline comparison that ignores pairing or clustering, so its intervals or p-values are invalid; pooled estimates without per-model results where models plainly differ; an automated judge used as the primary outcome measure with no human validation or with agreement too low to support the reported differences; or undisclosed handling of missing, failed or excluded generations that could shift the main effect.
what_triggers_warn: Methods that are sound in principle but under-reported or under-powered: intervals present but wide and not discussed; multiple contrasts without correction or an explicit exploratory label; human validation done on a small or non-random subset; single-run results with no estimate of rerun variability; robustness or subset analyses missing or post hoc without being labelled as such; reproducibility materials incomplete.
what_triggers_fatal: The design cannot answer the research question at all: the outcome measure is shown to be invalid or circular (for example the judge being evaluated is also the reference), the reported effects cannot be recomputed from the described data and procedure, or there is evidence of data leakage or fabricated or selectively reported results that invalidates the core findings.

### D3: argumentative_coherence
dimension_id: D3
what_to_look_for: Each claim in the abstract, conclusion and title traced back to a specific result with its uncertainty; claim strength calibrated to sample size, interval width and number of models tested; mechanistic or causal language supported by a design that manipulates the factor of interest with suitable controls; generalisation limited to the populations, languages and models actually sampled; null, mixed or contrary results reported and discussed instead of omitted; limitations that address the main threats to validity named in the methods.
what_triggers_block: A central claim rests on a contrast that is not statistically supported or is contradicted by the paper's own reported numbers, or causal or general conclusions are drawn from a design that cannot isolate the claimed factor, and this overreach is load-bearing for the thesis.
what_triggers_warn: Wording overstates the evidence in places (for example generalising beyond the sampled models or items, or treating a non-significant trend as an effect) without changing the core thesis; limitations exist but leave out a material validity threat; some results that cut against the narrative get less attention than supportive ones.
what_triggers_fatal: The core thesis is contradicted by the paper's own primary results, or depends on a logical or statistical fallacy so basic that removing it leaves no supported central claim.

criteria_binding_unavailable

[CONTRACT-ACKNOWLEDGED]
