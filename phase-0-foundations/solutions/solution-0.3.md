# Solutions — Lesson 0.3

Back to the lesson: [[lesson-0.3-vectors-and-similarity]]

## Warm-up
1. `[x * x for x in [1, 2, 3]]` → `[1, 4, 9]`
2. Letters with marks (ô, ư, ạ, ế…) are stored with 2–3 bytes in UTF-8; plain English letters need 1 byte.
3. It walks two (or more) lists side by side, giving pairs `(a[0], b[0]), (a[1], b[1]), …`

## A. By hand

1. `u · v = 2×0 + 0×5 = 0`. Cosine = 0 / (2 × 5) = 0. The arrows are at 90° (one points right, one points up).
2. `1×4 + 2×5 + 3×6 = 4 + 10 + 18 = 32`
3. √(6² + 8²) = √(36 + 64) = √100 = 10
4. Multiplying by 10 makes the arrow longer but keeps its direction. Cosine only measures direction: (a · 10a) / (|a| × 10|a|) = 10|a|² / 10|a|² = 1.
5. The 0.95 pair: their arrows point almost the same way.

## B. Code

6.
```python
import math
import numpy as np

def my_dot(u, v):
    return sum(x * y for x, y in zip(u, v))

def my_norm(u):
    return math.sqrt(my_dot(u, u))

u, v = [1, 2, 3], [4, 5, 6]
print(my_dot(u, v), np.dot(u, v))            # 32 32
print(my_norm(u), np.linalg.norm(u))          # 3.7416... 3.7416...
```

7. Example (your numbers can differ — what matters is the pattern):
```python
import numpy as np

def cosine(u, v):
    return np.dot(u, v) / (np.linalg.norm(u) * np.linalg.norm(v))

emb = {
    "mèo":    np.array([0.9, 0.8, 0.1, 0.0]),
    "chó":    np.array([0.8, 0.9, 0.2, 0.0]),
    "cá":     np.array([0.7, 0.3, 0.1, 0.1]),
    "Hà Nội": np.array([0.0, 0.1, 0.9, 0.8]),
    "Huế":    np.array([0.1, 0.0, 0.8, 0.9]),
    "Đà Nẵng": np.array([0.05, 0.05, 0.85, 0.85]),   # big numbers in the "city" dimensions
    "chim":   np.array([0.8, 0.6, 0.2, 0.1]),        # big numbers in the "animal" dimensions
}

def most_similar(query_word, k=2):
    q = emb[query_word]
    scores = [(w, round(float(cosine(q, v)), 3)) for w, v in emb.items() if w != query_word]
    return sorted(scores, key=lambda p: p[1], reverse=True)[:k]

print(most_similar("Đà Nẵng"))   # Hà Nội / Huế on top
print(most_similar("chim"))      # animals on top
```

8.
```python
import numpy as np

rng = np.random.default_rng(0)
X = rng.standard_normal((1000, 384))
first = X[0]
cos = X[1:] @ first / (np.linalg.norm(X[1:], axis=1) * np.linalg.norm(first))
print(cos.mean(), cos.std())     # about 0.00 and about 0.05
```
Random vectors in high dimensions are almost always **nearly perpendicular** (cosine ≈ 0). So a cosine of 0.3 between two real embeddings is already a meaningful signal, not noise. (The `@` sign is matrix multiplication — next lesson.)

## C. Challenge

9.
```python
import numpy as np

emb2 = {
    "king":  np.array([0.9, 0.9, 0.1]),
    "queen": np.array([0.9, 0.1, 0.9]),
    "man":   np.array([0.1, 0.9, 0.1]),
    "woman": np.array([0.1, 0.1, 0.9]),
    "apple": np.array([0.5, 0.5, 0.5]),
}

def cosine(u, v):
    return np.dot(u, v) / (np.linalg.norm(u) * np.linalg.norm(v))

target = emb2["king"] - emb2["man"] + emb2["woman"]
print(target)                     # [0.9 0.1 0.9]
candidates = {w: cosine(target, v) for w, v in emb2.items() if w not in ("king", "man", "woman")}
print(max(candidates, key=candidates.get))   # queen
```
Reading the toy dimensions as [royalty, male, female]: removing "male" and adding "female" to "king" lands on "queen". Real embeddings show this only approximately.
