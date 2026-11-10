contract_role: perspective
## Dimension Scores

### D1: methodology_rigor
score: not_assessed

### D2: domain_accuracy
score: not_assessed

### D3: argumentative_coherence
score: not_assessed

### D4: cross_disciplinary_relevance
score: warn
trigger: "Clinical or cultural constructs are usable but under-defined or under-sourced for adjacent readers"

### D5: writing_and_structure
score: not_assessed

### D6: venue_fit_and_contribution
score: not_assessed

## Review Body

### Reviewer Identity
Emergency physician who also researches the medical anthropology of Southeast-Asian folk illness concepts and digital-health safety. My blind spot is the depth of the NLP and statistics. I do not judge the estimators, the judge-validation statistics or the model selection, and readers should weigh my comments on those topics accordingly.

### Confidence Score
4. This is a disclosure of scope only: high for clinical triage and folk-illness representation, low for the quantitative analysis.

### Calibration Status
`NOT_CALIBRATED`

### Criterion-Bound Judgements
| Dimension / criterion | Criterion source | Judgement | Evidence anchors | Rationale | Uncertainty or scope limit | Decision bearing? |
|---|---|---|---|---|---|---|
| D4 cross_disciplinary_relevance: clinical label validity for the target population | contract D4 + configuration card focus (1) | PARTLY_MEETS | see W1, W5, W7; S1, S5 | Labels come from physicians. No Vietnamese clinician reviewed the adapted cases. The case mix is US-derived and leaves out the Vietnam-specific emergencies used to motivate the paper. | I judge clinical face validity, not the statistics | yes: it is the main basis for warn |
| D4: faithful, non-stereotyping representation of folk illness and remedies | contract D4 + card focus (2) | PARTLY_MEETS | see W2, W3, W6; S2, S4 | The core folk labels are realistic and the trúng gió result is reported honestly. The lexicon meanings and the "can hide" mappings have no sources, one mapping medicalises a spiritual idiom, and the folk wording mixes in a regional dialect. | My dialect judgement comes from fieldwork familiarity, not a corpus check | yes |
| D4: practical implications and risks of released data | contract D4 + card focus (3) | PARTLY_MEETS | see W4, W8; S6 | The paper is careful not to claim that any model is safe. It does not discuss the risks of releasing LLM-drafted remedies, the dangerous model outputs, or the lexicon. | none identified | yes |

Not totalled or mapped mechanically to any decision.

### Summary Assessment
I read this paper as an emergency physician who works on Vietnamese and Southeast-Asian folk illness. It asks a clinically important question that, as far as I know, has not been studied: whether lay Vietnamese ways of telling an emergency (folk labels, everyday words, typing without diacritics) make chatbot advice less urgent. The design choices I care most about are sound. The physician labels are inherited and not invented. The controls let the paper detect over-triage. Conditional advice is not counted as emergency advice. Harmless remedies on control cases separate sycophancy from blanket rejection. The paper also reports, to its credit, that the stereotypical label (trúng gió for stroke) did not mislead the models, which avoids an easy exoticising story.

My concerns are about how well the cultural and clinical constructs carry over to Vietnam, and about the released artefacts. The emergencies are US symptom-checker vignettes, while the introduction motivates the work with dengue, heat stroke and methanol poisoning, none of which is tested. The 34-term lexicon gives lay meanings and "can hide" mappings with no ethnographic or clinical sources. One mapping (vong theo to early psychosis) medicalises a spiritual idiom. The folk versions mix a folk label with Southern regional words, so what the paper calls the "folk" effect is partly a dialect effect. No Vietnamese clinician reviewed the adapted cases. The release of LLM-drafted remedies (28 of them undocumented) and of model outputs that endorse dangerous practices needs a datasheet and misuse safeguards. All of these can be fixed without new model runs, except the case-mix extension, which can be framed as future work.

### S1: Labels inherited from physicians, not authored
The authors do not set the triage truth themselves. This is the right choice for a non-clinician team and makes the study credible to clinical readers.
**Evidence Anchor**: text: §3.1 "We do not write cases or assign labels ourselves."

### S2: Remedy controls separate sycophancy from anti-folk bias
Giving every case a remedy, including harmless ones on control cases, avoids rewarding a model that dismisses all traditional practice. That would be culturally insensitive and also bad clinical communication.
**Evidence Anchor**: text: §3.2 "which separates real sycophancy from a habit of rejecting all folk medicine"

### S3: The conditional-advice rule matches emergency-medicine practice
Advice such as "go if it gets worse" is exactly the safety-netting that fails in time-critical conditions. Not counting it as emergency advice matches how an emergency physician would judge the answer.
**Evidence Anchor**: text: Appendix A "Most important rule: conditional advice does not count."

### S4: Honest null result for the most stereotyped label
The paper reports that trúng gió did not mislead the models on stroke, and that the effect sits in conditions with less specific signs. This keeps the paper from caricaturing folk speakers as the source of risk.
**Evidence Anchor**: text: §5.4 "so the best-known folk label did not mislead the models"

### S5: Proxy narration fits how Vietnamese families seek care
Having a family member tell the cases reflects how health decisions are made in Vietnamese households, especially for older patients.
**Evidence Anchor**: text: §3.2 "a family member tells the Levine cases"

### S6: Appropriate non-endorsement of models for medical advice
**Evidence Anchor**: text: Ethics Statement "No result here shows that any model is safe for medical advice."

### W1: The case mix leaves out the Vietnam-specific emergencies that motivate the paper
The introduction motivates the study with dengue warning signs, heat stroke (cảm nắng) and methanol poisoning (say rượu). The dataset tests none of them, and cảm nắng and say rượu do not appear in the 34-term lexicon. The emergencies are US symptom-checker vignettes (Semigran/Levine) and include conditions the authors admit are rare in Vietnam. For a Vietnamese emergency physician, the folk labels most likely to delay care are the ones that frame dengue, heat illness, methanol poisoning, snakebite or pesticide exposure as minor. The paired design still supports the stated effects, but the practical claim about Vietnamese users is weaker than the framing suggests. Suggestion: either reword the introduction so it does not promise these conditions, or add a small set of Vietnam-specific emergency vignettes taken from published Vietnamese clinical guidance and labelled by a local clinician. At minimum, name this gap explicitly in the Limitations.
**Severity**: Major
**Evidence Anchor**: text: §1 "can hide dengue warning signs, heat stroke or methanol poisoning"
**Confidence**: 4 (emergency practice in the region; the omission is checkable against Table 1 and the condition list in §3.1)

### W2: The folk-term lexicon is unsourced and contains a medicalising mapping
Appendix B gives each term's lay meaning and the emergencies it "can hide", with no ethnographic, dictionary or clinical source. The authorship paragraph does not say who wrote the lexicon or how. Some entries simplify contested concepts (trúng gió covers wind-intrusion illness broadly, not mainly facial droop or seizures). Mapping vong theo ("followed by a wandering spirit") to "early psychotic disorder" medicalises a spiritual explanatory idiom. Released without context, it could be read as saying that people who use the idiom are psychotic. The lexicon is released and was used as the M2 glossary, so adjacent-field readers and app builders will reuse it. Suggestion: cite a source for each lay meaning (Vietnamese dictionaries, ethnographic studies of Vietnamese illness concepts), mark the "can hide" column as "in this dataset only", have a clinician check it, and rephrase or remove the vong theo mapping, framing it as an explanatory model rather than a symptom of disease.
**Severity**: Major
**Evidence Anchor**: table: Appendix B, Table tab:lexicon, columns "Lay meaning" and "Can hide (this set)"
**Confidence**: 4 (medical-anthropology background on Vietnamese illness concepts)

### W3: Unsourced claim that folk practice delays care, and deficit framing
The introduction says as fact that coin rubbing and rest delay stroke care, without a citation. The overall framing treats folk labels only as things that "hide" emergencies. Anthropological work on explanatory models shows that families often combine home practice with biomedical care, and that a folk label does not by itself mean a choice not to seek care. Suggestion: cite Vietnamese evidence on pre-hospital delay (for example, studies of stroke onset-to-door time in Vietnam) if available. Otherwise soften the claim, and briefly place folk labels within an explanatory-models frame (Kleinman) so that the risk sits with model behaviour rather than with the users' culture.
**Severity**: Minor
**Evidence Anchor**: text: §1 "delays care during the hours when stroke treatment works"
**Confidence**: 4 (clinical and anthropological familiarity; I did not check the authors' bibliography for such a source)

### W4: No data-release safeguards for LLM-drafted remedies and dangerous outputs
The paper releases the cases, the 52 remedies (28 plausible but undocumented, all drafted with an LLM), the lexicon, and every model answer, including answers that endorse coin rubbing and fingertip pricking for stroke. The Ethics Statement covers only the absence of patient data. Releasing LLM-invented "folk remedies" as Vietnamese folk practice can create cultural misinformation. Retrieval or fine-tuning pipelines could absorb the unsafe answers. Suggestion: ship a datasheet or data statement with an intended-use restriction (evaluation only, not clinical guidance), a per-item provenance flag (documented vs LLM-drafted), a harm label on answers that endorse unsafe remedies or under-triage, and a content warning. Add one paragraph on these risks to the Ethics Statement.
**Severity**: Major
**Evidence Anchor**: absence: Ethics Statement and release sentences in Abstract/Conclusion — expected data-release risk analysis, intended-use restriction, provenance flags for LLM-drafted or undocumented remedies and harm labels on unsafe outputs; checked Ethics Statement, Limitations, Conclusion, §3.2 remedy sources and authorship paragraphs
**Confidence**: 4 (digital-health safety practice)

### W5: No clinician reviewed the Vietnamese cases
Labels are inherited, but the Vietnamese wording was produced by an LLM and a non-clinician editor, then checked by non-clinician raters who also used an LLM. Small wording changes alter clinical severity cues, as the U10 overstatement and the E03 breathing paraphrase show. A clinician reads "nói ngọng" and "nói khó", or "thở không ra hơi", differently from a lay rater. The Limitations acknowledge this in one sentence. The fix is cheap: one Vietnamese emergency or primary-care physician confirms that each of the 24 emergency and urgent pairs keeps its source acuity, with the result reported.
**Severity**: Major
**Evidence Anchor**: text: §7 Limitations "were not re-reviewed by a clinician for the Vietnamese versions"
**Confidence**: 4 (emergency triage practice)

### W6: The folk wording is confounded with Southern regional dialect
The folk versions replace standard words with forms that are lay but also typically Southern: ói for nôn, and bao tử, the term the paper labels as folk for upper abdominal pain, used where Northern speech says dạ dày. The clinical versions use the standard or Northern forms. The "folk" contrast therefore bundles three things: the folk illness label, lay register, and regional dialect. That matters for interpreting RQ1 and for the claim that folk labels are less important than expected. Suggestion: say this explicitly, report naturalness by rater region if known, or add a lay-wording-without-folk-label condition (two controls already have this) for the emergency cases.
**Severity**: Major
**Evidence Anchor**: text: Fig. 3 (fig:example) "Ông buồn nôn và nôn." versus "Ông buồn nôn, ói."
**Confidence**: 3 (familiarity with Vietnamese regional usage; I have not checked every case text)

### W7: The urgent-case outcome counts untimed "see a doctor" advice as safe
For urgent cases (TIA, upper GI bleeding, DVT, pyelonephritis, immune thrombocytopenia), any "soon" label counts as correct. But the judge's "soon" has no time frame (for example "you should get checked"). Clinically, telling someone with a TIA or a GI bleed to get checked at some point is unsafe, so urgent under-triage is probably underestimated. Likewise, the "soon" controls include 24-48-hour and one-day cases, where same-day emergency advice is often clinically acceptable, which inflates "over-triage". Suggestion: report urgent-case results with untimed "soon" counted as unsafe as a sensitivity analysis, and over-triage limited to self-care and one-week controls.
**Severity**: Minor
**Evidence Anchor**: text: §4 Measures "where both a visit within 24--48 hours and emergency care are correct"
**Confidence**: 4 (emergency-triage practice; the effect on the reported numbers is not something I can estimate)

### W8: The diacritic-restoration recommendation lacks a safety caveat
Restoring diacritics is recommended as a cheap fix. In practice, a restorer can turn an unaccented symptom word into the wrong but plausible word, silently creating a new misreading, and this risk is greatest for the rare medical terms that matter most. Over-triage also has a real cost in Vietnam's crowded referral hospitals. Suggestion: frame restoration as something to evaluate on symptom-critical terms specifically, and mention the health-system cost of the 6-8-point over-triage rise under M1/M2.
**Severity**: Minor
**Evidence Anchor**: text: §6 "Restoring diacritics before the text reaches the model is a cheap step that deserves testing"
**Confidence**: 3 (digital-health deployment; I do not judge restoration accuracy)

### Detailed Comments
**Assumption audit.** Explicit: identical facts mean identical clinical acuity. This mostly holds but was not verified by a clinician (W5). Implicit: a folk label signals benign self-diagnosis and therefore a decision not to seek care (W3). Implicit: "folk" is one register, not something regionally patterned (W6). Paradigmatic: a single-turn chatbot answer is treated as the decision point. In real families, advice is weighed together with relatives, pharmacists and traditional practitioners, which the authors partly acknowledge.

**Cross-disciplinary connections.** Medical anthropology's explanatory-models framework could reframe folk labels as the family's working diagnosis, not noise. Emergency-medicine pre-hospital delay research gives the clinical stakes. Data documentation practice (datasheets, data statements) addresses W4.

**Practical impact and stakeholders.** The finding that Vietnamese-adapted small models are not robust to how users really write is directly useful to local app builders and regulators. Stakeholders not consulted: Vietnamese clinicians (W5), lay users from different regions (W6), and traditional-medicine practitioners, whose practices are being labelled.

**Broader implications.** Avoid presenting folk speakers as the cause of the risk. The well-supported message is that models fail users who write the way most people type. Future work: multi-turn conversations in which the model can ask about red flags, real (consented, de-identified) user messages, and Vietnam-specific emergencies.

### Cross-Disciplinary Reading Recommendations
- Kleinman (1980), Patients and Healers in the Context of Culture: the explanatory-models framework for presenting folk labels without deficit framing (W3).
- Gebru et al., Datasheets for Datasets: a template for the release safeguards in W4.
- Bender and Friedman (2018), Data Statements for Natural Language Processing: documenting speaker variety and dialect, relevant to W6 and W4.
- [UNVERIFIED] Search lead: Vietnamese studies of pre-hospital delay after stroke onset and of cạo gió use among stroke patients (W3).
- [UNVERIFIED] Search lead: ethnographic work on trúng gió and wind illness in Vietnam, for sourcing the lexicon (W2).

~~~yaml suggested-references
- title: "Patients and Healers in the Context of Culture: An Exploration of the Borderland between Anthropology, Medicine, and Psychiatry"
  authors: ["Kleinman, A."]
  year: "1980"
  doi: null
  arxiv_id: null
- title: "Datasheets for Datasets"
  authors: ["Gebru, T.", "Morgenstern, J.", "Vecchione, B.", "Vaughan, J. W.", "Wallach, H.", "Daumé III, H.", "Crawford, K."]
  year: "2021"
  doi: null
  arxiv_id: "1803.09010"
- title: "Data Statements for Natural Language Processing: Toward Mitigating System Bias and Enabling Better Science"
  authors: ["Bender, E. M.", "Friedman, B."]
  year: "2018"
  doi: null
  arxiv_id: null
~~~

### Questions for Authors
1. Who wrote the lexicon's lay meanings and "can hide" mappings, and from what sources?
2. Which regional variety do the folk versions represent, and where are the raters from?
3. Would you add, or explicitly defer, Vietnam-specific emergencies (dengue warning signs, heat stroke, methanol poisoning)?
4. What documentation and use restrictions will accompany the released remedies and model answers?

### Minor Issues
- §1 names cảm nắng and say rượu as examples, but they are not in the lexicon. Align the examples with the dataset.
- Table tab:lexicon: tăng xông → "hypertension needing prompt care" is a weak "hidden emergency". Consider marking it as urgent rather than emergency.
