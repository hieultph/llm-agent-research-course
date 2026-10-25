# Solutions — Lesson 0.8

Back to the lesson: [[lesson-0.8-talking-to-an-llm]]

## Warm-up
1. forward → loss → zero_grad → backward → step
2. 1 billion × 2 bytes = 2 GB
3. Divides the logits before softmax: low temperature makes the distribution sharper (more confident), high temperature makes it flatter (more random).

## A. Check your understanding

1. The tokenizer works on UTF-8 **bytes**. A letter like "ế" takes 3 bytes; if those bytes are not merged into one token during tokenizer training, they are split across tokens.
2. 210 / 120 = 1.75 tokens per word.
3. 1 = batch size (one text), 9 = number of input tokens (one row of scores per position), 151,936 = vocabulary size (one score per possible next token).
4. Hosted models can be updated without notice. Without the date and exact model name, nobody — including you in 6 months — can reproduce or explain your results. Reviewers check this.

## B. Code

5.
```python
from transformers import AutoTokenizer

tok = AutoTokenizer.from_pretrained("Qwen/Qwen2.5-0.5B-Instruct")

def fertility(tokenizer, text):
    return len(tokenizer.encode(text, add_special_tokens=False)) / len(text.split())

texts = [
    "Tôi muốn đặt vé máy bay đi Đà Nẵng vào tối mai",
    "Toi muon dat ve may bay di Da Nang vao toi mai",
    "I want to book a flight to Da Nang tomorrow evening",
    "Căn cứ Nghị định số 13/2023/NĐ-CP về bảo vệ dữ liệu cá nhân",   # formal
    "ko bít mai có mưa ko nữa, chán ghê",                            # chatty
]
for t in texts:
    print(f"{fertility(tok, t):.2f}  {t}")
```
Your numbers depend on the tokenizer. Typical pattern: English lowest, standard Vietnamese higher, chatty/teen-code text different again. Diacritic-free text is sometimes *shorter* in tokens (plain ASCII letters merge easily) — yet models often understand it *worse*. That tension is exactly what idea 1A investigates: fewer tokens does not mean easier for the model.
`add_special_tokens=False` avoids counting markers some tokenizers add at the start.

6.
```python
q = "Kể tên ba món ăn nổi tiếng của Hà Nội."
for t in [0, 1.2]:
    print(f"--- temperature {t}")
    for _ in range(5):
        print(chat(q, temperature=t, max_new_tokens=60))
```
At temperature 0 (greedy) all five answers are identical. At 1.2 they vary, and some may drift off-topic or contain mistakes — small models get noticeably worse at high temperature.

7.
```python
import torch

def top_next(prompt, k=5):
    inputs = tok(prompt, return_tensors="pt").to(device)
    with torch.no_grad():
        probs = torch.softmax(model(**inputs).logits[0, -1].float(), dim=-1)
    top = torch.topk(probs, k)
    return [(tok.decode([int(i)]), round(p.item(), 3)) for p, i in zip(top.values, top.indices)]

print(top_next("Thủ đô của Việt Nam là"))
print(top_next("Thu do cua Viet Nam la"))
```
Usually the correct continuation (" Hà" / " Ha") keeps a high rank in both, but its probability tends to drop and the list gets more scattered without diacritics. Write down what *your* model does — that observation is data.

## C. Challenge

8.
```python
import torch

def answer_logprob(prompt, answer):
    prompt_ids = tok(prompt, add_special_tokens=False)["input_ids"]
    full_ids = tok(prompt + answer, add_special_tokens=False)["input_ids"]
    assert full_ids[:len(prompt_ids)] == prompt_ids, "prompt tokens changed; end the prompt without a trailing space"
    ids = torch.tensor([full_ids], device=device)
    with torch.no_grad():
        logprobs = torch.log_softmax(model(ids).logits[0].float(), dim=-1)
    total = 0.0
    for pos in range(len(prompt_ids), len(full_ids)):
        token_id = full_ids[pos]
        total += logprobs[pos - 1, token_id].item()   # the token at `pos` is predicted at position pos-1
    return total

for p, answers in [("Thủ đô của Việt Nam là", [" Hà Nội", " Huế"]),
                   ("Thu do cua Viet Nam la", [" Ha Noi", " Hue"])]:
    for a in answers:
        print(f"{p!r} + {a!r}: {answer_logprob(p, a):.2f}")
```
Key details:
- The score for the token at position `pos` comes from the logits at `pos − 1` (the model predicts the *next* token).
- Put the space at the start of the answer, not the end of the prompt: tokenizers usually attach a leading space to the following word, and splitting differently changes the tokens.
- Compare log-probs (sums of logs) rather than raw probabilities to avoid tiny numbers (Lesson 0.5). Longer answers get lower totals simply because they have more tokens; benchmarks often divide by the number of tokens to compare fairly.
This "score each option by log-probability" method is how many multiple-choice benchmarks evaluate models without generating text.
