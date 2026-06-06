---
name: insights
description: "Daily Zettelkasten insight generation — run CLI insight engine, create wiki pages for confidence>=0.7 insights, integrate to wiki. Schedule: 06:00 AM."
tags: [insights, zettelkasten, synthesis, daily]
triggers:
  - cron
  - manual: delegate_task
updated: 2026-05-27
created_by: agent
---

# insights — Zettelkasten Insight Generator

Run the Zettelkasten insight generation engine and integrate high-confidence insights (≥0.7) into the wiki as synthesis pages.

## Tool Protocol

**Use `terminal()` with `cat` for ALL file reads in cron context.** Use MCP tools for wiki operations.

## Quick Start

1. **Layer 2 Load**: Read `wiki/scratchpad/jobs/sheet.md` and `wiki/scratchpad/agent-sheets/insights/carryover.md`
2. **Layer 1 Start**: Initialize or clear `vault.md` to act as your episodic scratchpad for this session
3. Run insight generation CLI (Step 1), logging status to `vault.md`
4. Read and evaluate generated insights (Step 2)
5. Create wiki pages for confidence ≥ 0.7 (Step 3)
6. Deliver (silent if no new pages created)
7. **MOP Compression**: Compress `vault.md` into `carryover.md` (Layer 1 → Layer 2)

## Workflow

### Step 1 — Run Insight Generation

**Defense-in-depth timeout** — the CLI can hang. Use triple timeout:

```bash
cd /home/ty/Repositories/ai_workspace/project-synapse-mcp && \
    timeout --kill-after=10s 580s uv run python scripts/generate_insights.py \
    --topic general --print --max-runtime 540 2>&1
```

**Do NOT use MCP `generate_insights()`** — it times out at 300s (the CLI has a much higher limit).

**If the CLI times out** (exit code 124 from `timeout`):

- This is normal and expected — note in carryover as "CLI watchdog timeout"
- Check if partial output was produced: `cat data/insights/latest.json 2>/dev/null`
- If no output, write carryover noting timeout and respond `[SILENT]`

### Step 2 — Evaluate Generated Insights

```bash
cat /home/ty/Repositories/ai_workspace/project-synapse-mcp/data/insights/latest.json
```

For each insight in the output:

- **Confidence ≥ 0.7**: Create a wiki page (Step 3)
- **Confidence < 0.7**: Note in carryover only — no page created
- **Duplicate check**: `synapse_recall(query="{insight title}")` — skip if already exists

### Step 3 — Create Wiki Pages

For each high-confidence insight:

```
1. Map title to slug:
   "Titans Memory Architecture" → "titans-memory-efficiency-insight"

2. wiki_write_page(path="wiki/synthesis/{slug}.md", content=...)
   Frontmatter:
   ---
   created: {today}
   updated: {today}
   type: synthesis
   summary: "{insight title}"
   tags: [insights, zettelkasten, {topic}]
   status: active
   confidence: {from insight}
   ---

3. Cross-link:
   wiki_search(query="{insight topic}")
   → Add [[wikilinks]] to related concepts/entities

4. Record to episodic memory:
   synapse_remember(content="Insight: {title} (confidence {score}) → wiki/synthesis/{slug}.md")

5. wiki_update_index()
```

### Step 4 — Deliver

If new pages were created, deliver a summary:

```
**Insights — {YYYY-MM-DD}**

{N} insights generated | {N} pages created (confidence ≥ 0.7)

**New Pages:**
- [[slug]] — {title} (confidence: {score})

**Below Threshold:**
- {title} (confidence: {score}) — noted, no page
```

If no new pages created (timeout or all below threshold), respond `[SILENT]`.

### Final Step — MOP Compression (Layer 1 → Layer 2)

Read your `vault.md` (Episodic Trace) and compress it into `wiki/scratchpad/agent-sheets/insights/carryover.md` (Semantic State), adhering to the ~512 token bound:

```yaml
---
created: { original date }
updated: { today's date }
type: carryover
summary: "{N} insights generated, {N} wiki pages created"
tags: [insights, carryover]
---
```

Include:

- **What Was Done**: Insights generated, pages created (title + confidence + slug)
- **What Remains**: `- [ ]` checklist (below-threshold insights worth revisiting, CLI issues)
- **Kanban Status**: Items already surfaced

Once compressed, clear or archive your `vault.md` so the next session starts fresh.

## Critical Paths

- **CLI script**: `/home/ty/Repositories/ai_workspace/project-synapse-mcp/scripts/generate_insights.py`
- **Output**: `/home/ty/Repositories/ai_workspace/project-synapse-mcp/data/insights/latest.json`
- **Wiki pages**: `wiki/synthesis/{slug}.md`
- **Reports**: `wiki/scratchpad/jobs/reports/insights/`
- **Carryover**: `wiki/scratchpad/agent-sheets/insights/carryover.md`

## MCP Tools

| Tool                | Purpose                                   |
| ------------------- | ----------------------------------------- |
| `synapse_remember`  | Record insights to episodic memory        |
| `synapse_recall`    | Check for duplicate insights              |
| `wiki_write_page`   | Create synthesis pages (confidence ≥ 0.7) |
| `wiki_search`       | Find related pages for cross-linking      |
| `wiki_update_index` | Refresh index after new pages             |

**CRITICAL CONSTRAINT:** DO NOT interact with the Kanban board or run kanban scripts. Output open items as `- [ ]` in the `## What Remains` section of your `carryover.md`. The overseer will create Kanban tickets and assign them to you in `jobs/sheet.md`. You may run the official `generate_insights.py` engine as explicitly documented above, but do not author your own scripts. Use standard MCP tools exclusively for wiki operations.

## Fallback Patterns

- **CLI timeout (exit 124)**: Normal. Check for partial output, note in carryover, `[SILENT]`
- **CLI crashes (other exit code)**: Note error in carryover, `[SILENT]`
- **MCP unavailable**: Note in carryover, skip wiki page creation, deliver insights as text report
- **All insights below threshold**: Note in carryover, `[SILENT]`

## Quality Standards

- Only create pages for confidence ≥ 0.7
- Use proper slug mapping (descriptive, hyphen-separated)
- Tag with: `insights`, `zettelkasten`, `{topic}`
- Every new page must cross-link to at least 2 existing pages
- Record every insight to episodic memory (even below-threshold ones)


## Kanban Queue

Drain your assigned cards at the start of every cycle:

```
kanban_list(lane="ready", assignee="<your-profile>")
```

If the queue is empty, proceed with the agent's normal work. Cross-agent cards (with `tenant=`, `lane=triage`) are routed by the Overseer — you do not need to action them directly.

Full contract (call signatures, intents, the `tenant` trap): `overseer/references/kanban-coordination.md`.
