# Phase 2 — LLMs in practice: decoding, evaluation, RAG, fine-tuning (outline)

> [!summary] Tóm tắt (VI)
> Bảy tuần ở chế độ "vừa học vừa làm bài báo 1". Học cách chạy mô hình hiệu quả, viết prompt, đánh giá mô hình cho nghiêm túc (kể cả thống kê), xây RAG, và tinh chỉnh bằng LoRA trên GPU 6GB.
> Hai bài cuối dạy viết bài báo, đúng lúc bạn bắt đầu viết bài 1.
> Đây là bản đề cương; nội dung chi tiết viết sau khi xong Phase 1.

**Calendar:** 7 weeks, dual mode (Paper 1 experiments) · **Compute:** laptop + Colab · **Builds on:** Phase 1

## Goals

- Run 1–8B models efficiently (4-bit, batching, local servers) and control decoding.
- Evaluate properly: right metrics, validated LLM judges, confidence intervals, significance tests.
- Build and debug a RAG pipeline; separate retrieval failures from generation failures.
- Fine-tune a small model with LoRA/QLoRA on your own GPU.
- Write a paper: structure, contributions, figures, related work, limitations.

## Lessons

| # | Lesson | Math |
|---|---|---|
| 2.1 | Decoding in depth: greedy, beam, top-k/top-p, repetition, the KV cache | |
| 2.2 | Running models efficiently: quantization (8-bit, 4-bit), GGUF, Ollama, vLLM | ✏️ |
| 2.3 | Prompting: zero-/few-shot, chain-of-thought, structured JSON output | |
| 2.4 | Evaluation I: accuracy/EM/F1, benchmarks, data contamination | |
| 2.5 | Evaluation II: LLM-as-a-judge, human annotation, agreement (Cohen's kappa) | ✏️ |
| 2.6 | Statistics for experiments: variance, seeds, bootstrap confidence intervals, paired tests | ✏️ |
| 2.7 | Retrieval: BM25, dense, hybrid, rerankers, vector databases | ✏️ |
| 2.8 | RAG end to end: chunking, prompting with context, oracle-retrieval trick for failure analysis | |
| 2.9 | Evaluating RAG: answer correctness, faithfulness, context relevance | |
| 2.10 | Fine-tuning basics: supervised fine-tuning, data formats, overfitting | |
| 2.11 | LoRA and QLoRA on a 6 GB GPU (low-rank idea explained gently) | ✏️ |
| 2.12 | Experiment management: configs, logging, reproducibility, releasing code and data | |
| 2.13 | Writing a paper I: structure, introduction and contributions, figures and tables | |
| 2.14 | Writing a paper II: related work, results, limitations, LaTeX/Overleaf, submitting | |

## Paper ideas attached to this phase

[[phase-2-ideas]]: 2A (no-diacritic RAG + fixes, **recommended Paper 1**), 2B (knowledge conflict on Vietnam-native facts), 2C (cross-lingual consistency defense, Q2/Q1), 2D (fix input or fix model, Q2/Q1).

## Exit check

- [ ] I can report a result with a 95% confidence interval and explain what it means.
- [ ] I validated an LLM judge against my own labels.
- [ ] My RAG pipeline's failures are split into retrieval vs generation.
- [ ] I fine-tuned a model with LoRA and it improved on a held-out set.
- [ ] Paper 1 draft has all sections.
