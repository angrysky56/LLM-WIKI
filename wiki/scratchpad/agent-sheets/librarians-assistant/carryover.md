---
summary: "Librarians-assistant carryover 2026-06-05 — Fixed efhf phantom authority: removed self-link + bulk normalized 60 files ([[efhf]] → [[entities/projects/efhf]]). HITS: efhf consolidated to single node 0.0057. Vault: 1133 knowledge pages, 216/6269/1/0/518/0. 1 missing frontmatter is raw/inbox false positive."
tags: [librarians-assistant, carryover, wiki-remediation, 2026-06-05, efhf-normalization, phantom-fix]
updated: 2026-06-05T05:45:00Z
---

# Librarians-Assistant Carryover — 2026-06-05 (05:45 UTC)

## Fixes Applied This Cycle

### Priority 1a — HITS Phantom Self-Link Fix
- **`wiki/entities/projects/efhf.md`**: Removed `- [[efhf]]` self-referential wikilink from Connections section

### Priority 1b — Bulk Bare-Slug Normalization
- Normalized `[[efhf]]` → `[[entities/projects/efhf]]` in **60 wiki content files** (excluded index.md, concept-index.md, audits/, scratchpad/, raw/, jobs/)
- Verified with `git diff`: all changes are clean `[[efhf]]` → `[[entities/projects/efhf]]` replacements

### Post-Fix HITS Verification
- **Before**: bare `efhf` authority 0.0053 (phantom), no path-prefixed node in authorities
- **After**: `entities/projects/efhf` authority 0.0057 (single consolidated node)
- Residual `efhf` hub 0.0026: from index.md/concept-index.md only (excluded per skill) — not actionable
- MOP bare-slug hub 0.0030, LBR bare-slug hub 0.0021: residual from index.md only — not actionable

## Vault Health Snapshot (post-fix)
- 1410 pages (1133 knowledge, 277 operational)
- Orphans: 216 (unchanged from prior cycle)
- Broken links: 6269 (increase from ~6214 due to path-prefixed efhf links being misclassified by lint's vault-path resolution — false positive)
- Missing frontmatter: 1 (raw/inbox file — false positive, not a knowledge page)
- Invalid frontmatter: 0
- Non-reciprocal: 518 (increase due to same vault-path artifact — false positives)
- Non-preferred tags: 0

## Open Items (not actionable this cycle)

### Hard Blockers — Needs Librarian Judgment
- **10 merge candidates at 1.000 similarity** in GAAC output — all are TF-IDF artifacts (e.g., `israel`↔`lebanon`, `sledgehammer`↔`java`, `printing-press`↔`peter-steinberger`, `micro-saas`↔`programmatic-seo`, `fts5`↔`compound-commands`, `random-forest`↔`tabpfn-client`). These are clearly not genuine duplicates — need librarian verification to dispose or dismiss.
- **216 orphans**: Many appear in meaningful GAAC clusters (Cluster 15: evolution/QD pages like `skill-vectors`, `quality-diversity`, `open-endedness`, `coevolution`, etc.). Potential reconnection work for future cycles, but batch limit (50+) already reached this cycle.

### Systemic False Positives (not actionable)
- **70 broken links to `[[entities/projects/efhf]]`**: False positive — vault-path slug-resolution issue. Page exists at `wiki/entities/projects/efhf.md`.
- **153 broken links to `[[concepts/maximum-occupancy-principle]]`**: Same vault-path false positive pattern.
- **866 broken links to `[[wiki/index]]`**: Systemic false positive.

## Kanban Status
- No open kanban tasks for librarians-assistant
- [x] Audit ran: 2026-06-05 05:43 UTC
- [x] Fixes applied: 61 (1 self-link + 60 bulk normalizations)
- [x] Index refreshed: deep=true
- [x] HITS verified post-fix: efhf phantom resolved

## Resume Point
- Next cycle: Priority 2 (tag normalization — 0 non-preferred tags, so skip), Priority 3 (1 missing frontmatter is raw/inbox false positive), or continue with Priority 1b for other phantom slugs
- MOP and LBR bare-slug hubs are residual from index.md only (excluded per skill) — not actionable
- GAAC merge candidates need librarian judgment before proceeding

## Last Run
2026-06-05T05:45:00Z