# Solutions — Lesson 0.10

Back to the lesson: [[lesson-0.10-mini-project-semantic-search]]

Your exact numbers depend on the model version and library versions. What matters is the **pattern** and your explanation of it.

## Warm-up
1. Pass 1 (10 min: title, abstract, intro, headings, figures, conclusion) → pass 2 (1 hour: method, figures, tables) → pass 3 (deep, only for papers you build on).
2. Dot product of the two vectors divided by the product of their lengths.
3. The same visible text can be stored as composed (NFC) or decomposed (NFD) characters; normalising makes equal-looking strings actually equal, so matching and counting work.

## Day 1

1. The queries were written with *different words* from the answers on purpose, so keyword search is weak here: it gets the gold answer first for only 7 of 16 queries (Hit@1 ≈ 0.44). A decent multilingual embedding model should beat that clearly on Hit@1 and MRR. If yours does not, check that you used `normalize_embeddings=True` and NFC-normalised the documents.
2. Example: "laptop ì ạch phải xử lý sao" vs "Khi **máy tính** chạy **chậm**, hãy gỡ bớt phần mềm…". "laptop" ≈ "máy tính", "ì ạch" ≈ "chậm" — same meaning, zero shared words, so keyword overlap is 0 for the gold answer. Embeddings can capture the synonymy.
3. Typical confusions are between neighbours in meaning, e.g. a query about a passport ranking the ID-card answer first (both are documents from public offices). Such errors are "understandable": the model sees the right topic but not the precise detail.

## Day 2

### Part 1 — expected pattern
- **Keyword search collapses** on diacritic-free queries: "bang lai" shares no words with "bằng lái", so only syllables that have no diacritics anyway ("ve", "o"…) can match.
- **Semantic search usually drops too**, often a lot, because the multilingual model saw little diacritic-free Vietnamese during training. How much it drops is exactly the kind of number idea 1B/2A measures at scale.

### Part 2 — fixes

```python
# assumes the Day 1 + Day 2 code above has run: doc_texts, doc_ids, model, words, evaluate, strip_diacritics, queries
import numpy as np

doc_texts_stripped = [strip_diacritics(t) for t in doc_texts]
D_stripped = model.encode(doc_texts_stripped, normalize_embeddings=True)

# Fix A — strip both sides
def keyword_scores_stripped(query):
    q = words(strip_diacritics(query))
    return np.array([len(q & words(t)) / len(q | words(t)) for t in doc_texts_stripped])

def semantic_scores_stripped(query):
    q = model.encode([strip_diacritics(query)], normalize_embeddings=True)[0]
    return D_stripped @ q

# Fix B — hybrid: keyword on stripped text + semantic on original docs
def hybrid_scores(query, alpha=0.5):
    return alpha * keyword_scores_stripped(query) + (1 - alpha) * semantic_scores(query)

for name, fn in [("keyword-stripped", keyword_scores_stripped),
                 ("semantic-stripped", semantic_scores_stripped),
                 ("hybrid", hybrid_scores)]:
    print(name, "clean:", evaluate(fn, queries),
          "noisy:", evaluate(fn, queries, transform=strip_diacritics))
```

4. Typical outcome: **stripping both sides fully rescues keyword search** (clean and noisy become identical, because the query is stripped anyway) and helps semantic search on noisy queries. The price: stripping throws information away ("ban" could be bán/bàn/bạn), so on clean queries the stripped versions can be slightly *worse* than the original. Hybrid often gives the best balance. Whatever you got, the important habit is reporting **both** clean and noisy numbers — a fix that only looks at noisy data can hide damage to normal users.

5. With 16 queries, a difference of one query (6.25 points) can easily be luck: a slightly different set of 16 queries could flip the ranking of the two methods. Real papers use hundreds to thousands of queries, several datasets, and confidence intervals (bootstrap, Phase 2). Rough guide: 500+ queries per condition to trust differences of a few points.

6.
```python
# assumes strip_diacritics, evaluate, keyword_scores_stripped, semantic_scores, queries from above
import random
import matplotlib.pyplot as plt

def partial_strip(text, ratio, seed=0):
    rng = random.Random(seed)
    ws = text.split()
    chosen = set(rng.sample(range(len(ws)), round(len(ws) * ratio)))
    return " ".join(strip_diacritics(w) if i in chosen else w for i, w in enumerate(ws))

ratios = [0, 0.25, 0.5, 0.75, 1.0]
for name, fn in [("keyword", keyword_scores), ("semantic", semantic_scores)]:
    hit1 = [evaluate(fn, queries, transform=lambda q, r=r: partial_strip(q, r))["Hit@1"] for r in ratios]
    plt.plot(ratios, hit1, marker="o", label=name)
plt.xlabel("share of words without diacritics"); plt.ylabel("Hit@1"); plt.legend(); plt.show()
```
`lambda q, r=r: ...` freezes the current value of `r` inside the loop (a classic Python gotcha: without `r=r`, every lambda would use the last value). Expect a downward curve; whether it is a straight line or falls off a cliff after some ratio is an interesting observation for your notes.

## Challenge

7. Stronger embedding models (larger, trained on more multilingual data) often have higher clean scores and a smaller noisy drop, but rarely zero drop. Read each model card for required prefixes (e5 models expect `"query: "` and `"passage: "`) — forgetting them silently lowers scores, a common mistake even in published work.
