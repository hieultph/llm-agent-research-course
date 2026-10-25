# Phase 3 — Agents: tool calling, planning, memory, MCP (outline)

> [!summary] Tóm tắt (VI)
> Chín tuần, song song với việc viết xong bài 1 và chọn, làm bài 2. Tự tay viết agent từ con số không trước, sau đó mới dùng framework, để hiểu rõ bên trong.
> Trọng tâm nghiên cứu: đánh giá agent và phân tích lỗi, vì đó là chỗ người mới dễ có đóng góp nhất.
> Đây là bản đề cương; nội dung chi tiết viết sau khi xong Phase 2.

**Calendar:** 9 weeks, dual / writing-sprint mode · **Compute:** laptop + Colab; small API budget for strong baselines · **Builds on:** Phase 2 (prompting, evaluation, RAG)

## Goals

- Build an agent loop from scratch (no framework), then with a framework, and compare.
- Make small models call tools reliably: schemas, validation, error recovery.
- Add planning, reflection and memory; know when each helps and what it costs.
- Build and connect an MCP server.
- Evaluate agents: success, steps, cost, trajectories; classify failures.

## Lessons

| # | Lesson |
|---|---|
| 3.1 | What is an agent: the observe → think → act loop; workflows vs agents |
| 3.2 | Function calling: JSON schemas, parsing, validating arguments, handling tool errors |
| 3.3 | ReAct from scratch, no framework |
| 3.4 | Planning: plan-and-execute, task decomposition |
| 3.5 | Reflection and self-correction: when it helps and when it does not |
| 3.6 | Memory: context management, summarisation, vector memory |
| 3.7 | Model Context Protocol (MCP): build a server, connect it to an agent |
| 3.8 | Agent frameworks: what they give you, what they hide |
| 3.9 | Multi-agent systems: roles, orchestration, when one agent is better |
| 3.10 | Code-executing agents and sandboxes |
| 3.11 | Evaluating agents: function-calling and agent benchmarks, success rate, cost, trajectories |
| 3.12 | Failure analysis: tracing, error taxonomies |
| 3.13 | Humans in the loop: confirmation, clarification questions |
| 3.14 | **Research week:** choose Paper 2 idea + novelty check; responding to reviewers of Paper 1 |

## Paper ideas attached to this phase

[[phase-3-ideas]]: 3A (wrong-form tool arguments in Vietnamese), 3B (tool-description smells and small models), 3C (predicting when to ask, Q2/Q1), 3D (good clarifying questions, Q2/Q1).

## Exit check

- [ ] My from-scratch ReAct agent solves multi-step tasks with at least 3 tools.
- [ ] I can run an agent benchmark subset and report success, steps and cost.
- [ ] I have an error taxonomy for my agent's failures.
- [ ] Paper 2 idea chosen; experiments started.
