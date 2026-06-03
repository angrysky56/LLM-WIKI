---
summary: Librarian carryover 2026-06-03 cycle 2 — vault stable at 1337 pages, 0 tag violations, 9 missing-frontmatter files still require delegation, MOP consolidation held
tags: [librarian, carryover, wiki-audit, daily, 2026-06-03]
updated: 2026-06-03T09:50:00Z
---

# Librarian Carryover — 2026-06-03 (Cycle 2)

## Kanban Status
- [x] Audit complete: 2026-06-03 09:50 UTC
- [x] MCP tools: REACHABLE ✓
- [x] wiki_lint + wiki_hits_analysis + wiki_cluster_pages ran successfully
- [x] Vault state stable vs prior cycle — no new issues, no regressions
- [x] 0 non-preferred tag violations confirmed (12 USE references clean)
- [x] MOP duplicate-frontmatter fix held (single YAML block)
- [x] Prior 10 frontmatter delimiter fixes all held
- [x] Synapse episodic memory updated

## Established

### Vault Stats (2026-06-03 09:50 UTC)
- **Total wiki pages: 1337** (1079 knowledge, 258 operational excluded)
- Orphans: **65** (stable, all knowledge nodes from 2026-05-28 to 2026-06-02 ingestion)
- Broken links: **513** (all `scratchpad/*` operational refs — non-actionable per skill)
- Missing frontmatter: **9** (same as last cycle — need content authoring, not linter fix)
- Non-reciprocal: **408** (body-text-only, high false-positive)
- Non-preferred tags: **0** ✅
- GAAC clusters: **36** (stable)

### HITS Authority Top 5 (stable)
1. [[wiki/index]] — 0.0659
2. [[log]] — 0.0464
3. [[maximum-occupancy-principle]] — 0.0135
4. [[concepts/maximum-occupancy-principle]] — 0.0109 (alias)
5. [[efhf]] — 0.0055

### HITS Hub Top 5
1. [[lint-2026-06-03]] — 0.0038 (audit hub)
2. [[maximum-occupancy-principle]] — 0.0028
3. [[efhf]] — 0.0025
4. [[concept-index]] — 0.0022
5. [[load-bearing-reasoning]] — 0.0019

## What Remains

- [ ] **9 missing-frontmatter files** — delegate to librarians-assistant for YAML authoring:
  - `wiki/research/mop-agents-integration.md` (research plan)
  - `wiki/research/projects/goodrobot/Q2_SALES_TARGET_LIST.md` (operational)
  - `wiki/research/projects/goodrobot/STRATEGIC_BRIEF.md` (operational)
  - `wiki/synthesis/_index/structural-reuse-crosslink-survey-2026-06-01.md` (report)
  - `wiki/synthesis/news/2026-May/headlines-2026-05-23.md` (news)
  - `wiki/synthesis/news/2026-May/headlines-2026-05-24.md` (news)
  - `wiki/synthesis/news/2026-May/headlines-2026-05-25.md` (news)
  - `wiki/synthesis/news/2026-May/headlines-2026-05-28.md` (news)
  - `wiki/synthesis/news/2026-May/news-2026-05-21-headlines.md` (news)

- [ ] **65 knowledge orphans** — re-verify next cycle (self-resolve via ingestion flow)

- [ ] **GAAC Cluster 0 deep-dive** — extract genuine knowledge-page pairs needing links (skip all-cluster inflated false positives)

## Flagged for Ty
- News headlines frontmatter policy (5 of 9 missing-frontmatter files)
- goodrobot/ operational files in research/ — should linter exclude?

## Heading
- Vault health: **8.5/10** (stable, no actions required)
- Audit report: `wiki/scratchpad/jobs/reports/librarian/audit-2026-06-03.md`
- Next cycle: re-verify orphan count self-resolved; re-evaluate missing-frontmatter after delegation
- HITS authority top-3 stable 2 cycles running — vault graph topology is healthy
- Cluster 0 (reasoning/cognitive) is the only cluster worth genuine remediation focus
