# Solutions — Lesson 0.7

Back to the lesson: [[lesson-0.7-pytorch-basics]]

## Warm-up
1. `w ← w − learning_rate × slope` (for every weight)
2. Steps overshoot the bottom; the loss bounces up and can explode to `inf`/`nan`.
3. It uses the chain rule to compute the gradient of the loss with respect to every weight, going backwards from the loss.

## A. Check your understanding

1. forward → loss → zero_grad → backward → step. Without zero_grad, gradients from earlier steps keep adding up, so each update uses a sum of old and new gradients — steps get too big and training goes wrong.
2. Tells PyTorch to record operations on this tensor so it can compute its gradient later.
3. Derivative of 3x² is 3 × 2x = 6x. At x = 2: **12**.
4. Some tensors are on the GPU and others on the CPU (often the data, or a new tensor created inside the loop). Move everything with `.to(device)`, and create new tensors with `device=device`.
5. float16: 3 billion × 2 bytes = 6 GB — the weights alone fill your RTX 3050, so it will not run. 4-bit: 3 billion × 0.5 = 1.5 GB — fits comfortably.

## B. Code

6.
```python
import torch
x = torch.tensor(2.0, requires_grad=True)
y = 3 * x ** 2
y.backward()
print(x.grad)   # tensor(12.)
```

7. Without `zero_grad`, the gradient after n steps is the sum of all n gradients so far, so each update keeps "remembering" old directions. In a test run the loss went **up** for the first ~20 steps (from about 9 to 13), then swung around and settled near 1.0 — far worse than the ~0.1 of the correct loop. Your numbers may differ; the point is that training stops behaving like gradient descent.

8.
```python
import torch
from torch import nn
import matplotlib.pyplot as plt

def train(hidden):
    torch.manual_seed(0)
    net = nn.Sequential(nn.Linear(1, hidden), nn.ReLU(), nn.Linear(hidden, 1))
    x = torch.linspace(-3, 3, 200).unsqueeze(1)
    y = torch.sin(x)
    opt = torch.optim.Adam(net.parameters(), lr=0.01)
    for _ in range(2000):
        loss = nn.functional.mse_loss(net(x), y)
        opt.zero_grad(); loss.backward(); opt.step()
    return net, x, y, loss.item()

for h in [4, 32, 128]:
    net, x, y, final = train(h)
    print(h, round(final, 5))
    with torch.no_grad():
        plt.plot(x, net(x), label=f"{h} hidden units")
plt.plot(x, y, "k--", label="sin(x)"); plt.legend(); plt.show()
```
With 4 units the fit is a rough zig-zag (few "bends" available; final loss about 0.12); 32 and 128 units fit closely (loss near 0). More units = more capacity. In LLMs, capacity grows with layers and width — and so does memory.

## C. Challenge

9. Without ReLU, `Linear → Linear` is still one straight line (a matrix times a matrix is just another matrix). The best straight line through a sine wave from −3 to 3 leaves a large error (final loss about 0.17, versus about 0.00003 with ReLU and 32 units). The non-linearity is what lets networks bend. Every transformer layer in Phase 1 contains such a non-linearity.
