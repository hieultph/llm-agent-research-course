# Lesson 0.3 — Vectors and similarity

> [!summary] Tóm tắt (VI)
> Vectơ chỉ là một danh sách số, và cũng là một mũi tên. LLM biến mọi chữ thành vectơ, nên hiểu vectơ là hiểu cách máy "nắm nghĩa".
> Học ba phép: cộng, nhân với một số, và tích vô hướng. Từ tích vô hướng suy ra độ tương đồng cosin: hai mũi tên cùng hướng thì nghĩa gần nhau.
> Toán ở đây chỉ cần nhân, cộng và căn bậc hai. Mọi công thức đều có ví dụ tính tay trước.

**Time:** 2 hours · **You need:** NumPy (`pip install numpy matplotlib`) · **Math:** ✏️ gentle

## Glossary

| English | Tiếng Việt | One-line meaning |
|---|---|---|
| vector | vectơ | A list of numbers = an arrow |
| dimension | chiều | How many numbers the vector has |
| element / component | phần tử / thành phần | One number inside the vector |
| scalar | vô hướng (một số) | A single number |
| dot product | tích vô hướng | Multiply matching pairs, add them up |
| length (norm) | độ dài (chuẩn) | How long the arrow is |
| cosine similarity | độ tương đồng cosin | How much two arrows point the same way, −1 to 1 |
| embedding | vectơ nhúng | A vector that represents the meaning of a word or sentence |
| NumPy array | mảng NumPy | Python's fast container for vectors and matrices |

## Warm-up (5 min, no peeking)

1. Write a list comprehension that gives the squares of `[1, 2, 3]`.
2. Why do Vietnamese words take more bytes in UTF-8 than plain English letters?
3. What does `zip(a, b)` do?

---

## Part 1 — A vector is a list of numbers, and an arrow (Pomodoro 1)

### Everyday example

You want to describe phones with numbers so a computer can compare them:

| Phone | Price (million VND) | Battery (hours) |
|---|---|---|
| A | 3 | 1 |
| B | 1 | 2 |

Phone A becomes the **vector** `[3, 1]`, phone B becomes `[1, 2]`. Each number is one **dimension**. Two numbers → 2 dimensions → we can draw it on paper as an arrow from the origin `(0, 0)` to the point.

![Vectors as arrows](vectors_2d.png)

Real embeddings have 384, 768 or 4,096 dimensions. You cannot draw that, but **everything you learn in 2-D works the same way in 4,096-D**. That is the magic: draw in 2-D, trust the maths for the rest.

### Two basic operations

**Add:** add matching numbers. On the picture: put arrow b at the tip of arrow a.

```
[3, 1] + [1, 2] = [3+1, 1+2] = [4, 3]
```

**Scale (multiply by one number):** stretch or shrink the arrow.

```
2 × [3, 1] = [6, 2]        (twice as long, same direction)
-1 × [3, 1] = [-3, -1]     (same length, opposite direction)
```

### In NumPy

Python lists do not do this maths. NumPy arrays do, and they are hundreds of times faster.

```python
import numpy as np

a = np.array([3, 1])
b = np.array([1, 2])
print(a + b)       # [4 3]
print(2 * a)       # [6 2]
print(a * b)       # [3 2]   <- multiplies matching pairs (not the dot product yet!)
print(a.shape)     # (2,)    <- a vector with 2 numbers
```

---

## Part 2 — Dot product, length, cosine similarity (Pomodoro 2)

### Dot product: multiply pairs, add them up

```
a = [3, 1]
b = [1, 2]

a · b = 3×1 + 1×2 = 3 + 2 = 5
```

That is all. For 4,096 dimensions you do 4,096 multiplications and add them. Computers love this.

What does it *mean*? Think of a shopping list and prices:

```
quantities = [2, 1, 3]          (2 bánh mì, 1 cà phê, 3 trứng)
prices     = [15, 25, 4]        (thousand VND each)
quantities · prices = 2×15 + 1×25 + 3×4 = 30 + 25 + 12 = 67   -> total bill
```

The dot product is a **weighted sum**. Every neural network layer is made of millions of them.

### Length: Pythagoras again

You remember the right triangle 3–4–5: the long side is √(3² + 4²) = √25 = 5. The length of an arrow is the long side of a triangle drawn under it:

```
length of a = √(3² + 1²) = √10 ≈ 3.162
length of b = √(1² + 2²) = √5  ≈ 2.236
```

Notice: length = √(a · a). The dot product of a vector with itself is its squared length.

### Cosine similarity: do they point the same way?

Long arrows give big dot products just because they are long. To compare **direction only**, divide by both lengths:

$$
\text{cosine}(a, b) = \frac{a \cdot b}{\text{length}(a) \times \text{length}(b)}
$$

Read the formula as: "dot product, but with the effect of length removed".

By hand:

```
cosine(a, b) = 5 / (3.162 × 2.236) = 5 / 7.071 ≈ 0.707
```

0.707 means the arrows are 45° apart — fairly similar.

![Cosine similarity cases](dot_product_cosine.png)

| Cosine | Arrows | Meaning for embeddings |
|---|---|---|
| close to 1 | same direction | very similar meaning |
| close to 0 | at right angles | unrelated |
| close to −1 | opposite | opposite (rare in practice for text) |

```python
import numpy as np

def cosine(u, v):
    return np.dot(u, v) / (np.linalg.norm(u) * np.linalg.norm(v))

a = np.array([3, 1])
b = np.array([1, 2])
print(np.dot(a, b))              # 5
print(np.linalg.norm(a))         # 3.162...
print(cosine(a, b))              # 0.707...
print(cosine(a, 10 * a))         # 1.0  -> length does not matter, only direction
```

---

## Part 3 — Embeddings: meaning as arrows (Pomodoro 3)

An **embedding model** turns a word or sentence into a vector so that **similar meanings get similar directions**. Nobody writes these numbers by hand — the model learns them from huge amounts of text (Phase 1 shows how).

![Toy embedding map](embedding_map.png)

This picture is a toy in 2-D, but real embeddings behave like it: animals cluster, cities cluster, and even *relationships* become directions (man → woman is roughly the same arrow as king → queen).

Let us fake some 4-D embeddings to practise:

```python
import numpy as np

emb = {
    "mèo":    np.array([0.9, 0.8, 0.1, 0.0]),
    "chó":    np.array([0.8, 0.9, 0.2, 0.0]),
    "cá":     np.array([0.7, 0.3, 0.1, 0.1]),
    "Hà Nội": np.array([0.0, 0.1, 0.9, 0.8]),
    "Huế":    np.array([0.1, 0.0, 0.8, 0.9]),
}

def cosine(u, v):
    return np.dot(u, v) / (np.linalg.norm(u) * np.linalg.norm(v))

words = list(emb)
print(" " * 8 + "".join(f"{w:>8}" for w in words))
for w1 in words:
    row = "".join(f"{cosine(emb[w1], emb[w2]):8.2f}" for w2 in words)
    print(f"{w1:>8}" + row)
```

You will see high numbers inside the animal group and inside the city group, low numbers between groups.

### Search = "which vector is closest?"

```python
def most_similar(query_word, k=2):
    q = emb[query_word]
    scores = [(w, cosine(q, v)) for w, v in emb.items() if w != query_word]
    return sorted(scores, key=lambda p: p[1], reverse=True)[:k]

print(most_similar("mèo"))
```

This is exactly how the "retrieval" part of RAG works: embed the question, embed every document, return the documents with the highest cosine. You will build a real one in Lesson 0.10.

> [!example] Research hook
> What happens to the embedding of "toi muon dat ve" compared with "tôi muốn đặt vé"? If the model puts them far apart, search breaks for users who type without diacritics. Measuring and fixing that gap is paper ideas 1B, 1D and 2A.

---

## Exercises (Pomodoro 4)

### A. By hand (paper + calculator)

1. `u = [2, 0]`, `v = [0, 5]`. Compute `u · v` and cosine(u, v). What angle is between them?
2. `u = [1, 2, 3]`, `v = [4, 5, 6]`. Compute `u · v`.
3. Length of `[6, 8]`?
4. Why is cosine(a, 10·a) equal to 1?
5. Two sentence embeddings have cosine 0.95, two others have 0.20. Which pair is more likely to mean similar things?

### B. Code

6. Without `np.dot` or `np.linalg.norm`, write `my_dot(u, v)` and `my_norm(u)` using a loop or comprehension over Python lists. Check they match NumPy.
7. Add two more words to the toy `emb` dictionary (e.g. "Đà Nẵng", "chim") with your own made-up vectors so they land in the right group. Check with `most_similar`.
8. Generate 1,000 random 384-D vectors with `np.random.randn(1000, 384)`. Compute the cosine between the first vector and each of the others. What is the average? What does this tell you about random high-dimensional vectors?

### C. Challenge (optional)

9. Compute the "analogy" `emb["king"] - emb["man"] + emb["woman"]` using these toy vectors and find the closest word (excluding the three input words):
   ```python
   emb2 = {
       "king":  np.array([0.9, 0.9, 0.1]),
       "queen": np.array([0.9, 0.1, 0.9]),
       "man":   np.array([0.1, 0.9, 0.1]),
       "woman": np.array([0.1, 0.1, 0.9]),
       "apple": np.array([0.5, 0.5, 0.5]),
   }
   ```

➡️ Answers: [[solution-0.3]]

## Feynman box

In 5 lines: what a vector is, what the dot product does, and why cosine similarity is used for search.

## Key takeaways

- A vector = a list of numbers = an arrow. Pictures in 2-D generalise to any dimension.
- Dot product = multiply pairs and add. Cosine = dot product with lengths divided out.
- Embeddings put similar meanings in similar directions; search = find the highest cosine.

**Next:** [[lesson-0.4-matrices]]
