# Solutions — Lesson 0.2

Back to the lesson: [[lesson-0.2-python-for-llm-work]]

## Warm-up
1. `["b", "c"]`
2. `d["lang"] = "vi"`
3. It ends the function and hands a value back to whoever called it.

## A. Check your understanding

1. `out = [w.lower() for w in ["Mèo", "CHÓ", "Cá"]]`
2. One string is NFC and the other is NFD (same letters, different internal storage). Fix: `unicodedata.normalize("NFC", s)` on both before comparing.
3. In Unicode, `đ` is its own letter, not "d + a mark". NFD does not split it, so removing combining marks would leave it unchanged.
4. Without it, `json.dump` writes Vietnamese letters as escape codes like `ô`. The file is still valid, but you cannot read it with your eyes.

## B. Write code

5.
```python
import random
import unicodedata

def strip_diacritics(text):
    text = text.replace("đ", "d").replace("Đ", "D")
    decomposed = unicodedata.normalize("NFD", text)
    return unicodedata.normalize("NFC", "".join(c for c in decomposed if unicodedata.category(c) != "Mn"))

def partial_strip(text, ratio, seed=0):
    """Strip diacritics from a random `ratio` of the words."""
    rng = random.Random(seed)            # own random generator -> repeatable
    words = text.split()
    k = round(len(words) * ratio)
    chosen = set(rng.sample(range(len(words)), k))
    return " ".join(strip_diacritics(w) if i in chosen else w for i, w in enumerate(words))

s = "Tôi muốn đặt vé máy bay đi Đà Nẵng"
for r in [0, 0.5, 1.0]:
    print(r, partial_strip(s, r))
```
Why `random.Random(seed)` instead of `random.seed(...)`: it does not affect other code that uses random numbers, and the same seed always picks the same words — essential for reproducible experiments.

6.
```python
import json

def save_jsonl(rows, path):
    with open(path, "w", encoding="utf-8") as f:
        for r in rows:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")

def load_jsonl(path):
    with open(path, encoding="utf-8") as f:
        return [json.loads(line) for line in f if line.strip()]

qa = [
    {"q": "Thủ đô của Việt Nam là gì?", "a": "Hà Nội"},
    {"q": "Sông dài nhất Việt Nam chảy qua nhiều nước là sông nào?", "a": "Sông Mê Kông"},
    {"q": "Phở có nguồn gốc từ miền nào?", "a": "Miền Bắc"},
]
save_jsonl(qa, "qa.jsonl")
print([row["q"] for row in load_jsonl("qa.jsonl")])
```
`if line.strip()` skips empty lines (e.g. a blank line at the end of the file).

7.
```python
class Conversation:
    def __init__(self, system_prompt):
        self.messages = [{"role": "system", "content": system_prompt}]

    def add(self, role, content):
        self.messages.append({"role": role, "content": content})

    def to_text(self):
        return "\n".join(f"{m['role']}: {m['content']}" for m in self.messages)

chat = Conversation("Bạn là trợ lý hữu ích.")
chat.add("user", "Xin chào!")
chat.add("assistant", "Chào bạn, mình giúp gì được?")
print(chat.to_text())
```

## C. Challenge

8.
```python
import unicodedata

def strip_diacritics(text):
    text = text.replace("đ", "d").replace("Đ", "D")
    decomposed = unicodedata.normalize("NFD", text)
    return unicodedata.normalize("NFC", "".join(c for c in decomposed if unicodedata.category(c) != "Mn"))

words = ["bán", "bàn", "bạn", "bản", "ban", "má", "mà", "mạ", "mả", "mã", "ma",
         "đi", "di", "dì", "đá", "đã", "da", "dạ", "đà"]
groups = {}
for w in words:
    groups.setdefault(strip_diacritics(w), []).append(w)

for key, originals in sorted(groups.items(), key=lambda kv: len(kv[1]), reverse=True):
    print(key, "<-", originals)
```
Output starts with `ma <- ['má', 'mà', 'mạ', 'mả', 'mã', 'ma']`: six different words collapse into one. Vietnamese has six tones, so a plain syllable can stand for up to six words (more when hats and hooks are added: "ma", "mơ", "mô"…). A restoration model must use the surrounding words to guess which one was meant — and sometimes it cannot.
