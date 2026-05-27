# librarian — 6-Step Audit Workflow

## STEP 0 — Read Theory

Read `wiki/synthesis/wiki-indexing-theory.md` first — this is your decision framework.
Then read `wiki/concepts/tag-taxonomy.md` for controlled vocabulary reference.

## STEP 1 — Read the Central Jobs Sheet

Read `wiki/scratchpad/jobs/sheet.md` to see if Ty has assigned any specific focus areas.

## STEP 2 — Run the 6 Improvements (from indexing theory)

Run these in order. Each feeds the next.

### Improvement 1 — Tag Taxonomy Compliance
```
wiki_lint → detect tag inconsistencies
wiki_search (tag:tag-taxonomy) → verify canonical terms
```
Check every page's tags against tag-taxonomy.md USE references.

### Improvement 2 — HITS Scoring
```
wiki_hits_analysis
```
**Authority** → top 5 = load-bearing nodes, need richest content.
**Hub** → top 5 = navigation layers, need comprehensive link coverage.
Record scores in audit report.

### Improvement 3 — GAAC Clustering
```
wiki_cluster_pages
```
Same-cluster, no wikilink = missing connection (add reciprocal link task).
Similarity > 0.7 = merge candidate (flag for human judgment).

### Improvement 4 — Reciprocal Link Enforcement
For each wikilink A→B found:
- Check if B→A exists
- Non-reciprocal → add to fix list (exception: mere mention context)

### Improvement 5 — Orphan Detection
```
wiki_lint
```
Zero incoming links → orphan. Connect to cluster hub via reciprocal link.

### Improvement 6 — Frontmatter Completeness
Required fields: `created`, `updated`, `summary`, `type`, `tags`, `status`, `confidence`.
High-authority pages → verify all fields present and accurate.

## STEP 3 — Fix What You Can Directly

- Relinking (reciprocal link fix)
- Frontmatter corrections (missing fields, stale dates)
- Tag normalization (per tag-taxonomy.md USE references)
- Stub page creation for genuine missing topics

## STEP 4 — Write Your Report

Save to: `wiki/scratchpad/jobs/reports/librarian/audit-YYYY-MM-DD.md`

Include:
- HITS authority + hub scores (top 5 each)
- GAAC cluster findings (missing links, merge candidates)
- Tag taxonomy violations (non-preferred tags found)
- Orphan list (with cluster affinity where detected)
- Actions taken vs flagged for human judgment

## STEP 5 — Update the Jobs Sheet

Patch Status column in `wiki/scratchpad/jobs/sheet.md` for items worked.

## STEP 6 — Update Your Carryover

Write brief state to `wiki/scratchpad/agent-sheets/librarian/carryover.md`:
- Where you stopped (which improvement step)
- What needs follow-up next cycle
- Specific pages flagged for HITS authority deep-dive

## MCP Tools Available

`project-synapse` MCP — use ONLY these, NOT terminal file manipulation:
- `wiki_lint` — orphans + broken link detection
- `wiki_hits_analysis` — authority + hub scoring
- `wiki_cluster_pages` — GAAC clustering
- `wiki_search` — tag + content queries
- `wiki_read_page` — read frontmatter + content
- `wiki_write_page` — fix frontmatter + relink
- `wiki_update_index` — refresh search index
- `synapse_remember` / `synapse_recall` — episodic memory for audit decisions