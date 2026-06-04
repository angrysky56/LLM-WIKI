---
created: 2026-06-04
updated: 2026-06-04
type: entity
summary: "DuckDB — embedded OLAP database used as the persistent backing store for the project-synapse vault index."
tags: [database, olap, infrastructure, project-synapse]
sources: [https://duckdb.org]
status: stub
confidence: 0.85
---

# DuckDB

An embedded OLAP (Online Analytical Processing) database used as the persistent backing store for the [[project-synapse]] vault index (`.synapse/vault_index.duckdb`). DuckDB was chosen for its zero-configuration embedded deployment, fast SQL queries over large vaults, and full-text search capabilities without a separate search service.

## Why DuckDB for a wiki index

The project-synapse vault index needs to answer three hot-path queries at low latency across 1,200+ pages:
1. **List pages** — paginated with tag filtering, SQL `LIMIT/OFFSET`
2. **Search pages** — full-text keyword search with excerpts, no file reads required
3. **Health checks** — link integrity and orphan detection via SQL joins

DuckDB's columnar storage handles all three with `<50ms` incremental sync (vs. multi-second filesystem walks), and its Python bindings make it easy to embed in an MCP server without requiring a running database process.

## Connections

- [[project-synapse]] — the MCP server using DuckDB as its index backend
- [[wiki/sources/articles/synapse-wiki-scaling-walkthrough]] — source page