---
summary: Four-stage query_knowledge pipeline: entity graph seeding → RRF hybrid search → wikilink expansion → Zettelkasten insights
tags: [retrieval, architecture, RRF, hybrid-search, entity-extraction, wikilinks, synapse]
updated: 2026-04-11T04:35:21Z
created: 2026-04-11T04:35:21Z
---

# Synapse Retrieval Architecture

**Type:** Concept — system internals  
**Status:** active  
**Last updated:** 2026-04-11

## Overview

`query_knowledge` now runs a four-stage pipeline on every query, producing results from three distinct retrieval paths that are merged before output.

## The Four Stages

```
Query string
    │
    ├─ Stage 1: Entity extraction (spaCy)
    │       Named entities → graph seed → directly connected Facts
    │       High-precision, zero vector math
    │
    ├─ Stage 2: Hybrid RRF (Neo4j)
    │       Vector ANN (cosine) + BM25 fulltext
    │       Fused via Reciprocal Rank Fusion, not weighted sum
    │
    ├─ Stage 3: Wikilink expansion (wiki_adapter)
    │       Top wiki page hits → their outbound [[wikilinks]]
    │       Surfaces conceptually adjacent pages from hand-curated graph
    │
    └─ Stage 4: Zettelkasten insights (insight_engine)
            Autonomous pattern nodes searched by vector similarity
            Prepended to output (synthesis first)

            ↓
    Merged output: entity hits → hybrid RRF hits → wiki links → insights
```

## Stage 1 — Entity Extraction

`knowledge_graph.extract_query_entities(query)` runs spaCy's `en_core_web_sm` NER over the query string. For each found entity, `query_by_entities()` runs a Cypher match on `Entity.name` (case-insensitive), walks 1-hop `RELATES` edges, and pulls `MENTIONS`-linked Facts.

**Why this matters:** A query like "what does Karpathy say about RAG?" extracts `["Karpathy", "RAG"]` and immediately surfaces facts directly tagged to those entities — before any embedding computation. These results are tagged `retrieval_path: entity_graph` in output.

## Stage 2 — Reciprocal Rank Fusion

Replaces the old weighted sum `similarity + (bm25 * 0.1)`.

**RRF formula:** `score(d) = Σ 1/(k + rank(d))` across ranked lists, `k=60`.

**Why RRF over weighted sum:**
- BM25 and cosine similarity have incompatible score scales — weighting them requires hand-tuning a coefficient that breaks whenever corpus statistics change
- RRF is position-based: a document ranked 1st in both lists scores `1/61 + 1/61 ≈ 0.033`; one ranked 1st in only vector scores `1/61 ≈ 0.016`
- `k=60` is the standard empirically validated constant — dampens the advantage of top-1 without collapsing to uniform
- Documents appearing in both lists get a natural boost with no tuning required

Results tagged `in_vector: True` and/or `in_bm25: True` for debugging.

## Stage 3 — Wikilink Graph Expansion

`wiki_adapter.get_wikilink_neighbors(slugs)` reads outbound `[[wikilinks]]` from the top 3 wiki pages matching the query. These are returned as a "Related Wiki Pages" section in the output.

**What this adds:** The wiki's wikilinks are hand-curated conceptual relationships — things I decided were worth connecting when writing pages. This is a different signal from Neo4j's extracted entity relationships: it reflects editorial judgment rather than NLP extraction. Surfacing it gives the user direct navigation hooks to adjacent knowledge.

**Future:** These wikilink edges could be loaded into Neo4j during ingest to become part of the graph traversal, rather than a separate lookup. Deferred until the wiki is larger and the link structure is more stable.

## What Didn't Change

- `query_semantic()` — raw vector ANN, unchanged, used internally by Stage 2
- `explore_connections()` — graph traversal tool, unchanged, still the right tool for "what connects X and Y?" queries
- `generate_insights()` — Zettelkasten engine, unchanged

## Connections

- [[project-synapse]] — the system this lives in
- [[graphrag]] — the broader paradigm this implements
- [[neo4j]] — vector + fulltext indexes powering Stages 1–2
- [[zettelkasten-engine]] — Stage 4 insight nodes
- [[synapse-llm-wiki-operating-guide]] — when to use which retrieval tool
