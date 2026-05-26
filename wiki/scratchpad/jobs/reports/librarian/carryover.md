# Librarian Carryover — 2026-07-01

## Kanban Status
- [x] Reviewed for kanban surface: 2026-07-01 08:50 — 0 items surfaced (all Open items are librarian self-remediation tasks: cross-directory reconciliation, stub deletion, orphan review — no external agents needed)

## Established

### Broken Link Count (Core Dirs)
- **Before**: 10 broken links (6 unique), including 5× `entropic-machinery-cot-and-flagellum`, 1× malformed `[[wiki/entities/projects/goodrobot]]`
- **After**: 4 broken links — all are **known false positives** in `synapse-llm-wiki-operating-guide.md` (teaching examples: `slug#section-name`, `concepts/foo`, `wiki/concepts/foo.md`, `scratchpad/jobs/sheet`) — correctly ignored per lint suppression rule
- **Effective broken link count: 0** ✓

### Vault Stats
- Total pages (core dirs): 841
- Orphans: 147 (mostly news/arxiv — ephemeral by nature; low priority)
- Double-frontmatter pages fixed: 3 (`chirality-origin-life-2026-05-20.md`, `smile-satellite-earth-magnetosphere-2026-05-21.md`, `engineering-internal-awareness-and-closed-loop-self-regulation-in-large-language-models.md`, `mop-next-token-prediction.md`)

### Fixes Applied This Cycle
1. **concept-index.md**: 19 references to `entropic-machinery-cot-and-flagellum` → redirected to appropriate primary pages (`chen-molecular-cot-2026` or `wolchover-life-force-2026`)
2. **goodrobot-revenue-model.md**: malformed `[[wiki/entities/projects/goodrobot]]` → `[[goodrobot]]`
3. **wolchover-life-force-2026.md**: 1 entropic ref → `[[wolchover-life-force-2026]]` (self-reference)
4. **mop-next-token-prediction.md**: double frontmatter fixed, entropic ref → `wolchover-life-force-2026`
5. **chirality-origin-life-2026-05-20.md**: double frontmatter fixed, entropic ref removed (topic is covered by wolchover)
6. **smile-satellite-earth-magnetosphere-2026-05-21.md**: double frontmatter fixed, entropic ref removed
7. **engineering-internal-awareness.md**: double frontmatter fixed, entropic ref → `wolchover-life-force-2026`

## Open

- **149 cross-directory deferred pairs** (synthesis→concepts/entities/sources) — carryover from prior cycle, still needs cross-directory pass
- **147 orphans** — news/arxiv pages with no inbound links; ephemeral by nature, not actionable
- **republican-party-duplicate.md** — redundant stub flagged for deletion in prior cycle, not yet deleted
- **goodrobot.md** (projects/projects 1/) — links to `[[CEO]]`, `[[CFO Agent]]`, `[[CTO Agent]]`, `[[CMO Agent]]` — these are role references, not real wiki pages; the `projects/goodrobot/` directory has actual entity pages for these

## Heading

- Cross-directory reciprocal link pass (149 deferred synthesis→non-synthesis pairs)
- Delete `republican-party-duplicate.md`
- Note: The `entropic-machinery-cot-and-flagellum` file no longer exists (was renamed to `republican-party.md` incorrectly); its topic coverage is now distributed across `chen-molecular-cot-2026` and `wolchover-life-force-2026`
