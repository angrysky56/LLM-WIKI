---
created: 2026-04-07 20:01:48+00:00
updated: 2026-04-07 20:01:48+00:00
type: entity
summary: Graph-backed MCP server providing semantic search, knowledge synthesis, and wiki bridge
tags: [project, mcp, neo4j, architecture, core]
sources: []
status: active
confidence: 0.8
---


# Project Synapse

Autonomous Knowledge Synthesis and Inference Engine — the graph-backed backbone of this wiki.

## What It Is

An MCP server that combines:
- **[[Neo4j]]** graph database with native vector indexes for semantic search
- **Montague Grammar** parser for formal semantic analysis
- **[[zettelkasten-engine]]** for autonomous pattern detection and insight generation
- **Wiki adapter** bridging the Obsidian vault with the knowledge graph

## Role in This Wiki

Project Synapse solves the scaling limitations of the [[llm-wiki-pattern|LLM Wiki Pattern]]:

| Karpathy Pattern | Project Synapse |
|---|---|
| index.md for page lookup | Vector ANN search over Neo4j |
| No cross-document graph | Full entity-relationship graph |
| Conflict resolution by LLM judgment | Timestamped nodes + confidence scores |
| Git for rollback | Git + graph versioning |

## Architecture

```
Raw Source → Semantic Pipeline → Neo4j (entities, facts, embeddings)
                                    ↕
                              Wiki Adapter
                                    ↕
                          Obsidian Vault (Markdown)
```

## Key Tools

- `wiki_ingest_raw` — reads raw files, runs semantic pipeline, stores in graph
- `wiki_write_page` / `wiki_read_page` — CRUD on wiki Markdown pages
- `query_knowledge` — vector semantic search over the graph
- `explore_connections` — graph traversal for hidden relationships
- `wiki_lint` — health check for orphans, broken links, missing frontmatter

## Connections
- [[entities/projects/mop-explorer]]
- [[synthesis/causal-state-edm-ood-isomorphism]]
- [[scratchpad/jobs/reports/librarian/audit-2026-05-21]]
- [[entities/tools/obsidian]]
- [[sources/articles/prd-ralph-loop-mop-gemini]]
- [[concepts/llm-wiki-pattern]]
- [[concepts/agent-onboarding]]
- [[sources/articles/hilbert-hotel-graph-architecture]]
- [[sources/articles/momoa-researcher]]
- [[concepts/graphrag]]
- [[concepts/rag]]
- [[concepts/multi-agent-llm-systems]]
- [[entities/projects/efhf]]
- [[concepts/multi-agent-coordination]]
- [[sources/documentation/obsidian-cli-skill]]
- [[synthesis/verifiable-graph-context-protocol]]
- [[concepts/extraction-quality-audit]]
- [[entities/projects/zettelkasten-engine]]
- [[sources/papers/bae-lmac-2026]]
- [[entities/tools/obsidian-skills-repo]]
- [[wiki/index]]
- [[synthesis/synapse-retrieval-architecture]]
- [[synthesis/wiki-indexing-theory]]
- [[sources/documentation/hermes-mcp-integration]]
- [[concept-index]]
- [[concepts/persistent-knowledge-compilation]]
- [[sources/articles/llm-wiki-pattern]]
- [[synthesis/mop-edm-cognitive-architecture]]
- [[log]]
- [[scratchpad/agent-sheets/librarian/carryover]]
- [[synthesis/efhf-mcp-configuration]]
- [[entities/projects/meta-harness]]
- [[sources/papers/xu-envfactory-2026]]
- [[entities/tools/neo4j]]
- [[neo4j]] — the graph/vector storage layer
- [[neo4j]] — the graph/vector storage layer
- [[obsidian]] — the human-readable wiki output layer
- [[zettelkasten-engine]] — the autonomous insight synthesis component
- [[rag]] — the stateless baseline this system supersedes
- [[graphrag]] — the graph-retrieval paradigm this implements
- [[persistent-knowledge-compilation]] — the core architectural philosophy
- [[llm-wiki-pattern]] — the Karpathy pattern this extends
- [[obsidian-skills-repo]] — agent skill definitions including defuddle for web content cleaning

- [[hilbert-hotel-graph-architecture]]
- [[prd-ralph-loop-mop-gemini]]
- [[extraction-quality-audit]]
- [[multi-agent-coordination]]
- [[momoa-researcher]]
- [[meta-harness]]
- [[agent-onboarding]]
- [[multi-agent-llm-systems]]
- [[obsidian-cli-skill]]
- [[mop-explorer]]