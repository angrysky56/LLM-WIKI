# Librarian Carryover

## Last Run
2026-06-09 (cron cycle)

## What Was Audited
- Full wiki lint (1509 pages, 1212 knowledge, 297 excluded)
- HITS authority/hub analysis (8 top each)
- GAAC clustering (33 clusters, 0 merge candidates)
- Frontmatter integrity check
- Orphan detection

## What Was Fixed
- 4 invalid frontmatter files (FIFTH pattern — unquoted colons in summaries):
  - drpo-divergence-regularized-policy-optimization.md
  - evaluation-cards-ai-evaluation-reporting.md
  - dcpm-dual-process-cognitive-memory-2026.md
  - observability-delegated-execution-agentic-2026.md
- All 4 had `summary:` values containing `:` (e.g. "DRPO: smooth advantage-weighted...") with no YAML quoting. Quoted with double quotes. Verified: invalid frontmatter dropped 6→2 (remaining 2 are raw/ false positives).

## Current Health
- Orphans: 246 (+15 from 231 — new ingestion)
- Broken links: 6552 (+114 from 6438 — new ingestion links to non-existent pages)
- Missing frontmatter: 0 — **clean**
- Invalid frontmatter: 2 — **raw/ false positives only** (wiki layer fully clean)
- Non-reciprocal: 584 (+33 from 551)
- Non-preferred tags: 0 — **clean**

## HITS Top-5
**Authorities:** wiki/index (0.0736), log (0.0555), concepts/maximum-occupancy-principle (0.0142), entities/projects/efhf (0.0057), concept-index (0.0053)
**New:** agentic-research (0.0035) entered top-8 authorities
**Hubs:** maximum-occupancy-principle (0.0031 bare-slug alias), efhf (0.0026 bare-slug alias), concept-index (0.0022), load-bearing-reasoning (0.0021), project-synapse (0.0020)
**New hubs:** reward-modeling, chain-of-thought, mixture-of-experts at 0.0020
No lint-report artifact in hub top. MOP phantom alias persists (documented limitation).

## GAAC
- 33 clusters (reconfigured from 15 — new pages shifted boundaries)
- 0 merge candidates (business↔innovation single-cycle artifact did NOT reappear — confirmed as transient)
- Cluster sizes range from 1 (Cluster 23: modelfile-reference) to 222 (Cluster 1)

## What Remains
- 246 orphans are genuine knowledge pages — expected to normalize over 1-2 cycles
- 6552 broken links are mostly operational path refs — not actionable
- No merge candidates to flag
- No tag taxonomy violations

## CarryoverState

### Established
- Frontmatter is effectively clean (0 wiki-layer invalid, 2 raw/ false positives)
- FIFTH pattern (unquoted colons in ingestor-created summaries) recurred — ingestor still writing unquoted summaries with colons
- 4 new paper source pages created since yesterday's audit
- GAAC reconfigured from 15→33 clusters; business↔innovation pair confirmed as transient

### Open
- **[Recurring]** Unquoted colons in ingestor summaries keep reappearing — 4 new instances this cycle. Flag for ingestor fix.
- **[Stable]** Vault health stable — no regression beyond expected ingestion growth
- MOP phantom alias still present (bare-slug vs prefixed from 50+ external links)

### Heading
- **[Monitor]** Watch for recurrence of FIFTH pattern on next cycle
- **[No delegation needed]** All actionable items fixed directly