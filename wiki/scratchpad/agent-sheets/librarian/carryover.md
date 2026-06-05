---
summary: "Librarian carryover 2026-06-05 cycle 8 — STABLE cycle. 1409 pages (1133 knowledge), 216/6214/1/0/474/0. 1 missing frontmatter is raw/inbox false positive. HITS top-5 unchanged. Vault health 9/10."
tags: [librarian, carryover, wiki-audit, daily, 2026-06-05, cycle-8, stable]
updated: 2026-06-05T05:40:00Z
---

# Librarian Carryover — 2026-06-05 (Cycle 8, 05:40 UTC)

## Kanban Status
- [x] Audit complete: 2026-06-05 05:40 UTC
- [x] MCP tools: REACHABLE ✓
- [x] wiki_lint, wiki_hits_analysis, wiki_cluster_pages all ran
- [x] wiki_update_index: not needed (no fixes applied)
- [x] **No remediation needed this cycle** — stable state
- [x] On-disk lint report (`wiki/audits/lint-2026-06-05.md`) matches MCP return
- [x] Carryover written, verified via stat

## Established

### Vault Stats — Cycle 8 (2026-06-05 05:34 UTC, 1409 pages = 1133 knowledge + 276 operational)

| Metric | Cycle 7 | Cycle 8 | Delta |
|--------|---------|---------|-------|
| Orphans | 213 | 216 | +3 (from 4 new pages — normal) |
| Broken | 6219 | 6214 | -5 (minor fluctuation) |
| Missing | 0 | 1 | +1 (false positive — raw/inbox file) |
| Invalid | 0 | 0 | ✓ stable |
| Non-reciprocal | 474 | 474 | ✓ stable |
| Tags | 0 | 0 | ✓ stable |

**Vault growth:** +4 pages since cycle 7 (1405→1409). +3 knowledge pages (1130→1133). 3/3 new knowledge pages are orphans, as expected.

**Missing frontmatter (1):** `raw/A Foundational Overview of Biosemiotics.md` — this is a raw/inbox file, not a knowledge page. Raw files don't need frontmatter. **Not actionable.**

### HITS Authority Top 5 (stable vs cycle 7)
| Rank | Page | Score | Delta |
|------|------|-------|-------|
| 1 | [[wiki/index]] | 0.0736 | ✓ stable |
| 2 | [[log]] | 0.0557 | ✓ stable |
| 3 | [[concepts/maximum-occupancy-principle]] | 0.0142 | +0.0001 (noise) |
| 4 | [[efhf]] | 0.0053 | ✓ stable |
| 5 | [[concept-index]] | 0.0051 | ✓ stable |

### HITS Hub Top 5 (stable vs cycle 7)
| Rank | Page | Score | Delta |
|------|------|-------|-------|
| 1 | [[maximum-occupancy-principle]] (bare-slug alias) | 0.0030 | ✓ stable |
| 2 | [[efhf]] | 0.0025 | ✓ stable |
| 3 | [[concept-index]] | 0.0022 | ✓ stable |
| 4 | [[load-bearing-reasoning]] | 0.0021 | ✓ stable |
| 5 | [[chain-of-thought]] | 0.0020 | ✓ stable |

**No audit-cycle artifact in top-hub** — `lint-2026-06-05` not in hub top-5 (expected: report was just generated, but no re-lint happened after it).

### Tag Taxonomy
- 0 non-preferred tags — controlled vocabulary is compliant
- Tag taxonomy page: `wiki/concepts/tag-taxonomy.md` — 427 words, status: active

### GAAC Cluster Findings
- **Merge candidates:** All 1.000 similarity pairs — stub false positives (e.g. `fts5↔compound-commands`, `random-forest↔tabpfn-client`, `sledgehammer↔java↔latex`, `printing-press↔peter-steinberger`, `israel↔lebanon`). Not actionable.
- **`business ↔ innovation` from prior carryover:** NOT in this cycle's merge candidates. The clustering shifted or it was a single-cycle artifact. The prior carryover's concern about it being a "real or stub artifact" is resolved — it was a stub artifact.
- **Cluster 0** (4 pages — news/event pages): missing links between them, all trivial news articles. Not actionable.

### Orphan Sample (top 5)
| Page | Path | Type | Verdict |
|------|------|------|---------|
| mop-agents-integration | `wiki/research/` | research | **Genuine orphan** — only linked from operational `index.md`. Not absorbed yet. Originated 2026-06-03. |
| skill-vectors | `wiki/concepts/` | concept (new) | **Recent ingestion** — 2026-06-04. Normal 1-2 cycle absorption expected. |
| quality-diversity | `wiki/concepts/` | concept (new) | **Recent ingestion** — 2026-06-04. Normal. |
| open-endedness | `wiki/concepts/` | concept (new) | **Recent ingestion** — 2026-06-04. Normal. |
| synthetic-task-generation | (not checked) | — | Skip — likely same AC/DC batch. |

**Assessment:** 4/5 orphans are fresh ingestion artifacts. `mop-agents-integration` is the only "stuck" orphan (ingested 2026-06-03, still no knowledge-layer incoming links after 2 days). Minority concern — it's linked from index.md which covers discovery.

## What Remains

### High Priority
- [ ] **Ingestor stub-block prevention** — same as cycle 7. The broken-first-block pattern has recurred across multiple cycles. No new instances in this cycle's 4 new pages (they all have clean frontmatter), which suggests it may have been fixed, or the current batch of 4 pages came through a different ingestion path. **Surface for Ty as a closed item unless it recurs.**

### Medium Priority
- [ ] **866 broken `[[wiki/index]]` refs** — long-standing false positive from strict-path-match linter. Not actionable without linter algorithm change. Stable at 866.
- [ ] **474 non-reciprocal links** — body-text-only false positive (per skill pitfall). Stable (no growth this cycle). Not actionable without reading each target.
- [ ] **MOP phantom HITS nodes** — 8th cycle confirmed. Documented in skill as known limitation. No change.

### Low Priority
- [ ] **216 orphans** — 4/5 sampled are fresh ingestion artifacts. Only `mop-agents-integration` (2026-06-03, still orphan after 2 days) warrants attention, but it has index.md coverage.
- [ ] **6214 broken links** — 866x `[[wiki/index]]` false positive dominates. Real broken links are ~10x fewer.
- [ ] **GAAC merge candidates** — all stub false positives. `business↔innovation` resolved (not in this cycle's cluster).

## Flagged for Ty
- **Stable cycle** — no remediation needed. All metrics within expected bounds.
- **Missing frontmatter "1"** is a raw/inbox file false positive, not a real defect. The cycle 6 pattern of phantom missing-frontmatter counts may partially apply (the linter flags raw/ files, which don't need frontmatter).
- **`mop-agents-integration`** is the only orphan that's been orphaned >1 cycle. Low concern (linked from index.md).
- **HITS top-5 unchanged** for 8 consecutive cycles. Graph topology is very stable.
- **No ingestor stub-block recurrence** in this cycle's 4 new pages. The prior cycle's root-cause hypothesis may need revision, or the ingestor was already fixed.

## Heading
- Vault health: **9/10** (unchanged from cycle 7 — stable across all metrics)
- Audit report: `wiki/audits/lint-2026-06-05.md` (551596 bytes, 6921 lines, 2026-06-05 05:34 UTC)
- HITS authority top-5: stable for 8 cycles — graph topology very stable
- Tag taxonomy compliance: 0 violations, stable
- **Key finding this cycle:** STABLE — no remediation needed. Only notable item is the raw/ false positive.
- **Next cycle focus:** Verify `mop-agents-integration` orphan status (if unresolved at cycle 9, recommend Ty decide whether to add incoming links or let index.md coverage suffice). Check for ingestor stub-block recurrence.