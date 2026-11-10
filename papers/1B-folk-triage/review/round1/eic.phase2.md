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
trigger: "Localised clarity problems"

### D6: venue_fit_and_contribution
score: warn
trigger: "The contribution is genuine but incremental or under-positioned against prior work"

## Review Body

### Reviewer Identity and Focus
I am a senior program-committee member for an applied NLP / AI-for-health track at an Asian LNCS conference, with experience of LLM-evaluation papers on low-resource languages. My focus is on novelty and significance relative to English-language prior work, whether the title and abstract match the findings, and length and presentation for LNCS. I do not go deep into statistics or data construction. Those belong to other seats.

### Overall Recommendation (seat signal for the synthesizer only)
Major Revision. The study fits the track well and is carefully reported. My concerns are about framing: the title and introduction lead with an effect that the authors' own results present as secondary, and the strongest result (diacritic loss) is not positioned against the work it most directly extends. Most of this can be fixed by rewriting rather than new experiments.

Confidence: 4 (high: venue fit, positioning and presentation are my core remit. I did not audit the statistics or the clinical content).

Calibration Status: `NOT_CALIBRATED`

### Summary Assessment
The paper translates 52 physician-labelled English triage vignettes into Vietnamese, writes each one in clinical and folk-illness wording, with and without diacritics, and adds a folk-remedy version. It then measures how nine LLMs change their urgency advice. The design keeps the facts fixed across versions and includes non-urgent controls. Because of this, the main contrasts are interpretable and the "less urgent overall" conclusion is credible. For an Asian applied-NLP / AI-for-health audience, the topic is timely and well within scope. Vietnamese consumer health use is real, and the released paired set and folk-term lexicon are useful resources.

The main problem for journal fit is that the paper sells a different story from the one its results tell. The title opens with "Trúng gió or Stroke?" and puts folk phrasing first. The results and conclusion, however, report that the trúng gió label did not mislead models on stroke, that folk wording adds only 3 points once diacritics are gone, and that diacritic loss drives most of the harm. Diacritic loss is a script-level perturbation. It is closely related to the typo and style perturbations already studied in English, so the paper should be positioned as an extension of that line of work, specific to Vietnamese. The averaged effects also depend on a model roster that is mostly 1.5–8B open models plus two Gemini variants that were barely affected, and the generalised wording "Lead LLMs" needs scoping. Presentation is otherwise good. The abstract is within LNCS norms (about 247 words), and the figures and tables are clear.

### S1: Paired design isolates wording from content
Holding the case and its signs fixed while varying only the telling gives the paper a clean causal reading that most robustness audits lack. This is the paper's main methodological selling point for the venue.
**Evidence Anchor**: text: §1 "We hold the case and its signs fixed and change only the telling."

### S2: Controls guard against a trivially cautious model
Including soon and self-care controls, and reporting over-triage alongside under-triage, makes the "less urgent across the board" conclusion meaningful. Without them it would be an artefact of caution.
**Evidence Anchor**: text: §3.1 "Without controls, a model that sends everyone to the emergency room would look perfect."

### S3: Licensed public sources and a released resource
The cases come from public, physician-labelled sets under MIT and CC0 licences, and the authors release the paired cases, the lexicon and all outputs. For a low-resource-language track, this resource value is a contribution in itself.
**Evidence Anchor**: dataset: Levine et al. (MIT) and Ramaswamy et al. (CC0) vignettes — licence and release of the 260 paired prompts, 34-term lexicon and model outputs (§3.1, Abstract)

### S4: Candid reporting of per-model imprecision and null results
The paper states plainly that no single-model contrast survives correction and that the best-known folk label did not mislead models. Reviewers at this venue will appreciate this candour, and it should be kept.
**Evidence Anchor**: text: §5.1 "With 14 cases per model, no single-model contrast survives Holm correction"

### S5: Clearly identified gap for the Vietnamese setting
The gap claim is specific and plausible: existing Vietnamese medical benchmarks test knowledge with multiple-choice questions, not how the way a layperson tells the story affects the advice.
**Evidence Anchor**: text: §2 "We are not aware of work that measures lay phrasing, folk-illness terms or missing diacritics in Vietnamese health questions."

### W1: Title and introduction foreground the effect the results downplay
**Problem**: The title opens with "Trúng gió or Stroke?" and names folk phrasing first. The introduction motivates the study with the trúng gió stroke scenario. The results and conclusion, however, say the trúng gió label did not mislead models on stroke, that the folk effect is modest (+11) and almost disappears once diacritics are removed (folk_nd only 3 points above clin_nd), and that diacritic loss is the main driver.
**Evidence Anchor**: text: §8 Conclusion "The main problem was not folk labels such as"
**Why it matters**: Readers who skim the title will take away the opposite of the paper's own main finding. PC members will read this as over-promising on the folk-illness angle.
**Suggestion**: Retitle so that diacritic loss leads and folk wording is the secondary factor (or pose the stroke question with its answer). Reorder the introduction and contribution list to match, and state the non-additivity result in the abstract.
**Severity**: Major
**Confidence**: 5 — core remit: title/abstract/conclusion consistency

### W2: The dominant finding is not positioned against diacritic-restoration and perturbation work
**Problem**: The novelty argument rests on folk labels "differing in kind" from typo-style perturbations. Yet the largest effect comes from diacritic removal, which is a surface perturbation. The related-work section cites one general diacritics paper and no work on Vietnamese diacritic restoration. The discussion recommends restoring diacritics as "a cheap step that deserves testing" but neither cites existing restoration systems nor tries one.
**Evidence Anchor**: absence: §2 Related Work and §6 Discussion — expected positioning against Vietnamese diacritic-restoration work and an explicit contrast with English typo/style perturbation magnitudes; checked §2, §6, §7 Limitations and every \cite key in the manuscript
**Why it matters**: Against English prior work (Gourabathina et al.), a reviewer can argue that the main result is "another surface perturbation, larger in Vietnamese". The paper needs to state clearly what is new beyond the larger size of the effect.
**Suggestion**: Add a related-work paragraph on Vietnamese diacritic restoration and unaccented-input robustness. State explicitly how the effect size compares with English perturbation shifts. If feasible, run one off-the-shelf restoration step on the _nd versions for one or two models. This would turn the recommendation into a finding.
**Severity**: Major
**Confidence**: 4 — core remit: novelty positioning; I am not certain how much the restoration literature covers health text

### W3: "LLMs" in the title generalises from a narrow, small-model-heavy roster
**Problem**: Seven of the nine models are open 1.5B–8B models. The only commercial models are two Gemini 3.5 variants, and one of them is also the judge. The Gemini models under-triage at most 1 of 14 emergencies in any version. The mean effects (+11, +25, +29) therefore mostly reflect small open models, and they would change with a different roster.
**Evidence Anchor**: table: Table 3 (tab:main) — gemini-3.5-flash and flash-lite rows at 0–7% in every version vs Qwen2.5-1.5B at 43/93/86/93%
**Why it matters**: For an AI-for-health readership, the practical question is whether deployed assistants are at risk. As written, the headline claim covers all LLMs, but the data show the risk is concentrated in small local models.
**Suggestion**: Scope the title, abstract and contribution 2 to the models tested (for example, "small open LLMs"). Report the mean separately for open and API models. Alternatively, add at least one larger open model or one non-Gemini commercial model.
**Severity**: Major
**Confidence**: 4 — core remit: significance and generalisation of headline claims

### W4: Contribution list overstates the remedy result
**Problem**: The contribution list says "some models" endorse dangerous remedies in up to half of emergencies. The results show only SeaLLMs at 50% on emergencies (Qwen2.5-1.5B reaches 60% on urgent cases), and the authors themselves treat the remedy figures as secondary because κ is 0.50.
**Evidence Anchor**: text: §1 contribution 2 "Some models endorse dangerous folk remedies in up to half of emergencies."
**Why it matters**: The wording is inconsistent with the abstract ("one model") and with the authors' own caveat.
**Suggestion**: Align the wording with the abstract and add the moderate-agreement caveat.
**Severity**: Minor
**Confidence**: 5 — direct text comparison

### W5: Per-condition analysis is claimed as a contribution but reported thinly
**Problem**: Contribution 3 lists a per-condition analysis, but §5.4 reports only three bullet points and one sentence, with no table or figure.
**Evidence Anchor**: text: §1 contribution 3 "A per-condition analysis and a mitigation study."
**Why it matters**: A claimed contribution with little visible support weakens the contribution list.
**Suggestion**: Either add a compact per-condition table (in the appendix if space is short) or drop it from the contribution list.
**Severity**: Minor
**Confidence**: 4 — presentation judgement

### W6: Meaning-check subsection is a single dense paragraph
**Problem**: §3.3 packs revision history, two agreement statistics, rater asymmetry and pair-by-pair adjudication into one paragraph of about 270 words.
**Evidence Anchor**: text: §3.3 "so the raters differed in strictness and rarely agreed on which pairs to flag"
**Why it matters**: The validity of the folk/clinical equivalence is central, and this paragraph is hard to follow on a first read.
**Suggestion**: Split it into procedure / agreement / adjudication, or move the pair-level adjudication into the appendix and keep only a one-sentence summary in the main text.
**Severity**: Minor
**Confidence**: 4 — presentation judgement

### Criterion-Bound Judgements
| Dimension / criterion | Criterion source | Judgement | Evidence anchors | Rationale | Uncertainty or scope limit | Decision bearing? |
|---|---|---|---|---|---|---|
| D5 writing_and_structure | contract D5; config focus (2), (3) | PARTLY_MEETS | W1, W5, W6 anchors | Clear prose, tables and figures; abstract within norms; title and contribution framing misaligned with the findings | Page count not verified from the compiled PDF | yes — warn |
| D6 venue_fit_and_contribution | contract D6; config focus (1) | PARTLY_MEETS | S3, S5, W2, W3 anchors | In scope, with a useful resource; novelty over English perturbation work is under-argued and generality is overstated | Did not survey the restoration literature myself | yes — warn |
| Venue length (LNCS) | config focus (3) | NOT_ASSESSED | — | 7,436 words plus a two-page lexicon appendix; compliance depends on the track's page limit | Compiled PDF not provided to this seat | no |

### Detailed Comments
- Journal fit: Squarely within an applied NLP / AI-for-health track at an Asian venue. The low-resource language, consumer-safety framing and released resource match the readership.
- Originality: The Vietnamese folk-label and remedy conditions are new. The diacritic result is the strongest but the least novel conceptually (W2).
- Significance: The practical message is valuable: small or locally adapted models fail on unaccented lay input, and a cautionary prompt does not close the gap. It should be scoped to the models tested (W3).
- Structural coherence: The research questions, results and conclusion are consistent with each other. The mismatch is between the title/introduction and everything else (W1).
- Conclusion: It states the real finding correctly, and the title should be brought into line with it.

### Questions for Authors
1. What is the compiled page count excluding references, and what page limit applies to the target track? If over the limit, could the lexicon table move to supplementary material?
2. Would a simple Vietnamese diacritic-restoration step applied to the _nd versions recover most of the lost emergency advice?
3. Why were no larger open models (for example, 30B+) included, given that the effect seems to shrink with model quality?
