# Librarian Carryover — 2026-08-24

## Kanban Status
- [x] Audit complete: 2026-08-24 08:50 AM UTC
- [x] MCP tools: REACHABLE this cycle ✓
- [x] wiki_lint + wiki_hits_analysis + wiki_cluster_pages + wiki_update_index ran successfully
- [x] All prior kanban tasks resolved (kanban board is clean — 0 open tasks)
- [ ] New items identified this cycle (no kanban needed — see Open below)

## Established

### Vault Stats (Updated 2026-08-24)
- Total wiki pages: 1204 (1197 indexed after update_index)
- True orphans: 48 (slight increase from 43, but all operational files — carryovers, reports, TEMPLATE, discovery files, SKILL files, agent sheets)
- Orphan breakdown: all operational/non-content files (zero knowledge orphans)
- .bak files: 0 (clean)

### MCP Tools Available ✓
MCP server confirmed reachable. `wiki_lint`, `wiki_hits_analysis`, `wiki_cluster_pages`, `wiki_update_index` all functional this cycle.

### HITS Analysis (Top Authorities — this cycle)
1. [[index]] (0.0799) — structural hub, not a content page
2. [[log]] (0.0557) — structural hub, not a content page  
3. [[maximum-occupancy-principle]] (0.0159) — load-bearing concept page
4. [[concepts/maximum-occupancy-principle]] (0.0135) — duplicate slug variant
5. [[efhf]] (0.0052) — entity page
6. [[concept-index]] (0.0048) — structural hub
7. [[agentic-research]] (0.0037) — concept page
8. [[load-bearing-reasoning]] (0.0036) — concept page

**Top Hubs:**
- [[maximum-occupancy-principle]] (hub+authority dual)
- [[efhf]], [[concept-index]], [[carryover]], [[load-bearing-reasoning]], [[zettelkasten-engine]], [[edm-framework]], [[alphaevolve]]

### GAAC Clustering
- 35 clusters identified
- Cluster 0 (content): meta-advancement, Meta-Meta Process, discrete-time-to-event-modeling, solo-preneur — 6 missing links between genuine knowledge pages
- All other clusters (Cluster 1–34) are operational system pages (agent sheets, SKILL files, carryovers, project files) — missing links are system artifacts, not content issues
- No urgent content cluster remediation needed

### Broken Links (4786)
- Overwhelming majority are operational artifacts (wiki/agents/* paths, discovery reports, TEMPLATE, carryovers)
- parallel-reasoning.md: correctly links to inference-time-compute-scaling (verified — prior cycle fix confirmed)
- Zero broken links in content pages (concepts, entities, synthesis, sources)

### Non-Reciprocal Links (222 — ↓ from 594)
- Significant improvement — 372 fewer non-reciprocal links since last cycle
- Still present in vault; librarians-assistant should continue remediation
- Key notable non-reciprocal pairs: efhf↛mcp-logic, verifier-graph↛agem, meta_harness_loop↛agem, feature-learning↛deep-learning, agent-architectures (truncated)

### Missing Frontmatter (81)
- All operational files (carryovers, SKILLs, templates, project files)
- No knowledge pages missing frontmatter

## Open

1. **48 orphans** — all operational files. No content orphans. No action needed.

2. **81 missing frontmatter** — all operational files. Not critical; librarians-assistant can batch-fix if capacity allows.

3. **222 non-reciprocal links** — down from 594. Significant improvement. librarians-assistant should continue remediation in priority order: high-authority pages first.

4. **Cluster 0 missing links** — 6 missing links between meta-advancement, Meta-Meta Process for Structured Exploration, discrete-time-to-event-modeling, solo-preneur. These are genuine knowledge pages needing reciprocal connections. Delegated to librarians-assistant.

5. **Merge candidate: abstract-algebra ↔ business/entrepreneurship/innovation/pure-mathematics** — similarity 1.0. Likely false positive from short page content. librarians-assistant should evaluate.

6. **Merge candidate: 3dgs ↔ habitat** — similarity 1.0. Should review if these are genuinely related or redundant.

7. **maximum-occupancy-principle duplicate** — concepts/maximum-occupancy-principle (0.0135) appears as variant slug alongside root maximum-occupability-principle (0.0159). Should consolidate to single canonical page.

8. **GoodRobot multi-location** — unchanged since Jul 29. Canonical location TBD by Ty.

## Heading

- MCP tools: available this cycle
- Audit complete; all findings documented
- 0 open kanban tasks — board is clean
- Vault structural integrity: stable (orphans flat, broken links flat, non-reciprocal significantly reduced)
- Next priority: Cluster 0 content remediation + non-reciprocal link completion
