## Contract Paraphrase

D1 (methodology_rigor, mandatory, owned by the methodology seat): The study design, how data are handled, how statistics are reported, and whether others could reproduce the work must reach the usual peer-review standard of the field. I do not score this. From a domain angle, I only note where a design choice matters for domain claims, for example how evaluation items were sourced or transformed, and I pass it to the methodology seat.

D2 (domain_accuracy, mandatory, owned by me): Claims must match current evidence in the field. Prior work must be described correctly and completely enough that the novelty claim can be checked. Domain terms and reported results from the literature must be stated correctly. For this field, that means LLM robustness on medical triage and consumer health questions, non-standard and noisy input, Vietnamese NLP (including diacritic restoration and Vietnamese LLM and medical benchmarks), and how any input-variant resource is built and documented. This is the dimension I score.

D3 (argumentative_coherence, mandatory, owned by the devil's advocate with methodology also eligible): The central thesis must hold together, the evidence must support the claims made, and no reasoning error may undermine the main argument. I do not score this. I flag domain cases where a mechanism is stated as established when the evidence only allows it as a hypothesis.

D4 (cross_disciplinary_relevance, high priority, owned by the perspective seat): Framing, definitions and implications must be clear to readers in neighbouring fields, and claims that cross disciplines must be backed by evidence. I do not score this.

D5 (writing_and_structure, normal priority, owned by the EIC): Organisation, clarity, figure and table quality, and adherence to venue conventions. I do not score this.

D6 (venue_fit_and_contribution, mandatory, owned by the EIC): The work must suit the target venue and make an original and significant contribution for its readers. I do not score this. My D2 judgement on whether the novelty claim survives the related-work check is input the EIC may use.

## Scoring Plan

### D2: domain_accuracy
dimension_id: D2
what_to_look_for: Related work covers the main lines (LLM triage and consumer-health QA robustness, perturbation and non-standard-input evaluation, Vietnamese medical and general LLM benchmarks, diacritic restoration and unaccented-text processing) and describes each cited work correctly; the novelty claim is stated at a scope the cited literature supports; dataset construction (translation, rewriting into colloquial or regional wording, meaning-preservation check, term lexicon, diacritic removal) is described with sources, licences and validation that match field practice, and the realism limits of automatically removed diacritics versus naturally unaccented user text are acknowledged; any proposed mechanism for the observed effects is either supported by direct evidence or labelled as a hypothesis; the released resource has enough documentation (schema, provenance, licence, intended use, known limits) for others to reuse it.
what_triggers_block: A closely related prior work or benchmark that undercuts or narrows the novelty claim is missing or misdescribed; or a mechanism for the effects is presented as established without supporting analysis; or the construction of transformed inputs lacks a stated meaning-preservation check or provenance needed to judge domain validity; or the released resource lacks the documentation or licence information needed for reuse.
what_triggers_warn: Coverage of one relevant strand is thin but does not change the novelty claim; minor inaccuracies in describing cited work or in domain terminology; realism limits of synthetic input variants are mentioned only briefly; resource documentation is present but incomplete on secondary points such as lexicon coverage or known failure cases.
what_triggers_fatal: The central novelty claim is directly contradicted by existing published work that the paper omits or misrepresents, or a core domain fact or cited result on which the main conclusion rests is factually wrong, such that the contribution cannot stand as stated.
criteria_binding_unavailable

[CONTRACT-ACKNOWLEDGED]
