---
created: 2026-05-28
updated: 2026-05-28
type: source
summary: "CODESKILL — RL-trained skill management policy for coding agents; learns to extract/evolve/maintain procedural skills from trajectories; +9.69 pass rate over no-skill, +4.01 over prompt-based baselines"
tags: [coding-agents, skill-management, RL, self-evolving-agents, grpo, skill-compaction, procedural-memory]
sources: https://arxiv.org/abs/2605.25430
status: active
confidence: high
---

# CODESKILL — Self-Evolving Skills for Coding Agents

## Executive Summary

CODESKILL addresses skill management for coding agents as a **learnable management policy** rather than fixed prompts or heuristic rules. The framework trains an LLM-based manager (Mθ) via GRPO to extract multi-granularity procedural skills from agent trajectories, evolve them with new/failed experience, and maintain a compact skill bank. Hybrid reward combines dense rubric-based skill-quality feedback with sparse verifiable execution feedback from the frozen downstream agent. On EnvBench, SWE-Bench Verified, and Terminal-Bench 2: +9.69 pass rate over no-skill baseline, +4.01 over strongest prompt-based/memory baselines (~33% and ~11% relative gains). Skill bank stays compact while performance scales.

## Technical Approach

**Skill Bank Architecture** — two granularity levels:
- **Task-level skills**: high-level strategies for task families (inspect repository, localize issue, validate fix)
- **Event-driven skills**: local guidance for recurring execution events (command failures, error patterns, test-output patterns)

**Skill Management Loop** — three operations per skill:
1. **Extract**: from trajectories → new task-level or event-driven skill (or skip)
2. **Evolve**: from new/failed evidence → revised candidate (update applicability, procedural guidance)
3. **Maintenance**: add / merge / drop candidate based on bank context

**Management Policy Training**:
- Warm-start: supervised data from teacher-generated skill operations
- RL: GRPO with hybrid reward
  - **Sparse verifiable feedback**: task success from frozen downstream agent
  - **Dense rubric-based judgment**: LLM-as-judge skill quality + behavior-skill alignment
- Evaluation: skill-conditioned rollout vs baseline (reverse retrieve)

**Skill Usage**: Dense semantic retrieval → skill bank → downstream agent prompt (policy parameters unchanged)

## Key Results

| Benchmark | vs No-Skill | vs Best Prompt/Memory Baseline |
|-----------|-------------|-------------------------------|
| EnvBench | +9.69 pass rate | +4.01 |
| SWE-Bench Verified | +9.69 pass rate | +4.01 |
| Terminal-Bench 2 | +9.69 pass rate | +4.01 |
| Relative gain | ~33% | ~11% |

OOD generalization: holds across both in-domain and OOD software engineering tasks.

## Wiki Connections

- [[mop-explorer]] — skill bank as compact representation for capability reuse; parallels MOP's object-centric abstraction
- [[bounded-representation-capacity]] — skill bank as compressed representation of trajectory experience; skill compaction as capacity management
- [[agentic-research]] — coding agents as long-horizon interactive RL tasks
- [[grpo]] — GRPO training with hybrid reward (from prior batch papers)
- [[verifier-graph]] — hybrid reward (sparse + dense) parallels verifier-graph multi-signal approach

## Key Quotes

> "CODESKILL reformulates skill management as a learnable management policy rather than relying on fixed prompts and heuristic criteria."

> "Static skill injection does not always improve coding agents — skill usefulness depends strongly on task fit and context, further motivating adaptive skill management."

> "The reward combines sparse verifiable feedback with dense rubric-based judgments, balancing executable outcomes with informative supervision when task success is sparse."