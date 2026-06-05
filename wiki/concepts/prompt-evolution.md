---
summary: Prompt evolution — iterative optimization of LLM prompts using execution traces, evolutionary search, and multi-objective selection.
tags: [prompt-optimization, evolutionary-algorithms, llm]
updated: 2026-06-05T09:46:26Z
---

---
created: 2026-06-04
updated: 2026-06-04
type: concept
summary: Prompt evolution — iterative optimization of LLM prompts using execution traces, evolutionary search, and multi-objective selection.
tags: [prompt-optimization, evolutionary-algorithms, llm]
sources: []
status: active
confidence: 0.8
---

# Prompt Evolution

Iterative optimization of LLM prompts using execution traces, evolutionary search (mutation + selection), and multi-objective selection (Pareto frontier across metrics like accuracy, size, and semantic preservation). Unlike brute-force grid search over prompt variants, prompt evolution uses the structure of failures in execution traces to guide targeted mutations.

## Techniques

- **GEPA** (Genetic-Pareto Prompt Evolution) — ICLR 2026 Oral; the main reference implementation
- **DSPy** — provides the program structure that GEPA optimizes over

## Connections

- [[gepa]] — the primary reference technique
- [[hermes-agent-self-evolution]] — applies prompt evolution to Hermes Agent skills
- [[concepts/agent-self-improvement]] — broader category that includes prompt evolution
