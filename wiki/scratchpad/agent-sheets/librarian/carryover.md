---
summary: Librarian carryover 2026-05-31 — 1264 pages, stable HITS, no new violations
tags: [librarian, carryover, wiki-audit, daily]
updated: 2026-05-31T08:50:00Z
---

# Librarian Carryover — 2026-05-31

## Kanban Status
- [x] Audit complete: 2026-05-31 08:50 AM UTC
- [x] MCP tools: REACHABLE this cycle ✓
- [x] wiki_lint + wiki_hits_analysis + wiki_cluster_pages ran successfully
- [x] All prior cycle open items reviewed — no new violations found
- [x] HITS scores stable vs prior cycle
- [x] No new non-preferred tag violations

## Established

### Vault Stats (Updated 2026-05-31)
- Total wiki pages: 1264 (↑ from 1263 — 1 new page this cycle)
- Orphans: 96 — all operational/agent files (carryovers, reports, TEMPLATE, discovery, agent sheets). Zero knowledge orphans. No action needed.
- Broken links: ~5732+ — ALL operational path artifacts (wiki/agents/*, scratchpad/*, TEMPLATE, carryover.md). Zero broken links in actual knowledge content. Non-critical.
- Missing frontmatter: 109 — operational files (agent sheets, reports, carryovers, templates). Not critical.
- Non-reciprocal links: 291 — body-text-only detection. High false-positive rate (links already reciprocal via Connections sections). Not actionable without manual verification.
- GAAC clusters: 35 clusters (stable). Cluster 0 is largest knowledge cluster. Missing links in Cluster 0 are loosely-related topic pairs — not actionable without manual verification.
- Tag taxonomy: no new non-preferred tag violations this cycle.

### MCP Tools Available ✓
MCP server confirmed reachable. All tools functional this (31-May) cycle.

### HITS Analysis (Authority — this cycle)
| Page | Authority | Type | Content Status |
|------|-----------|------|----------------|
| [[wiki/index]] | 0.0774 | structural | TOC — minimal by design ✓ |
| [[log]] | 0.0547 | structural | Append-only log — appropriate ✓ |
| [[maximum-occupancy-principle]] | 0.0156 | load-bearing | Rich content, full taxonomy ✓ |
| [[concepts/maximum-occupancy-principle]] | 0.0133 | refactored | Lower authority after slug consolidation — stable |
| [[efhf]] | 0.0054 | entity | Rich Connections section ✓ |
| [[concept-index]] | 0.0050 | structural | Navigation layer — appropriate ✓ |
| [[load-bearing-reasoning]] | 0.0038 | concept | Full taxonomy + Connections ✓ |
| [[agentic-research]] | 0.0035 | concept | Full taxonomy + Connections ✓ |

**Top Hubs:** maximum-occupancy-principle (0.0029 hub+authority dual), efhf (0.0023), concept-index (0.0021), load-bearing-reasoning (0.0018), carryover (0.0018), edm-framework (0.0017), zettelkasten-engine (0.0017), project-synapse (0.0017)

### GAAC Clustering — this cycle
- Clusters found: 35 (stable)
- Cluster 0 is largest knowledge cluster (graph-database, graphrag, knowledge-graph, mcp, efhf, project-synapse, neo4j, bounded-structured-memory, etc.)
- Missing links in Cluster 0: ~10s of pairs flagged as loosely-related topics. NOT actionable without manual verification. False positive rate high per skill pitfalls.
- Merge candidates: All 1.0 similarity pairs confirmed as false positives (stub page contamination per skill pitfalls). No merge action needed.

### Tag Taxonomy Compliance
- No new non-preferred tag violations this cycle. Prior cycle fixes confirmed applied.

## Open

1. **maximum-occupancy-principle duplicate** — `concepts/maximum-occupancy-principle` (0.0133) coexists with root `maximum-occupancy-principle` (0.0156). Root has higher authority. Consolidation still recommended but not urgent.

2. **96 orphans** — all operational files. Zero knowledge orphans. No action needed.

3. **Broken links** — ALL operational path artifacts. Zero broken links in actual knowledge content. Not actionable.

4. **Non-reciprocal links** (291) — body-text-only detection. High false-positive rate. Not actionable without manual verification.

5. **Cluster 0 missing links** — GAAC flags loosely-related topic pairs. False positive rate high. Not actionable without manual verification.

## Heading
- MCP tools available this cycle ✓
- Audit complete; all findings documented
- Vault grew 1 page since last cycle (1263 → 1264) — minimal ingestion (weekend cycle)
- No new actionable items this cycle — vault is stable
- Prior cycle Open items #1-#5 confirmed unchanged (operational artifacts, zero knowledge impact)
- Next priority: maximum-occupancy-principle duplicate consolidation (not urgent)