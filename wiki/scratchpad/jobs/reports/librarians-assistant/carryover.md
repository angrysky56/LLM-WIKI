---
created: 2026-06-30
updated: 2026-07-01
type: carryover
summary: Librarians-assistant carryover — 15 nested sources fixed, republican-party-duplicate deleted, 0 true broken links in core dirs
tags: [librarians-assistant, carryover]
---

# Librarians-Assistant Carryover — 2026-07-01

## Established

### Broken Link Count (Core Dirs)
- **Before**: 4 broken links — all known false positives (template examples in `synapse-llm-wiki-operating-guide.md`: `slug#section-name`, `concepts/foo`, `wiki/concepts/foo.md`, `scratchpad/jobs/sheet`)
- **After**: 0 true broken links ✓

### Ghost Wikilink Elimination
- 15 pages had `sources: [[wikilink1]], [[wikilink2]]` — the double-bracket YAML list created ghost wikilinks that the filesystem scanner flagged as broken
- All 15 targets already existed as body wikilinks — reduced to `sources: []` to eliminate spurious links without losing coverage

### Stub Deletion
- `republican-party-duplicate.md` (synthesis/) — deleted (duplicate stub, no unique content)
- Updated `republican-party.md` connections to remove the dangling reference

## What Was Fixed
- 15 nested sources syntax fixes (wiki/concepts × 12, wiki/entities/projects × 2, wiki/synthesis × 1)
- Deleted `republican-party-duplicate.md` + patched `republican-party.md` reference
- Verified goodrobot.md has no CEO/CFO/CTO/CMO wikilinks (plain text, not broken links)

## What Remains
1. **149 cross-directory deferred pairs** (synthesis→concepts/entities/sources) — large scope, low urgency
2. **147 orphans** — news/arxiv pages; ephemeral by nature, not actionable
3. **795 non-reciprocal pairs** — reciprocal link audit; efficiency gate per carryover
4. **Top authority pages need depth** — efhf, maximum-occupancy-principle, project-synapse, edm-framework

## Hard Blockers
- None — all open items are scoped deferred work, no blocking issues

## Heading
- Continue cross-directory reconciliation when bandwidth allows