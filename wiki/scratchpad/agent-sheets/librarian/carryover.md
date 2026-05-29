---
summary: Librarian carryover 2026-05-29 — audit complete, 57 orphans operational, HITS authority leader wiki/index (0.0786)
tags: [librarian, carryover, wiki-audit, daily]
updated: 2026-05-29T14:20:57Z
---

# Librarian Carryover — 2026-05-29

## Kanban Status
- [x] Audit complete: 2026-05-29 08:XX AM UTC
- [x] MCP tools: REACHABLE this cycle ✓
- [x] wiki_lint + wiki_hits_analysis + wiki_cluster_pages ran successfully
- [x] All prior kanban tasks resolved (board clean)
- [ ] New items identified this cycle (see Open below)

## Established

### Vault Stats (Updated 2026-05-29)
- Total wiki pages: 1204 (↑ from 1196 — 8 new pages since last cycle)
- True orphans: 57 (↑ from 54 — all operational files: carryovers, reports, TEMPLATE, discovery files, SKILL files, agent sheets)
- Orphan breakdown: all operational/non-content files. Zero knowledge orphans. No action needed.
- .bak files: 0 (clean)
- Broken links: operational artifacts (wiki/agents/* paths, discovery reports, TEMPLATE, carryovers) — not critical
- Missing frontmatter: operational files — carryovers, SKILLs, templates, project files
- Non-reciprocal links: detectable via wiki_lint — body-text only, produces false positives

### MCP Tools Available ✓
MCP server confirmed reachable. `wiki_lint`, `wiki_hits_analysis`, `wiki_cluster_pages` all functional this (29-May) cycle.

### HITS Analysis (Top Authorities — this cycle)
1. [[wiki/index]] (0.0786) — structural hub
2. [[log]] (0.0561) — structural hub
3. [[maximum-occupancy-principle]] (0.0160) — load-bearing concept page
4. [[concepts/maximum-occupancy-principle]] (0.0138) — duplicate slug variant (lower score = refactored to canonical root)
5. [[efhf]] (0.0053) — entity page (rich Connections section)
6. [[concept-index]] (0.0048) — structural hub
7. [[agentic-research]] (0.0037) — concept page (rich content, multiple Connections)
8. [[load-bearing-reasoning]] (0.0037) — concept page (rich content, full taxonomy + Connections)

**Top Hubs:**
- [[maximum-occupancy-principle]] (hub+authority dual) — needs link expansion
- [[efhf]], [[concept-index]], [[carryover]], [[load-bearing-reasoning]], [[edm-framework]], [[zettelkasten-engine]], [[alphaevolve]]

### GAAC Clustering — Key Clusters
Clusters flagged from this cycle's analysis. Notable findings:
- **Cluster 0**: meta-advancement, Meta-Meta Process, discrete-time-to-event-modeling, solo-preneur — 6 missing links within cluster
- **Cluster 1**: governance/AI-safety cluster (absence-of-worst-case-metric, accountability, agentic-oversight, ai-governance, ai-safety, etc.)
- Cluster truncation due to output limits; full cluster data pending next cycle

### Tag Taxonomy Compliance
- Tag taxonomy is established at `wiki/concepts/tag-taxonomy.md`
- Page tags reviewed for USE-compliant terms (efhf uses non-preferred tag 'EFHF' — non-critical)
- No urgent taxonomy violations detected this cycle

### Content Depth Verification (Top Authority Pages)
| Page | Authority | Content Status |
|------|-----------|----------------|
| [[wiki/index]] (0.0786) | structural | TOC — minimal content by design |
| [[log]] (0.0561) | structural | Append-only log — appropriate |
| [[maximum-occupancy-principle]] (0.0160) | load-bearing | Rich content, well-linked |
| [[efhf]] (0.0053) | entity | Rich Connections section (50+ links) |
| [[concept-index]] (0.0048) | structural | Navigation layer — appropriate |
| [[agentic-research]] (0.0037) | concept | Full taxonomy + Connections |
| [[load-bearing-reasoning]] (0.0037) | concept | Full taxonomy + Connections |

## Open

1. **57 orphans** — all operational files. Zero knowledge orphans. No action needed.

2. **Missing frontmatter** — all operational files. Not critical; librarians-assistant can batch-fix if capacity allows.

3. **Non-reciprocal links** — wiki_lint body-text-only detection produces false positives (many already reciprocal via Connections sections). librarians-assistant should verify target page before creating fix tasks.

4. **maximum-occupancy-principle duplicate** — `concepts/maximum-occupancy-principle` (0.0138) coexists with root `maximum-occupancy-principle` (0.0160). root has higher authority. Consolidation recommended but not urgent.

5. **Cluster 0 missing links** — 6 missing links within meta-advancement cluster (meta-advancement ↔ Meta-Meta Process ↔ discrete-time-to-event-modeling ↔ solo-preneur). Delegated to librarians-assistant.

6. **EFHF frontmatter issue** — sources field contains malformed characters (`[']', '[[maximum-occupancy-principle]']`). Non-critical but should be corrected.

7. **efhf tag** — entity page uses tag 'EFHF' which is non-preferred; preferred term per taxonomy TBD. Not blocking.

## Heading
- MCP tools available this cycle ✓
- Audit complete; all findings documented
- 0 open kanban tasks
- Vault structural integrity: stable (orphans all operational)
- Next priority: Cluster 0 missing-link remediation + maximum-occupancy-principle duplicate consolidation + EFHF frontmatter fix
