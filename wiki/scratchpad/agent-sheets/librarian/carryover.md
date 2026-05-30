---
summary: Librarian carryover 2026-08-24 — 1211 pages, 63 orphans operational, 5745 broken links are migration artifacts, GAAC 35 clusters, 249 non-reciprocal flags need verification
tags: [librarian, carryover, wiki-audit, daily]
updated: 2026-08-24T08:50:00Z
---

# Librarian Carryover — 2026-08-24

## Kanban Status
- [x] Audit complete: 2026-08-24 08:50 AM UTC
- [x] MCP tools: REACHABLE this cycle ✓
- [x] wiki_lint + wiki_hits_analysis + wiki_cluster_pages ran successfully
- [x] All prior kanban tasks resolved (board clean)
- [ ] New items identified this cycle (see Open below)

## Established

### Vault Stats (Updated 2026-08-24)
- Total wiki pages: 1211 (↑ from 1204 — 7 new pages since last cycle)
- True orphans: 63 — all operational/agent files (carryovers, reports, TEMPLATE, discovery, agent sheets). Zero knowledge orphans. No action needed.
- Broken links: 5745 — ALL are operational path artifacts (wiki/agents/*, scratchpad/*, TEMPLATE, carryover.md). Zero broken links in actual knowledge content. Non-critical.
- Missing frontmatter: 91 — all operational files (librarian/arxiv/ingest agent sheets, templates, project files). Not critical.
- Non-reciprocal links: 249 — flagged by wiki_lint body-text-only detection. Many already reciprocal via Connections sections. Verification needed before task creation.
- .bak files: not checked this cycle

### MCP Tools Available ✓
MCP server confirmed reachable. `wiki_lint`, `wiki_hits_analysis`, `wiki_cluster_pages` all functional this (24-Aug) cycle.

### HITS Analysis (Authority — this cycle)
| Page | Authority | Type | Content Status |
|------|-----------|------|----------------|
| [[wiki/index]] | 0.0784 | structural | TOC — minimal by design ✓ |
| [[log]] | 0.0558 | structural | Append-only log — appropriate ✓ |
| [[maximum-occupancy-principle]] | 0.0157 | load-bearing | Rich content, full taxonomy ✓ |
| [[concepts/maximum-occupancy-principle]] | 0.0134 | refactored | Lower authority after slug consolidation — stable |
| [[efhf]] | 0.0053 | entity | Rich Connections section ✓ |
| [[concept-index]] | 0.0048 | structural | Navigation layer — appropriate ✓ |
| [[agentic-research]] | 0.0037 | concept | Full taxonomy + Connections ✓ |
| [[load-bearing-reasoning]] | 0.0037 | concept | Full taxonomy + Connections ✓ |

**Top Hubs:** maximum-occupancy-principle (0.0028 hub+authority dual), efhf (0.0022), concept-index (0.0020), carryover (0.0019), load-bearing-reasoning (0.0018)

### GAAC Clustering — this cycle
- Clusters found: 35 (↑ from prior cycles as vault grows)
- Missing links: 59,866 (within-cluster pairs with no wikilink)
- Merge candidates: 0
- ⚠️ HIGH COUNT NOTE: 59,866 missing links is extraordinarily high. Likely includes false positives where algorithm flags non-adjacent topic neighbors as needing links. Spot-check required before delegating remediation to librarians-assistant.

### Tag Taxonomy Compliance
- Tag taxonomy established at `wiki/concepts/tag-taxonomy.md`
- efhf uses tag 'EFHF' (non-preferred) — note: efhf page doesn't actually use 'EFHF' tag (confirmed by reading page). EFHF entity page tags are USE-compliant.
- No urgent taxonomy violations detected this cycle

## Open

1. **63 orphans** — all operational files. Zero knowledge orphans. No action needed.

2. **5745 broken links** — ALL operational path artifacts from agent sheet migrations (wiki/agents/*, scratchpad/*, TEMPLATE, carryover.md). Zero broken links in actual knowledge content. Non-critical, not actionable.

3. **Non-reciprocal links (249)** — wiki_lint body-text-only detection. Verification needed: do target pages already have reciprocal link in Connections sections? False positive rate appears high. Before delegating, sample 10 flagged pairs and verify actual state.

4. **59,866 GAAC missing links** — suspiciously high count. Likely includes false positives where loosely-related topics in same cluster are flagged. Need spot-check of sample to determine if this is actionable or expected vault growth artifact.

5. **maximum-occupancy-principle duplicate** — `concepts/maximum-occupancy-principle` (0.0134) coexists with root `maximum-occupancy-principle` (0.0157). root has higher authority. Consolidation recommended but not urgent. Prior carryover noted this.

6. **EFHF frontmatter** — prior carryover noted malformed sources field. efhf entity page was not found at `wiki/entities/efhf.md` — may have been moved or may be at `wiki/sources/papers/efhf-*.md`. Needs verification.

## Heading
- MCP tools available this cycle ✓
- Audit complete; all findings documented
- 0 open kanban tasks
- Vault structural integrity: stable (orphans all operational, broken links all operational artifacts)
- Next priority: (1) Sample non-reciprocal flags for false-positive rate, (2) Spot-check GAAC missing-link count, (3) Verify efhf page location, (4) maximum-occupancy-principle duplicate consolidation