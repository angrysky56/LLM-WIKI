---
title: "AI-Powered BRD & PRD Generator"
source: "https://www.clearlyreqs.com/blog/hermes-agent-team-gateway-best-practices"
author:
  - "[[Clearly]]"
published: 2026-05-15
created: 2026-05-22
description: "Generate professional BRDs and PRDs in minutes with AI. Clearly's intelligent wizard guides you from idea to complete requirements document. Free trial."
tags:
  - "clippings"
---
HMAI & Development

TL;DR

Team gateways need deliberate choices across **security isolation**, **authorization**, **profiles**, **skills**, **memory**, **MCP governance**, **terminal backends**, **cron**, and **observability**. Layer controls—no single switch is enough—and keep updating: security fixes ship frequently.

## 1\. Gateway architecture for teams

The messaging gateway is not a thin proxy: it caches `AIAgent` instances per session, preserves Anthropic prompt cache across turns, routes approvals, and manages hygiene. Multi-platform mode shares memory and configuration unless you isolate with **profiles**.

| Platform | Setup | Voice | Groups | Best for |
| --- | --- | --- | --- | --- |
| Telegram | Low | Full | Yes | Fast 24/7 team rollout |
| Discord | Medium | Full | Yes | Engineering teams, roles |
| Slack | Medium | Limited | Yes | Corporate integrations |
| WhatsApp | Medium | Full | No | Individual / mobile-first |
| Signal | Low | Full | No | Privacy-focused individuals |

Run `hermes gateway add <platform>` per surface, then `hermes gateway start`. Adapters reconnect independently—partial outage on one channel should not kill the others.

## 2\. Security hardening

Treat production gateways like privileged automation: **authorization**, **approvals**, **container isolation**, **secrets hygiene**, and **network policy** stack together.

### 2.1 Never use GATEWAY\_ALLOW\_ALL\_USERS

Prefer **static allowlists** for tiny stable teams, or **DM pairing** for growth: users request a code, admins run `hermes pairing approve …`. Codes expire (~1 hour), rate limits apply, and repeated failures can lock the platform temporarily.

```
hermes pairing list
hermes pairing revoke telegram 987654321
hermes pairing clear-pending
```

### 2.2 Approval modes

| Mode | Behavior | Use case |
| --- | --- | --- |
| manual (default) | Prompt on risky commands | Maximum safety; can backlog under load |
| smart | Risk-ranked auto approve/deny/prompt | Balanced production default |
| off | No checks (YOLO) | CI/disposable sandboxes only |

### 2.3 Terminal backends

Do **not** run production gateways on `local` backend. Prefer Docker with hardened flags and empty `docker_forward_env` unless you explicitly scope secrets.

```
docker:
  backend: docker
  docker_image: "nikolaik/python-nodejs:python3.11-nodejs20"
  docker_forward_env: []
  container_cpu: 1
  container_memory: 5120
  container_disk: 51200
  container_persistent: true
```

For execution on another host while the gateway stays DMZ-safe:

```
terminal:
  backend: ssh
  persistent_shell: true

# ~/.hermes/.env — never commit
TERMINAL_SSH_HOST=agent-worker.local
TERMINAL_SSH_USER=hermes
TERMINAL_SSH_KEY=~/.ssh/hermes_agent_key
```

### 2.4 Credentials and MCP env

Keep secrets in `~/.hermes/.env` at mode `0600`. MCP subprocesses receive filtered env—declare only what each server needs.

```
mcp_servers:
  github:
    command: "npx"
    args: ["-y", "@modelcontextprotocol/server-github"]
    env:
      GITHUB_PERSONAL_ACCESS_TOKEN: "ghp_..."
```

### 2.5 Website blocklist

```
security:
  website_blocklist:
    enabled: true
    domains:
      - "*.internal.company.com"
      - "admin.example.com"
```

### 2.6 Production checklist (samples)

| # | Check | Verify |
| --- | --- | --- |
| 1 | Explicit allowlists | hermes pairing list |
| 2 | Docker backend | hermes config get terminal.backend → docker |
| 3 | Resource limits | container\_\* defined |
| 4 | Secrets chmod | ~/.hermes/.env is -rw------- |
| 5 | No open gateway | No GATEWAY\_ALLOW\_ALL\_USERS=true |
| 6 | Non-root gateway | whoami ≠ root |
| 7 | Logs | journalctl -u hermes-gateway |
| 8 | Patches | hermes update within ~7 days |

## 3\. Profiles and distributions

Profiles isolate config, env, memory, and skills. Clone a golden profile per role or user; ship standards via git-backed **profile distributions** (`hermes profile install …`). `auth.json` and `.env` stay local.

```
hermes profile list
hermes profile create NAME --clone
hermes profile use NAME
hermes profile export NAME
hermes profile install https://github.com/your-org/hermes-team.git
```

| Pattern | Structure | When |
| --- | --- | --- |
| Shared gateway | Single default profile | Small tight teams |
| Role-based | devops / backend / frontend | Different toolsets |
| Environment-based | prod / staging / dev | Different risk tiers |
| User-isolated | Per-user profiles | Personal memory on shared host |
| Hybrid | Base distribution + overlays | Org standards + personalization |

## 4\. Skills at scale

Progressive disclosure keeps token cost manageable (~600 tokens for dozens of skills in the index). Share read-only trees via `external_dirs`; agent writes land under `~/.hermes/skills/` (local overrides win).

```
skills:
  external_dirs:
    - /opt/hermes-team-skills
    - /home/shared/project-skills
  guard_agent_created: true   # review before auto-saving workflows
```

Run the **Curator** on a cadence: grade, prune low scores, consolidate duplicates (`hermes curator run --dry-run` first).

## 5\. Memory and context

Built-in `MEMORY.md` (~2.2k chars) and `USER.md` (~1.375k chars) snapshot into the system prompt at session start—updates mid-session apply next boot. On shared gateways, facts blend across teammates unless you adopt profiles or external memory.

**Mem0** is recommended for multi-user semantic recall with user scoping:

```
memory:
  provider: mem0
  mem0:
    api_key: "${MEM0_API_KEY}"
    user_id_field: "platform_user_id"
```

Compression pairs **gateway session hygiene** (~85% window) with **ContextCompressor** (~50% threshold): prune stale tool blobs, protect recent tail, summarize the middle with an auxiliary model.

```
compression:
  enabled: true
  threshold: 0.50
  target_ratio: 0.20
  protect_last_n: 20
```

For Anthropic, keep the system prefix stable to preserve prompt cache; Hermes uses a `system_and_3` caching strategy—mutating the system block every turn defeats savings.

## 6\. MCP governance

MCP servers run external code and may trigger nested LLM calls—cap sampling budgets and whitelist tools.

```
mcp_servers:
  github:
    command: "npx"
    args: ["-y", "@modelcontextprotocol/server-github"]
    tools:
      include: [list_issues, create_issue, update_issue, search_code]
      exclude: [delete_repository]
      resources: false
      prompts: false
```

Reload MCP without bouncing the gateway: `hermes mcp reload`.

## 7\. Terminal backend matrix

| Backend | Isolation | Best for |
| --- | --- | --- |
| local | None | Dev laptops only |
| docker | Namespaces + caps | Default production gateway |
| ssh | Network boundary | Gateway DMZ + internal workers |
| modal | Cloud VM | Ephemeral compute |
| daytona | Cloud container | Hibernating sandboxes |
| vercel\_sandbox | MicroVM | Vercel-centric workflows |
| singularity | HPC-style | Shared clusters |

## 8\. Cron and automation

Gateway cron checks every ~60 seconds; jobs spawn fresh agents, optionally attach skills, and deliver to a channel.

```
hermes cron add "every day at 9am" \
  --task "Generate daily progress report from memory" \
  --deliver telegram

hermes cron add "0 9 * * 1-5" \
  --task "Weekly team summary" \
  --deliver slack
```

## 9\. Workspace directories

| Context | Default CWD | Override |
| --- | --- | --- |
| CLI | Where you launched | cd first |
| Messaging gateway | ~ | MESSAGING\_CWD in.env |
| Docker / SSH | Home inside target | TERMINAL\_CWD |

```
MESSAGING_CWD=/home/hermes/gateway-workspace
```

## 10\. Observability

Structured logs live under `~/.hermes/logs/` with redaction. Enable Langfuse via the bundled observability plugin for trace-level cost and latency insight.

```
hermes plugins enable observability/langfuse

# ~/.hermes/.env
HERMES_LANGFUSE_PUBLIC_KEY=pk-lf-...
HERMES_LANGFUSE_SECRET_KEY=sk-lf-...
HERMES_LANGFUSE_BASE_URL=https://cloud.langfuse.com
```

## 11\. 24/7 service management

```
sudo hermes gateway install --system
sudo hermes gateway start --system

# Multiple installs via HERMES_HOME
export HERMES_HOME=/opt/hermes-prod
```

## 12\. Context files

| File | Role | Notes |
| --- | --- | --- |
| .hermes.md / HERMES.md | Project instructions (high priority) | Walk to git root |
| AGENTS.md | Architecture / conventions | CWD + children |
| CLAUDE.md | Claude Code parity | Discovery alongside AGENTS |
| .cursorrules | Cursor parity | CWD only |
| SOUL.md | Voice / tone | HERMES\_HOME only |

## 13\. Multi-agent patterns

Use `delegate_task` for parallel research branches or separate implement vs validate loops—each subagent gets its own thread and tooling context.

## 14\. Maintenance discipline

```
hermes --version
hermes update
hermes config check
hermes config migrate
sudo hermes gateway restart --system
```

| Cadence | Task |
| --- | --- |
| Daily | Scan gateway logs |
| Weekly | hermes curator run; review pairing queue |
| Monthly | Update + migrate config |
| Quarterly | Full security checklist replay |

## 15\. Summary matrix

| Dimension | Recommendation |
| --- | --- |
| Platform | Telegram first; add Discord for engineering |
| Authorization | DM pairing + admin approval |
| Approvals | smart for production throughput |
| Terminal | Docker + empty docker\_forward\_env |
| Secrets | .env 0600; never bulk-forward env |
| Profiles | Base distribution + personal overlays |
| Skills | external\_dirs + Curator |
| Memory | Mem0 when multi-user recall matters |
| MCP | Tool filters + sampling caps |
| Observability | Langfuse + log alerts |
| Updates | Weekly hermes update habit |

Layered security only works with operational hygiene—review pairing lists, prune skills, patch promptly, and monitor logs. Compounding agent value (skills + memory + cron) depends on that foundation.

Condensed from `docs/hermes-agents-best-practice.html`. Verify commands against your Hermes version. For framework trade-offs see [OpenClaw vs Hermes Agent](https://www.clearlyreqs.com/blog/openclaw-vs-hermes-agent).