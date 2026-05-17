---
updated: 2026-05-17T17:55:40Z
created: 2026-05-17T17:55:40Z
---

---
created: 2026-05-17T11:00:00Z
updated: 2026-05-17T11:00:00Z
type: source
summary: Custom subagents in Claude Code are Markdown files with YAML frontmatter — specialize behavior with focused prompts, restrict tools, and route tasks to faster/cheaper models. Scope options: project (.claude/agents/), user (~/.claude/agents/), or plugin.
tags: [claude-code, subagents, delegation, multi-agent, context-management]
sources: https://code.claude.com/docs/en/sub-agents
status: reference
confidence: 0.95
---

## Core Insight

Subagents are specialized AI assistants defined as Markdown files with YAML frontmatter, enabling task-specific behavior with constrained tools and independent context windows. They preserve main-conversation context by keeping exploration and implementation in isolated sessions, returning only summaries.

## Key Claims

| Feature | Detail |
|---------|--------|
| **Built-in subagents** | Explore (Haiku, read-only), Plan, General-purpose |
| **Tool restrictions** | Subagents can be denied Write/Edit tools — enforce constraints |
| **Scope priority** | Managed settings > CLI flag > .claude/agents/ > ~/.claude/agents/ > Plugin |
| **Context savings** | Exploration stays in subagent context; main conversation stays clean |
| **Cost control** | Route to Haiku (fast/cheap) for appropriate tasks |
| **/agents command** | Interactive tabbed UI for managing subagents (Library + Running tabs) |
| **Agent teams** | For sessions that communicate with each other |
| **Background agents** | For parallel independent sessions monitored from one place |

## Connections

- [[delegation]] — subagents are a form of delegation
- [[hermes-agent]] — Hermes has similar subagent delegation capabilities
- [[claude-code]] — parent platform for subagent feature
