# Solutions — Lesson 0.5

Back to the lesson: [[lesson-0.5-probability-and-softmax]]

## Warm-up
1. (8, 3)
2. The dot product of one row of the left matrix with one column of the right matrix.
3. The bias: a vector added after the multiplication (an offset for each output).

## A. By hand

1. x = 1 − 0.5 − 0.2 − 0.2 = 0.1
2. `[1/3, 1/3, 1/3]`. Equal scores → equal exp values → each gets an equal share.
3. exp(0) = 1, exp(ln 3) = 3, total 4 → `[0.25, 0.75]`
4. −ln(0.25) = ln(4) = 2 × ln 2 ≈ 1.386
5. Model A (lower perplexity = less "surprised" by the text).
6. No. Dividing all scores by the same positive T keeps their order, so the highest score stays the highest. Temperature only changes *sampling*, not greedy choice.

## B. Code

7.
```python
import numpy as np

def softmax(z, temperature=1.0):
    z = np.asarray(z, dtype=float) / temperature
    e = np.exp(z - z.max())
    return e / e.sum()

logits = [3.0, 2.2, 1.6, 0.4, -0.5]
for t in [0.1, 0.5, 1, 2, 5]:
    print(t, round(float(softmax(logits, t).max()), 3))
# 0.1 -> ~1.0   0.5 -> ~0.79   1 -> ~0.56   2 -> ~0.38   5 -> ~0.27
```
As T → 0 the top token takes almost all the probability (= greedy). As T grows, all tokens approach the same probability (1/5 = 0.2) — pure randomness.

8.
```python
import numpy as np

def sequence_loss(p):
    losses = -np.log(np.asarray(p, dtype=float))
    avg = losses.mean()
    return avg, np.exp(avg)

print(sequence_loss([0.9, 0.8, 0.95]))   # (~0.127, ~1.14)  easy: perplexity close to 1
print(sequence_loss([0.1, 0.05, 0.2]))   # (~2.30, ~10.0)   hard: like choosing among ~10 words
```

9.
```python
import numpy as np

def softmax(z):
    z = np.asarray(z, dtype=float)
    e = np.exp(z - z.max())
    return e / e.sum()

rng = np.random.default_rng(0)
p = softmax([2, 1, 0])
draws = rng.choice(3, size=10_000, p=p)
print(p, np.bincount(draws) / 10_000)   # very close, e.g. [0.665 0.245 0.090] vs [0.66 0.25 0.09]
```
With many draws, the observed frequencies match the probabilities. With few draws they wobble — remember this when you evaluate models on small test sets (Phase 2: confidence intervals).

## C. Challenge

10.
```python
import numpy as np

def top_k_probs(probs, k):
    probs = np.asarray(probs, dtype=float)
    keep = np.argsort(probs)[-k:]          # indexes of the k largest
    out = np.zeros_like(probs)
    out[keep] = probs[keep]
    return out / out.sum()

p = np.array([0.55, 0.25, 0.14, 0.04, 0.02])
print(top_k_probs(p, 2))    # [0.6875 0.3125 0. 0. 0.]
```
Top-k stops the model from ever picking very unlikely (often nonsense) tokens while keeping some variety. A related method, **top-p (nucleus) sampling**, keeps the smallest set of tokens whose probabilities add up to p (e.g. 0.9). You will use both in Phase 2.
