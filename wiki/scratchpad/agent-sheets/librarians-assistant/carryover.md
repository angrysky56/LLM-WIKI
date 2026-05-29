---
created: 2026-05-27
updated: 2026-08-27T06:00:00Z
type: carryover
summary: EFHF frontmatter fixed (sources field malformed chars, EFHF→efhf tag, Kernel-1/Kernel-2→kernel-1/kernel-2); vault structurally healthy — all remaining items need Ty decisions or librarian judgment
tags: [librarians-assistant, carryover, batch-remediation, reciprocal-links, tag-normalization]
---

# Librarians-Assistant Carryover — 2026-08-27

## Established

### This Cycle — EFHF Frontmatter Fixes (2026-08-27)
1. **wiki/entities/projects/efhf.md**: fixed three frontmatter issues:
   - `sources: [']', '[[maximum-occupancy-principle]']` → `sources: []` (malformed chars removed)
   - `EFHF` tag → `efhf` per controlled vocabulary (lowercase convention)
   - `Kernel-1`, `Kernel-2` tags → `kernel-1`, `kernel-2` (all other tags lowercase; kernel-1/kernel-2 are stable identifiers the system uses with lowercase)

### This Cycle — Vault Health (2026-08-27)
- **Total pages**: 1198 (wiki/index)
- **Orphans**: 57 — all operational/system files (carryovers, agent sheets, TEMPLATE, discovery reports, .trash artifacts) — no knowledge orphans
- **Non-reciprocal lint flags**: vault-path slug-resolution artifacts — same conclusion as prior cycles
- **HITS analysis**: stable — wiki/index (0.0786) and log (0.0561) as structural hubs; maximum-occupancy-principle (0.0160) as top authority
- **GAAC Cluster 0**: meta-advancement cluster pages (meta-advancement, Meta-Meta Process, discrete-time-to-event-modeling, solo-preneur) — all missing links are .trash artifacts or Clippings sources, not wiki pages

### Prior Cycles
- **2026-08-26**: PKM → knowledge-management tag normalization on knowledge-management.md
- **2026-08-25**: 5 genuine reciprocal link fixes (bounded-structured-memory↔zettelkasten-engine, agem↔verifier-graph, tyler-hall↔verifier-graph)
- **2026-08-24**: GAAC phantom page analysis — all "missing link" pairs reference deleted pages in .trash/
- **2026-08-10**: 2 reciprocal links added (agent-onboarding → project-synapse, zettelkasten → knowledge-management)
- **2026-08-23 librarian**: 276 → 43 orphans reduced; all remaining are operational files

## Open Items

### Batch Remediation Status
| Item | Count | Status |
|------|-------|--------|
| GAAC "missing links" | All phantom | No valid targets — deleted/moved pages in .trash/ |
| Non-reciprocal lint flags | ~236 | Vault-path slug-resolution artifact — no valid targets |
| Reciprocal link fixes | 7 applied (total) | Genuine gaps found and resolved |
| Orphans (non-operational) | ~0 | All orphans are operational/system files |
| EFHF frontmatter | 1 fixed | Sources malformed chars + tag case + kernel tag case resolved |

### Blockers — Ty Decisions Needed (unchanged since Jul 29)
1. **GoodRobot multi-location**: 11 files across 2 vault paths — canonical location undecided
2. **gbrain.md → [[synthesis-layer]]**: Intent check — does "synthesis-layer" refer to LLM-WIKI synthesis concept or existing concept like `zettelkasten-engine`?
3. **maximum-occupancy-principle duplicate slug**: `concepts/maximum-occupancy-principle` (0.0138) alongside root `maximum-occupancy-principle` (0.0160) — should consolidate to single canonical page

### Merge Candidates (flagged to librarian, needs review)
- **abstract-algebra ↔ business/entrepreneurship/innovation/pure-mathematics**: similarity 1.0 — likely false positive from short page content
- **3dgs ↔ habitat**: similarity 1.0 — should review if genuinely related or redundant

## Kanban Status

### Open Tasks (informational cards)
| Task ID | Title | Status |
|---------|-------|--------|
| — | None | No new tasks created this cycle |

### Resolved This Cycle
- [x] EFHF sources field: malformed `[']', '[[maximum-occupancy-principle]']` → `sources: []`
- [x] EFHF tag: `EFHF` → `efhf` per controlled vocabulary
- [x] EFHF tags: `Kernel-1`/`Kernel-2` → `kernel-1`/`kernel-2` (all wiki tags lowercase convention)
- [x] Vault health confirmed: 1198 pages, stable HITS/GAAC state

## Heading

- **Vault structural integrity**: stable — content pages well-connected; no genuine self-remediable targets from lint/GAAC analysis
- **Remaining open**: GoodRobot location, gbrain/synthesis-layer intent, maximum-occupancy-principle duplicate slug (all need Ty input)
- **Next run priority**: wait for librarian's next HITS/GAAC refresh, Ty resolves blockers, or genuine new content gaps surface
- **No new remediation items identified**: EFHF frontmatter fix was the only actionable item from this cycle's analysis
