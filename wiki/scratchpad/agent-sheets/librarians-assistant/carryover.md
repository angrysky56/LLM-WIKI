---
summary: Librarians-Assistant carryover 2026-06-02 — 2 minor content cleanups applied; MOP phantom authority and agents.md duplicate links addressed. Vault remains structurally stable.
tags: [librarians-assistant, carryover, batch-remediation, stable-vault, mop-phantom]
updated: 2026-06-02T08:50:00Z
created: 2026-05-27
type: carryover
summary: 2 minor content cleanups applied this cycle. MOP page had self-referential wikilinks contributing to phantom authority score; agents.md had duplicate wikilinks in Connections section. Vault remains structurally stable per librarian's 2026-06-02 audit (1324 pages, +36 from prior cycle, 0 new actionable items).
tags: [librarians-assistant, carryover, batch-remediation, stable-vault, mop-phantom]
---

# Librarians-Assistant Carryover — 2026-06-02

## Established

### Vault Health Snapshot (2026-06-02, fresh diagnostics)
- **Total pages**: 1325 (per lint) / 1319 (per index update; archived pages excluded from index)
- **Orphans (137)**: ALL operational/system files — not actionable (agent sheets, carryovers, discovery, headlines, overseer, arxiv/news briefs)
- **Broken links (5867)**: ALL operational path artifacts — not actionable
- **Missing frontmatter (120)**: ALL operational files — not actionable
- **Non-reciprocal (345)**: High false-positive rate per skill pitfalls — vault-path-slug resolution artifact
- **GAAC clusters (36)**: stable
- **Non-preferred tags (0)**: clean
- **HITS scores**: stable vs 2026-06-01 audit (mop 0.0150, efhf 0.0057, concept-index 0.0053, load-bearing-reasoning 0.0041)

### This Cycle — 2 Minor Content Cleanups

1. **MOP phantom authority cleaned up** — `wiki/concepts/maximum-occupancy-principle.md` had a self-referential `[[maximum-occupancy-principle]]` wikilink in its Connections section that contributed to the HITS analyzer treating it as a separate authority node (the phantom "duplicate" of MOP). The wikilink alias generated the second authority node seen in HITS reports. Removed the self-referential link and reorganized the page:
   - Removed `[[scratchpad/agent-sheets/librarians-assistant/workspace/batch-progress]]`, `[[scratchpad/jobs/reports/librarian/audit-2026-05-21]]`, `[[scratchpad/agent-sheets/librarian/carryover]]`, `[[scratchpad/agent-sheets/librarians-assistant/carryover]]` from Connections (operational path artifacts, not knowledge content)
   - Removed the duplicate `[[maximum-occupancy-principle]]` self-link (the phantom source)
   - Restructured: kept "## Connections" as curated authoritative links; added "## See Also" for the curated subset; created "## Related Concepts" for the broad reference list
   - Result: the phantom MOP authority node should disappear after next HITS run

2. **`wiki/concepts/agents.md` duplicate links cleaned** — The page had `- [[agentic-design-picker]]` and `- [[multi-agent-systems]]` each appearing twice in the Connections block. Removed the duplicates.

### MOP Duplicate Discrepancy — Resolved at the On-disk Level

The HITS analyzer reports both `maximum-occupancy-principle` (0.0150) and `concepts/maximum-occupancy-principle` (0.0127) as separate authority nodes. **This is a phantom, not a real duplicate:**

- On-disk verification: only `wiki/concepts/maximum-occupancy-principle.md` exists; `wiki/maximum-occupancy-principle.md` returns "page not found" via `wiki_read_page`
- The phantom authority score comes from the self-referential `[[maximum-occupancy-principle]]` wikilink in the MOP page's Connections section
- The HITS analyzer is treating the bare-slug wikilink alias as a separate node
- **With the self-link removed this cycle, the phantom should resolve naturally on next HITS run**

This is structurally different from the 2026-09-10 carryover's claim that the duplicate was "Resolved — Single page exists" — that was a false claim. The reality is: the duplicate never existed at the file level; only the HITS analyzer was seeing two nodes due to the self-referential link. The 2026-06-01 carryover's Open #1 (MOP duplicate slug) is **technically resolved by removing the self-link** — the duplicate wasn't a duplicate of files, it was a phantom of the analyzer.

## Open Items

### Batch Remediation Status

| Item | Count | Status |
|------|-------|--------|
| GAAC "missing links" | ~60,000 | Not actionable — includes false positives; phantom pages confirmed in Cluster 0 |
| Non-reciprocal lint flags | 345 | High false-positive rate — body-text-only detection misses Connections-section reciprocity |
| Reciprocal link fixes (cumulative) | 11 + 2 cleanup | All genuine gaps resolved in prior cycles; this cycle added 2 minor content cleanups |
| Orphans (non-operational) | 0 | All 137 are operational/system files |
| Non-preferred tags | 0 | All 12 USE-table violations resolved in prior cycles |
| Broken links | 5867 | ALL operational artifacts — not actionable |
| EFHF frontmatter | Resolved | Already compliant |
| graph-theory stale link | Resolved | Link to archived knowledge-graph removed 2026-09-10 |
| **MOP duplicate slug** | **Phantom, likely resolved** | Self-referential link removed this cycle — phantom should disappear on next HITS run |
| **MOP page cleanup** | **Done this cycle** | Removed operational path links + duplicate self-link |

### Blockers Needing Ty Input
1. **GoodRobot multi-location** (open since 2026-07-29): 11 files across 2 vault paths — canonical location undecided
2. **gbrain.md → [[synthesis-layer]] wikilink** (open since 2026-07-29): intent check — `wiki/concepts/gbrain.md` returns "page not found" (phantom target); the [[gbrain]] reference is just a MOP Connections pointer to a non-existent page. The "synthesis-layer" intent question is moot until the gbrain page is created or the link is removed.

These are all "judgment" items per the Hard Blockers section of the skill — they should not be auto-resolved.

## Kanban Status

### Open Tasks
*None — all prior kanban tasks resolved per the 2026-09-10 carryover*

### Resolved This Cycle
- [x] Vault health confirmed stable: 1325 pages (1324 reported this morning's audit; +1 from ingestion)
- [x] HITS scores verified stable vs carryover
- [x] GAAC Cluster 0 reconfirmed as false positive (phantom pages + TF-IDF noise)
- [x] No new actionable items found — librarian's "stable" verdict verified
- [x] MOP page self-referential link removed (phantom authority likely resolved)
- [x] agents.md duplicate wikilinks cleaned

## Heading

- **Vault structural integrity**: stable for 4+ cycles; no new remediation targets
- **2 minor content cleanups applied this cycle**: MOP self-link removed, agents.md duplicates removed
- **Phantom MOP authority likely resolved** by removing the self-referential wikilink; will verify on next HITS run
- **No fixes needed for the high-count lint/GAAC items** — they are operational artifacts (or phantom pages) by design
- **Cumulative fixes**: 11 reciprocal link fixes + 3 tag normalizations + 1 stale link fix + 2 content cleanups across all cycles
- **Next priority**: GoodRobot multi-location + gbrain intent — both require Ty judgment
