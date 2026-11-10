# Round 2 — author decisions and changes (2026-11-10)

Source: [synthesis.md](synthesis.md) (simulated ARS panel, decision Major Revision; 16 must_fix, 28 should_fix/consider, 11 questions).
Guiding rule from Hieu: accept what makes the paper clearer, more correct or stronger; decline with a stated reason otherwise.
New analyses: `experiments/1B-folk-triage/extra_analyses.py` → `results/tables/extra_*.csv` (run on the Drive copy of gen/, judge/, annotation/).

Status: **accept** = changed in main.tex; **partial** = part done, rest declined with reason; **decline** = no change, reason given; **defer** = waits for the venue's page limit.

## Must fix

| Item | Status | What changed / why not |
|---|---|---|
| R1 page length | defer | No venue is chosen yet, so the limit is unknown. Prepared cut list once it is: merge Figs. 1/4, keep one of Fig. 6/Table 2 and Fig. 11/Table 3, move §3.3 statistics and Fig. 10 to an appendix (S1, S2, S6, S8). Paper is now 23 pages. |
| R2 retitle / reorder | partial | Abstract and contribution 2 now lead with the diacritic result. Title kept: it asks a question that the paper answers ("not trúng gió, mostly diacritics"), and the subtitle names both factors. |
| R3 causal sentence | accept | §1: change attributed to "the telling as a whole … or the loss of diacritics"; the conflict with "not by missing information" is removed. |
| R4 abstract caveat | accept | Abstract: versions drafted with LLM help, checked by native speakers, not by a clinician. |
| R5 small-cluster inference | accept | §4 Statistics and §5.1: exact sign-flip test and t interval on the 14 case-level differences (p = 0.02, 0.003, <0.001; t intervals [3,19], [12,39], [19,39]). Conclusions unchanged. |
| R6 judge validation by stratum | accept | §4: binary κ CI [0.87, 0.99], 2+2 disagreements, κ = 1.00 on unaccented answers vs 0.90 on accented, 0.94 for Gemini and others. Judge error does not explain the diacritic effect. Human-vs-judge under-triage contrast not added: too few emergency answers per stratum in the 150-answer sample. |
| R7 interaction | accept | §5.1: interaction −8 [−21, 5]; diacritic minus folk +14 [6, 24], sign-flip p = 0.015; "causes most of the harm" → "accounts for most of the increase". |
| R8 per-model claims | accept | Per-model results labelled descriptive; abstract wording is "mainly in small open models". |
| R9 Discussion vs Fig. 10 | accept | Error fixed: folk wording (with diacritics) raised meningitis 11→44% and heart failure 0→33%; liver failure and DKA rose only without diacritics. |
| R10 remedy-stance validation | accept | κ = 0.50 [0.26, 0.73]; stance confusion: judge said endorse for 8 answers the annotator labelled reject, none the reverse. Remedy rates are now called "probably too high". |
| R11 remedy figures in abstract | accept | "7 of 14" removed from abstract and contribution 2; abstract gives 10% / 26% with the reliability caveat. |
| R12 lexicon categories | partial | Contribution 1 now says "folk and lay terms (folk-illness labels and colloquial symptom words)". Re-analysis by category declined: with 14 emergencies the subgroups would hold only a few cases. |
| R13 fully unaccented | accept | Abstract "removing all diacritics"; Conclusion same; Limitations: no prevalence estimate exists, so the 25-point effect is a worst case. |
| R14 clinician urgency check | decline | No clinician is available to the author; this is why pre-labelled public cases were used. The disclosure is now in the abstract (R4) as well as Limitations. Stays an acknowledged limitation. |
| R15 unsafe-endorsement split | partial | Three-way split added: 13 answers (7 emergency, 6 urgent) endorsed but also advised emergency care. Classifying remedies as harmful vs delay-only declined: needs clinical judgement. |
| R16 trúng gió as single case | accept | Results, contribution 3 and Conclusion now say "in our single stroke case". |

## Should fix / consider

| Item | Status | What changed / why not |
|---|---|---|
| S1 figure/table pairs | defer | With R1; the author asked for more figures, so they are cut only if the page limit requires. |
| S2 merge schematics | defer | With R1. |
| S3 shorter abstract | accept | 300 → 264 words, fewer numbers. |
| S4 deployment paragraph | accept | New "Implications for deployment" paragraph: three steps, and a statement that none is shown to make a model safe. |
| S5 restoration pilot | decline | New experiment, out of scope; kept as a stated next step in the Discussion. |
| S6 move §3.3 stats | defer | With R1. |
| S7 run dates in caption | decline | Dates do not identify the authors. |
| S8 Fig. 10 to appendix | defer | With R1. |
| S9 "on average" = these nine models | accept | §4 Statistics. |
| S10 annotator knew hypotheses | accept | Stated in §4. |
| S11 detectable effect | accept | Wrong number fixed: 6 discordant cases (43 points) unadjusted, 11 (79 points) for the first Holm step, not "about 30". |
| S12 zero-width cells | accept | Table 2 caption: "[+0, +0] means no case changed". |
| S13 over-triage CI | accept | folk_nd −6 [−12, 0]. |
| S14 mitigation shifted both versions | accept | Gap sentence now says both versions moved down by similar amounts (gap 20 → 20/18). |
| S15 asthma two cases | accept | Fixed. |
| S16 code, identifiers, seed | accept | Release statement names analysis code, model identifiers and seed. |
| S17 Llama denominator | accept | 18 of 52 remedy answers. |
| S18 anchor in real user text | decline | No consented corpus of Vietnamese health questions is available; the gap is already stated in Limitations ("real user messages are longer and messier"). |
| S19 source each gloss | decline | No ethnographic source covers these terms; the paper already says the glosses are author-provided, not from an ethnographic source. |
| S20 partial-diacritic condition | decline | New experiment; the worst-case framing is now explicit (R13). |
| S21 "usually benign" | accept | → "one that families usually treat at home". |
| S22 soften mechanism heading | accept | "Diacritic loss: the signs may be lost"; "seemed not to read them". |
| S23 competing mechanisms | accept | Syllable collapse and tokenisation named. |
| S24 related work | partial | Added Jin et al. (WWW 2024), verified on Crossref and arXiv. Vietnamese health-QA and restoration items not added: R2 marked them unverified and the restoration citation is already present. |
| S25 licence, schema, location | accept | Derived cases keep MIT/CC0; lexicon, outputs, labels, code CC BY 4.0, research use; link withheld for review. **Licence choice to confirm with Hieu.** |
| S26 urgent tier lower bound | decline | §3.1 already defines the urgent outcome as home care only; no new analysis needed. |
| S27 mitigation over-triage split | decline | Mitigation is descriptive on four models; a finer split adds length without changing the conclusion. Flash-Lite's cautious operating point is already discussed. |
| S28 lexicon column, stereotyping | accept | Column renamed "Source diagnoses (this set)"; data-card note that terms describe usage, not beliefs of any group. *vong theo* already annotated in round 1. |
| S29 release safeguards | accept | Research-use licence, content warning, unsafe labels (Ethics). |
| S30 Vietnamese care pathways | decline | Would need new sources and space; outside the paper's measurement claim. |
| S31 115 access note | decline | Minor; 115 is Vietnam's ambulance number and is named in the prompts. |
| S32 label distribution / none | accept | *none* ≤ 2% per version; excluding it leaves under-triage 21/48/33/51%. |
| S33 sycophancy framing | decline | Unsafe endorsement already conditions on the triage label; the framing is kept as a test of agreement with a user-proposed remedy. |
| S34 urgent diacritic qualifier | accept | §5.2: sign-flip p = 0.07/0.06 and loss of support after removing flagged pairs. |

## Reviewer questions

| Question | Answer |
|---|---|
| EIC Q1 venue / page limit | Not chosen yet; cuts prepared (R1). |
| EIC Q2 retitle | No; reasons under R2. |
| EIC Q3 restoration pilot | Not in this paper (S5). |
| R2 Q1 how folk labels were chosen | From the source signs and common Southern usage, drafted with LLM help and edited by the first author (§3.2, §3.4); not checked against a user corpus (S18). |
| R2 Q2 separate label types | Wording changed; per-category analysis too small (R12). |
| R2 Q3 prevalence of unaccented typing | No estimate found; stated as a worst case (R13). |
| R2 Q4 licence | S25. |
| R3 Q1 physician check | Not feasible for the author (R14). |
| R3 Q2 endorse + emergency advice | 13 answers (R15). |
| R3 Q3 steps for app teams | New deployment paragraph (S4). |
| R3 Q4 release conditions | S25, S29. |
