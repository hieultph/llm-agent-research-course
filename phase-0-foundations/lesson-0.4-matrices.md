# Lesson 0.4 — Matrices

> [!summary] Tóm tắt (VI)
> Ma trận là bảng số. Nhân ma trận nghe đáng sợ nhưng thực ra chỉ là làm nhiều phép tích vô hướng cùng lúc: mỗi ô kết quả = một hàng nhân với một cột.
> Quy tắc vàng về kích thước: (m × n) nhân (n × p) ra (m × p), hai số ở giữa phải bằng nhau. Nắm quy tắc này là đọc được 80% code mạng nơ-ron.
> Mỗi lớp của mạng nơ-ron là "nhân ma trận rồi cộng thêm một vectơ". LLM là hàng trăm lớp như vậy chồng lên nhau.

**Time:** 2 hours · **You need:** NumPy · **Math:** ✏️ gentle (only multiply and add)

## Glossary

| English | Tiếng Việt | One-line meaning |
|---|---|---|
| matrix | ma trận | A table of numbers with rows and columns |
| row / column | hàng / cột | Horizontal line / vertical line of numbers |
| shape | kích thước | (number of rows, number of columns) |
| matrix–vector product | nhân ma trận với vectơ | One dot product per row |
| matrix multiplication | nhân hai ma trận | One dot product per (row, column) pair |
| transpose | chuyển vị | Swap rows and columns |
| weight matrix | ma trận trọng số | The learnable numbers in a neural network layer |
| bias | độ lệch (bias) | A vector added after the multiplication |
| batch | lô (batch) | Many examples processed together |
| broadcasting | lan truyền kích thước | NumPy stretching a smaller array to match a bigger one |

## Warm-up (5 min, no peeking)

1. Compute `[2, 3] · [4, 1]` by hand.
2. What does cosine similarity measure, in one sentence?
3. What is the length of `[3, 4]`?

---

## Part 1 — A matrix is a table; matrix × vector = many dot products (Pomodoro 1)

### Everyday example: university entrance scores

Three students, three subjects (Toán, Văn, Anh). That is a 3 × 3 table — a **matrix** of **shape** (3, 3):

|  | Toán | Văn | Anh |
|---|---|---|---|
| An | 8 | 7 | 9 |
| Bình | 6 | 9 | 8 |
| Chi | 9 | 6 | 7 |

A university counts Toán double: weights `w = [2, 1, 1]`. Each student's total is a **dot product** of their row with the weights:

```
An:   8×2 + 7×1 + 9×1 = 16 + 7 + 9 = 32
Bình: 6×2 + 9×1 + 8×1 = 12 + 9 + 8 = 29
Chi:  9×2 + 6×1 + 7×1 = 18 + 6 + 7 = 31
```

That is **matrix × vector**: one dot product per row. Result: a vector `[32, 29, 31]`, one number per student.

```python
import numpy as np

G = np.array([[8, 7, 9],
              [6, 9, 8],
              [9, 6, 7]])
w = np.array([2, 1, 1])

print(G.shape)     # (3, 3)
print(G @ w)       # [32 29 31]    <- @ means matrix multiplication
print(G[0])        # first row (An): [8 7 9]
print(G[:, 0])     # first column (Toán): [8 6 9]
```

`G[:, 0]` reads "all rows, column 0". The `:` means "everything".

---

## Part 2 — Matrix × matrix, and the shape rule (Pomodoro 2)

### Two weighting schemes at once

Another university counts Văn double: `[1, 2, 1]`. Put both schemes side by side as **columns** of a matrix `W` of shape (3, 2):

|  | Scheme 1 (Toán ×2) | Scheme 2 (Văn ×2) |
|---|---|---|
| Toán | 2 | 1 |
| Văn | 1 | 2 |
| Anh | 1 | 1 |

`G @ W` gives every student's total under every scheme — a (3, 2) result. Each cell = one row of G · one column of W:

```
An, scheme 2:   8×1 + 7×2 + 9×1 = 8 + 14 + 9 = 31
Bình, scheme 2: 6×1 + 9×2 + 8×1 = 6 + 18 + 8 = 32
Chi, scheme 2:  9×1 + 6×2 + 7×1 = 9 + 12 + 7 = 28
```

```python
W = np.array([[2, 1],
              [1, 2],
              [1, 1]])
print(G @ W)
# [[32 31]
#  [29 32]
#  [31 28]]
```

Under scheme 1 An wins; under scheme 2 Bình wins. Same data, different weights → different answer. That is what training a neural network does: it searches for the weights that give the answers we want.

### The shape rule — learn this by heart

![Matrix multiplication shapes](matmul_shapes.png)

```
(m × n) @ (n × p)  ->  (m × p)
      └──┘ must match
```

- The **inner** numbers must be equal (each row of the left has as many numbers as each column of the right).
- The result takes the **outer** numbers.

| Left | Right | Result |
|---|---|---|
| (3, 3) | (3,) vector | (3,) |
| (3, 3) | (3, 2) | (3, 2) |
| (32, 768) | (768, 3072) | (32, 3072) |
| (5, 4) | (5, 4) | ❌ error: 4 ≠ 5 |

When code crashes with `shapes (5,4) and (5,4) not aligned`, this rule is why. Fix: **transpose** one of them (swap rows and columns): `A @ B.T` is (5, 4) @ (4, 5) → (5, 5).

```python
A = np.ones((5, 4))
B = np.ones((5, 4))
print(B.T.shape)        # (4, 5)
print((A @ B.T).shape)  # (5, 5)
```

---

## Part 3 — Matrices inside neural networks (Pomodoro 3)

### A matrix transforms space

Multiplying every point of a grid by a matrix moves it: stretch, rotate, skew. A neural network layer reshapes its input space so that the answer becomes easy to read off.

![A matrix transforms the grid](matrix_transform.png)

### One layer of a neural network

$$
y = W x + b
$$

Read it as: "take input vector `x`, compute weighted sums with `W` (one per output), then add an offset `b`". Exactly the university example, plus `b`.

```python
rng = np.random.default_rng(0)
x = rng.standard_normal(4)          # input: 4 numbers
W = rng.standard_normal((3, 4))     # 3 outputs, each looks at 4 inputs
b = np.zeros(3)
y = W @ x + b
print(y.shape)                      # (3,)
```

An LLM is hundreds of these layers (plus a few other pieces you will meet in Phase 1). A "7B model" has about 7 billion numbers inside its `W`s and `b`s.

### The embedding table is a matrix

Give every token in a vocabulary an ID. Stack all their embedding vectors as rows: a matrix of shape (vocabulary size, embedding size). Looking up a token = taking one row.

```python
vocab = {"tôi": 0, "học": 1, "AI": 2}
E = rng.standard_normal((3, 5))      # 3 tokens, 5-D embeddings
ids = [vocab[t] for t in ["tôi", "học", "AI"]]
print(E[ids].shape)                  # (3, 5): one row per token
```

### Batches: many inputs at once

GPUs are fast because they process many inputs together. Stack 32 inputs as rows of `X` (32, 4); then `X @ W.T + b` gives (32, 3) — every output for every input in one go.

```python
X = rng.standard_normal((32, 4))
Y = X @ W.T + b          # b (3,) is "broadcast": added to every row
print(Y.shape)           # (32, 3)
```

**Broadcasting:** NumPy automatically repeats `b` for all 32 rows. Handy, but also a source of silent bugs — always print shapes.

> [!tip] The habit that saves hours
> Every time you write a matrix operation, write the expected shape in a comment: `Y = X @ W.T  # (32,4) @ (4,3) -> (32,3)`. In Phase 1 the shapes become (batch, sequence length, embedding size) and this habit is the only way to stay sane.

---

## Exercises (Pomodoro 4)

### A. By hand

1. Compute:
   ```
   [[1, 2],     @   [5,
    [3, 4]]          6]
   ```
2. Shape of the result? Or "error"?
   a. (4, 3) @ (3, 7)  b. (10, 768) @ (768,)  c. (2, 5) @ (2, 5)  d. (1, 3) @ (3, 1)
3. What is the transpose of `[[1, 2, 3], [4, 5, 6]]`, and its shape?
4. A layer takes 768 numbers in and gives 3,072 numbers out. What is the shape of `W` in `y = W x + b`? How many numbers are in `W` and `b` together?

### B. Code

5. Write `matvec(M, v)` using only Python lists and your `my_dot` from Lesson 0.3. Check it against `M @ v`.
6. Using the toy embeddings from Lesson 0.3, stack all 5 vectors into a matrix `E` of shape (5, 4). Normalise each row to length 1 (`E / np.linalg.norm(E, axis=1, keepdims=True)`). Then compute `S = E @ E.T`. What is `S`, and why is its diagonal all 1s?
7. Time it: compute 1,000 cosine similarities with a Python loop vs with one matrix multiplication (`%timeit` in a notebook, or `time.perf_counter()`). How many times faster is NumPy?

### C. Challenge (optional)

8. Matrix multiplication is **not** commutative: `A @ B` is usually not `B @ A`. Find two 2 × 2 matrices where they differ, and two where they are equal.

➡️ Answers: [[solution-0.4]]

## Feynman box

In 5 lines: what matrix multiplication computes (use the university example), and the shape rule.

## Key takeaways

- Matrix × vector = one dot product per row. Matrix × matrix = one dot product per (row, column).
- Shape rule: (m × n) @ (n × p) → (m × p). Write shapes in comments.
- A neural network layer is `W x + b`; an embedding table is a matrix; batches are rows.

**Next:** review day (Anki + redo wrong exercises), then [[lesson-0.5-probability-and-softmax]]
