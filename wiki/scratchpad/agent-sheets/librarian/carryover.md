# Librarian Carryover — 2026-07-26

## Kanban Status
- [x] Audit complete: 2026-07-26 08:50 AM UTC
- [x] MCP tools: REACHABLE this cycle ✓
- [x] Kanban tasks created for open items (per kanban-review skill):
  - t_029ba0b1e28a199f: GoodRobot multi-location consolidation — blocked, needs Ty
  - [x] t_2dc7aaf9d398a4c8: 44 .bak files — RESOLVED: bulk deleted per dashboard directive
  - t_0adf1f46e814ee2f: 8 stub concepts — ready (delegate)
  - t_8d4282a9420e6d6e: 85 broken links — ready (delegate)

## Established

### Vault Stats (Updated)
- Total wiki pages: 1102 (+6 since last carryover 2026-07-21)
- concepts/: 490 | entities/: 68 | synthesis/: 130 | sources/: 223 | projects/: 13
- Stub concepts (≤15 lines): 6 (was 8 — grpo.md deleted [alias redirect], word-cloud-communication.md deleted [zero incoming links])
  - beta, delta, epsilon, gamma, zeta, legal-accountability-stub
  - Greek stubs (5): kept, frontmatter upgraded to full schema (were missing created/updated/type/summary/status/confidence)
- .bak files: 0 (was 44 — bulk deleted 2026-05-26 per dashboard directive)
- No new broken links detected (0 broken-ref patterns)
- 852 pages have ## Connections sections (strong linking culture)

### MCP Tools Available ✓
MCP server confirmed reachable for this cycle. `wiki_lint`, `wiki_hits_analysis`, `wiki_cluster_pages` all functional.

### GoodRobot Duality (UNCHANGED — Ty decision still needed)
- `wiki/entities/projects/goodrobot.md` — SHUT DOWN (May 18), zero-human company simulating governance
- `wiki/projects/projects 1/goodrobot.md` — Active (May 13), SMB plug-and-play agent teams
- Both are `type: entity` — different writeups of same company from different angles
- Additional related files in projects/projects 1/: gtm-strategy.md, research-pipeline.md, technical-architecture.md
- Also: wiki/synthesis/news/goodrobot-revenue-model.md (another angle)
- Priority: MEDIUM — storage redundancy, no functional breakage

### Stub Concepts (8 files — low priority)
Minimal content (≤15 lines each). Not critical issues but low informational value. Candidates for merge/expand/delete review.

### .bak Files (44 files — Ty decision needed)
45+ days accumulated. Each represents an in-place overwrite. No functional impact but storage housekeeping. Suggested: selective restore review or bulk delete of pre-2026 .bak files.

## Open

1. **GoodRobot multi-location** — 5 files across 3 vault locations (entities/, projects/projects 1/, synthesis/) for same entity — needs Ty consolidation decision
2. ~~44 .bak files~~ — RESOLVED: bulk deleted per dashboard directive
3. **8 stub concepts** — low-value minimal pages — needs expand/merge/delete decision
4. **85 broken links** — teaching examples in operating docs + genuine missing refs — needs Ty decision
5. **252 orphans** — high count expected given operational files (agent-sheets) and daily reports; genuine orphans are mostly news/headlines reports and discovery reports (time-stamped, not linked after creation)

## Heading

- MCP tools: available this cycle (previously unavailable in cron context)
- No remediation delegated this cycle — open items are all Ty-decision items
- Ready for kanban surfacing per kanban-review skill
