---
title: "gsd-build/get-shit-done: A light-weight and powerful meta-prompting, context engineering and spec-driven development system for Claude Code by TÂCHES."
source: "https://github.com/gsd-build/get-shit-done"
author:
published:
created: 2026-05-11
description: "A light-weight and powerful meta-prompting, context engineering and spec-driven development system for Claude Code by TÂCHES. - gsd-build/get-shit-done"
tags:
  - "clippings"
---
## GET SHIT DONE

**English** · [Português](https://github.com/gsd-build/get-shit-done/blob/main/README.pt-BR.md) · [简体中文](https://github.com/gsd-build/get-shit-done/blob/main/README.zh-CN.md) · [日本語](https://github.com/gsd-build/get-shit-done/blob/main/README.ja-JP.md) · [한국어](https://github.com/gsd-build/get-shit-done/blob/main/README.ko-KR.md)

**A light-weight meta-prompting, context engineering, and spec-driven development system for Claude Code, OpenCode, Gemini CLI, Kilo, Codex, Copilot, Cursor, Windsurf, and more.**

**Solves context rot — the quality degradation that happens as your AI fills its context window.**

```
npx get-shit-done-cc@latest
```

**Works on Mac, Windows, and Linux.**

[![GSD Install](https://github.com/gsd-build/get-shit-done/raw/main/assets/terminal.svg)](https://github.com/gsd-build/get-shit-done/blob/main/assets/terminal.svg)

*"If you know clearly what you want, this WILL build it for you. No bs."*

*"I've done SpecKit, OpenSpec and Taskmaster — this has produced the best results for me."*

*"By far the most powerful addition to my Claude Code. Nothing over-engineered. Literally just gets shit done."*

**Trusted by engineers at Amazon, Google, Shopify, and Webflow.**

---

> [!important] Important
> **Returning to GSD?**
> 
> Run `/gsd-map-codebase` to re-index your codebase, then `/gsd-new-project` to rebuild GSD's planning context. Your code is fine — GSD just needs its context rebuilt. See the [CHANGELOG](https://github.com/gsd-build/get-shit-done/blob/main/CHANGELOG.md) for what's new.

---

## Why I Built This

I'm a solo developer. I don't write code — Claude Code does.

Other spec-driven tools exist, but they're all built for 50-person engineering orgs — sprint ceremonies, story points, stakeholder syncs, Jira workflows. I'm not that. I'm a creative person trying to build great things consistently.

So I built GSD. The complexity is in the system, not in your workflow. Behind the scenes: context engineering, XML prompt formatting, subagent orchestration, state management. What you see: a few commands that just work.

The system gives Claude everything it needs to do the work *and* verify it. I trust the workflow. It just does a good job.

— **TÂCHES**

---

## How It Works

The loop is six commands. Each one does exactly one thing.

### 1\. Initialize

```
/gsd-new-project
```

Questions → research → requirements → roadmap. You approve it, then you're ready to build.

> **Already have code?** Run `/gsd-map-codebase` first. It analyzes your stack, architecture, and conventions so `/gsd-new-project` asks the right questions.

### 2\. Discuss

```
/gsd-discuss-phase 1
```

Your roadmap has a sentence per phase. That's not enough to build it the way *you* imagine it. Discuss captures your decisions before anything gets planned: layouts, API shapes, error handling, data structures — whatever gray areas exist for this specific phase.

The output feeds directly into research and planning. Skip it, get reasonable defaults. Use it, get your vision.

### 3\. Plan

```
/gsd-plan-phase 1
```

Research → plan → verify, in a loop until the plans pass. Each plan is small enough to execute in a fresh context window.

### 4\. Execute

```
/gsd-execute-phase 1
```

Plans run in parallel waves. Each executor gets a fresh 200k-token context. Each task gets its own atomic commit. Walk away, come back to completed work with a clean git history.

Your main context window stays at 30–40%. The work happens in the subagents.

### 5\. Verify

```
/gsd-verify-work 1
```

Walk through what was built. Anything broken gets a diagnosed fix plan — ready for immediate re-execution. You don't debug manually; you just run execute again.

### 6\. Repeat → Ship

```
/gsd-ship 1
/gsd-complete-milestone
/gsd-new-milestone
```

Loop discuss → plan → execute → verify → ship until the milestone is done. Then archive, tag, and start the next one fresh.

---

## Getting Started

```
npx get-shit-done-cc@latest
```

The installer prompts for your runtime (Claude Code, OpenCode, Gemini CLI, Kilo, Codex, Copilot, Cursor, Windsurf, and more) and whether to install globally or locally.

```
claude --dangerously-skip-permissions
```

GSD is built for frictionless automation. Skip-permissions is how it's intended to run.

See **[docs/USER-GUIDE.md](https://github.com/gsd-build/get-shit-done/blob/main/docs/USER-GUIDE.md)** for the full walkthrough, non-interactive install flags for all 15 runtimes, minimal install (`--minimal`), Docker setup, and permissions configuration.

---

## Commands

The main loop:

| Command | What it does |
| --- | --- |
| `/gsd-new-project` | Questions → research → requirements → roadmap |
| `/gsd-discuss-phase [N]` | Capture implementation decisions before planning |
| `/gsd-plan-phase [N]` | Research + plan + verify |
| `/gsd-execute-phase <N>` | Execute plans in parallel waves |
| `/gsd-verify-work [N]` | Manual acceptance testing |
| `/gsd-ship [N]` | Create PR from verified phase work |
| `/gsd-progress --next` | Auto-detect and run the next step |
| `/gsd-complete-milestone` | Archive milestone and tag release |
| `/gsd-new-milestone` | Start next version |

For ad-hoc tasks, autonomous mode, codebase analysis, forensics, and the full command surface — see **[docs/COMMANDS.md](https://github.com/gsd-build/get-shit-done/blob/main/docs/COMMANDS.md)**.

---

## Why It Works

Three things most AI-coding setups get wrong:

**1\. Context bloat.** As a session grows, quality degrades. GSD keeps your main context clean by doing the heavy work in fresh subagent contexts. Researchers, planners, and executors each start fresh with exactly what they need.

**2\. No shared memory.** GSD maintains structured artifacts that survive session boundaries: `PROJECT.md` (vision), `REQUIREMENTS.md` (scope), `ROADMAP.md` (where you're going), `STATE.md` (current position and decisions), `CONTEXT.md` (per-phase implementation decisions). Every new session loads these and knows exactly where things stand.

**3\. No verification.** Code that "runs" isn't code that "works." GSD's verify step walks you through what was built, diagnoses failures with dedicated debug agents, and generates fix plans before you declare a phase done.

See **[docs/ARCHITECTURE.md](https://github.com/gsd-build/get-shit-done/blob/main/docs/ARCHITECTURE.md)** for how the multi-agent orchestration and context engineering work in detail.

---

## Configuration

Settings live in `.planning/config.json`. Configure during `/gsd-new-project` or update with `/gsd-settings`.

Key dials:

| Setting | What it controls |
| --- | --- |
| `mode` | `interactive` (confirm each step) or `yolo` (auto-approve) |
| Model profiles | `quality` / `balanced` / `budget` — controls which model each agent uses |
| `workflow.research` / `plan_check` / `verifier` | Toggle the quality agents that add tokens and time |
| `parallelization.enabled` | Run independent plans simultaneously |

For the full configuration reference — all settings, git branching strategies, per-runtime model overrides, workstream config inheritance, agent skills injection — see **[docs/CONFIGURATION.md](https://github.com/gsd-build/get-shit-done/blob/main/docs/CONFIGURATION.md)**.

---

## Documentation

| Doc | What's in it |
| --- | --- |
| [User Guide](https://github.com/gsd-build/get-shit-done/blob/main/docs/USER-GUIDE.md) | End-to-end walkthrough, install options, all runtime flags, configuration reference |
| [Commands](https://github.com/gsd-build/get-shit-done/blob/main/docs/COMMANDS.md) | Every command with flags and examples |
| [Configuration](https://github.com/gsd-build/get-shit-done/blob/main/docs/CONFIGURATION.md) | Full config schema, model profiles, git branching |
| [Architecture](https://github.com/gsd-build/get-shit-done/blob/main/docs/ARCHITECTURE.md) | How the multi-agent orchestration works |
| [CLI Tools](https://github.com/gsd-build/get-shit-done/blob/main/docs/CLI-TOOLS.md) | `gsd-sdk query` and programmatic SDK dispatch seams |
| [Features](https://github.com/gsd-build/get-shit-done/blob/main/docs/FEATURES.md) | Complete feature index |
| [Changelog](https://github.com/gsd-build/get-shit-done/blob/main/CHANGELOG.md) | What changed in each release |

---

## Troubleshooting

**Commands not showing up?** Restart your runtime after install. GSD installs to `~/.claude/skills/gsd-*/` (Claude Code), `~/.codex/skills/gsd-*/` (Codex), or the equivalent for your runtime.

**Something broken?** Re-run the installer — it's idempotent:

```
npx get-shit-done-cc@latest
```

**Containers or Docker?** Set `CLAUDE_CONFIG_DIR` before installing to avoid tilde-expansion issues:

```
CLAUDE_CONFIG_DIR=/home/youruser/.claude npx get-shit-done-cc --global
```

Full troubleshooting and uninstall instructions in **[docs/USER-GUIDE.md](https://github.com/gsd-build/get-shit-done/blob/main/docs/USER-GUIDE.md#troubleshooting)**.

---

## Community

| Project | Platform |
| --- | --- |
| [gsd-opencode](https://github.com/rokicool/gsd-opencode) | Original OpenCode port |
| [Discord](https://discord.gg/mYgfVNfA2r) | Community support |

---

## Star History

[

![Star History Chart](https://camo.githubusercontent.com/7dd96c0bf87a45304ff893d3280cb88546481e51119beb239349b3b0f319b7c9/68747470733a2f2f6170692e737461722d686973746f72792e636f6d2f7376673f7265706f733d6773642d6275696c642f6765742d736869742d646f6e6526747970653d44617465)

](https://star-history.com/#gsd-build/get-shit-done&Date)

---

## License

MIT License. See [LICENSE](https://github.com/gsd-build/get-shit-done/blob/main/LICENSE) for details.

---

**Claude Code is powerful. GSD makes it reliable.**