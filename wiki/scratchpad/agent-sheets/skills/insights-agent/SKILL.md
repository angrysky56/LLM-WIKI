---
created: 2026-05-24T00:00:00Z
updated: 2026-05-24T00:00:00Z
type: skill
summary: Agent skill — Wiki Insights Generator via Zettelkasten, runs daily at 06:00 AM
tags: [agent-skill, skill, insights, zettelkasten]
sources: 
status: active
confidence: 0.9
---

# Insights Agent

**Wiki root:** `/home/ty/Documents/LLM-WIKI`  
**Synapse MCP server:** `project-synapse-mcp` at `/home/ty/Repositories/ai_workspace/project-synapse-mcp`

---

## Overview

The Insights Agent runs Zettelkasten autonomous insight generation and integrates results into the LLM-WIKI. It executes daily at 06:00 AM via Hermes cron.

---

## MCP Tools

**Available in active MCP session:** `debug_test`, `wiki_write_page`, `wiki_search`, `wiki_lint`, `synapse_remember`, `wiki_update_index`

**NOT available in cron context:** All MCP tools are deferred — the Synapse MCP server runs in the `project-synapse-mcp` venv, not `hermes-agent`'s python. Do NOT attempt to call them in cron.

---

## Bootstrap

1. Read this skill file (done)
2. Read the agent sheet: `wiki/scratchpad/agent-sheets/insights.md`
3. Execute the workflow per the agent sheet

---

## MCP Availability Check

**CRITICAL:** `synapse_mcp` is installed in the `project-synapse-mcp` venv, NOT the `hermes-agent` venv. Cron runs under `hermes-agent`'s python.

```bash
/home/ty/Repositories/ai_workspace/project-synapse-mcp/.venv/bin/python3 -c "from synapse_mcp.zettelkasten.insight_engine import InsightEngine; print('OK')" 2>/dev/null && echo "MCP OK" || echo "MCP UNAVAILABLE"
```

If MCP is available, use `debug_test` to confirm, then proceed.

---

## Workflow

### Phase 1: Generate Insights

Run the CLI via `timeout` wrapper (NOT the MCP tool — it times out at 300s):

**CRITICAL:** Use the shell `timeout` wrapper as the outermost layer. Defense-in-depth:
- Shell `timeout` (580s SIGTERM, 590s SIGKILL) — outermost
- App `--max-runtime 540` — soft cap via `asyncio.wait_for`
- App SIGALRM watchdog at `max_runtime + 30s` — hard cap for blocking numpy/networkx

```bash
cd /home/ty/Repositories/ai_workspace/project-synapse-mcp && \
    timeout --kill-after=10s 580s uv run python scripts/generate_insights.py \
    --topic general --print --max-runtime 540 2>&1
```

**Exit codes:** `0` = success, `3` = timeout exceeded (file may still be valid), `1` = init failure.

> **Exit code 3 is expected and not a failure.** The hard watchdog fires at 570s when the LLM synthesis phase takes longer than the soft cap. Output files (`latest.md`, `latest.json`) are written incrementally and are valid. Proceed to Phase 2 immediately — do not re-run.

This takes ~10 minutes on a healthy run.

### Phase 2: Read Results

After completion, read both output files to understand what was generated:

- `/home/ty/Repositories/ai_workspace/project-synapse-mcp/data/insights/latest.md` (human-readable summary)
- `/home/ty/Repositories/ai_workspace/project-synapse-mcp/data/insights/latest.json` (structured data with evidence chains)

### Phase 3: Integrate Insights into Wiki

For each insight with `confidence >= 0.7`:

1. Create synthesis page at `wiki/synthesis/insights/<slug>.md`
2. Frontmatter: `created`, `updated`, `type=synthesis`, `summary` (one-line from title), `tags=[insights, zettelkasten, <topic>]`, `sources=[derived from evidence]`, `status=active`, `confidence`
3. Body: title (`## heading`), content paragraph, evidence section

**Slug mapping:** Insight Title → `lower-hyphen-insight`, e.g. `Titans Memory Architecture` → `titans-memory-efficiency-insight`

### Phase 4: Index

**Cron environment note:** MCP tools (`wiki_update_index()`, `synapse_remember()`) are unavailable in a cron context because the Synapse MCP server runs in the `project-synapse-mcp` venv, not `hermes-agent`'s python. Do NOT attempt to call them — they will fail or hang.

Workaround: After creating pages:
1. Verify pages exist on disk (`ls wiki/synthesis/insights/`)
2. Record open items in carryover for manual follow-up in an active MCP session

### Phase 5: Episodic Memory

**Deferred in cron.** Cannot call `synapse_remember()` — MCP context unavailable. After pages are created, add to carryover:

```
### Open
- Run wiki_update_index() + synapse_remember() for N new insight pages (in active MCP session)
```

The episodic memory recording must be done manually or by a follow-up agent running in an active MCP session.

---

## Key Paths

```
Wiki root:              /home/ty/Documents/LLM-WIKI
Insight output:         /home/ty/Repositories/ai_workspace/project-synapse-mcp/data/insights/latest.md
JSON data:              /home/ty/Repositories/ai_workspace/project-synapse-mcp/data/insights/latest.json
Insight pages:         /home/ty/Documents/LLM-WIKI/wiki/synthesis/insights/
Agent sheet:           wiki/scratchpad/agent-sheets/insights.md
Carryover:             wiki/scratchpad/jobs/reports/insights/carryover.md
Synapse MCP location:  /home/ty/Repositories/ai_workspace/project-synapse-mcp
```

---

## Confidence Threshold

**Only create pages for insights with `confidence >= 0.7`.** Lower-confidence insights should be noted in carryover but not integrated as pages.

---

## Delivery Rules

- No insights generated or all below threshold 0.7: `[SILENT]`
- 1+ pages created: brief summary → deliver to origin
- CLI failure: report what failed and carry open items to next cycle

---

## See Also

- Agent sheet: `wiki/scratchpad/agent-sheets/insights.md`
- Insights catalog entry: `wiki/agents/skills/index.md` (section: Wiki Insights Generator)