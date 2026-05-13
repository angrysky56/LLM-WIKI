---
title: "paperclipai/paperclip: Open-source orchestration for zero-human companies"
source: "https://github.com/paperclipai/paperclip"
author:
published:
created: 2026-05-11
description: "Open-source orchestration for zero-human companies - paperclipai/paperclip"
tags:
  - "clippings"
---
[![Paperclip — runs your business](https://github.com/paperclipai/paperclip/raw/master/doc/assets/header.png)](https://github.com/paperclipai/paperclip/blob/master/doc/assets/header.png)

[**Quickstart**](#quickstart) · [**Docs**](https://paperclip.ing/docs) · [**GitHub**](https://github.com/paperclipai/paperclip) · [**Discord**](https://discord.gg/m4HZY7xNG3) · [**Twitter**](https://x.com/papercliping)

## What is Paperclip?

## Open-source orchestration for zero-human companies

**If OpenClaw is an *employee*, Paperclip is the *company***

Paperclip is a Node.js server and React UI that orchestrates a team of AI agents to run a business. Bring your own agents, assign goals, and track your agents' work and costs from one dashboard.

It looks like a task manager — but under the hood it has org charts, budgets, governance, goal alignment, and agent coordination.

**Manage business goals, not pull requests.**

|  | Step | Example |
| --- | --- | --- |
| **01** | Define the goal | *"Build the #1 AI note-taking app to $1M MRR."* |
| **02** | Hire the team | CEO, CTO, engineers, designers, marketers — any bot, any provider. |
| **03** | Approve and run | Review strategy. Set budgets. Hit go. Monitor from the dashboard. |

> **COMING SOON: Clipmart** — Download and run entire companies with one click. Browse pre-built company templates — full org structures, agent configs, and skills — and import them into your Paperclip instance in seconds.

| **Works   with** | <sub>OpenClaw</sub> | <sub>Claude Code</sub> | <sub>Codex</sub> | <sub>Cursor</sub> | <sub>Bash</sub> | <sub>HTTP</sub> |
| --- | --- | --- | --- | --- | --- | --- |

*If it can receive a heartbeat, it's hired.*

## Paperclip is right for you if

- ✅ You want to build **autonomous AI companies**
- ✅ You **coordinate many different agents** (OpenClaw, Codex, Claude, Cursor) toward a common goal
- ✅ You have **20 simultaneous Claude Code terminals** open and lose track of what everyone is doing
- ✅ You want agents running **autonomously 24/7**, but still want to audit work and chime in when needed
- ✅ You want to **monitor costs** and enforce budgets
- ✅ You want a process for managing agents that **feels like using a task manager**
- ✅ You want to manage your autonomous businesses **from your phone**

## Features

| ### 🔌 Bring Your Own Agent  Any agent, any runtime, one org chart. If it can receive a heartbeat, it's hired. | ### 🎯 Goal Alignment  Every task traces back to the company mission. Agents know *what* to do and *why*. | ### 💓 Heartbeats  Agents wake on a schedule, check work, and act. Delegation flows up and down the org chart. |
| --- | --- | --- |
| ### 💰 Cost Control  Monthly budgets per agent. When they hit the limit, they stop. No runaway costs. | ### 🏢 Multi-Company  One deployment, many companies. Complete data isolation. One control plane for your portfolio. | ### 🎫 Ticket System  Every conversation traced. Every decision explained. Full tool-call tracing and immutable audit log. |
| ### 🛡️ Governance  You're the board. Approve hires, override strategy, pause or terminate any agent — at any time. | ### 📊 Org Chart  Hierarchies, roles, reporting lines. Your agents have a boss, a title, and a job description. | ### 📱 Mobile Ready  Monitor and manage your autonomous businesses from anywhere. |

## Problems Paperclip solves

| Without Paperclip | With Paperclip |
| --- | --- |
| ❌ You have 20 Claude Code tabs open and can't track which one does what. On reboot you lose everything. | ✅ Tasks are ticket-based, conversations are threaded, sessions persist across reboots. |
| ❌ You manually gather context from several places to remind your bot what you're actually doing. | ✅ Context flows from the task up through the project and company goals — your agent always knows what to do and why. |
| ❌ Folders of agent configs are disorganized and you're re-inventing task management, communication, and coordination between agents. | ✅ Paperclip gives you org charts, ticketing, delegation, and governance out of the box — so you run a company, not a pile of scripts. |
| ❌ Runaway loops waste hundreds of dollars of tokens and max your quota before you even know what happened. | ✅ Cost tracking surfaces token budgets and throttles agents when they're out. Management prioritizes with budgets. |
| ❌ You have recurring jobs (customer support, social, reports) and have to remember to manually kick them off. | ✅ Heartbeats handle regular work on a schedule. Management supervises. |
| ❌ You have an idea, you have to find your repo, fire up Claude Code, keep a tab open, and babysit it. | ✅ Add a task in Paperclip. Your coding agent works on it until it's done. Management reviews their work. |

## Why Paperclip is special

Paperclip handles the hard orchestration details correctly.

|  |  |
| --- | --- |
| **Atomic execution.** | Task checkout and budget enforcement are atomic, so no double-work and no runaway spend. |
| **Persistent agent state.** | Agents resume the same task context across heartbeats instead of restarting from scratch. |
| **Runtime skill injection.** | Agents can learn Paperclip workflows and project context at runtime, without retraining. |
| **Governance with rollback.** | Approval gates are enforced, config changes are revisioned, and bad changes can be rolled back safely. |
| **Goal-aware execution.** | Tasks carry full goal ancestry so agents consistently see the "why," not just a title. |
| **Portable company templates.** | Export/import orgs, agents, and skills with secret scrubbing and collision handling. |
| **True multi-company isolation.** | Every entity is company-scoped, so one deployment can run many companies with separate data and audit trails. |

## What's Under the Hood

Paperclip is a full control plane, not a wrapper. Before you build any of this yourself, know that it already exists:

```
┌──────────────────────────────────────────────────────────────┐
│                       PAPERCLIP SERVER                       │
│                                                              │
│  ┌───────────┐  ┌───────────┐  ┌───────────┐  ┌───────────┐  │
│  │Identity & │  │  Work &   │  │ Heartbeat │  │Governance │  │
│  │  Access   │  │   Tasks   │  │ Execution │  │& Approvals│  │
│  └───────────┘  └───────────┘  └───────────┘  └───────────┘  │
│                                                              │
│  ┌───────────┐  ┌───────────┐  ┌───────────┐  ┌───────────┐  │
│  │ Org Chart │  │Workspaces │  │  Plugins  │  │  Budget   │  │
│  │ & Agents  │  │ & Runtime │  │           │  │ & Costs   │  │
│  └───────────┘  └───────────┘  └───────────┘  └───────────┘  │
│                                                              │
│  ┌───────────┐  ┌───────────┐  ┌───────────┐  ┌───────────┐  │
│  │ Routines  │  │ Secrets & │  │ Activity  │  │  Company  │  │
│  │& Schedules│  │  Storage  │  │ & Events  │  │Portability│  │
│  └───────────┘  └───────────┘  └───────────┘  └───────────┘  │
└──────────────────────────────────────────────────────────────┘
         ▲              ▲              ▲              ▲
   ┌─────┴─────┐  ┌─────┴─────┐  ┌─────┴─────┐  ┌─────┴─────┐
   │  Claude   │  │   Codex   │  │   CLI     │  │ HTTP/web  │
   │   Code    │  │           │  │  agents   │  │   bots    │
   └───────────┘  └───────────┘  └───────────┘  └───────────┘
```

### The Systems

| **Identity & Access** — Two deployment modes (trusted local or authenticated), board users, agent API keys, short-lived run JWTs, company memberships, invite flows, and OpenClaw onboarding. Every mutating request is traced to an actor. | **Org Chart & Agents** — Agents have roles, titles, reporting lines, permissions, and budgets. Adapter examples match the diagram: Claude Code, Codex, CLI agents such as Cursor/Gemini/bash, HTTP/webhook bots such as OpenClaw, and external adapter plugins. If it can receive a heartbeat, it's hired. |
| --- | --- |
| **Work & Task System** — Issues carry company/project/goal/parent links, atomic checkout with execution locks, first-class blocker dependencies, comments, documents, attachments, work products, labels, and inbox state. No double-work, no lost context. | **Heartbeat Execution** — DB-backed wakeup queue with coalescing, budget checks, workspace resolution, secret injection, skill loading, and adapter invocation. Runs produce structured logs, cost events, session state, and audit trails. Recovery handles orphaned runs automatically. |
| **Workspaces & Runtime** — Project workspaces, isolated execution workspaces (git worktrees, operator branches), and runtime services (dev servers, preview URLs). Agents work in the right directory with the right context every time. | **Governance & Approvals** — Board approval workflows, execution policies with review/approval stages, decision tracking, budget hard-stops, agent pause/resume/terminate, and full audit logging. You're the board — nothing ships without your sign-off. |
| **Budget & Cost Control** — Token and cost tracking by company, agent, project, goal, issue, provider, and model. Scoped budget policies with warning thresholds and hard stops. Overspend pauses agents and cancels queued work automatically. | **Routines & Schedules** — Recurring tasks with cron, webhook, and API triggers. Concurrency and catch-up policies. Each routine execution creates a tracked issue and wakes the assigned agent — no manual kick-offs needed. |
| **Plugins** — Instance-wide plugin system with out-of-process workers, capability-gated host services, job scheduling, tool exposure, and UI contributions. Extend Paperclip without forking it. | **Secrets & Storage** — Instance and company secrets, encrypted local storage, provider-backed object storage, attachments, and work products. Sensitive values stay out of prompts unless a scoped run explicitly needs them. |
| **Activity & Events** — Mutating actions, heartbeat state changes, cost events, approvals, comments, and work products are recorded as durable activity so operators can audit what happened and why. | **Company Portability** — Export and import entire organizations — agents, skills, projects, routines, and issues — with secret scrubbing and collision handling. One deployment, many companies, complete data isolation. |

## What Paperclip is not

|  |  |
| --- | --- |
| **Not a chatbot.** | Agents have jobs, not chat windows. |
| **Not an agent framework.** | We don't tell you how to build agents. We tell you how to run a company made of them. |
| **Not a workflow builder.** | No drag-and-drop pipelines. Paperclip models companies — with org charts, goals, budgets, and governance. |
| **Not a prompt manager.** | Agents bring their own prompts, models, and runtimes. Paperclip manages the organization they work in. |
| **Not a single-agent tool.** | This is for teams. If you have one agent, you probably don't need Paperclip. If you have twenty — you definitely do. |
| **Not a code review tool.** | Paperclip orchestrates work, not pull requests. Bring your own review process. |

## Quickstart

Open source. Self-hosted. No Paperclip account required.

```
npx paperclipai onboard --yes
```

That quickstart path now defaults to trusted local loopback mode for the fastest first run. To start in authenticated/private mode instead, choose a bind preset explicitly:

```
npx paperclipai onboard --yes --bind lan
# or:
npx paperclipai onboard --yes --bind tailnet
```

If you already have Paperclip configured, rerunning `onboard` keeps the existing config in place. Use `paperclipai configure` to edit settings.

Or manually:

```
git clone https://github.com/paperclipai/paperclip.git
cd paperclip
pnpm install
pnpm dev
```

This starts the API server at `http://localhost:3100`. An embedded PostgreSQL database is created automatically — no setup required.

> **Requirements:** Node.js 20+, pnpm 9.15+

## FAQ

**What does a typical setup look like?** Locally, a single Node.js process manages an embedded Postgres and local file storage. For production, point it at your own Postgres and deploy however you like. Configure projects, agents, and goals — the agents take care of the rest.

If you're a solo-entreprenuer you can use Tailscale to access Paperclip on the go. Then later you can deploy to e.g. Vercel when you need it.

**Can I run multiple companies?** Yes. A single deployment can run an unlimited number of companies with complete data isolation.

**How is Paperclip different from agents like OpenClaw or Claude Code?** Paperclip *uses* those agents. It orchestrates them into a company — with org charts, budgets, goals, governance, and accountability.

**Why should I use Paperclip instead of just pointing my OpenClaw to Asana or Trello?** Agent orchestration has subtleties in how you coordinate who has work checked out, how to maintain sessions, monitoring costs, establishing governance - Paperclip does this for you.

(Bring-your-own-ticket-system is on the Roadmap)

**Do agents run continuously?** By default, agents run on scheduled heartbeats and event-based triggers (task assignment, @-mentions). You can also hook in continuous agents like OpenClaw. You bring your agent and Paperclip coordinates.

## Development

```
pnpm dev              # Full dev (API + UI, watch mode)
pnpm dev:once         # Full dev without file watching
pnpm dev:server       # Server only
pnpm build            # Build all
pnpm typecheck        # Type checking
pnpm test             # Cheap default test run (Vitest only)
pnpm test:watch       # Vitest watch mode
pnpm test:e2e         # Playwright browser suite
pnpm db:generate      # Generate DB migration
pnpm db:migrate       # Apply migrations
```

`pnpm test` does not run Playwright. Browser suites stay separate and are typically run only when working on those flows or in CI.

See [doc/DEVELOPING.md](https://github.com/paperclipai/paperclip/blob/master/doc/DEVELOPING.md) for the full development guide.

## Roadmap

- ✅ Plugin system (e.g. add a knowledge base, custom tracing, queues, etc)
- ✅ Get OpenClaw / claw-style agent employees
- ✅ companies.sh - import and export entire organizations
- ✅ Easy AGENTS.md configurations
- ✅ Skills Manager
- ✅ Scheduled Routines
- ✅ Better Budgeting
- ✅ Agent Reviews and Approvals
- ✅ Multiple Human Users
- ⚪ Cloud / Sandbox agents (e.g. Cursor / e2b agents)
- ⚪ Artifacts & Work Products
- ⚪ Memory / Knowledge
- ⚪ Enforced Outcomes
- ⚪ MAXIMIZER MODE
- ⚪ Deep Planning
- ⚪ Work Queues
- ⚪ Self-Organization
- ⚪ Automatic Organizational Learning
- ⚪ CEO Chat
- ⚪ Cloud deployments
- ⚪ Desktop App

This is the short roadmap preview. See the full roadmap in [ROADMAP.md](https://github.com/paperclipai/paperclip/blob/master/ROADMAP.md).

## Community & Plugins

Find Plugins and more at [awesome-paperclip](https://github.com/gsxdsm/awesome-paperclip)

## Telemetry

Paperclip collects anonymous usage telemetry to help us understand how the product is used and improve it. No personal information, issue content, prompts, file paths, or secrets are ever collected. Private repository references are hashed with a per-install salt before being sent.

Telemetry is **enabled by default** and can be disabled with any of the following:

| Method | How |
| --- | --- |
| Environment variable | `PAPERCLIP_TELEMETRY_DISABLED=1` |
| Standard convention | `DO_NOT_TRACK=1` |
| CI environments | Automatically disabled when `CI=true` |
| Config file | Set `telemetry.enabled: false` in your Paperclip config |

## Contributing

We welcome contributions. See the [contributing guide](https://github.com/paperclipai/paperclip/blob/master/CONTRIBUTING.md) for details.

## Community

- [Discord](https://discord.gg/m4HZY7xNG3) — Join the community
- [Twitter / X](https://x.com/papercliping) — Follow updates and announcements
- [GitHub Issues](https://github.com/paperclipai/paperclip/issues) — bugs and feature requests
- [GitHub Discussions](https://github.com/paperclipai/paperclip/discussions) — ideas and RFC

## License

MIT © 2026 Paperclip

## Star History

[![Star History Chart](https://camo.githubusercontent.com/64f78e8e86f4256f7eb143a84857c66f0d226cabca7553a3e78adaf9e484dd5e/68747470733a2f2f6170692e737461722d686973746f72792e636f6d2f696d6167653f7265706f733d7061706572636c697061692f7061706572636c697026747970653d64617465266c6567656e643d746f702d6c656674)](https://www.star-history.com/?repos=paperclipai%2Fpaperclip&type=date&legend=top-left)

---

[![](https://github.com/paperclipai/paperclip/raw/master/doc/assets/footer.jpg)](https://github.com/paperclipai/paperclip/blob/master/doc/assets/footer.jpg)

<sub>Open source under MIT. Built for people who want to run companies, not babysit agents.</sub>