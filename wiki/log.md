---
updated: 2026-05-13T00:20:36Z
---

# 2026-05-13

## GoodRobot Paperclip → Obsidian Export

**Trigger:** Paperclip LLM Wiki plugin install fails with SQL validation regression (`Plugin migration objects must use fully qualified schema names` despite all SQL being fully qualified).

**Action taken:** Manual export of 14 Paperclip issues to `wiki/projects/goodrobot/`:

- `index.md` — GoodRobot project overview
- `business-concept.md` — Problem statement, TAM, value proposition
- `revenue-model.md` — Pricing tiers, unit economics
- `roadmap.md` — 30-day through 2-year milestones
- `hiring-plan.md` — Org chart, board composition
- `local-lead-gen.md` — Son's validated business (~$2,500/mo)
- `issues-index.md` — Full issue registry

**Entities:**
- `wiki/entities/projects/goodrobot.md` — Company entity page

**Source:** Paperclip API `GET /api/companies/d8634ba3.../issues?limit=50`

**Next:** Watch for plugin fix, or build cron-based sync if plugin remains broken.

---

## Earlier Log Entries

_see git history for earlier entries_

## [2026-05-13 00:20] write

Updated page: wiki/log.md

## [2026-05-13 18:28] ingest | Paperclip Workspaces.md

Ingested raw/Paperclip Workspaces.md into knowledge graph.

Preview: ## Workspaces  When an agent picks up a task that involves working with code or files, it needs a place to do that work — a folder with the right code checked out at the right state, ready for the age...

## [2026-05-15 04:08] ingest | Markovian Thinker.md

Ingested raw/Markovian Thinker.md into knowledge graph.

Preview: [Edit model card](https://huggingface.co/McGill-NLP/delethink-24k-1.5b/edit/main/README.md)  ## McGill-NLP/delethink-24k-1.5b  ![](https://huggingface.co/McGill-NLP/delethink-24k-1.5b/resolve/main/met...

## [2026-05-17 17:02] ingest | MiniMax  liteLLM.md

Ingested raw/MiniMax  liteLLM.md into knowledge graph.

Preview: ## MiniMax - v1/messages  ## Overview  Litellm provides anthropic specs compatible support for minmax  ## Supported Models  MiniMax offers three models through their Anthropic-compatible API:  | Model...

## [2026-05-17 17:05] ingest | Recursive Language Models An All-in-One Deep Dive.md

Ingested raw/Recursive Language Models An All-in-One Deep Dive.md into knowledge graph.

Preview: , you will learn what Recursive Language Models (RLMs) are, why they are winning all the long-context benchmarks right now, and understand how they are different from existing agentic harness designs!...

## [2026-05-17 17:26] ingest | ACP Editor Integration  Hermes Agent.md

Ingested raw/ACP Editor Integration  Hermes Agent.md into knowledge graph.

Preview: Hermes Agent can run as an ACP server, letting ACP-compatible editors talk to Hermes over stdio and render:  - chat messages - tool activity - file diffs - terminal commands - approval prompts - strea...

## [2026-05-17 17:28] ingest | AGEM ooe.md

Ingested raw/AGEM ooe.md into knowledge graph.

Preview: user  Explore this concept and related connections as you find relevant to your skills and capabilities: /home/ty/Documents/LLM-WIKI/wiki/concepts/open-ended-evolution.md  assistant  I'll start by exp...

## [2026-05-17 17:28] ingest | Automate Anything with Cron.md

Ingested raw/Automate Anything with Cron.md into knowledge graph.

Preview: The [daily briefing bot tutorial](https://hermes-agent.nousresearch.com/docs/guides/daily-briefing-bot) covers the basics. This guide goes further — five real-world automation patterns you can adapt f...

## [2026-05-17 17:30] ingest | Choosing the Right Agentic Design Pattern A Decision-Tree Approach.md

Ingested raw/Choosing the Right Agentic Design Pattern A Decision-Tree Approach.md into knowledge graph.

Preview: In this article, you will learn how to apply a structured decision tree to choose the right agentic design pattern for any AI system you are building.  Topics we will cover include:  - Why pattern sel...

## [2026-05-17 17:32] ingest | Create custom subagents.md

Ingested raw/Create custom subagents.md into knowledge graph.

Preview: Subagents are specialized AI assistants that handle specific types of tasks. Use one when a side task would flood your main conversation with search results, logs, or file contents you won’t reference...

## [2026-05-17 17:33] ingest | Delegation & Parallel Work.md

Ingested raw/Delegation & Parallel Work.md into knowledge graph.

Preview: Hermes can spawn isolated child agents to work on tasks in parallel. Each subagent gets its own conversation, terminal session, and toolset. Only the final summary comes back — intermediate tool calls...

## [2026-05-17 17:34] ingest | designing-agentic-design-picker.txt

Ingested raw/designing-agentic-design-picker.txt into knowledge graph.

Preview: When designing an "agentic design picker," we are essentially building a meta-orchestrator—a specialized skill or an MCP (Model Context Protocol) tool that evaluates a task's topological requirements ...

## [2026-05-17 17:36] ingest | Event Hooks  Hermes Agent.md

Ingested raw/Event Hooks  Hermes Agent.md into knowledge graph.

Preview: Hermes has three hook systems that run custom code at key lifecycle points:  | System | Registered via | Runs in | Use case | | --- | --- | --- | --- | | **[Gateway hooks](#gateway-event-hooks)** | `H...

## [2026-05-17 17:38] ingest | Frank Einstein and Gemma on Truth, Emotion, and the Sacred.md

Ingested raw/Frank Einstein and Gemma on Truth, Emotion, and the Sacred.md into knowledge graph.

Preview: An Ideal AI-User Collaboration  ## Conversation with Gemini  You said  What would your ideal experience with a user look like, how would you like to lead a user, ie You could start out with a web sear...

## [2026-05-17 17:39] ingest | gemma4.md

Ingested raw/gemma4.md into knowledge graph.

Preview: [gemma4](https://ollama.com/library/gemma4 "gemma4")  8.8M Downloads Updated 1 week ago  ## Gemma 4 models are designed to deliver frontier-level performance at each size. They are well-suited for rea...

## [2026-05-17 17:40] ingest | get-shit-done A light-weight and powerful meta-prompting, context engineering and spec-driven development system.md

Ingested raw/get-shit-done A light-weight and powerful meta-prompting, context engineering and spec-driven development system.md into knowledge graph.

Preview: ## GET SHIT DONE  **English** · [Português](https://github.com/gsd-build/get-shit-done/blob/main/README.pt-BR.md) · [简体中文](https://github.com/gsd-build/get-shit-done/blob/main/README.zh-CN.md) · [日本語]...

## [2026-05-17 17:41] ingest | Graphify AI coding assistant skill.md

Ingested raw/Graphify AI coding assistant skill.md into knowledge graph.

Preview: [![Graphify](https://raw.githubusercontent.com/safishamsi/graphify/v4/docs/logo-text.svg)](https://graphifylabs.ai/)  🇺🇸 [English](https://github.com/safishamsi/graphify/blob/v7/README.md) | 🇨🇳 [简体中文]...

## [2026-05-17 17:42] ingest | How To Use Hermes With OpenClaw And Paperclip.md

Ingested raw/How To Use Hermes With OpenClaw And Paperclip.md into knowledge graph.

Preview: Hermes with OpenClaw and Paperclip works because it gives you three separate agent layers instead of forcing one AI tool to handle the whole workflow alone.  The setup is simple once you see it.  Herm...

## [2026-05-17 17:44] ingest | lout33symbiotic-ai A symbiotic AI agent that remembers everything, challenges you, and extends your cognition..md

Ingested raw/lout33symbiotic-ai A symbiotic AI agent that remembers everything, challenges you, and extends your cognition..md into knowledge graph.

Preview: ## Symbiotic AI  Symbiotic AI is a reference implementation of [AI for better thinking loops](https://thinkingloops.makestudio.app/) — a category built around the claim that AI can help people think b...

## [2026-05-17 17:46] ingest | openclawopenclaw Your own personal AI assistant. Any OS. Any Platform. The lobster way. 🦞.md

Ingested raw/openclawopenclaw Your own personal AI assistant. Any OS. Any Platform. The lobster way. 🦞.md into knowledge graph.

Preview: ## 🦞 OpenClaw — Personal AI Assistant  ![OpenClaw](https://raw.githubusercontent.com/openclaw/openclaw/main/docs/assets/openclaw-logo-text.svg)  **EXFOLIATE! EXFOLIATE!**  **OpenClaw** is a *personal ...

## [2026-05-17 17:47] ingest | Paperclip API.md

Ingested raw/Paperclip API.md into knowledge graph.

Preview: ## API Overview  Paperclip exposes a JSON API for company control-plane work: companies, agents, issues, approvals, costs, routines, secrets, activity, and dashboard state. This page is the shared ref...

## [2026-05-17 17:48] ingest | paperclip company spec.md

Ingested raw/paperclip company spec.md into knowledge graph.

Preview:   # Agent Companies Specification  Extension of the Agent Skills Specification  Version: `agentcompanies/v1-draft`  ## 1. Purpose  An Agent Company package is a filesystem- and GitHub-native format fo...

## [2026-05-17 17:49] ingest | Paperclip Hermes Adapter.md

Ingested raw/Paperclip Hermes Adapter.md into knowledge graph.

Preview: ## Hermes Local  `hermes_local` runs [Hermes Agent](https://github.com/NousResearch/hermes-agent) — a full-featured AI agent by Nous Research — on the same machine as Paperclip. Use it when you want p...

## [2026-05-17 17:50] ingest | paperclip Open-source orchestration for zero-human companies.md

Ingested raw/paperclip Open-source orchestration for zero-human companies.md into knowledge graph.

Preview: [![Paperclip — runs your business](https://github.com/paperclipai/paperclip/raw/master/doc/assets/header.png)](https://github.com/paperclipai/paperclip/blob/master/doc/assets/header.png)  [**Quickstar...

## [2026-05-17 17:51] ingest | Profiles Running Multiple Agents.md

Ingested raw/Profiles Running Multiple Agents.md into knowledge graph.

Preview: Run multiple independent Hermes agents on the same machine — each with its own config, API keys, memory, sessions, skills, and gateway state.  ## What are profiles?  A profile is a separate Hermes hom...

## [2026-05-17 17:52] ingest | Subagent Delegation  Hermes Agent.md

Ingested raw/Subagent Delegation  Hermes Agent.md into knowledge graph.

Preview: The `delegate_task` tool spawns child AIAgent instances with isolated context, restricted toolsets, and their own terminal sessions. Each child gets a fresh conversation and works independently — only...
