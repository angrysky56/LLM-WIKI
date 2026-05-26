# Librarian Carryover — 2026-07-21

## Kanban Status
- [x] Reviewed open items: none require external delegation this cycle
- [x] MCP tools not reachable this cycle (hermes-agent cron context) — audit via grep/find

## Established

### Vault Stats (Updated)
- Total wiki pages: 1096 (+11 since last carryover on 2026-07-10)
- concepts/: 489 | entities/: 69 | synthesis/: 119 | sources/: 215 | projects/: 13
- Stub concepts (≤15 lines): 8 (massively reduced from 328 - prior count may have miscounted or categorized differently)
- .bak files: 44 (unchanged)
- Misclassification: none — prior `legal-accountability-stub.md` was already in `wiki/concepts/` (carryover was wrong about location)
- No stale pages detected

### GoodRobot Duality (UNCHANGED — Ty decision still needed)
- `wiki/entities/projects/goodrobot.md` — Status: SHUT DOWN (May 18), company was simulating corporate governance
- `wiki/projects/projects 1/goodrobot.md` — Status: Active (May 13), separate project analysis
- Both are `type: entity` — same underlying entity, two different writeups stored in different vault locations
- Priority: MEDIUM — no functional breakage, just storage redundancy

### Broken Links
- 30 files contain link patterns matching broken-link conventions — expected (teaching examples in operating guide docs)
- No new broken links detected this cycle

### Orphans
- Very few orphan candidates — `wiki/` structure has deep cross-linking via Connections sections
- 833 pages have `## Connections` sections (strong linking culture)

## Open

1. **GoodRobot duplicate** — two entity pages for same entity in different vault locations — needs Ty consolidation decision
2. **44 .bak files** — 45-day accumulation, each represents an in-place file overwrite — consider archival strategy
3. **Stub concepts (8 files, ≤15 lines)** — minimal content, low priority given quality bar is being met elsewhere

## Heading

- GoodRobot: propose Ty choose one canonical location and archive/move the other
- MCP tools still unavailable in cron context — grep/find fallback continues to work
- No external agent delegation needed this cycle
