# Solutions — Lesson 0.9

Back to the lesson: [[lesson-0.9-reading-research-papers]]

## Warm-up
1. The logits for the **last** input position of the first (only) text in the batch — the scores for the next token after the whole prompt.
2. Average number of tokens per word (tokens ÷ words).
3. Local: free and private, full control of the version. Hosted: access to much larger, stronger models.

## A. Pass 1 — model notes

Your wording will differ; check that you captured the same essentials.

**1. Attention Is All You Need (2017)**
- Category: method.
- Context: sequence-to-sequence models for translation built on recurrent networks (RNNs) plus attention.
- Contribution: the **Transformer**, an architecture using only attention (no recurrence), which reached better translation quality while training faster because it processes all positions in parallel.
- Why it matters for you: every LLM is a Transformer. Phase 1 rebuilds it.

**2. How Robust Are LLMs to Vietnamese Dialects? (2026)**
- Category: analysis / benchmark.
- Context: Vietnamese NLP datasets (emotion recognition, NLI, QA, multiple-choice QA) and robustness studies of LLMs.
- Contribution: human-written rewrites of 400 standard examples into six regional dialect groups (2,400 total); ten models tested; all lose accuracy on dialect input (about 2.8% on average), Central varieties hurt most, no model is fully invariant.
- Relevance: same family of problem as your ideas 1A/2A, different noise type.

**3. Which Works Best for Vietnamese? (EACL 2026 Findings)**
- Category: empirical study + resource.
- Context: lexical, sparse, dense, late-interaction and hybrid retrieval; Vietnamese and multilingual embedding models.
- Contribution: a reproducible comparison across ten datasets in six domains, two new QA datasets from real counselling and customer-service conversations, released data and scripts. Hybrid lexical+semantic retrieval is useful; model size predicts quality poorly.
- Relevance: its released datasets and scripts are a ready-made starting point for idea 2A.

## B. Questions

4. It does not test **diacritic removal or teen code**, and it does **not test mitigations** such as normalising dialect text to standard Vietnamese or normalisation-aware prompting. Your ideas 1A, 2A and 2D target exactly these gaps — this is how a limitations section becomes a research idea.
5. Depends on who counts it. Most institutions accept the **best** quartile across the journal's categories (Q2 here), but some require the quartile of the category that matches your field. Check your university's or funder's rule.
6. Check: is the journal indexed in Scopus *now* (Scopus Sources, and not on the discontinued list)? Its SJR page and quartile? Do the editors work in your field? Do past papers look like real research? 7-day review + unsolicited praise + fee are classic predatory signs — most likely ignore it.

## C. Challenge
No fixed answer. Keep the three pass-1 notes in your vault; they are the start of the related-work section for that idea.
