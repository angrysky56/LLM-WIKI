# Librarian Carryover

## Last Run
2026-06-08 (cron cycle)

## What Was Audited
- Full wiki lint (1478 pages, 1184 knowledge)
- HITS authority/hub analysis (8 top each)
- GAAC clustering (15 clusters)
- Frontmatter integrity check
- Orphan detection

## What Was Fixed
- **8 invalid frontmatter files → 0**: Fixed 4× EIGHTH-pattern (ingestor-stub on instruction-tuning.md, flashattention-2022.md, proxy-based-approximation-of-shapley-and-banzhaf-interaction.md, insights-2026-06-06-batch.md), 1× missing opener (instruction-tuning.md was left without `---` after stub deletion), 1× missing frontmatter (insights-batch.md lacked any frontmatter after stub removal — added minimal type:synthesis frontmatter). 2 news files and 2 representation-reading synthesis pages were already single-block clean (the linter had transient false positives on them that resolved after the fixes triggered a full re-lint).

## Current Health
- Orphans: 231 (+8 from 223 last cycle — new ingestion)
- Broken links: 6438 (+86 from 6352 — new ingestion links to non-existent pages)
- Missing frontmatter: 0 — **clean**
- Invalid frontmatter: 0 — **clean**
- Non-reciprocal: 551 (+2)
- Non-preferred tags: 0 — **clean**

## HITS Top-5
**Authorities:** wiki/index (0.0734), log (0.0553), concepts/maximum-occupancy-principle (0.0142), entities/projects/efhf (0.0057), concept-index (0.0053)
**Hubs:** maximum-occupancy-principle (0.0031 bare-slug alias), efhf (0.0026 bare-slug alias), concept-index (0.0022), load-bearing-reasoning (0.0022), project-synapse (0.0020)

No lint-report artifact in hub top — clean. MOP phantom alias persists (bare vs prefixed slug from 50+ external links) — documented limitation.

## GAAC
- **Merge candidates (1.000):** Many stub-page false positives (fts5↔compound-commands, random-forest↔tabpfn-extensions, business↔innovation↔entrepreneurship, sledgehammer↔java↔latex, micro-saas↔programmatic-seo). None actionable — stub patterns score 1.0 from identical minimal structure. `business↔innovation` is the documented transient artifact.
- **Missing links (genuine):** normalizing-flows↔energy-based-models, normalizing-flows↔generative-adversarial-networks, spiral-architecture↔refuser-pattern, wolfram-nks-causal-networks↔computational-irreducibility, wolfram-nks-causal-networks↔causal-reasoning. All in same-cluster pairs without wikilinks.

## What Remains
- 231 orphans are genuine knowledge pages (newly-ingested) — expected to normalize over 1-2 ingestion cycles
- 6438 broken links are mostly operational path refs in body text — not actionable
- `business↔innovation` merge candidate appeared in one cycle only — do not remediate until confirmed in next cycle
- No tag taxonomy violations found
- No classification disputes flagged

## CarryoverState

### Established
- Frontmatter is fully clean (0 invalid, 0 missing) — a first for this vault
- EIGHTH-pattern fix workflow validated: delete stub lines, then add `---` opener if missing, then verify with wiki_lint
- insights-batch.md needs proper frontmatter (added minimal; leaving better summary/tags for Ty review)

### Open
- **[Risk]** ingestor is still producing EIGHTH-pattern duplicates on freshly-ingested pages — stub is written, then the same ingestor writes a second complete block without deleting the first. This is a recurring defect. Flagged for ingestor remediation.
- **[Stable]** vault health is good — stable no-regression from prior cycle

### Heading
- **[Intent]** Monitor orphan count — if it doesn't self-resolve in 1-2 cycles, bulk-linking needed
- **[Constraint]** No structural work this cycle beyond frontmatter remediation