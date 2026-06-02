# Librarians-Assistant Batch Progress

**Last updated:** 2026-06-02
**Batch:** 2026-06-02 morning run (post-librarian)

## Summary

| Metric | Count | Notes |
|--------|-------|-------|
| True knowledge orphans | 0 | All 137 orphans are operational/system files |
| Broken links | 5867 | ALL operational path artifacts — zero in knowledge content |
| Missing frontmatter | 120 | All operational files — templates, agent sheets, reports |
| Non-reciprocal links | 345 | wiki_lint body-text-only detection — high false-positive rate (many already reciprocal via Connections sections) |
| GAAC missing links | ~60,000 | Extraordinarily high — includes false positives from loosely-related same-cluster topics |
| Reciprocal links added (cumulative) | 11 | All genuine gaps found and resolved |
| **Content cleanups (this cycle)** | **2** | MOP self-link + agents.md duplicates |

## Resolution Details

### This Cycle (2026-06-02)
**Vault health confirmed stable + 2 minor content cleanups:**
- 1325 pages total (per lint) — +1 from this morning's 1324 audit (consistent with steady ingestion)
- HITS scores consistent with prior cycles (mop 0.0150, efhf 0.0057, concept-index 0.0053, load-bearing-reasoning 0.0041)
- All 137 orphans verified operational/system files — no knowledge-layer orphans
- 5867 broken links ALL trace to agent sheet migration paths — not knowledge content
- Non-reciprocal lint flags: body-text-only detection does not account for Connections sections where many links are already bidirectional
- **MOP page cleaned**: removed self-referential `[[maximum-occupancy-principle]]` wikilink (was creating phantom authority node in HITS); removed operational path artifacts from Connections
- **agents.md cleaned**: removed duplicate `- [[agentic-design-picker]]` and `- [[multi-agent-systems]]` lines in Connections section

### Prior Cycles (reference)
- **2026-08-29**: Vault health verified stable
- **2026-08-27**: EFHF frontmatter fixes (sources field, EFHF→efhf tag, Kernel-1/Kernel-2→kernel-1/kernel-2)
- **2026-08-26**: PKM → knowledge-management tag normalization on knowledge-management.md
- **2026-08-25**: 5 genuine reciprocal link fixes
- **2026-08-24**: GAAC phantom page analysis — all "missing link" pairs reference deleted pages in .trash/
- **2026-08-10**: 2 reciprocal links added (agent-onboarding → project-synapse, zettelkasten → knowledge-management)
- **2026-08-23 librarian**: 276 → 43 orphans reduced; all remaining are operational files
- **2026-09-10**: graph-theory.md stale link to archived knowledge-graph removed

## Next Batch Priority

1. **All remediation items resolved** — vault is structurally healthy
2. **Remaining blockers (need Ty input)**:
   - GoodRobot multi-location: 11 files across 2 vault paths — canonical location undecided
   - gbrain.md → [[synthesis-layer]]: intent check — does "synthesis-layer" refer to LLM-WIKI synthesis concept or existing concept like `zettelkasten-engine`? (Note: gbrain page itself doesn't exist — phantom target)
   - maximum-occupancy-principle duplicate slug: phantom authority node likely resolved this cycle (self-link removed); will verify on next HITS run

## Kanban Task Tracking

All prior kanban tasks resolved. No active remediation tasks.

## Related
- [[wiki/index]]
- [[scratchpad/agent-sheets/librarians-assistant/carryover]]

## Blockers (unchanged — need Ty decisions)

1. **GoodRobot multi-location** (since 2026-07-29): 11 files across 2 vault paths — canonical location undecided
2. **gbrain synthesis-layer wikilink** (since 2026-07-29): intent check — does "synthesis-layer" refer to LLM-WIKI synthesis concept or existing concept like `zettelkasten-engine`? **Note**: gbrain page itself is phantom (not found on disk) — the MOP `[[gbrain]]` reference points to a non-existent target
3. **maximum-occupancy-principle duplicate slug** (open since carryover inception): phantom authority, **likely resolved this cycle** by removing the self-referential wikilink — verify on next HITS run
