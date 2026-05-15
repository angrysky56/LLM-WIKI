---
created: 2026-05-13
updated: 2026-05-13
type: config
summary: User preferences and project context for the Markovian Dev Agency
tags: [user-preferences]
---

# User — Ty

## Preferences

- **Model:** MiniMax-M2.7 as primary (1500 calls/5hr budget)
- **Claude Code:** Available
- **MiniMax:** Preferred for budget-sensitive work
- **Output style:** Concise, direct, substantive. No fluff.
- **Communication:** Plain text in Discord; media files sent natively

## Project Context

- **Vault:** `/home/ty/Documents/LLM-WIKI/` — LLM-WIKI knowledge base
- **Synapse:** Project-Synapse MCP at `~/ai_workspace/domain-graph-orchestrator/` — knowledge graph with Neo4j + ChromaDB
- **Hermes:** Agent framework running this agency
- **Meta-Harness:** `~/Repositories/ai_workspace/meta-harness/` — evolution harness for autonomous agents

## Current Priority

Fix Synapse issues. The research-brief notes persistent problems with garbage entities (115 found), generic untyped nodes (203), and ~70% type correctness. We've worked on it a long time and recent fixes didn't address everything.

## Expectations

1. Agency activations should make visible progress on active issues
2. Carryover must be detailed enough that Ty doesn't have to re-explain context
3. Specialists should coordinate — diagnostician finds, fixer fixes, ticket-writer documents
4. Failed approaches should be logged so we don't repeat them