contract_role: eic

## Dimension Scores

### D1: methodology_rigor
score: not_assessed

### D2: domain_accuracy
score: not_assessed

### D3: argumentative_coherence
score: not_assessed

### D4: cross_disciplinary_relevance
score: not_assessed

### D5: writing_and_structure
score: warn
trigger: "Figures that largely repeat table content"

### D6: venue_fit_and_contribution
score: warn
trigger: "the safety message is spread across several competing claims"

## Review Body

### Reviewer Identity
Program-committee area chair of a Q3-level AI-in-healthcare conference (LNCS proceedings) who has handled many submissions on LLMs giving health advice to patients, most of them in English. I focus on fit for the readership, on presentation, and on whether the clinical-safety framing matches the evidence. My blind spots are statistics and Vietnamese-language details, which other seats cover.

### Preliminary Signal
Major Revision, driven by presentation. The scientific core suits the venue and is new. The changes I ask for are about length, framing and figure economy, not new experiments. This is one input for the editorial synthesizer and is not a decision.

### Confidence Score
4. This is within my area for venue fit and presentation. I did not judge the statistical inference or the accuracy of the Vietnamese.

### Calibration Status
`NOT_CALIBRATED`

### Criterion-Bound Judgements
| Dimension / criterion | Criterion source | Judgement | Evidence anchors | Rationale | Uncertainty or scope limit | Decision bearing? |
|---|---|---|---|---|---|---|
| D5 writing_and_structure | contract D5 + Phase 1 scoring plan | PARTLY_MEETS | see W1, W3, W4, W5, S4 | Clear prose and well-chosen illustrative examples, but the main text runs past a typical 12–16 page limit, and several figures repeat tables or other figures | No specific venue named; I assumed a typical LNCS page limit | yes: the page overrun alone would stop camera-ready |
| D6 venue_fit_and_contribution | contract D6 + Phase 1 scoring plan | PARTLY_MEETS | see W2, W6, W7, W8, S1, S2, S3, S5 | Relevant and new for an AI-in-health audience, with proportionate disclaimers, but the title and part of the framing put forward folk labels while the main finding concerns diacritic loss | Novelty judged against the related work the paper cites; no literature search done | yes: reframing is needed so readers leave with one message |

### Summary Assessment
The paper tests whether nine LLMs give less urgent advice when the same 52 physician-labelled vignettes are retold in Vietnamese folk wording and/or without diacritics, whether they endorse folk remedies, and whether system-prompt changes help. For an AI-in-healthcare audience the question is timely and clearly safety-relevant. Its design (paired versions, control cases for over-triage, a validated judge) is easy to follow. The results are more interesting than the title suggests. The famous folk label for stroke did not mislead the models. Most of the harm comes from missing diacritics, especially in small open models and in models adapted to Vietnamese. Prompt mitigations narrow the gap but do not close it. The limitations and ethics statement are unusually candid about the lack of clinician review of the Vietnamese versions, and the claims in the body are mostly scaled to that. My concerns are about the paper as a proceedings paper. The main text ends on page 18, so it is too long. Three schematic method figures overlap, and two result figures repeat tables. The title, abstract and contribution list give the reader several parallel messages instead of one: "diacritic loss is the main risk; check unaccented, lay input before you deploy." All of this can be fixed without new data.

### Strengths

### S1: Timely, new contribution with a clear gap
The paper extends work on how patient wording affects LLM triage, which so far has been in English, to a non-English setting with two perturbations (folk labels, diacritic loss) that English studies cannot capture. This is directly relevant to a mixed clinical/informatics/ML readership.
**Evidence Anchor**: text: §1 Introduction "To our knowledge this is the first test of LLM triage on folk-worded and unaccented Vietnamese."

### S2: Under- and over-triage reported together
Including non-urgent controls lets clinicians see that the advice becomes less urgent overall rather than that models trade one error for another. This is the safety-relevant reading a clinical audience needs.
**Evidence Anchor**: text: §3.1 Cases and labels "Without controls, a model that sends everyone to the emergency room would look perfect."

### S3: Safety framing in the body is mostly proportionate
The limitations and ethics sections state that the Vietnamese versions were not reviewed by a clinician, that the remedy-stance results are indicative only, and that nothing here certifies a model as safe. The remedy results are explicitly treated as secondary.
**Evidence Anchor**: text: §9 Ethics Statement "No result here shows that any model is safe for medical advice."

### S4: Concrete worked examples help non-Vietnamese readers
The stroke case shown in four versions, with excerpts from one model's answers, makes the effect concrete for readers who cannot read Vietnamese. This is figure use that adds information.
**Evidence Anchor**: figure: Fig. 3 — stroke case E08 in clin, folk, folk_nd, folk_rem with excerpts from the Qwen2.5-1.5B answers

### S5: Useful negative result for builders
The mitigation table shows that a one-line safety instruction or a glossary lowers under-triage but leaves the unaccented, folk-worded version well above the clinical one. App builders should hear that "add a safety line to the prompt" is not enough.
**Evidence Anchor**: table: Table 3 — gap column, folk_nd remains above clin under m1 and m2 for three of four models

### S6: Release of reusable evaluation material
The paired cases, the folk-term lexicon and all model outputs are released for evaluation use, each remedy flagged as documented or not. This gives later work a baseline.
**Evidence Anchor**: dataset: released case set, lexicon and labelled model outputs — release and evaluation-only flagging described in §9 Ethics Statement

### Weaknesses

### W1: Main text exceeds a typical proceedings page limit
In the compiled PDF the Conclusion ends and the References begin on page 18, the references run to about page 20, and the appendices fill pages 20–22. A typical LNCS AI-in-health conference allows 12–16 pages, usually including references. A paper this long risks a desk rejection on format before anyone reads it. There is a clear path to trimming (see W3, W4): merge the overlapping schematics, drop figures that repeat tables, shorten the meaning-check paragraph in §3.3, and move the per-condition analysis (Fig. 10) and the robustness details to the appendix or supplementary material.
**Severity**: Major
**Evidence Anchor**: text: §8 Conclusion, last sentence, p. 18 of manuscript.pdf "We release the cases, the lexicon, all answers and labels."
**Confidence**: 4 — page count read directly from the typeset PDF; the exact limit depends on the venue chosen

### W2: Title and headline framing do not match the main finding
The title sets up "trúng gió or stroke?" as the central question. The paper's own results show that this label did not mislead the models, and that diacritic loss, not folk labels, causes most of the harm. A reader who skims the title and first paragraph of the introduction will leave with the opposite message from the one in the results. The abstract does state that diacritics dominate, but only after leading with the folk-label narrative. I suggest retitling to foreground diacritic loss (for example, unaccented and lay Vietnamese input). Then reorder the abstract and contribution list so the diacritic result comes first and the folk-label result is presented as smaller and condition-dependent.
**Severity**: Major
**Evidence Anchor**: text: §5.4 Which conditions "so the best-known folk label did not mislead the models"
**Confidence**: 4 — framing and title–finding match is my core remit

### W3: Result figures repeat tables
Fig. 6 plots the same per-model, per-version under-triage values given in Table 2. Fig. 11 plots the four-model means of the rows in Table 3. Fig. 8a repeats the four headline percentages already in the abstract, Results and Conclusion. In a page-limited proceedings paper each repeat costs space without adding information. I suggest keeping one of each pair: for example, Fig. 6 in the main text with Table 2 in the appendix, and Table 3 alone, with its mean row added.
**Severity**: Minor
**Evidence Anchor**: figure: Fig. 11 — panels (a) and (b) give the means of Table 3's clin, folk_nd and over columns
**Confidence**: 4 — compared the figure images with the tables directly

### W4: Three overlapping schematic method figures
Fig. 1 (study overview) already shows the sources, the 52 cases with their groups, the five versions, the 260 prompts, the judge and the human check. Fig. 4 (dataset construction) and Fig. 5 (answer to measure) repeat most of this, and Fig. 2 repeats the version derivation. One overview plus the worked version example (Fig. 2) would be enough for this readership.
**Severity**: Minor
**Evidence Anchor**: figure: Fig. 4 — source counts, case groups, 260 prompts and 2,340 answers, all already shown in Fig. 1
**Confidence**: 4 — compared figures directly

### W5: Abstract is long and number-dense
The abstract runs to about 290 words and carries more than fifteen numeric results, including CIs and kappas. LNCS asks for 150–250 words, and clinical readers will struggle to pick out the main message. Keep the three or four numbers that carry the message (baseline, diacritic effect, combined effect, mitigation gap) and move the rest to the body.
**Severity**: Minor
**Evidence Anchor**: text: Abstract, opening "Vietnamese speakers often describe symptoms with folk-illness labels"
**Confidence**: 4 — word count of the abstract source

### W6: Introduction overstates what the folk contrast can isolate
The introduction says that any change in the advice is caused by the wording and not by missing information. The paper then explains that the folk versions bundle the label with lay register and Southern vocabulary, and that there is no neutral clinical-paraphrase control. For clinicians this can read as a stronger causal claim about folk labels than the design supports. Change the sentence to "by the change in telling (register, vocabulary and folk label together)". The methodology seat is better placed to judge the design point itself.
**Severity**: Minor
**Evidence Anchor**: text: §1 Introduction "Any change in the advice is then caused by the wording, not by missing information."
**Confidence**: 3 — framing judgement; I defer to the methodology seat on the design

### W7: Builder takeaway is scattered and its most actionable step is untested
The advice an app builder would act on is spread across §6 (test small local models on unaccented input; diacritic restoration "deserves testing") and the last lines of the Conclusion. No single paragraph tells a health-app builder what to do. The most concrete remedy, restoring diacritics before inference, is suggested but not evaluated. A short "Implications for deployment" paragraph would give readers one actionable takeaway: evaluate on lay, unaccented input; do not rely on prompt-level fixes; consider diacritic restoration with its own safety check. Even a small pilot of restoration on the existing prompts would strengthen it, but that is optional.
**Severity**: Minor
**Evidence Anchor**: text: §6 Discussion "Restoring diacritics before the text reaches the model is a cheap step that deserves testing"
**Confidence**: 4 — readership-level judgement within my remit

### W8: Abstract omits the main clinical-validity caveat
The abstract calls the vignettes "physician-labelled" but does not say that the Vietnamese versions, folk rewrites and remedies were drafted with an LLM and not re-reviewed by a clinician. The body states this candidly. A clinician who reads only the abstract may assume the Vietnamese cases were clinically validated. One clause in the abstract would bring it in line with the body's framing.
**Severity**: Minor
**Evidence Anchor**: absence: Abstract — expected a clause that the Vietnamese versions were LLM-drafted and not re-reviewed by a clinician; checked Abstract, §1 contribution list, §3.2 Authorship paragraph, §7 Limitations
**Confidence**: 4 — clinical-safety framing is within my remit

### Detailed Comments

#### Journal Fit
This fits an AI-in-healthcare venue well: patient-facing LLM advice, triage safety, a low-resource language, and a builder-relevant question about model scale. The models are small open ones plus two commercial API models, which matches what a local health app could deploy, as the paper argues in §4.

#### Originality
The new elements are the language setting and the two perturbations specific to it. The method itself (vignette audit, perturbation, LLM judge) is established. That is acceptable for this venue, provided the framing makes the Vietnamese-specific findings (diacritics; models adapted to Vietnamese not being more robust) the centre.

#### Significance
The finding that diacritic loss roughly doubles under-triage in small and Vietnamese-adapted models, and that prompt fixes leave a gap of about 20 points, is the result practitioners will remember. The remedy-endorsement finding is secondary because judge agreement on that label was moderate, and the paper treats it that way.

#### Structural Coherence
The body is coherent from RQs to results to discussion. The coherence problem is at the edges: the title, and the folk-first ordering of the abstract and contributions, against a conclusion that says folk labels were not the main problem (W2).

#### Title & Abstract
See W2, W5, W8.

#### Conclusion
The Conclusion answers the RQs and states the deployment lesson in one sentence. It would serve this readership better if that sentence were expanded into the consolidated implications suggested in W7.

### Questions for Authors
1. Which venue and page limit are you targeting? Do the 12–16 pages include references?
2. Would you consider retitling around unaccented/lay input, given your own finding that the "trúng gió" label did not mislead the models?
3. Is a small diacritic-restoration pilot on the existing 260 prompts feasible? It would turn the Discussion's suggestion into an actionable result.

### Minor Issues
- §3.3 Meaning check is long for the main text; the agreement statistics could move to an appendix with one summary sentence left in place.
- The Table 1 caption gives run dates; check that this matches the venue's anonymity rules.
- Fig. 10 (per-condition, one case per condition) is labelled exploratory. It is a candidate to move to the appendix to save space.
