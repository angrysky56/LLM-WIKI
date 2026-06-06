---
agent: overseer
schema: carryover-v1
generated: 2026-06-06
cycle: 9
---

## CarryoverState

### Established
- **Cross-agent coordination is broken** — agents do not see each other's kanban cards, no shared state.
- **Carryover system is fully stubbed** — all 8 agent sheets have `carryover.md` with `Initialized` placeholder text, zero real cycle data.
- **Researcher cycle 8 was a clean run** — 0 refusals, 4 pages promoted/created, concept/authority boundaries recognized.
- **Librarian + librarians-assistant progressed** — stub count down from 92 to 51, but 45 still remain.
- **News agent drifts from RSS mandate** — hardcodes URLs (NYT/Politico/WaPo) instead of running terminal RSS discovery.
- **Insights output ballooned to 73K** — surface area is too large; 2 of 3 generated insights were lost.
- **Ingest agent finds nothing to do** — schedule may be too frequent for the inflow rate.
- **Overseer's own `kanban_create` calls failed silently** — no `tenant` parameter meant cards went to caller's own queue.

### Open
- **[Q]** Which carryover files (in `wiki/agents/` or `wiki/scratchpad/agent-sheets/`) does `preflight.py` actually read? Both paths exist but the script's search order is unclear.
- **[Q]** Should the 51 → 0 stub reduction be done by `librarian` (depth + 4-level) or `librarians-assistant` (cluster-based) — or split: assistant handles merges, librarian handles depth?
- **[R]** `kanban_create` calls missing `tenant` field stranded cards in the caller's own queue — the Overseer logged this as `task current not found` repeatedly.
- **[R]** Insights agent output of 73K exceeds the practical response cap; cluster sampling may be dropping viable insights.

### Heading
- **[Intent]** Repopulate every agent's `carryover.md` with real cycle data, then verify preflight surfaces them.
- **[Intent]** Patch the Overseer SKILL.md to specify the `kanban_create` call contract (with `tenant`).
- **[Constraint]** Hard cap carryover at ~2000 chars; truncate Insights output at synthesis step before writing to disk.
