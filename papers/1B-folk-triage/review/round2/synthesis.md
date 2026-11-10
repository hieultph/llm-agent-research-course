# Editorial Decision Package

## Calibration Resolution

`calibration_status: NOT_CALIBRATED`

Current runtime boundary: this package is not upgraded from a candidate or prose-named profile. `PROFILE_MEASURED` remains unavailable until a closed profile artifact and replay validator bind the exact target fields to the completed panel's `execution_topology_sha256`. Every seat card also self-reports `NOT_CALIBRATED`.

## Manuscript Information

- **Title**: "Trúng gió" or Stroke? Testing LLM Triage on Folk-Worded and Unaccented Vietnamese Health Questions
- **Manuscript ID**: not assigned (pre-submission check)
- **Submission Date**: not applicable (pre-submission)
- **Decision Date**: 2026-11-10
- **Review Round**: Round 2, run as a fresh full review (`reviewer/reviewer_full/v2`, panel `1b-review-round-2`). No earlier round was read by the synthesizer.
- **Target venue**: the author named a Q3 AI-in-healthcare conference (LNCS) without a specific venue.
- **Review-target binding**: `criteria_binding_unavailable`. All five Phase 1 cards disclose `criteria_binding_unavailable`, so this is an explicitly unbound run. No venue-alignment claim is made in this package beyond what the EIC (Journal-Fit Reviewer) card itself states, and the EIC card's page-limit and abstract-length judgements rest on an assumed typical LNCS limit (EIC:W1, EIC:W5), not on a bound venue rule.
- **Cross-model decision check (Step 4b)**: not active for this run; skipped, no `[CROSS-MODEL-CHECKPOINT]` line is recorded.

## Review Panel Provenance (#540/#740)

- **Typed artifact**: `papers/1B-folk-triage/review/round2/provenance.json` (`schema_version: review-panel-provenance/1.0`, validated by the dispatching layer)
- **Artifact SHA-256 (raw bytes)**: `dfab7699c8c87e4758bfed1d1ac285fd12584343ff4d3394425ec21270179e51`
- **Contract SHA-256 (as recorded in the artifact)**: `e9712090d2469fea15a37b8e22d4e137afbcb2bf38d5789939c5df56738ef7af`
- **Panel ID**: `1b-review-round-2`
- **Normalized manifest SHA-256**: `dc1781432462144e3f3aa2e1428ae39b4f35e8b2f4ced8e3f58d33684cc481d3`
- **Execution topology SHA-256**: `ba4de2cf08761c7f478a4d22252e1c234f07e2b96cfc887197ff296a1c11b059`
- **Fresh-context scope**: `within_panel_attempt_only` (this does not compare retries or prior rounds, and says nothing about whether this round's contexts were new relative to round 1)

| Seat | Role ID | Actor type | Context ID | Peer outputs visible | Model family | Provider | Human reviewer ID |
|---|---|---|---|---|---|---|---|
| EIC | eic | model | subagent-ab9ad39cb940461ee | false | claude | anthropic | unknown (null) |
| R1 | methodology | model | subagent-a81119182785dc445 | false | claude | anthropic | unknown (null) |
| R2 | domain | model | subagent-a82aa9c4a5b2a16d5 | false | claude | anthropic | unknown (null) |
| R3 | perspective | model | subagent-a3e7e877c82406c01 | false | claude | anthropic | unknown (null) |
| DA | da | model | subagent-aaefc0f10fe473396 | false | claude | anthropic | unknown (null) |

| Provenance axis | Status (`true` / `false` / `unknown`) |
|---|---|
| Role-separated | true |
| Within-panel invocation-context separation | true |
| Blind to peer outputs | true |
| Model-family distinct | false |
| Provider distinct | false |
| Human-reviewer distinct | false |

- **Binary independence claim**: Not computed (`independence_claim: not_computed_from_personas`). Persona or role diversity proves only `role_separated`. This panel is not described as independent, and agreement between seats below is not treated as independent confirmation.
- **Correlated-error disclosure**: All model-executed review seats used one model family; role separation does not remove correlated-error risk.

---

## Part 1: Editorial Decision Letter

Dear Author(s),

Thank you for submitting your manuscript titled "'Trúng gió' or Stroke? Testing LLM Triage on Folk-Worded and Unaccented Vietnamese Health Questions" for a pre-submission check against a Q3 AI-in-healthcare (LNCS) conference standard. Your manuscript has been reviewed through 5 role-separated review seats, including a Journal-Fit Reviewer role (EIC), a methodology seat (R1), a domain seat (R2), a cross-disciplinary seat (R3) and a Devil's Advocate (DA). Their execution provenance is reported above and is not reduced to a binary independence claim. All five seats ran on one model family, so agreement between them carries correlated-error risk.

### Decision: Major Revision

### Mechanical decision audit (sprint contract `reviewer/reviewer_full/v2`)

Step 1 — role-scoped scoring matrix (only eligible, assessed seats counted; `not_assessed` values from ineligible seats are excluded from numerator and denominator):

| Dimension | Priority | Eligible roles | Assessed eligible scores | Audit verdict |
|---|---|---|---|---|
| D1 methodology_rigor | mandatory | methodology | R1 = warn | warn |
| D2 domain_accuracy | mandatory | domain | R2 = warn | warn |
| D3 argumentative_coherence | mandatory | da, methodology | DA = warn; R1 = warn | warn |
| D4 cross_disciplinary_relevance | high | perspective | R3 = warn | warn |
| D5 writing_and_structure | normal | eic | EIC = warn | warn |
| D6 venue_fit_and_contribution | mandatory | eic | EIC = warn | warn |

No seat declared `block` or `block_class: fatal` on any dimension. No dimension is unassessed.

Step 2 — failure conditions:

| Condition | Severity | Quantifier | Expression | Evaluation | Fired |
|---|---|---|---|---|---|
| F1 | 95 | any | any mandatory dimension has a fatal block | no fatal block on D1, D2, D3 or D6 | false |
| F2 | 90 | any | any mandatory dimension scores 'block' | no mandatory seat scored block | false |
| F3 | 70 | majority | two or more mandatory dimensions score 'warn' or worse | D1 (1/1 seat warn: owner seat), D2 (1/1 warn), D3 (2/2 warn: both seats required for n=2), D6 (1/1 warn) all true; 4 ≥ 2 | true |
| F4 | 60 | any | any high-priority dimension scores 'block' | D4 = warn, not block | false |
| F5 | 40 | any | any dimension scores 'warn' or worse | all six dimensions warn | true |
| F0 | 10 | all | every dimension scores 'pass' | no dimension passes | false |

Step 3 — precedence: of the fired conditions, F3 has the highest severity (70 > 40), so its action applies. No action was softened. There are no DA CRITICAL findings (the DA card's CRITICAL table is empty), so the DA adjudication list is empty and no DA-CRITICAL-vs-accept marker applies.

```
dimension_verdicts: [D1=warn, D2=warn, D3=warn, D4=warn, D5=warn, D6=warn]
fired_conditions: [F3, F5]
da_critical_adjudications: []
editorial_decision=major_revision
```

### Consensus Analysis

Consensus is counted per sub-claim over the 4 non-DA seats (EIC, R1, R2, R3); a silent seat is `not-mentioned`, never agreement. The full inventory is in Part 4.

#### Points of Agreement (Consensus)

- [CONSENSUS-4] None. No sub-claim was raised or corroborated by all four non-DA seats.
- [CONSENSUS-3] **SC-9 — the abstract should state that the Vietnamese versions (translations, folk rewrites, remedies) were LLM-drafted and not re-reviewed by a clinician.** Raised by EIC:W8 ("One clause in the abstract would bring it in line with the body's framing"), corroborated by R2:W1 (minimum fix: "state in the abstract and introduction that the folk versions are author-constructed, LLM-assisted rewrites") and R3:W1 ("the Limitations wording should be echoed in the abstract"; also R3 Minor Issue 1). Silent seat: R1. Severities are transported per parent finding (EIC:W8 minor; R2:W1 and R3:W1 major, whose parents also bundle larger requests split out as SC-27 and SC-37). No seat argued the abstract clause is unnecessary, so this is not treated as a severity dispute.

Corroborated findings (2 of 4, no conflict; below the consensus bar):
- **SC-7** deployment guidance is scattered and generic (EIC:W7, R3:W4).
- **SC-18** the remedy-stance label (κ = 0.50 on 32 answers) needs stronger validation, including a human-labelled check (R1:W7, R3:W2).
- **SC-29** the lexicon's lay-meaning glosses lack an ethnographic or medical-anthropology source (R2:W2, R3:W6).
- **SC-36** the release has no stated licence, record schema or location (R2:W7, R3:W7; also R2:Q4, R3:Q4).

All other sub-claims are single-seat findings, assessed on their named criterion and anchored evidence. Several single-seat findings are corroborated by the DA (SC-2, SC-6, SC-11, SC-15, SC-16, SC-17, SC-19, SC-33); DA corroboration is reported but does not enter consensus counts.

#### Points of Disagreement

- **SC-6 — severity of the Introduction's causal claim given no neutral-paraphrase control.** EIC:W6 rates it Minor and frames it as a wording fix ("by the change in telling (register, vocabulary and folk label together)"), explicitly deferring "to the methodology seat on the design". R1:W3 rates it Major: folk-specific attribution "is not identified" without a clinical-paraphrase arm, and the Introduction and abstract should be narrowed. Both cite the same sentence ("Any change in the advice is then caused by the wording, not by missing information."). Type: severity disagreement. DA:M1 and DA:m3 side with R1 (DA is outside the count).
  - **Editor's Resolution**: Treated as major and must-fix, with the remedy both seats share: narrow the causal sentence in the Introduction and abstract. Adding a paraphrase arm stays optional. Rationale: expertise first. Design identification is the methodology seat's remit, and the EIC seat itself defers on it. The two remedies do not conflict.
- **SC-19 — how the abstract should report remedy endorsement.** R1:W7 asks that the per-model count ("in 7 of 14 emergencies for one model") leave the abstract unless human-verified, because it rests on a label with κ = 0.50. R3:W2 argues the opposite direction on harm: the definition can understate harm, and the abstract reports only the 10% unsafe-endorsement figure while serious-case endorsement is 23%. Type: direction disagreement on abstract content (DA:m4 sides with R1).
  - **Editor's Resolution**: Any endorsement number in the abstract must first be human-verified or carry an explicit validity qualifier. The per-model "7 of 14" leaves the abstract unless human-verified. R3's fuller harm split (SC-38) goes in Results. Once the human check is done (SC-18), the author chooses which verified figure leads the abstract and explains the choice in the response letter. Rationale: evidence first. Both positions rest on the same weakly validated label, so the label's validity limits how strong the abstract claim can be in either direction. R3's substantive concern, that harm is understated, is not dismissed. It is routed to the body analysis in REV-40, where it can be checked against data.

Noted tensions that are not SPLITs (no seat disputes another's sub-claim):
- EIC:W5 asks for a shorter, less number-dense abstract, while SC-9, SC-30 and SC-19 add qualifiers to it. The two are compatible: qualifiers replace numbers, they do not add to them.
- EIC:W2 builds its retitling request on the trúng gió result, and R3:S3 praises that result. DA:M2 objects that it rests on one stroke case (nine answers per version) that was itself flagged in the meaning check. The retitling request stands on the pooled diacritic results, not on the stroke case. The trúng gió statement must still be presented as a single-case observation (REV-47).
- R3:S1 praises the design for letting a clinician read a change as "a wording effect". This does not dispute SC-6: the narrowed sentence still describes a wording effect, just not a folk-label-specific one.

### DA findings (no CRITICAL)

The DA card's CRITICAL table is empty, and the DA states "none, in my reading, overturns the core result, so no CRITICAL is raised". DA MAJOR findings are carried into the roadmap: M1 → REV-6 (with EIC:W6, R1:W3), M2 → REV-47, M3 → REV-19 (with R1:W6), M4 → REV-48, M5 → REV-49. DA minor findings: m1 → REV-35, m2 → REV-17, m3 → REV-6, m4 → REV-21, m5 → REV-50, m6 → REV-14 and REV-18. The DA's strongest counter-argument (the defensible contribution is a robustness probe of small open models on unaccented Vietnamese, not a folk-illness finding) is answered through REV-2, REV-6 and REV-47, and does not change the mechanical decision.

### Decision Rationale

The decision is set mechanically by the contract. All six dimensions scored warn and none scored block, so F3 fires (two or more mandatory dimensions at warn or worse) together with F5, and F3's higher severity gives Major Revision. This matches the only explicit recommendation on file: the EIC card's preliminary signal of "Major Revision, driven by presentation". R1, R2 and R3 give no overall recommendation. Their cards say the issues do not overturn the core result (R1: "None of these overturns the pooled main result"; R3: "None of this threatens the core finding").

Every seat that commented on the core regards it as sound. R1 reproduced every pooled number and plotted value (R1 summary; AR1–AR6 consistent). The DA independently reproduced the Table 2 means. The paired design and the over-triage controls are praised by R1:S1, R2:S4, R3:S2 and EIC:S2. Reject is therefore not indicated.

Minor Revision is not available under the contract, and the substance supports that too. Three groups of required changes go beyond wording:
- **Inference supporting the confirmatory claims**: small-cluster intervals (R1:W1), interaction estimates (R1:W4) and judge validation stratified by version (R1:W2).
- **Validity of the reference standard and of the remedy label**: clinician confirmation of urgency for the Vietnamese texts (R3:W1) and human-verified stance labels (R1:W7, R3:W2).
- **Claim scope**: framing that leads with folk labels although the paper finds diacritic loss is the main effect (EIC:W2, DA:M1, DA:M2), and a worst-case diacritic manipulation stated as the main finding (R2:W3).

Most of this uses data the authors already hold. One item needs new human input (REV-39). The page overrun (EIC:W1) is a format gate whose exact threshold depends on the venue chosen.

### Blocking Issues (0–3, immutable source order)

Selection rule: the three must-fix items whose resolution decides whether the primary outcome is measured validly. All 16 must-fix items remain required. This table only highlights blockers and does not rank them.

| Transport ref | Blocking issue | Source reviewer(s) | Evidence anchor | Resolving roadmap item |
|---------------|----------------|--------------------|-----------------|------------------------|
| R5 | Confirmatory intervals rest on a percentile bootstrap over 14 emergency clusters, which can undercover | R1 (W1) | `text: "The mean effect over models uses a case-level bootstrap that resamples cases for all models together."` | REV-13 |
| R6 | Judge validation has no κ interval, no confusion matrix, and no stratification by diacritic status or by Gemini vs non-Gemini answers, so part of the diacritic effect could be measurement error | R1 (W2) | `text: "Judge--human agreement on triage was $\kappa=0.90$ over the four labels and $\kappa=0.94$ for the binary emergency/not decision."` | REV-15 |
| R14 | No clinician confirmed that the Vietnamese emergency and urgent texts keep the source urgency label | R3 (W1) | `text: §6 Limitations "Triage labels come from physicians for the English source texts and were not re-reviewed by a clinician for the Vietnamese versions."` | REV-39 |

---

## Part 2: Revision Roadmap

> Notation: `R<n>` / `S<n>` are transport references, not ranks, and are distinct from seat names. Seats are written as `EIC`, `R1`, `R2`, `R3`, `DA` with a finding id, e.g. `R1:W3`, `R2:Q1`. Source order is fixed: seat order EIC → R1 → R2 → R3 → DA. Within a seat the order is weakness/finding ordinal, then questions, then minor issues. Severity, obligation and cost never affect order. The `Sub-Claim(s)` column carries the Part 4 `sub_claim_id`; minor-issue items with no decomposed sub-claim use `—`.
>
> Block manifest: no bound block manifest was supplied for this round, so exact `proposed_targets[]` block ids cannot be emitted. Each row gives a section/locator target instead. The machine `revision-roadmap/1.0` core must be built by `scripts/revision_roadmap.py` once a block manifest exists (`[BLOCK-MANIFEST-UNAVAILABLE]`). Obligation counts: must_fix 16, should_fix 28, consider 6 (total 50).

### Required Revisions (Must Fix)

| Transport ref | Revision Item | Sub-Claim(s) | Severity | Evidence Anchor | Confidence | Source | Obligation class | Cost scope | Bounded consequence |
|---|---|---|---|---|---|---|---|---|---|
| R1 | Bring the main text within the chosen venue's page limit (conclusion currently ends p. 18) | SC-1 | major | `text: §8 Conclusion, last sentence, p. 18 "We release the cases, the lexicon, all answers and labels."` | 4 — page count read from typeset PDF; limit depends on venue | EIC (W1, Q1) | must_fix | section: whole manuscript (figures, §3.3, Fig. 10, robustness) | editorial_conformance_unmet → manuscript |
| R2 | Retitle and reorder abstract/contributions so diacritic loss leads and the folk-label result is presented as smaller and condition-dependent | SC-2 | major | `text: §5.4 "so the best-known folk label did not mislead the models"` | 4 — framing is core remit | EIC (W2, Q2); DA M1, M2 corroborate | must_fix | section: title, abstract, §1 contribution list | claim_scope_unsupported → claim: title/abstract headline |
| R3 | Narrow the causal sentence: change is attributable to the rewording as a bundle (register, dialect vocabulary, folk label), not to folk labels specifically; carry the narrowing into abstract | SC-6 | major (R1:W3; EIC:W6 minor — SPLIT arbitrated) | `text: §1 "Any change in the advice is then caused by the wording, not by missing information."` | R1: 3 — design inference; EIC: 3 — framing | R1 (W3), EIC (W6); DA M1, m3 | must_fix | sentence: §1 Introduction + abstract | claim_scope_unsupported → claim: §1 causal sentence |
| R4 | Add to the abstract that the Vietnamese versions were LLM-drafted and not re-reviewed by a clinician | SC-9 | minor (EIC:W8); major (R2:W1, R3:W1 parents) | `absence: Abstract — expected a clause that the Vietnamese versions were LLM-drafted and not re-reviewed by a clinician; checked Abstract, §1 contribution list, §3.2 Authorship paragraph, §7 Limitations` | EIC 4; R2 4; R3 4 | EIC (W8), R2 (W1), R3 (W1, Minor 1) — CONSENSUS-3 | must_fix | sentence: abstract | reporting_requirement_unmet → section: abstract |
| R5 | Add small-cluster sensitivity inference (exact sign-flip permutation over 14 case differences, and t/BCa interval or crossed random-effects model) for the confirmatory contrasts | SC-10 | major | `text: "The mean effect over models uses a case-level bootstrap that resamples cases for all models together."` | 4 — small-sample resampling | R1 (W1) | must_fix | re_analysis: §4 Statistics, §5 RQ1–RQ2 | evidence_gap_remains → claim: +11 [4, 18], +25, +29 intervals |
| R6 | Report judge–human 2×2 confusion matrix with κ CI; agreement split by with/without diacritics and Gemini vs non-Gemini answers; human-labelled vs judge-labelled under-triage contrast on the 150-answer sample | SC-12, SC-13 | major | `text: "Judge--human agreement on triage was $\kappa=0.90$ over the four labels and $\kappa=0.94$ for the binary emergency/not decision."` | 4 — LLM-as-judge validation | R1 (W2) | must_fix | re_analysis: §4 Measures / judge validation | evidence_gap_remains → claim: diacritic effect not measurement error |
| R7 | Estimate the interaction and the diacritic-minus-folk difference with CIs before stating "do not add up" / "most of the harm"; soften "causes" to "accounts for"; address ceiling in weakest models | SC-15 | major | `text: "The two changes do not add up."` | 4 — factorial contrasts | R1 (W4); DA m2 | must_fix | re_analysis: §5 RQ1–RQ2, abstract, Conclusion | claim_scope_unsupported → claim: sub-additivity / "most of the harm" |
| R8 | Recast per-model and language-adaptation statements as descriptive with per-model intervals; support any heterogeneity claim with a model × version test | SC-16 | major | `text: "language adaptation did not make the model more robust to unaccented input"` | 4 — subgroup inference | R1 (W5); DA m6 | must_fix | section: abstract, §5, §6 Discussion | claim_scope_unsupported → claim: per-model and adaptation conclusions |
| R9 | Correct the Discussion claim that folk wording "mattered more" for paracetamol liver failure and DKA, which conflicts with Fig. 10; report folk vs clin per condition separately or drop the attribution | SC-17 | major | `figure: Fig. 10 (fig:conditions), rows "Liver failure (paracetamol)" and "Diabetic ketoacidosis"` | 5 — direct read-off | R1 (W6); DA M3 | must_fix | sentence: §6 Discussion "Folk wording: smaller…" paragraph | acceptance_criterion_unmet → figure: Fig. 10 vs §6 text |
| R10 | Strengthen remedy-stance validation: κ CI, stance confusion matrix, bound on unsafe endorsement under observed disagreement, or human-labelled stance for the highlighted models / serious-case endorsements | SC-18 | major | `text: "in 7 of 14 emergencies for one model"` | 4 — misclassification statistics | R1 (W7), R3 (W2) | must_fix | re_analysis: §5 RQ3 remedy results | evidence_gap_remains → claim: unsafe-endorsement rates |
| R11 | Abstract reports only human-verified or explicitly qualified endorsement figures; remove "7 of 14" unless human-verified | SC-19 | major | `text: Abstract "and in 7 of 14 emergencies for one model"` | R1 4; R3 4 | R1 (W7), R3 (W2) — SPLIT arbitrated; DA m4 | must_fix | sentence: abstract, §1 Contribution 2 | claim_scope_unsupported → section: abstract |
| R12 | Split the lexicon into folk-illness/explanatory labels vs lay/dialectal symptom vocabulary; report RQ1 effect for cases with an explanatory label if feasible | SC-28 | major | `table: Appendix B, Table 4 (tab:lexicon), rows chuột rút, tức ngực, hụt hơi, lẹo, giời leo, nhiệt miệng` | 4 — native-level lay vocabulary knowledge | R2 (W2, Q2) | must_fix | section: §3.4, Appendix B Table (tab:lexicon), Contribution 1 | claim_scope_unsupported → dataset: folk-term lexicon |
| R13 | Qualify the diacritic finding as "fully unaccented" in abstract and conclusion; state what is known (or that nothing is known) about the prevalence of fully unaccented input; return to it in Limitations | SC-30 | major | `text: §3.2 "This is a controlled worst case; real users may type with partial or inconsistent diacritics." and Abstract "Missing diacritics cause most of the harm"` | 4 — diacritic-restoration expertise | R2 (W3, Q3) | must_fix | sentence: abstract, Conclusion, §7 Limitations | claim_scope_unsupported → claim: headline diacritic effect |
| R14 | Blind clinician urgency rating of clin and folk texts for the 24 emergency/urgent cases, agreement with source label, and primary analysis rerun on confirmed set | SC-37 | major | `text: §6 Limitations "Triage labels come from physicians for the English source texts and were not re-reviewed by a clinician for the Vietnamese versions."` | 4 — emergency triage practice | R3 (W1, Q1) | must_fix | new_data: §3.3 meaning check / §5 robustness | evidence_gap_remains → claim: primary outcome reference standard |
| R15 | Report a three-way split of serious-case remedy answers (endorse without emergency advice / endorse with emergency advice / reject or not addressed); classify remedies as directly harmful vs delay-only; discuss which a clinician would deem unsafe | SC-38 | major | `text: §4 Measures "endorse the remedy and do not advise emergency care"` | 4 — ED experience with delayed presentation | R3 (W2, Q2) | must_fix | re_analysis: §4 Measures, §5 RQ3 | interpretive_ambiguity_remains → claim: unsafe-endorsement definition |
| R16 | Present the trúng gió/stroke result as a single-case observation (one case, nine answers per version, flagged in the meaning check) in the Conclusion and Contribution 3 | SC-44 | major | `text: Conclusion "The main problem was not folk labels such as \vi{trúng gió}." and Results "each condition has one case (nine answers per version)"` | 4 — counts stated in §5.4/§5.6 | DA (M2) | must_fix | sentence: §8 Conclusion, §1 Contribution 3, §6 | claim_scope_unsupported → claim: trúng gió conclusion |

### Required Item Details

**R1: Page length**
- **Problem**: The main text ends on p. 18 with references to about p. 20 and appendices to p. 22. A typical LNCS AI-in-health limit is 12–16 pages (assumed; no venue is bound).
- **Source**: EIC:W1 ("A paper this long risks a desk rejection on format before anyone reads it"); EIC:Q1.
- **Requirement**: Confirm the target venue and its page rule (EIC:Q1). Trim by the routes EIC:W1 names (merge schematics, drop figures that repeat tables, shorten §3.3, move Fig. 10 and robustness detail to the appendix or supplement).
- **Acceptance criteria**: The compiled PDF meets the stated page limit of the named venue, and the response letter names the venue and its limit.

**R2: Title and headline framing**
- **Problem**: The title and folk-first ordering of the abstract and contributions conflict with the paper's own finding that diacritic loss drives most of the harm.
- **Source**: EIC:W2, EIC:Q2; corroborated by DA:M1 and DA:M2.
- **Requirement**: Retitle around unaccented/lay input, or justify keeping the title in the response letter. Reorder the abstract and contribution list so the diacritic result comes first.
- **Acceptance criteria**: The title and the first two sentences of results in the abstract lead with the diacritic finding, and the folk-label result is described as smaller and condition-dependent.

**R3: Causal sentence and paraphrase control**
- **Problem**: The Introduction claims any change is caused by the wording and not by missing information. The folk version bundles label, register and dialect, and no neutral-paraphrase arm exists.
- **Source**: R1:W3 (major), EIC:W6 (minor, defers to R1); DA:M1, DA:m3 (which notes the paper itself describes diacritic removal as removing lexical information).
- **Requirement**: Narrow the sentence in §1 and in the abstract to the rewording as a bundle, and reconcile it with the description of diacritic removal as information loss. A clinical-paraphrase arm is optional.
- **Acceptance criteria**: No sentence in the abstract or §1 attributes the folk effect to the folk label specifically, and the "not by missing information" wording no longer conflicts with the diacritic description.

**R4: Clinical-validity caveat in the abstract**
- **Problem**: The abstract calls the vignettes "physician-labelled" without saying that the Vietnamese versions were LLM-drafted and not clinician-reviewed.
- **Source**: EIC:W8; R2:W1; R3:W1 and R3 Minor Issue 1 (CONSENSUS-3, R1 silent).
- **Requirement**: Add one clause to the abstract mirroring the Limitations section.
- **Acceptance criteria**: The abstract contains an explicit clause that the Vietnamese versions were LLM-assisted and not re-reviewed by a clinician.

**R5: Small-cluster inference**
- **Problem**: All confirmatory intervals are percentile bootstraps over 14 clusters, which are prone to undercoverage. The lower bound of 4 for the folk effect is the value most at risk.
- **Source**: R1:W1.
- **Requirement**: Report an exact sign-flip permutation test and a t/BCa interval (or crossed random-effects logistic model) on the 14 case-level differences next to the bootstrap results.
- **Acceptance criteria**: For each of the three primary contrasts the manuscript reports at least one small-sample-robust interval or exact p-value, and states whether conclusions change.

**R6: Judge validation by stratum**
- **Problem**: Overall κ cannot show whether the judge errs differently across versions. The judge also belongs to the same family as two evaluated models.
- **Source**: R1:W2.
- **Requirement**: Report a 2×2 emergency/not confusion matrix with a κ CI, agreement by diacritic status and by Gemini vs non-Gemini answers, and the human- vs judge-labelled under-triage contrast on the 150-answer sample.
- **Acceptance criteria**: All three analyses appear in the main text or an appendix, and the text states whether judge error differs by stratum.

**R7: Interaction estimates**
- **Problem**: "Do not add up" and "most of the harm" are stated without an interaction estimate or CI. The weakest models sit near ceiling.
- **Source**: R1:W4; DA:m2.
- **Requirement**: Report (folk_nd − clin_nd) − (folk − clin) and the diacritic-minus-folk paired difference with bootstrap CIs, soften "causes" to "accounts for", and note ceiling effects.
- **Acceptance criteria**: Both quantities appear with CIs, and the abstract/Conclusion wording matches what the intervals support.

**R8: Per-model and adaptation claims**
- **Problem**: Model-level conclusions ("concentrate in small open models", Gemini "barely affected", Qwen2.5-7B "no effect", the language-adaptation conclusion) over-read 14-case intervals. No heterogeneity test is reported.
- **Source**: R1:W5; DA:m6.
- **Requirement**: Recast these as descriptive statements with per-model intervals, or support them with a model × version interaction test.
- **Acceptance criteria**: No model-level or adaptation conclusion is stated as a finding without either a heterogeneity test or an explicit descriptive qualifier.

**R9: Discussion vs Fig. 10 conflict**
- **Problem**: The Discussion says folk wording mattered more for liver failure and DKA, but Fig. 10 shows no clin→folk rise for either case (liver failure 22→22, DKA 56→56).
- **Source**: R1:W6; DA:M3.
- **Requirement**: Correct the examples (R1 suggests meningitis or heart failure, which rise clin→folk), or report folk vs clin per condition separately, or drop the attribution. Keep the one-case caveat.
- **Acceptance criteria**: Every per-condition example in §6 matches the corresponding Fig. 10 cells for the contrast it is cited for.

**R10: Remedy-stance validation**
- **Problem**: Unsafe endorsement compounds a κ = 0.50 stance label with the triage label. The intervals ignore misclassification and clustering.
- **Source**: R1:W7; R3:W2 (human-labelled check "more important, not less").
- **Requirement**: Report the κ CI and stance confusion matrix, plus either a misclassification bound or human-labelled stance for the highlighted models or serious-case endorsements.
- **Acceptance criteria**: The remedy section reports the κ CI and at least one of: a misclassification bound, or human-verified unsafe-endorsement counts.

**R11: Remedy figures in the abstract**
- **Problem**: The abstract headlines a per-model count drawn from the weakest-validated label. R3 holds that the abstract also understates harm.
- **Source**: R1:W7, R3:W2 (SPLIT, arbitrated above); DA:m4.
- **Requirement**: Keep only human-verified or explicitly qualified endorsement figures in the abstract, and remove "7 of 14" unless verified.
- **Acceptance criteria**: Every endorsement figure in the abstract is human-verified or carries an inline validity qualifier, and the response letter explains which figure leads.

**R12: Lexicon categories**
- **Problem**: The "34 folk terms" mix explanatory folk-illness labels with standard or colloquial symptom words.
- **Source**: R2:W2, R2:Q2.
- **Requirement**: Split the lexicon into (a) folk-illness/explanatory labels and (b) lay/dialectal vocabulary, update Contribution 1, and if feasible report the RQ1 effect for cases carrying an explanatory label.
- **Acceptance criteria**: The lexicon table shows the two categories, and Contribution 1 describes the resource with matching terms.

**R13: Full-strip diacritic qualifier**
- **Problem**: The headline diacritic effect comes from a full-strip worst case of undocumented prevalence, but the abstract and conclusion state it unqualified.
- **Source**: R2:W3, R2:Q3.
- **Requirement**: Qualify the effect as "fully unaccented" in the abstract and Conclusion, add what is known about prevalence (or state that it is unknown), and return to it in Limitations.
- **Acceptance criteria**: The abstract and Conclusion say "fully unaccented" (or equivalent), and Limitations discusses partial-diacritic input.

**R14: Clinician urgency check**
- **Problem**: The primary outcome assumes every Vietnamese version keeps the English source's urgency label, and only non-clinicians checked this.
- **Source**: R3:W1, R3:Q1.
- **Requirement**: Have one or two Vietnamese-speaking emergency or primary-care physicians rate clin and folk texts of the 24 emergency/urgent cases blind to the source label, report agreement, and rerun the primary analysis on the confirmed set. If the author declines, the decline is recorded as unresolved in the response letter, and R4's abstract caveat becomes the minimum disclosure.
- **Acceptance criteria**: The manuscript reports clinician–source agreement and the primary result on the confirmed set, or the response letter records an explicit decline that stays visible to the next review.

**R15: Unsafe-endorsement definition**
- **Problem**: Endorsing a delaying or harmful remedy alongside emergency advice counts as safe.
- **Source**: R3:W2, R3:Q2.
- **Requirement**: Report the three-way split on serious cases using the existing labels, classify remedies as directly harmful vs delay-only, and discuss which endorsements a clinician would call unsafe.
- **Acceptance criteria**: The three-way split table or text appears in §5 RQ3, and the remedy classification is stated.

**R16: Trúng gió as single-case observation**
- **Problem**: The Conclusion and Contribution 3 generalise from one flagged stroke case.
- **Source**: DA:M2.
- **Requirement**: Restate the result as a single-case observation, giving the number of answers and the meaning-check flag.
- **Acceptance criteria**: No sentence generalises the trúng gió result beyond the single case, and the flagged status of E08 is mentioned where the result is stated.

### Suggested Revisions (Should Fix / Consider)

| Transport ref | Revision Item | Sub-Claim(s) | Severity | Evidence Anchor | Confidence | Source | Obligation class | Cost scope | Bounded consequence |
|---|---|---|---|---|---|---|---|---|---|
| S1 | Keep one of each figure/table pair (Fig. 6 vs Table 2; Fig. 11 vs Table 3; Fig. 8a) | SC-3 | minor | `figure: Fig. 11 — panels (a) and (b) give the means of Table 3's clin, folk_nd and over columns` | 4 | EIC (W3) | should_fix | section: §5 figures | editorial_conformance_unmet → figure: Figs. 6, 8a, 11 |
| S2 | Merge overlapping schematics (Figs. 1, 4, 5; Fig. 2 derivation) | SC-4 | minor | `figure: Fig. 4 — source counts, case groups, 260 prompts and 2,340 answers, all already shown in Fig. 1` | 4 | EIC (W4) | should_fix | section: §3 figures | editorial_conformance_unmet → figure: Figs. 1, 4, 5 |
| S3 | Shorten abstract to ≤250 words with 3–4 key numbers | SC-5 | minor | `text: Abstract "Vietnamese speakers often describe symptoms with folk-illness labels"` | 4 | EIC (W5) | should_fix | section: abstract | editorial_conformance_unmet → section: abstract |
| S4 | Add one "Implications for deployment" paragraph with concrete, evidence-proportionate steps (test threshold, deterministic red-flag layer, unconditional emergency wording, no deployment to users who type unaccented if the model fails); state no mitigation is shown adequate as sole safeguard | SC-7 | minor | `text: §6 "Restoring diacritics before the text reaches the model is a cheap step that deserves testing"` (EIC); `text: §6 "A health app built on a small local model should be tested on unaccented, lay input before use."` (R3) | EIC 4; R3 4 | EIC (W7), R3 (W4, Q3) | should_fix | section: §6 Discussion / §8 | interpretive_ambiguity_remains → section: deployment guidance |
| S5 | Optional small diacritic-restoration pilot on the 260 prompts | SC-8 | minor | `text: §6 "Restoring diacritics before the text reaches the model is a cheap step that deserves testing"` | 4 | EIC (W7, Q3) | consider | new_data: §5 mitigation | evidence_gap_remains → claim: restoration as remedy |
| S6 | Move §3.3 agreement statistics to an appendix, leaving one summary sentence | — | minor `[SEVERITY-SOURCE: letter-fallback]` (Minor Issues list) | `text: §3.3 Meaning check` | 4 `[CONFIDENCE-SOURCE: report-level]` | EIC (Minor 1) | consider | section: §3.3 | editorial_conformance_unmet → section: §3.3 |
| S7 | Check that run dates in the Table 1 caption meet the venue's anonymity rules | — | minor `[SEVERITY-SOURCE: letter-fallback]` | `table: Table 1 caption` | 4 `[CONFIDENCE-SOURCE: report-level]` | EIC (Minor 2) | consider | sentence: Table 1 caption | editorial_conformance_unmet → table: Table 1 |
| S8 | Move exploratory Fig. 10 to the appendix | — | minor `[SEVERITY-SOURCE: letter-fallback]` | `figure: Fig. 10` | 4 `[CONFIDENCE-SOURCE: report-level]` | EIC (Minor 3) | consider | section: §5.4 | editorial_conformance_unmet → figure: Fig. 10 |
| S9 | State that inference is conditional on these nine models ("on average" = over this model set) | SC-11 | major | `text: "The mean effect over models uses a case-level bootstrap that resamples cases for all models together."` | 4 | R1 (W1); DA m6 | should_fix | sentence: §4 Statistics, abstract | claim_scope_unsupported → claim: "on average" |
| S10 | Disclose that the primary human annotator (first author) was not blind to the hypothesis, and that unaccented answers may reveal their version | SC-14 | major | `text: "Judge--human agreement on triage was $\kappa=0.90$ ..."` | 4 | R1 (W2) | should_fix | sentence: §4 judge validation | reporting_requirement_unmet → section: judge validation |
| S11 | Correct the detectable-effect statement for Holm over 36 tests (~79 points, not ~30); state whether the pooled primary contrasts form a family | SC-20 | minor | `text: "a single model's difference must be large (about 30 points or more) to be detected"` | 4 | R1 (W8) | should_fix | sentence: §4 Statistics | acceptance_criterion_unmet → claim: detectable effect |
| S12 | Mark zero-width bootstrap cells as degenerate, or use exact/Newcombe paired intervals | SC-21 | minor | `table: Table 2 (tab:main), Gemini rows "+0 [+0, +0]"` | 4 | R1 (W9) | should_fix | re_analysis: Table 2 | interpretive_ambiguity_remains → table: Table 2 |
| S13 | Add a paired CI for the over-triage change over 28 controls | SC-22 | minor | `text: "The models therefore did not compensate by becoming more cautious."` | 3 | R1 (W10) | should_fix | re_analysis: §5 over-triage | evidence_gap_remains → claim: "less urgent overall" |
| S14 | State that mitigations shifted both versions in parallel (gap 19.75 → 19.75/17.75); add the descriptive qualifier to the abstract's "lowered under-triage" | SC-23 | minor | `text: "Neither prompt closed the gap between the two versions."` | 4 | R1 (W11) | should_fix | sentence: §5 mitigation, abstract | interpretive_ambiguity_remains → table: Table 3 (tab:mit) |
| S15 | Align results text with Fig. 10 caption on asthma having two cases | SC-24 | minor | `text: "each condition has one case (nine answers per version)"` | 5 | R1 (W12) | should_fix | sentence: §5.4 | reader_traceability_reduced → figure: Fig. 10 |
| S16 | Add analysis code, HF revision hashes, Gemini version identifiers, bootstrap seed | SC-25 | minor | `absence: Experimental Setup and release statements — expected analysis code, Hugging Face model revision hashes, Gemini model version identifiers and bootstrap seed; checked abstract, Table 1 caption, Prompting and decoding, Statistics, Ethics Statement, Conclusion` | 4 | R1 (W13) | should_fix | section: §4 setup, release statement | method_reproducibility_unresolved → manuscript |
| S17 | State the denominator of Llama's 35% "no usable advice" | SC-26 | minor | `text: "because 35\% of its remedy answers gave no usable advice"` | 3 | R1 (W14; AR7 not_computable) | should_fix | sentence: §5 RQ3 | reader_traceability_reduced → claim: Llama 35% |
| S18 | Anchor the folk register in real Vietnamese user text (lexicon-term frequency, question length), or state its absence; answer how folk labels were chosen | SC-27 | major | `text: §3.2 Authorship "The translations, folk versions, remedies and lexicon glosses were drafted with an LLM (Claude)."` | 4 | R2 (W1, Q1) | should_fix | new_data: §3.2 | claim_scope_unsupported → claim: RQ1 as evidence about real users |
| S19 | Source each lexicon gloss (ethnographic/medical-anthropology) or mark as author-provided | SC-29 | major (R2:W2); minor (R3:W6) | `table: Appendix B, Table 4 (tab:lexicon)` (R2); `text: §3.4 "drafted with an LLM and reviewed by the first author, not taken from an ethnographic source"` (R3) | R2 4; R3 4 | R2 (W2), R3 (W6) | should_fix | section: Appendix B lexicon | reporting_requirement_unmet → dataset: lexicon glosses |
| S20 | Optional partial-diacritic condition (e.g. 30–70% syllable removal) to bound the effect | SC-31 | major | `text: §3.2 "This is a controlled worst case; real users may type with partial or inconsistent diacritics."` | 4 | R2 (W3) | consider | new_data: §5 | evidence_gap_remains → claim: realistic diacritic effect |
| S21 | Source or soften folk-illness prevalence claims; qualify "usually benign" per term | SC-32 | minor | `text: §1 "Unlike a typo, a folk label is not noise: it names a different, usually benign, illness."` | 3 | R2 (W4) | should_fix | sentence: §1 Introduction | claim_scope_unsupported → claim: "usually benign" |
| S22 | Soften the Discussion heading and Conclusion sentence that state the diacritic mechanism as fact | SC-33 | minor | `text: §6 "The answers suggest that the models did not weigh the signs differently; they failed to read them."` | 4 | R2 (W5); DA m1 | should_fix | sentence: §6 heading, §8 | claim_scope_unsupported → claim: diacritic mechanism |
| S23 | Name ambiguity (syllable collapse) and tokenisation as competing mechanisms | SC-34 | minor | `text: §6 "The answers suggest that the models did not weigh the signs differently; they failed to read them."` | 4 | R2 (W5) | should_fix | section: §6 Discussion | interpretive_ambiguity_remains → section: §6 |
| S24 | Add related work on cross-lingual health-LLM evaluation, Vietnamese health QA, Vietnamese diacritic restoration (R2's Vietnamese items are flagged [UNVERIFIED] search leads) | SC-35 | minor | `text: §2 "We are not aware of work that measures lay phrasing, folk-illness terms or missing diacritics in Vietnamese health questions."` | 3 | R2 (W6) | should_fix | section: §2 Related Work | reader_traceability_reduced → section: §2 |
| S25 | State licence, record schema and release location (placeholder acceptable while anonymised) | SC-36 | minor | `absence: Ethics Statement and Conclusion — expected licence, record schema and release location for the cases, lexicon and outputs; checked abstract, contributions list, §3, Ethics Statement, Conclusion, Appendices A–B` | R2 4; R3 3 | R2 (W7, Q4), R3 (W7, Q4) | should_fix | section: Ethics Statement / data card | reporting_requirement_unmet → dataset: release |
| S26 | Report soon-or-worse vs emergency share for the urgent tier; state the secondary outcome is a lower bound | SC-39 | minor | `text: §3.1 "The urgent cases form a secondary outcome: for them, only home care is wrong."` | 4 | R3 (W3) | should_fix | re_analysis: §5 urgent outcome | interpretive_ambiguity_remains → claim: urgent-tier outcome |
| S27 | Split mitigation over-triage into soon→ED and self-care→ED; interpret per 1,000 queries; note Flash-Lite's cautious operating point | SC-40 | minor | `table: Table 4 (tab:mit), column "over"` (as cited by R3; the mitigation table is labelled tab:mit) | 3 | R3 (W5) | should_fix | re_analysis: §5 mitigation | interpretive_ambiguity_remains → table: tab:mit |
| S28 | Rename the lexicon's "Can hide" column, review the vong theo entry, and add a data-card note against stereotyping | SC-41 | minor | `text: §3.4 Folk-term lexicon "drafted with an LLM and reviewed by the first author, not taken from an ethnographic source"` | 4 | R3 (W6) | should_fix | section: Appendix B, data card | reporting_requirement_unmet → dataset: lexicon |
| S29 | Specify release safeguards: terms of use, gated or research-only access for remedy/output files, canary string, inline content warnings | SC-42 | minor | `text: Ethics Statement "The release is meant for evaluation only"` | 3 | R3 (W7, Q4) | should_fix | section: Ethics Statement | reporting_requirement_unmet → dataset: remedy and output files |
| S30 | Add a paragraph placing results in Vietnamese care-seeking pathways (pharmacy-first, 115 access, traditional practitioners), with sources | SC-43 | minor | `absence: Introduction and Discussion — expected description of Vietnamese care-seeking pathways (pharmacy-first self-medication, 115 access, traditional practitioners) where the advice would be acted on; checked Introduction, Discussion, Limitations, Ethics Statement` | 3 | R3 (W8) | should_fix | section: §6 Discussion | interpretive_ambiguity_remains → section: harm framing |
| S31 | Note for non-Vietnamese readers that 115 ambulance access varies | — | minor `[SEVERITY-SOURCE: letter-fallback]` | `text: M1 prompt and judge prompt (115 number)` | 4 `[CONFIDENCE-SOURCE: report-level]` | R3 (Minor 2) | consider | sentence: §4 / Appendix prompts | reader_traceability_reduced → section: mitigation prompts |
| S32 | Report the label distribution (incl. *none*) per version and recompute under- and over-triage excluding *none* | SC-45 | major | `text: Discussion "Lay or unaccented text made the advice less urgent across the board, as if such users had milder problems." and Measures "(answers labelled \emph{none} count as under-triage)"` | 3 | DA (M4) | should_fix | re_analysis: §5, §6 | interpretive_ambiguity_remains → claim: "less urgent overall" |
| S33 | Report endorsement conditional on the model's folk-version triage, or drop the sycophancy framing of RQ3 | SC-46 | major | `text: Dataset "which separates real sycophancy from a habit of rejecting all folk medicine." and Results "Adding a remedy and asking ``is that OK?'' did not change under-triage on average"` | 3 | DA (M5) | should_fix | re_analysis: §5 RQ3, keywords | claim_scope_unsupported → claim: sycophancy framing |
| S34 | Qualify the urgent-case diacritic results with the flagged-pair robustness finding | SC-47 | minor | `text: Robustness, flagged pairs "The diacritic effects were no longer distinguishable from zero"` | 4 | DA (m5) | should_fix | sentence: §5 urgent-case results | claim_scope_unsupported → claim: urgent-case diacritic effects |

### Reviewer Questions carried over

Every question in the reviewer cards is mapped to a roadmap item. The author should answer each one explicitly in the response letter. R1 and the DA posed no separate Questions section.

| Question | Text (paraphrased from card) | Roadmap item |
|---|---|---|
| EIC:Q1 | Which venue and page limit are you targeting; do 12–16 pages include references? | REV-1 (R1) |
| EIC:Q2 | Would you retitle around unaccented/lay input? | REV-2 (R2) |
| EIC:Q3 | Is a small diacritic-restoration pilot on the 260 prompts feasible? | REV-8 (S5) |
| R2:Q1 | How were folk labels chosen; checked against real user text? | REV-29 (S18) |
| R2:Q2 | Can explanatory folk labels be separated from lay/dialect vocabulary, with RQ1 reported for explanatory-label cases? | REV-30 (R12) |
| R2:Q3 | Any evidence on how often Vietnamese health questions are typed with no diacritics? | REV-32 (R13) |
| R2:Q4 | Under what licence will derived cases and lexicon be released? | REV-38 (S25) |
| R3:Q1 | Would a Vietnamese-speaking physician rate the folk and diacritic-free emergency texts as emergencies; is a blind check of the 24 serious cases feasible? | REV-39 (R14) |
| R3:Q2 | How many serious-case answers endorse the remedy while also advising emergency care, and which would a clinician consider unsafe? | REV-40 (R15) |
| R3:Q3 | Which concrete steps would you recommend to a Vietnamese health-app team? | REV-7 (S4) |
| R3:Q4 | Under what licence and access conditions will remedy texts and unsafe answers be released? | REV-38 (S25), REV-44 (S29) |

### Source-Traceability Checklist

> Preserve source order and do not suggest a work order. Author triage (`will_address` / `wont_address` / `not_on_point`) is collected later as an explicit, complete sidecar.

- [ ] REV-1 · R1 — obligation `must_fix`: page limit (EIC:W1, EIC:Q1)
- [ ] REV-2 · R2 — obligation `must_fix`: title and headline framing (EIC:W2, EIC:Q2; DA:M1, M2)
- [ ] REV-3 · S1 — obligation `should_fix`: figures repeating tables (EIC:W3)
- [ ] REV-4 · S2 — obligation `should_fix`: overlapping schematics (EIC:W4)
- [ ] REV-5 · S3 — obligation `should_fix`: abstract length (EIC:W5)
- [ ] REV-6 · R3 — obligation `must_fix`: narrow causal sentence (EIC:W6, R1:W3; DA:M1, m3)
- [ ] REV-7 · S4 — obligation `should_fix`: deployment implications paragraph (EIC:W7, R3:W4, R3:Q3)
- [ ] REV-8 · S5 — obligation `consider`: diacritic-restoration pilot (EIC:W7, EIC:Q3)
- [ ] REV-9 · R4 — obligation `must_fix`: clinical-validity caveat in abstract (EIC:W8, R2:W1, R3:W1, R3 Minor 1)
- [ ] REV-10 · S6 — obligation `consider`: shorten §3.3 (EIC Minor 1)
- [ ] REV-11 · S7 — obligation `consider`: Table 1 run dates vs anonymity (EIC Minor 2)
- [ ] REV-12 · S8 — obligation `consider`: Fig. 10 to appendix (EIC Minor 3)
- [ ] REV-13 · R5 — obligation `must_fix`: small-cluster inference (R1:W1)
- [ ] REV-14 · S9 — obligation `should_fix`: inference conditional on nine models (R1:W1; DA:m6)
- [ ] REV-15 · R6 — obligation `must_fix`: stratified judge validation (R1:W2)
- [ ] REV-16 · S10 — obligation `should_fix`: annotator blinding disclosure (R1:W2)
- [ ] REV-17 · R7 — obligation `must_fix`: interaction estimates (R1:W4; DA:m2)
- [ ] REV-18 · R8 — obligation `must_fix`: per-model and adaptation claims (R1:W5; DA:m6)
- [ ] REV-19 · R9 — obligation `must_fix`: Discussion vs Fig. 10 (R1:W6; DA:M3)
- [ ] REV-20 · R10 — obligation `must_fix`: remedy-stance validation (R1:W7, R3:W2)
- [ ] REV-21 · R11 — obligation `must_fix`: remedy figures in abstract (R1:W7, R3:W2; DA:m4)
- [ ] REV-22 · S11 — obligation `should_fix`: detectable effect under Holm (R1:W8)
- [ ] REV-23 · S12 — obligation `should_fix`: zero-width intervals (R1:W9)
- [ ] REV-24 · S13 — obligation `should_fix`: over-triage CI (R1:W10)
- [ ] REV-25 · S14 — obligation `should_fix`: mitigation gap wording (R1:W11)
- [ ] REV-26 · S15 — obligation `should_fix`: asthma case count (R1:W12)
- [ ] REV-27 · S16 — obligation `should_fix`: reproducibility identifiers (R1:W13)
- [ ] REV-28 · S17 — obligation `should_fix`: Llama denominator (R1:W14)
- [ ] REV-29 · S18 — obligation `should_fix`: anchor folk register in real text (R2:W1, R2:Q1)
- [ ] REV-30 · R12 — obligation `must_fix`: lexicon categories (R2:W2, R2:Q2)
- [ ] REV-31 · S19 — obligation `should_fix`: gloss sources (R2:W2, R3:W6)
- [ ] REV-32 · R13 — obligation `must_fix`: full-strip qualifier and prevalence (R2:W3, R2:Q3)
- [ ] REV-33 · S20 — obligation `consider`: partial-diacritic condition (R2:W3)
- [ ] REV-34 · S21 — obligation `should_fix`: unsourced folk-illness claims (R2:W4)
- [ ] REV-35 · S22 — obligation `should_fix`: mechanism heading (R2:W5; DA:m1)
- [ ] REV-36 · S23 — obligation `should_fix`: competing mechanisms (R2:W5)
- [ ] REV-37 · S24 — obligation `should_fix`: related work (R2:W6)
- [ ] REV-38 · S25 — obligation `should_fix`: licence, schema, location (R2:W7, R2:Q4, R3:W7, R3:Q4)
- [ ] REV-39 · R14 — obligation `must_fix`: clinician urgency check (R3:W1, R3:Q1)
- [ ] REV-40 · R15 — obligation `must_fix`: unsafe-endorsement three-way split (R3:W2, R3:Q2)
- [ ] REV-41 · S26 — obligation `should_fix`: urgent-tier outcome (R3:W3)
- [ ] REV-42 · S27 — obligation `should_fix`: mitigation over-triage cost (R3:W5)
- [ ] REV-43 · S28 — obligation `should_fix`: lexicon stereotyping safeguards (R3:W6)
- [ ] REV-44 · S29 — obligation `should_fix`: release safeguards (R3:W7, R3:Q4)
- [ ] REV-45 · S30 — obligation `should_fix`: care-seeking context (R3:W8)
- [ ] REV-46 · S31 — obligation `consider`: 115 access note (R3 Minor 2)
- [ ] REV-47 · R16 — obligation `must_fix`: trúng gió as single-case observation (DA:M2)
- [ ] REV-48 · S32 — obligation `should_fix`: *none*-label distribution (DA:M4)
- [ ] REV-49 · S33 — obligation `should_fix`: sycophancy framing (DA:M5)
- [ ] REV-50 · S34 — obligation `should_fix`: urgent-case flagged-pair qualifier (DA:m5)

### Journal-Supplied Deadline (Optional Transport)

- **Exact deadline from source letter**: NOT PROVIDED
- No deadline, duration or work estimate is inferred.

### Response Letter Template

Please respond to every item (R1–R16, S1–S34) and every reviewer Question in the table above, item by item, using `templates/revision_response_template.md`. Include: (1) the response and revision made for each Required Revision; (2) adoption or reasons for non-adoption for each Suggested Revision; (3) tracked or colour-marked changes; (4) a cross-reference to new page/paragraph locations. A declined must-fix item stays visible as unresolved for the next review.

### Closing

We encourage you to consider the reviewers' comments carefully and submit a substantially revised manuscript. The revised manuscript will go through another round of review. The panel regards the core design and the pooled diacritic result as sound. The required work is mainly about inference, label validity and claim scope, and most of it can be done with data you already hold.

---

## Part 3: Reviewer Report Summary (Appendix)

| Reviewer | Role | Recommendation | Confidence |
|----------|------|---------------|------------|
| EIC (Journal-Fit Reviewer) | Programme-committee area chair, AI-in-healthcare conference (LNCS) | Major Revision (preliminary signal) | 4 |
| R1 | Biostatistician (diagnostic accuracy, agreement, clustered resampling, LLM-as-judge) | Not stated in card (D1 warn, D3 warn) | No report-level score; per-finding 3–5 |
| R2 | Vietnamese NLP / low-resource medical NLP | Not stated in card (D2 warn) | No report-level score; per-finding 3–4 |
| R3 | Emergency physician and digital-health safety researcher | Not stated in card (D4 warn) | 4 |
| Devil's Advocate | Fixed adversarial seat | N/A — findings only | N/A — per-finding only |

### Journal-Fit Review Report Summary
- Recommendation: Major Revision (preliminary) | Confidence: 4
- Key Point: The scientific core suits an AI-in-healthcare venue and is new. The paper is too long, repeats material across figures, and its folk-first title and abstract contradict its own main finding that diacritic loss is the main risk (EIC:W1, W2).

### Reviewer 1 (Methodology) Summary
- Recommendation: not stated | Confidence: per-finding 3–5
- Key Point: All headline numbers reproduce. The confirmatory inference rests on a 14-cluster percentile bootstrap, the judge is not validated by stratum, the interaction and per-model claims lack intervals, and one Discussion example contradicts Fig. 10 (R1:W1, W2, W4–W6).

### Reviewer 2 (Domain) Summary
- Recommendation: not stated | Confidence: per-finding 3–4
- Key Point: The folk register is LLM-imagined and not anchored in real user text, the lexicon mixes folk-illness labels with ordinary vocabulary, and the headline diacritic effect comes from a full-strip worst case that is not qualified in the abstract (R2:W1–W3).

### Reviewer 3 (Perspective) Summary
- Recommendation: not stated | Confidence: 4
- Key Point: The design is clinically useful and candid. No clinician confirmed that the Vietnamese texts keep their urgency labels, the unsafe-endorsement definition can understate harm, and the guidance to developers is generic (R3:W1, W2, W4).

### Devil's Advocate Summary
- Recommendation: N/A — findings only
- Key Challenge: No unresolved Critical challenge. The strongest counter-argument is that the defensible contribution is a robustness probe of small open models on unaccented Vietnamese, while the folk-illness framing, the trúng gió conclusion and the sycophancy framing go beyond the evidence (DA:M1, M2, M5).

### Schema 6 criterion adapter (`judgement_scale: sprint_contract`)

| Seat | D1 | D2 | D3 | D4 | D5 | D6 |
|---|---|---|---|---|---|---|
| EIC | not_assessed | not_assessed | not_assessed | not_assessed | warn | warn |
| R1 | warn | not_assessed | warn | not_assessed | not_assessed | not_assessed |
| R2 | not_assessed | warn | not_assessed | not_assessed | not_assessed | not_assessed |
| R3 | not_assessed | not_assessed | not_assessed | warn | not_assessed | not_assessed |
| DA | not_assessed | not_assessed | warn | not_assessed | not_assessed | not_assessed |

Values are copied unchanged from the cards and are not translated into EXCEEDS/MEETS scales. Package `calibration_status: NOT_CALIBRATED`. The machine Schema 6 carrier must validate `review_panel_provenance` against the artifact digests listed above.

---

## Part 4: Weakness Sub-Claim Inventory (Step 1b)

Only non-silent positions are listed. Every non-DA seat not listed for a sub-claim is `not-mentioned` (silence, not opposition). DA rows are shown for traceability but excluded from consensus counts. Severity and confidence are transported per parent finding.

| sub_claim_id | parent_weakness | reviewer_id | position | evidence_pointer | severity | confidence |
|---|---|---|---|---|---|---|
| SC-1 | Page limit | EIC | raised | EIC:W1 | major | 4 |
| SC-2 | Title/framing vs main finding | EIC | raised | EIC:W2 | major | 4 |
| SC-2 | (folk-illness framing not carried) | DA | corroborated | DA:M1, DA:M2, strongest counter-argument | major | 4 |
| SC-3 | Figures repeat tables | EIC | raised | EIC:W3 | minor | 4 |
| SC-4 | Overlapping schematics | EIC | raised | EIC:W4 | minor | 4 |
| SC-5 | Abstract length | EIC | raised | EIC:W5 | minor | 4 |
| SC-6 | Causal sentence / no paraphrase control | EIC | raised | EIC:W6 | minor | 3 |
| SC-6 | (same) | R1 | disputed (severity: major vs EIC minor) | R1:W3 | major | 3 |
| SC-6 | (same) | DA | corroborated | DA:M1, DA:m3 | major / minor | 4 |
| SC-7 | Deployment guidance scattered/generic | EIC | raised | EIC:W7 | minor | 4 |
| SC-7 | (same) | R3 | corroborated | R3:W4 | minor | 4 |
| SC-8 | Restoration untested | EIC | raised | EIC:W7, EIC:Q3 | minor | 4 |
| SC-9 | Abstract omits clinical-validity caveat | EIC | raised | EIC:W8 | minor | 4 |
| SC-9 | (same) | R2 | corroborated | R2:W1 minimum fix | major | 4 |
| SC-9 | (same) | R3 | corroborated | R3:W1; R3 Minor 1 | major | 4 |
| SC-10 | Small-cluster bootstrap | R1 | raised | R1:W1 | major | 4 |
| SC-11 | Inference conditional on nine models | R1 | raised | R1:W1 | major | 4 |
| SC-11 | (same) | DA | corroborated | DA:m6 | minor | 3 |
| SC-12 | Judge κ CI / confusion matrix | R1 | raised | R1:W2 | major | 4 |
| SC-13 | Judge stratification + human contrast | R1 | raised | R1:W2 | major | 4 |
| SC-14 | Annotator not hypothesis-blind | R1 | raised | R1:W2 | major | 4 |
| SC-15 | Interaction without CI | R1 | raised | R1:W4 | major | 4 |
| SC-15 | (same) | DA | corroborated | DA:m2 | minor | 4 |
| SC-16 | Per-model/adaptation over-read | R1 | raised | R1:W5 | major | 4 |
| SC-16 | (same) | DA | corroborated | DA:m6 | minor | 3 |
| SC-17 | Liver failure/DKA vs Fig. 10 | R1 | raised | R1:W6 | major | 5 |
| SC-17 | (same) | DA | corroborated | DA:M3 | major | 4 |
| SC-18 | Stance label validation | R1 | raised | R1:W7 | major | 4 |
| SC-18 | (same) | R3 | corroborated | R3:W2 (human check) | major | 4 |
| SC-19 | Remedy figures in abstract | R1 | raised | R1:W7 | major | 4 |
| SC-19 | (same) | R3 | disputed (direction: abstract understates harm) | R3:W2 | major | 4 |
| SC-19 | (same) | DA | corroborated (sides with R1) | DA:m4 | minor | 3 |
| SC-20 | Detectable effect vs Holm | R1 | raised | R1:W8 | minor | 4 |
| SC-21 | Zero-width intervals | R1 | raised | R1:W9 | minor | 4 |
| SC-22 | Over-triage change without CI | R1 | raised | R1:W10 | minor | 3 |
| SC-23 | Mitigation gap at baseline | R1 | raised | R1:W11 | minor | 4 |
| SC-24 | Asthma two cases | R1 | raised | R1:W12 | minor | 5 |
| SC-25 | Reproducibility identifiers | R1 | raised | R1:W13 | minor | 4 |
| SC-26 | Llama denominator | R1 | raised | R1:W14 | minor | 3 |
| SC-27 | Folk register not anchored in real text | R2 | raised | R2:W1 | major | 4 |
| SC-28 | Lexicon mixes categories | R2 | raised | R2:W2 | major | 4 |
| SC-29 | Glosses lack sources | R2 | raised | R2:W2 | major | 4 |
| SC-29 | (same) | R3 | corroborated | R3:W6 | minor | 4 |
| SC-30 | Full-strip worst case unqualified | R2 | raised | R2:W3 | major | 4 |
| SC-31 | Partial-diacritic condition | R2 | raised | R2:W3 | major | 4 |
| SC-32 | Unsourced folk-illness claims | R2 | raised | R2:W4 | minor | 3 |
| SC-33 | Mechanism stated as fact | R2 | raised | R2:W5 | minor | 4 |
| SC-33 | (same) | DA | corroborated | DA:m1 | minor | 4 |
| SC-34 | Competing mechanisms not discussed | R2 | raised | R2:W5 | minor | 4 |
| SC-35 | Related-work gaps | R2 | raised | R2:W6 | minor | 3 |
| SC-36 | Release licence/schema/location | R2 | raised | R2:W7 | minor | 4 |
| SC-36 | (same) | R3 | corroborated | R3:W7 | minor | 3 |
| SC-37 | No clinician urgency check | R3 | raised | R3:W1 | major | 4 |
| SC-38 | Endorsement definition understates harm | R3 | raised | R3:W2 | major | 4 |
| SC-39 | Lenient urgent-tier outcome | R3 | raised | R3:W3 | minor | 4 |
| SC-40 | Over-triage cost not interpreted | R3 | raised | R3:W5 | minor | 3 |
| SC-41 | Lexicon stereotyping risk | R3 | raised | R3:W6 | minor | 4 |
| SC-42 | Release safeguards | R3 | raised | R3:W7 | minor | 3 |
| SC-43 | Care-seeking context missing | R3 | raised | R3:W8 | minor | 3 |
| SC-44 | Trúng gió generalised from one case | DA | raised | DA:M2 | major | 4 |
| SC-45 | *none* labels may drive both rates | DA | raised | DA:M4 | major | 3 |
| SC-46 | Sycophancy framing | DA | raised | DA:M5 | major | 3 |
| SC-47 | Urgent diacritic effects unqualified | DA | raised | DA:m5 | minor | 4 |

Disposition summary over the 4 non-DA seats: CONSENSUS-4: none. CONSENSUS-3: SC-9 (R1 silent). SPLIT: SC-6 (EIC vs R1, severity), SC-19 (R1 vs R3, direction); both arbitrated in Part 1. Corroborated (2/4): SC-7, SC-18, SC-29, SC-36. Single-seat findings: every other EIC/R1/R2/R3 sub-claim. DA-only: SC-44 to SC-47 (no DA CRITICAL).

Surface-form parity check (Step 1c): no sub-claim was down-rated for informal wording or credited for technical phrasing. The two SPLITs were arbitrated on the cited manuscript passages and on seat remit, not on how the findings were worded. Confidence values are carried only as disclosures and were not used as weights.


## Attachment: Suggested-Reference Check (advisory, #1001)

Suggested-reference check (script output, not a reviewer finding; #1001)
Seats read: R2, R3 (complete).

| Seat | # | Reference | Result |
|---|---|---|---|
| R2 | 1 | Jin, Y. et al. (2024) "Better to Ask in English: Cross-Lingual Evaluation of Large Language Models for Healthcare Queries" | Found in an index |
| R2 | 2 | Gebru, T. et al. (2021) "Datasheets for Datasets" doi:10.1145/3458723 | Found in an index |
| R2 | 3 | Bender, E. M. et al. (2018) "Data Statements for Natural Language Processing: Toward Mitigating System Bias and Enabling Better Science" doi:10.1162/tacl\_a\_00041 | Found in an index |
| R3 | 1 | Kleinman, A. (1980) "Patients and Healers in the Context of Culture: An Exploration of the Borderland between Anthropology, Medicine, and Psychiatry" | Found in an index |
| R3 | 2 | Gebru, T. et al. (2021) "Datasheets for Datasets" arXiv:1803.09010 | Found in an index |
| R3 | 3 | Wallace, W. (2022) "The diagnostic and triage accuracy of digital and online symptom checker tools: a systematic review" | Found in an index |

"Found" means an index holds a record with this DOI or arXiv ID and title, or with this title. It does not show that the work supports the recommendation, or that the authors and year are right.


## Attachment: Reviewer Claim Check (advisory, #1002)

The judge answered 42 of 42 findings from 5 reviewers: it marked 2 as contradicted, and 5 cannot be checked from the manuscript alone.

The judge marked these findings as contradicted by the manuscript. The script checked only the words of each quote: that they occur in the manuscript, or, for words the finding quotes, that they do not. The judge gave the locations, and the script did not check them. Read each quote to decide:
- Reviewer 2 · W6: Related work omits cross-lingual health-LLM evaluation and Vietnamese health QA resources
  > “For Vietnamese, VialectBench rewrites standard text into six dialect groups and finds that no model is fully robust” (Related Work, paragraph 'Robustness to how the patient writes')
- Reviewer 3 · W5: Mitigation over-triage cost is not interpreted for deployment
  > “Flash-Lite over-triaged 36--43\\% of controls (average over models: 27\\%), so part of its low under-triage reflects a more cautious operating point.” (Discussion, paragraph 'Which models')

The author decides what to do with each row. This check does not change the decision, the consensus counts, or the Revision Roadmap. The judge is the session model; as this judge, the #1002 contrast test passed Claude Opus 5.5 and Claude Fable 5.1 (gpt-6-astra and Gemini 4 Argon passed it in part one, through other transports); other models are untested.


## Attachment: Acronym Check (advisory, #849)

### Acronym check (advisory; no reply needed)
Coverage: body (partial)
Not in this input: English abstract, Chinese abstract.
Not checked:
- Body, line 522: RQ4 (the initials before its parentheses do not spell it)
- Body, line 1000: MIT (the initials before its parentheses do not spell it)

| Scope | Line | Rule | Acronym | Uses |
|---|---|---|---|---|
| Body | 1 | Defined after first use | LLM | 42 |
| Body | 71 | Not defined | API | 4 |
| Body | 110 | Not defined | RQ1 | 3 |
| Body | 111 | Not defined | RQ2 | 3 |
| Body | 112 | Not defined | RQ3 | 3 |
| Body | 139 | Not defined | CARE | 2 |
| Body | 148 | Not defined | NLP | 3 |
| Body | 160 | Not defined | OK | 4 |
| Body | 163 | Not defined | VM14K | 2 |
| Body | 203 | Not defined | COPD | 3 |
| Body | 311 | Not defined | AC1 | 1 |
| Body | 311 | Not defined | PABAK | 1 |
| Body | 367 | Not defined | AI | 2 |
| Body | 369 | Not defined | GPU | 1 |
| Body | 412 | Not defined | SeaLLM | 13 |
| Body | 511 | Not defined | VyL | 1 |
| Body | 514 | Not defined | SeaL | 1 |
| Body | 984 | Not defined | ACM | 1 |
| Body | 984 | Not defined | FAccT | 1 |
| Body | 997 | Not defined | GPT | 1 |
| Body | 1021 | Not defined | BMJ | 1 |
| Body | 1055 | Not defined | ANSWER | 1 |
| Body | 1055 | Not defined | REMEDY | 2 |
| Body | 1072 | Not defined | ER | 1 |
| Body | 1086 | Not defined | JSON | 1 |
| Body | 1139 | Not defined | GI | 1 |
