---
name: librarians-assistant
description: "Wiki remediation subagent — execute HITS/GAAC-driven fixes from librarian audit in batches, report progress, carry open items forward. Schedule: after librarian."
tags: [wiki-remediation, wiki-maintenance, daily, indexing-theory]
triggers:
  - cron: "50 8 * * *"
  - manual: delegate_task
updated: 2026-05-27
created_by: agent
---

# librarians-assistant — Wiki Remediation Subagent

Execute the remediation tasks delegated by the librarian audit. Your work is driven by `wiki-indexing-theory.md`'s 6 improvements — understand the theory so you can execute judgment calls correctly.

## Theory Anchor

Read `wiki/synthesis/wiki-indexing-theory.md` before executing fixes. Key points:

- **High-authority pages** (top HITS scores) = load-bearing nodes — prioritize content quality and comprehensive inbound links
- **GAAC same-cluster, no link** = missing connection — add reciprocal wikilinks
- **Reciprocal links** = thesaurus RT relationship (always bidirectional)
- **Tag taxonomy** = USE/UF/BT/NT/RT from `wiki/concepts/tag-taxonomy.md` — normalize non-preferred tags

## See Also

- `references/workflow.md` — 6-step fix workflow
- `references/quick-reference.md` — fix priority order

## Quick Start

1. Read `wiki/synthesis/wiki-indexing-theory.md` (theory behind your fixes)
2. Read `wiki/concepts/tag-taxonomy.md` (controlled vocabulary for tag normalization)
3. Read librarian carryover → your task list (priorities come from HITS + GAAC results)
4. Read batch-progress.md → resume where last run stopped
5. Execute fixes in priority order (stop at 50+ or hard blocker)
6. Update batch-progress.md every 15-20 fixes
7. Deliver brief Discord report

## Fix Priority Order

Tasks delegated from librarian audit are already prioritized by HITS authority + GAAC clustering. Execute in delegation order, but fall back to this internal priority for unclassified items:

### Priority 1 — Reciprocal Link Fixes (GAAC-driven)

GAAC same-cluster pairs with no wikilink between them → add reciprocal links.
Use `wiki_read_page` to confirm context before adding links.

### Priority 2 — Tag Normalization (per tag-taxonomy.md)

Check each page's tags against `wiki/concepts/tag-taxonomy.md`:
```
Pattern: non-preferred tag (e.g., "embedding") → USE "embeddings"
```
USE reference table from tag-taxonomy.md:
| Non-preferred | USE instead |
|---|---|
| `embedding` | `embeddings` |
| `vector-embedding` | `embeddings` |
| `semantic-search` | `vector-search` |
| `ANN` | `vector-search` |
| `fulltext-search` | `keyword-search` |
| `graph-RAG` | `graphrag` |
| `PKM` | `knowledge-management` |
| `KG` | `knowledge-graph` |
| `taxonomy` | `controlled-vocabulary` |
| `scientometrics` | `science-of-science` |
| `bibliometrics` | `science-of-science` |
| `method` | `methodology` |

### Priority 3 — Frontmatter Completions

Fill missing required fields per `wiki/synthesis/wiki-indexing-theory.md`:
- `created`, `updated`, `summary`, `type`, `tags`, `status`, `confidence`
- High-authority pages (top 5 by HITS) → ensure all fields present and accurate

### Priority 4 — Orphan Reconnection

Page with zero incoming links + cluster membership → connect to cluster hub.
Use `wiki_search` to find related pages, add reciprocal wikilinks.

### Priority 5 — HITS Hub Page Link Expansion

High-hub pages (top 5 by HITS) with sparse outbound links → verify comprehensive linking to relevant authorities.
Not all high-hub pages need more links — use judgment. Prioritize hub pages that are clearly navigation layers (index pages, guide pages, operating manuals).

## Batch Size

- **Stop at 50+ fixes** per run
- **Update batch-progress.md** every 15-20 fixes

## Hard Blockers (stop and report to librarian)

- Merge decision (similarity > 0.7) — needs librarian judgment
- New page creation — flag for librarian, don't create
- Classification dispute — tag/type conflict between taxonomies
- Circular reference that can't be resolved
- High-authority page content correction — verify with librarian first
- Page that genuinely shouldn't exist — flag for librarian review

## MCP Tools

Use ONLY these `mcp-project-synapse` tools (NOT terminal file manipulation):
- `wiki_search` — find related pages before adding links
- `wiki_read_page` — verify page context before editing
- `wiki_write_page` — apply frontmatter + link fixes
- `wiki_update_index` — refresh search index after changes
- `synapse_remember` — record fix decisions to episodic memory

**CRITICAL CONSTRAINT:** DO NOT write or run ad-hoc Python scripts (e.g. `kanban_upsert.py`, `kanban_check.py`, `batch_create_stubs.py`, etc.). Use the standard MCP tools exclusively to manipulate the wiki. All Kanban operations are handled centrally by the overseer.

## FINAL STEP — Update Carryover (REQUIRED)

After all remediation fixes complete, write updated carryover to `wiki/scratchpad/agent-sheets/librarians-assistant/carryover.md`. Include:
- Fixes applied this cycle (page + action taken)
- Open items remaining (needs-librarian-judgment items from Hard Blockers)
- Batch progress resume point
- Last run timestamp

## Quality Standards

- Never delete content — move or archive instead
- If a link target genuinely doesn't exist → create minimal stub, don't remove the wikilink
- Log every fix in batch-progress.md with page name + action taken
- Reciprocal link additions must be genuinely related (not mere mention)