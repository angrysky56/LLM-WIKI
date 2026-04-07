---
summary: Karpathy's pattern for LLM-maintained persistent Markdown knowledge bases
tags: [knowledge-management, RAG, LLM, wiki, architecture]
updated: 2026-04-07T20:00:55Z
created: 2026-04-07T20:00:55Z
---

# LLM Wiki Pattern (Karpathy)

Source: [GitHub Gist](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f) by [[Andrej Karpathy]]

## Core Thesis

Instead of stateless [[RAG]] (retrieve → generate → forget), the LLM **incrementally builds and maintains a persistent wiki** — a structured, interlinked Markdown knowledge base that compounds over time. The wiki sits between the user and raw sources. The LLM writes it; the user reads it.

Key insight: **the wiki is a persistent, compounding artifact.** Cross-references already exist. Contradictions already flagged. Synthesis reflects everything ingested.

## Three-Layer Architecture

1. **Raw sources** — immutable curated documents. LLM reads but never modifies.
2. **The wiki** — LLM-generated Markdown. Summaries, entity pages, concept pages. LLM owns this entirely.
3. **The schema** — a config doc (e.g. CLAUDE.md) defining structure, conventions, and workflows.

## Core Operations

- **Ingest**: Drop source into raw/, LLM reads it, creates summary, updates entity/concept pages, updates index, appends to log. One source may touch 10-15 pages.
- **Query**: LLM reads index → finds relevant pages → synthesizes answer. Good answers get filed back as new wiki pages.
- **Lint**: Health-check for contradictions, orphans, stale claims, missing cross-references.

## Key Design Decisions

- **index.md** is content-oriented (catalogue of pages with summaries). Works surprisingly well at ~100 sources without embedding infrastructure.
- **log.md** is chronological (append-only timeline of operations).
- The wiki is a git repo — version history, branching, and collaboration for free.
- [[Obsidian]] as the IDE, LLM as the programmer, wiki as the codebase.

## Limitations Identified

- No built-in semantic search at scale (index.md breaks down past hundreds of pages)
- No vector embeddings or graph structure — purely file-system based
- Conflict resolution left to LLM judgment (no formal protocol)
- No rollback mechanism beyond git

## Relation to [[Project Synapse]]

Project Synapse addresses all four limitations: [[Neo4j]] provides graph structure + vector search, the [[Zettelkasten Engine]] handles conflict detection, and git handles rollback. The LLM-WIKI pattern provides the human-readable persistent output layer that Synapse lacked.
