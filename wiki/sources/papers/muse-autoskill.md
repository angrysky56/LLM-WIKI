---
created: 2026-05-27T00:00:00Z
updated: 2026-05-27T00:00:00Z
type: source
summary: "MUSE-Autoskill: agents create, reuse, evaluate, and refine skills via a unified lifecycle — skill-level memory accumulates experience across tasks, improving reuse, reliability, and cross-agent transfer."
tags: [arxiv, llm-agent, skill-lifecycle, skill-creation, memory, grpo]
sources: https://arxiv.org/abs/2605.27366v1
status: active
confidence: 0.9
---

# MUSE-Autoskill (2605.27366)

**Self-Evolving Agents via Skill Creation, Memory, Management, and Evaluation**

## Core Thesis

LLM agents rely on reusable skills to solve complex tasks, but existing approaches treat skills as **isolated static artifacts** — no accumulation of cross-task experience, no systematic evaluation, no lifecycle. MUSE-Autoskill proposes skills as **long-lived, experience-aware, testable assets** with a five-phase lifecycle:

1. **Creation** — on-demand skill generation for novel sub-problems
2. **Memory** — skill-level experience accumulated across tasks
3. **Management** — organization and efficient selection
4. **Evaluation** — unit tests + runtime feedback
5. **Refinement** — iterative improvement from evaluation signals

## Key Mechanisms

### Skill-Level Memory
Each skill accumulates experience across tasks via a persistent memory store. When a task resembles prior ones, relevant skills are retrieved and their stored experience guides adaptation — enabling more effective reuse than cold-start approaches.

### Unified Lifecycle
Skills are not monolithic subroutines — they have:
- **Unit tests** that verify correctness in isolation
- **Runtime feedback** tracking task success, efficiency, reuse rate
- **Cross-agent transfer** enabling skills learned by one agent to benefit others

### On-Demand Creation
Agents create skills when confronted with novel sub-problems that don't match existing skill library. Skills are generated and immediately battle-tested via evaluation before entering the reusable library.

## Findings (SkillsBench)

Experiments on SkillsBench show:
- **Task success**: improved when lifecycle-managed skills used
- **Efficiency**: faster task completion through skill reuse
- **Reuse rate**: skills accumulated and reused across tasks
- **Cross-agent transfer**: skills trained on one agent improve performance on others

## Connections
- [[wiki/index]]
- [[sources/papers/muse-autoskill]]

- [[agentic-research]] — MUSE-Autoskill is an agentic AI framework
- [[bounded-representation-capacity]] — skills as bounded, reusable representation units
- [[credit-assignment]] — lifecycle evaluation connects to how credit is assigned across skill components
- [[grpo]] — GRPO mentioned in related work for skill-aligned RL training
- [[skill-lifecycle]] — direct concept link (skills have a defined lifecycle in this paper)
- [[muse-autoskill]] — this paper

## Cross-Paper Theme Connection

This paper directly extends the **instance-level behavioral decomposition** theme from the 2026-05-26 batch:
- AKBE decomposed per-instance tool need
- PRISM decomposed per-step intention
- **MUSE-Autoskill** decomposes per-skill task-solving — each skill is a reusable behavioral unit with its own experience memory, evaluation loop, and refinement pathway

## Notes

- Published 2026-05-26, arXiv
- primary_category: cs.AI
- Also categorized: cs.CL, cs.LG, cs.MA
