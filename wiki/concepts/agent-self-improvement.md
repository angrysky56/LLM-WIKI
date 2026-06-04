---
created: 2026-06-04
updated: 2026-06-04
type: concept
summary: "Agent self-improvement — techniques where LLM agents iteratively improve their own skills, prompts, tool descriptions, or code via execution feedback, closing the improvement loop inside the agent's own operation"
tags: [agent-improvement, evolutionary-algorithms, llm, self-improvement, agentic-ai]
sources: [https://arxiv.org/abs/2503.12627 (GEPA), DSPy reference, hermes-agent self-evolution docs]
status: active
confidence: 0.8
---

# Agent Self-Improvement

A family of techniques where LLM agents iteratively improve their own artifacts — skills, prompts, tool descriptions, or code — using execution feedback. Self-improvement contrasts with external human-led improvement (RLHF, SFT) by closing the loop inside the agent's own operation.

## Approaches

1. **Prompt evolution** — optimize system prompts using execution traces ([[gepa]], [[dspy]])
2. **Skill refinement** — edit skill files based on task failure patterns
3. **Code evolution** — modify tool implementations via evolutionary search ([[entities/projects/darwinian-evolver]])
4. **Continuous improvement loops** — fully automated pipelines from trace collection to deployment

## Connections

- [[hermes-agent-self-evolution]] — the reference implementation
- [[concepts/prompt-evolution]] — specific technique used within self-improvement
- [[gepa]] — the evolutionary optimizer used