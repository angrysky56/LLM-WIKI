---
summary: Librarian carryover 2026-08-25 — 1212 pages, 66 orphans operational, 5745 broken links migration artifacts, 249 non-reciprocal flags need verification, 35 GAAC clusters, merge candidates need investigation
tags: [librarian, carryover, wiki-audit, daily]
updated: 2026-08-25T08:50:00Z
---

# Librarian Carryover — 2026-08-25

## Kanban Status
- [x] Audit complete: 2026-08-25 08:50 AM UTC
- [x] MCP tools: REACHABLE this cycle ✓
- [x] wiki_lint + wiki_hits_analysis + wiki_cluster_pages ran successfully
- [x] All prior kanban tasks resolved (board clean)
- [ ] New items identified this cycle (see Open below)

## Established

### Vault Stats (Updated 2026-08-25)
- Total wiki pages: 1212 (↑ from 1211 — 1 new page since last cycle)
- True orphans: 66 — all operational/agent files (carryovers, reports, TEMPLATE, discovery, agent sheets). Zero knowledge orphans. No action needed.
- Broken links: 5745 — ALL operational path artifacts (wiki/agents/*, scratchpad/*, TEMPLATE, carryover.md). Zero broken links in actual knowledge content. Non-critical.
- Missing frontmatter: 92 — all operational files (templates, reports, agent sheets). Not critical.
- Non-reciprocal links: 249 — body-text-only detection. Many already reciprocal via Connections sections. Verification still recommended before delegating.
- GAAC clusters: 35 (reasonable count, down from prior inflated counts)
- .bak files: not checked this cycle

### MCP Tools Available ✓
MCP server confirmed reachable. All tools functional this (25-Aug) cycle.

### HITS Analysis (Authority — this cycle)
| Page | Authority | Type | Content Status |
|------|-----------|------|----------------|
| [[wiki/index]] | 0.0785 | structural | TOC — minimal by design ✓ |
| [[log]] | 0.0559 | structural | Append-only log — appropriate ✓ |
| [[maximum-occupancy-principle]] | 0.0157 | load-bearing | Rich content, full taxonomy ✓ |
| [[concepts/maximum-occupancy-principle]] | 0.0134 | refactored | Lower authority after slug consolidation — stable |
| [[efhf]] | 0.0053 | entity | Rich Connections section ✓ |
| [[concept-index]] | 0.0048 | structural | Navigation layer — appropriate ✓ |
| [[agentic-research]] | 0.0037 | concept | Full taxonomy + Connections ✓ |
| [[load-bearing-reasoning]] | 0.0037 | concept | Full taxonomy + Connections ✓ |

**Top Hubs:** maximum-occupancy-principle (0.0028 hub+authority dual), efhf (0.0022), concept-index (0.0020), carryover (0.0018), load-bearing-reasoning (0.0018)

### GAAC Clustering — this cycle
- Clusters found: 35 (↓ from prior inflated counts — more accurate now)
- Missing links: high count within clusters (news/papers clusters generate many flags — expected)
- Merge candidates: Several suspicious pairs with similarity 1.0 (see Open item #2)

### Tag Taxonomy Compliance
- No urgent taxonomy violations detected this cycle
- EFHF entity page confirmed at `wiki/entities/efhf.md` (resolves prior carryover question)

## Open

1. **66 orphans** — all operational files. Zero knowledge orphans. No action needed.

2. **5745 broken links** — ALL operational path artifacts. Zero broken links in actual knowledge content. Non-critical, not actionable.

3. **Non-reciprocal links (249)** — wiki_lint body-text-only detection. False positive rate appears high. Many flagged pairs already reciprocal via Connections sections. Not actionable without manual verification — defer.

4. **35 GAAC clusters** — count is reasonable. Cluster 0 is the largest (agent/arxiv papers cluster). Missing links within clusters are mostly news/papers temporal adjacency — expected, not actionable.

5. **maximum-occupancy-principle duplicate** — `concepts/maximum-occupancy-principle` (0.0134) coexists with root `maximum-occupancy-principle` (0.0157). Root has higher authority. Consolidation still recommended but not urgent.

6. **Merge candidates with similarity 1.0** — flagged pairs:
   - `[[Firecracker]]` ↔ `[[overlayfs]]` (1.0) — need to determine if real similarity or contamination
   - `[[abstract-algebra]]` ↔ `[[business]]`, `[[entrepreneurship]]`, `[[innovation]]`, `[[pure-mathematics]]` (1.0) — likely false positive (abstract math has no business relationship to these)
   - These 1.0 similarity scores suggest possible content contamination or edge case in similarity computation. **Flag for librarians-assistant investigation** — not a clear merge case.

7. **92 missing frontmatter** — all operational files (templates, reports, agent sheets). Not critical.

## Heading
- MCP tools available this cycle ✓
- Audit complete; all findings documented
- 0 open kanban tasks
- Vault structural integrity: stable (orphans all operational, broken links all operational artifacts)
- Next priority: (1) Investigate 1.0 similarity merge candidates — likely false positives, (2) maximum-occupancy-principle duplicate consolidation, (3) EFHF frontmatter resolved (confirmed at wiki/entities/efhf.md)