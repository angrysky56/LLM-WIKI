---
summary: MOP-guided research agent using EFHF as verification backbone — autonomously explores concept spaces, generates hypotheses, verifies via L2-L5 pipeline, commits validated insights
tags: [MOP, EFHF, exploration, agent, knowledge-graph, research, synthesis, project]
updated: 2026-04-14T04:14:28Z
created: 2026-04-14T04:14:28Z
---

# MOP Explorer

**Type:** Project — MOP-guided research agent + concept space explorer
**Repository:** `/home/ty/Repositories/ai_workspace/mop-explorer`
**Status:** PRD drafted (v0.2, EFHF-integrated); Phase 1 not yet started
**PRD:** `mop-explorer/PRD.md`

---

## What It Is

A proactive exploration agent that uses the [[maximum-occupancy-principle]] as Layer 0 of the [[efhf]] architecture. The agent autonomously navigates concept spaces (knowledge graphs, research papers, wiki content), generates hypotheses, verifies them through the EFHF L2-L5 pipeline, and commits validated insights to the wiki.

Unlike a standard research assistant (reactive, task-completing), MOP Explorer maximizes action-state path entropy through concept space — exploring broadly by default, becoming goal-directed when epistemic energy is low, and avoiding epistemic dead-ends via formal verification.

## Architecture

MOP as Layer 0 generates exploration targets. The EFHF pipeline (conscience-servitor → LLM → hipai-montague → mcp-logic → advanced-reasoning → sheaf-consistency-enforcer) provides verification. Commits only occur at KERNEL1 closure status.

Seven cognitive actions: TRIAGE, QUERY, EXPLORE, HYPOTHESIZE, VERIFY, SYNTHESIZE, REPLENISH.

## Phases

1. **Core MOP Loop + EFHF** — Python orchestrator, full L0-L5+ pipeline, CLI
2. **EDM Disruption Scoring** — Neo4j embedding-based Δ measurement, Zettelkasten integration
3. **Concept Explorer UI** — React + D3 visualization of agent trajectory and concept space
4. **Multi-Agent MOP** — Cooperative exploration with β-weighted altruism

## Connections

- [[maximum-occupancy-principle]] — the behavioral theory
- [[efhf]] — the verification and consistency architecture
- [[mop-edm-cognitive-architecture]] — the synthesis document
- [[edm-framework]] — disruption measurement
- [[project-synapse]] — knowledge graph infrastructure
- [[zettelkasten-engine]] — insight generation seeding
