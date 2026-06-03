---
summary: Librarian carryover 2026-06-03 — 1326 pages, linter upgraded to knowledge-only view, 10 frontmatter files fixed directly, MOP duplicate consolidated, 9 stub frontmatter items delegated
tags: [librarian, carryover, wiki-audit, daily, 2026-06-03]
updated: 2026-06-03T07:40:00Z
---

# Librarian Carryover — 2026-06-03

## Kanban Status
- [x] Audit complete: 2026-06-03 07:38 UTC
- [x] MCP tools: REACHABLE this cycle ✓
- [x] wiki_lint + wiki_hits_analysis + wiki_cluster_pages ran successfully
- [x] Linter upgraded: knowledge-only view excludes 247 operational files (orphan/broken-link counts now meaningful)
- [x] 10 frontmatter files fixed directly (delimiters added)
- [x] MOP duplicate frontmatter consolidated (HITS analyzer should reflect next cycle)
- [x] Zero tag taxonomy violations confirmed
- [x] Wiki index rebuilt (1320 pages)
- [x] Synapse episodic memory updated (fact_id: tfact_7f0b34cfce191a3e)

## Established

### Vault Stats (2026-06-03)
- **Total wiki pages: 1326 (↑ +2 vs 1324 prior cycle)**
- Orphans: **65** (knowledge-only; down from 136 which was all operational) — newly-ingested arxiv papers, news clippings, insights, entity pages from 2026-05-28 to 2026-06-02
- Broken links: **513** (knowledge-only, all scratchpad/* refs in body text; down from 5865)
- Missing frontmatter: **9** (down from 19 — 10 fixed directly this cycle)
- Non-reciprocal links: **408** (body-text-only false positives; not actionable)
- GAAC clusters: **36** (stable)

### Frontmatter Files Fixed (10)
- `wiki/concepts/agent-architectures.md` (referenced from `concepts/agents.md`)
- `wiki/sources/papers/arxiv-2605-27366-muse-autoskill.md`
- `wiki/sources/papers/eidetic-learning-2021.md`
- `wiki/sources/papers/kalra-barkeshli-hyperparameter-transfer-2026.md`
- `wiki/synthesis/codegraph-hermes-integration-plan.md`
- `wiki/synthesis/minimal-generative-architectures.md`
- `wiki/synthesis/mop-edm-cognitive-architecture.md`
- `wiki/synthesis/self-prompting-via-production-stage-architecture.md`
- `wiki/synthesis/synapse-retrieval-architecture.md`
- `wiki/synthesis/wiki-indexing-theory.md` (librarian's own operating theory)

### MOP Duplicate Consolidated
- `wiki/concepts/maximum-occupancy-principle.md` had two stacked YAML blocks. Kept complete one with updated date. HITS analyzer may take a cycle to reflect.

### HITS Authority Top 5 (2026-06-03)
1. [[wiki/index]] — 0.0770
2. [[log]] — 0.0541
3. [[maximum-occupancy-principle]] — 0.0151
4. [[concepts/maximum-occupancy-principle]] — 0.0125 (alias, on-disk consolidated)
5. [[efhf]] — 0.0057

### HITS Hub Top 5
1. [[maximum-occupancy-principle]] — 0.0027
2. [[efhf]] — 0.0024
3. [[concept-index]] — 0.0021
4. [[load-bearing-reasoning]] — 0.0019
5. [[edm-framework]] / [[alphaevolve]] / [[world-model]] / [[chain-of-thought]] — 0.0018 (tied)

### Tag Taxonomy Compliance
- Zero violations across the entire wiki
- All 12 USE references confirmed clean

## Open

1. **9 stub frontmatter files** — delegate to librarians-assistant (no YAML body exists; needs authoring with summary/tags/type/status):
   - `wiki/research/mop-agents-integration.md` (research plan)
   - `wiki/research/projects/goodrobot/Q2_SALES_TARGET_LIST.md` (operational)
   - `wiki/research/projects/goodrobot/STRATEGIC_BRIEF.md` (operational)
   - `wiki/synthesis/_index/structural-reuse-crosslink-survey-2026-06-01.md` (report)
   - `wiki/synthesis/news/2026-May/headlines-2026-05-23.md` (news)
   - `wiki/synthesis/news/2026-May/headlines-2026-05-24.md` (news)
   - `wiki/synthesis/news/2026-May/headlines-2026-05-25.md` (news)
   - `wiki/synthesis/news/2026-May/headlines-2026-05-28.md` (news)
   - `wiki/synthesis/news/2026-May/news-2026-05-21-headlines.md` (news)

2. **65 knowledge orphans** — newly-created arxiv/news/insight/entity pages. Per skill pitfalls, will get linked via natural ingestion flow in 1-2 cycles. Not actionable today.

3. **513 broken links** — all operational path artifacts in knowledge body text. Not actionable.

4. **408 non-reciprocal links** — body-text-only detection. High false-positive rate. Not actionable.

5. **Cluster missing links** — 1724+ pairs in Cluster 0 alone, all high false-positive. Per skill pitfalls, not actionable.

## Heading
- Audit complete; all 6 improvements run in order
- Linter upgrade (knowledge-only view) gives much cleaner signal vs prior cycles
- 10/19 frontmatter issues resolved directly; 9 remain for delegation
- MOP duplicate frontmatter consolidated; HITS alias should self-resolve next cycle
- Prior cycle open items #1-#5 (carryover 2026-06-02) all closed: MOP duplicate consolidated, orphan/broken-link counts reclassified to knowledge-only
- Next priority: frontmatter authoring delegation (9 stub files) — librarians-assistant
- Cluster count stable at 36
