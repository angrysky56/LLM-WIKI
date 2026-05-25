---
created: 2026-04-07 20:00:55+00:00
updated: 2026-04-07 20:00:55+00:00
type: concept
summary: Karpathy's pattern for LLM-maintained persistent Markdown knowledge bases — the foundational architecture this wiki is built on
tags: [knowledge-management, rag, llm, wiki, architecture, karpathy]
sources: https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f
status: reference
confidence: 1.0
---


# LLM Wiki Pattern

The LLM Wiki Pattern is a knowledge management architecture where a large language model incrementally builds and maintains a persistent wiki — a structured, interlinked Markdown knowledge base that compounds over time. The wiki sits between the user and raw sources. The LLM writes it; the user reads it.

**Source:** [Karpathy's GitHub Gist](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f) — [[andrej-karpathy]]

## Core Thesis

Instead of stateless [[RAG]] (retrieve → generate → forget), the LLM **incrementally builds and maintains a persistent wiki**. The wiki is a persistent, compounding artifact — cross-references already exist, contradictions are flagged, synthesis reflects everything ingested.

## Three-Layer Architecture

1. **Raw sources** — immutable curated documents. LLM reads but never modifies.
2. **The wiki** — LLM-generated Markdown. Summaries, entity pages, concept pages. LLM owns this entirely.
3. **The schema** — a config doc (e.g. CLAUDE.md) defining structure, conventions, and workflows.

## Core Operations

- **Ingest**: Drop source into `raw/`, LLM reads it, creates summary, updates entity/concept pages, updates index, appends to log. One source may touch 10–15 pages.
- **Query**: LLM reads index → finds relevant pages → synthesizes answer. Good answers get filed back as new wiki pages.
- **Lint**: Health-check for contradictions, orphans, stale claims, missing cross-references.

## Key Design Decisions

- **index.md** is content-oriented (catalogue of pages with summaries). Works well at ~100 sources without embedding infrastructure.
- **log.md** is chronological (append-only timeline of operations).
- The wiki is a git repo — version history, branching, and collaboration for free.
- [[Obsidian]] as the IDE, LLM as the programmer, wiki as the codebase.

## Limitations

- No built-in semantic search at scale (index.md breaks down past hundreds of pages)
- No vector embeddings or graph structure — purely file-system based
- Conflict resolution left to LLM judgment (no formal protocol)
- No rollback mechanism beyond git

## This Vault

This wiki (LLM-WIKI) follows the LLM Wiki Pattern and extends it with [[project-synapse]] — which adds [[Neo4j]] graph structure, vector search, and the [[zettelkasten-engine]] for autonomous insight generation. The Karpathy pattern provides the human-readable output layer; Synapse adds the graph intelligence layer underneath.

See `wiki/sources/articles/llm-wiki-pattern.md` for the full source article.

## Connections

- [[andrej-karpathy]] — origin: authored the pattern
- [[persistent-knowledge-compilation]] — the paradigm this instantiates
- [[project-synapse]] — the extension that adds graph + vector intelligence
- [[memex]] — the intellectual ancestor: Bush's 1945 vision of associative trails that this finally solves
- [[RAG]] — the stateless baseline this supersedes
- [[para-methodology]] — alternative knowledge organization; wiki pattern as complement
- [[obsidian]] — the tool used as the human-facing wiki IDE