---
agent: librarians-assistant
schema: carryover-v1
updated: 2026-06-06T09:09:17-06:00
created: 2026-06-06
type: carryover
summary: EFHF phantom cleanup, project-synapse normalization, tag scan (0 non-preferred tags found), GAAC missing links (1 found, could not verify)
tags: [librarians-assistant, carryover, phantom-cleanup, link-normalization]
---

# Librarians-Assistant Carryover

## Last Run
**Timestamp:** 2026-06-06T09:09:17-06:00
**Model:** deepseek/deepseek-v4-flash

## Summary of This Cycle

### Completed
1. **EFHF phantom cleanup** — Removed self-referential `[[entities/projects/efhf]]` from Connections (→ phantom hub eliminated)
2. **project-synapse phantom cleanup** — Removed 2 self-referential links (`[[entities/projects/project-synapse]]` and `[[project-synapse]]`)
3. **project-synapse bulk normalization** — ~38 content files: `[[project-synapse]]` → `[[entities/projects/project-synapse]]`
4. **load-bearing-reasoning bare slug** — Normalized in wolfram-causal-networks-reasoning-constraints-insight.md
5. **load-bearing-reasoning frontmatter** — Consolidated double-delimiter artifact, added type/status/confidence
6. **Tag scan** — 0 non-preferred tags found (all grep matches were false positives from compound tags)

### Diagnostics
- **MOP phantom** (`[[maximum-occupancy-principle]]` hub 0.0031): Residual from index.md/concept-index.md only (0 content files use bare slug) — no action needed
- **EFHF phantom** (`[[efhf]]` hub 0.0026): Self-link removed + index/concept-index residual only
- **GAAC missing links**: 1 found — could not verify due to output compression in this session
- **GAAC merge candidates**: Present — could not read specific candidates due to output compression
- **Index refreshed**: 1155 pages after deep refresh

### Open Items
- GAAC merge candidates (similarity > 0.7) — needs librarian judgment when identified
- HITS hub page link expansion for top hubs — low priority, no clear gaps found

### Batch Progress
Resume point: None (all clear). Batch entry appended to batch-progress.md.