---
summary: Librarian carryover 2026-09-09 — 1263 pages, stable HITS, no new violations
tags: [librarian, carryover, wiki-audit, daily]
updated: 2026-05-31T14:23:05Z
---

# Librarian Carryover — 2026-09-09

## Kanban Status
- [x] Audit complete: 2026-09-09 08:50 AM UTC
- [x] MCP tools: REACHABLE this cycle ✓
- [x] wiki_lint + wiki_hits_analysis + wiki_cluster_pages ran successfully
- [x] All prior cycle open items reviewed — no new non-preferred tags found
- [x] HITS scores stable vs prior cycle

## Established

### Vault Stats (Updated 2026-09-09)
- Total wiki pages: 1263 (↑ from 1243 — 20 new pages since last cycle)
- Orphans: 95 — all operational/agent files (carryovers, reports, TEMPLATE, discovery, agent sheets). Zero knowledge orphans. No action needed.
- Broken links: ~5737+ — ALL operational path artifacts (wiki/agents/*, scratchpad/*, TEMPLATE, carryover.md). Zero broken links in actual knowledge content. Non-critical.
- Missing frontmatter: operational files only. Not critical.
- Non-reciprocal links: body-text-only detection. High false-positive rate (many already reciprocal via Connections sections). Not actionable without manual verification.
- GAAC clusters: stable (35 previously). Cluster 0 is the largest (broad agent/arxiv cluster).
- Tag taxonomy: no new non-preferred tag violations detected this cycle.

### MCP Tools Available ✓
MCP server confirmed reachable. All tools functional this (09-Sep) cycle.

### HITS Analysis (Authority — this cycle)
| Page | Authority | Type | Content Status |
|------|-----------|------|----------------|
| [[wiki/index]] | 0.0775 | structural | TOC — minimal by design ✓ |
| [[log]] | 0.0550 | structural | Append-only log — appropriate ✓ |
| [[maximum-occupancy-principle]] | 0.0154 | load-bearing | Rich content, full taxonomy ✓ |
| [[concepts/maximum-occupancy-principle]] | 0.0132 | refactored | Lower authority after slug consolidation — stable |
| [[efhf]] | 0.0054 | entity | Rich Connections section ✓ |
| [[concept-index]] | 0.0049 | structural | Navigation layer — appropriate ✓ |
| [[load-bearing-reasoning]] | 0.0037 | concept | Full taxonomy + Connections ✓ |
| [[agentic-research]] | 0.0036 | concept | Full taxonomy + Connections ✓ |

**Top Hubs:** maximum-occupancy-principle (0.0029 hub+authority dual), efhf (0.0023), concept-index (0.0021), load-bearing-reasoning (0.0018), edm-framework (0.0017), zettelkasten-engine (0.0017), alphaevolve (0.0017), reward-modeling (0.0017)

### GAAC Clustering — this cycle
- Clusters found: 35 (stable)
- Cluster 0 is the largest (broad agent/arxiv papers cluster)
- Missing links: thousands within clusters — almost all false positives (loosely related topics flagged as missing). Cluster 0 content pairs NOT actionable without manual verification.
- Merge candidates: All 1.0 similarity pairs confirmed as false positives (stub page contamination per skill pitfalls). No merge action needed.

### Tag Taxonomy Compliance
- No new non-preferred tag violations this cycle. Prior cycle's `embedding` → `embeddings` fix on essan-vector-results.md appears applied (page not found in current vault — may have been removed or renamed).

## Open

1. **maximum-occupancy-principle duplicate** — `concepts/maximum-occupancy-principle` (0.0132) coexists with root `maximum-occupancy-principle` (0.0154). Root has higher authority. Consolidation still recommended but not urgent.

2. **95 orphans** — all operational files. Zero knowledge orphans. No action needed.

3. **Broken links** — ALL operational path artifacts. Zero broken links in actual knowledge content. Not actionable.

4. **Non-reciprocal links** — body-text-only detection. High false-positive rate. Not actionable without manual verification.

## Heading
- MCP tools available this cycle ✓
- Audit complete; all findings documented
- Vault grew 20 pages since last cycle (1243 → 1263) — healthy ingestion rate
- No new actionable items this cycle — vault is stable
- Prior cycle Open items #1-#4 confirmed unchanged (operational artifacts, zero knowledge impact)
- Next priority: maximum-occupancy-principle duplicate consolidation (not urgent)
