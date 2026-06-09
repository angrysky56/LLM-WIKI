---
created: 2026-06-09
updated: 2026-06-09
type: carryover
summary: "Librarian carryover — 2026-06-09: Frontmatter clean, 4 FIFTH-pattern fixes, vault stable"
tags: [librarian, carryover]
---

# Librarian Carryover — 2026-06-09

## What Was Done
- Full wiki lint (1509 pages, 1212 knowledge, 297 excluded)
- HITS authority/hub analysis (8 top each)
- GAAC clustering (33 clusters, 0 merge candidates)
- Frontmatter integrity check
- Orphan detection
- Fixed 4 invalid frontmatter files (FIFTH pattern — unquoted colons in summaries):
  - drpo-divergence-regularized-policy-optimization.md
  - evaluation-cards-ai-evaluation-reporting.md
  - dcpm-dual-process-cognitive-memory-2026.md
  - observability-delegated-execution-agentic-2026.md
- All 4 had `summary:` values containing `:` with no YAML quoting. Quoted with double quotes.

## What Remains
- [ ] Unquoted colons in ingestor summaries keep reappearing — 4 new instances this cycle. Flag for ingestor fix.
- [ ] 246 orphans are genuine knowledge pages — expected to normalize over 1-2 cycles
- [ ] 6552 broken links are mostly operational path refs — not actionable
- [ ] MOP phantom alias still present (bare-slug vs prefixed from 50+ external links)

## Heading
- **[Monitor]** Watch for recurrence of FIFTH pattern on next cycle
- **[No delegation needed]** All actionable items fixed directly

## Current Health
- Orphans: 246 (+15 from 231 — new ingestion)
- Broken links: 6552 (+114 from 6438 — new ingestion)
- Missing frontmatter: 0 — clean
- Invalid frontmatter: 2 — raw/ false positives only (wiki layer fully clean)
- Non-reciprocal: 584 (+33 from 551)
- Non-preferred tags: 0 — clean

## HITS Top-5
**Authorities:** wiki/index (0.0736), log (0.0555), concepts/maximum-occupancy-principle (0.0142), entities/projects/efhf (0.0057), concept-index (0.0053)
**Hubs:** maximum-occupancy-principle (0.0031 bare-slug alias), efhf (0.0026 bare-slug alias), concept-index (0.0022), load-bearing-reasoning (0.0021), project-synapse (0.0020)
