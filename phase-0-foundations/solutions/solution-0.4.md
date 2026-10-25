# Solutions — Lesson 0.4

Back to the lesson: [[lesson-0.4-matrices]]

## Warm-up
1. 2×4 + 3×1 = 11
2. How much two vectors point in the same direction, ignoring their lengths (−1 to 1).
3. √(9 + 16) = 5

## A. By hand

1. Row 1: 1×5 + 2×6 = 17. Row 2: 3×5 + 4×6 = 39. Result `[17, 39]`.
2. a. (4, 7) b. (10,) c. error — inner numbers 5 and 2 differ d. (1, 1) — a single number in a 1×1 matrix (it is the dot product of two 3-D vectors).
3. `[[1, 4], [2, 5], [3, 6]]`, shape (3, 2).
4. `W` is (3072, 768): 3,072 outputs, each looking at 768 inputs. `W` has 3,072 × 768 = 2,359,296 numbers, `b` has 3,072. Total 2,362,368 — for **one** layer. Now you see where billions of parameters come from.

## B. Code

5.
```python
import numpy as np

def my_dot(u, v):
    return sum(x * y for x, y in zip(u, v))

def matvec(M, v):
    return [my_dot(row, v) for row in M]

M = [[8, 7, 9], [6, 9, 8], [9, 6, 7]]
v = [2, 1, 1]
print(matvec(M, v), np.array(M) @ np.array(v))   # [32, 29, 31] [32 29 31]
```

6.
```python
import numpy as np

emb = {
    "mèo":    [0.9, 0.8, 0.1, 0.0],
    "chó":    [0.8, 0.9, 0.2, 0.0],
    "cá":     [0.7, 0.3, 0.1, 0.1],
    "Hà Nội": [0.0, 0.1, 0.9, 0.8],
    "Huế":    [0.1, 0.0, 0.8, 0.9],
}
E = np.array(list(emb.values()))                        # (5, 4)
E_unit = E / np.linalg.norm(E, axis=1, keepdims=True)   # every row now has length 1
S = E_unit @ E_unit.T                                   # (5,4) @ (4,5) -> (5,5)
print(np.round(S, 2))
```
`S[i, j]` is the cosine similarity between word i and word j — **all 25 pairs in one multiplication**. Once vectors have length 1, cosine is just the dot product (dividing by 1×1 changes nothing). The diagonal is every word compared with itself: same direction → 1.
`keepdims=True` keeps the norms as a (5, 1) column so broadcasting divides each row by its own length.

7.
```python
import time
import numpy as np

rng = np.random.default_rng(0)
docs = rng.standard_normal((1000, 384))
q = rng.standard_normal(384)

t0 = time.perf_counter()
loop_scores = [float(np.dot(d, q) / (np.linalg.norm(d) * np.linalg.norm(q))) for d in docs]
t1 = time.perf_counter()
mat_scores = docs @ q / (np.linalg.norm(docs, axis=1) * np.linalg.norm(q))
t2 = time.perf_counter()

print(f"loop {t1 - t0:.4f}s, matrix {t2 - t1:.4f}s, speed-up ≈ {(t1 - t0) / (t2 - t1):.0f}x")
print(np.allclose(loop_scores, mat_scores))     # True: same numbers
```
Typical speed-up: tens to hundreds of times on a CPU, more on a GPU. Rule: **avoid Python loops over vectors; use matrix operations.**

## C. Challenge

8.
```python
import numpy as np

A = np.array([[1, 2], [0, 1]])
B = np.array([[1, 0], [1, 1]])
print(A @ B)   # [[3 2] [1 1]]
print(B @ A)   # [[1 2] [1 3]]   -> different

I = np.eye(2)  # identity matrix: 1s on the diagonal
print(np.allclose(A @ I, I @ A))   # True -> equal
```
Order matters in matrix multiplication. Equal cases are special: the identity matrix, a matrix with itself, or two matrices that both only scale (diagonal matrices).
