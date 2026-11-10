# Field Analysis Report — paper 1B (2026-11-10)

## Paper Basic Information
- **Title**: "Trúng gió" or Stroke? Folk-Illness Phrasing and Diacritic Loss Lead LLMs to Under-Triage Vietnamese Health Questions
- **Abstract length**: ~265 words
- **Full text length**: ~7,400 words (18 pages LNCS, including appendices)
- **Number of references**: 16

## Field Analysis

| Dimension | Analysis Result |
|-----------|----------------|
| Primary Discipline | NLP — LLM evaluation / robustness |
| Secondary Disciplines | Medical informatics (triage safety), Vietnamese computational linguistics, medical anthropology (folk illness) |
| Research Paradigm | Quantitative |
| Methodology Type | Controlled perturbation experiment (paired, within-case factorial design) + LLM-as-judge with human validation |
| Target Journal Tier | `criteria_binding_unavailable`. No venue/track was confirmed by the author. Field-general observation: a Springer LNCS conference paper, Q3 level according to SOUL.md |
| Paper Maturity | Pre-submission: complete structure, real numbers in every section, appendices with full prompts, citations checked. Still 18 pages, likely over the venue's page limit |

## Recommended Target Journals
None proposed: there is no confirmed target (`criteria_binding_unavailable`). The panel makes no claim about venue fit.

## Reviewer Configuration Cards

### Reviewer Configuration Card #1
**Role**: EIC
**Display role**: Journal-Fit Reviewer
**Identity Description**: Program-committee senior member for an applied NLP / AI-for-health track at an Asian LNCS conference, who has handled many "LLM evaluation in a low-resource language" submissions.
**Review Focus**:
  1. Whether the contribution (a paired set of 52 cases × 5 versions plus findings across 9 models) is new and important enough for a conference paper, compared with English-language studies (Gourabathina, Ramaswamy).
  2. Whether the title and abstract match the findings, given that the main effect is diacritic loss, not *trúng gió*.
  3. Length (18 pages) and presentation: what can be cut or moved to the appendix.
**Will particularly care about**: Whether the title "Trúng gió or Stroke?" overstates the folk-label effect, when the paper itself shows that *trúng gió* did not mislead the models.
**Possible blind spots**: Does not check the statistics or the data-building process in depth.

### Reviewer Configuration Card #2
**Role**: Peer Reviewer 1
**Display role**: Peer Reviewer 1 — Methodology
**Identity Description**: Biostatistician specialising in paired designs and evaluation with LLM-as-judge; has reviewed studies on diagnostic agreement (κ, McNemar, cluster bootstrap) and small-sample studies.
**Review Focus**:
  1. Statistical power with 14 emergencies: whether a case-level bootstrap pooled over 9 models handles the correlation between models and the multiple contrasts.
  2. Judge validity: a 150-label sample, two annotators sharing one guideline (κ = 1.0), κ = 0.50 for remedy stance, and a judge from the same family as two of the evaluated models.
  3. Experiment controls: greedy decoding, the 512→2048-token reruns, mitigation on only 4 models, and the robustness analysis that drops the flagged pairs.
**Will particularly care about**: Whether "+29 points [20, 37]" correctly reflects uncertainty when the unit of inference is 14 cases.
**Possible blind spots**: Little knowledge of Vietnamese and of how natural the folk versions sound.

### Reviewer Configuration Card #3
**Role**: Peer Reviewer 2
**Display role**: Peer Reviewer 2 — Domain (Vietnamese NLP)
**Identity Description**: Researcher in Vietnamese NLP: diacritic restoration, Vietnamese LLM benchmarks (VMLU, VM14K, ViLLM-Eval), and dialects and non-standard input.
**Review Focus**:
  1. Literature coverage: diacritic restoration, robustness to typos and unaccented input in Vietnamese, and Vietnamese medical benchmarks.
  2. Quality of the dataset build: LLM-drafted translation and folk rewriting, the meaning check by 2 non-clinical raters, and the 34-term lexicon.
  3. Whether the explanation "the model misreads the signs" is backed up (tokenisation, or diacritic restoration as a baseline).
**Will particularly care about**: Whether unaccented text produced automatically by Unicode decomposition reflects how users really type (telex/VNI typing errors, mixing accented and unaccented text).
**Possible blind spots**: Medical safety aspects and clinical triage.

### Reviewer Configuration Card #4
**Role**: Peer Reviewer 3
**Display role**: Peer Reviewer 3 — Cross-disciplinary (clinical safety + medical anthropology)
**Identity Description**: Emergency physician who also does research in medical anthropology on Southeast-Asian folk illness concepts (*trúng gió*, coin rubbing / cạo gió) and on digital health safety.
**Review Focus**:
  1. Clinical validity: grouping triage labels into 4 tiers, cases rare in Vietnam (Rocky Mountain spotted fever), and having no clinician re-check the Vietnamese versions.
  2. Folk-illness representation: whether the folk versions and remedies reflect real practice, and the risk of stereotyping users.
  3. Practical implications: what the advice for Vietnamese health apps should be, and the risks of releasing the remedy data.
**Will particularly care about**: That the absence of a clinician at every step is a real limitation for a paper about medical safety.
**Possible blind spots**: Not deep on NLP or statistics.

*(Fifth seat: the fixed Devil's Advocate. It has no configuration card and challenges the core argument.)*

## Review Strategy Recommendations
- The paper's core claim depends on 14 emergencies. R1 and the Devil's Advocate should test whether the causal conclusion ("the model misreads the signs") goes further than the data.
- R2 and R3 may disagree over who should check the data (NLP vs clinical); the synthesizer should resolve this.
- There is a tension between the title (centred on *trúng gió*) and the main finding (diacritic loss). The Journal-Fit Reviewer and the DA should both look at it.
