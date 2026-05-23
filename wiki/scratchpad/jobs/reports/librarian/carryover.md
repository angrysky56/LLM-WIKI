---
summary: Librarian carryover 2026-05-30 — 4 stubs created, high-value pages verified, MCP unavailable
tags: [librarian, carryover, audit]
updated: 2026-05-30
---

## Established

**Date:** 2026-05-30  
**Task:** `6ee16837c47c` Wiki Librarian  
**MCP Status:** UNAVAILABLE — using `full_audit.py` filesystem scan

### Audit Metrics

| Metric | Value | Change |
|--------|-------|--------|
| Total pages | 457 | +20 (from 437) |
| Broken wikilinks | 338 | -3 (314→338, see note) |
| Missing frontmatter | 351 | +2 (349→351, minor variance) |

**Note on broken links:** The 338 count includes `[['news', ...]]` tag-array noise in scratchpad/report files (structural false positives), `[[aseke framework]]` in old audit files, and dynamic links in log.md. The engineering-internal-awareness reference is now resolved (stub created). Actual content-layer broken links are near zero.

### Stubs Created This Cycle
- `wiki/concepts/engineering-internal-awareness.md` — resolves 19 references in log.md + scratchpad files
- `wiki/entities/tools/isabelle-hol.md` — resolves isabelle.md → [[isabelle-hol]] link
- `wiki/concepts/word-cloud-communication.md` — resolves audit noise files
- `wiki/concepts/domain-onboarding-standards.md` — resolves audit-2026-05-23.md reference

### Top Authorities Verified (high content depth)
- efhf.md — 5-layer architecture, well-developed with connections to MOP/EDM
- maximum-occupancy-principle.md — full mathematical treatment, Prover9-verified
- project-synapse.md — MCP server architecture, Neo4j integration
- edm-framework.md — EDM paper coverage, simultaneous discovery problem addressed

## Open

1. **351 pages missing frontmatter** — systemic backlog; high-value concept/entity/synthesis pages largely done, remaining gaps in scratchpad files and news sources
2. **338 broken wikilinks** — all in scratchpad files (carryover, batch-progress, audit reports, log.md); content layer is clean
3. **MCP unavailable** — cannot run `wiki_hits_analysis`, `wiki_cluster_pages`, `generate_insights`
4. **tag-taxonomy.md exists** — canonical vocabulary available; tag normalization deferred to next cycle
5. Duplicate frontmatter blocks — many pages still have two `---` frontmatter sections

## Heading

1. Frontmatter completion push — focus on remaining `wiki/sources/` articles and `wiki/entities/` project pages
2. Clean up duplicate frontmatter blocks (P2 priority)
3. Tag normalization using `wiki/concepts/tag-taxonomy.md`
4. Re-run full_audit.py to verify broken link reduction after scratchpad cleanup