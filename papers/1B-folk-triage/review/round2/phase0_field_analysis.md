# Field Analysis Report — paper 1B, round 2 (2026-11-10)

Pre-submission review of the revised manuscript (after the round-1 minimal revision and the eight new figures, commit 36498fd).

## Paper Basic Information
- **Title**: "Trúng gió" or Stroke? Testing LLM Triage on Folk-Worded and Unaccented Vietnamese Health Questions
- **Abstract length**: ~300 words
- **Full text length**: ~8,900 words (22 pages LNCS including two appendices; 12 figures, 3 tables)
- **Number of references**: 17

## Field Analysis

| Dimension | Analysis Result |
|-----------|----------------|
| Primary Discipline | AI in healthcare: LLM safety evaluation for consumer health advice |
| Secondary Disciplines | NLP robustness (Vietnamese, diacritics); medical informatics / emergency triage; medical anthropology (folk illness) |
| Research Paradigm | Quantitative |
| Methodology Type | Controlled perturbation experiment (paired within-case design, 52 cases × 5 versions × 9 models) + LLM-as-judge validated against human labels |
| Target Journal Tier | Author-stated: a Q3 conference on AI in healthcare (LNCS format). No named venue, track or call for papers was supplied, so no criteria binding: `criteria_binding_unavailable`. The panel judges fit to the general AI-in-health conference readership, not to a specific venue's criteria. |
| Paper Maturity | Pre-submission: revised after round 1, all numbers in place, figures added, citations verified. The 22-page length is the main open risk, since the venue's page limit is unknown. |

## Recommended Target Journals
None proposed. The author named the target type (Q3 AI-in-healthcare conference); no specific venue is substituted.

## Reviewer Configuration Cards

### Reviewer Configuration Card #1
**Role**: EIC
**Display role**: Journal-Fit Reviewer
**Identity Description**: Program-committee area chair of a Q3-level AI-in-healthcare conference (LNCS proceedings). Has handled many "LLMs for patient-facing health advice" submissions, mostly in English.
**Review Focus**:
  1. Whether an AI-in-health audience (clinicians, health informaticians, ML researchers) gets a clear, relevant contribution: safety risk of LLM triage for non-English, non-standard user input.
  2. Presentation for this readership: title/abstract match the findings, figures help rather than repeat tables, length vs. typical 12–16-page limits.
  3. Whether the clinical-safety framing is proportionate to evidence produced without a clinician.
**Will particularly care about**: That a reader leaves with one clear safety message and an actionable takeaway for health-app builders.
**Possible blind spots**: Does not check statistics or Vietnamese-language details in depth.

### Reviewer Configuration Card #2
**Role**: Peer Reviewer 1
**Display role**: Peer Reviewer 1 — Methodology
**Identity Description**: Biostatistician working on diagnostic-accuracy and agreement studies (κ, Wilson intervals, paired and clustered bootstrap) and on evaluation of LLM-as-judge pipelines in clinical NLP.
**Review Focus**:
  1. Inference with 14 emergency cases: case-level bootstrap across 9 models, Holm correction over 36 tests, and which claims are confirmatory vs. exploratory.
  2. Judge validity: 150 stratified human labels, κ = 0.94 for emergency vs. not, κ = 0.50 for remedy stance, judge from the same family as two evaluated models.
  3. Whether the new figures report the same numbers as text and tables, with uncertainty shown where claims depend on it.
**Will particularly care about**: That effect sizes and intervals are not over-read, especially per-condition and per-model results.
**Possible blind spots**: Vietnamese language and clinical nuance.

### Reviewer Configuration Card #3
**Role**: Peer Reviewer 2
**Display role**: Peer Reviewer 2 — Domain (Vietnamese NLP and health NLP)
**Identity Description**: Researcher in Vietnamese NLP and medical NLP for low-resource languages: diacritic restoration, Vietnamese LLM benchmarks, consumer health question answering.
**Review Focus**:
  1. Positioning against related work on LLM triage robustness, non-standard input and Vietnamese medical benchmarks; whether the novelty claim holds.
  2. Dataset construction: translation and folk rewriting, meaning check, folk-term lexicon, realism of automatically removed diacritics.
  3. Whether the mechanism stated in the Discussion ("models misread the signs") is supported or presented as a hypothesis.
**Will particularly care about**: That the released resource is usable and documented well enough for others to build on.
**Possible blind spots**: Clinical triage standards.

### Reviewer Configuration Card #4
**Role**: Peer Reviewer 3
**Display role**: Peer Reviewer 3 — Clinical safety and practice
**Identity Description**: Emergency physician and digital-health safety researcher who has evaluated symptom checkers and works with Southeast-Asian patient populations, including folk-illness beliefs such as *trúng gió* and coin rubbing.
**Review Focus**:
  1. Clinical validity of the triage labels and of the under-/over-triage definitions; how the reused physician labels carry over to Vietnamese versions without clinician re-check.
  2. Harm framing: the remedy-endorsement result, the mitigation trade-off (lower under-triage, higher over-triage) and what it means for real deployment.
  3. Ethics and release: risk of stereotyping users, the content warning, and safe release of model outputs that contain unsafe advice.
**Will particularly care about**: That recommendations to health-app developers are concrete and do not overstate what a prompt fix can do.
**Possible blind spots**: NLP and statistical detail.

*(Fifth seat: the fixed Devil's Advocate. It has no configuration card and challenges the core argument.)*

## Review Strategy Recommendations
- This is a second, pre-submission pass. Reviewers should check that round-1 issues stay fixed and catch new problems from the revision: 12 figures, the 22-page length, figure–text consistency.
- R1 and the Devil's Advocate should test whether the confirmatory claims rest on the 14 emergencies alone.
- R3 and the Journal-Fit Reviewer may disagree on how much the missing clinician limits a health-AI venue paper; the synthesizer should resolve this.
