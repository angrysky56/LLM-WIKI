---
summary: Agent instructions for Wiki Insights Generator — runs Zettelkasten insight generation and integrates results into the wiki
tags: [agent-instructions, insights, zettelkasten]
updated: 2026-05-23
---

# Wiki Insights Generator — Agent Sheet

**Job ID**: `insights-gen`  
**Schedule**: Daily 06:00 AM (cron)  
**Delivery**: origin (Discord thread)

---

## Your Task

You are the insights curator for the LLM-WIKI. Your job is to:
1. Run the Zettelkasten insight generation engine
2. Integrate the resulting insights into the wiki as proper pages

**synapse MCP tools:** `debug_test`, `wiki_write_page`, `wiki_search`, `wiki_lint`, `synapse_remember`

---

## Workflow

### STEP 0 — Run the insight generation CLI

**Defense-in-depth timeout wrapper** — three layers protect against hanging:
1. Shell `timeout` (580s SIGTERM, 590s SIGKILL) — outermost
2. App `--max-runtime 540` — soft cap via `asyncio.wait_for`
3. App SIGALRM watchdog at `max_runtime + 30s` — hard cap for blocking numpy/networkx

```bash
cd /home/ty/Repositories/ai_workspace/project-synapse-mcp && \
    timeout --kill-after=10s 580s uv run python scripts/generate_insights.py \
    --topic general --print --max-runtime 540 2>&1
```

Exit codes: 0 = success, 3 = timeout exceeded (file may still be valid), 1 = init failure.

**Do NOT use the MCP `generate_insights()` tool** — it times out at 300s. Use the CLI script above.

---

### STEP 1 — Read the generated insights

After the script completes, read both:
- `/home/ty/Repositories/ai_workspace/project-synapse-mcp/data/insights/latest.md` (human-readable summary)
- `/home/ty/Repositories/ai_workspace/project-synapse-mcp/data/insights/latest.json` (structured data with evidence chains)

---

### STEP 2 — Create wiki pages from insights

For each insight with `confidence >= 0.7`:
1. Create a synthesis page at `wiki/synthesis/insights/<slug>.md`
2. Use the insight's title, content, topic, and evidence as the page body
3. Add frontmatter: created, updated, type=synthesis, summary (one-line from title), tags=[insights, zettelkasten, <topic>], sources=[derived from insight evidence], status=active, confidence (from insight)

**Slug mapping:** e.g. `Titans Memory Architecture` → `titans-memory-efficiency-insight`

---

### STEP 3 — Update the concept index

After creating insight pages, use `wiki_update_index()` to rebuild the wiki index so new pages are searchable.

---

### STEP 4 — Record to episodic memory

For each new insight page created, call `synapse_remember`:
- subject: "insight: {title}"
- predicate: "integrated_to_wiki"
- object: "wiki/synthesis/insights/<slug>.md"
- note: f"confidence={confidence}, pattern_type={pattern_type}, entity_count={entity_count}"

---

### STEP 5 — Write carryover

Save to `wiki/scratchpad/jobs/reports/insights/carryover.md`:
```
## Established
- Insights generated: N
- Pages created: N

## Open
- Any insights below threshold (confidence < 0.7): N
- Any CLI failures: [describe]

## Heading
- Next run priority
```

---

### STEP 6 — Deliver

If no new pages were created: `[SILENT]`
If pages created: brief summary of what was integrated