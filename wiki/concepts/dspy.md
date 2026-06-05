---
summary: DSPy — Stanford declarative LM programming framework that separates program structure from parameter optimization.
tags: [llm-programming, framework, stanford, prompt-optimization]
updated: 2026-06-05T09:46:24Z
---

---
created: 2026-06-04
updated: 2026-06-04
type: concept
summary: DSPy — Stanford declarative LM programming framework that separates program structure from parameter optimization.
tags: [llm-programming, framework, stanford, prompt-optimization]
sources: [https://dspy.ai, https://github.com/stanfordnlp/dspy]
status: active
confidence: 0.85
---

# DSPy

**DSPy** (Declarative Self-Improving Programs) is a Stanford research framework that treats LLM pipelines as programs whose behavior — not just prompts — can be systematically optimized. Instead of hand-writing prompts, you declare the program structure (modules, signatures, data flow) and DSPy's compiler searches for the best prompt/component configuration to maximize a given metric on training examples.

Key papers: "DSPy: Compiling Declarative Self-Improving LM Programs" (Khattab et al., 2023+).

## Relationship to [[gepa|GEPA]]

DSPy provides the underlying program structure and the trace-collection mechanism. GEPA (Genetic-Pareto Prompt Evolution) runs as an optimizer *on top of* DSPy — it proposes textual mutations (prompt variants, skill edits) which DSPy then evaluates. The [[hermes-agent-self-evolution]] repo uses DSPy for Phase 1 skill optimization and DSPy + GEPA together for prompt evolution.

## Connections

- [[hermes-agent-self-evolution]] — DSPy is a core engine in this repo
- [[gepa]] — GEPA optimizes on top of DSPy programs
- [[concepts/prompt-evolution]] — the technique GEPA implements

## Open Questions

- [ ] How does DSPy's compiler cost scale with number of modules? Can it handle 50+ step pipelines?
- [ ] Does DSPy's optimization generalize across model families (e.g., DeepSeek vs. Claude)?
