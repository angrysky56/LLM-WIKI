# librarian — MCP Tools Quick Reference

22 synapse MCP tools available to the librarian agent.

## Core Wiki Tools

| # | Tool | Purpose | Key Args |
|---|------|---------|----------|
| 1 | `wiki_lint` | Detect broken links, orphans, missing frontmatter | — |
| 2 | `wiki_read_page` | Read a page to fix it | `path` |
| 3 | `wiki_write_page` | Fix frontmatter, add wikilinks, normalize tags | `path`, `body`, `summary`, `tags` |
| 4 | `wiki_search` | Find related pages for orphan linking | `query` |
| 5 | `wiki_list_pages` | List all wiki pages | `subdir` (wiki/raw) |
| 6 | `wiki_update_index` | Rebuild wiki index after fixes | `deep` |
| 7 | `wiki_cluster_pages` | Find same-cluster pages for cross-linking | `n_clusters` |
| 8 | `wiki_hits_analysis` | Compute HITS hub and authority scores | — |
| 9 | `wiki_ingest_raw` | Ingest raw file into wiki + Neo4j | `filename` |
| 10 | `wiki_fetch_url` | Fetch URL with defuddle, save to raw/, ingest | `url`, `ingest` |

## Synapse Episodic Memory

| # | Tool | Purpose | Key Args |
|---|------|---------|----------|
| 11 | `synapse_remember` | Record time-stamped fact | `subject`, `predicate`, `object`, `valid_from` |
| 12 | `synapse_recall` | Look up facts about entity | `entity`, `direction`, `as_of` |
| 13 | `synapse_timeline` | Chronological view of facts | `entity`, `limit` |
| 14 | `synapse_invalidate` | Mark fact as no longer true | `subject`, `predicate`, `object`, `ended` |
| 15 | `synapse_causal_window` | Find candidate causes by temporal correlation | `effect_entity`, `before`, `within_days` |
| 16 | `synapse_memory_stats` | Quick stats on stored facts | — |

## Analysis Tools

| # | Tool | Purpose | Key Args |
|---|------|---------|----------|
| 17 | `debug_test` | Test if MCP server is working | — |
| 18 | `generate_insights` | Trigger Zettelkasten insight generation | `topic`, `confidence_threshold` |
| 19 | `query_knowledge` | Query knowledge graph via natural language | `query`, `include_insights`, `max_results` |
| 20 | `explore_connections` | Traverse graph around entity | `entity`, `depth`, `connection_types` |
| 21 | `analyze_semantic_structure` | Montague Grammar parsing | `text`, `include_logical_form` |
| 22 | `ingest_text` | Process text into knowledge graph | `text`, `source`, `metadata` |

## Quick Lookup

| Task | Tool(s) |
|------|---------|
| Find broken links | `wiki_lint` |
| Fix orphan page | `wiki_search` + `wiki_write_page` |
| Rebuild after fixes | `wiki_update_index` |
| Find cross-link candidates | `wiki_cluster_pages` |
| Identify key pages | `wiki_hits_analysis` |
| Log decision | `synapse_remember` |
| Find what caused X | `synapse_causal_window` |