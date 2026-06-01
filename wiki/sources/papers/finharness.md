---
updated: 2026-05-27T14:18:01Z
created: 2026-05-27T14:18:01Z
---

---
created: 2026-05-27T14:20:00Z
updated: 2026-05-27T14:20:00Z
type: source
summary: "Inline safety harness for finance LLM agents: Query Monitor + Tool Monitor + Cascade module cut attack success rate from 38.3% to 15.0%"
tags: [paper, arxiv, llm-agents, safety, finance, inline-monitoring, cascade-routing]
sources: https://arxiv.org/abs/2605.27333
status: active
confidence: high
---

# FinHarness: An Inline Lifecycle Safety Harness for Finance LLM Agents

**arXiv:** [2605.27333](https://arxiv.org/abs/2605.27333) | **Authors:** Haoxuan Jia, Yang Liu, Bin Chong et al. | **Published:** 2026-05-26

## Core Contribution

FinHarness is an inline safety harness for finance LLM agents that wraps the agent end-to-end with three components:

| Component | Role |
|-----------|------|
| **Query Monitor** | Fuses single-turn intent with cross-turn drift → session-level risk cumulant |
| **Tool Monitor** | Evaluates each prospective tool call using permission, parameter, and sequence priors |
| **Cascade Module** | Accumulates per-step risk over a sliding window, adaptively routes verification between lightweight and advanced-tier LLM judge |

Fired risk factors are re-injected into agent input as ex-ante evidence, enabling the agent to autonomously refuse, re-plan, or escalate — rather than requiring an external gatekeeper.

## Key Results

- On **FinVault** (856-trace synthesis stress set): routed FinHarness cuts ASR from **38.3% → 15.0%** while preserving benign approval (41.1% → 39.3%)
- Uses **4.7× fewer** advanced-judge calls than always-advanced ablation
- Agent-initiated refusal rises by **+15.7 pp**
- Active interception (hard-stop / self-rejection / escalation) rises by **+6.7 pp**

## Why Inline Positioning Matters

Two dominant deployment patterns fail finance agents:
1. **Boundary filters** — lightweight, stateless, blind to mid-trajectory tool calls; attacks fragmenting payloads across turns evade them
2. **Post-hoc LLM judges** — accurate but intervene after termination (transfer already cleared); context grows linearly with trajectory length

Both treat protection as an external supervisor over a black-box agent. FinHarness operates *within* the execution loop, observing every intermediate state and feeding safety signals directly back into the agent's subsequent decisions.

**Key failure mode addressed**: A five-step semantic-obfuscation attack maintains per-step score at 0.22 (below decisive-risk threshold), yet cumulative risk increases monotonically and crosses escalation threshold at final step. Per-step lightweight judge would approve; FinHarness accumulates across trace.

## Architecture

```
Trajectory
  ↓
[Query Monitor] → single-turn intent + cross-turn drift → risk cumulant
  ↓
[Tool Monitor] → permission check, parameter check, sequence priors
  ↓
[Cascade Window] → per-step risk st → sliding window sum
  ↓
[Router] → lightweight judge (low risk) / advanced judge (high risk)
  ↓
Risk evidence re-injected → agent: refuse / re-plan / approve / escalate
```

## Connections
- [[scratchpad/jobs/reports/arxiv/arxiv-2026-05-27-top-papers]]
- [[wiki/index]]
- [[sources/papers/finharness]]
- [[finharness]]

- [[llm-agents]] — tool-using agents and safety
- [[agentic-research]] — agent safety benchmarks (AgentDojo, Agent-SafetyBench)
- [[rlhf]] — alignment and safety signals
- [[agentic-safety]] — Boiling the Frog (agentic safety) from prior cycle
- [[inline-monitoring]] — architectural pattern of inline vs post-hoc safety

## Notes

- Related to prior cycle's [[agentic-safety]] work (Boiling the Frog) — different domain (finance) but same inline-vs-external supervision theme
- Cascade routing pattern (lightweight/advanced judge) connects to [[sae]] for implicit risk signals
- FinVault benchmark = finance-specific state-changing workflows

- [[stateful-monitoring-distributed-agent-attacks]] — FinHarness focuses on per-turn scoring; stateful monitoring extends to cross-account aggregation via stream clustering, catching distributed attacks 30% earlier
