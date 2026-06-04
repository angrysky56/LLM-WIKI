---
created: 2026-06-04
updated: 2026-06-04
type: entity
summary: "Darwinian Evolver — git-based code evolution CLI used in Phase 4 of the hermes-agent-self-evolution pipeline."
tags: [code-evolution, git, cli, hermes-agent]
sources: [https://github.com/NousResearch/hermes-agent-self-evolution]
status: stub
confidence: 0.8
---

# Darwinian Evolver

A git-based code evolution engine — called as an external CLI — used in Phase 4 of the [[hermes-agent-self-evolution]] pipeline. Where GEPA handles prompt evolution via textual mutations, the Darwinian Evolver handles *code* evolution: it reads tool implementation code, proposes mutations at the code level, and manages the git workflow for candidate variants.

## Phase 4 role

In the hermes-agent-self-evolution phased plan, Phase 4 targets tool implementation code:

| Phase | Target | Engine |
|-------|--------|--------|
| 1 | Skill files | DSPy + GEPA |
| 2 | Tool descriptions | DSPy + GEPA |
| 3 | System prompts | DSPy + GEPA |
| 4 | Tool code | Darwinian Evolver |

## Connections

- [[hermes-agent-self-evolution]] — Phase 4 engine
- [[concepts/code-evolution]] — broader category