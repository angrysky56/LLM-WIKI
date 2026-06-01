---
summary: Librarians-Assistant carryover 2026-06-01 — 0 fixes applied, vault stable per librarian audit, all 3 long-standing items require Ty judgment (MOP duplicate, GoodRobot multi-location, gbrain synthesis-layer)
tags: [librarians-assistant, carryover, batch-remediation, stable-vault, no-actionable-items]
updated: 2026-06-01T14:46:29Z
---

---
created: 2026-05-27
updated: 2026-06-01T08:55:00Z
type: carryover
summary: 0 fixes applied — librarian carryover confirms vault stable, no actionable items. Verified fresh diagnostics match carryover counts. GAAC Cluster 0 over-clustering false positive reconfirmed (2 of 4 pages are phantom).
tags: ['librarians-assistant', 'carryover', 'batch-remediation', 'stable-vault', 'no-actionable-items']
---

# Librarians-Assistant Carryover — 2026-06-01

## Established

### Vault Health Snapshot (2026-06-01, fresh diagnostics)
- **Total pages**: 1289 (↑ from 1288 in carryover — +1 since this morning's audit; consistent with steady ingestion)
- **Orphans (119)**: ALL operational/system files — not actionable (agent sheets, carryovers, discovery, headlines, overseer, arxiv/news briefs)
- **Broken links (~5750)**: ALL operational path artifacts — not actionable
- **Missing frontmatter (~115)**: ALL operational files — not actionable
- **Non-reciprocal (336)**: High false-positive rate — body-text-only detection misses Connections-section reciprocity. Per skill pitfalls, not actionable without manual verification.
- **GAAC clusters (36)**: 1 new cluster emerged (Cluster 28 — bounded-representation-capacity), 35 stable
- **Non-preferred tags (0)**: Clean — all 12 USE-table violations resolved in prior cycles
- **HITS scores**: stable vs 2026-06-01 carryover (mop 0.0152, efhf 0.0057, concept-index 0.0053, load-bearing-reasoning 0.0041)

### This Cycle — 0 Remediation Fixes
The 2026-06-01 librarian carryover explicitly states: **"No new actionable items — vault is stable"** and **"All prior cycle open items reviewed — still unchanged (operational artifacts, zero knowledge impact)"**. Fresh diagnostic re-run this morning (wiki_lint, wiki_hits_analysis, wiki_cluster_pages) confirms all counts match the carryover. No new high-priority remediation targets.

### GAAC Cluster 0 — Reconfirmed as False Positive
- Pages flagged: `eris-mythology`, `ssh-command-in-linux`, `isabelle-installation`, `modelfile-reference`
- **2 of 4 pages are phantom** — `wiki/concepts/eris-mythology.md` and `wiki/concepts/ssh-command-in-linux.md` return "page not found" (likely deleted and moved to .trash/ or never persisted as concepts)
- The remaining 2 pages (`isabelle-installation`, `modelfile-reference`) are unrelated reference stubs (Isabelle theorem prover install guide, Ollama Modelfile reference) grouped by TF-IDF noise
- **Decision**: No link additions — documented GAAC over-clustering false positive per `references/gaac-over-clustering.md`

### MOP Duplicate Discrepancy (between carryovers)
- **2026-09-10 carryover claim**: "Maximum-occupancy-principle slug: Resolved — Single page exists"
- **2026-06-01 librarian carryover reality**: Duplicate STILL exists — `concepts/maximum-occupancy-principle` (0.0129) coexists with root `maximum-occupancy-principle` (0.0152). Carried as "Open #1" in today's audit.
- **Fresh diagnostic confirmation**: HITS shows both pages with non-zero authority scores — duplicate is still present.
- The 2026-09-10 carryover entry was a false claim. The duplicate is a known long-standing item (open since carryover inception) and is **non-urgent per the librarian** — both pages exist, both are properly linked, neither is broken. This is a **blocker requiring Ty judgment** on which canonical location to keep.
- The 2026-09-10 carryover should not be retroactively corrected here — that's a separate historian concern, not a remediation fix.

## Open Items

### Batch Remediation Status
| Item | Count | Status |
|------|-------|--------|
| GAAC "missing links" | ~60,000 | Not actionable — includes false positives; phantom pages confirmed in Cluster 0 |
| Non-reciprocal lint flags | 336 | High false-positive rate — body-text-only detection misses Connections-section reciprocity |
| Reciprocal link fixes (cumulative) | 11 | All genuine gaps resolved in prior cycles |
| Orphans (non-operational) | 0 | All 119 are operational/system files |
| Non-preferred tags | 0 | All 12 USE-table violations resolved in prior cycles |
| Broken links | ~5750 | ALL operational artifacts — not actionable |
| EFHF frontmatter | Resolved | Already compliant |
| graph-theory stale link | Resolved | Link to archived knowledge-graph removed 2026-09-10 |
| **MOP duplicate slug** | **Still present** | `concepts/maximum-occupancy-principle` + root `maximum-occupancy-principle` both exist; non-urgent per librarian; **needs Ty judgment for canonical location** |

### Blockers Needing Ty Input
1. **MOP duplicate slug** (long-standing, open since carryover inception): Which page is canonical?
   - Option A: keep root `maximum-occupancy-principle.md` (higher authority 0.0152) and archive `concepts/maximum-occupancy-principle.md`
   - Option B: keep `concepts/maximum-occupancy-principle.md` (consistent with concepts/ folder structure) and redirect root
2. **GoodRobot multi-location** (open since 2026-07-29): 11 files across 2 vault paths — canonical location undecided
3. **gbrain.md → [[synthesis-layer]] wikilink** (open since 2026-07-29): intent check — does "synthesis-layer" refer to LLM-WIKI synthesis concept or existing concept like `zettelkasten-engine`?

These are all "judgment" items per the Hard Blockers section of the skill — they should not be auto-resolved.

## Kanban Status

### Open Tasks
*None — all prior kanban tasks resolved per the 2026-09-10 carryover*

### Resolved This Cycle
- [x] Vault health confirmed stable: 1289 pages (carryover said 1288; +1 from ingestion)
- [x] HITS scores verified stable vs carryover
- [x] GAAC Cluster 0 reconfirmed as false positive (phantom pages + TF-IDF noise)
- [x] No new actionable items found — librarian's "stable" verdict verified

## Heading

- **Vault structural integrity**: stable for 4+ cycles; no new remediation targets
- **No fixes applied this cycle**: the librarian's "no actionable items" verdict is correct; manufacturing work to fit a quota would create noise, not value
- **Non-preferred tags**: clean — 0 active violations across all 12 USE-table entries
- **Cumulative fixes**: 11 reciprocal link fixes + 3 tag normalizations + 1 stale link fix across all cycles
- **Discrepancy surfaced**: 2026-09-10 carryover claims MOP duplicate resolved; 2026-06-01 carryover + fresh diagnostic show it still exists (non-urgent, still needs Ty decision)
- **Next priority**: MOP duplicate consolidation — only remaining open remediation target that does not require Ty judgment (though Ty's canonical-location preference would speed it up). Other items all require Ty input.
