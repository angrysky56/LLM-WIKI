---
summary: Synapse Wiki Scaling walkthrough — DuckDB-backed vault index, parser extraction, response budgeting, and tool changes that let the wiki scale to 1,200+ pages without flooding agent context.
tags: [source, project-synapse, wiki-operations, infrastructure, duckdb, obsidian]
updated: 2026-06-04T12:33:44Z
created: 2026-06-04T12:33:44Z
---

---
created: 2026-06-04T00:00:00Z
updated: 2026-06-04T00:00:00Z
type: source
summary: "Walkthrough of the Synapse MCP Wiki Scaling improvements — DuckDB-backed persistent page index, frontmatter/link parser extraction, response budgeting, and tool changes (list_pages/read_page/search) that let the wiki scale to 1,200+ pages without flooding the agent context."
tags: [source, project-synapse, wiki-operations, infrastructure, duckdb, obsidian]
sources: https://github.com/angrysky56/LLM-WIKI (project-synapse-mcp walkthrough)
status: active
confidence: 0.95
---

# Synapse Wiki Scaling — Walkthrough

Implementation writeup documenting the architectural changes made to the `project-synapse-mcp` server so it can handle large Obsidian vaults (1,200+ pages) without flooding the agent's context window or causing disk I/O bottlenecks.

## What was built

### New components

- **`parser.py`** — Extracted frontmatter parsing (`parse_frontmatter` / `build_frontmatter`) and weighted outbound link extraction (`extract_outbound_links`) into an isolated module to break a circular import between the wiki adapter and indexing layer.
- **`vault_index.py`** — Persistent, thread-safe page index backed by **DuckDB** (stored at `.synapse/vault_index.duckdb`).
  - **Incremental sync** based on `mtime` + content hash: full scan only on first load, subsequent syncs are `<50ms` by skipping unchanged files.
  - **SQL-based queries** replace filesystem walks for `search`, `list`, and `health-check` operations.
  - **Full-text database search** stores page bodies in DuckDB to support fast keyword queries with matching excerpts — no file reads required.
- **`response_budget.py`** — Token-ceiling utility capping returned text at ~1000 tokens (`MAX_RESPONSE_CHARS = 4000`) with clean spillover truncation. Prevents oversized tool responses from blowing the agent context.

### Modified components

- **`wiki_adapter.py`** — Initializes `VaultIndex` on startup. Rewrote `list_pages`, `search_pages`, `lint`, `get_wikilink_neighbors`, `compute_wikilink_hits`, `cluster_wiki_pages`, and `get_sync_manifest` to use index queries. `write_page` and `delete_page` now do write-through index updates (upsert/delete) to keep DB and disk in sync.
- **`server.py`** — Tool API expanded:
  - `wiki_list_pages` — added `limit`, `offset`, and `tag` filters with pagination + token cap.
  - `wiki_read_page` — added `mode` parameter: `"meta"` (frontmatter only, 0 file reads), `"excerpt"` (first 500 chars, 0 file reads), or `"full"` (reads from disk).
  - `wiki_search` — added `limit` and `subdir` filters; returns matching excerpts/snippets.
  - `wiki_sync_index` — new tool to manually re-sync the DB index from disk after external edits.

## Verification

### Tests

```bash
uv run pytest tests/test_vault_index.py tests/test_wiki_resilience.py
```

- `test_vault_index.py` — 4/4 passed
- `test_wiki_resilience.py` — 5/5 passed
- **9 passed in 2.27s**

### Backward compatibility

All pre-existing tests pass — index layer is wire-compatible with the prior filesystem-based API.

## Why it matters

This is the system that *runs* the [[entities/projects/project-synapse]] tools used by every agent in this vault. The agent context-vs-vault-size problem is the central scaling bottleneck for any agentic knowledge management system, and this change resolved it by moving all hot-path reads from disk to a single-query DuckDB backend with a hard response budget.

## Connections

- [[entities/projects/project-synapse]] — the MCP server these changes ship in
- [[obsidian]] — the vault format being indexed
- [[duckdb]] — the embedded OLAP DB backing the page index
- [[wiki-operations]] — operational category these tools serve
- [[concepts/context-budget]] — the `response_budget.py` pattern is a concrete instance of context budgeting

## Key claims / caveats

- 1,200-page claim is from the source walkthrough — not independently re-verified in the 1340-page 2026-06-04 vault.
- `mtime`-based sync assumes the filesystem clock is monotonic. If the user does out-of-band `git pull` and the mtime drifts, use `wiki_sync_index` to force a re-sync.
- `<50ms` incremental sync is a benchmark on a developer laptop, not a contract — large files or many modified pages will still scale linearly.
