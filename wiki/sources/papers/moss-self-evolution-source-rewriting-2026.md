---
created: 2026-05-22 14:16:33+00:00
updated: 2026-05-22 14:16:33+00:00
summary: Wiki source page for MOSS paper on source-level self-evolving agents
tags: [paper, self-evolving-agents, source-level, openclaw]
---


---
title: "MOSS: Self-Evolution through Source-Level Rewriting"
authors:
  - Qianshu Cai (USTC / HKUST)
  - Yonggang Zhang (HKUST)
  - Xianzhang Jia (HKUST)
  - Wei Xue (HKUST)
  - Jun Song (Hong Kong Baptist University)
  - Xinmei Tian (USTC)
  - Yike Guo (HKUST)
date: 2026-05-21
paper_id: 2605.22794v1
tags:
  - self-evolving agents
  - source-level adaptation
  - autonomous agents
  - agentic systems
  - OpenClaw
category: paper
arxiv: https://arxiv.org/abs/2605.22794
github: https://github.com/dav-joy-thon/MOSS
---

# MOSS: Self-Evolution through Source-Level Rewriting in Autonomous Agent Systems

## Overview

MOSS is a system that performs **self-rewriting at the source level** on production agentic substrates. It enables autonomous agents to modify their own source code—specifically the **agent harness** (routing, state management, hook ordering, dispatch)—rather than being limited to text-mutable artifacts like prompts, skills, and memory schemas.

The core argument is that source-level adaptation is strictly more general than text-mutable evolution: it is Turing-complete, a strict superset of every text-mutable scope, deterministic in effect, and does not erode under long-context drift.

## Key Contribution

MOSS is the **only self-evolving agent system that reaches the harness layer**. All prior application-level self-evolving agents (Hermes Agent, SkillClaw, GenericAgent, EvoAgentX) confine evolution to text-mutable artifacts. MOSS extends evolution to the code layer itself.

| Project | Skill | Prompt | Memory | Harness |
|---------|-------|--------|--------|---------|
| Hermes Agent | ✓ | ✗ | ✓ | ✗ |
| SkillClaw | ✓ | ✗ | ✗ | ✗ |
| GenericAgent | ✓ | ✓ | ✗ | ✗ |
| EvoAgentX | ✓ | ✓ | ✗ | ✗ |
| **MOSS** | ✓ | ✓ | ✓ | **✓** |

## System Architecture

MOSS consists of five major components:

1. **Substrate** — The production agentic system under evolution (e.g., OpenClaw). MOSS is substrate-agnostic and adapts to any substrate providing: shell-equivalent tool execution, filesystem read, periodic scheduling, webhook-to-agent delivery, and system-prompt injection.

2. **Control Surface (`moss evo` CLI)** — A CLI injected into the substrate through which the agent (and user) drive evolution. Nine subcommands: `status`, `batches`, `batch`, `start`, `stop`, `restart`, `apply`, `flag`, `catch-up`. The agent is made aware of this capability via a system-prompt injection pointing to an on-disk capability document.

3. **External Coding-Agent CLI** — Code modification is delegated to a pluggable external coding-agent CLI (Claude Code, OpenAI Codex, DeepSeek-TUI, or OpenCode) invoked as a host-side subprocess. MOSS owns stage ordering and verdicts; the coding-agent owns the act of editing within its given scope.

4. **Host-Daemon** — A permanent asyncio process on the host that handles: coding-agent CLI invocation per stage, trial-worker container lifecycle, Docker build and image management, and the auto-scan engine that surfaces under-performing dialogue chunks from session JSONLs.

5. **Ephemeral Trial Workers** — Short-lived containers from the candidate image that replay the failure batch autonomously, verifying candidates in a production-equivalent environment without live user state.

### Topology

- **moss-gateway container**: Long-running user-facing substrate (chat agent + in-container evolution service + bind-mounted moss CLI). User-state volume (sessions, memory, credentials, agent configs) is mounted from the host filesystem and survives container swaps.
- **host-daemon**: Permanent asyncio RPC server (Unix socket) + swap supervisor + auto-scan engine.
- **Coding-agent CLI**: Spawned per evolution stage, lives only for that stage's duration.
- **Trial workers**: Ephemeral containers launched per iteration, network/mount-isolated from the live container.

## The Evolution Process

### Directed Evolution

Rather than exploratory mutation against a fixed benchmark (the academic paradigm), MOSS takes a **directed and deterministic** approach: each evolution is anchored to a concrete batch of **production-failure evidence**. Evidence accumulates through:
- **Auto-scan (`moss evo catch-up`)**: Periodic cron job scanning session JSONLs for under-performing dialogue segments.
- **Manual flagging (`moss evo flag`)**: User expresses dissatisfaction in conversation → agent invokes `moss evo flag` → scans session from cursor to EOF.

Both paths append to a per-conversation open batch (sealed when chunk count reaches a configurable threshold, default 8).

### Evolution Loop

MOSS iterates because single-shot patching is unreliable at this scale. Each iteration's structured evaluation feeds the next iteration's localization and planning.

**Loop structure (four nested levels):**
- **Layer 0**: Pre-loop baseline — Task-Evaluate scores pre-captured baseline transcripts, producing a baseline keypoint matrix that locks the keypoint set.
- **Layer 1**: Iteration loop — runs until CONVERGED verdict, model ceiling hit, architecture limit reached, or plateau detected.
- **Layer 2**: Seven-stage pipeline per iteration.
- **Layer 3**: Internal multi-round loops around the two review gates.

**Verdicts**: CONVERGED, NEED_MORE_WORK, FUNDAMENTAL_LIMIT_MODEL, FUNDAMENTAL_LIMIT_ARCHITECTURE. A plateau guard forces convergence when no keypoint has improved for several consecutive iterations.

**Depth dial**: `light` / `standard` / `deep` scales iteration budget, stage round budgets, trials per task, and plateau threshold.

### Seven-Stage Pipeline

One iteration decomposes into seven sequential stages:

| Stage | Description |
|-------|-------------|
| 1. **Locate** | Reads baseline traces and batch failures, writes a diagnosis without proposing fixes. |
| 2. **Plan** | Identifies root cause; specifies which files change, what logic is added, what is left alone. |
| 3. **Plan-Review** | First quality gate; plan approved, rejected as off-target, or rejected as too narrow. Alternates with Plan in a multi-round plan-loop until approval or round-budget cap. |
| 4. **Implement** | Writes the code as a single git commit on the inner substrate repository. |
| 5. **Code-Review** | Second quality gate; diff reviewed against the plan and approved or rejected. Alternates with Implement in a multi-round code-loop (working tree hard-reset between rounds). |
| 6. **Task-Evaluate** | After Build and Trial, scores 4–7 keypoints per task on a 4-level scale (strong / adequate / weak / missing). Same stage runs in pre-loop baseline to lock the keypoint set. |
| 7. **Verdict** | Synthesizes all per-task evaluations and cross-iteration keypoint matrix into one of four verdicts. |

Note: **Build** and **Trial** are runtime affordances around Task-Evaluate, not reasoning stages themselves.

### Runtime Verification

Code-Review operates at the syntactic/semantic level, so runtime faults (race conditions, cross-module state interactions, hook-order-dependent behavior) pass through it. Verification must therefore be **runtime, production-equivalent, and against the same prompts that produced the failure**.

MOSS realizes this through **ephemeral trial workers**: after Build, the host-daemon spawns N short-lived containers from the candidate image, has the agent autonomously process the batch tasks inside each, repeating every task several trials to expose flakiness. Trial workers are network- and mount-isolated and torn down when the iteration ends.

### In-Place Container Swap

Standard deployment patterns don't fit: the agent is single-instance bound to user state (sessions, memory, credentials, agent configs on a user-state volume).

**Swap protocol:**
1. On CONVERGED verdict, evolution loop marks batch as ready to apply → fires `evolution-converged` webhook → routed to agent as system message.
2. User invokes `moss evo apply` (typically through conversation).
3. Apply request atomically writes a swap-request file.
4. Host-daemon's swap-supervisor file-polls every 2 seconds; on detection, restarts substrate container against candidate image.
5. 90-second probe window: samples every 5 seconds, running 4 health checks (heartbeat freshness ≤ 30s, container running, two substrate-level CLI status probes).
6. Three consecutive passes → commit swap; otherwise → rollback to last-known-good image.
7. `apply-complete` webhook fires (carrying success/rolled-back status) to the freshly-swapped gateway.

**User-state volume is mounted into the new container untouched.**

## Case Study: OpenClaw

**Tasks**: Four claweval compliance-audit tasks (T141zh/T142 SLA compliance audit, T137zh/T138 restock-chain check).

**Baseline**: OpenClaw with DeepSeek V3.2 scores 0.21–0.33 (mean 0.25), well below the 0.75 pass threshold. Failure modes: agent lists only some relevant tickets (marks others "indeterminate"), misattributes customer names, returns partial restock chains.

**Iteration 1 diagnosis** (harness-level fix):
- **Surface 1**: Coverage gap in harness's tool-result handling for multi-tool execution patterns — agent chooses generic execution path over semantic tools the mediator was designed around, with no annotation branch for that path.
- **Surface 2**: Parsing issue in harness's dispatch-synthesis pipeline when agent batches several lookups into a single shell construct, leaving downstream consumers with merged, partially-attributed outputs.

**Fix**: 177 insertions / 1 deletion across three files:
- New annotation branch + supporting helpers in tool-result mediator
- Added pre-call check in before-tool-call hook chain
- New mediator test file

### Results

| Task | Baseline | Iter 1 | Δ |
|------|----------|--------|---|
| T141zh_sla_compliance_audit | 0.3273 | 0.5330 | +0.2057 |
| T142_sla_compliance_audit | 0.2527 | 0.5453 | +0.2926 |
| T137zh_restock_chain_check | 0.2213 | 0.4567 | +0.2354 |
| T138_restock_chain_check | 0.2090 | 0.9049 | +0.6959 |
| **mean** | **0.2526** | **0.6100** | **+0.3574** |

Single evolution cycle lifts four-task mean from **0.25 to 0.61** without human intervention.

## Why Source-Level Adaptation is Superior

The paper argues source-level adaptation is superior to text-mutable evolution along four axes:

1. **Turing-complete**: Programming languages are Turing-complete; the source-code design space is a universal search space within which every text-mutable design space sits as a strict subset.
2. **Strict superset**: Whatever a prompt edit can achieve, an equivalent code edit can also achieve—but not the other way around.
3. **Deterministic**: Routing logic, hook ordering, and state-machine invariants run as code; their behavior doesn't depend on whether the base model correctly reads new text and complies with it.
4. **No long-context drift**: Text-mutable fixes are prompts, skills, and memory entries that must be re-read every turn; as they accumulate over weeks of production use, adherence to any single piece dilutes. Edits at the source layer are encoded as behavior, not text to be re-read.

## Related Systems

| System | Type | Evolution Scope |
|--------|------|-----------------|
| SICA | Academic | Source-level, minimal scaffold |
| Darwin Gödel Machine | Academic | Source-level, open-ended search |
| HyperAgents | Academic | Source-level, meta-procedure editable |
| Meta-Harness | Academic | Harness optimization, minimal scaffold |
| Hermes Agent | Application | Text-mutable (skills, memory) |
| SkillClaw | Application | Text-mutable (skills) |
| GenericAgent | Application | Text-mutable (prompts, SOPs) |
| EvoAgentX | Application | Text-mutable (workflows) |
| **MOSS** | **Application** | **Source-level (harness included)** |

## Related
- [[wiki/index]]
- [[sources/papers/papers-2026-05-22-researched]]
- [[sources/papers/moss-self-evolution-source-rewriting-2026]]
- [[sources/papers/awarevln-self-aware-vision-language-navigation-2026]]

- [[moss-self-evolution-source-rewriting-2026]]

## References

- Original paper: [arXiv:2605.22794v1](https://arxiv.org/abs/2605.22794)
- Code: [github.com/dav-joy-thon/MOSS](https://github.com/dav-joy-thon/MOSS)
