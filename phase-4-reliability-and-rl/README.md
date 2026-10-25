# Phase 4 — Reliability, safety and reinforcement learning (outline)

> [!summary] Tóm tắt (VI)
> Chín tuần, song song với bài 2 và bắt đầu bài 3 (mức Q2). Học cách đo độ tự tin của mô hình, phát hiện bịa đặt, phòng chống tấn công chèn lệnh, công cụ nhìn vào bên trong mô hình, và học tăng cường (RLHF, DPO, GRPO).
> Phần học tăng cường có toán nhiều nhất khóa, sẽ giải thích chậm bằng ví dụ trò chơi trước khi vào công thức.
> Đây là bản đề cương; nội dung chi tiết viết sau khi xong Phase 3.

**Calendar:** 9 weeks, dual mode · **Compute:** laptop + Colab; 40–100 rented GPU hours for RL (Paper 3) · **Builds on:** Phases 2–3

## Goals

- Measure calibration and uncertainty; know which uncertainty signals detect errors.
- Understand hallucination, jailbreaks and prompt injection; evaluate defenses fairly (attack success *and* utility).
- Use interpretability tools (logit lens, probing, activation patching) on small models.
- Understand RL from the ground up and train a small model with DPO and GRPO.
- Plan a Q2/Q1 paper and a path toward graduate research.

## Lessons

| # | Lesson | Math |
|---|---|---|
| 4.1 | Uncertainty and calibration: ECE, reliability diagrams | ✏️ |
| 4.2 | Uncertainty for LLMs: token probability, verbalised confidence, self-consistency, semantic entropy | ✏️ |
| 4.3 | Hallucination: detection and mitigation | |
| 4.4 | Safety basics: jailbreaks, direct and indirect prompt injection, threat models | |
| 4.5 | Defenses: instruction hierarchy, spotlighting, classifiers, sandboxing; measuring utility | |
| 4.6 | Looking inside: logit lens, probing, activation patching (for idea 1C) | ✏️ |
| 4.7 | RL basics I: agent, environment, reward, policy; multi-armed bandits | ✏️ |
| 4.8 | RL basics II: policy gradients (REINFORCE) explained with a game | ✏️ |
| 4.9 | RLHF: reward models, PPO overview | ✏️ |
| 4.10 | DPO: learning from preferences without a reward model | ✏️ |
| 4.11 | GRPO and RL with verifiable rewards | ✏️ |
| 4.12 | Hands-on: GRPO on a 0.5B model with an open-source RL library | |
| 4.13 | RL for agents: multi-turn rewards, user simulators, reward hacking | |
| 4.14 | **Research week:** Paper 3 plan; where to go next (Q1 venues, graduate research) | |

## Paper ideas attached to this phase

[[phase-4-ideas]]: 4A (calibration under noisy input), 4B (prompt injection in Vietnamese), 4C (RL to learn when to ask, Q2/Q1), 4D (noise-robust calibration training, Q2/Q1).

## Exit check

- [ ] I can draw a reliability diagram and compute ECE for a model.
- [ ] I evaluated one defense with both attack success rate and utility.
- [ ] I trained a small model with GRPO and the reward went up for the right reason.
- [ ] Paper 3 experiments are running.
