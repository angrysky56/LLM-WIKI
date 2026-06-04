---
created: 2026-06-04
updated: 2026-06-04
type: entity
summary: "hermes-agent-self-evolution — Nous Research repo using DSPy + GEPA evolutionary optimization for Hermes Agent skills, prompts, and tool descriptions."
tags: [hermes-agent, self-improvement, dspy, gepa, nous-research, repository]
sources: [https://github.com/NousResearch/hermes-agent-self-evolution]
status: reference
confidence: 0.9
---

# hermes-agent-self-evolution

**Repository**: [NousResearch/hermes-agent-self-evolution](https://github.com/NousResearch/hermes-agent-self-evolution)  
**License**: MIT  
**Phase**: Phase 1 shipping; Phases 2–5 planned

Evolutionary self-improvement toolkit for [[hermes-agent]] using [[dspy|DSPy]] + [[gepa|GEPA]] (Genetic-Pareto Prompt Evolution). Optimizes skills, tool descriptions, system prompts, and (eventually) tool code via reflective evolutionary search over execution traces.

## Five-phase plan

| Phase | Target | Engine | Status |
|-------|--------|--------|--------|
| 1 | Skill files (SKILL.md) | DSPy + GEPA | ✅ Shipping |
| 2 | Tool descriptions | DSPy + GEPA | 🔲 Planned |
| 3 | System prompt sections | DSPy + GEPA | 🔲 Planned |
| 4 | Tool implementation code | Darwinian Evolver | 🔲 Planned |
| 5 | Continuous improvement loop | Automated pipeline | 🔲 Planned |

## Connections

- [[hermes-agent]] — the system being improved
- [[dspy]] — declarative LM program framework
- [[gepa]] — genetic-pareto prompt evolution (ICLR 2026 Oral)
- [[entities/projects/darwinian-evolver]] — code evolution engine for Phase 4
- [[concepts/prompt-evolution]] — underlying technique
- [[concepts/agent-self-improvement]] — broader category