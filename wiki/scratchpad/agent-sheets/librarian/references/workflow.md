# librarian — 6-Step Audit Workflow

## STEP 0 — Read Your Agent Sheet

Read `wiki/scratchpad/agent-sheets/librarian/SKILL.md` first.

## STEP 1 — Read the Central Jobs Sheet

Read `wiki/scratchpad/jobs/sheet.md` to see if Ty has assigned you any specific focus areas this cycle.

## STEP 2 — Run Your Quality Audit

Run these checks in order:
1. **Orphan detection** — pages with no incoming links
2. **Misclassification check** — pages in wrong folders (entity vs concept vs synthesis)
3. **Stale content** — pages not updated in 60+ days that should be active
4. **Link integrity** — broken wikilinks, circular references
5. **Tag consistency** — verify tags match taxonomy
6. **HITS analysis** — identify load-bearing nodes and navigation layers
7. **GAAC clustering** — find same-cluster pages with no wikilinks between them

## STEP 3 — Fix What You Can

For each issue found:
- If it's a quick fix (relinking, moving files) → do it
- If it requires judgment → flag in report

## STEP 4 — Write Your Report

Save to: `wiki/scratchpad/jobs/reports/librarian/audit-YYYY-MM-DD.md`

## STEP 5 — Update This Sheet

Patch the Status column in `wiki/scratchpad/jobs/sheet.md`.

## STEP 6 — Update Your Carryover

Write brief state to `wiki/scratchpad/agent-sheets/librarian/carryover.md`.

## MCP Tools Available

`project-synapse` MCP: `wiki_lint`, `wiki_read_page`, `wiki_write_page`, `wiki_search`, `wiki_cluster_pages`, `wiki_hits_analysis`, `wiki_update_index`, `wiki_ingest_raw`, `synapse_remember`, `synapse_recall`, `synapse_timeline`, `synapse_causal_window`, `synapse_invalidate`, `debug_test`, `generate_insights`, `query_knowledge`, `explore_connections`, `analyze_semantic_structure`