
summary: MUSE-Autoskill: skill-centric agent framework with on-demand creation, per-skill memory, and self-refinement via evaluation
tags: [skill-creation, agent-architecture, LLM-agents, skill-memory, self-evolution]
updated: 2026-05-28T20:01:29Z
created: 2026-05-28T20:01:29Z

# MUSE-Autoskill: Self-Evolving Agents via Skill Creation, Memory, Management, and Evaluation

**Paper**: [2605.27366](https://arxiv.org/pdf/2605.27366)  
**Authors**: Huawei Lin, Peng Li, Jie Song, Fuxin Jiang, Tieying Zhang (ByteDance / Rochester Institute of Technology)  
**Date**: 2026-05-28

## Core Problem

Existing LLM agent skill creation approaches treat skills as **isolated, static artifacts** — limiting reusability, reliability, and long-term improvement. Skills aren't first-class citizens with their own memory, evaluation, and refinement lifecycle.

## MUSE-Autoskill Framework

MUSE = **Memory-Utilizing Skill Evolution**. A skill-centric agent framework with a unified lifecycle:

```
Creation → Memory → Management → Evaluation → Refinement
```

### Key Components

**1. Skill Creation (on-demand)**
- Agents create skills dynamically based on task requirements
- Not pre-defined static library — skills emerge as needed

**2. Skill-Level Memory**
- Each skill accumulates experience across tasks
- Enables effective reuse and adaptation over time
- Memory per skill (not just global agent memory)

**3. Skill Management**
- Organization and efficient selection
- Which skill to use for which task

**4. Evaluation**
- Unit tests for skill reliability
- Runtime feedback for continuous refinement

**5. Refinement Loop**
- Skills improve via feedback over time

## Experimental Setting

Evaluated on **SkillsBench** (a benchmark for skill-oriented agent capabilities).

## Relevance to Meta-Harness

This is a concrete implementation of the "skill-as-first-class-citizen" pattern — exactly the architecture that meta-harness domain bootstrapping could leverage. Key ideas transferable to meta-harness:

- **Skill creation on demand** → agents dynamically generate capabilities, not just use fixed tools
- **Per-skill memory accumulation** → skills improve via experience, not just via pipeline re-runs
- **Unit-test + runtime-feedback evaluation** → skills self-verify and self-refine
- **Unified lifecycle** → creation/memory/management/evaluation/refinement as a closed loop

The contrast with the Kolmogorov paper is interesting: where Musat's paper is about the theoretical optimal prior (Solomonoff), MUSE-Autoskill is about the engineering layer — how to actually build, store, evaluate, and improve skills in practice.

## Tags

#skill-creation #agent-architecture #LLM-agents #skill-memory #self-evolution #bytedance
