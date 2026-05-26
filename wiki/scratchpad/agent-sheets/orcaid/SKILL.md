---
name: orcaid
description: "Daily OrCAID multi-agent delegation — run commit0/self_improve/paperbench tasks, evaluate output, deliver results. Schedule: 09:00 AM."
tags: [orcaid, self-improve, commit0, paperbench, paper2code, daily]
triggers:
  - cron: "0 9 * * *"
  - manual: delegate_task
updated: 2026-05-25
created_by: agent
---

# orcaid — OrCAID Multi-Agent Delegation

Run the OrCAID multi-agent delegation framework. Three task types: `commit0` (stub implementation), `self_improve` (self-refactor), `paperbench` (paper reproduction). Choose the right mechanism for the job.

## See Also

- `references/task-types.md` — commit0 / self_improve / paperbench details
- `references/execution-mechanisms.md` — ACTIVE vs PASSIVE mechanisms
- `templates/run-report.md` — run report format

## Execution Mechanisms

**Mechanism 1 — ACTIVE**: `orcaid.cli` → produces new outcomes
**Mechanism 2 — PASSIVE**: `run_evolution.py --domain orcaid` → computes metrics from memory (no new outcomes)
**Mechanism 3 — PASSIVE**: `run_evolution.py --domain paper2code` → evaluates Paper2Code outputs

## Three Task Types

| Task | Use When | Docker Image |
|------|----------|--------------|
| `commit0` | Fix missing stubs in repo | `wentingzhao/minitorch:v0` |
| `self_improve` | Refactor/improve OrCAID itself | `python:3.12-slim` |
| `paperbench` | Reproduce scientific paper | `ghcr.io/openhands/agent-server:latest-python` |

## Critical Constraints

- **Always use `uv run python`** — NOT bare `python`
- **Orchestrator-memory path**: `~/.hermes/orchestrator-memory/` (NOT `~/.orcaid/`)
- **Retry policy**: Always `export ORCAID_RETRY_POLICY=kl`
- **Report delivery**: origin (Discord) — needs human attention on failures

## Quality Standards

- Distinguish "task ran" vs "task produced correct output"
- Document Docker image pull time on first run
- Always update carryover — OrCAID debugging depends on historical pattern recognition