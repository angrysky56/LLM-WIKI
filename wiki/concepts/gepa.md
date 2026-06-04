---
created: 2026-06-04
updated: 2026-06-04
type: concept
summary: GEPA (Genetic-Pareto Prompt Evolution) — ICLR 2026 Oral paper on evolutionary prompt optimization over execution traces.
tags: [prompt-evolution, genetic-algorithms, llm, iclr-2026]
sources: [https://arxiv.org/abs/2605.00550]
status: reference
confidence: 0.85
---

# GEPA

**GEPA** (Genetic-Pareto Prompt Evolution) — an ICLR 2026 Oral paper presenting an evolutionary approach to prompt optimization. GEPA reads execution traces to understand *why* a prompt fails (not just that it failed), then proposes targeted textual mutations evaluated against a fitness function. The Pareto dimension refers to multi-objective selection: simultaneously optimizing for task performance and other constraints (size, semantic preservation).

## How it works

1. **Trace collection** — Gather execution traces showing how a skill/prompt performs in context
2. **Failure analysis** — Identify failure modes at the textual/behavioral level
3. **Mutation proposal** — Generate candidate edits targeting specific failure modes
4. **Pareto evaluation** — Select on multiple axes (e.g., accuracy vs. token count vs. semantic drift)
5. **Iteration** — loop until convergence or constraint violation

## Used in

- [[hermes-agent-self-evolution]] — GEPA is the prompt evolution engine for Phases 1–3 (MIT licensed)
- [[dspy]] — GEPA runs as an optimizer on top of DSPy programs

## Connections

- [[concepts/prompt-evolution]] — the broader technique GEPA implements
- [[hermes-agent-self-evolution]] — production use of GEPA
- [[dspy]] — DSPy provides the program structure GEPA optimizes