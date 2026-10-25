# How to study when you forget fast, get sleepy and lose focus

> [!summary] Tóm tắt (VI)
> Đọc lại nhiều lần là cách học kém nhất. Cách tốt nhất là tự hỏi bản thân trước khi nhìn đáp án, ôn đúng lúc sắp quên (Anki lo việc này), và luôn tự tay làm.
> Mỗi buổi chia 4 Pomodoro. Buồn ngủ thì chuyển sang gõ code hoặc viết tay, đừng đọc tiếp.
> Mỗi tối viết 3 dòng nhật ký học. Mỗi Chủ nhật ôn tuần 30 phút.

## 1. Why you forget (and why it is normal)

Memory fades fast after you learn something — most of it within a few days — unless you **pull it back out** of your head at the right moments. Each time you successfully recall something just before forgetting it, it lasts much longer the next time.

![Forgetting curve with and without spaced review](forgetting_curve.png)

Orange: learn once, never review. Blue: each short review resets the curve and makes it fall more slowly next time (what Anki does for you). The shape is illustrative, not exact data — the point is the gap.

So the method is not "study harder". It is:

1. **Recall, don't reread.** Close the note and try to answer. Struggling to recall *is* the learning.
2. **Space it out.** Review at growing gaps: 1 day, 3 days, 1 week, 2 weeks… Anki schedules this automatically.
3. **Do, don't watch.** Type every code example yourself. Change a number and predict what happens before you run it.
4. **Explain it simply.** If you cannot explain it in 5 plain lines, you do not understand it yet (Feynman technique).

## 2. A 2-hour session, minute by minute

| Time | What you do |
|---|---|
| 0:00–0:05 | Phone in another room. Open only the lesson file and one code window. |
| 0:05–0:10 | **Warm-up recall**: answer the lesson's warm-up questions on paper, *without* looking. |
| 0:10–0:35 | Pomodoro 1: Part 1 of the lesson. Type the code. |
| 0:35–0:40 | Break: stand up, water, look out of the window. No phone. |
| 0:40–1:05 | Pomodoro 2: Part 2. |
| 1:05–1:10 | Break. |
| 1:10–1:35 | Pomodoro 3: Part 3 (or paper work in dual mode). |
| 1:35–1:40 | Break. |
| 1:40–2:00 | Pomodoro 4: exercises, then check `solutions/`. Write the Feynman box. |
| after | Anki 10 minutes (can be on the phone, on the bus, before sleep). |

## 3. When you get sleepy

Sleepiness usually means you have been *reading passively* for too long. Switch the type of activity instead of pushing through:

- **Switch to typing code.** Hands busy = brain awake.
- **Switch to paper.** Draw the diagram from memory. Write the formula by hand.
- **Stand up.** Study standing for one Pomodoro.
- **Talk out loud.** Explain the concept to an imaginary friend (or record a 1-minute voice note).
- **Cold water on the face, 2 minutes of walking** — then restart the timer.
- If you are still falling asleep after 2 switches, stop, sleep, and do the remaining part tomorrow. Studying half-asleep gives near-zero retention.

Study at the time of day when you are most alert. For most people that is morning or right after a short rest — not right after a big meal.

## 4. When you lose focus

- One tab, one task. Close chat apps and social media during a Pomodoro.
- Keep a **"distraction list"** on paper. When a thought pops up ("check message", "look up X"), write it down and get back to work. Handle the list during breaks.
- Small wins: tick the lesson part in [[03-progress-tracker]] as soon as it is done. Seeing ticks keeps motivation up.
- If a part takes more than 2 Pomodoros, it is too big — split it, or skip and mark it with `#stuck` to return to later.

## 5. Using Obsidian well

- Keep these course files **read-only**. Write your own notes in a separate folder, e.g. `my-notes/`, using [[daily-note]].
- Link your notes to course concepts with `[[...]]`. Over months, your graph becomes a personal map of the field.
- For papers you read, use [[paper-note]]. You will reuse these notes when writing related work sections.
- Use tags: `#stuck`, `#review`, `#idea`. An `#idea` tag on anything that sparks a research thought — check these during the weekly review.

## 6. Using Anki well

- Import each phase's CSV once. The cards are short on purpose.
- Do reviews **every day**, even only 5 minutes. Missing days makes the pile grow and feel scary.
- When a card feels unclear, edit it in your own words — your wording sticks better than mine.
- Add your own cards for anything you got wrong in exercises.
- Rule: **never skip Anki more than 2 days in a row.**

## 7. Weekly review (Sunday, 30 minutes)

1. Look at the week's ticks in [[03-progress-tracker]].
2. Without notes, write the 5 most important ideas from the week on one page.
3. Compare with the lessons. Anything missing → make an Anki card.
4. Check `#stuck` tags. Re-try one.
5. Check `#idea` tags. Write one line about each in your research log.
6. Plan next week: which lessons, which days are dual mode.
