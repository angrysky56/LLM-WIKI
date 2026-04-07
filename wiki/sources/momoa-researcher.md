---
summary: Google Labs agentic research scientist using Mixture of Mixture of Agents
tags: [AI, research, agents, Google, MoMoA]
updated: 2026-04-07T22:32:15Z
created: 2026-04-07T22:32:15Z
---

# MoMoA Researcher (Google Labs)

Source: [labs.google/code/experiments/momoa-researcher](https://labs.google/code/experiments/momoa-researcher)

## What It Is

An **agentic research scientist** built on Google's Mixture of Mixture of Agents (MoMoA) framework. Extends a multi-agent software development system with research-specific roles, tools, and workflows to conduct actual scientific research — not just information retrieval.

## Core Idea

> "I can write decent software already. What I really want is an agent to do things I'm not an expert in."

The system doesn't just look things up. It proposes hypotheses, designs experiments, runs them, evaluates results, and iterates — producing academic-grade research reports.

## Architecture

- **Senior Researcher** agent — drives scientific rigor, hypothesis formation, experimental design
- **Research Room** — collaborative space for investigation and analysis
- Existing MoMoA agents: software devs, tech writers, project managers
- **Continuous loop** — iterates on research tasks within a broader research project

## Research Tools

- **Optimizer** — runs Python/Rust evaluators for grid search, random search, with statistical significance (multiple trials, mean/std dev)
- **Code Runner** — executes Python/Rust scripts in sandboxed environment
- **Research Logger** — append-only log ensuring experimental provenance (cannot be edited by the agent)

## Key Design Decisions

- Research Logger is **append-only** — the agent cannot alter previous experimental results, building trust in the output
- Each session is a **Research Task** within a **Research Project** — the initial prompt becomes the project definition, tasks accumulate context
- Post-task auto-evaluation: "How well did you do? What would you recommend next?"
- Proposed follow-up tasks enable continuous autonomous research

## Relevance to This Wiki

MoMoA Researcher demonstrates the same principle as [[Project Synapse]]: shifting AI from reactive Q&A to **autonomous, accumulating knowledge work**. Key parallels:

| MoMoA Researcher | Project Synapse |
|---|---|
| Append-only Research Logger | wiki/log.md (append-only) |
| Research Project → Tasks | Raw sources → wiki pages |
| Continuous research loop | Ingest → query → lint cycle |
| Agent can't edit its own logs | Git provides rollback |

## Scaling Limitations

Current prototype runs on a single VM with limited compute. Future: parallel VMs, integration with [[AlphaEvolve]] for evolutionary search at scale.
