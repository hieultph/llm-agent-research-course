contract_role: da
## Dimension Scores

### D1: methodology_rigor
score: not_assessed

### D2: domain_accuracy
score: not_assessed

### D3: argumentative_coherence
score: warn
trigger: "a credible alternative explanation is left unaddressed"

### D4: cross_disciplinary_relevance
score: not_assessed

### D5: writing_and_structure
score: not_assessed

### D6: venue_fit_and_contribution
score: not_assessed

## Review Body

### Calibration Status

`NOT_CALIBRATED`. No review-target criteria binding was supplied, so this card makes no venue-alignment claim and emits no criterion-bound judgement table.

### What the paper does well

The design holds the case facts fixed and varies only the telling, which makes it a controlled perturbation study rather than a correlational audit. It reports under-triage and over-triage together, so a model cannot look safe just by sending everyone to emergency care. The authors also report results that cut against their framing: the best-known folk label did not mislead the models, the folk effect shrinks to 3 points once diacritics are gone, and no single-model contrast survives Holm correction. They also re-ran the pooled analysis without the flagged meaning-check pairs. The diacritic-loss result (+25 points, CI [13, 37]) is large, consistent across most models, and survives that sensitivity check on emergencies.

### Strongest Counter-Argument

A sceptic would say the paper shows that small open models are brittle to any change in input, and that "folk-illness phrasing" plays no special part in it. Under greedy decoding, small models flip labels after minor rewording. When about 78% of emergency answers start out correctly labelled emergency, random instability alone pushes under-triage up, because many more answers can flip from emergency to non-emergency than the other way. Run the same models on a neutral clinical paraphrase with no lay vocabulary and no folk label, and you might see a rise of several points too. Without that control, the +11-point folk effect cannot be attributed to folk labels, or even to lay register. The paper's own sampling check hints at this. Qwen2.5-7B shows no folk_nd effect under greedy decoding (36 vs 36) but a 14-point effect under sampling (43 vs 29), so single-condition greedy estimates move by amounts as large as the folk effect itself. The per-model folk deltas range from -14 to +43, and two models go the wrong way. The effect is carried by Qwen2.5-1.5B, SeaLLMs and Llama, while both commercial models stay at or near zero. So the defensible thesis is narrower than the title: diacritic-stripped Vietnamese degrades triage advice in models of 8B parameters or fewer. The paper's own conclusion concedes that folk labels are not the main problem, yet the title leads with a folk label (trúng gió) that, by the paper's own analysis, did not mislead the models. Finally, the remedy headline ("up to half") rests on a judge whose remedy-stance agreement with humans is κ=0.50 on 32 answers. The paper calls these figures secondary in Results but promotes them in the contributions.

### Challenge commentary

Logic chain, folk effect. The introduction claims causal attribution from the paired design ("Any change in the advice is then caused by the wording"). That licenses "this particular rewrite changed the advice". It does not license "folk-illness phrasing caused it". The folk version bundles at least three changes: lay vocabulary, an added folk label, and slightly longer text (46.4 vs 50.0 words). Two control cases have lay wording with no label at all. No contrast separates the label from the register, and the paper says there are too few repeated terms for a per-term analysis. The title and abstract still name folk-illness phrasing as a cause.

Logic chain, diacritic mechanism. The conclusion that models "misread the signs" in unaccented text, and that a system prompt "cannot fix this", rests on two qualitative examples. No systematic check, such as whether answers restate the key signs, backs it. The mitigation table also does not cleanly support "cannot fix". The mean gap between folk_nd and clin for the four mitigation models is about 20 points both at baseline and under M1/M2, so the prompts reduced under-triage roughly evenly across versions. That fits a uniform caution shift as well as it fits misreading. The mechanism remains a plausible hypothesis, not a finding.

Internal tension on information content. The introduction says diacritic removal "removes much of the lexical information", and yet it also says advice changes are "not by missing information". For the _nd versions, information really is missing: stripped Vietnamese is lexically ambiguous. The diacritic result is therefore partly a test of disambiguation under information loss, not a pure wording effect. That is still a valid and practically important finding, but it should be framed that way.

Minor points, which do not change the decision. (a) The Discussion says the Vietnamese effect is "larger" than in English work "because the change hides the signs". This compares across studies with different models and metrics, and it contradicts the design premise that folk texts never drop or soften a fact. (b) The judge is Gemini 3.5 Flash, and the two Gemini models are the paper's robust exemplars. The paper reports a pooled κ but no per-model judge-human agreement, so self-family leniency cannot be ruled out for the "barely affected" claim. (c) The stroke case E08, which illustrates trúng gió, is one of the flagged meaning-check pairs. (d) The claim that "language adaptation did not make these models more robust" has a matched base only for Arcee-VyLinh (Qwen2.5-3B). SeaLLMs-v3 is Qwen2-based, and Qwen2 was not tested. (e) Gemini over-triages 33-39% of controls under every prompt, so its near-zero under-triage partly reflects a cautious operating point. The "barely affected" framing should say so.

Ignored alternative explanations: generic paraphrase instability (no neutral-paraphrase control); register shift versus folk label (bundled); a uniform caution shift rather than sign-misreading under the mitigations; and same-family judge leniency.

Missing stakeholder perspective (named only): clinicians, who never reviewed the Vietnamese versions or the remedy-danger framing.

Unexamined premise: the paper assumes that automatic Unicode diacritic stripping represents how Vietnamese users "actually type". Real unaccented input also includes Telex/VNI remnants, abbreviations and partial accents. Nothing in the paper establishes that the synthetic _nd condition is ecologically valid.

#### CRITICAL
| # | Dimension | Issue Description | Evidence Anchor | Confidence | Field-Norm Boundary | Evidence-Crossing Rationale |
|---|-----------|-------------------|-----------------|------------|---------------------|-----------------------------|

#### MAJOR
| # | Dimension | Issue Description | Evidence Anchor | Confidence | Field-Norm Boundary | Evidence-Crossing Rationale |
|---|-----------|-------------------|-----------------|------------|---------------------|-----------------------------|
| M1 | D3 | The folk effect (+11) is attributed to the wording, but a credible alternative is not ruled out: generic paraphrase instability of small greedy-decoded models, which mechanically raises under-triage when most baselines are correct. The paper's own sampling check moves Qwen2.5-7B by 14 points between decoding modes. A neutral clinical-paraphrase control, or a matching rewording of the claim, is needed. | text: §1 "Any change in the advice is then caused by the wording, not by missing information."; §5.6 "43\% vs 29\% for Qwen2.5-7B" | 4 (logic from reported numbers; no access to raw outputs) | n/a: severity rests on the paper's internal logic, not a field norm | n/a |
| M2 | D3 | The title and abstract attribute the effect to folk-illness phrasing, but the folk condition bundles lay vocabulary with the folk label, so the label's contribution is not identified. The paper's own conclusion says folk labels are not the main problem, and the title leads with trúng gió, which did not mislead the models. The headline framing contradicts the reported result. | text: §3.2 "The same facts in everyday wording (\vi{ói} for vomiting, \vi{tào tháo đuổi} for diarrhoea), plus the folk label a family would use"; §9 "The main problem was not folk labels such as \vi{trúng gió}." | 5 (direct textual comparison) | n/a: internal consistency | n/a |
| M3 | D3 | The claim "Lead LLMs to Under-Triage" overgeneralises. Both commercial models stay at 0-7% under-triage on every version. The effect sits in models of 8B or fewer, so the mean over models depends on which models were chosen and is not a property of LLMs in general. The scope should be stated in the title, abstract and contributions. | table: Table~\ref{tab:main}, gemini-3.5-flash and gemini-3.5-flash-lite rows versus the Mean over models row | 4 (read from the reported table) | n/a: scope of inference from the paper's own sample | n/a |
| M4 | D3 | The contributions state as a headline that some models endorse "dangerous" remedies in up to half of emergencies. This rests on a remedy judge with κ=0.50 on 32 answers, which Results itself calls secondary. "Dangerous" is not established either: only 24/52 remedies are documented, and documentation shows that a practice exists, not that it causes harm. Hedging is inconsistent between sections. | text: §1 "Some models endorse dangerous folk remedies in up to half of emergencies."; §5.3 "so we treat these figures as secondary" | 4 (direct textual comparison plus reported κ) | n/a: internal consistency | n/a |
| M5 | D3 | The mechanism claim, that models misread the signs and that prompting cannot fix this, is stated in the Discussion and Conclusion as the main explanation. It rests on two anecdotes. The mitigation data (a stable ~20-point gap while all versions improve) fit a uniform caution shift just as well. It needs a systematic analysis, such as whether answers restate key signs per version, or a downgrade to a hypothesis. | text: §6 "The emergency is lost before any triage reasoning starts. A system prompt that asks for more caution cannot fix this"; §9 "models misread the signs in unaccented text" | 4 (logic from reported tables and examples) | n/a: inference from the paper's own evidence | n/a |

