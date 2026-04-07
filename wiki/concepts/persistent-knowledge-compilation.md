---
summary: Paradigm of LLM pre-compiling knowledge into persistent structured bases vs stateless RAG
tags: [knowledge-management, RAG, architecture, core-concept]
updated: 2026-04-07T20:01:08Z
created: 2026-04-07T20:01:08Z
---

# Persistent Knowledge Compilation

A paradigm shift from stateless [[RAG]] to **compile-time knowledge synthesis**.

## Definition

Rather than re-deriving answers from raw documents on every query (RAG), an LLM pre-processes sources into a persistent, structured knowledge base. The synthesis happens once at ingest time and is kept current — not re-derived on every query.

## Key Properties

- **Accumulative**: Each source ingested enriches the existing knowledge. Connections compound.
- **Persistent**: Written to disk as Markdown/graph nodes. Survives across sessions.
- **Pre-digested**: Query-time latency drops because the LLM queries structured summaries, not raw text.
- **Transparent**: The compiled state is human-readable (Markdown files, graph visualization).

## Analogies

- Compiler vs. interpreter: RAG interprets on every run; this pattern compiles once.
- Vannevar Bush's [[Memex]] (1945): private, curated knowledge store with associative trails.
- The difference between a search engine and an encyclopedia.

## Implementations

- [[LLM Wiki Pattern|wiki/sources/llm-wiki-pattern]] — Karpathy's file-system-only approach
- [[Project Synapse]] — graph-backed implementation with Neo4j + vector search

## Open Questions

- At what scale does compilation cost exceed query-time RAG cost?
- How to handle contradictions between sources without human arbitration?
- Can compilation be made incremental enough to be real-time?
