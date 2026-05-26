---
name: insights
description: "Daily Zettelkasten insight generation — run CLI insight engine, create wiki pages for confidence>=0.7 insights, integrate to wiki. Schedule: 06:00 AM."
tags: [insights, zettelkasten, synthesis, daily]
triggers:
  - cron: "0 6 * * *"
  - manual: delegate_task
updated: 2026-05-25
created_by: agent
---

# insights — Zettelkasten Insight Generator

Run the Zettelkasten insight generation engine and integrate high-confidence insights (≥0.7) into the wiki as synthesis pages.

## See Also

- `references/workflow.md` — 6-step insight generation workflow
- `references/insight-merge.md` — how to create wiki pages from insights

## Quick Start

1. Load the `insights` skill
2. Run insight generation CLI (defense-in-depth: 580s shell timeout → 540s app → SIGALRM)
3. Read generated insights from `data/insights/latest.md` and `latest.json`
4. Create wiki page for each insight with confidence ≥ 0.7
5. Rebuild wiki index
6. Record to episodic memory via `synapse_remember`
7. Deliver (silent if no new pages created)

## Defense-in-Depth Timeout

```bash
cd /home/ty/Repositories/ai_workspace/project-synapse-mcp && \
    timeout --kill-after=10s 580s uv run python scripts/generate_insights.py \
    --topic general --print --max-runtime 540 2>&1
```

**Do NOT use MCP `generate_insights()`** — it times out at 300s.

## Quality Standards

- Only create pages for confidence ≥ 0.7
- Use slug mapping (e.g., `Titans Memory Architecture` → `titans-memory-efficiency-insight`)
- Frontmatter: type=synthesis, status=active, confidence from insight
- Tag with: insights, zettelkasten, {topic}