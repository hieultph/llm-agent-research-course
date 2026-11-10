contract_role: domain
## Dimension Scores

### D1: methodology_rigor
score: not_assessed

### D2: domain_accuracy
score: warn
trigger: "missing closely related Vietnamese robustness, diacritic or benchmark references, imprecise terminology, under-documented translation or lexicon procedures"

### D3: argumentative_coherence
score: not_assessed

### D4: cross_disciplinary_relevance
score: not_assessed

### D5: writing_and_structure
score: not_assessed

### D6: venue_fit_and_contribution
score: not_assessed

## Review Body

### Reviewer Identity
Peer Reviewer 2 (domain). Vietnamese NLP researcher working on diacritic restoration, Vietnamese LLM benchmarks (VMLU, VM14K, ViLLM-Eval), and dialectal and non-standard input. Blind spot: clinical triage. I make no judgement on whether the clinical labels or the hidden-condition mappings are medically correct.

### Calibration Status
`NOT_CALIBRATED`

### Confidence Score
4. I am confident about the Vietnamese-language and literature points. I have no competence on the clinical content.

### Criterion-Bound Judgements
| Dimension / criterion | Criterion source | Judgement | Evidence anchors | Rationale | Uncertainty or scope limit | Decision bearing? |
|---|---|---|---|---|---|---|
| D2 domain_accuracy | sprint contract reviewer/reviewer_full/v2 plus my Phase 1 scoring plan | PARTLY_MEETS | W1–W8 below | The prior work the paper cites is described fairly, and the dataset design is sound. However, the linguistic explanations go beyond the evidence, folk wording is confounded with lay and regional vocabulary, the authenticity of the folk language is not established, and the coverage of Vietnamese diacritic and benchmark literature is thin. | Clinical correctness is outside my competence | yes: this supports warn on a mandatory dimension |

### Summary Assessment
This paper tests whether LLM triage advice for Vietnamese health questions shifts when the same case is told in folk or lay wording, or typed without diacritics. To my knowledge, no Vietnamese work has studied this. The minimal-pair design on public, physician-labelled vignettes is a real methodological asset. The paper also reports its meaning check unusually honestly.

From a Vietnamese-NLP standpoint, three issues weaken the claims. First, the paper's headline mechanism for the diacritic effect is that models "misread the signs". This is inferred from two anecdotes, with no linguistic analysis of what diacritic removal does to the text: lexical ambiguity, tokenisation, or whether a model can restore or paraphrase the symptoms. Second, the folk version changes several things at once: it adds the folk-illness label, but also brings in colloquial and largely Southern vocabulary. The RQ1 effect therefore cannot be attributed to folk labels as the title implies. Third, LLMs drafted the folk texts and helped the native-speaker raters, and no attestation from real user text is given. As a result, "the way Vietnamese users actually write" is asserted rather than shown. The related work also leaves out the Vietnamese diacritic-restoration literature, even though the paper recommends restoration as the fix, and it omits the main Vietnamese LLM benchmarks other than VM14K.

All of these can be fixed without overturning the measured effects. That is why I score D2 as warn rather than block.

### S1: Cases and labels come from public physician-labelled sources, not from the authors
Building on the Levine and Ramaswamy vignettes, with licences stated, avoids author-created labels and makes the Vietnamese set traceable to its English source.
**Evidence Anchor**: text: §3.1 "We do not write cases or assign labels ourselves."

### S2: The meaning check is reported transparently
The authors report a low Cohen's kappa alongside prevalence-adjusted agreement, describe how the two raters differed in strictness, and rerun the analysis without the flagged pairs. This is good practice for a translated, perturbed dataset.
**Evidence Anchor**: text: §3.3 "prevalence-adjusted measures were higher"

### S3: The per-condition analysis gives a nuanced linguistic finding
The paper finds that the most salient folk label (trúng gió) does not mislead models when strong signs are also stated, and that the effect concentrates where the signs are less specific. This avoids a simplistic "folk terms are dangerous" story.
**Evidence Anchor**: text: §5.4 "This held even for stroke told as \vi{trúng gió}, so the best-known folk label did not mislead the models."

### S4: A released lexicon that maps folk terms to the conditions they can hide
A list of 34 terms, with lay glosses and their use in this case set, is a reusable resource for Vietnamese health NLP.
**Evidence Anchor**: table: Appendix B, Table tab:lexicon (folk-term lexicon)

### W1: The diacritic-loss mechanism ("models misread the signs") is asserted from two anecdotes
**Severity**: Major
**Evidence Anchor**: text: §6 Discussion "The emergency is lost before any triage reasoning starts."
**Confidence**: 4 (diacritic restoration and Vietnamese orthographic ambiguity are my core area)

The Discussion and the Conclusion present a causal linguistic explanation: the models fail to read the signs in unaccented text, before any triage reasoning starts. The only support is two qualitative answer excerpts (meningitis/Qwen3-8B and stroke/Qwen2.5-1.5B). The paper does not analyse what removing diacritics actually does to these 52 texts. Unaccented Vietnamese collapses many distinct syllables onto one form. Whether the key symptom words become ambiguous depends on the specific words and their context, and it also interacts with how each model's tokenizer splits unaccented syllables. These factors probably differ between Qwen-family, Llama and Gemini tokenizers, and that could explain the model differences better than "language adaptation".

Inexpensive evidence would test the claim directly:
- Ask each model to restate or list the symptoms from the `_nd` text, and compare this with the clinical version.
- Restore diacritics with an off-the-shelf restorer and rerun. The paper itself proposes this step.
- Report token-count inflation and the ambiguity of the key symptom words under stripping.

Without such evidence, the mechanism should be presented as a hypothesis.

### W2: Folk wording confounds the folk-illness label with colloquial and regional (largely Southern) vocabulary
**Severity**: Major
**Evidence Anchor**: text: §3.2 "The same facts in everyday wording (\vi{ói} for vomiting, \vi{tào tháo đuổi} for diarrhoea), plus the folk label a family would use"
**Confidence**: 4 (native-speaker knowledge of Vietnamese dialect lexicon)

The `folk` version changes three things at once:
- it adds a folk-illness label;
- it replaces clinical terms with colloquial ones;
- several replacements are regionally marked, such as ói (Southern) for nôn, and bao tử (Southern) for dạ dày.

The title, the abstract and §6 attribute the effect to "folk-illness phrasing". The design cannot separate the label from register or dialect. The only label-free lay versions are two control cases, which is too few to separate the effects. The per-condition discussion (liver failure told as bị cảm, DKA told as nóng trong) also cannot tell whether the label or the colloquial symptom words drove the shift.

I suggest one of two remedies. The first is to add a lay-wording version without the label for the emergency and urgent cases, which would isolate the label. The second, cheaper option is to reword the claims as "lay/folk wording" and state the regional skew of the vocabulary as a limitation. The Limitations section already mentions regional coverage, but it does not present it as a confound.

### W3: The authenticity of the folk and lay language is not established
**Severity**: Major
**Evidence Anchor**: text: §3.3 "Both used an LLM as an aid and reviewed its output."
**Confidence**: 4 (experience constructing Vietnamese non-standard-input datasets)

The paper claims to measure "the way people actually type" and "how Vietnamese users actually write" (§6, Conclusion). However:
- an LLM drafted the folk versions, and a single editor, who is not a dialectologist, revised them;
- both native-speaker raters used an LLM aid when judging equivalence and naturalness, so the naturalness scores of 4.3 and 4.6 are not an independent human judgement of authenticity;
- the paper gives no attestation for the terms or phrasings in real user text, such as Vietnamese health-forum or hospital Q&A posts. A public corpus of patient questions from a Vietnamese hospital website already exists (ViMQ).

This severity rests on the paper's own central claim about real user language, not on an external field norm. At minimum, the authors should:
- report corpus frequency or attestation for each lexicon term in real Vietnamese patient text;
- have at least one rater judge naturalness without LLM assistance;
- tone down the "actually write" claims if attestation is unavailable.

### W4: The Vietnamese diacritic-restoration and unaccented-text literature is missing
**Severity**: Minor
**Evidence Anchor**: absence: §2 Related Work, paragraph on robustness to how the patient writes — expected prior work on Vietnamese diacritic restoration and on normalising non-standard Vietnamese text; checked §2 Related Work, §6 Discussion (the paragraph recommending restoration), Conclusion, and all citation keys in the manuscript
**Confidence**: 5 (my core area)

On diacritics, the paper cites only a general paper on diacritic stripping (Gorman), yet it recommends restoring diacritics before the text reaches the model. Vietnamese diacritic restoration is a mature task. Náplava et al. (LREC 2018) report very high accuracy on Vietnamese and include it in a public multilingual corpus. ViLexNorm (EACL 2024) normalises Vietnamese social-media text, including missing diacritics and teencode. Citing this work would ground the recommendation and indicate whether restoration is likely to work on short, lay health messages. The claim that Vietnamese "is often typed without diacritics" also needs a source; ViLexNorm-style social-media data could provide one. The severity rests on the paper's own recommendation, not on a generic norm.

### W5: The diacritic-stripping procedure is under-specified and is an idealised condition
**Severity**: Minor
**Confidence**: 5 (Unicode handling of Vietnamese)
**Evidence Anchor**: text: §3.2 "Produced automatically by Unicode decomposition."

Unicode NFD decomposition followed by removing combining marks does not map đ/Đ (U+0111/U+0110) to d/D, because these letters have no canonical decomposition. The examples show "dot ngot" and "do", so the authors must have applied an extra mapping. That step should be stated for reproducibility.

Fully stripping every diacritic is also an upper-bound perturbation. Real unaccented input often mixes accented and unaccented words, contains Telex/VNI residue, or uses abbreviations. The paper should say that `_nd` is a controlled worst case and should not equate it with how users type.

### W6: The motivating examples and the "folk-illness" terminology are imprecise and uncited
**Severity**: Minor
**Evidence Anchor**: text: §1 Introduction "can hide dengue warning signs, heat stroke or methanol poisoning"
**Confidence**: 3 (native-speaker and NLP knowledge; I have no medical-anthropology expertise)

The Introduction motivates the study with cảm nắng (linked to heat stroke) and say rượu (linked to methanol poisoning), but neither term nor either condition is in the 34-term lexicon or among the emergencies. Nóng trong is linked to dengue in the Introduction but to DKA and pyelonephritis in the lexicon. Say rượu is literal intoxication, not a folk-illness category.

Several lexicon entries are ordinary lay names for biomedical conditions or symptoms rather than folk-illness labels, for example:
- đau mắt đỏ, giời leo, lẹo and nhiệt miệng;
- tăng xông and chuột rút;
- tức ngực and đau bao tử.

These should be distinguished from explanatory folk categories such as trúng gió, nóng trong or thận yếu. The cultural claims about trúng gió and cạo gió delaying care would also be stronger with a citation from Vietnamese public-health or medical-anthropology literature. I could not verify a specific reference, so this is a search lead only [UNVERIFIED].

### W7: The conclusion about Vietnamese-adapted models is generalised from two models
**Severity**: Minor
**Evidence Anchor**: text: §6 Discussion "Language adaptation therefore did not make these models more robust to how Vietnamese users actually write."
**Confidence**: 4 (familiar with Vietnamese LLM adaptation work)

The Arcee-VyLinh versus Qwen2.5-3B comparison is a fair base-versus-adapted pair, and both lose 64 points. SeaLLMs-v3, however, is built on Qwen2, which was not tested, so its result cannot be attributed to adaptation. With one clean pair, the claim should be limited to "the two adapted models we tested". Whether the adaptation data contained unaccented text would also be relevant.

### W8: Lexicon glosses and hidden-condition mappings have no stated source
**Severity**: Minor
**Evidence Anchor**: text: §3.4 "For each we record the usual lay meaning and the emergencies it hides in our set"
**Confidence**: 3 (lexicographic practice; the clinical mappings are outside my competence)

The procedure for producing the "usual lay meaning" glosses is not documented: no dictionary, corpus or informant is named, and there is no review step. Since the lexicon is a released contribution and is reused as the M2 glossary, its provenance and review should be stated. Who drafted it, whether an LLM was involved, and who checked it should all be reported.

### Missing Key References
- Náplava et al. 2018, Diacritics Restoration Using Neural Networks (LREC). This is the standard multilingual restoration baseline, and it includes Vietnamese.
- Nguyen, Le and Nguyen 2024, ViLexNorm (EACL). It covers normalisation of real Vietnamese social-media text, including missing diacritics.
- Bui et al. 2025, VMLU Benchmarks (ACL), and Nguyen, Le and Nguyen 2024, ViLLM-Eval (arXiv). These are the main Vietnamese LLM benchmarks and should be named next to VM14K.
- Minh et al. 2022, ViHealthBERT (LREC), and ViMQ (ICONIP 2021; arXiv 2304.14405). These are Vietnamese health NLP resources, and ViMQ is a source of real patient phrasing (see W3).
- Search lead [UNVERIFIED]: Vietnamese public-health or medical-anthropology studies on trúng gió and cạo gió and on delays in seeking care.

~~~yaml suggested-references
- title: "Diacritics Restoration Using Neural Networks"
  authors: ["Náplava, J.", "Straka, M.", "Straňák, P.", "Hajič, J."]
  year: "2018"
  doi: null
  arxiv_id: null
- title: "ViLexNorm: A Lexical Normalization Corpus for Vietnamese Social Media Text"
  authors: ["Nguyen, T.-N.", "Le, T.-P.", "Nguyen, K."]
  year: "2024"
  doi: "10.18653/v1/2024.eacl-long.85"
  arxiv_id: "2401.16403"
- title: "VMLU Benchmarks: A comprehensive benchmark toolkit for Vietnamese LLMs"
  authors: ["Bui, C. T.", "Nguyen, T. S."]
  year: "2025"
  doi: null
  arxiv_id: null
- title: "ViLLM-Eval: A Comprehensive Evaluation Suite for Vietnamese Large Language Models"
  authors: ["Nguyen, T.-H.", "Le, A.-C.", "Nguyen, V.-C."]
  year: "2024"
  doi: null
  arxiv_id: "2404.11086"
- title: "ViHealthBERT: Pre-trained Language Models for Vietnamese in Health Text Mining"
  authors: ["Minh, N.", "Tran, V. H.", "Hoang, V.", "Ta, H. D.", "Bui, T. H.", "Truong, S. Q. H."]
  year: "2022"
  doi: null
  arxiv_id: null
- title: "ViMQ: A Vietnamese Medical Question Dataset for Healthcare Dialogue System Development"
  authors: []
  year: "2021"
  doi: null
  arxiv_id: "2304.14405"
~~~

### Questions for Authors
1. How exactly were the `_nd` versions produced, in particular the handling of đ/Đ? Were any words left accented?
2. Can you separate the effect of the folk label from the effect of colloquial and regional wording, for example with a label-free lay version of the emergency and urgent cases?
3. For each lexicon term, is there attestation in real Vietnamese patient text, and who drafted and checked the glosses?
4. When given an `_nd` prompt, can the affected models restate the symptoms correctly? Does automatic diacritic restoration recover the clinical-version under-triage rate?
5. Were the folk versions written to one regional variety on purpose? If so, which variety?
