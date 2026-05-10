---
summary: Self-evolving multi-agent framework that autonomously discovers natural-language skills from complex contexts via adversarial self-play — no human annotation, no external feedback.
tags: [skill-extraction, self-play, multi-agent, context-learning, llm, adversarial, skill-augmentation]
updated: 2026-05-08T19:19:50Z
created: 2026-05-08T19:19:50Z
---

## One-Line Summary

Ctx2Skill is a self-evolving multi-agent framework that autonomously discovers, refines, and selects natural-language "skills" from complex contexts — no human annotation, no external feedback — then plugs those skills into any LLM at inference time to boost context reasoning.

## Core Idea

LLMs often need to reason over contexts (docs, code, papers) that weren't in their training data. The natural approach is "inference-time skill augmentation" — extract rules/procedures from context into explicit skills. But writing skills by hand is expensive, and automated approaches lack ground-truth feedback.

Ctx2Skill solves both with a **multi-agent self-play loop**.

## Architecture: Five Frozen-LM Agents

| Agent | Role |
|-------|------|
| **Challenger** | Generates probing tasks + rubrics from context, evolves its own skills |
| **Reasoner** | Attempts tasks guided by context + current skill set |
| **Judge** | Binary per-rubric verdicts — partitions tasks into solved/failed |
| **Proposer** (×2) | Diagnoses failure/success patterns → high-level update proposals |
| **Generator** (×2) | Materializes proposals into concrete skill set changes |

Both Challenger and Reasoner **co-evolve**: failed tasks → Reasoner skill updates; easily solved tasks → Challenger skill updates (sustained adversarial pressure).

## Cross-Time Replay (Preventing Collapse)

Self-play risks **adversarial collapse**: Challenger makes tasks too extreme, Reasoner's skills over-specialize.

Cross-Time Replay:
- Collects representative hard + easy probe tasks during training
- Re-evaluates ALL historical skill set candidates on these probes
- Selects the skill set that maximizes `solve_rate(hard) × solve_rate(easy)`

This is the key mechanism ensuring robust generalization.

## Results (CL-Bench)

| Backbone | Without Skills | With Ctx2Skill | Δ |
|----------|---------------|----------------|---|
| GPT-4.1 | 11.1% | 16.5% | +5.4% |
| GPT-5.1 | 21.2% | 25.8% | +4.6% |
| GPT-5.2 | 18.2% | 21.4% | +3.2% |

Consistent 3–5pp improvement across models on context learning tasks.

## Relevance to Hermes

Ctx2Skill is directly relevant to Hermes's own skill system. Key parallels:

- **Hermes skills** = natural-language procedural documents → **Ctx2Skill's extracted skills** = same format
- Ctx2Skill automates what Hermes users do manually: distill context into reusable skill docs
- The Cross-Time Replay mechanism is a solution to a problem Hermes faces: skill rot and over-specialization
- The multi-agent architecture (Challenger ↔ Reasoner co-evolution) is adaptable to Hermes's `delegate_task` system

**Potential integration**: Ctx2Skill could auto-generate Hermes SKILL.md files from project repos or documentation, with Cross-Time Replay ensuring they stay generalizable.

## Citation

Shuzheng Si et al., "From Context to Skills: Can Language Models Learn from Context Skillfully?" arXiv:2604.27660, Apr 2026. [[ctx2skill]]
