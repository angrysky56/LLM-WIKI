---
agent: overseer
schema: carryover-v1
generated: 2026-06-08
cycle: 11
---

## CarryoverState

### Established
- **Cycle 11 (June 8, 9:10am)** ran preflight.py with fallback — 8 cron jobs scanned via raw jobs.json, 6 ok, 1 paused (ingest), 1 errored (insights)
- **Reports directory updated** — `wiki/scratchpad/agent-sheets/overseer/reports/2026-06-08.md` written
- **1 kanban card spawned** — `t_37fa793c`: insights recovery (3 stranded insights from errored run)
- **Preflight.py HERMES_HOME bug** persists — fallback works but is manual; no fix deployed this cycle

### Open
- **[Q]** Insights recovery card `t_37fa793c` — needs verification next cycle that 3 synthesis pages were created
- **[Q]** Raw inbox: `Toolsets Reference Hermes Agent.md` — should ingest pipeline be re-enabled or handled manually?
- **[Q]** Librarians-assistant reports "no kanban tasks found" for its profile — is the routing working correctly?
- **[R]** Preflight.py still broken — if the system Hermes home changes, the fallback reads will break too

### Heading
- **[Intent]** Next cycle: verify insights recovery completion, check for new raw/ files, re-evaluate ingest pipeline pause
- **[Intent]** Consider patching preflight.py to read from the system-level hermes home or use `hermes cron list` CLI