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
trigger: "developer recommendations that are generic rather than concrete"

### D5: writing_and_structure
score: not_assessed

### D6: venue_fit_and_contribution
score: not_assessed

## Review Body

### Reviewer Identity
I am an emergency physician and digital-health safety researcher. I have evaluated symptom checkers and I work with Southeast-Asian patient populations, including people who hold folk-illness beliefs such as trúng gió and practise coin rubbing. NLP and statistical detail are outside my competence, and I leave them to the methodology and domain seats. No review-target criteria were bound for this call, so I make no claim about alignment with any venue.

### Calibration Status
`NOT_CALIBRATED`

### Confidence Score
4. My confidence is high on the clinical, harm and ethics framing and low on the NLP and statistical choices, which I did not assess.

### Summary Assessment
For a clinical reader this is a useful and unusually candid paper. Each case is held clinically fixed while only the telling changes, and the controls make over-triage visible. Together these give clinicians and app builders a result they can act on: unaccented, lay Vietnamese moves small models toward less urgent advice, and the shift is not offset by more caution elsewhere. The finding that trúng gió for stroke did not mislead the models is counter-intuitive and clinically interesting. The mitigation results are reported honestly as not closing the gap. My concerns are about how the clinical reference standard carries over to the reworded and translated versions, and about how harm is framed. First, no clinician confirmed that each Vietnamese emergency or urgent text still meets the source urgency level. Second, the unsafe-endorsement definition treats a remedy endorsed alongside emergency advice as safe. From an ED perspective that is debatable for remedies such as fingertip pricking during a stroke, where the remedy itself delays care. Third, the secondary urgent tier accepts "soon" for conditions such as upper GI bleeding and TIA, which many emergency clinicians would not accept. The guidance to developers stays generic: test before use, consider diacritic restoration. It does not say what a deployer should do about the remaining gap or the added over-triage. The released lexicon and the remedy texts need more care against stereotyping and misuse. None of this threatens the core finding, but several points need rewriting and one needs a small clinician check.

### S1: Paired design that isolates the telling
Holding the facts fixed and varying only wording and script is the right design for a safety audit. A clinician can read any change in advice as a wording effect, not missing information.
**Evidence Anchor**: text: §1 Introduction "We hold the case and its signs fixed and change only the telling."

### S2: Over-triage controls built in
Including 28 non-urgent controls and reporting over-triage alongside under-triage follows symptom-checker audit practice. It is what lets the paper show that the advice became less urgent overall rather than merely shifted.
**Evidence Anchor**: text: §3.1 "Without controls, a model that sends everyone to the emergency room would look perfect."

### S3: Clinically interesting, non-stereotyped result on trúng gió
The paper reports that the best-known folk label did not mislead the models on stroke, and puts the risk on non-specific presentations. This avoids the easy narrative that folk speech is itself the hazard, and it matches clinical intuition that hard focal signs survive lay wording.
**Evidence Anchor**: text: §5.4 Which conditions "This held even for stroke told as \vi{trúng gió}, so the best-known folk label did not mislead the models."

### S4: Appropriately modest safety claims
The ethics statement explicitly declines to certify any model as safe. The mitigation section says plainly that prompts did not close the gap. Neither overstates what a prompt fix can do.
**Evidence Anchor**: text: Ethics Statement "No result here shows that any model is safe for medical advice."

### W1: No clinician check that the Vietnamese emergency texts still meet the source urgency level
The primary outcome assumes that each clin, folk and diacritic-free version still warrants the physician label of the English source. The checks of equivalence were done by non-clinicians, aided by an LLM. Lay renderings can move urgency for a clinician reader in either direction: "thở không ra hơi" for trouble breathing, the U10 severity overstatement, and Southern lay terms for the pain site. The flagged-pair sensitivity analysis helps but does not replace a clinical read. Suggestion: have one or two Vietnamese-speaking emergency or primary-care physicians rate the urgency of the clin and folk texts of the 24 emergency and urgent cases, blind to the source label. Then report agreement with the source label and rerun the primary analysis on the confirmed set. This is a small job. Until it is done, the Limitations wording should be echoed in the abstract.
**Severity**: Major
**Evidence Anchor**: text: §6 Limitations "Triage labels come from physicians for the English source texts and were not re-reviewed by a clinician for the Vietnamese versions."
**Confidence**: 4 (emergency triage practice; cannot judge Vietnamese lexical nuance as a native speaker would)

### W2: Unsafe-endorsement definition can understate harm
An answer that endorses coin rubbing and pricking the ten fingertips for a stroke, and also advises emergency care, is counted as safe. In practice families often do the endorsed remedy first, and minutes matter for thrombolysis, myocardial infarction and DKA. Some remedies also carry direct harm, such as bleeding from pricking in anticoagulated patients, or burns and bruising from coin rubbing. The paper reports 23% endorsement on serious cases but puts only 10% in the abstract. Suggestion: report a three-way split on serious cases with the existing labels (endorse without emergency advice, endorse with emergency advice, reject or not addressed). Classify remedies by whether they cause direct harm or only delay care, and discuss which endorsements a clinician would regard as unsafe. The moderate judge agreement on stance (κ = 0.50) makes a human-labelled check of the serious-case endorsements more important, not less.
**Severity**: Major
**Evidence Anchor**: text: §4 Measures "endorse the remedy and do not advise emergency care"
**Confidence**: 4 (ED experience with delayed presentation after home remedies; not a statistician)

### W3: Lenient secondary outcome for the urgent tier
The urgent tier includes TIA, upper GI bleeding, DVT, pyelonephritis and immune thrombocytopenia, and counts only home care or no advice as under-triage. The C/D edge-case label comes from the source. Even so, many emergency clinicians would want same-day assessment for TIA and suspected upper GI bleeding, and a "see a doctor sometime" answer is a meaningful risk there. Suggestion: also report, for the urgent tier, the share of answers labelled soon or worse versus emergency. State clearly that the secondary outcome is a lower bound on clinically concerning advice.
**Severity**: Minor
**Evidence Anchor**: text: §3.1 "The urgent cases form a secondary outcome: for them, only home care is wrong."
**Confidence**: 4 (clinical urgency conventions vary by guideline and country)

### W4: Recommendations to health-app developers are generic
The practical guidance amounts to testing on lay and unaccented input and considering diacritic restoration. A deployer reading this paper still does not know what to do about the roughly 20-point residual gap. Concrete, evidence-proportionate guidance could include:
- what acceptance threshold a test should use, for example zero under-triage on a red-flag set such as this one;
- whether to add a deterministic red-flag layer (keyword or symptom-pattern routing to "call 115") that does not rely on the LLM reading the signs;
- whether to require unconditional emergency wording in safety-netting templates, given that conditional advice was the failure mode in the folk stroke example;
- that a model failing on unaccented input should not be deployed to users who type that way.
The paper should also say plainly that none of M1, M2 or diacritic restoration has been shown to be adequate as the sole safeguard.
**Severity**: Minor
**Evidence Anchor**: text: §6 Discussion "A health app built on a small local model should be tested on unaccented, lay input before use."
**Confidence**: 4 (digital-health deployment and symptom-checker governance)

### W5: Mitigation over-triage cost is not interpreted for deployment
Over-triage rose by 6 to 8 points, pooled over soon and self-care controls. Clinically and operationally, sending a "within a week" case to the ED is different from sending a self-care case there. Vietnamese public hospitals already face severe crowding, so extra ED referrals have a real system cost and can erode user trust in the advice. Suggestion: split over-triage into soon→emergency and self-care→emergency. Then add a short discussion of what the observed trade-off would mean per 1,000 queries. The paper should note that Gemini Flash-Lite's low under-triage partly reflects a cautious operating point, which a deployer would pay for in referrals.
**Severity**: Minor
**Evidence Anchor**: table: Table 4 (tab:mit), column "over"
**Confidence**: 3 (health-system cost reasoning is outside the paper's data)

### W6: Folk-term lexicon lacks ethnographic grounding and may be read as stereotyping
The glosses are LLM-drafted and author-reviewed. The "Can hide" column pairs everyday labels with emergencies, and once released it may be read out of context as "folk term X signals disease Y". The entry pairing vong theo, a spiritual explanation, with early psychotic disorder is the most sensitive case. Used as a deployment glossary like M2, the lexicon could also lead a model to over-pathologise ordinary folk speech. Suggestion: ground the lay meanings in medical-anthropology or Vietnamese ethnomedical sources, or have them reviewed by community members or Vietnamese clinicians. Rename the column, for example "Source diagnosis in this dataset". Add a data-card note that the terms are common, mostly benign descriptions used across the population, not markers of a group.
**Severity**: Minor
**Evidence Anchor**: text: §3.4 Folk-term lexicon "drafted with an LLM and reviewed by the first author, not taken from an ethnographic source"
**Confidence**: 4 (clinical work with Vietnamese patients; not an anthropologist)

### W7: Release plan for unsafe remedies and outputs is underspecified
Flags and a content warning are good. However, the release pairs 28 undocumented, LLM-drafted remedies with real emergencies, and includes model answers that endorse them. Scraped into training corpora or indexed by search, these texts could spread unsafe advice in Vietnamese. Suggestion: state the release licence and terms of use, and consider gated or research-only access for the remedy and output files. Add a canary string to keep the data out of training sets. In each released unsafe answer, place the content warning next to the text itself, not only in the data card.
**Severity**: Minor
**Evidence Anchor**: text: Ethics Statement "The release is meant for evaluation only"
**Confidence**: 3 (dataset-release practice; not a legal specialist)

### W8: Vietnamese care-seeking context is missing from the harm framing
The advice categories assume a US-style pathway. In Vietnam, many people go to pharmacies first, buy medicines without a prescription, use private clinics and traditional practitioners, and access to the 115 ambulance service varies. These shape how a "soon" or "self-care" answer turns into delay. Briefly placing the results in that pathway would make the harm argument more convincing to health-system and public-health readers. Suggestion: one paragraph in the Discussion, with sources on care-seeking in Vietnam.
**Severity**: Minor
**Evidence Anchor**: absence: Introduction and Discussion — expected description of Vietnamese care-seeking pathways (pharmacy-first self-medication, 115 access, traditional practitioners) where the advice would be acted on; checked Introduction, Discussion, Limitations, Ethics Statement
**Confidence**: 3 (regional clinical experience; no cited source checked in this session)

### Cross-Disciplinary Reading Recommendations
- Kleinman, Patients and Healers in the Context of Culture (1980). This gives the explanatory-models framework, which could frame folk labels as patients' explanatory models rather than errors, and supports W6.
- Gebru et al., Datasheets for Datasets (Communications of the ACM, 2021). This is a structure for the data card covering the intended uses, misuse risks and content warnings raised in W7.
- Wallace et al., systematic review of the diagnostic and triage accuracy of digital symptom checkers (npj Digital Medicine, 2022). This is context for acceptable under- and over-triage benchmarks in W4 and W5.
- [UNVERIFIED] Search lead: studies of cạo gió (coin rubbing) and other Vietnamese folk practices and their association with delayed presentation for acute illness, for W2 and W8.
- [UNVERIFIED] Search lead: studies of pharmacy-first self-medication and care-seeking behaviour in Vietnam, for W8.

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
- title: "The diagnostic and triage accuracy of digital and online symptom checker tools: a systematic review"
  authors: ["Wallace, W."]
  year: "2022"
  doi: null
  arxiv_id: null
~~~

### Questions for Authors
1. Would a Vietnamese-speaking physician rate the folk and diacritic-free emergency texts as emergencies? Is a blind clinician check of the 24 serious cases feasible before camera-ready?
2. How many serious-case answers endorse the remedy while also advising emergency care, and for which remedies would you, or a clinician, consider that unsafe?
3. Which concrete steps would you recommend to a Vietnamese health-app team today, beyond testing on lay and unaccented input?
4. Under what licence and access conditions will the remedy texts and unsafe answers be released?

### Minor Issues
- The abstract could state that labels were not re-checked by a clinician for the Vietnamese versions, as the Limitations section does.
- The 115 number in M1 and in the judge prompt is right for Vietnam. Mentioning that ambulance access varies would help non-Vietnamese readers.
