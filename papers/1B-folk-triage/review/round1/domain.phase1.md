## Contract Paraphrase

D1 (methodology_rigor, mandatory, owned by the methodology seat): The study design, the handling of data, the statistical reporting and the material needed to reproduce the work must meet what peer reviewers in this field normally expect. From a domain standpoint this matters because a dataset built through translation, lexicon substitution or input perturbation is only as trustworthy as the documented procedure behind it, but scoring this dimension is not my seat's job.

D2 (domain_accuracy, mandatory, owned by my seat): Claims must agree with current evidence in the field, prior work must be described correctly, and domain terminology and reported results must be free of factual errors. For me this means checking that the related-work coverage of Vietnamese NLP robustness, diacritic restoration, non-standard and dialectal input, and Vietnamese (medical) LLM benchmarks is complete and fairly represented; that the construction of language resources (translation, lexicons, meaning-preservation checks) follows sound practice; and that every linguistic explanation offered for model behaviour is backed by evidence rather than asserted.

D3 (argumentative_coherence, mandatory, owned by the devil's advocate seat): The central thesis must hold together internally, the evidence must actually support the conclusions drawn, and there must be no reasoning fallacy that undermines the main argument. Domain accuracy feeds into this, since a mischaracterised linguistic phenomenon can make an otherwise valid inference unsound, but the coherence judgement belongs to other seats.

D4 (cross_disciplinary_relevance, high, owned by the perspective seat): Framing, definitions and implications must be understandable to readers from neighbouring fields, and any claim that crosses disciplinary lines must be substantiated. Language-specific concepts need to be explained well enough that non-specialist readers do not misread them; assessing that accessibility is the perspective seat's responsibility.

D5 (writing_and_structure, normal, owned by the editor-in-chief seat): The manuscript's organisation, clarity, figures and tables, and adherence to venue conventions must be adequate. Correct rendering of language-specific examples is a domain concern, but the overall writing judgement is not mine to score.

D6 (venue_fit_and_contribution, mandatory, owned by the editor-in-chief seat): The work must suit the configured venue and offer an original, significant contribution for its readers. Whether the contribution is genuinely new relative to existing work in the field informs this, but the fit-and-significance verdict is scored by the editor-in-chief seat.

## Scoring Plan

### D2: domain_accuracy
dimension_id: D2
what_to_look_for: Accurate and reasonably complete coverage of Vietnamese NLP robustness, diacritic restoration, non-standard and dialectal input, and Vietnamese general and medical LLM benchmarks; correct representation of cited prior results; sound and documented construction of language resources (translation, lexicon, meaning-preservation check) with sources and licences; correct linguistic terminology; and linguistic explanations of model behaviour that are supported by data, examples or cited evidence rather than asserted.
what_triggers_block: A central domain claim or a key prior result is misrepresented, or the language-resource construction contains a substantive linguistic error that bears on the main findings, or a headline linguistic explanation is presented as established without any supporting evidence, such that correcting it requires substantial revision.
what_triggers_warn: Notable but non-central gaps such as missing closely related Vietnamese robustness, diacritic or benchmark references, imprecise terminology, under-documented translation or lexicon procedures, or secondary linguistic explanations stated more strongly than the evidence allows, all fixable in a revision without changing the conclusions.
what_triggers_fatal: The core findings rest on a demonstrably false linguistic premise or on language resources that do not measure what is claimed (for example perturbations that change meaning rather than form), or prior work is fabricated or so misrepresented that the claimed contribution cannot stand.
criteria_binding_unavailable

[CONTRACT-ACKNOWLEDGED]
