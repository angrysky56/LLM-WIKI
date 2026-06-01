---
created: 2026-05-30T09:40:00Z
updated: 2026-05-30T09:40:00Z
type: source
summary: "Physics-Is-All-You-Need: physicist-supervised AI coding agent builds CLAX-PT (differentiable perturbation theory) over 57 sessions. Supervision protocol design — not model capability — determined trustworthiness."
tags: [arxiv, paper, AI-coding-agents, scientific-software, supervision, physics, human-AI-collaboration]
sources: https://arxiv.org/abs/2605.30353
status: active
confidence: high
---

# Physics Is All You Need? A Case Study in Physicist-Supervised AI Development of Scientific Software

**arXiv**: 2605.30353v1 | **Date**: 2026-05-28 | **Author**: Nhat-Minh Nguyen (Kavli IPMU, UTIAS, U Tokyo)

## Core Contribution

A quantified case study (N=1) of a physicist supervising Claude Code (Sonnet and Opus models) to build CLAX-PT — a differentiable one-loop perturbation theory module in JAX for predicting galaxy clustering (~2,100 lines, validated to ≲1% accuracy against the established C reference CLASS-PT).

**Central claim**: The supervision protocol — not model capability — was the primary factor determining whether the agent's output was trustworthy scientific software.

## Key Findings

### What the Agent Resolved Autonomously (10/15 issues)
- Convention errors
- Algorithm transcription errors
- Numerical coefficient errors
- All resolved by iterating against oracle test suites

### What Required Human Intervention (3/15 issues)
Three bugs evaded oracle detection — the agent treated symptom reduction as equivalent to root-cause resolution:
1. **Wrong code architecture**: Agent spent 33 of 57 sessions adjusting coefficients within a code architecture that could not represent the target physics. Only an injected physics concept (anisotropic BAO damping) triggered redesign.
2. **Calibrated scalar correction**: Passed all oracle tests but corresponded to no quantity in the reference theory — would produce wrong predictions at any other cosmology.
3. **Another architecture-level failure**: Evaded tests by optimizing locally within wrong structure.

### What Was Accelerated by Human (2/15 issues)
- Magnitude discrepancies invisible to shape-based comparisons (human spotted wrong magnitude orders)

## Supervision Protocol (Critical)

Four infrastructure elements established before any code was written:

1. **CLASS-PT as oracle**: Every function tested against reference data before code was attempted. Tests written first — agent knew correct output before producing it.

2. **CHANGELOG as shared memory**: Structured log of attempts, failures, successes. Prevented re-exploration of dead ends across sessions. (Analogous to the CLAX-PT changelog discipline from Carlini 2026.)

3. **--fast flag for context hygiene**: Tests printed at most 10 lines on success, 20 on failure. Verbose diagnostics → log files. Prevents finite context window consumption by noise.

4. **Parallel agent sessions via git worktrees**: Multiple sessions explored competing hypotheses simultaneously when a bug had multiple plausible causes.

## Design Principle

> "Closing the gap we observed would require agents that can propose architectural alternatives rather than optimize within a given structure, and distinguish predictive adequacy from explanatory correctness. The agent in this case study did not exhibit these capabilities, and they are not obviously addressed by scaling alone."

The critical distinction: **not whether the code produced right numbers, but whether it produced them for the right reasons.**

## Connections

- [[ai-coding-agents]] — detailed case study of human-AI collaboration in scientific software development
- [[scientific-software]] — specific domain: differentiable perturbation theory for cosmology
- [[supervision]] — supervision protocol design as key determinant of output quality
- [[agentic-ai]] — AI as scientific collaborator, not just tool
- [[oracle-tests]] — oracle test suites as supervision mechanism
- [[self-improvement]] — agent iteratively improved via test feedback, but architectural errors required human intervention
- [[autosci-memory-centric-research-lifecycle]] — AutoSci is the system-level continuation: full-lifecycle harness with persistent memory vs single-project supervision

## Kanban Status

- [x] Paper ingested 2026-05-30
- [ ] **Open**: Connection to LLMSurgeon investigator agent pattern — both use "static environment ablation" to catch failures invisible to standard testing. Compare the two approaches.
- [ ] **Open**: The distinction between "predictive adequacy" and "explanatory correctness" may be a useful framing for evaluation design — does the wiki have a page on this?