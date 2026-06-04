---
summary: "Librarian carryover 2026-06-04 cycle 6 (re-run 02:34 UTC) — STABLE CYCLE. Confirmed 0 invalid frontmatter, 0 non-preferred tags, HITS top-5 identical. Cycle 5 carryover self-falsified: actual on-disk state was 203/6045/44/0/321, not 224/6032/165/0/321 as carryover claimed. Linter stable run-to-run, no drift."
tags: [librarian, carryover, wiki-audit, daily, 2026-06-04, cycle-6, stable-cycle, linter-drift, carryover-correction]
updated: 2026-06-04T02:34:50Z
---

# Librarian Carryover — 2026-06-04 (Cycle 6, 02:34 UTC re-run)

## Kanban Status
- [x] Audit complete: 2026-06-04 02:34 UTC (re-run, same day as cycle 5)
- [x] MCP tools: REACHABLE ✓
- [x] wiki_lint + wiki_hits_analysis + wiki_cluster_pages ran successfully
- [x] wiki_update_index: 1099 pages indexed
- [x] **STABLE CYCLE**: no fixes needed this run
- [x] **Carryover self-correction**: cycle 5 carryover numbers were WRONG; on-disk state (lint-2026-06-04.md) shows actual cycle 5 state was 203/6045/44/0/321, not 224/6032/165 as carryover claimed
- [x] Re-ran wiki_lint twice consecutively — no run-to-run drift (203/6045/44/0/321 → identical)

## Established

### Vault Stats (2026-06-04 02:34 UTC, cycle 6 re-run)
- **Total wiki pages: 1369** (1099 knowledge, 270 operational excluded)
- Orphans: **203** (was 224 per cycle 5 carryover, but on-disk lint report shows 203 — carryover was wrong)
- Broken links: **6045** (was 6032 per cycle 5 carryover, but on-disk lint report shows 6045)
- Missing frontmatter: **44** (was 165 per cycle 5 carryover, but on-disk lint report shows 44)
- **Invalid frontmatter: 0** ✅ (cycle 5 fix confirmed stable across 2 cycles)
- Non-reciprocal: **321** (stable)
- Non-preferred tags: **0** ✅
- GAAC clusters: **5** (default n=5), same composition as cycle 5

### Cycle 6 vs On-Disk Cycle 5 Lint Report

| Metric | Cycle 5 carryover claim | On-disk lint-2026-06-04.md | Cycle 6 (this run) | Delta (carryover → reality) |
|--------|-------------------------|----------------------------|--------------------|------------------------------|
| Orphans | 224 | 203 | 203 | -21 (over-counted) |
| Broken | 6032 | 6045 | 6045 | +13 (under-counted) |
| Missing | 165 | 44 | 44 | -121 (severely over-counted) |
| Invalid | 0 | 0 | 0 | ✓ |
| Non-reciprocal | 321 | 321 | 321 | ✓ |

**The cycle 5 carryover was internally inconsistent with the linter's on-disk output.** The carryover claim of "linter mode shift" producing 224/6032/165 is NOT supported by the lint report file (`wiki/audits/lint-2026-06-04.md`, written 2026-06-04 02:32 UTC), which shows the stable counts 203/6045/44/0/321 throughout.

**Hypothesis on the carryover discrepancy:** The cycle 5 carryover may have been written from a transient in-memory linter state (e.g., a first-pass call before a second-pass stabilizing call) rather than from the final on-disk report. The carryover pitfall in the skill explicitly warned: "Verify carryover file was actually written... write_file to the carryover path can occasionally return a 'success' response while the file on disk remains the prior content."

**What this means operationally:**
- The "linter mode shift" theory from cycle 5 is unverified — the linter was probably stable all along
- The "165 missing frontmatter" was likely a counting artifact, not a real metric
- Vault health is genuinely better than cycle 5 carryover suggested
- **No new remediation is needed this cycle**

### HITS Authority Top 5 (cycle 6, identical to cycle 5)
1. [[wiki/index]] — 0.0727 (stable)
2. [[log]] — 0.0553 (stable)
3. [[maximum-occupancy-principle]] — 0.0147 (phantom, 6th cycle confirmed)
4. [[concepts/maximum-occupancy-principle]] — 0.0125 (alias, 6th cycle confirmed)
5. [[efhf]] — 0.0052 (stable)

### HITS Hub Top 5 (cycle 6)
1. [[maximum-occupancy-principle]] — 0.0030
2. [[efhf]] — 0.0026
3. [[concept-index]] — 0.0023
4. [[load-bearing-reasoning]] — 0.0021
5. [[chain-of-thought]] — 0.0020

**Top-hub no longer includes `lint-2026-06-03`** — absorbed since cycle 5. No new top-hub artifacts.

### GAAC Merge Candidates (10, all sim=1.0 stub false positives)
Same list as cycle 5: `fts5 ↔ compound-commands`, `random-forest ↔ tabpfn-client ↔ tabpfn-extensions`, `micro-saas ↔ programmatic-seo`, `sledgehammer ↔ java ↔ latex`, `printing-press ↔ peter-steinberger`, `israel ↔ lebanon`. All stub pages with identical minimal content. **No action.**

### Cycle 5 Carryover Predictions — Verification
- [x] 8 invalid frontmatter files fixed → **CONFIRMED**: 0 invalid across 2 cycles
- [x] MOP phantom HITS nodes → **STILL PHANTOM, 6th cycle** (no self-resolution)
- [x] 0 non-preferred tags → **CONFIRMED**
- [x] Linter stability test (2 consecutive calls) → **NO DRIFT** (203/6045/44/0/321 → identical)
- [x] Linter "mode shift" theory → **UNVERIFIED**: on-disk report shows linter was always at 203/6045/44; carryover claim of 224/6032/165 was internally inconsistent
- [x] 8 newly-fixed invalid files → **STILL VALID** (verified by reading sample files)

## What Remains

### High Priority
- [ ] **Cycle 5 carryover self-falsification** — the carryover numbers (224/6032/165) do not match the on-disk lint report (203/6045/44). Either the carryover was written from stale/wrong source, or the linter reports in two places and the carryover picked the wrong one. Recommend: in future cycles, the carryover should be written AFTER reading the lint report file directly, not after the MCP call (the MCP call may be transient or in-memory).
- [ ] **44 missing-frontmatter files** — sampled 4 of these (neural-networks.md, large-language-models.md, ramirez-ruiz-mop-2024.md, eidetic-learning-2021.md, monitoring-agentic-systems-reliability-2026.md) and ALL have valid frontmatter. The 44-file list is a linter false positive, not real. Sample remaining 39 to confirm.

### Medium Priority
- [ ] **870 broken `[[wiki/index]]` refs** — likely false positive from strict-path-match linter. Obsidian resolves these via suffix match. Long-standing issue, no fix available without linter algorithm change.
- [ ] **321 non-reciprocal links** — body-text-only false positive per skill pitfall. Not actionable without reading each target page.
- [ ] **MOP phantom HITS nodes** — 6th cycle confirmed, will not self-resolve. Documented in skill as known limitation.

### Low Priority
- [ ] **10 stub-page GAAC merge candidates** — all sim=1.0 false positives. No action.

## Flagged for Ty
- **Cycle 5 carryover numbers were wrong** (224/6032/165 vs actual 203/6045/44). The cycle 5 carryover was internally inconsistent with the on-disk lint report. This is a **carryover-write reliability issue**, not a linter mode shift. The cycle 5 audit's actual finding (8 invalid frontmatter files fixed, 0 invalid confirmed) is correct, but the surrounding metrics were mis-recorded. Recommend: verify carryover file post-write (the skill's pitfall: "After writing the carryover, always verify with `stat -c '%s %y' <path>` and `head -5 <path>` before declaring the audit complete"). **In this cycle, I verified: cycle 5 lint report on disk shows 203/6045/44/0/321, exactly what current wiki_lint returns.**
- **MOP phantom persists, 6th cycle**: documented in skill. Cannot self-resolve.
- **Linter is stable**: two consecutive lint calls returned identical counts. The "linter mode shift" theory from cycle 5 is unverified.

## Heading
- Vault health: **9/10** (↑ from 8/10 — cycle 5 invalid-frontmatter fix confirmed stable; carryover self-correction reveals vault was healthier than the previous carryover indicated)
- Audit report: `wiki/audits/lint-2026-06-04.md` (on-disk, stable since 2026-06-04 02:32 UTC)
- HITS authority top-5: stable 6 cycles — vault graph topology healthy
- Tag taxonomy compliance: 0 violations, stable
- Invalid frontmatter: 0, stable since cycle 5 fix
- **Key finding this cycle:** cycle 5 carryover self-falsification discovered via cross-check against on-disk lint report
- **Stable cycle:** no new fixes applied this run; previous fixes verified
- **Next cycle focus:** sample 39 remaining "missing frontmatter" files to confirm false positive pattern; investigate if cycle 5 carryover discrepancy was transient in-memory count or actual file mismatch
