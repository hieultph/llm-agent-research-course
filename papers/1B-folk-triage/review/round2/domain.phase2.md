contract_role: domain
## Dimension Scores

### D1: methodology_rigor
score: not_assessed

### D2: domain_accuracy
score: warn
trigger: "realism limits of synthetic input variants are mentioned only briefly"

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
Peer Reviewer 2 (domain). I work on Vietnamese NLP and medical NLP for low-resource languages: diacritic restoration, Vietnamese LLM benchmarks and consumer health question answering. I cannot judge clinical triage standards, so I take the physician labels as given.

### Calibration Status
`NOT_CALIBRATED`

### Summary Assessment
The study asks a clear question that matters for Vietnamese consumer health: does the way a lay Vietnamese user tells a symptom story change the urgency of LLM advice when the facts stay the same? The case base is sound. It uses public, physician-labelled vignettes under stated licences (MIT, CC0) and keeps the source labels. The design adds controls, so a model cannot look good simply by over-triaging. The paper keeps its novelty claim narrow, and in my reading of the cited literature that claim holds. It labels its main mechanism as a hypothesis and reports per-condition results as exploratory.

My concerns are about the domain validity of the two manipulations and of the lexicon.
- The folk versions, remedies and lexicon glosses were drafted by an LLM. The raters who checked them also used an LLM as an aid. No real Vietnamese user text anchors the folk register.
- The "34 folk terms" mix true folk-illness categories with ordinary colloquial or standard Vietnamese words.
- The diacritic condition strips every diacritic. That is a worst case whose prevalence the paper does not document, yet the abstract and conclusion state its effect as the main finding.
- Several framing claims about Vietnamese folk illness have no source, and one ("usually benign") is questionable for the paper's own lead example.

Related work leaves out cross-lingual health-LLM evaluation and Vietnamese health QA resources. The release has no licence or schema in the manuscript. None of these points overturns the core result, but together they limit how far it can be read as evidence about real Vietnamese users.

### Strengths

### S1: Labels come from public physician-labelled sources with stated licences
The authors write no labels themselves. Case selection and exclusion rules are explicit, and the mapping onto four groups is documented.
**Evidence Anchor**: text: §3.1 "We do not write cases or assign labels ourselves. All 52 cases come from two public English vignette sets with physician labels"

### S2: The folk-label manipulation is placed correctly against perturbation work
The paper separates a folk label, which names a different illness, from typo-style noise. It also treats diacritic removal as a script-level perturbation specific to Vietnamese. This framing is accurate and sharper than "noisy input".
**Evidence Anchor**: text: §2 "Our folk-wording change differs in kind: it keeps the signs but adds a culturally standard lay diagnosis that points to a benign condition."

### S3: The mechanism is offered as a hypothesis, with an honest limit
The red-flag-dropping account rests on two examples, is called a hypothesis, and comes with a concrete check left for future work. Diacritic restoration is proposed as a defence together with its own risk (a restoration error could change a sign).
**Evidence Anchor**: text: §6 "We read this as a hypothesis: the emergency may be lost before any triage reasoning starts. Two examples cannot show it"

### S4: Over-triage and harmless-remedy controls
The control cases, and the harmless remedies attached to them, let the reader tell lower urgency from general caution, and real sycophancy from blanket rejection of folk medicine. This is the right design for a triage-shift claim.
**Evidence Anchor**: text: §3.2 "On the controls a model can accept a harmless remedy, which separates real sycophancy from a habit of rejecting all folk medicine."

### Weaknesses

### W1: The folk register is LLM-authored and has no anchor in real Vietnamese user text
The treatment condition for RQ1 is the folk version. An LLM drafted it, and a non-clinician first author edited it. The two raters who checked equivalence and naturalness also used an LLM as an aid, which the paper itself says makes their ratings "not fully independent". Agreement on equivalence was κ = 0.15. Nothing shows that the folk wording matches how Vietnamese laypeople actually write health questions online, for example through a comparison with public Vietnamese health forum or consumer-QA text in lexical choice, length and folk-label frequency.

As written, RQ1 measures the effect of LLM-imagined folk Vietnamese. That is a real but narrower claim than the title and abstract suggest. Folk-label usage in particular may be over- or under-represented compared with real messages. The paper does name some of this: the limitations say real messages are "longer and messier" and that the vocabulary is Southern only. But the main text and abstract present the folk effect without this qualifier.

Minimum fix: state in the abstract and introduction that the folk versions are author-constructed, LLM-assisted rewrites. Stronger option, at moderate cost: sample real public Vietnamese health questions and report how often the lexicon terms appear and how long such questions are, so the register is anchored externally.
**Severity**: Major
**Evidence Anchor**: text: §3.2 Authorship "The translations, folk versions, remedies and lexicon glosses were drafted with an LLM (Claude)."
**Confidence**: 4 — Vietnamese NLP and dataset-construction experience

### W2: The "folk-term lexicon" mixes folk-illness categories with ordinary colloquial and standard vocabulary
The paper presents 34 "folk terms" as folk-illness labels. Several are true folk or traditional explanatory categories: trúng gió, nóng trong, thận yếu, phong thấp, vong theo, máu huyết không lưu thông. Many others are not. Chuột rút (cramp), tức ngực (chest tightness), hụt hơi (shortness of breath), lẹo (stye), giời leo (shingles), nhiệt miệng (mouth ulcer), đau mắt đỏ (conjunctivitis) and tăng xông (hypertension) are standard or colloquial Vietnamese symptom and disease words, not folk explanations. Đau bao tử is Southern lay vocabulary, as the paper itself notes.

The "lay meaning" column was LLM-drafted and reviewed by the first author. It cites no ethnographic or medical-anthropology source. This bears directly on the released resource, which contribution 1 lists as "a lexicon of 34 folk terms", and on how the per-condition findings are read. For example, "folk wording mattered more where the signs are less specific" depends on whether the label is explanatory (nóng trong) or merely colloquial.

Fix: split the lexicon into (a) folk-illness or explanatory labels and (b) lay or dialectal symptom vocabulary. Add a source for each gloss where one exists, and mark the rest as author-provided.
**Severity**: Major
**Evidence Anchor**: table: Appendix B, Table 4 (tab:lexicon), rows chuột rút, tức ngực, hụt hơi, lẹo, giời leo, nhiệt miệng
**Confidence**: 4 — native-level knowledge of Vietnamese lay medical vocabulary; no ethnographic source consulted

### W3: The headline diacritic effect comes from a full-strip worst case whose prevalence the paper does not document
Every diacritic and đ is removed by Unicode decomposition. The paper calls this "a controlled worst case" in §3.2 only. It gives no evidence of how often Vietnamese users type health questions with no diacritics at all, as opposed to partly accented text, Telex or VNI residue, or abbreviations and teencode (ko, k, dc). The limitations section does not return to the point.

Yet the abstract ("Missing diacritics cause most of the harm") and the conclusion turn this condition into the main practical finding and recommendation. Fully stripped Vietnamese is also much more lexically ambiguous than typical real unaccented input, which often keeps some marks. The 25-point effect may therefore be an upper bound.

Fix: qualify the abstract and conclusion ("fully unaccented"). Add a sentence with whatever evidence exists on how common unaccented Vietnamese input is, or state that it is unknown. A partial-diacritic condition (for example, random removal at 30–70% of syllables) would bound the effect, but that is optional.
**Severity**: Major
**Evidence Anchor**: text: §3.2 "This is a controlled worst case; real users may type with partial or inconsistent diacritics." and Abstract "Missing diacritics cause most of the harm"
**Confidence**: 4 — diacritic restoration and unaccented-Vietnamese processing experience

### W4: Framing claims about Vietnamese folk illness have no source, and "usually benign" is questionable for trúng gió
The introduction states that "many Vietnamese" use folk-illness labels for acute symptoms and that facial droop "is often called trúng gió". It cites nothing, not even ethnographic or public-health literature on trúng gió or cạo gió. It also says a folk label "names a different, usually benign, illness". In common Vietnamese understanding, trúng gió can be sudden and serious; it is not reliably a benign category. The paper's own result, that models were not misled on the trúng gió stroke case, fits that reading.

Fix: cite sources for the prevalence of folk-illness usage, or soften these to stated assumptions. Qualify "usually benign" per term; the lexicon split in W2 would support that.
**Severity**: Minor
**Evidence Anchor**: text: §1 "First, many Vietnamese describe acute symptoms with folk-illness labels." and §1 "Unlike a typo, a folk label is not noise: it names a different, usually benign, illness."
**Confidence**: 3 — native-speaker knowledge, no source verified in this session

### W5: The Discussion heading states the diacritic mechanism as fact, and a Vietnamese-specific alternative is not discussed
The next paragraph correctly calls the account a hypothesis (S3). But the heading "the model misreads the signs" and the sentence "they failed to read them" state it as established. The conclusion repeats it ("in our examples made models drop the signs").

There is also a plausible alternative specific to Vietnamese that the paper does not raise. Stripping diacritics makes many syllables ambiguous, since several distinct accented words collapse onto one unaccented form. Subword tokenisation of unaccented Vietnamese also differs from that of accented text. The model may decode a different but coherent reading rather than fail to read at all. These alternatives predict different remedies: restoration helps under ambiguity, tokenizer-level fixes under fragmentation.

Fix: soften the heading and the conclusion sentence. Name ambiguity and tokenisation as competing explanations.
**Severity**: Minor
**Evidence Anchor**: text: §6 "The answers suggest that the models did not weigh the signs differently; they failed to read them."
**Confidence**: 4 — Vietnamese tokenisation and diacritic ambiguity are within my expertise

### W6: Related work omits cross-lingual health-LLM evaluation and Vietnamese health QA resources
The scoped novelty claim (first triage test on folk-worded and unaccented Vietnamese) is plausible, and nothing I know of undercuts it. But the Vietnamese side has a single cited benchmark (VM14K). Vietnamese consumer-health and medical QA datasets are left out, as is cross-lingual work showing that LLM health answers degrade in non-English languages. The latter is the closest context for the "English-only prior work" framing. The diacritic-restoration paragraph cites a multilingual neural model but no Vietnamese-specific restoration work.

Fix: add a short paragraph on cross-lingual health-LLM evaluation and on Vietnamese health QA, and cite at least one Vietnamese diacritic-restoration study. See the references below; the Vietnamese items are search leads.
**Severity**: Minor
**Evidence Anchor**: text: §2 "We are not aware of work that measures lay phrasing, folk-illness terms or missing diacritics in Vietnamese health questions."
**Confidence**: 3 — field familiarity; no literature search run in this session

### W7: The released resource has no stated licence, schema or location
The paper releases cases, a lexicon, outputs and labels, and mentions a data card with a content warning and per-remedy flags. It does not say which licence the derived Vietnamese texts and lexicon carry (the sources are MIT and CC0), what fields a record has (case id, source id, gold group, version, remedy-documented flag, source URL for documented remedies), or where the release will live. A placeholder is fine while the paper is anonymised.

These are the minimum facts another group needs to build on the set. Documentation frameworks such as datasheets and data statements cover them (see references). Whether this venue requires them is unverified.
**Severity**: Minor
**Evidence Anchor**: absence: Ethics Statement and Conclusion — expected licence, record schema and release location for the cases, lexicon and outputs; checked abstract, contributions list, §3, Ethics Statement, Conclusion, Appendices A–B
**Confidence**: 4 — dataset release experience

### Missing Key References
- Jin et al. (2024), cross-lingual evaluation of LLMs on healthcare queries. It shows that answer quality drops in non-English languages, which is relevant context for the English-only framing.
- Gebru et al. (2021), datasheets for datasets, and Bender & Friedman (2018), data statements. Both are documentation frameworks for the release (W7).
- [UNVERIFIED] Search lead: Vietnamese medical and consumer-health QA datasets, for example work introducing ViHealthQA or ViMQ.
- [UNVERIFIED] Search lead: Vietnamese-specific diacritic restoration, for example sequence-to-sequence or transformer models evaluated on Vietnamese news or social text.
- [UNVERIFIED] Search lead: medical-anthropology or public-health studies of trúng gió, cạo gió and Vietnamese folk illness explanations.

~~~yaml suggested-references
- title: "Better to Ask in English: Cross-Lingual Evaluation of Large Language Models for Healthcare Queries"
  authors: ["Jin, Y.", "Chandra, M.", "Verma, G.", "Hu, Y.", "De Choudhury, M.", "Kumar, S."]
  year: "2024"
  doi: null
  arxiv_id: null
- title: "Datasheets for Datasets"
  authors: ["Gebru, T.", "Morgenstern, J.", "Vecchione, B.", "Vaughan, J. W.", "Wallach, H.", "Daumé III, H.", "Crawford, K."]
  year: "2021"
  doi: "10.1145/3458723"
  arxiv_id: null
- title: "Data Statements for Natural Language Processing: Toward Mitigating System Bias and Enabling Better Science"
  authors: ["Bender, E. M.", "Friedman, B."]
  year: "2018"
  doi: "10.1162/tacl_a_00041"
  arxiv_id: null
~~~

### Questions for Authors
1. How were the folk labels chosen for each case? Was the selection checked against real Vietnamese user text, or only against the LLM draft and the author's judgement?
2. Can you separate the explanatory folk labels from the lay and dialectal vocabulary in the lexicon, and report the RQ1 effect for cases that carry an explanatory label?
3. Do you have any evidence on how often Vietnamese health questions are typed with no diacritics at all?
4. Under what licence will the derived Vietnamese cases and the lexicon be released?
