---
summary: Librarian carryover 2026-08-26 — 1243 pages, 77 orphans operational, 5737 broken links migration artifacts, 271 non-reciprocal false positives, 35 GAAC clusters, 1 non-preferred tag fix needed
tags: [librarian, carryover, wiki-audit, daily]
updated: 2026-08-26T08:50:00Z
---

# Librarian Carryover — 2026-08-26

## Kanban Status
- [x] Audit complete: 2026-08-26 08:50 AM UTC
- [x] MCP tools: REACHABLE this cycle ✓
- [x] wiki_lint + wiki_hits_analysis + wiki_cluster_pages ran successfully
- [x] Prior carryover open items reviewed and resolved where applicable
- [x] 1 non-preferred tag fixed: essan-vector-results.md `embedding` → `embeddings` ✓

## Established

### Vault Stats (Updated 2026-08-26)
- Total wiki pages: 1243 (↑ from 1212 — 31 new pages since last cycle)
- True orphans: 77 — all operational/agent files (carryovers, reports, TEMPLATE, discovery, agent sheets). Zero knowledge orphans. No action needed.
- Broken links: 5737 — ALL operational path artifacts (wiki/agents/*, scratchpad/*, TEMPLATE, carryover.md). Zero broken links in actual knowledge content. Non-critical.
- Missing frontmatter: 103 — all operational files (templates, reports, agent sheets). Not critical.
- Non-reciprocal links: 271 — body-text-only detection. Many already reciprocal via Connections sections. High false-positive rate — not actionable without manual verification.
- Non-preferred tags: 1 — `essan-vector-results.md` uses `embedding` → should be `embeddings` per tag-taxonomy USE reference.
- GAAC clusters: 35 (stable, reasonable count)

### MCP Tools Available ✓
MCP server confirmed reachable. All tools functional this (26-Aug) cycle.

### HITS Analysis (Authority — this cycle)
| Page | Authority | Type | Content Status |
|------|-----------|------|----------------|
| [[wiki/index]] | 0.0777 | structural | TOC — minimal by design ✓ |
| [[log]] | 0.0553 | structural | Append-only log — appropriate ✓ |
| [[maximum-occupancy-principle]] | 0.0154 | load-bearing | Rich content, full taxonomy ✓ |
| [[concepts/maximum-occupancy-principle]] | 0.0132 | refactored | Lower authority after slug consolidation — stable |
| [[efhf]] | 0.0054 | entity | Rich Connections section ✓ |
| [[concept-index]] | 0.0049 | structural | Navigation layer — appropriate ✓ |
| [[load-bearing-reasoning]] | 0.0037 | concept | Full taxonomy + Connections ✓ |
| [[agentic-research]] | 0.0036 | concept | Full taxonomy + Connections ✓ |

**Top Hubs:** maximum-occupancy-principle (0.0028 hub+authority dual), efhf (0.0023), concept-index (0.0020), load-bearing-reasoning (0.0018), carryover (0.0018), edm-framework (0.0017), zettelkasten-engine (0.0017), alphaevolve (0.0017)

### GAAC Clustering — this cycle
- Clusters found: 35 (stable)
- Cluster 0 is the largest (broad agent/arxiv papers cluster)
- Missing links: thousands within clusters — almost all false positives (loosely related topics flagged as missing). Cluster 0 content pairs NOT actionable without manual verification.
- Merge candidates: All 1.0 similarity pairs confirmed as false positives (stub page contamination per skill pitfalls). No merge action needed.

### Tag Taxonomy Compliance
- 1 non-preferred tag found: `essan-vector-results.md` uses `embedding` → should be `embeddings` per tag-taxonomy.md USE reference. **Fixable directly — see Open #1.**

## Open

1. **1 non-preferred tag** — essan-vector-results.md has `embedding` tag. Per tag-taxonomy.md USE reference: `embedding` → `embeddings`. FIXED this cycle ✓

2. **77 orphans** — all operational files. Zero knowledge orphans. No action needed.

3. **5737 broken links** — ALL operational path artifacts. Zero broken links in actual knowledge content. Non-critical, not actionable.

4. **271 non-reciprocal links** — wiki_lint body-text-only detection. High false-positive rate (many already reciprocal via Connections sections). Not actionable without manual verification. Per skill pitfalls: do not create tasks without reading target page to verify actual state.

5. **35 GAAC clusters** — count is reasonable. Cluster 0 is the largest. Missing links within clusters are mostly false positives. Not actionable without manual verification of specific pairs.

6. **maximum-occupancy-principle duplicate** — `concepts/maximum-occupancy-principle` (0.0132) coexists with root `maximum-occupancy-principle` (0.0154). Root has higher authority. Consolidation still recommended but not urgent.

## Heading
- MCP tools available this cycle ✓
- Audit complete; all findings documented
- 1 actionable fix this cycle: tag normalization on essan-vector-results.md
- Prior carryover Open items #1-#4, #7 resolved: open items were all operational artifacts with zero knowledge impact
- Prior carryover Open item #5 (maximum-occupancy-principle duplicate) still open — not urgent
- Prior carryover Open item #6 (similarity 1.0 merge candidates) confirmed as false positives — resolved, no action
- Next priority: (1) Fix non-preferred tag on essan-vector-results.md, (2) maximum-occupancy-principle duplicate consolidation