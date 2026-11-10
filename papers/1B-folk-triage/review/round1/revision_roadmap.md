# Revision Roadmap — paper 1B, review round 1 (2026-11-10)

Prepared with the ARS `academic-paper` skill in `revision-coach` mode (peer-review branch; the source is a simulated ARS panel, not a real committee).

**Source:** the decision letter `synthesis.md` (Major Revision), plus the "Questions for Authors" sections in `eic.phase2.md`, `domain.phase2.md` and `perspective.phase2.md`.

**Excluded:** three advisory attachments: acronym check, suggested-reference check and claim check. They are script output, not reviewer comments, so they are not counted as items to fix. The claim-check results are given only as a reference note (section C).

**Order:**
- Items are listed by source: the decision letter's order (R1–R20, S1–S22), then the questions (Q1–Q12).
- The order is **not** a priority ranking or a work order.
- The columns severity, obligation class, cost scope and consequence come from the letter and were not inferred from one another.

**Missing machine artifacts:**
- There is no block-anchored draft or block manifest, so this file has no `revision-roadmap/1.0` JSON and no exact block IDs. The "Location" column gives only the section.
- No Schema 11 ledger was produced, because this run is outside the pipeline.

**Author triage:** the "Hieu decides" column is empty. For each row choose:
- `will_address`: you will fix it, and you state where;
- `wont_address`: you won't fix it, with a reason;
- `not_on_point`: the reviewer misread the paper, with a reason.

Claude does not choose for you.

---

## A. Required fixes (must_fix): 20 items

| Ref | What to do | Reviewer severity | Raised by | Cost scope | Consequence if not fixed | Location | Hieu decides | Reason (if not fixing) |
|---|---|---|---|---|---|---|---|---|
| R1 | Change the title and reorder the introduction and contributions so that diacritic loss comes first; state that the folk effect is small and that the two effects do not add up | major | EIC W1 (+DA M2) | section | the title claims something the results do not support | title, abstract, §1 | | |
| R2 | Add literature on Vietnamese diacritic restoration and on unaccented text | major / minor | EIC W2, R2 W4 | section | evidence gap in §2 | §2 | | |
| R3 | State what is new beyond "a larger effect than in English"; any cross-study comparison must note that the models and metrics differ | major | EIC W2 | section | novelty claim not supported | §1, §2, §6 | | |
| R4 | Narrow "LLMs" in the title, abstract and contribution 2 to the models tested; report the open-model mean and the API-model mean separately | major / minor | EIC W3, R1 W5 (+DA M3) | section | title overgeneralises | title, abstract, §1 | | |
| R5 | Make the wording about remedy endorsement match across the abstract and the contributions, and add the κ = 0.50 caveat | minor / major | EIC W4, R1 W1 (+DA M4) | sentence | contribution 2 overclaims | abstract, §1 | | |
| R6 | Drop the per-condition analysis from the contributions, or keep it only with a full table (R9) | minor / major | EIC W5, R1 W3 | sentence | contribution 3 overclaims | §1 | | |
| R7 | Add Wilson CIs for the endorsement rates, a confusion matrix for remedy stance, and a sensitivity estimate from human labels only | major | R1 W1 (+DA M4) | re_analysis | RQ3 rates have no measure of uncertainty | §5.3 | | |
| R8 | Add paired bootstrap CIs for the RQ4 changes (under-triage, gap, over-triage); say that the gap did not change; soften the abstract | major | R1 W2 (+DA M5) | re_analysis | Table 4 has no inference | §5.5, Table 4 | | |
| R9 | Label the per-condition analysis exploratory, report all 14 conditions with intervals, and present the "sign-specificity" explanation as a hypothesis | major | R1 W3 (R2 S3, R3 S4 disagree) | re_analysis | §5.4 and the conclusion overclaim | §5.4, §8 | | |
| R10 | Attribute RQ1 to the whole lay/folk rewrite rather than to the folk label alone; state this confound in Limitations | minor / major | R1 W9, R2 W2, R3 W6 (+DA M2) | section | "folk-illness phrasing" claim not supported | title, abstract, §6–§8 | | |
| R11 | State that the meaning check used an LLM aid; get **at least one naturalness judgement made without an LLM** | minor / major | R1 W9, R2 W3, R3 W5 | **new_data** | evidence gap in §3.3 | §3.3 | | |
| R12 | Present "the model misreads the signs" as a hypothesis, or test it systematically (do answers restate the signs, a restoration rerun, token counts) | minor / major | R1 W12, R2 W1 (+DA M5) | section (or re_analysis) | mechanism claim not supported | §6, §8 | | |
| R13 | Name the Southern regional bias of the folk vocabulary (*ói*, *bao tử*) as a confound; say which variety was targeted and where the raters are from | major | R2 W2, R3 W6 | section | RQ1 interpretation ambiguous | §3.2, §7 | | |
| R14 | Show that the lexicon terms occur in real Vietnamese patient text (e.g. ViMQ), or soften "how users actually write" | major | R2 W3 | section | "actually write" claim not supported | §3.4, §6, §8 | | |
| R15 | Make the examples in the introduction (dengue, heat stroke, methanol; *cảm nắng*, *say rượu*, *nóng trong*) match the dataset, or mark them as not tested | minor / major | R2 W6, R3 W1 | sentence | §1 claims beyond the data | §1 | | |
| R16 | Document where the lexicon came from (who drafted it, whether an LLM was used, who checked it, sources); mark "can hide" as applying to this dataset only | minor / major | R2 W8, R3 W2 | section | lexicon not traceable | §3.4, Appendix B | | |
| R17 | In Limitations, say the set lacks Vietnam-specific emergencies (dengue, heat stroke, methanol…), or add clinician-labelled cases | major | R3 W1 | section | practical claim overreaches | §7 | | |
| R18 | Reword or remove the mapping *vong theo* → "early psychotic disorder", presenting it instead as an explanatory model | major | R3 W2 | sentence | lexicon row breaks editorial norms | Appendix B | | |
| R19 | Add a datasheet (evaluation use only, provenance flag for each remedy, harm labels, content warning) and a paragraph on release risks in the Ethics statement | major | R3 W4 | other: datasheet | release lacks documentation | Ethics, release | | |
| R20 | Have a Vietnamese physician confirm that the **24 emergency/urgent pairs** keep their source acuity | major | R3 W5 | **new_data** | evidence gap for 24 pairs | §3.3, §7 | | |

## B. Should fix / consider: 22 items

| Ref | What to do | Severity | Raised by | Obligation | Cost scope | Location | Hieu decides | Reason (if not fixing) |
|---|---|---|---|---|---|---|---|---|
| S1 | Split the §3.3 meaning-check paragraph into procedure / agreement / adjudication | minor | EIC W6 | should_fix | section | §3.3 | | |
| S2 | Report judge confusion matrices and agreement by version and model family (including the Gemini judge with the Gemini models), plus a sample from the mitigation runs | minor | R1 W4 (+DA b) | should_fix | re_analysis | §4 | | |
| S3 | State the estimand of the pooled estimate; add a GLMM or cluster CI; report the effect without the Qwen models | minor | R1 W5 | should_fix | re_analysis | §4 | | |
| S4 | Bootstrap CI for the interaction ("do not add up") | minor | R1 W6 | should_fix | re_analysis | §5.1 | | |
| S5 | Give the over-triage denominator and the pooled versions in Table 4 | minor | R1 W7 | should_fix | sentence | Table 4 | | |
| S6 | Report the share of disagreement between reruns and a paired CI under sampling; rerun some API calls | minor | R1 W8 | should_fix | re_analysis | §5.6 | | |
| S7 | Say whether the edited flagged pairs were re-rated | minor | R1 W9 | should_fix | sentence | §3.3 | | |
| S8 | Add model revision IDs, bootstrap seed, code release statement | minor | R1 W10 | should_fix | sentence | Table 2 | | |
| S9 | Report the `none` rate by model/version, and the main contrasts excluding `none` | minor | R1 W11 | should_fix | re_analysis | §4, §5 | | |
| S10 | State the number of tests in the Holm family | minor | R1 (AR8) | consider | sentence | §4 | | |
| S11 | Cite a source for the claim that Vietnamese is often typed without diacritics | minor | R2 W4 | should_fix | sentence | §1 | | |
| S12 | Describe how đ/Đ is handled and whether any words keep their diacritics in `_nd` | minor | R2 W5 | should_fix | sentence | §3.2 | | |
| S13 | Call `_nd` a controlled worst case, not "how users actually type" | minor | R2 W5 | should_fix | sentence | §3.2, §6 | | |
| S14 | Separate ordinary lay names (*đau mắt đỏ*, *giời leo*…) from folk-illness categories | minor | R2 W6 | consider | section | §3.4, App. B | | |
| S15 | Cite a source, or soften, the claim that *trúng gió*/*cạo gió* delays stroke care | minor | R2 W6, R3 W3 | should_fix | sentence | §1 | | |
| S16 | Limit the "language adaptation did not help" conclusion to the one matched pair (Qwen2.5-3B / VyLinh) | minor | R2 W7 (+DA d) | should_fix | sentence | §6 | | |
| S17 | Frame folk labels as explanatory models so the risk lies in model behaviour, not in the users' culture | minor | R3 W3 | consider | section | §1, §6 | | |
| S18 | Sensitivity analysis: count "soon" with no time frame as unsafe for urgent cases; limit over-triage to self-care and one-week cases | minor | R3 W7 | should_fix | re_analysis | §5 | | |
| S19 | Add a safety caveat to the diacritic-restoration recommendation; mention the cost of the over-triage rise under M1/M2 | minor | R3 W8 | should_fix | sentence | §6 | | |
| S20 | Address the alternative explanation "any paraphrase makes small models unstable" (neutral clinical-paraphrase control, or discussion) | major (DA) | DA M1 | should_fix | new_data or section | §5.1, §6 | | |
| S21 | Qualify "larger than in English" in §6 (models and metrics differ) | minor | DA a | consider | sentence | §6 | | |
| S22 | Note that Gemini's near-zero under-triage comes with 33–39% over-triage | minor | DA e | consider | sentence | §5.1, §6 | | |

## C. Reviewer questions: 12 items

The questions are a separate channel: they have no severity and you are not required to change the paper. The response letter still has to answer each one. The "Overlaps with" column shows which fix already answers the question.

| Ref | Reviewer | Question (summary) | Overlaps with | Hieu decides | Note |
|---|---|---|---|---|---|
| Q1 | EIC | Page count, and the venue's page limit? Move the lexicon to supplementary material? | — (no roadmap item) | | |
| Q2 | EIC | Does a diacritic-restoration step recover the lost emergency advice? | R12 | | |
| Q3 | EIC | Why are there no larger open models (30B+)? | R4 | | |
| Q4 | R2 | How exactly was `_nd` produced; how is đ/Đ handled? | S12 | | |
| Q5 | R2 | Can the folk-label effect be separated from colloquial/regional wording? | R10, R13 | | |
| Q6 | R2 | Are the lexicon terms attested in real patient text; who wrote the glosses? | R14, R16 | | |
| Q7 | R2 | Do the models restate the symptoms correctly for `_nd`? Does restoration recover the result? | R12 | | |
| Q8 | R2 | Were the folk versions written in one regional variety on purpose? | R13 | | |
| Q9 | R3 | Who wrote the lay meanings / "can hide" mappings, and from what sources? | R16 | | |
| Q10 | R3 | Which regional variety, and where are the raters from? | R13 | | |
| Q11 | R3 | Will you add, or defer, Vietnam-specific emergencies? | R17 | | |
| Q12 | R3 | What documentation and use restrictions will come with the released data? | R19 | | |

**Claim-check reference note** (script output, not a reviewer comment): the claim check flagged two findings as contradicted by the manuscript. You may consider `not_on_point` (fully or partly) for these items if you think the reviewer misread the paper:
- **R19 / R3 W4:** the Ethics statement already says "We do not build or recommend a medical advice system… We used an LLM to draft…". There is no datasheet, however.
- **R6 / EIC W5:** §5.4 does report numbers for each condition, though not in a table.

## D. Items that need new data or reruns (to help you plan)

- **New data:**
  - **R11:** naturalness judgement without an LLM. Needs a rater.
  - **R20:** a physician to check 24 pairs. Needs a clinician.
  - **S20:** a neutral-paraphrase control, if you choose a new run.
- **New analysis on existing data:** R7, R8, R9, S2–S4, S6, S9, S18, and R12 if you choose to test it.
- **All the rest:** rewriting, narrowing claims or adding citations only.

---

## E. Approved decisions (Hieu, 2026-11-10): a minimal-change approach

Hieu approved a minimal-change plan for a Q3 venue: rewrite sentences and narrow claims, with no new experiments. On R11, Hieu confirmed (as the 2026-11-08 journal records) that both meaning-check raters used AI support and reviewed its output themselves.

| Item | Decision | What was done in `main.tex` (or the reason for not fixing) |
|---|---|---|
| R1 | will_address | New title: "Testing LLM Triage on Folk-Worded and Unaccented Vietnamese Health Questions". Abstract: missing diacritics cause most of the harm. Intro: added a novelty sentence (first test; foundation for later work) |
| R2 | will_address | One sentence + citation to Náplava et al. 2018 (LREC; covers Vietnamese) in Related Work |
| R3 | will_address | Novelty sentence in §1; the comparison with English work notes that the models and metrics differ |
| R4 | will_address | The new title no longer claims "LLMs"; abstract: effects concentrate in small open models, Gemini barely affected; Limitations: open models are ≤8B |
| R5 | will_address | Abstract and contribution 2: "7 of 14 emergencies for one model", κ = 0.50 |
| R6 | will_address (partly not_on_point) | Kept as a contribution, but labelled "exploratory (one case per condition)" |
| R7 | will_address | Wilson CIs: 13/126 [6, 17], 23/90 [18, 35], SeaLLMs 7/14 [27, 73], Qwen2.5-1.5B 6/10 [31, 83]; noted the intervals are approximate |
| R8 | will_address (softened) | RQ4 stated as descriptive: one run, no CI, models move in different directions. No new bootstrap |
| R9 | will_address | §5.4 labelled exploratory: one case per condition, only the largest shifts reported |
| R10 | will_address | §3.2: the folk version changes the register as well as adding the label; Limitations repeats this |
| R11 | will_address (disclosure) | Limitations: raters used an LLM aid and reviewed its output, so their ratings are not fully independent human judgements. No re-rating |
| R12 | will_address | §6: the mechanism is a hypothesis, two examples cannot show it, a systematic check is future work |
| R13 | will_address | §3.2: Southern lay vocabulary; Limitations: both raters are from the South, Northern and Central speech not covered |
| R14 | will_address | Removed "how users actually write/type" (§6 and conclusion) |
| R15 | will_address | Intro: the examples are now cases in the set (*bị cảm* → liver failure, *nóng trong* → DKA); removed dengue/methanol from §1 |
| R16 | will_address | Authorship + §3.4: lexicon glosses drafted with an LLM and reviewed by the first author; the "can hide" column is the source diagnosis of the cases (this dataset only) |
| R17 | will_address (limitation) | Limitations: dengue, heat stroke and methanol are not tested |
| R18 | will_address | *vong theo* row: added "a spiritual explanation…, not a diagnosis" |
| R19 | will_address (partly not_on_point) | Ethics: evaluation use only, remedies flagged, unsafe labels, content warning; added a Data card to `experiments/1B-folk-triage/README.md` |
| R20 | wont_address | No clinician available. Labels come from physicians in the source datasets; the translations keep the facts; clinician review is listed as future work in Limitations |
| S5 | will_address | Table 4 caption: 14 emergencies; over-triage n = 112 per row |
| S10 | will_address | Holm: 36 tests per outcome |
| S12, S13 | will_address | §3.2: đ→d, every diacritic removed; `_nd` is a controlled worst case |
| S11 | will_address (softened) | "is often typed" → "can be typed" |
| S15 | will_address (softened) | "delays care" → "care can be delayed" |
| S16 | will_address | Language-adaptation conclusion limited to the Qwen2.5-3B / VyLinh pair |
| S19 | will_address | Diacritic restoration needs its own safety check |
| S20 | will_address (limitation) | Limitations: no neutral-paraphrase control |
| S21 | will_address | Comparison with English work qualified (§6) |
| S22 | will_address | Flash-Lite over-triages 36–43% of controls (average 27%) |
| S1, S2, S3, S4, S6, S7, S8, S9, S14, S17, S18 | wont_address | Outside the scope of a minimal-change revision for a Q3 conference; for analyses (S2–S4, S6, S9, S18), the existing robustness section and Limitations already note the limits |
| Q1 | pending | Page count is 19, depending on the venue's limit |
| Q2–Q12 | answered via the matching R/S items | |
