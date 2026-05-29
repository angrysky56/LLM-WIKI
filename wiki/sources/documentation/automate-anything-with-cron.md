---
updated: 2026-05-17T17:55:38Z
created: 2026-05-17T17:55:38Z
---

---
created: 2026-05-17T11:00:00Z
updated: 2026-05-17T11:00:00Z
type: source
summary: Five real-world Hermes cron automation patterns — website monitoring, weekly reports, GitHub watchers, data pipelines, and multi-skill workflows. Key trick: [SILENT] suppresses delivery when nothing noteworthy happens.
tags: [hermes-agent, cron, automation, monitoring, scripting, workflow]
sources: https://hermes-agent.nousresearch.com/docs/guides/automate-with-cron
status: reference
confidence: 0.95
---

## Core Insight

Cron jobs in Hermes run in fresh, self-contained sessions with no memory of previous conversations. The critical pattern: include `[SILENT]` in the prompt to suppress delivery when nothing happens, and use the `--script` parameter to handle mechanical work (fetching, diffing, state) before the LLM reasoning layer runs.

## Key Claims

| Pattern | Description |
|---------|-------------|
| **Website Monitor** | Python script fetches+hashes URL, diffs against state; agent analyzes change only when detected |
| **Weekly Report** | Web search + GitHub trending + HN API → formatted digest, delivered to Telegram/Discord |
| **GitHub Watcher** | `gh issue/pr list` filtered to last 6 hours; [SILENT] if nothing new |
| **Data Pipeline** | Script collects data (prices, etc.) to JSONL; agent analyzes trends, alerts on significant moves |
| **Multi-Skill Workflow** | Chain skills (`--skill arxiv --skill obsidian`) — arxiv teaches paper search, obsidian teaches note-writing |
| **[SILENT] trick** | When agent's response contains `[SILENT]`, delivery is suppressed — only notify on real changes |
| **Script parameter** | Python script stdout becomes context for the agent; script handles mechanical work |
| **Delivery targets** | `origin`, `local`, `telegram`, `discord`, `slack`, or specific chat/thread |

## Connections
- [[wiki/index]]
- [[sources/documentation/automate-anything-with-cron]]
- [[automate-anything-with-cron]]

- [[hermes-agent]] — parent system with cron feature
- [[hermes-agent-skills]] — skills like arxiv, obsidian can be chained in cron workflows
