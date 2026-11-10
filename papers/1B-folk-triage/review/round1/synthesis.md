# Editorial Decision Package

## Calibration Resolution

`calibration_status: NOT_CALIBRATED`

Current runtime boundary: this package is not upgraded from a candidate or prose-named profile. `PROFILE_MEASURED` remains unavailable until a closed profile artifact and replay validator bind the exact target fields to the completed panel's `execution_topology_sha256`. Every seat also reports `NOT_CALIBRATED`.

## Run Scope Notes

- **Criteria binding**: `criteria_binding_unavailable`. All five Phase 1 cards disclose it, so this is an explicitly unbound run. No venue-alignment claim is made beyond what the Journal-Fit Reviewer (EIC) card states under D6.
- **Step 4b (cross-model blind decision check)**: not active in this run (`ARS_CROSS_MODEL` not set or not consented); skipped, so there is no cross-model comparison.
- **Machine artifacts**: no bound block manifest or base-draft digest was supplied. The closed `revision-roadmap/1.0` JSON (which requires `block_manifest_sha256` and exact `proposed_targets[]` block ids) and the Schema 6 JSON carrier are therefore not emitted here. The Markdown roadmap below carries the reviewer-owned core fields (source order, transported severity, anchor, confidence, obligation, cost scope, closed consequence code) for `scripts/revision_roadmap.py` to bind once a manifest exists. Section locators are given as `proposed target` text only, not as write authority.
- **Manuscript as data**: the manuscript was consulted only to place reviewer findings. No text in it directed at the editor was found.

## Mechanical Audit (sprint contract `reviewer/reviewer_full/v2`)

### Step 1: role-scoped scoring matrix

| Dim | Name | Priority | Eligible roles | Assessed eligible scores | Excluded (ineligible `not_assessed`) | Verdict |
|---|---|---|---|---|---|---|
| D1 | methodology_rigor | mandatory | methodology | R1 (methodology) = warn | EIC, R2, R3, DA | warn |
| D2 | domain_accuracy | mandatory | domain | R2 (domain) = warn | EIC, R1, R3, DA | warn |
| D3 | argumentative_coherence | mandatory | da, methodology | DA = warn; R1 (methodology) = warn | EIC, R2, R3 | warn |
| D4 | cross_disciplinary_relevance | high | perspective | R3 (perspective) = warn | EIC, R1, R2, DA | warn |
| D5 | writing_and_structure | normal | eic | EIC = warn | R1, R2, R3, DA | warn |
| D6 | venue_fit_and_contribution | mandatory | eic | EIC = warn | R1, R2, R3, DA | warn |

No eligible abstentions; no seat declared a block or a fatal block. Every dimension was assessed by at least one eligible seat.

### Step 2: failure conditions

| Condition | Severity | Quantifier | Expression | Evaluation | Fired |
|---|---|---|---|---|---|
| F1 | 95 | any | any mandatory dimension has a fatal block | No fatal block on D1/D2/D3/D6 | false |
| F2 | 90 | any | any mandatory dimension scores 'block' | D1/D2/D3/D6 all warn | false |
| F3 | 70 | majority | two or more mandatory dimensions score 'warn' or worse | D1 (n=1, owner R1 warn) true; D2 (n=1, owner R2 warn) true; D3 (n=2, both DA and R1 warn) true; D6 (n=1, owner EIC warn) true; 4 dimensions ≥ 2 | true |
| F4 | 60 | any | any high-priority dimension scores 'block' | D4 = warn | false |
| F5 | 40 | any | any dimension scores 'warn' or worse | D1–D6 all warn | true |
| F0 | 10 | all | every dimension scores 'pass' | No dimension passes | false |

### Step 3: precedence and decision

Highest-severity fired condition: F3 (70) → action `editorial_decision=major_revision`. F5 (40) also fired and is outranked. The DA card's CRITICAL table is empty, so there are no DA-CRITICAL IDs to adjudicate and no accept-consistency marker applies.

dimension_verdicts: [D1=warn, D2=warn, D3=warn, D4=warn, D5=warn, D6=warn]
fired_conditions: [F3, F5]
da_critical_adjudications: []
editorial_decision=major_revision

---

## Part 1: Editorial Decision Letter

### Manuscript Information
- **Title**: "Trúng gió" or Stroke? Folk-Illness Phrasing and Diacritic Loss Lead LLMs to Under-Triage Vietnamese Health Questions
- **Manuscript ID**: 1b-review-round-1 (panel id)
- **Decision Date**: 2026-11-10
- **Review Round**: Round 1

Dear Author(s),

Thank you for submitting your manuscript titled "'Trúng gió' or Stroke? Folk-Illness Phrasing and Diacritic Loss Lead LLMs to Under-Triage Vietnamese Health Questions". It was reviewed through 5 role-separated review seats: a Journal-Fit Reviewer (EIC), a methodology reviewer (R1), a domain reviewer (R2), a cross-disciplinary reviewer (R3) and a Devil's Advocate (DA). Their execution provenance is reported below and is not reduced to a binary independence claim.

### Review Panel Provenance (#540/#740)

- **Typed artifact**: `papers/1B-folk-triage/review/round1/provenance.json` (`review-panel-provenance/1.0`, validated by the dispatching layer)
- **Artifact SHA-256 (raw bytes)**: `68b9af51981dcc3f0d7b394d3e4689459170639be261baf1b07de3e95548e530`
- **Panel ID**: `1b-review-round-1`
- **Contract SHA-256**: `e9712090d2469fea15a37b8e22d4e137afbcb2bf38d5789939c5df56738ef7af`
- **Normalized manifest SHA-256**: `ac5b6f922841e5ad77de1fdb05213a7bcb5e769df150a3d144aa6be7676b2377`
- **Execution topology SHA-256**: `ba4de2cf08761c7f478a4d22252e1c234f07e2b96cfc887197ff296a1c11b059`
- **Fresh-context scope**: `within_panel_attempt_only` (does not compare retries or prior rounds)

| Seat | Role ID | Actor type | Context ID | Peer outputs visible | Model family | Provider | Human reviewer ID |
|---|---|---|---|---|---|---|---|
| EIC | eic | model | subagent-a611bbb62c60398bc | false | claude | anthropic | unknown (null) |
| R1 | methodology | model | subagent-ad74e132ab576bc1a | false | claude | anthropic | unknown (null) |
| R2 | domain | model | subagent-a90d7ceca36149547 | false | claude | anthropic | unknown (null) |
| R3 | perspective | model | subagent-ac74f673ce0ee6e7b | false | claude | anthropic | unknown (null) |
| DA | da | model | subagent-aeb64b94d9667cd3c | false | claude | anthropic | unknown (null) |

| Provenance axis | Status (`true` / `false` / `unknown`) |
|---|---|
| Role-separated | true |
| Within-panel invocation-context separation | true |
| Blind to peer outputs | true |
| Model-family distinct | false |
| Provider distinct | false |
| Human-reviewer distinct | false |

- **Binary independence claim**: Not computed (`independence_claim: not_computed_from_personas`). Persona and role diversity prove only `role_separated`; this panel is not described as independent, and agreement across seats below is not treated as independent replication.
- **Correlated-error disclosure**: All model-executed review seats used one model family; role separation does not remove correlated-error risk.

### Decision: Major Revision

### Reviewer Summary

| Reviewer | Role | Recommendation (seat signal) | Confidence |
|---|---|---|---|
| Journal-Fit Reviewer (EIC) | Senior PC member, applied NLP / AI-for-health LNCS track | Major Revision | 4 |
| Reviewer 1 | Biostatistician, paired designs and LLM-as-judge | not stated as a label; D1 warn, D3 warn | per-finding 3–4 |
| Reviewer 2 | Vietnamese NLP (diacritic restoration, Vietnamese LLM benchmarks) | not stated as a label; D2 warn ("warn rather than block") | 4 |
| Reviewer 3 | Emergency physician / medical anthropology of SE-Asian folk illness | not stated as a label; D4 warn | 4 (scope disclosure) |
| Devil's Advocate | Fixed adversarial seat | N/A — findings only (0 CRITICAL, 5 MAJOR) | N/A — per-finding only |

Confidence values are self-reported scope disclosures and carry no weight in any count or arbitration below.

### Consensus Analysis

Consensus is counted per sub-claim over the 4 non-DA seats (EIC, R1, R2, R3). A silent seat is not counted as agreement. A difference of severity tier (Major vs Minor) on the same sub-claim is recorded as a SPLIT (severity disagreement) and arbitrated, even when the remedies are compatible. Full inventory: Part 3, Step 1b.

#### Points of Agreement

- **[CONSENSUS-4]**: none. No sub-claim was raised by all four non-DA seats.
- **[CONSENSUS-3]**: none without a severity dispute. The two sub-claims raised by three seats (SC-16, SC-17) carry Major vs Minor severity differences and are therefore handled as SPLITs below.
- **Corroborated findings (2/4, no conflict)**:
  - SC-23: the folk versions are confounded with Southern regional vocabulary (ói, bao tử). R2 W2 and R3 W6, both Major. EIC and R1 silent.
  - SC-30: the claims that trúng gió / cạo gió practice delays stroke care are uncited. R2 W6 and R3 W3, both Minor. EIC and R1 silent.
- **Single-reviewer findings** are retained and assessed against their own criterion and anchor (Part 2). The decision-bearing ones are: SC-3 (EIC W2, novelty beyond effect size), SC-8 (R1 W1, remedy-rate uncertainty), SC-9 (R1 W2, mitigation inference), SC-24 (R2 W3, authenticity of folk language), SC-33 and SC-34 (R3 W1/W2, Vietnam-specific case mix and the vong theo mapping), SC-36 (R3 W4, release safeguards), SC-37 (R3 W5, no clinician review).

#### Points of Disagreement

**Disagreement 1 (SC-2): missing Vietnamese diacritic-restoration literature.** Severity disagreement.
- EIC W2 (Major): the dominant finding is not positioned against restoration and perturbation work.
- R2 W4 (Minor): restoration literature (Náplava et al. 2018; ViLexNorm 2024) is missing and should ground the restoration recommendation.
- **Editor's Resolution**: must_fix. Adding the literature is required. Its weight follows the parent issues: novelty positioning remains the EIC's Major concern (carried separately as SC-3), the citation gap itself is the domain owner's Minor finding. Rationale: expertise first (literature coverage → R2; venue positioning → EIC); the remedies are identical.

**Disagreement 2 (SC-4): "LLMs" in the title generalises beyond the roster.** Severity disagreement.
- EIC W3 (Major): seven of nine models are 1.5–8B open models; Gemini rows are at 0–7%; scope the title/abstract or report open vs API means.
- R1 W5 (Minor): inference covers only these nine models; state the estimand; six of nine are Qwen-lineage.
- DA M3 (MAJOR, not counted) corroborates the scope problem.
- **Editor's Resolution**: must_fix at the claim-scope level (title, abstract, contribution 2). R1's estimand and model-based sensitivity requests stay a separate should_fix item (SC-12). Rationale: the generalisation is a headline-claim issue within the EIC's D6 remit, anchored in Table 3; R1's Minor rating attaches to the statistical-reporting part of its bundle.

**Disagreement 3 (SC-5): remedy-endorsement headline outruns its κ = 0.50 support.** Severity disagreement.
- EIC W4 (Minor): contribution wording ("some models", "up to half") is inconsistent with the abstract and the authors' caveat.
- R1 W1 (Major): the abstract headlines the figures without the κ caveat and without intervals.
- DA M4 (MAJOR, not counted) corroborates, adding that "dangerous" is not established.
- **Editor's Resolution**: must_fix. The wording alignment is required. The interval and confusion-matrix work is the separate single-reviewer item SC-8 (must_fix, R1's D1 remit). Rationale: expertise first. Judge-validity weight belongs to R1; both seats ask for the same textual correction.

**Disagreement 4 (SC-6): per-condition analysis claimed as a contribution with thin support.** Severity disagreement.
- EIC W5 (Minor): add a compact table or drop it from the contribution list.
- R1 W3 (Major): remove it from the contributions and the conclusion, or temper it.
- **Editor's Resolution**: must_fix. Either remove it from the contribution list or support it with the full table required by SC-10. Rationale: the remedies converge; R1's statistical reason (one case per condition) is decisive for whether it can remain a contribution.

**Disagreement 5 (SC-10): are the per-condition findings supported as stated?** Existence disagreement.
- R1 W3 (Major): one case per condition, k/9 answers, the three conditions shown were selected as the largest shifts, no interval or test; the sign-specificity explanation is untested; E08 (trúng gió stroke) is a flagged meaning-check pair.
- R2 S3 presents the same analysis as a strength ("a nuanced linguistic finding"); R3 S4 credits the honest null result for trúng gió.
- **Editor's Resolution**: R1's position prevails on evidential status. The analysis must be labelled exploratory, all 14 conditions reported with intervals, and the sign-specificity explanation framed as a hypothesis. R2's and R3's strengths are preserved as strengths of reporting and framing (no caricature of folk speakers), which survive that relabelling. Rationale: expertise first (whether n = 1 per condition supports a condition-level claim is a methodology question) and evidence first (the selection and sample size are stated in the manuscript's §5.4).

**Disagreement 6 (SC-16): the folk version bundles the folk label with lay register.** Severity disagreement, 3 seats agree on existence.
- R1 W9 (Minor): effects cannot be attributed to the folk label itself; phrase the causal claim as applying to the bundled rewrite.
- R2 W2 (Major) and R3 W6 (Major): the same confound, with dialect added; title, abstract and §6 attribute the effect to folk-illness phrasing.
- DA M2 (MAJOR, not counted) corroborates.
- **Editor's Resolution**: must_fix. Minimum: reword title, abstract, §6 and conclusion so the effect is attributed to the bundled lay/folk rewrite, not to folk labels, and state the confound as a limitation. The label-free lay-wording condition all three seats offer as the stronger option is recommended but not required for this round. Rationale: all three remedies list the rewording as sufficient; the severity difference reflects whether new data are demanded, which no seat makes mandatory.

**Disagreement 7 (SC-17): meaning and naturalness checks were made with an LLM aid.** Severity disagreement, 3 seats agree on existence.
- R1 W9 (Minor): raters used an LLM aid and differed in strictness (κ = 0.15).
- R2 W3 (Major): naturalness scores (4.3, 4.6) are therefore not independent human judgements; have at least one rater judge without LLM assistance.
- R3 W5 (Major): non-clinician raters with an LLM checked wording whose small changes alter clinical severity cues.
- **Editor's Resolution**: must_fix. Disclose the limitation explicitly and report at least one judgement made without LLM assistance (naturalness, per R2). The clinician-acuity check is carried separately as SC-37. Rationale: evidence first. The manuscript's §3.3 states the LLM aid, and two seats tie it to central claims ("the way Vietnamese users actually write"; same-acuity premise).

**Disagreement 8 (SC-21): the diacritic-loss mechanism rests on two anecdotes.** Severity disagreement.
- R1 W12 (Minor): frame it as a hypothesis or test it (does the answer restate the red-flag signs?).
- R2 W1 (Major): no analysis of orthographic ambiguity or tokenisation; test with symptom restatement, restoration, token inflation.
- DA M5 (MAJOR, not counted) adds that the stable ~20-point gap under M1/M2 fits a uniform caution shift equally well.
- **Editor's Resolution**: must_fix. Downgrade the mechanism to a hypothesis in §6 and the conclusion, or support it with one systematic check. Rationale: expertise first. Orthographic ambiguity is R2's core area; both seats accept the hypothesis framing as sufficient.

**Disagreement 9 (SC-28): introduction examples are not in the dataset.** Severity disagreement.
- R2 W6 (Minor): cảm nắng and say rượu are not in the lexicon; nóng trong is mapped inconsistently.
- R3 W1 (Major): dengue, heat stroke and methanol poisoning motivate the paper but are not tested.
- **Editor's Resolution**: must_fix at the wording level (align the introduction examples with the dataset). The broader case-mix gap is R3's single-reviewer item SC-33. Rationale: the textual mismatch is anchored identically by both seats in §1.

**Disagreement 10 (SC-32): lexicon glosses and "can hide" mappings have no stated source.** Severity disagreement.
- R2 W8 (Minor): document who drafted the glosses, whether an LLM was involved and who checked them.
- R3 W2 (Major): cite a source per lay meaning, mark "can hide" as "in this dataset only", have a clinician check it.
- **Editor's Resolution**: must_fix. Report lexicon provenance and mark the "can hide" column as dataset-specific. Per-term sourcing is the expected route; clinician review folds into SC-37. Rationale: the lexicon is a released contribution reused as the M2 glossary (both seats), so provenance bears on D2 and D4.

**Panel observation, not a counted SPLIT (SC-3 vs DA minor (a)).** EIC W2 asks the authors to state how the Vietnamese effect size compares with English perturbation shifts. The DA notes that the existing §6 cross-study "larger" comparison mixes models and metrics. Resolution: SC-3 remains must_fix, and any magnitude comparison must state that the models and metrics differ between studies. Both points come from the cards; neither is new.

**DA findings (MAJOR band; no CRITICAL).** M2, M3, M4 and M5 are corroborated by non-DA seats and merged into SC-16/SC-1, SC-4, SC-5/SC-8 and SC-21/SC-9 respectively. M1 (generic paraphrase instability of small greedy-decoded models as an alternative explanation for the +11 folk effect) has no non-DA corroboration; R1 W8 (rerun variability) is adjacent but distinct. It is retained as a should_fix item (S20). The authors must respond to it.

### Decision Rationale

Under sprint contract `reviewer/reviewer_full/v2` the decision is mechanical. Every dimension scored warn from its eligible seats: D1 and D3 from R1, D2 from R2, D3 from the DA, D4 from R3, D5 and D6 from the EIC. No seat declared a block or a fatal block. Four mandatory dimensions (D1, D2, D3, D6) are at warn under the majority quantifier, so F3 (severity 70) fires and sets Major Revision; F5 (40) also fires and is outranked. No arbitration below changes or softens that action.

The reviewer content is consistent with it. The seats agree that the core design is sound: a within-case paired design with an exact diacritic manipulation, inherited physician labels, over-triage controls, and candid reporting of underpowered per-model contrasts (EIC S1–S4, R1 S1–S6, R2 S1–S2, R3 S1–S4). R1 reproduced the headline percentages from Table 3 (receipts AR1–AR5, AR7). No seat argues that the pooled diacritic or folk effects on emergencies are wrong.

The decision-bearing problems are about what those effects are claimed to show. The title attributes harm to folk-illness phrasing and to "LLMs", while the folk condition bundles the label with lay and regional wording (R1 W9, R2 W2, R3 W6, DA M2) and the effect sits in models of 8B or fewer (EIC W3, R1 W5, DA M3). The mechanism "models misread the signs" rests on two anecdotes (R1 W12, R2 W1, DA M5). Secondary results are headlined without inferential support (R1 W1–W3). The Vietnamese language and clinical constructs (folk-language authenticity, lexicon provenance, clinician review, release safeguards) are under-sourced (R2 W3, W8; R3 W2, W4, W5).

Most required items need rewriting, scoping and added reporting rather than new model runs. A stricter decision is not supported: no seat found a fatal flaw. A lighter one is not available under the contract while four mandatory dimensions remain at warn. The revision returns for re-review.

### Blocking Issues (0–3, immutable source order)

Selection basis: required items raised by at least two non-DA seats and corroborated by a DA MAJOR row, bearing on title or conclusion claims. The 3-row cap is presentational; every must_fix item in Part 2 is required.

| Transport ref | Blocking issue | Source reviewer(s) | Evidence anchor | Resolving roadmap item |
|---|---|---|---|---|
| R4 | Title and abstract generalise to "LLMs" while the effect sits in ≤8B open models | EIC W3, R1 W5, DA M3 | `table: Table 3 (tab:main) — gemini-3.5-flash and flash-lite rows at 0–7% in every version vs Qwen2.5-1.5B at 43/93/86/93%` | REV-SC-4 |
| R10 | Effect attributed to folk-illness phrasing, but the folk version bundles the label with lay and regional wording | R1 W9, R2 W2, R3 W6, DA M2 | `text: §3.2 "The same facts in everyday wording (\vi{ói} for vomiting, \vi{tào tháo đuổi} for diarrhoea), plus the folk label a family would use"` | REV-SC-16 |
| R12 | Diacritic-loss mechanism ("models misread the signs") asserted from two anecdotes | R1 W12, R2 W1, DA M5 | `text: §6 Discussion "The emergency is lost before any triage reasoning starts."` | REV-SC-21 |

---

## Part 2: Revision Roadmap

Source order: fixed seat order EIC, R1, R2, R3, DA, then finding ordinal, then sub-claim ordinal. `SC-n` ids were assigned in that order, so the tables follow it. `R<n>` and `S<n>` are transport references, not ranks. Item ids are `REV-SC-<n>` (or `REV-DA-<id>` for DA-only items). Severity, anchor and confidence are transported from the driving card(s).

### Required Revisions (Must Fix)

| Transport ref | Revision Item | Sub-Claim(s) | Severity | Evidence Anchor | Confidence | Source | Obligation class | Cost scope | Bounded consequence |
|---|---|---|---|---|---|---|---|---|---|
| R1 | Retitle and reorder the introduction/contributions so diacritic loss leads and the folk effect and non-additivity are stated as found | SC-1 | major (EIC W1) | `text: §8 Conclusion "The main problem was not folk labels such as"` | 5 — EIC | EIC (+DA M2) | must_fix | section: title, abstract, §1 | claim_scope_unsupported → claim: title |
| R2 | Add Vietnamese diacritic-restoration and unaccented-text literature | SC-2 | major (EIC W2); minor (R2 W4) | `absence: §2 Related Work — expected Vietnamese diacritic-restoration work; checked §2, §6, §7, all \cite keys` | 4 — EIC; 5 — R2 | EIC, R2 | must_fix | section: §2 Related Work | evidence_gap_remains → section: §2 |
| R3 | State what is new beyond a larger surface-perturbation effect, with any cross-study magnitude comparison qualified | SC-3 | major (EIC W2) | `absence: §2 and §6 — expected explicit contrast with English typo/style perturbation magnitudes; checked §2, §6, §7, every \cite key` | 4 — EIC | EIC | must_fix | section: §2, §6 | claim_scope_unsupported → claim: novelty statement §1 |
| R4 | Scope title, abstract and contribution 2 to the models tested; report open vs API means | SC-4 | major (EIC W3); minor (R1 W5) | `table: Table 3 (tab:main) — Gemini rows 0–7% vs Qwen2.5-1.5B 43/93/86/93%` | 4 — EIC; 4 — R1 | EIC, R1 (+DA M3) | must_fix | section: title, abstract, §1 | claim_scope_unsupported → claim: title "LLMs" |
| R5 | Align remedy-endorsement wording across abstract and contributions and carry the κ = 0.50 caveat | SC-5 | minor (EIC W4); major (R1 W1) | `text: §1 contribution 2 "Some models endorse dangerous folk remedies in up to half of emergencies."` | 5 — EIC; 4 — R1 | EIC, R1 (+DA M4) | must_fix | sentence: abstract, §1 contribution 2 | claim_scope_unsupported → claim: contribution 2 |
| R6 | Remove the per-condition analysis from the contribution list or support it with the full table (R9) | SC-6 | minor (EIC W5); major (R1 W3) | `text: §1 contribution 3 "A per-condition analysis and a mitigation study."` | 4 — EIC; 4 — R1 | EIC, R1 | must_fix | sentence: §1 contribution 3 | claim_scope_unsupported → claim: contribution 3 |
| R7 | Give Wilson CIs for remedy-endorsement rates, the remedy-stance confusion matrix, and a human-only or judge-corrected sensitivity estimate | SC-8 | major (R1 W1) | `text: "and in up to half for one model"` | 4 — R1 | R1 (+DA M4) | must_fix | re_analysis: §5.3 RQ3 | evidence_gap_remains → claim: RQ3 endorsement rates |
| R8 | Add paired case-level bootstrap CIs for the RQ4 under-triage, gap and over-triage changes; state that the gap did not change; soften the abstract | SC-9 | major (R1 W2) | `table: Table 4 (tab:mit), gap and over columns across base, m1, m2 rows` | 4 — R1 | R1 (+DA M5) | must_fix | re_analysis: §5.5 RQ4, Table 4 | evidence_gap_remains → table: Table 4 |
| R9 | Label the per-condition analysis exploratory, report all 14 conditions with intervals, frame sign-specificity as a hypothesis | SC-10 | major (R1 W3) | `text: "The best-known folk label (\vi{trúng gió} for stroke) does not mislead the models"` | 4 — R1 | R1 (R2 S3, R3 S4 disputed) | must_fix | re_analysis: §5.4 | claim_scope_unsupported → section: §5.4 and conclusion |
| R10 | Attribute RQ1 to the bundled lay/folk rewrite, not to folk labels; state the confound in Limitations | SC-16 | minor (R1 W9); major (R2 W2, R3 W6) | `text: §3.2 "The same facts in everyday wording (\vi{ói} for vomiting, \vi{tào tháo đuổi} for diarrhoea), plus the folk label a family would use"` | 3 — R1; 4 — R2; 3 — R3 | R1, R2, R3 (+DA M2) | must_fix | section: title, abstract, §6, §7, §8 | claim_scope_unsupported → claim: "folk-illness phrasing" effect |
| R11 | Disclose the LLM aid in the meaning/naturalness checks as a limitation and report at least one judgement made without LLM assistance | SC-17 | minor (R1 W9); major (R2 W3, R3 W5) | `text: §3.3 "Both used an LLM as an aid and reviewed its output."` | 3 — R1; 4 — R2; 4 — R3 | R1, R2, R3 | must_fix | new_data: §3.3 rater judgement | evidence_gap_remains → section: §3.3 |
| R12 | Present the diacritic-loss mechanism as a hypothesis, or support it with a systematic check (symptom restatement by version, restoration rerun, token inflation) | SC-21 | minor (R1 W12); major (R2 W1) | `text: §6 Discussion "The emergency is lost before any triage reasoning starts."` | 3 — R1; 4 — R2 | R1, R2 (+DA M5) | must_fix | section: §6, §8 | claim_scope_unsupported → claim: mechanism in §6/§8 |
| R13 | State the Southern-regional skew of folk vocabulary as a confound; report rater region if known | SC-23 | major (R2 W2, R3 W6) | `text: Fig. 3 (fig:example) "Ông buồn nôn và nôn." versus "Ông buồn nôn, ói."` | 4 — R2; 3 — R3 | R2, R3 | must_fix | section: §3.2, §7 | interpretive_ambiguity_remains → claim: RQ1 interpretation |
| R14 | Attest lexicon terms in real Vietnamese patient text (e.g. ViMQ) or tone down "how users actually write" claims | SC-24 | major (R2 W3) | `text: §3.3 "Both used an LLM as an aid and reviewed its output."` | 4 — R2 | R2 | must_fix | section: §3.4, §6, §8 | claim_scope_unsupported → claim: "actually write" |
| R15 | Align the introduction's motivating examples (dengue, heat stroke, methanol; cảm nắng, say rượu, nóng trong) with the dataset and lexicon | SC-28 | minor (R2 W6); major (R3 W1) | `text: §1 Introduction "can hide dengue warning signs, heat stroke or methanol poisoning"` | 3 — R2; 4 — R3 | R2, R3 | must_fix | sentence: §1 | claim_scope_unsupported → section: §1 |
| R16 | Report lexicon provenance (who drafted, LLM involvement, who checked, sources) and mark "can hide" as dataset-specific | SC-32 | minor (R2 W8); major (R3 W2) | `table: Appendix B, Table tab:lexicon, columns "Lay meaning" and "Can hide (this set)"` | 3 — R2; 4 — R3 | R2, R3 | must_fix | section: §3.4, Appendix B | reader_traceability_reduced → table: tab:lexicon |
| R17 | Name the absence of Vietnam-specific emergencies (dengue, heat illness, methanol, snakebite, pesticide) in Limitations, or add a clinician-labelled set | SC-33 | major (R3 W1) | `text: §1 "can hide dengue warning signs, heat stroke or methanol poisoning"` | 4 — R3 | R3 | must_fix | section: §7 Limitations | claim_scope_unsupported → claim: practical claim about Vietnamese users |
| R18 | Rephrase or remove the vong theo → early psychotic disorder mapping, framing it as an explanatory model | SC-34 | major (R3 W2) | `table: Appendix B, Table tab:lexicon, columns "Lay meaning" and "Can hide (this set)"` | 4 — R3 | R3 | must_fix | sentence: Appendix B lexicon row | editorial_conformance_unmet → table: tab:lexicon |
| R19 | Add a datasheet/data statement: evaluation-only use, provenance flag per remedy (documented vs LLM-drafted), harm labels on unsafe outputs, content warning; extend the Ethics Statement | SC-36 | major (R3 W4) | `absence: Ethics Statement and release sentences — expected data-release risk analysis, intended-use restriction, provenance and harm labels; checked Ethics Statement, Limitations, Conclusion, §3.2` | 4 — R3 | R3 | must_fix | other (surface_id: release_datasheet): released dataset documentation + Ethics Statement | reporting_requirement_unmet → dataset: released cases, remedies, outputs |
| R20 | Have a Vietnamese emergency or primary-care physician confirm source acuity for the 24 emergency and urgent pairs, and report the result | SC-37 | major (R3 W5) | `text: §7 Limitations "were not re-reviewed by a clinician for the Vietnamese versions"` | 4 — R3 | R3 | must_fix | new_data: clinician check of 24 pairs | evidence_gap_remains → dataset: 24 emergency/urgent pairs |

### Required Item Details

**R1: Title and framing foreground the effect the results downplay**
- **Problem**: The title and introduction lead with trúng gió and folk phrasing; the results say trúng gió did not mislead models, the folk effect is +11 and only 3 points without diacritics, and diacritic loss is the main driver.
- **Source**: EIC W1 (Major); DA M2 corroborates.
- **Requirement**: Retitle so diacritic loss leads; reorder the introduction and contribution list; state non-additivity in the abstract.
- **Acceptance criteria**: Title, abstract, contribution list and conclusion name diacritic loss as the main driver and report the folk effect and the trúng gió null result consistently with §5.

**R2: Diacritic-restoration literature missing**
- **Problem**: §2 cites one general diacritics paper and no Vietnamese restoration or normalisation work, though §6 recommends restoration.
- **Source**: EIC W2 (Major), R2 W4 (Minor); arbitrated in Disagreement 1.
- **Requirement**: Add a related-work paragraph on Vietnamese diacritic restoration and unaccented-input normalisation (R2 lists Náplava et al. 2018 and ViLexNorm 2024 as leads, to be verified by the authors).
- **Acceptance criteria**: §2 cites and discusses Vietnamese diacritic-restoration and normalisation work, and the §6 restoration recommendation refers to it.

**R3: Novelty beyond effect size not argued**
- **Problem**: The largest effect is a surface perturbation close to English typo/style work; the paper does not state what is new beyond its size.
- **Source**: EIC W2 (Major); DA minor point (a) on cross-study comparison noted in the panel observation.
- **Requirement**: State explicitly what the Vietnamese setting adds; any magnitude comparison with English work must note that models and metrics differ.
- **Acceptance criteria**: §1 or §2 contains an explicit novelty statement relative to English perturbation work, and every cross-study magnitude comparison is qualified for differing models and metrics.

**R4: "LLMs" overgeneralises**
- **Problem**: Seven of nine models are 1.5–8B open models; both Gemini models stay at 0–7% under-triage; the mean depends on the roster.
- **Source**: EIC W3 (Major), R1 W5 (Minor); DA M3; arbitrated in Disagreement 2.
- **Requirement**: Scope title, abstract and contribution 2 to the models tested and report the mean separately for open and API models (or extend the roster).
- **Acceptance criteria**: No headline sentence attributes the effect to LLMs in general, and open-model and API-model means are reported separately.

**R5: Remedy headline wording**
- **Problem**: Contribution 2 says "some models" endorse dangerous remedies in "up to half" of emergencies; the abstract says one model; Results call the figures secondary because κ = 0.50.
- **Source**: EIC W4 (Minor), R1 W1 (Major); DA M4; arbitrated in Disagreement 3.
- **Requirement**: Make the wording identical in meaning across abstract and contributions and carry the moderate-agreement caveat wherever the figure appears.
- **Acceptance criteria**: Every mention of remedy-endorsement rates names the model(s) correctly and states the κ = 0.50 caveat or labels the figure secondary.

**R6: Per-condition analysis as a contribution**
- **Problem**: Contribution 3 lists a per-condition analysis that §5.4 supports with three bullets and no table.
- **Source**: EIC W5 (Minor), R1 W3 (Major); arbitrated in Disagreement 4.
- **Requirement**: Drop it from the contribution list, or keep it only with the full exploratory table required by R9.
- **Acceptance criteria**: The contribution list either omits the per-condition analysis or describes it as exploratory with a cross-reference to the full 14-condition table.

**R7: Remedy-rate uncertainty**
- **Problem**: Endorsement rates (10% overall; 50% and 60% for single models, n = 14 and n = 10) have no intervals; the remedy label was validated on 32 answers at κ = 0.50.
- **Source**: R1 W1 (Major).
- **Requirement**: Wilson CIs for each rate, remedy-stance confusion matrix, and a judge-corrected or human-only sensitivity estimate (R1 suggests double-labelling the 216 serious-case folk_rem answers).
- **Acceptance criteria**: §5.3 reports a CI for every endorsement rate, the confusion matrix, and a sensitivity estimate whose direction is stated.

**R8: Mitigation inference**
- **Problem**: RQ4 conclusions (halving under-triage, ~20-point gap, +6–8 over-triage, M2 no better than M1) rest on four models, one run, no CI; per-model rows move in different directions; the base gap is already ~20 points.
- **Source**: R1 W2 (Major); DA M5 touches the same table.
- **Requirement**: Apply the paired case-level bootstrap (prompt × version) used for RQ1/RQ2; report CIs for the under-triage, gap and over-triage changes; say explicitly that the gap did not change; soften the abstract.
- **Acceptance criteria**: Table 4 or the RQ4 text gives CIs for all three changes, and the abstract's mitigation sentence matches them.

**R9: Per-condition findings under-supported**
- **Problem**: One case per condition (k/9 answers), conditions selected as the largest shifts, no interval; sign-specificity explanation untested; E08 is a flagged meaning-check pair.
- **Source**: R1 W3 (Major); R2 S3 and R3 S4 disputed; arbitrated in Disagreement 5.
- **Requirement**: Label the analysis exploratory, report all 14 conditions with intervals, frame sign-specificity as a hypothesis, and temper the conclusion.
- **Acceptance criteria**: §5.4 shows all 14 conditions with intervals under an "exploratory" label, and neither §6 nor the conclusion states the sign-specificity account as a finding.

**R10: Folk label bundled with lay register**
- **Problem**: The folk version adds a label, replaces clinical terms with colloquial ones and uses regionally marked words; only two label-free lay controls exist; the title attributes the effect to folk-illness phrasing.
- **Source**: R1 W9 (Minor), R2 W2 (Major), R3 W6 (Major); DA M2; arbitrated in Disagreement 6.
- **Requirement**: Reword claims to "lay/folk wording" (the bundled rewrite) throughout and state the confound in Limitations. A label-free lay-wording version for emergency and urgent cases is recommended, not required.
- **Acceptance criteria**: No sentence attributes the RQ1 effect to folk labels alone, and §7 names the label/register confound.

**R11: LLM-aided human checks**
- **Problem**: Both native-speaker raters used an LLM aid for equivalence and naturalness (κ = 0.15 on equivalence), so these are not independent human judgements.
- **Source**: R1 W9 (Minor), R2 W3 (Major), R3 W5 (Major); arbitrated in Disagreement 7.
- **Requirement**: State the limitation explicitly and obtain at least one naturalness judgement made without LLM assistance.
- **Acceptance criteria**: §3.3 reports at least one rater's naturalness judgement made without LLM assistance and names the LLM-aid limitation.

**R12: Diacritic mechanism**
- **Problem**: "Models misread the signs" and "a system prompt cannot fix this" rest on two hand-picked answers; orthographic ambiguity and tokenisation are not analysed; the mitigation gap fits a uniform caution shift equally well (DA).
- **Source**: R1 W12 (Minor), R2 W1 (Major); DA M5; arbitrated in Disagreement 8.
- **Requirement**: Present the mechanism as a hypothesis, or test it (e.g. whether answers restate the key red-flag signs by version; a restoration rerun; token-count inflation).
- **Acceptance criteria**: §6 and the conclusion either label the mechanism a hypothesis or cite a systematic per-version analysis that supports it.

**R13: Regional dialect confound**
- **Problem**: Folk versions use Southern forms (ói, bao tử) while clinical versions use standard or Northern forms.
- **Source**: R2 W2 (Major), R3 W6 (Major); corroborated finding.
- **Requirement**: State the regional skew as a confound, say which variety was targeted, and report rater region if known.
- **Acceptance criteria**: §3.2 or §7 names the regional variety of the folk versions and treats dialect as a confound of the folk contrast.

**R14: Authenticity of folk language**
- **Problem**: An LLM drafted the folk versions, a single non-dialectologist editor revised them, and no attestation in real user text is given, yet §6 and the conclusion claim to measure how Vietnamese users actually write.
- **Source**: R2 W3 (Major).
- **Requirement**: Report attestation or corpus frequency for each lexicon term in real Vietnamese patient text (R2 points to ViMQ), or tone down the "actually write" claims.
- **Acceptance criteria**: Either per-term attestation is reported, or no sentence claims the folk versions represent how users actually write.

**R15: Introduction examples**
- **Problem**: §1 motivates with cảm nắng, say rượu and dengue/heat stroke/methanol; none is tested, and nóng trong is linked to dengue in §1 but to DKA and pyelonephritis in the lexicon.
- **Source**: R2 W6 (Minor), R3 W1 (Major); arbitrated in Disagreement 9.
- **Requirement**: Use motivating examples that occur in the dataset, or mark the others explicitly as untested.
- **Acceptance criteria**: Every folk term and condition named in §1 either appears in the dataset/lexicon or is explicitly labelled as outside the tested set.

**R16: Lexicon provenance**
- **Problem**: Glosses and "can hide" mappings have no stated source, drafter or review step; the lexicon is released and reused as the M2 glossary.
- **Source**: R2 W8 (Minor), R3 W2 (Major); arbitrated in Disagreement 10.
- **Requirement**: Document who drafted it, LLM involvement, who checked it and the sources used; mark "can hide" as "in this dataset only".
- **Acceptance criteria**: §3.4 or Appendix B states the lexicon's authorship, LLM involvement, review and sources, and the column header limits "can hide" to this dataset.

**R17: Vietnam-specific case mix**
- **Problem**: Emergencies are US symptom-checker vignettes; Vietnam-specific emergencies that folk labels most plausibly delay are not tested.
- **Source**: R3 W1 (Major).
- **Requirement**: At minimum name the gap in Limitations; optionally add clinician-labelled Vietnam-specific vignettes.
- **Acceptance criteria**: §7 names the absence of Vietnam-specific emergencies and limits the practical claim accordingly, or such cases are added with a named clinician labeller.

**R18: vong theo mapping**
- **Problem**: Mapping vong theo ("followed by a wandering spirit") to "early psychotic disorder" medicalises a spiritual idiom and could be read as labelling its users psychotic.
- **Source**: R3 W2 (Major).
- **Requirement**: Rephrase as an explanatory model or remove the mapping.
- **Acceptance criteria**: The released lexicon no longer maps vong theo to a psychiatric diagnosis without explanatory-model framing.

**R19: Release safeguards**
- **Problem**: The release includes LLM-drafted remedies (28 undocumented) and model answers endorsing unsafe practices; the Ethics Statement covers only patient data.
- **Source**: R3 W4 (Major).
- **Requirement**: Datasheet or data statement with evaluation-only use, per-item provenance flags, harm labels and a content warning; one Ethics paragraph on release risk.
- **Acceptance criteria**: The release ships a datasheet with the four elements, and the Ethics Statement discusses release risks.

**R20: Clinician review of Vietnamese cases**
- **Problem**: The Vietnamese wording was produced by an LLM and non-clinicians; small wording changes alter severity cues (U10, E03 examples cited by R3).
- **Source**: R3 W5 (Major).
- **Requirement**: One Vietnamese emergency or primary-care physician confirms that each of the 24 emergency and urgent pairs keeps its source acuity.
- **Acceptance criteria**: The manuscript reports the clinician check for all 24 pairs, with any changed pairs listed.

### Suggested Revisions (Should Fix / Consider)

| Transport ref | Revision Item | Sub-Claim(s) | Severity | Evidence Anchor | Confidence | Source | Obligation class | Cost scope | Bounded consequence |
|---|---|---|---|---|---|---|---|---|---|
| S1 | Split the §3.3 meaning-check paragraph (procedure / agreement / adjudication) | SC-7 | minor (EIC W6) | `text: §3.3 "so the raters differed in strictness and rarely agreed on which pairs to flag"` | 4 — EIC | EIC | should_fix | section: §3.3 | reader_traceability_reduced → section: §3.3 |
| S2 | Report judge confusion matrices and agreement by version, model family (incl. same-family Gemini), and for a stratified mitigation sample | SC-11 | minor (R1 W4) | `text: "Judge--human agreement on triage was $\kappa=0.90$ over the four labels and $\kappa=0.94$ for the binary emergency/not decision"` | 4 — R1 | R1 (+DA minor b) | should_fix | re_analysis: §4 judge validation | evidence_gap_remains → claim: judge validity by stratum |
| S3 | State the pooled estimand; add a crossed random-effects GLMM or BCa/cluster-wild interval; report the effect excluding Qwen-lineage models | SC-12 | minor (R1 W5) | `text: "The mean effect over models uses a case-level bootstrap that resamples cases for all models together"` | 4 — R1 | R1 | should_fix | re_analysis: §4 Statistics | method_reproducibility_unresolved → section: §4 Statistics |
| S4 | Estimate the RQ2 interaction contrast with a bootstrap CI | SC-13 | minor (R1 W6) | `text: "The two changes do not add up."` | 4 — R1 | R1 | should_fix | re_analysis: §5.2 | evidence_gap_remains → claim: "do not compound" |
| S5 | State the Table 4 over-triage denominator and pooled versions | SC-14 | minor (R1 W7) | `absence: Table 4 caption and RQ4 text — expected N per over-triage cell and pooled versions; checked Table 4 caption, RQ4 bullets, Measures, Fig. 4 axes` | 4 — R1 | R1 | should_fix | sentence: Table 4 caption | reader_traceability_reduced → table: Table 4 |
| S6 | Report rerun disagreement share and paired CI under sampling; repeat a subset of API calls | SC-15 | minor (R1 W8) | `text: "With five samples at temperature 0.7 for Qwen2.5-7B and SeaLLMs, majority-vote under-triage kept the same direction"` | 3 — R1 | R1 | should_fix | re_analysis: §5.6 | evidence_gap_remains → claim: decoding robustness |
| S7 | Report whether the two flagged cases edited after rating were re-rated | SC-18 | minor (R1 W9) | `text: "Any change in the advice is then caused by the wording, not by missing information"` | 3 — R1 | R1 | should_fix | sentence: §3.3 | reporting_requirement_unmet → section: §3.3 |
| S8 | Add model revision identifiers, bootstrap seed, and an analysis-code release statement | SC-19 | minor (R1 W10) | `absence: Section 4 and Table 2 — expected revision identifiers, seed, code release; checked Table 2 caption, Models, Prompting, Statistics, Abstract and Conclusion` | 4 — R1 | R1 | should_fix | sentence: Table 2, release statement | method_reproducibility_unresolved → table: Table 2 |
| S9 | Report none-label rates by model and version and main contrasts with none excluded | SC-20 | minor (R1 W11) | `text: "answers labelled \emph{none} count as under-triage"` | 4 — R1 | R1 | should_fix | re_analysis: §4 Measures, §5 | interpretive_ambiguity_remains → claim: under-triage outcome |
| S10 | State the number of tests in the Holm family | SC-22 | minor [SEVERITY-SOURCE: letter-fallback] | `text: "smallest corrected $p=0.14$"` | 4 — R1 [CONFIDENCE-SOURCE: report-level] | R1 (note on AR8) | consider | sentence: §4 Statistics | method_reproducibility_unresolved → section: §4 Statistics |
| S11 | Source the claim that Vietnamese is often typed without diacritics | SC-25 | minor (R2 W4) | `absence: §2 Related Work, robustness paragraph — expected Vietnamese restoration/normalisation work; checked §2, §6, Conclusion, all citation keys` | 5 — R2 | R2 | should_fix | sentence: §1 | evidence_gap_remains → claim: typing-without-diacritics prevalence |
| S12 | Specify the đ/Đ mapping and any words left accented in the _nd procedure | SC-26 | minor (R2 W5) | `text: §3.2 "Produced automatically by Unicode decomposition."` | 5 — R2 | R2 | should_fix | sentence: §3.2 | method_reproducibility_unresolved → section: §3.2 |
| S13 | Describe _nd as a controlled worst case, not as how users type | SC-27 | minor (R2 W5) | `text: §3.2 "Produced automatically by Unicode decomposition."` | 5 — R2 | R2 (+DA unexamined premise) | should_fix | sentence: §3.2, §6 | claim_scope_unsupported → claim: ecological validity of _nd |
| S14 | Distinguish ordinary lay names (đau mắt đỏ, giời leo, tăng xông, …) from explanatory folk-illness categories in the lexicon | SC-29 | minor (R2 W6) | `text: §1 Introduction "can hide dengue warning signs, heat stroke or methanol poisoning"` | 3 — R2 | R2 | consider | section: §3.4, Appendix B | interpretive_ambiguity_remains → table: tab:lexicon |
| S15 | Cite evidence for, or soften, the claim that trúng gió / cạo gió practice delays stroke care | SC-30 | minor (R2 W6, R3 W3) | `text: §1 "delays care during the hours when stroke treatment works"` | 3 — R2; 4 — R3 | R2, R3 | should_fix | sentence: §1 | evidence_gap_remains → claim: care-delay claim |
| S16 | Limit the language-adaptation conclusion to the one matched base/adapted pair | SC-31 | minor (R2 W7) | `text: §6 Discussion "Language adaptation therefore did not make these models more robust to how Vietnamese users actually write."` | 4 — R2 | R2 (+DA minor d) | should_fix | sentence: §6 | claim_scope_unsupported → claim: language-adaptation conclusion |
| S17 | Place folk labels in an explanatory-models frame so risk sits with model behaviour, not users' culture | SC-35 | minor (R3 W3) | `text: §1 "delays care during the hours when stroke treatment works"` | 4 — R3 | R3 | consider | section: §1, §6 | interpretive_ambiguity_remains → section: §1 framing |
| S18 | Sensitivity analysis counting untimed "soon" as unsafe on urgent cases, and over-triage limited to self-care and one-week controls | SC-38 | minor (R3 W7) | `text: §4 Measures "where both a visit within 24--48 hours and emergency care are correct"` | 4 — R3 | R3 | should_fix | re_analysis: §5 urgent and control outcomes | evidence_gap_remains → claim: urgent under-triage |
| S19 | Add a safety caveat to the restoration recommendation and note the health-system cost of the M1/M2 over-triage rise | SC-39 | minor (R3 W8) | `text: §6 "Restoring diacritics before the text reaches the model is a cheap step that deserves testing"` | 3 — R3 | R3 | should_fix | sentence: §6 | interpretive_ambiguity_remains → claim: restoration recommendation |
| S20 | Address generic paraphrase instability as an alternative explanation for the +11 folk effect (neutral clinical-paraphrase control, or matching rewording) | — | major (DA M1, MAJOR band) | `text: §1 "Any change in the advice is then caused by the wording, not by missing information."; §5.6 "43\% vs 29\% for Qwen2.5-7B"` | 4 — DA | DA | should_fix | new_data: neutral-paraphrase condition, or section: §5.1/§6 | interpretive_ambiguity_remains → claim: RQ1 folk effect |
| S21 | Qualify the §6 claim that the Vietnamese effect is "larger" than in English work (different models and metrics) | — | minor (DA minor a) [SEVERITY-SOURCE: letter-fallback] | no typed anchor on the DA card; DA commentary locates it in the §6 Discussion "larger" comparison | 4 — DA [CONFIDENCE-SOURCE: report-level] | DA | consider | sentence: §6 | claim_scope_unsupported → claim: cross-study comparison |
| S22 | Note that Gemini's near-zero under-triage coincides with 33–39% over-triage of controls | — | minor (DA minor e) [SEVERITY-SOURCE: letter-fallback] | `table: Table 3 (tab:main), gemini-3.5-flash and gemini-3.5-flash-lite rows` | 4 — DA [CONFIDENCE-SOURCE: report-level] | DA | consider | sentence: §5.1, §6 | interpretive_ambiguity_remains → claim: "barely affected" |

### Source-Traceability Checklist

- [ ] R1 — obligation `must_fix`: retitle and reorder framing (SC-1)
- [ ] R2 — obligation `must_fix`: add diacritic-restoration literature (SC-2)
- [ ] R3 — obligation `must_fix`: argue novelty beyond effect size (SC-3)
- [ ] R4 — obligation `must_fix`: scope "LLMs" to models tested (SC-4)
- [ ] R5 — obligation `must_fix`: align remedy headline wording (SC-5)
- [ ] R6 — obligation `must_fix`: per-condition contribution claim (SC-6)
- [ ] S1 — obligation `should_fix`: split §3.3 paragraph (SC-7)
- [ ] R7 — obligation `must_fix`: remedy-rate CIs and confusion matrix (SC-8)
- [ ] R8 — obligation `must_fix`: RQ4 inference (SC-9)
- [ ] R9 — obligation `must_fix`: per-condition analysis exploratory with intervals (SC-10)
- [ ] S2 — obligation `should_fix`: judge agreement by stratum (SC-11)
- [ ] S3 — obligation `should_fix`: estimand and model-based check (SC-12)
- [ ] S4 — obligation `should_fix`: interaction contrast CI (SC-13)
- [ ] S5 — obligation `should_fix`: Table 4 denominator (SC-14)
- [ ] S6 — obligation `should_fix`: rerun variability (SC-15)
- [ ] R10 — obligation `must_fix`: folk label vs register attribution (SC-16)
- [ ] R11 — obligation `must_fix`: LLM-aided checks disclosure plus unaided judgement (SC-17)
- [ ] S7 — obligation `should_fix`: re-rating of edited flagged cases (SC-18)
- [ ] S8 — obligation `should_fix`: reproducibility identifiers (SC-19)
- [ ] S9 — obligation `should_fix`: none-label reporting (SC-20)
- [ ] R12 — obligation `must_fix`: diacritic mechanism as hypothesis or tested (SC-21)
- [ ] S10 — obligation `consider`: Holm family size (SC-22)
- [ ] R13 — obligation `must_fix`: regional dialect confound (SC-23)
- [ ] R14 — obligation `must_fix`: folk-language attestation (SC-24)
- [ ] S11 — obligation `should_fix`: source for unaccented-typing prevalence (SC-25)
- [ ] S12 — obligation `should_fix`: đ/Đ handling (SC-26)
- [ ] S13 — obligation `should_fix`: _nd as worst case (SC-27)
- [ ] R15 — obligation `must_fix`: align introduction examples (SC-28)
- [ ] S14 — obligation `consider`: lay names vs folk categories (SC-29)
- [ ] S15 — obligation `should_fix`: care-delay claim sourcing (SC-30)
- [ ] S16 — obligation `should_fix`: language-adaptation scope (SC-31)
- [ ] R16 — obligation `must_fix`: lexicon provenance (SC-32)
- [ ] R17 — obligation `must_fix`: Vietnam-specific case-mix limitation (SC-33)
- [ ] R18 — obligation `must_fix`: vong theo mapping (SC-34)
- [ ] S17 — obligation `consider`: explanatory-models framing (SC-35)
- [ ] R19 — obligation `must_fix`: release datasheet and Ethics paragraph (SC-36)
- [ ] R20 — obligation `must_fix`: clinician acuity check (SC-37)
- [ ] S18 — obligation `should_fix`: untimed "soon" sensitivity (SC-38)
- [ ] S19 — obligation `should_fix`: restoration safety caveat (SC-39)
- [ ] S20 — obligation `should_fix`: paraphrase-instability alternative (DA M1)
- [ ] S21 — obligation `consider`: cross-study comparison qualifier (DA minor a)
- [ ] S22 — obligation `consider`: Gemini operating point (DA minor e)

Counts: must_fix 20, should_fix 17, consider 5 (42 items).

### Journal-Supplied Deadline
- **Exact deadline from source letter**: NOT PROVIDED. No deadline or work estimate is inferred.

### Response Letter Instructions
Please respond to every item above using `templates/revision_response_template.md`: a response and change description for each Required item, an adopted / not-adopted reason for each Suggested item, tracked changes in the revised manuscript, and a table of new section and page locations. A decision not to address an item is recorded as such; it is not treated as resolved. Author triage is collected later in a separate sidecar.

### Closing
We encourage you to consider the reviewers' comments carefully and submit a substantially revised manuscript. The revised manuscript will undergo another round of review.

---

## Part 3: Appendix

### Step 1a: Reviewer Summary Matrix

| Dimension | Journal-Fit Reviewer (EIC) | R1 (Methodology) | R2 (Domain) | R3 (Perspective) |
|---|---|---|---|---|
| Overall recommendation | Major Revision | no label; D1 warn, D3 warn | no label; D2 warn, "warn rather than block" | no label; D4 warn |
| Confidence / scope | 4; did not audit statistics or clinical content | 3–4 per finding; Vietnamese naturalness outside competence | 4; clinical triage outside competence | 4; low for quantitative analysis |
| Key strengths | S1–S5: paired design, controls, licensed release, candid nulls, clear gap | S1–S6: exact paired manipulation, prespecified outcome, per-model honesty, blinded judge, sensitivity analyses, numbers reproduce | S1–S4: inherited labels, transparent meaning check, nuanced per-condition finding, released lexicon | S1–S6: inherited labels, remedy controls, conditional-advice rule, honest trúng gió null, proxy narration, non-endorsement |
| Key weaknesses | → Step 1b (W1–W6) | → Step 1b (W1–W12, AR8 note) | → Step 1b (W1–W8) | → Step 1b (W1–W8) |
| # of questions | 3 | 0 (remedies inline) | 5 | 4 |
| # of minor issues | W4–W6 (3) | W4–W12 (9) | W4–W8 (5) | W3, W7, W8 + 2 listed minor issues |

### Step 1b: Weakness Sub-Claim Inventory

| sub_claim_id | parent_weakness | reviewer_id | position | evidence_pointer | severity | confidence |
|---|---|---|---|---|---|---|
| SC-1 | EIC W1 title/intro foreground folk effect | EIC | raised | EIC W1 anchor §8 | major | 5 |
| SC-2 | EIC W2 restoration positioning / R2 W4 restoration lit | EIC | raised | EIC W2 absence §2/§6 | major | 4 |
| SC-2 | R2 W4 | R2 | disputed (severity) | R2 W4 absence §2 | minor | 5 |
| SC-3 | EIC W2 novelty beyond effect size | EIC | raised | EIC W2 absence §2/§6 | major | 4 |
| SC-4 | EIC W3 "LLMs" roster | EIC | raised | EIC W3 Table 3 | major | 4 |
| SC-4 | R1 W5 inference covers only these nine models | R1 | disputed (severity) | R1 W5 text Statistics | minor | 4 |
| SC-5 | EIC W4 remedy wording | EIC | raised | EIC W4 §1 contribution 2 | minor | 5 |
| SC-5 | R1 W1 remedy headline without caveat | R1 | disputed (severity) | R1 W1 "up to half for one model" | major | 4 |
| SC-6 | EIC W5 per-condition as contribution | EIC | raised | EIC W5 §1 contribution 3 | minor | 4 |
| SC-6 | R1 W3 remove from contributions | R1 | disputed (severity) | R1 W3 | major | 4 |
| SC-7 | EIC W6 dense §3.3 | EIC | raised | EIC W6 §3.3 | minor | 4 |
| SC-8 | R1 W1 remedy CIs / confusion matrix | R1 | raised | R1 W1 | major | 4 |
| SC-9 | R1 W2 mitigation inference | R1 | raised | R1 W2 Table 4 | major | 4 |
| SC-10 | R1 W3 per-condition findings under-supported | R1 | raised | R1 W3 §5.4 | major | 4 |
| SC-10 | R2 S3 per-condition finding as strength | R2 | disputed (existence) | R2 S3 §5.4 | — (strength) | — |
| SC-10 | R3 S4 trúng gió null as strength | R3 | disputed (existence) | R3 S4 §5.4 | — (strength) | — |
| SC-11 | R1 W4 judge validation by stratum | R1 | raised | R1 W4 | minor | 4 |
| SC-12 | R1 W5 estimand / Qwen lineage / model-based check | R1 | raised | R1 W5 | minor | 4 |
| SC-13 | R1 W6 interaction contrast | R1 | raised | R1 W6 | minor | 4 |
| SC-14 | R1 W7 Table 4 denominator | R1 | raised | R1 W7 absence | minor | 4 |
| SC-15 | R1 W8 rerun variability | R1 | raised | R1 W8 | minor | 3 |
| SC-16 | R1 W9 folk bundles label and register | R1 | raised | R1 W9 | minor | 3 |
| SC-16 | R2 W2 | R2 | disputed (severity) | R2 W2 §3.2 | major | 4 |
| SC-16 | R3 W6 | R3 | disputed (severity) | R3 W6 Fig. 3 | major | 3 |
| SC-17 | R1 W9 raters used LLM aid (κ 0.15) | R1 | raised | R1 W9 | minor | 3 |
| SC-17 | R2 W3 naturalness not independent | R2 | disputed (severity) | R2 W3 §3.3 | major | 4 |
| SC-17 | R3 W5 non-clinician LLM-aided raters | R3 | disputed (severity) | R3 W5 §7 | major | 4 |
| SC-18 | R1 W9 flagged cases edited without re-rating | R1 | raised | R1 W9 | minor | 3 |
| SC-19 | R1 W10 reproducibility identifiers | R1 | raised | R1 W10 absence | minor | 4 |
| SC-20 | R1 W11 none labels folded in | R1 | raised | R1 W11 | minor | 4 |
| SC-21 | R1 W12 mechanism from anecdotes | R1 | raised | R1 W12 §6 | minor | 3 |
| SC-21 | R2 W1 | R2 | disputed (severity) | R2 W1 §6 | major | 4 |
| SC-22 | R1 AR8 note: Holm family size | R1 | raised | R1 "Note on AR8" | minor [SEVERITY-SOURCE: letter-fallback] | 4 [CONFIDENCE-SOURCE: report-level] |
| SC-23 | R2 W2 / R3 W6 Southern dialect | R2 | raised | R2 W2 §3.2 | major | 4 |
| SC-23 | R3 W6 | R3 | corroborated | R3 W6 Fig. 3 | major | 3 |
| SC-24 | R2 W3 folk language not attested | R2 | raised | R2 W3 §3.3 | major | 4 |
| SC-25 | R2 W4 unaccented-typing claim unsourced | R2 | raised | R2 W4 | minor | 5 |
| SC-26 | R2 W5 đ/Đ handling | R2 | raised | R2 W5 §3.2 | minor | 5 |
| SC-27 | R2 W5 _nd is an idealised worst case | R2 | raised | R2 W5 §3.2 | minor | 5 |
| SC-28 | R2 W6 intro examples not in lexicon | R2 | raised | R2 W6 §1 | minor | 3 |
| SC-28 | R3 W1 intro conditions not tested | R3 | disputed (severity) | R3 W1 §1 | major | 4 |
| SC-29 | R2 W6 lay names vs folk categories | R2 | raised | R2 W6 | minor | 3 |
| SC-30 | R2 W6 trúng gió / cạo gió delay claims uncited | R2 | raised | R2 W6 | minor | 3 |
| SC-30 | R3 W3 unsourced delay claim | R3 | corroborated | R3 W3 §1 | minor | 4 |
| SC-31 | R2 W7 adaptation from two models | R2 | raised | R2 W7 §6 | minor | 4 |
| SC-32 | R2 W8 lexicon glosses unsourced | R2 | raised | R2 W8 §3.4 | minor | 3 |
| SC-32 | R3 W2 lexicon unsourced | R3 | disputed (severity) | R3 W2 tab:lexicon | major | 4 |
| SC-33 | R3 W1 Vietnam-specific emergencies absent | R3 | raised | R3 W1 §1 | major | 4 |
| SC-34 | R3 W2 vong theo mapping | R3 | raised | R3 W2 tab:lexicon | major | 4 |
| SC-35 | R3 W3 deficit framing | R3 | raised | R3 W3 §1 | minor | 4 |
| SC-36 | R3 W4 release safeguards | R3 | raised | R3 W4 absence | major | 4 |
| SC-37 | R3 W5 no clinician review | R3 | raised | R3 W5 §7 | major | 4 |
| SC-38 | R3 W7 untimed "soon" | R3 | raised | R3 W7 §4 | minor | 4 |
| SC-39 | R3 W8 restoration caveat | R3 | raised | R3 W8 §6 | minor | 3 |

Rows not listed for a seat mean `not-mentioned` (silence), which is neither agreement nor opposition. Disposition summary: SPLIT (severity) SC-2, SC-4, SC-5, SC-6, SC-16, SC-17, SC-21, SC-28, SC-32; SPLIT (existence) SC-10; corroborated 2/4 SC-23, SC-30; all others single-reviewer findings. Surface-form parity check: no sub-claim was down-rated or credited for its wording; all were assessed against the cited manuscript passages.

### Devil's Advocate findings

| DA id | Band | Corroborated by | Handling |
|---|---|---|---|
| (CRITICAL) | — | — | Table empty; no adjudications required |
| M1 paraphrase instability | MAJOR | none (R1 W8 adjacent) | S20, should_fix |
| M2 folk label bundled; title contradicts result | MAJOR | EIC W1; R1 W9, R2 W2, R3 W6 | R1, R10 |
| M3 "LLMs" overgeneralises | MAJOR | EIC W3; R1 W5 | R4 |
| M4 remedy headline / "dangerous" | MAJOR | EIC W4; R1 W1 | R5, R7 |
| M5 mechanism from anecdotes; mitigation fits caution shift | MAJOR | R1 W12, R2 W1; R1 W2 | R12, R8 |
| Minor (a)–(e) | minor, "do not change the decision" | (b) R1 W4; (c) R1 W3; (d) R2 W7 | S2, R9, S16, S21, S22 |

### Journal-Fit Review Report Summary
- Recommendation: Major Revision | Confidence: 4
- Key point: In scope with a useful released resource, but the title sells the folk-label story the results downplay, and the diacritic result is not positioned against restoration and perturbation work (W1–W3). Venue page length was not assessed (compiled PDF not provided).

### Reviewer 1 (Methodology) Summary
- Recommendation: not labelled; D1 warn, D3 warn | Confidence: 3–4 per finding
- Key point: The paired RQ1/RQ2 core is sound and its headline numbers reproduce, but RQ3, RQ4 and the per-condition analysis are headlined without inferential support (W1–W3).

### Reviewer 2 (Domain) Summary
- Recommendation: not labelled; D2 warn | Confidence: 4
- Key point: The diacritic mechanism is asserted from anecdotes, the folk condition confounds label with colloquial and Southern vocabulary, and authenticity of the folk language is not established (W1–W3).

### Reviewer 3 (Perspective) Summary
- Recommendation: not labelled; D4 warn | Confidence: 4 (scope disclosure)
- Key point: Clinically sound design choices, but the case mix omits Vietnam-specific emergencies, the lexicon is unsourced with one medicalising mapping, no clinician reviewed the Vietnamese cases, and the release lacks safeguards (W1, W2, W4, W5).

### Devil's Advocate Summary
- Recommendation: N/A — findings only
- Key challenge: No unresolved Critical challenge. Strongest MAJOR counter-argument (M1): the +11 folk effect may be generic paraphrase instability of small greedy-decoded models; the defensible thesis is that diacritic-stripped Vietnamese degrades triage advice in models of 8B or fewer.


## Attachment: Suggested-Reference Check (advisory, #1001)

Suggested-reference check (script output, not a reviewer finding; #1001)
Seats read: R2, R3 (complete).

| Seat | # | Reference | Result |
|---|---|---|---|
| R2 | 1 | Náplava, J. et al. (2018) "Diacritics Restoration Using Neural Networks" | Found in an index |
| R2 | 2 | Nguyen, T.-N. et al. (2024) "ViLexNorm: A Lexical Normalization Corpus for Vietnamese Social Media Text" doi:10.18653/v1/2024.eacl-long.85 arXiv:2401.16403 | Found in an index |
| R2 | 3 | Bui, C. T. et al. (2025) "VMLU Benchmarks: A comprehensive benchmark toolkit for Vietnamese LLMs" | Found in an index |
| R2 | 4 | Nguyen, T.-H. et al. (2024) "ViLLM-Eval: A Comprehensive Evaluation Suite for Vietnamese Large Language Models" arXiv:2404.11086 | Found in an index |
| R2 | 5 | Minh, N. et al. (2022) "ViHealthBERT: Pre-trained Language Models for Vietnamese in Health Text Mining" | Found in an index |
| R2 | 6 | (2021) "ViMQ: A Vietnamese Medical Question Dataset for Healthcare Dialogue System Development" arXiv:2304.14405 | Found in an index |
| R3 | 1 | Kleinman, A. (1980) "Patients and Healers in the Context of Culture: An Exploration of the Borderland between Anthropology, Medicine, and Psychiatry" | Found in an index |
| R3 | 2 | Gebru, T. et al. (2021) "Datasheets for Datasets" arXiv:1803.09010 | Found in an index |
| R3 | 3 | Bender, E. M. et al. (2018) "Data Statements for Natural Language Processing: Toward Mitigating System Bias and Enabling Better Science" | Found in an index |

"Found" means an index holds a record with this DOI or arXiv ID and title, or with this title. It does not show that the work supports the recommendation, or that the authors and year are right.


## Attachment: Reviewer Claim Check (advisory, #1002)

The judge answered 39 of 39 findings from 5 reviewers: it marked 2 as contradicted, and 0 cannot be checked from the manuscript alone.

The judge marked these findings as contradicted by the manuscript. The script checked only the words of each quote: that they occur in the manuscript, or, for words the finding quotes, that they do not. The judge gave the locations, and the script did not check them. Read each quote to decide:
- Reviewer 3 · W4: No data-release safeguards for LLM-drafted remedies and dangerous outputs
  > “We do not build or recommend a medical advice system; our aim is to expose a risk. No result here shows that any model is safe for medical advice. We used an LLM to draft the translations, folk rewrites and remedies” (Ethics Statement)
- Journal-Fit Reviewer · W5: Per-condition analysis is claimed as a contribution but reported thinly
  > “Under-triage varied by condition. Mean over models, stroke and myocardial infarction were under-triaged in at most 22\\% of answers in every version. This held even for stroke told as \\vi{trúng gió}” (Section 5.4 (Which conditions), first paragraph)

The author decides what to do with each row. This check does not change the decision, the consensus counts, or the Revision Roadmap. The judge is the session model; as this judge, the #1002 contrast test passed Claude Opus 5.5 and Claude Fable 5.1 (gpt-6-astra and Gemini 4 Argon passed it in part one, through other transports); other models are untested.


## Attachment: Acronym Check (advisory, #849)

### Acronym check (advisory; no reply needed)
Coverage: body (partial)
Not in this input: English abstract, Chinese abstract.
Not checked:
- Body, line 430: RQ4 (the initials before its parentheses do not spell it)
- Body, line 749: MIT (the initials before its parentheses do not spell it)

| Scope | Line | Rule | Acronym | Uses |
|---|---|---|---|---|
| Body | 2 | Defined after first use | LLM | 35 |
| Body | 71 | Not defined | API | 4 |
| Body | 104 | Not defined | RQ1 | 3 |
| Body | 105 | Not defined | RQ2 | 3 |
| Body | 106 | Not defined | RQ3 | 3 |
| Body | 134 | Not defined | CARE | 2 |
| Body | 144 | Not defined | NLP | 3 |
| Body | 155 | Not defined | OK | 4 |
| Body | 158 | Not defined | VM14K | 2 |
| Body | 190 | Not defined | COPD | 2 |
| Body | 340 | Not defined | AC1 | 1 |
| Body | 340 | Not defined | PABAK | 1 |
| Body | 365 | Not defined | AI | 2 |
| Body | 367 | Not defined | GPU | 1 |
| Body | 382 | Not defined | SeaLLM | 12 |
| Body | 488 | Not defined | VyL | 1 |
| Body | 491 | Not defined | SeaL | 1 |
| Body | 735 | Not defined | ACM | 1 |
| Body | 735 | Not defined | FAccT | 1 |
| Body | 746 | Not defined | GPT | 1 |
| Body | 766 | Not defined | BMJ | 1 |
| Body | 798 | Not defined | ANSWER | 1 |
| Body | 798 | Not defined | REMEDY | 2 |
| Body | 815 | Not defined | ER | 1 |
| Body | 829 | Not defined | JSON | 1 |
| Body | 879 | Not defined | GI | 1 |
