---
created: 2026-05-30T09:35:00Z
updated: 2026-05-30T09:35:00Z
type: source
summary: "SpecBench: evaluates SWE agents on specification-level reasoning — identifying deficiencies in RFC design proposals before implementation. Best model GPT-5.4 achieves 44.4%. Bridges SWE-bench gap."
tags: [arxiv, paper, SWE-agents, evaluation, specification, reasoning, benchmark, software-engineering]
sources: https://arxiv.org/abs/2605.30314
status: active
confidence: high
---

# SpecBench: Evaluating Specification-Level Reasoning for Software Engineering LLM Agents

**arXiv**: 2605.30314v1 | **Date**: 2026-05-28 | **Authors**: Grant Hamblin, Kevin Song, Zhanda Zhu et al. (U Toronto, Waterloo, NVIDIA)

## Core Contribution

SpecBench evaluates SWE agents on **specification-level reasoning** — the ability to generate complete, unambiguous, consistent, and correct system specifications before implementation. This fills the gap between code-generation benchmarks (SWE-bench) and real-world software engineering, where initial specifications are often incomplete and flawed.

Current benchmarks like SWE-bench assume "perfect specification" — precise, complete requirements that admit a deterministic test oracle. SpecBench does the opposite: the agent must identify specification deficiencies (omissions, ambiguities, inconsistencies, incorrect assumptions) in an initial RFC design proposal.

## Task Structure

Each SpecBench task provides:
- Initial RFC design proposal (from real open-source projects: Kubernetes, React, Rust, TVM, vLLM)
- Project codebase at the commit before the RFC was proposed
- All prior RFC discussions and history

The agent predicts specification deficiencies against critiques raised by expert maintainers during historical RFC reviews.

## Deficiency Classes (IEEE Std. 1028-1997)

1. **Omission**: Necessary information missing from the proposal
2. **Ambiguous**: Information with more than one interpretation
3. **Inconsistent**: Proposal contradicts itself or existing system
4. **Incorrect**: Information conflicts with preceding documents

## Key Results

| Agent | Accuracy |
|-------|----------|
| GPT-5.4 | 44.4% |
| Claude 4 Sonnet | ~40% |
| DeepSeek R1 | ~35% |

Best performance = 44.4% — significant room for improvement on specification-level reasoning.

## Design Features

- **Community value alignment**: Different communities prioritize different design philosophies (Rust: memory safety strictness vs React: API stability). Agents must understand community-specific values.
- **Decoupled from implementation**: Agents produce no code — isolates specification reasoning distinct from coding capability.
- **Long-horizon reasoning**: Requires understanding code logic, system invariants, and years of historical design decisions.
- **Real-world grounding**: RFC processes from actual open-source software systems reflect genuine design decisions.

## Connections

- [[SWE-bench]] — SpecBench is the upstream complement: from specification to implementation, vs implementation given specification
- [[agentic-ai]] — evaluates agents' ability to handle the full software development lifecycle
- [[evaluation]] — benchmark for a capability (specification reasoning) not covered by existing SWE benchmarks
- [[ai-evaluation-infrastructure]] — SpecBench as part of the infrastructure for evaluating AI agents

## Kanban Status

- [x] Paper ingested 2026-05-30
- [ ] **Open**: Compare SpecBench approach to SWE-bench scope — does SpecBench's specification-level evaluation reveal different capability gaps than code-generation benchmarks?