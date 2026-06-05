---
summary: "Librarian carryover 2026-06-05 cycle 9 — REMEDIATION cycle. 1423 pages (1141 knowledge), 209/6263/0/0/528/0. Fixed 2 invalid-frontmatter pages (EIGHTH pattern — ingestor-stub first block). HITS top-5 authority stable. Vault health 9/10."
tags: [librarian, carryover, wiki-audit, daily, 2026-06-05, cycle-9, remediation]
updated: 2026-06-05T14:35:00Z
---

# Librarian Carryover — 2026-06-05 (Cycle 9, 14:35 UTC)

## Kanban Status
- [x] Audit complete: 2026-06-05 14:35 UTC
- [x] wiki_lint, wiki_hits_analysis, wiki_cluster_pages all ran
- [x] wiki_update_index: ran (1141 pages indexed)
- [x] **Invalid frontmatter: 2 → 0** — EIGHTH pattern (ingestor-stub) on two new paper sources. Deleted broken prefixed first `---` block.
  - `sources/papers/deltadirect-directional-motion-blindness-video-llms-2026.md`
  - `sources/papers/ai-chatbots-news-intermediaries-2026.md`
- [x] Re-lint confirmed both counts dropped to 0 (missing: 2→0, invalid: 2→0 after second pass for blank-line artifact)
- [x] On-disk lint report (`wiki/audits/lint-2026-06-05.md`) 14:32 UTC: Orphans:209, Broken:6263, Missing:0, Invalid:0, Non-reciprocal:528, Tags:0 — **matches MCP return ✓**

## Established

### Vault Stats — Cycle 9 (2026-06-05 14:32 UTC, 1423 pages = 1141 knowledge + 282 operational excluded)

| Metric | Cycle 8 (05:40) | Cycle 9 (14:32) | Delta |
|--------|---------|---------|-------|
| Orphans | 216 | 209 | -7 (normal — some got linked) |
| Broken | 6214 | 6263 | +49 (from 8 new pages) |
| Missing | 1 (raw/false positive) | 0 | -1 |
| Invalid | 0 | 0 | ✓ stable (was 2, fixed → 0) |
| Non-reciprocal | 474 | 528 | +54 (new pages, body-text false positives) |
| Tags | 0 | 0 | ✓ stable |

**Vault growth:** +14 pages since cycle 8 (1409→1423). +8 knowledge pages (1133→1141). Growth consistent with afternoon ingestion.

**Missing frontmatter: 0** — the 2 new files after EIGHTH-pattern fix had trailing blank-line artifact (lines 1-2 blank, `---` started at line 3). Fixed via full-content rewrite. After re-lint: 0 missing, 0 invalid.

### HITS Authority Top 5
| Rank | Page | Score | Delta vs Cycle 8 |
|------|------|-------|-------|
| 1 | `wiki/index` | 0.0734 | ✓ stable |
| 2 | `log` | 0.0554 | ✓ stable |
| 3 | `concepts/maximum-occupancy-principle` | 0.0142 | ✓ stable |
| 4 | `entities/projects/efhf` | 0.0058 | +0.0005 (noise) |
| 5 | `concept-index` | 0.0052 | +0.0001 (noise) |

**Stable — 9th cycle in a row.** Graph topology frozen. No authority page has changed content depth this cycle.

### HITS Hub Top 5
| Rank | Page | Score | Delta |
|------|------|-------|-------|
| 1 | `maximum-occupancy-principle` (bare-slug alias) | 0.0031 | ✓ stable |
| 2 | `efhf` | 0.0026 | ✓ stable |
| 3 | `concept-index` | 0.0022 | ✓ stable |
| 4 | `load-bearing-reasoning` | 0.0021 | ✓ stable |
| 5 | `project-synapse` | 0.0020 | *new* (was `chain-of-thought`) |

**`project-synapse` replaced `chain-of-thought` in hub top-5** — both at 0.0020, this is a rounding-level tie. Not meaningful.

**No audit-cycle artifact** in top-hub (no `lint-*` page).

### Tag Taxonomy
- 0 non-preferred tags — controlled vocabulary compliant
- No tag violations detected

### GAAC Cluster Findings
- **Merge candidates:** All 1.000 similarity pairs — stub false positives (same set as prior cycles: `fts5↔compound-commands`, `random-forest↔tabpfn-client`/`tabpfn-extensions`, `micro-saas↔programmatic-seo`, `sledgehammer↔java`/`latex`, `printing-press↔peter-steinberger`, `israel↔lebanon`). Not actionable.
- **`business ↔ innovation`** — not in this cycle's merge candidates (confirmed resolved as single-cycle artifact from prior runs).
- **No new merge candidates** with similarity between 0.7 and 1.0 seen in output.

### Orphan Status
- 209 orphans (down from 216 — 7 got linked naturally since cycle 8)
- First 10 unchanged: `mop-agents-integration`, `oMCD-calibration-protocol`, `skill-vectors`, `quality-diversity`, `open-endedness`, `synthetic-task-generation`, `astar-structural-pathfinding`, `coevolution`, `coverage-metric`, `alqr-memory-estimates`
- **`mop-agents-integration`** — still orphan after 2+ days (originated 2026-06-03). Linked from `index.md` which covers discovery. Recommend Ty decide whether to add knowledge-layer incoming links or let index.md coverage suffice.
- Fresh ingestion orphans (skill-vectors, quality-diversity, open-endedness, synthetic-task-generation) from 2026-06-04 — normal 1-2 cycle absorption expected.

## What Remains

### High Priority
- [ ] **Ingestor stub-block recurrence confirmed** — the prior cycle (08:40) noted "No new instances in this cycle's 4 new pages" and suggested it may be fixed. At 14:27, 2 new paper sources appeared with the same EIGHTH pattern `--- ... --- / blank / --- ... ---` structure (broken first block with unquoted `summary:` containing colon/em-dash, complete second block). **This confirms the ingestor is still producing the defect.** The 05:40 batch of 4 pages was clean; the 14:22-14:23 batch had the defect. This may depend on the ingestion path or specific paper type. **Surface for Ty** — the ingestor root cause needs fixing at source.

### Medium Priority
- [ ] **855 broken `[[wiki/index]]` refs** — long-standing false positive from strict-path-match linter. Stable.
- [ ] **528 non-reciprocal links** — body-text-only false positive per skill pitfall. Up from 474 (+54 from new pages).
- [ ] **MOP phantom HITS nodes** — 9th cycle confirmed. Known limitation documented in skill.

### Low Priority
- [ ] **209 orphans** — mostly fresh ingestion artifacts. `mop-agents-integration` (2+ days orphan) warrants attention.
- [ ] **6263 broken links** — 855x `[[wiki/index]]` false positive dominates.
- [ ] **GAAC merge candidates** — all stub false positives, same set as prior cycles.

## Flagged for Ty
- **Ingestor stub-block recurrence at 14:22-14:23 UTC** — contradicts prior cycle's hypothesis that it was fixed. The ingestor produced the defect on 2 new paper sources despite 4 clean ones in the morning batch.
- **`mop-agents-integration`** — 2+ days orphaned. Linked from `index.md` but no knowledge-layer incoming links. Recommend Ty decide whether to add links or accept index.md coverage.
- **Vault health: 9/10** — stable across all metrics after remediation.
- **HITS top-5 authority unchanged for 9 cycles** — graph topology essentially frozen.

## Heading
- Vault health: **9/10** (unchanged — stable after minor remediation)
- **Action this cycle:** Fixed 2 invalid-frontmatter files (EIGHTH pattern). No other remediation needed.
- **Key finding:** Ingestor stub-block defect is still active — just confirmed with fresh instances at 14:22-14:23 UTC.
- **Next cycle focus:** Check for new ingestor stub-block instances. Verify `mop-agents-integration` orphan status (3+ days at next cycle).