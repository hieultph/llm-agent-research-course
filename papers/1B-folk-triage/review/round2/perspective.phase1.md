## Contract Paraphrase

D1 (methodology_rigor, mandatory, owned by the methodology seat): The design, data handling, statistics and reproducibility material have to reach the normal peer-review standard for the field. From my cross-disciplinary seat I do not score this. I will only pass on points where a methodological choice changes what clinicians or app developers could safely conclude, for example how a triage reference standard was set and whether its validity survives each transformation applied to the test items.

D2 (domain_accuracy, mandatory, owned by the domain seat): Claims must match current evidence, prior work must be represented correctly, and domain terms and results must be free of factual errors. I do not score this. As an outside reader from emergency medicine and digital-health safety, I may flag clinical terminology or urgency categories that an adjacent-field reader would read differently from how they are presented, and leave the judgement to the domain seat.

D3 (argumentative_coherence, mandatory, owned by the devil's advocate, also eligible to methodology): The core thesis must hang together, the evidence must support the claims, and no fallacy may undermine the central argument. I do not score this. I will note any place where practical or deployment conclusions go beyond what the evidence supports, but stress-testing the argument belongs to the devil's advocate.

D4 (cross_disciplinary_relevance, high priority, owned by my perspective seat): The framing, definitions and implications have to be accessible to readers in adjacent fields, here clinicians, patient-safety and digital-health practitioners, public-health and medical-anthropology readers, and health-app developers. Any claim that crosses disciplines has to be backed up. This is the only dimension I score. I will judge it on clinical validity of the triage framing, how harm is framed, the ethics of how folk beliefs and users are represented, and whether the advice to practitioners is concrete and in proportion to the evidence.

D5 (writing_and_structure, normal priority, owned by the journal-fit seat): Organisation, clarity, figure and table quality and venue conventions. I do not score this. I may mention clarity problems that specifically block a clinical or non-NLP reader.

D6 (venue_fit_and_contribution, mandatory, owned by the journal-fit seat): The work has to fit the configured venue and make an original, significant contribution for its readers. I do not score this. Because no specific venue is bound, I make no claim about alignment with any venue.

## Scoring Plan

### D4: cross_disciplinary_relevance
dimension_id: D4
what_to_look_for: Whether triage categories and the under-triage and over-triage definitions are stated in clinically recognisable terms and tied to a named reference standard; whether physician-assigned labels kept across reworded or translated item versions are justified or re-checked by a clinician; whether harm from endorsing unsafe folk remedies is defined separately from triage error; whether the trade-off of a mitigation (fewer under-triage cases against more over-triage) is explained for real deployment, including load on emergency services; whether folk-illness concepts are presented respectfully, with enough cultural context for non-specialist readers and without stereotyping the users who hold them; whether model outputs that contain unsafe advice come with content warnings and a safe release plan; and whether recommendations to health-app developers are concrete, actionable and limited to what a prompt-level fix can actually achieve.
what_triggers_block: Practical or clinical recommendations that an adjacent-field reader would take as deployment-ready, such as presenting a prompt change as a sufficient safety fix, while the paper either has no clinically valid reference standard for its triage labels or does not mention the over-triage cost of the mitigation, so a practitioner acting on the paper could be misled about patient safety.
what_triggers_warn: The clinical, harm and ethics framing holds up overall but has gaps an adjacent-field reader would notice: labels carried across versions without stating that no clinician re-checked them, harm definitions or deployment trade-offs that are only loosely explained, folk-illness context too thin for non-specialists, release or content-warning handling of unsafe outputs left underspecified, or developer recommendations that are generic rather than concrete.

criteria_binding_unavailable

[CONTRACT-ACKNOWLEDGED]
