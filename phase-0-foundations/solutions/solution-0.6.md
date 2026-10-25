# Solutions — Lesson 0.6

Back to the lesson: [[lesson-0.6-derivatives-and-gradient-descent]]

## Warm-up
1. `[0.5, 0.5]`
2. Small: −ln(0.9) ≈ 0.105.
3. They become more even (flatter); the top token loses probability, unlikely tokens gain.

## A. By hand

1. 15 / 300 = 0.05
2. 2 × 5 = 10 and 2 × (−5) = −10. At x = 5, moving right goes up (positive); at x = −5, moving right goes down (negative) — you are on the left side of the valley.
3. Each step: w − 0.1 × 2w = 0.8w → 8, 6.4, 5.12. Steady progress toward 0.
4. lr = 1.0: w − 2w = −w → −10, 10, −10… bounces forever, never improves. lr = 1.5: w − 3w = −2w → −20, 40, −80… explodes (diverges).
5. Too low → `prediction − truth` is negative → slope for b is negative → `b − lr × (negative)` = b goes **up**. Correct: predictions were too low, so raising b helps.

## B. Code

6.
```python
def numerical_slope(f, x, h=1e-5):
    return (f(x + h) - f(x)) / h

g = lambda x: 3 * x ** 2 + 2 * x + 1
for x in [0, 1, 2]:
    print(x, round(numerical_slope(g, x), 3))   # 2, 8, 14
```
The slope grows by 6 for each step in x and is 2 at x = 0 → rule `6x + 2`. (Using the table: 3·x² → 3 × 2x = 6x, 2x → 2, the constant 1 → 0.)

7.
```python
import numpy as np

rng = np.random.default_rng(0)
area = rng.uniform(0.2, 1.0, 40)
price = 5.0 * area + 0.5 + rng.normal(0, 0.35, 40)

def loss_fn(w, b):
    return np.mean((w * area + b - price) ** 2)

w, b, lr, h = 0.0, 0.0, 0.5, 1e-6
for step in range(501):
    gw = (loss_fn(w + h, b) - loss_fn(w, b)) / h
    gb = (loss_fn(w, b + h) - loss_fn(w, b)) / h
    w -= lr * gw
    b -= lr * gb
print(round(w, 3), round(b, 3))    # same as the formula version (to ~3 decimals)
```
Numerical slopes give the same answer but need 2 extra loss computations **per weight**. For a model with 7 billion weights that is impossible — which is why backpropagation (exact slopes for all weights in one backward pass) matters.

8.
```python
import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng(0)
area = rng.uniform(0.2, 1.0, 40)
price = 5.0 * area + 0.5 + rng.normal(0, 0.35, 40)

for lr in [0.05, 0.5, 2.0]:
    w, b, history = 0.0, 0.0, []
    for step in range(100):
        err = w * area + b - price
        history.append(np.mean(err ** 2))
        w -= lr * 2 * np.mean(err * area)
        b -= lr * 2 * np.mean(err)
    plt.plot(history, label=f"lr={lr}")
plt.yscale("log"); plt.xlabel("step"); plt.ylabel("loss (log scale)"); plt.legend()
plt.show()
```
lr = 0.05 decreases slowly; lr = 0.5 drops fast and flattens; lr = 2.0 shoots upward (diverges). The log scale makes all three visible on one chart.

## C. Challenge

9. With areas 20–100, `area × error` is huge, so the slope for w is huge and lr = 0.5 explodes immediately (`inf`/`nan`). A working learning rate is around 0.0001 — thousands of times smaller. But then b (whose slope does not involve area) learns extremely slowly: you need tens of thousands of steps. Large inputs make different weights need very different step sizes; scaling the inputs fixes this. This is why every deep learning pipeline normalises its inputs, and why Phase 1 introduces "layer normalisation" inside transformers.
