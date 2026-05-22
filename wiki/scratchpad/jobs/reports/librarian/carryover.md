---
summary: Librarian carryover — 155 orphans, 338 broken links, 110 non-reciprocal, insight gen timed out
tags: [librarian, carryover, audit]
updated: 2026-05-21
---

## Cycle State

**Date:** 2026-05-21  
**Task:** `6ee16837c47c` Wiki Librarian  
**Run via:** delegate_task workaround (cron `48a3a009a820` not firing — last_run_at stays null)

### Audit Complete — Full 10-task checklist run

| # | Check | Result |
|---|-------|--------|
| 1 | Tag consistency | ⚠️ tag-taxonomy.md missing from agent-sheets/ (not found) |
| 2 | HITS authority/hub scoring | ✅ Done — top auth: efhf (0.0467), top hub: concept-index (0.0586) |
| 3 | Reciprocal wikilinks | ❌ **110 non-reciprocal** (A→B without B→A) |
| 4 | GAAC semantic clustering | ✅ Done — massive output (~817KB), many missing-link flags |
| 5 | Conceptual index health | ⚠️ concept-index.md stable (171 lines), last updated 2026-04-28 — **may need refresh** |
| 6 | Mere mention review | ⚠️ Not run as separate step — flagged in broken-links output |
| 7 | Frontmatter completeness | ✅ 31 pages missing frontmatter (carryover from 326 → cleaned by librarians-assistant) |
| 8 | Broken wikilinks repair | ❌ **338 broken** links across vault |
| 9 | Wiki-layer orphan detection | ❌ **155 orphans** — significant regression from 0 at last run |
| 10 | Insight generation trigger | ❌ Timed out after 300s |

### Vault Health Summary

| Metric | This Run | Previous Run (approx) | Delta |
|--------|----------|------------------------|-------|
| Pages | 357 | 344 | +13 |
| Orphans | **155** | 0 | **+155 🚨** |
| Broken links | 338 | 390 | -52 ✅ |
| Missing frontmatter | 31 | 326 | -295 ✅ |
| Non-reciprocal links | 110 | not reported | new |

### Critical Issues

1. **Orphan explosion (155):** Unknown cause — either accumulated since last run or previous scan methodology differed. Many are news/sources articles that may not need inbound links. Needs triage:哪些是真正的孤立页面 vs哪些只是导航页面不需要入站链接。

2. **Non-reciprocal links (110):** Pages that link to others but don't get linked back. High-priority pairs include:
   - `[[symbolic-regression]]` → `[[mcp-logic]]`
   - `[[self-correction]]` → `[[load-bearing-reasoning]]`, `[[agentic-research]]`, `[[metacognitive-architecture-closed-loop-self-regulation]]`, `[[chain-of-thought]]`, `[[process-reward-model]]`
   - `[[maximum-occupancy-principle]]` → `[[edm-framework]]`, `[[efhf]]`, `[[zettelkasten-engine]]`
   - `[[agem]]` → `[[efhf]]`

3. **Broken links (338):** Mix of:
   - Tag-list wikilinks (e.g., `[['news', 'geopolitics', ...]]`)
   - Non-existent concepts (ASEKE Framework, Word Cloud Communication, taylors-law, etc.)
   - Relative paths used in wikilinks (e.g., `[[wiki/sources/news/2026-05/...]]`)

4. **Insight generation timed out:** `generate_insights` call exceeded 300s. Zettelkasten engine may need optimization or conf threshold adjustment.

### Top Authorities Needing Deepening
- `[[efhf]]` (0.0467) — highest authority, also high hub
- `[[maximum-occupancy-principle]]` (0.0360)
- `[[project-synapse]]` (0.0326)
- `[[edm-framework]]` (0.0255)

### Top Hubs Needing Link Coverage
- `[[concept-index]]` (0.0586) — already comprehensive
- `[[carryover]]` (0.0242) — carryover pages should stay lean
- `[[causal-state-edm-ood-isomorphism]]` (0.0219)
- `[[mop-edm-cognitive-architecture]]` (0.0197)

### GAAC Clustering Notes
Massive cluster output (~817KB). Many intra-cluster missing links flagged — e.g., cluster 0 has `[[isabelle]]` with missing links to multiple unrelated pages, suggesting TF-IDF clustering is pulling heterogeneous pages together. Consider review of cluster quality.

### Open Items
- [ ] Triage 155 orphans: news pages may be expected-orphans (no inbound expected)
- [ ] Fix 110 non-reciprocal link pairs (some are intentional, need judgment)
- [ ] Resolve 338 broken links (many are clearly garbage: tag lists, non-concepts)
- [ ] Re-trigger insight generation with higher confidence threshold or lower timeout
- [ ] Verify concept-index.md currency (last updated 2026-04-28)
- [ ] tag-taxonomy.md missing — check if it lives elsewhere or was never created

### Next Cycle Priorities
1. Orphan triage (distinguish expected-orphans from real orphans)
2. Non-reciprocal repair (focus on high-authority pairs first)
3. Broken link bulk repair (strip tag-list wikilinks, create stubs for real concepts)