# Solutions — Lesson 0.1

Back to the lesson: [[lesson-0.1-setup-and-python-basics]]

## Warm-up
No fixed answers. Keep your paper and re-read it at the end of Phase 0.

## A. Predict, then run

1. `[20, 30, 40]` — slice from index 1 to the end.
2. `NGÔN NGỮ` — `.upper()` works with Vietnamese letters too.
3. `2` — a dictionary cannot have duplicate keys. The second `"a"` overwrites the first, so the dict is `{"a": 3, "b": 2}`.
4. `10` — `range(1, 5)` is 1, 2, 3, 4 (5 is excluded). 1+2+3+4 = 10.
5. The body of the function is not indented. Python raises `IndentationError`. Fix:
   ```python
   def square(x):
       return x * x
   ```

## B. Write code

6.
```python
def average(numbers):
    """Return the mean of a list of numbers."""
    return sum(numbers) / len(numbers)

print(average([8, 7.5, 9]))   # 8.1666...
```
Note: an empty list would cause division by zero. A safer version checks `if not numbers: return None`.

7.
```python
def longest_word(text):
    """Return the longest word; the first one wins on ties."""
    best = ""
    for w in text.split():
        if len(w) > len(best):
            best = w
    return best

print(longest_word("tôi đang học mô hình ngôn ngữ lớn"))   # "đang" (first of the 4-letter words)
```
Shorter version: `max(text.split(), key=len)`.

8.
```python
prices = {"phở": 50000, "bún chả": 45000, "cơm tấm": 40000}
for dish, price in prices.items():
    if price < 48000:
        print(dish)
# bún chả
# cơm tấm
```

## C. Challenge

9.
```python
def top_k_words(text, k):
    counts = {}
    for w in text.lower().split():
        counts[w] = counts.get(w, 0) + 1
    ranked = sorted(counts.items(), key=lambda pair: pair[1], reverse=True)
    return ranked[:k]

print(top_k_words("mèo ăn cá mèo ngủ mèo chơi cá", 2))   # [('mèo', 3), ('cá', 2)]
```
`lambda pair: pair[1]` is a tiny unnamed function: "for each (word, count) pair, sort by the count". Python also has `collections.Counter(words).most_common(k)` which does the same in one line.
