---
title: "I Switched from OpenClaw to Hermes Agent. Here’s What Nobody Told Me"
source: "https://medium.com/@sathishkraju/i-switched-from-openclaw-to-hermes-agent-heres-what-nobody-told-me-5f33a746b6ca"
author:
  - "[[Sathish Raju]]"
published: 2026-04-22
created: 2026-05-08
description: "More"
tags:
  - "clippings"
---
*Hermes Agent hit* ***110k*** *GitHub stars in ten weeks — the fastest-growing agent framework of 2026. Here’s what actually makes it different from OpenClaw, how the self-learning loop works, and when you should (and shouldn’t) switch.*

> Every developer who has used an AI coding assistant has experienced the same frustration. You spend an afternoon teaching your agent the quirks of your codebase — the naming conventions, the deployment pipeline, the legacy schema nobody documented. Then you close the session. When you open a new one, most of that context is gone. Two projects are attacking this problem from fundamentally different directions. Only one of them is designed to get better over time.

In this article

**PART2** of this article is here [https://medium.com/@sathishkraju/your-hermes-agent-has-no-performance-review-heres-how-to-fix-that-92254efdfe18](https://medium.com/@sathishkraju/your-hermes-agent-has-no-performance-review-heres-how-to-fix-that-92254efdfe18)

**PART3** of this article is here [https://medium.com/@sathishkraju/why-your-ai-agent-has-amnesia-and-how-hermes-agent-actually-fixes-it-9b5329992c0d](https://medium.com/@sathishkraju/why-your-ai-agent-has-amnesia-and-how-hermes-agent-actually-fixes-it-9b5329992c0d?postPublishedType=repub)

## The context: what’s happening in open-source agents right now

OpenClaw launched in late 2025 as a weekend project by Austrian developer Peter Steinberger. It became one of the fastest-growing open-source projects in GitHub history — 345,000 stars by early April 2026, a ClawHub marketplace with 13,000+ community skills, and integrations across 24 messaging platforms. It solved a real problem: self-hosted AI agents that connect to the apps developers already use, work with every major model provider, and give teams a way to automate workflows without vendor lock-in.

Then the security incidents hit. Nine CVEs in four days in March 2026, including one scoring CVSS 9.9. A supply chain audit of ClawHub found 341 malicious skills in an initial scan of 2,857 entries — roughly 12% malware rate. Security researchers found 135,000+ publicly exposed OpenClaw instances across 82 countries. Cisco called personal AI agents like OpenClaw “a security nightmare.”

Into this environment, Nous Research — the lab behind the Hermes, Nomos, and Psyche model families — shipped Hermes Agent on February 25, 2026. It made a completely different architectural bet.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*zknXhtvHfaHCKaJzVQuK2w.png)

## What Hermes Agent actually is

Hermes Agent is an open-source AI agent framework built around a single architectural principle: the agent should get better at your specific workflows over time. Not through fine-tuning or model updates — through a closed learning loop that runs after every task.

Most agent frameworks follow a fixed loop: receive task → plan → execute → return result. Session ends. Nothing is retained. The next task starts from the same baseline. Run the same type of task a hundred times in OpenClaw and the agent doesn’t get better at it — it approaches each one as a new problem.

Hermes adds a layer after execution. When it completes a complex task, it enters what Nous Research calls a “Reflective Phase.” It analyzes its own performance, extracts reusable patterns, and writes a new skill file encoding exactly how it solved that problem. ==The next time a similar task arrives, the agent queries its own skill library instead of reasoning from scratch.== The accumulated institutional knowledge compounds across sessions.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*Hrq9sV_lZc9uelWvCv1QDQ.jpeg)

OpenClaw & Hermes Agent

> ***The core architectural difference***
> 
> OpenClaw’s skills are human-written files distributed through ClawHub. You write them, review them, install them. Hermes’ skills are written by the agent itself from its own experience. Think of OpenClaw as an assistant who follows an instruction manual. Think of Hermes as an assistant who writes their own manual after finishing a task — so they do the job better next time.

## The closed learning loop — how Hermes gets smarter

The learning loop is the technical heart of Hermes and the reason it compounds in ways OpenClaw cannot. Three components make it work:

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*rpEaWZpuI_lh3SYsFO450w.png)

Fig. 1 — The Hermes closed learning loop. Every completed task feeds back into an expanding skill library. Future similar tasks skip re-reasoning and query existing skills — cutting task time by 40% on domain-similar tasks after 20+ skills are accumulated.

**Skill creation.** When Hermes completes a task successfully, it writes a markdown skill file encoding the exact steps it took. The format follows the agentskills.io open standard — the same spec used by Claude Code and Cursor — so skills are portable. Over time, the library grows from 118 bundled skills to hundreds of domain-specific ones created from the agent’s own experience.

**User modeling.** Hermes builds a persistent model of the user across sessions. Not just what tasks they assign, but how they prefer answers formatted, what level of detail they want, what past decisions they’ve made in similar situations, and which feedback signals they’ve given. This model carries forward. Over weeks, the agent stops asking for clarification on things it already knows.

**Self-evaluation.** After creating a new skill, Hermes runs an internal evaluation pass to test whether the skill generalizes cleanly or only applies to the specific instance that generated it. Skills that fail the evaluation are refined before being added to the library. This is what prevents the skill library from accumulating garbage over time.

## The three-layer memory system

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*PfZbSqwhQ7iDqdy2rcs6Dg.png)

As of v0.10.0, the memory system is fully pluggable. You can swap in third-party backends — Honcho, vector stores, or custom databases — via a plugin interface. Six third-party memory providers are supported out of the box. This is a deliberate architectural choice: Nous Research doesn’t want memory to become a lock-in point.

> **Important gotcha:** Self-learning is disabled by default. This trips up a lot of first-time users. You must explicitly enable persistent memory and skill generation in `~/.hermes/config.yaml`. If you skip this step, Hermes behaves like a standard single-session agent and the "grows with you" promise doesn't materialize.

## Getting started: setup and configuration

Hermes runs on anything from a $5 VPS to serverless infrastructure with virtually no idle costs — you only pay for LLM API calls when the agent is actively thinking. The total cost for a solo developer is typically $0.30 per complex task on budget models plus optional hosting.

```c
# Install Hermes Agent
pip install hermes-agent

# Or from source
git clone https://github.com/NousResearch/hermes-agent
cd hermes-agent && pip install -e .

# Initialize your workspace
hermes init ~/my-hermes-workspace
cd ~/my-hermes-workspace
```

The critical configuration step — enabling the learning loop:

```c
# ~/.hermes/config.toml — the most important file

[model]
provider = "anthropic"    # or openai, google, openrouter, etc.
model    = "claude-opus-4-5"
base_url = "https://api.anthropic.com"  # one line to switch providers

[memory]
enabled           = true     # REQUIRED — disabled by default
skill_generation  = true     # REQUIRED — enables the learning loop
user_modeling     = true     # builds persistent user profile
episodic_archive  = true     # SQLite FTS5 cold recall
backend           = "sqlite" # or "honcho", "pinecone", custom

[agent]
workspace         = "~/my-hermes-workspace"
skill_eval        = true     # validate skills before adding to library
max_skills        = 500      # cap before pruning low-use skills
reflection_depth  = "standard"  # "light" | "standard" | "deep"

[integrations]
slack    = false
discord  = false
telegram = false
```

## Migrating from OpenClaw

Hermes ships a migration tool that imports your OpenClaw persona, memory, skills, configuration, and API keys:

```c
# Dry run first — preview what will be imported
hermes claw migrate --dry-run --source ~/.openclaw

# Run the actual migration
hermes claw migrate --source ~/.openclaw

# Verify the import
hermes skills list
hermes memory status
```

## Working with Hermes: code examples

***Running a task and observing skill creation***

```c
import asyncio
from hermes_agent import HermesAgent

async def main():
    agent = await HermesAgent.create(
        config_path="~/.hermes/config.toml"
    )

    # First time: agent reasons through the task
    result = await agent.run(
        "Review this PR diff and flag any security issues: {diff}",
        context={"diff": open("pr_diff.txt").read()}
    )

    print(result.response)
    print(f"New skills created: {result.skills_created}")
    print(f"Skills used: {result.skills_used}")
    print(f"Reflection: {result.reflection_summary}")

asyncio.run(main())
```
```c
Output after first run:
  New skills created: ["pr-security-review-v1.md"]
  Skills used: []
  Reflection: "Identified SQL injection risk in line 47.
               Created skill for future SQL review tasks."

Output after 20 similar PRs:
  New skills created: []
  Skills used: ["pr-security-review-v1.md", "sql-injection-patterns.md"]
  Task completed 40% faster — skill library handled pattern matching
```

***Querying the skill library***

```c
# Inspect what the agent has learned
async def inspect_skills():
    agent = await HermesAgent.create()

    # List all self-generated skills
    skills = await agent.skills.list(source="self-generated")
    for skill in skills:
        print(f"{skill.name}: used {skill.use_count}x, "
              f"success_rate={skill.success_rate:.1%}")

    # View user model
    user_model = await agent.memory.get_user_model()
    print(f"Preferences: {user_model.preferences}")
    print(f"Common tasks: {user_model.frequent_task_types}")
    print(f"Sessions logged: {user_model.session_count}")
```

## Hermes vs. OpenClaw: full head-to-head comparison

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*2D_AuszLH2E-JKgbV3b1Wg.png)

## The security picture

This is where the comparison gets uncomfortable for OpenClaw. CVE-2026–25253 (CVSS 8.8) exposed a cross-site WebSocket hijacking vulnerability — the `/api/export-auth` endpoint lacked authentication, allowing anyone on the network to extract all stored API keys from any reachable OpenClaw instance. Nine CVEs were disclosed in four days in March 2026. Security researchers found 135,000+ publicly exposed instances across 82 countries.

The root cause isn’t incompetence — it’s architectural. OpenClaw was designed as a consumer-friendly local tool that grew into a networked agent. Many of its security assumptions were reasonable for a personal tool but dangerous at scale.

Hermes has zero reported agent-specific CVEs as of April 2026. Its architecture includes container hardening, namespace isolation for subagents, and credential rotation via the pluggable memory system. Most importantly: because Hermes skills are self-generated rather than downloaded from a community marketplace, it sidesteps the supply chain attack vector entirely. There is no ClawHub equivalent to distribute malicious packages through.

> **Important caveat:** Hermes launched in February 2026. OpenClaw has been deployed at far greater scale for far longer. Less exposure time means fewer discovered vulnerabilities — which isn’t the same as being inherently more secure. The zero-CVE record is encouraging, not a guarantee. If you’re deploying at enterprise scale, both frameworks require serious security review regardless of their public CVE history.

## Honest limitations you need to know

***Self-learning is disabled by default***

This is the most common complaint from new users. The “grows with you” promise requires explicitly enabling `persistent memory` and `skill_generation` in the config. Without this, Hermes behaves like any other single-session agent. Many reviewers who dismissed Hermes as "nothing special" had never enabled the learning loop.

***Not a code-generation tool***

Hermes is explicitly a conversational agent framework. For software engineering tasks — writing code, debugging, refactoring — Cursor, Windsurf, or Claude Code outperform it. If you’re primarily looking to replace your AI coding assistant, Hermes is not the right choice. If you’re building a personal AI that handles research, analysis, repetitive workflows, and knowledge accumulation over months, it’s a strong candidate.

***Memory is opaque***

OpenClaw’s memory is transparent — every memory entry is a visible file you can inspect, edit, or delete directly. Hermes trades that transparency for convenience. The SQLite episodic archive is not easily human-readable. Users who care about knowing exactly what their agent “remembers” about them will find this frustrating. As of v0.10.0, there’s a `hermes memory inspect` command that surfaces the user model and recent episodic entries, but it's not as transparent as OpenClaw's file-per-memory approach.

***Fewer integrations — and that’s a deliberate choice***

Six messaging platforms vs. OpenClaw’s 24+. Nous Research has been explicit: they’d rather deeply integrate six platforms than shallowly support twenty-four. For users who need WhatsApp + Telegram + Slack + Discord all talking to the same agent from a single instance, OpenClaw remains the stronger choice.

***Young project, fewer releases***

Hermes has had 10 releases. OpenClaw has had 82. One Reddit commenter put it directly: “Hermes has had 6 releases to OC’s 82. 3 of those didn’t even work. Don’t listen to claims of it being more stable because it hasn’t been around long enough to make that claim.” This was based on an earlier count, and v0.10.0 has been stable, but the point stands — Hermes hasn’t been tested at OpenClaw’s scale yet.

## Who should switch and who shouldn’t

**Switch to Hermes if:** You use your agent daily for the same categories of tasks — weekly code reviews, recurring research workflows, repetitive document analysis. The learning loop pays off over months, not days. After 20+ self-generated skills in your domain, the 40% task-time reduction is real. You also want simpler setup, better default security, and an architecture that doesn’t require managing a Docker stack and YAML configuration.

**Stay on OpenClaw if:** You need 24+ messaging platform integrations from a single agent. You’re deploying agents for a team or organization where ecosystem breadth matters more than per-instance learning. You value transparent file-based memory. You need the kind of multi-agent orchestration that OpenClaw’s mature implementation provides. Or you’ve already invested significant time in the ClawHub skill ecosystem.

**Use both if:** This is the answer the Reddit community is converging on for complex setups. OpenClaw as the multi-channel orchestration layer. Hermes as the execution agent for specific workflow types where accumulated learning matters. They complement each other more than they compete.

**Real-world cost breakdown:**

A Hermes instance running daily on a $5 VPS with Claude Sonnet costs approximately $30–65/month in API calls for moderate usage. An OpenClaw instance with similar usage on self-managed Docker hosting runs $40–80/month. The cost difference isn’t significant for solo developers — what matters is whether you want to spend your time on Docker configuration or on working with the agent.

> ***The honest bottom line***
> 
> OpenClaw proved that self-hosted AI agents could manage your inbox, automate workflows, and run 24/7 across all your apps. Hermes Agent proved that an agent doesn’t have to start from scratch on every task. These are both real advances — they just make different trade-offs. The question isn’t which one is better. It’s which trade-off fits your actual workflow.

**PART2 — I have published part 2 of this article here** [https://medium.com/@sathishkraju/your-hermes-agent-has-no-performance-review-heres-how-to-fix-that-92254efdfe18](https://medium.com/@sathishkraju/your-hermes-agent-has-no-performance-review-heres-how-to-fix-that-92254efdfe18)

**PART3** of this article is here [https://medium.com/@sathishkraju/why-your-ai-agent-has-amnesia-and-how-hermes-agent-actually-fixes-it-9b5329992c0d](https://medium.com/@sathishkraju/why-your-ai-agent-has-amnesia-and-how-hermes-agent-actually-fixes-it-9b5329992c0d?postPublishedType=repub)