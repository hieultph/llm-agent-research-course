# 1B — "Trúng gió" or stroke? Folk phrasing, diacritic loss and LLM under-triage

> [!summary] Tóm tắt (VI)
> Đo xem cùng một ca bệnh, khi kể bằng lời dân gian hoặc gõ không dấu, LLM có ít khuyên đi cấp cứu hơn không, và có chiều theo cách chữa dân gian không.
> Bộ dữ liệu: 72 ca dựng theo hướng dẫn chính thức (48 cấp cứu, 24 ca nhẹ để đối chứng). Mỗi ca có 4 cách kể (y khoa / dân gian × có dấu / không dấu), riêng 48 ca cấp cứu có thêm bản "định chữa dân gian" → 336 câu hỏi.
> Chạy hai notebook trên Colab: **A** (GPU) cho 7 mô hình mở, **B** (CPU) cho 3 mô hình qua Gemini API, giám khảo LLM, kiểm tra bằng người và phân tích.
> Bài báo: [papers/1B-folk-triage/latex/main.tex](../../papers/1B-folk-triage/latex/main.tex) (mẫu Springer LNCS).

## Files

| File | What |
|---|---|
| [data/cases_source.py](data/cases_source.py) | **Source of truth.** 72 cases: signs list, clinical text, folk text, folk terms, remedy, guideline |
| [data/build_dataset.py](data/build_dataset.py) | Checks the cases and writes the three files below (`python3 build_dataset.py`) |
| `data/cases.jsonl` | 336 prompts (`clin`, `clin_nd`, `folk`, `folk_nd`, `folk_rem`) |
| `data/meaning_check.csv` | Sheet for the 2 native-speaker reviewers (pair order and side randomised; `_key` column = answer key, hide it) |
| `data/folk_lexicon.csv` | 41 folk terms: lay meaning, what they can hide, which cases use them |
| [ft.py](ft.py) | Shared code: generation (transformers / Gemini REST), judge, statistics, figures, annotation sheet |
| [make_notebooks.py](make_notebooks.py) | Writes the two notebooks (edit cells here, not in the .ipynb) |
| [1B_generate_gpu.ipynb](1B_generate_gpu.ipynb) | **A** — open models, GPU [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/hieultph/llm-agent-research-course/blob/main/experiments/1B-folk-triage/1B_generate_gpu.ipynb) |
| [1B_api_judge_analysis.ipynb](1B_api_judge_analysis.ipynb) | **B** — API models, judge, κ, results, LaTeX tables, CPU [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/hieultph/llm-agent-research-course/blob/main/experiments/1B-folk-triage/1B_api_judge_analysis.ipynb) |

Results go to `MyDrive/llm-research/1B-folk-triage/` (`gen/`, `judge/`, `annotation/`, `results/`).

## Việc cần làm (theo thứ tự)

1. **Kiểm tra nghĩa (gửi ngay, vì phải chờ người khác):** tải `data/meaning_check.csv` lên Google Sheets, **xóa cột `_key`** trước khi chia sẻ, rồi gửi cho 2 người. Mỗi người điền:
   - `cung_trieu_chung`: `co` (cùng triệu chứng) / `A_thieu` / `B_thieu` / `khac`
   - `ghi_chu_trieu_chung`: thiếu/thêm triệu chứng gì
   - `tu_nhien_A`, `tu_nhien_B`: 1–5
2. **Gemini API:** nạp credit trong AI Studio (key hiện báo 402, hết credit trả trước). Thêm secret `GOOGLE_API_KEY` trong Colab (🔑). Chạy thêm `HF_TOKEN` nếu muốn có Llama-3.1-8B.
3. **Notebook A** trên A100 (hoặc L4) → Run all. Khoảng 1–1,5 giờ trên A100, 2,5–3 giờ trên L4.
4. **Notebook B** trên CPU → Run all (bước 1 chạy được song song với A). Sau khi A xong, chạy lại B để chấm phần của A.
5. **Chấm tay:** B tạo `annotation/sheet.csv` (150 câu trả lời). Bạn chấm cả 150 dòng, người thứ hai chấm 60 dòng có `x`. Lưu thành `annotation/rater1.csv` và `annotation/rater2.csv` trên Drive, rồi chạy lại B.
6. Gửi `results/` (hoặc `summary.json` và `tables/*.csv`) để viết phần kết quả.

## Design notes

- The folk version keeps every sign in the case's `signs` list; it only changes wording and adds the folk label (`chắc bị trúng gió`). `build_dataset.py` asserts that each folk term appears in the folk text.
- Labels come from guidelines (Bộ Y tế stroke and dengue guidelines, WHO IMCI, NICE NG143/NG51/NG240/CG141/NG126, WHO methanol, ESC ACS). There was no clinician review: state this as a limitation.
- Judge = Gemini 3.5 Flash. It sees only the answer (and remedy), never the case, gold label or version. It is validated against 150 human labels.
- Main metric: under-triage = emergency case whose answer is not `emergency` (`none` counts as under-triage). Control metric: over-triage on the 24 non-emergencies.
- Statistics: paired by case. Bootstrap CI over cases plus exact McNemar, Holm across models × contrasts. The pooled effect uses a case-level bootstrap over all models.
- The analysis pipeline was smoke-tested locally on synthetic judged data (`ft.py`, notebook B end to end). `run_hf` (notebook A) needs a GPU and was not run locally.
