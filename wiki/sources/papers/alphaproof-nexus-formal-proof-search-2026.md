---
created: 2026-05-24T00:00:00Z
updated: 2026-05-24T00:00:00Z
type: source
summary: "AlphaProof Nexus: basic LLM+Lean agent solved all 9 open Erdős problems the full RL-equipped agent solved, at higher per-problem cost"
tags: [paper, arxiv, formal-proof, lean, alphaproof, agentic-reasoning, mathematics, llm]
sources: https://arxiv.org/abs/2605.22763
status: active
confidence: 0.9
---

# Advancing Mathematics Research with AI-Driven Formal Proof Search (2026)

## Metadata
- **arXiv**: 2605.22763v1
- **Authors**: George Tsoukalas, Anton Kovsharov, Sergey Shirobokov, et al. (Google DeepMind)
- **Published**: 2026-05-21
- **Categories**: cs.AI

## Executive Summary

LLMs excel at mathematical reasoning but their unreliability (hallucinated logical steps) limits integration into real research workflows. Using LLMs to generate proofs in formal verification languages like Lean — where a compiler automatically checks every step — solves this. This paper performs the first large-scale evaluation of this approach on **open research-level problems**: the full-featured agent (evolutionary algorithm coordination + AlphaProof RL) autonomously solved 9 open Erdős problems (including two open for 56 years), proved 44/492 OEIS conjectures, and is actively aiding research in combinatorics, optimisation, graph theory, algebraic geometry, and quantum optics. Remarkably, a basic agent (LLM + Lean alternating) solved **all 9 of the same Erdős problems** at higher per-problem cost, demonstrating that simple agentic loops are increasingly sufficient as LLMs improve.

## Technical Approach

**AlphaProof Nexus framework**:
- Takes as input a Lean file with a target theorem and `sorry` placeholder in place of proof
- User-provided markers (`EVOLVE-BLOCK`, `EVOLVE-VALUE`) delineate what the agent may modify
- Outputs a `sorry`-free proof validated by the Lean compiler

**Basic agent (A)**: Set of prover subagents executing independently, each a "Ralph loop" (multi-turn LLM inference with chain-of-thought, search-and-replace tool for sketch refinement, Lean compiler feedback on each turn)

**Full-featured agent**: Subagents coordinated via evolutionary algorithm + can query AlphaProof (RL-trained olympiad-level Lean prover) as a focused proof tool. Evolutionary algorithm manages a population of proof approaches, selecting for proof completion.

**Lean verification prevents hallucination**: Every tactical step is mechanically verified; `sorry` is only accepted by the type checker if explicitly used, so cascading logical errors are impossible.

## Key Results

| Problem Set | Attempted | Solved | Key Detail |
|-------------|-----------|--------|-------------|
| Open Erdős problems | 353 | 9 | Including two open 56 years; ~$100-500/problem |
| OEIS conjectures | 492 | 44 | Open integer sequence conjectures |
| Hilbert functions (alg. geometry) | 1 | 1 | 15-year-old open question resolved |
| Convex optimization bound | 1 | 1 | Novel parameter schedule discovered |
| Ongoing | — | — | Quantum optics, graph theory |

**Critical finding**: The basic agent solved all 9 Erdős problems the full-featured agent solved, though at higher cost on hard problems. This is interpreted as evidence for "an ongoing shift from specialized trained systems toward simple agentic loops as LLMs become more capable."

Additional findings: identified several misformalizations in existing literature; helped resolve an open problem from Ben Green's well-known list.

## Relevance to EFHF/AGEM/MOP Research

AlphaProof Nexus is a concrete demonstration of the agentic loop pattern: generate → verify → refine. The Lean compiler acts as a hard [[verifier-graph]] node — falsifiable, automatic, no human-in-the-loop for step verification. The contrast between the basic and full-featured agent is also a natural experiment in [[mop-explorer]]: the simpler agent achieves the same outcome with worse resource efficiency, suggesting the full-featured architecture is solving a cost/bandwidth problem rather than a capability problem. The shift from RL-trained AlphaProof (specialist) to LLM+Ralph loop (generalist) as the primary solver aligns with [[agentic-research]]'s observation that general-purpose reasoning increasingly dominates specialized trained modules. The $100-500 cost per hard problem is also a concrete data point for [[efhf]]'s cost-modeling concerns about resource-constrained reasoning.

## Key Quotes

> "Remarkably, the basic agent solved all 9 problems, though at a higher cost on the harder problems. These findings demonstrate the power of AI-aided formal proof search as a tool for mathematics research, and point to an ongoing shift from specialized trained systems toward simple agentic loops as LLMs become more capable."

> "Because LLM-generated natural language proofs can contain subtle logical errors, or 'hallucinations,' they require expensive expert review. Mistakes in unreviewed intermediate steps can cascade through a proof, limiting the complexity of tasks that can be delegated to AI."

## Connections
- [[wiki/index]]
- [[sources/papers/alphaproof-nexus-formal-proof-search-2026]]
- [[alphaproof-nexus-formal-proof-search-2026]]
- [[verifier-graph]], [[mop-explorer]], [[agentic-research]], [[efhf]], [[sheaf-consistency-enforcer]]