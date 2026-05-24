---
name: project-synapse-mcp-tools
description: Complete reference of Project Synapse MCP tools available to wiki agents. Load this sheet for any agent working with the wiki knowledge graph.
created: 2026-05-31T
updated: 2026-05-31T
type: reference
tags: [mcp, tools, project-synapse, reference]
status: active
confidence: 1.0
sources: [message.txt from Project Synapse MCP server]
---

# Project Synapse MCP Tools Reference

**Source:** Actual tool list from `project-synapse` MCP server. All tools below are available to any agent with the MCP connection.

**Wiki root:** `/home/ty/Documents/LLM-WIKI/`
**Raw archive:** `/home/ty/Documents/LLM-WIKI/Clippings/`
**Paper research PDFs:** `/home/ty/Documents/paper-research/`

---

## Core Knowledge Graph

### 1. `ingest_text`
Ingest and process text into the knowledge graph using semantic analysis.

- **Args:** `text` (raw text), `source` (provenance identifier), `metadata` (optional dict)
- **Pipeline:** Montague Grammar parsing → Entity extraction → Relationship identification → Neo4j storage → Insight triggers
- **Returns:** Processing summary with entities and relationships extracted

### 2. `query_knowledge`
Query the knowledge graph for facts and insights using natural language.

- **Args:** `query`, `include_insights` (bool, default true), `max_results` (int, default 10)
- **Returns:** Facts, insights, and reasoning trails — prioritizes synthesized insights over raw facts
- **Use for:** Direct KB queries before doing web research

### 3. `explore_connections`
Explore connections around a specific entity via graph traversal.

- **Args:** `entity`, `depth` (1–5 hops, default 2), `connection_types` (optional filter)
- **Returns:** Visual representation of connections and discovered patterns
- **Use for:** Non-obvious relationship discovery

### 4. `synapse_remember`
Record a time-stamped fact in Synapse's episodic memory.

- **Args:** `subject`, `predicate` (snake_case verb), `object`, `valid_from` (ISO datetime), `valid_to` (optional), `confidence` (0–1), `source` (default "agent:claude"), `note`
- **Returns:** Fact ID (stable content hash — safe to call twice)

### 5. `synapse_recall`
Look up time-stamped facts about an entity.

- **Args:** `entity`, `as_of` (optional ISO datetime), `direction` ("outgoing" | "incoming" | "both")
- **Returns:** Newline-separated list of facts with timestamps

### 6. `synapse_timeline`
Chronological view of remembered facts.

- **Args:** `entity` (optional, omit for global), `limit` (default 50)
- **Returns:** Time-ordered fact list, oldest first

### 7. `synapse_invalidate`
Mark a previously-recorded fact as no longer true.

- **Args:** `subject`, `predicate`, `object`, `ended` (ISO datetime, defaults to now)
- **Returns:** Number of facts affected

### 8. `synapse_causal_window`
Find candidate causes by temporal correlation.

- **Args:** `effect_entity`, `before` (ISO datetime), `within_days` (default 30)
- **Returns:** Ranked list of candidate cause-effect pairings with day deltas
- **Use for:** "Track everything to find what caused X" pattern

### 9. `synapse_memory_stats`
Quick stats on temporal facts stored.

- **Returns:** Count of facts, time span covered

### 10. `analyze_semantic_structure`
Analyze text using Montague Grammar parsing.

- **Args:** `text`, `include_logical_form` (bool, default false)
- **Returns:** Entities, relations, and optional formal logical representations

### 11. `generate_insights`
Trigger autonomous Zettelkasten insight generation from the knowledge graph.

- **Args:** `topic` (optional), `confidence_threshold` (float, default 0.8)
- **Returns:** Generated insights with confidence scores and evidence trails
- **⚠️ WARNING: Times out at 300s** — use CLI wrapper instead: `timeout --kill-after=10s 580s uv run python scripts/generate_insights.py --print --max-runtime 540`

---

## Wiki Operations

### 12. `wiki_list_pages`
List all markdown pages in the wiki vault.

- **Args:** `subdir` ("wiki" | "raw", default "wiki")

### 13. `wiki_read_page`
Read a wiki page by relative path.

- **Args:** `path` (relative from vault root, e.g. "wiki/concepts/rag.md")

### 14. `wiki_write_page`
Write or update a wiki page with frontmatter. **Primary wiki write channel.**

- **Args:** `path` (relative, e.g. "wiki/entities/neo4j.md"), `body` (markdown), `summary` (one-line for index), `tags` (comma-separated)
- **Notes:**
  - Always use this for wiki content — NOT `write_file`
  - Creates frontmatter automatically if omitted
  - Updates `updated` timestamp if page exists

### 15. `wiki_search`
Full-text keyword search across wiki pages.

- **Args:** `query` (space-separated terms)

### 16. `wiki_lint`
Run health check on the wiki vault.

- **Detects:** Orphan pages (zero inbound wikilinks), broken wikilinks, missing frontmatter
- **Returns:** Structured health report
- **Speed:** ~5s

### 17. `wiki_hits_analysis`
Compute HITS hub and authority scores on the wikilink graph.

- **Authorities:** Pages cited by many others — load-bearing knowledge nodes needing deepest content
- **Hubs:** Pages linking to many good authorities — navigation layers needing comprehensive link coverage
- **Speed:** ~10s

### 18. `wiki_cluster_pages`
Cluster wiki pages by semantic similarity using GAAC (TF-IDF).

- **Identifies:** Natural topic clusters, same-cluster pages with no wikilink between them, merge candidates (sim > 0.7)
- **Args:** `n_clusters` (optional, auto = sqrt of page count if omitted)
- **Speed:** ~10s

### 19. `wiki_update_index`
Rebuild the wiki index from all wiki pages.

- **Args:** `deep` (bool, if true performs disk-level verification of all indexed files)
- **Speed:** ~30s

### 20. `wiki_ingest_raw`
Read a raw source file, ingest into Neo4j, and create wiki summary page.

- **Args:** `filename` (inside the raw/ directory)
- **Pipeline:** Reads from `raw/` → Synapse semantic pipeline → Neo4j → Creates `wiki/sources/` page
- **Use for:** Processing archived web content, paper abstracts, raw notes

### 21. `wiki_fetch_url`
Fetch a URL, extract clean markdown, save to raw/, ingest to Neo4j, archive to Clippings/.

- **Args:** `url`, `ingest` (bool, default true — set false to save raw only for manual review)
- **Speed:** ~15s
- **Returns:** Path to archived file, node/edge counts from ingestion
- **Note:** Strips navigation and clutter via defuddle — much cleaner than raw web_fetch
- **Use for:** Web research → auto-ingests to Neo4j + creates raw archive + wiki source page

### 22. `debug_test`
Simple health check — confirms MCP server is reachable.

- **Returns:** `{"ok": true}` if server is responding

---

## Tool Availability in Cron

**The MCP server IS available in cron jobs.** The `project-synapse` MCP server runs as a long-lived process. Cron agents inherit the MCP connection.

If a tool call fails with "tool not found" or module import error:
- The tool may not be registered in the current MCP server session
- Try `debug_test` first to confirm connectivity
- If `debug_test` returns ok but specific tools fail, the MCP server may need a restart

**Known tool issues:**
- `wiki_lint`, `wiki_cluster_pages`, `wiki_hits_analysis` — underlying Python modules (`synapse_mcp.zettelkasten.wiki_lint`, etc.) may not exist in the installed package. Use filesystem fallback (`full_audit.py`) if MCP returns import errors.
- `generate_insights` — times out at 300s. Always use the CLI wrapper: `timeout --kill-after=10s 580s uv run python scripts/generate_insights.py --print --max-runtime 540`

---

## Directives Directory

**This is where agents receive instructions:** `/home/ty/Documents/LLM-WIKI/wiki/scratchpad/jobs/`

- `carryover.md` — Open issues from prior runs (agents read this first)
- `reports/` — Per-agent run reports
- `sheet.md` — Master job schedule and configuration

Agents check this directory each cycle for new directives from Ty or from other agents.