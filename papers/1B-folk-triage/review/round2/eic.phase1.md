## Contract Paraphrase

D1 (methodology_rigor), mandatory, scored by the methodology seat. From an editorial-oversight view, this asks whether the study design, data handling, statistical reporting and reproducibility support would pass ordinary peer review in this field. I will not score it, but if the methodology seat finds a serious flaw, my verdicts on contribution and fit have to account for it.

D2 (domain_accuracy), mandatory, scored by the domain seat. This asks whether the claims match current domain evidence, whether prior work is described correctly, and whether domain terms and reported results are free of factual errors. From an editorial view, a domain error weakens any claim of a significant contribution, so I will take the domain seat's finding into account but not score it myself.

D3 (argumentative_coherence), mandatory, scored by the devil's-advocate and methodology seats. This asks whether the central thesis holds together, whether the evidence supports what is claimed, and whether any reasoning error undermines the main argument. For editorial oversight, this is where I check that the headline message a reader takes away is actually supported by the evidence.

D4 (cross_disciplinary_relevance), high priority, scored by the perspective seat. This asks whether the framing, definitions and implications are accessible to readers from neighbouring fields, and whether claims that cross disciplines are backed up. For a mixed readership of clinicians, health informaticians and ML researchers, this is closely tied to journal fit, but the score belongs to the perspective seat.

D5 (writing_and_structure), normal priority, scored by me. This asks whether the manuscript is well organised, clearly written, uses figures and tables well and follows venue conventions. I will judge it as an area chair would read an LNCS-style submission: does the title and abstract match the findings, do the figures add to the tables rather than repeat them, and does the length suit a typical 12 to 16 page proceedings limit.

D6 (venue_fit_and_contribution), mandatory, scored by me. This asks whether the manuscript suits an applied AI-in-healthcare venue and makes an original, significant contribution for that readership. I will judge whether a reader leaves with one clear safety message and a takeaway that health-app builders can act on, and whether the clinical-safety framing is proportionate to evidence gathered without clinician involvement.

## Scoring Plan

### D5: writing_and_structure
dimension_id: D5
what_to_look_for: Title and abstract that state the findings accurately; a logical section order a busy area chair can skim; figures that add information beyond the tables; captions that stand alone; length and formatting consistent with LNCS proceedings conventions and a 12-16 page limit.
what_triggers_block: The title or abstract claims findings the results do not show, or the main text clearly exceeds a typical proceedings page limit with no obvious path to trimming, or key results can only be followed through appendices.
what_triggers_warn: Figures that largely repeat table content, captions or section transitions that need cross-referencing to follow, uneven section lengths, or minor departures from LNCS formatting that will need fixing before camera-ready.

### D6: venue_fit_and_contribution
dimension_id: D6
what_to_look_for: A contribution the AI-in-healthcare audience would see as new compared with existing LLM health-advice evaluations; one clearly stated safety message; at least one concrete, actionable recommendation for health-app builders; clinical-safety claims scaled to the evidence that was actually collected, including whether clinicians were involved.
what_triggers_block: The paper offers no clear safety message or actionable takeaway for builders, or it makes clinical-safety claims well beyond its evidence (for example, presenting non-clinician judgements as clinical validation) in a way that a framing revision could fix but that currently misleads readers.
what_triggers_warn: The contribution is relevant but only incrementally new, the safety message is spread across several competing claims, or the safety framing slightly overstates the evidence and needs hedging or an explicit limitations statement.
what_triggers_fatal: The work is outside the scope of an AI-in-healthcare venue, or its central contribution duplicates existing work with no new insight, or its core safety claim depends on evidence the study design cannot provide, so that no revision within the venue's scope could make the contribution sound.

criteria_binding_unavailable

[CONTRACT-ACKNOWLEDGED]
