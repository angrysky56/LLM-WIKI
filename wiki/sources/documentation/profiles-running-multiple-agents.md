---
updated: 2026-05-17T17:56:51Z
created: 2026-05-17T17:56:51Z
---

---
created: 2026-05-17T11:00:00Z
updated: 2026-05-17T11:00:00Z
type: source
summary: Hermes profiles — independent agent instances on the same machine, each with own config, API keys, memory, skills, and gateway. Created via hermes profile create, accessed via command aliases like `coder chat`.
tags: [hermes-agent, profiles, multi-agent, configuration]
sources: https://hermes-agent.nousresearch.com/docs/user-guide/profiles
status: reference
confidence: 0.95
---

## Core Insight

Hermes profiles are completely isolated agent instances sharing the same binary but with separate ~/.hermes/profiles/<name>/ directories. Each gets its own config.yaml, .env, SOUL.md, memories, sessions, skills, cron jobs, and state. Create with `hermes profile create <name>` which auto-creates command aliases like `<name> chat`, `<name> setup`, `<name> gateway start`.

## Key Claims

| Clone Option | What Gets Copied |
|-------------|-----------------|
| `--clone` (default) | config.yaml, .env, SOUL.md only (fresh sessions/memory) |
| `--clone-all` | Everything — full snapshot including memories, sessions, cron jobs |
| `--clone --clone-from <other>` | Clone config from specific profile |

When Honcho is enabled, `--clone` also creates a dedicated AI peer for the new profile sharing the same user workspace.

## Connections

- [[hermes-agent]] — parent system
- [[delegation]] — profiles complement but differ from subagent delegation
