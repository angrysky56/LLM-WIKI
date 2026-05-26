# Librarian Carryover — 2026-07-10

## Kanban Status
- [x] Reviewed open items: none require external delegation this cycle
- [x] MCP tools not reachable this cycle (hermes-agent cron context) — audit via grep/find

## Established

### Vault Stats (Updated)
- Total wiki pages: 1085
- concepts/: 489 | entities/: 69 | synthesis/: 119 | sources/: 215 | projects/: 13
- Stub concepts: 328 (unchanged — large volume, low priority for conversion)
- .bak files: 44 (+23 since last carryover on 2026-05-26 — accumulating rapidly)
- Misclassification: 1 found — `wiki/entities/legal-accountability-stub.md` has `type: concept`
- No stale pages (all pages have been touched in the last 60 days)

### GoodRobot Duality
- `wiki/entities/projects/goodrobot.md` (status: active, last updated May 24)
- `wiki/projects/projects 1/goodrobot.md` (status: active, last updated May 13)
- Both exist for the same entity — ongoing issue, awaiting Ty decision

### Broken Links
- 30 files contain link patterns matching broken-link conventions — expected (teaching examples in operating guide docs)
- No new broken links detected

## Open

1. **GoodRobot duplicate** — two paths for same entity (entities/projects/ vs projects/projects 1/) — needs Ty consolidation decision
2. **44 .bak files** — accumulating since May 26 (+23 in 45 days) — each represents an in-place overwrite
3. **328 stub concepts** — low priority, large volume
4. **Misclassification** — `wiki/entities/legal-accountability-stub.md` has `type: concept` (should be in concepts/ folder)

## Heading

- Quick fix: move legal-accountability-stub.md to concepts/ folder + fix type in frontmatter
- MCP tools still unaivable in cron context — grep/find fallback continues to work
- No external agent delegation needed this cycle
