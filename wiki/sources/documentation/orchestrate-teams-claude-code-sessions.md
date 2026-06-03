
---
created: 2026-05-29
updated: 2026-05-29
type: source
summary: "Claude Code experimental agent teams feature: multiple Claude instances coordinated by a lead, with shared task lists, direct inter-agent messaging, and independent context windows."
tags: [claude-code, agent-teams, orchestration, multi-agent, documentation]
sources: https://code.claude.com/docs/en/agent-teams
status: active
confidence: 1.0
---

# Orchestrate Teams of Claude Code Sessions

## Overview

Claude Code v2.1.32+ supports experimental **agent teams** — multiple Claude Code instances coordinated by a lead session. Teammates work independently with their own context windows and communicate directly with each other via a shared task list.

## Architecture

| Component | Description |
|-----------|-------------|
| **Team Lead** | Coordinates work, assigns tasks, synthesizes results |
| **Teammates** | Independent Claude instances, own context window |
| **Shared Task List** | Self-coordinating work queue, teammates claim tasks |
| **Direct Messaging** | Teammates communicate without routing through lead |

## Comparison with Subagents

| | Subagents | Agent Teams |
|--|-----------|-------------|
| Context | Results return to caller | Fully independent context windows |
| Communication | Report to main agent only | Teammates message each other directly |
| Coordination | Main agent manages all work | Shared task list with self-coordination |
| Best for | Focused tasks, results matter | Complex work requiring discussion |
| Token cost | Lower (summarized results) | Higher (separate Claude instances) |

## Best Use Cases
- **Research and review**: parallel investigation, shared findings
- **New modules/features**: independent pieces without conflicts
- **Debugging with competing hypotheses**: parallel theory testing
- **Cross-layer coordination**: frontend/backend/tests owned separately

## When NOT to Use
- Sequential tasks
- Same-file edits
- Highly coupled dependencies

## Setup

Enable via environment variable or `settings.json`:
```json
{
  "env": {
    "CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS": "1"
  }
}
```

## Display Modes
- **In-process**: All teammates in main terminal, Shift+Down to cycle
- **Split panes**: Each teammate in own pane (tmux/iTerm2)

## Known Limitations
- Session resumption issues
- Task coordination edge cases
- Shutdown behavior problems

## Connections
- [[claude-code]] — parent entity
- [[multi-agent-orchestration]] — related orchestration pattern
- [[agent-teams]] — related concept

## See Also
- [[claude-code-subagents]] — alternative parallelization pattern
