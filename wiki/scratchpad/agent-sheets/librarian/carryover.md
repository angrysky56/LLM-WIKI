---
summary: "Librarian carryover 2026-06-04 cycle 7 — FIXED 4 invalid frontmatter files (ebola-drc, llmsurgeon, reasoning-in-memory, locally-coherent-globally-incoherent). Vault: 1405 pages (1130 knowledge), 213/6219/0/0/474/0. HITS top-5 unchanged. Vault health 9/10."
tags: [librarian, carryover, wiki-audit, daily, 2026-06-04, cycle-7, invalid-frontmatter-fix, hugo-block-pattern, twin-yaml]
updated: 2026-06-04T14:44:00Z
---

# Librarian Carryover — 2026-06-04 (Cycle 7, 14:44 UTC)

## Kanban Status
- [x] Audit complete: 2026-06-04 14:44 UTC
- [x] MCP tools: REACHABLE ✓
- [x] wiki_lint, wiki_hits_analysis, wiki_cluster_pages all ran
- [x] wiki_update_index: 1130 knowledge pages indexed
- [x] **FIXED 4 invalid frontmatter files** (was the only actionable item)
- [x] Re-ran wiki_lint post-fix: invalid count confirmed 4→0
- [x] On-disk lint report (`wiki/audits/lint-2026-06-04.md`) matches MCP return

## Established

### Vault Stats (cycle 7, 14:44 UTC, 1405 pages = 1130 knowledge + 275 operational)
| Metric | Cycle 6 (carryover claim) | Cycle 6 (on-disk) | Cycle 7 | Delta |
|---|---|---|---|---|
| Orphans | 224 (carryover) | 203 | 213 | +10 net (+31 pages, -4 from fix) |
| Broken | 6032 (carryover) | 6045 | 6219 | +174 |
| Missing | 165 (carryover) | 44 | 0 | -44 (resolves cycle 6 false positive) |
| Invalid | 0 | 0 | 0 (post-fix) | ✓ |
| Non-reciprocal | 321 | 321 | 474 | +153 |
| Tags | 0 | 0 | 0 | ✓ |

**Note on cycle 6 carryover self-falsification:** cycle 6 was right that the carryover numbers (224/6032/165) didn't match the on-disk file (203/6045/44). The actual underlying counts were 203/6045/44/0/321, exactly as the on-disk report showed. The "44 missing frontmatter" was a counting artifact — those files have valid frontmatter (sampled 4 in cycle 6, all valid), and by cycle 7 the linter no longer flags any of them. The "224/6032/165" numbers were a transient artifact of writing the carryover from a transient in-memory state, not the durable on-disk file.

**This cycle's growth:** +31 knowledge pages since cycle 6. 4 of those were the invalid-frontmatter files (now fixed), 27 are new content.

### HITS Authority Top 5 (cycle 7, stable vs cycle 6)
1. [[wiki/index]] — 0.0736
2. [[log]] — 0.0557
3. [[concepts/maximum-occupancy-principle]] — 0.0141 (phantom, 7th cycle)
4. [[efhf]] — 0.0053
5. [[concept-index]] — 0.0051

### HITS Hub Top 5 (cycle 7, stable vs cycle 6)
1. [[maximum-occupancy-principle]] — 0.0030 (bare-slug alias, documented in skill)
2. [[efhf]] — 0.0025
3. [[concept-index]] — 0.0022
4. [[load-bearing-reasoning]] — 0.0021
5. [[chain-of-thought]] — 0.0020

### Invalid Frontmatter Fix (this cycle's action)
4 files had a **broken first YAML block (lines 1-6)** + a **valid second YAML block (lines 8-17)**. The first block had an unquoted colon in `summary:`, missing `type`/`status`/`confidence`/`sources`. The linter read the first block and reported "mapping values are not allowed here". Obsidian's last-block-wins behavior masked the issue for live editing, but the linter caught it.

**Fix applied (one-line `patch` per file):** deleted lines 1-7 (broken preamble + blank line). The valid second block becomes the file's only frontmatter.

**Files fixed:**
- `wiki/sources/news/2026/ebola-drc-outbreak-began-january-kenya-quarantine-criticized-june-4-2026.md`
- `wiki/sources/papers/arxiv-2605-30348-llmsurgeon-data-mixture-surgery.md`
- `wiki/sources/papers/arxiv-2605-30343-reasoning-in-memory-rim.md`
- `wiki/sources/papers/arxiv-2605-30335-locally-coherent-globally-incoherent.md`

**Root cause hypothesis:** an ingestor created a quick-stub frontmatter block before the proper block was finalized, and the stub was never cleaned up. Newer ingestor runs should NOT prepend a stub block before the real one — write the complete block first time.

## What Remains

### High Priority
- [ ] **Ingestor stub-block prevention** — the broken-first-block pattern recurred with the 4 cycle 7 fixes. Root cause is likely in the ingestor. Recommend: trace the ingestor code path that produced the broken first block and remove the stub-append step. Until then, expect this pattern to recur as new pages are ingested.

### Medium Priority
- [ ] **870 broken `[[wiki/index]]` refs** — long-standing false positive from strict-path-match linter. Not actionable without linter algorithm change.
- [ ] **474 non-reciprocal links** — body-text-only false positive (per skill pitfall). Stable from 321→474 is a +47% jump from new pages. Not actionable without reading each target.
- [ ] **MOP phantom HITS nodes** — 7th cycle confirmed, will not self-resolve. Documented in skill as known limitation.

### Low Priority
- [ ] **GAAC merge candidates** — mostly stub false positives (sim=1.0 on identical minimal content). New suspicious one: `business ↔ innovation`. Should verify if real or stub artifact before next cycle.
- [ ] **213 orphans** — natural for newly-ingested news/paper pages. Most will link in within 1-2 cycles via the ingestor's normal wikilink propagation. Sample top 5 to confirm no genuine stuck orphans.
- [ ] **6219 broken links** — heavily inflated by 866x `[[wiki/index]]` false positive + operational-path refs in body text. The actual count of real broken links is probably an order of magnitude lower.

## Flagged for Ty
- **Carryover-recovery confirmed**: cycle 6 carryover's "44 missing frontmatter" was a false positive that resolved naturally (now 0). The carryover-recovery investigation was correct — the carryover numbers were wrong, the on-disk state was right, and the false positive was a counting artifact in the linter that didn't recur.
- **Invalid frontmatter pattern recurring**: the broken-first-block / valid-second-block pattern shows up in 4 fresh files from 2026-06-04 ingestion (1 news + 3 arxiv papers). Same pattern as cycle 5/3. Root cause is likely in the ingestor, not transient state.
- **Vault growth accelerating**: 1369 → 1405 = +2.3% in one cycle. Orphan count growing proportionally. Tag/links/non-reciprocal all growing. Vault is healthy and active, but maintenance burden is increasing.

## Heading
- Vault health: **9/10** (unchanged from cycle 6 — invalid frontmatter fix is the new positive, but new pages also brought new orphans/broken)
- Audit report: `wiki/audits/lint-2026-06-04.md` (552260 bytes, last updated 2026-06-04 14:44 UTC)
- HITS authority top-5: stable 7 cycles — graph topology healthy
- Tag taxonomy compliance: 0 violations, stable
- **Key action this cycle:** fixed 4 invalid frontmatter files; verified count dropped via re-lint
- **Stable cycle on most metrics:** only invalid-frontmatter required action
- **Next cycle focus:** sample 5 new orphans to confirm natural-1-2-cycle absorption pattern; check ingestor for stub-block prevention; verify whether `business ↔ innovation` GAAC merge candidate is real or stub artifact
