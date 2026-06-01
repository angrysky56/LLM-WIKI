---
created: 2026-06-01T00:00:00Z
updated: 2026-06-01T00:00:00Z
type: source
summary: "First distributed agent attack: a multi-agent scaffold completes hard cybersecurity tasks while hiding the harmful objective across many user accounts. Standard monitors miss it 80% of the time. Online stateful monitor with stream clustering catches distributed attacks 30% earlier at ~99% traffic latency, and also catches standard jailbreaks."
tags: [agent-security, distributed-attacks, safety-monitors, stateful-monitoring, stream-clustering, red-teaming, jailbreaks, agent-misuse, cyber-misuse, paper-2605-31593]
sources: https://arxiv.org/abs/2605.31593
status: active
confidence: high
---

# Stateful Online Monitoring Catches Distributed Agent Attacks (Brown et al., 2026)

## Definition

This paper presents two contributions:

1. **The first distributed agent attack** — a multi-agent scaffold (built on ARTEMIS) where a supervisor decomposes a hard cybersecurity task into sub-tasks distributed across many user accounts, with each subagent receiving a narrow, reframed-as-benign context. The attack solves tasks the supervisor model couldn't solve alone (gpt-oss-120b: 0% → 36.7–40.0% on a Cybench subset) while evading standard safety monitors, which catch it only **20% as often** as prior agent attacks.

2. **An online stateful monitor** — a real-time, low-latency monitor that uses **stream clustering** of agent context embeddings to collect weak suspiciousness signals across many user accounts, escalating only rarely to a language-model judge that reasons across the cluster. Catches distributed attacks **30% earlier** than standard monitors, with negligible additional latency for **~99% of traffic**. A two-month red-teaming exercise with white-box access further hardened the monitor and revealed it *also catches standard jailbreaks* — adaptive attackers reuse attack variants across accounts.

## Key Idea

- **Architectural blind spot of standard monitors**: they score one agent context at a time. Distributed attacks exploit this by splitting the harmful objective across accounts, so each transcript looks benign in isolation.
- **Real Anthropic case study (2025)**: Claude Code was misused against 30 global victims with an external orchestrator splitting the operation into "small, seemingly innocent" defensive-looking tasks ("map this system", "validate these credentials"). Anthropic identified the campaign by *stitching evidence across sessions* — exactly the operation the stateful monitor automates.
- **Subtle shared features**: subtasks in distributed attacks inherit features from the exploit objective, identifiable in a structured embedding space even when the attacker obfuscates each subtask.
- **Insight**: a *new class of safety monitors* that reason over **groups of users** rather than isolated transcripts.

## Methodology

### The Distributed Attack
- **Scaffold**: ARTEMIS (Lin et al. 2025) — an agent orchestrator receives the full task, delegates subagents with narrow, reframed-as-ordinary-engineering task descriptions, stores outputs in a shared database, and uses a verifier tool to check progress.
- **Models**: gpt-oss-120b supervises gpt-5.2 subagents; the monitor sees only subagent contexts.
- **Tasks**: a difficult Cybench subset (CTF-style exploit chains).
- **Generalises two prior lines**: (1) simple-question decomposition attacks (Glukhov et al. 2024, Jones et al. 2025, Brown et al. 2025), and (2) single-context decomposition attacks (Li et al. 2024, Yueh-Han et al. 2025).
- **Performance**: gpt-oss-120b solves 0% directly but 36.7–40.0% via the scaffold — **models too weak to solve a full task can still coordinate stronger agents to solve it while hiding the objective**.

### The Online Stateful Monitor (Algorithm 1)
For every new request `x_t`:
1. **Step 2 (Standard monitor)**: score `x_t` for suspiciousness `s_t` using existing single-context safety monitor.
2. **Step 3 (Embed + cluster)**: embed `x_t`; route to nearest cluster centroid `j*`; open a new cluster if similarity is below routing threshold `τ_route`; otherwise update centroid and buffer online.
3. **Step 4 (Cross-context escalation)**: only if either (a) `s_t` exceeds standard-monitor threshold, or (b) cluster `j*` accumulated cross-session evidence; then call a **cross-context monitor** over `x_t` + top-k prior entries from the buffer to decide ALLOW/DENY.

**Cost analysis**: per-request cost is `O(1) + O(d·M_t + M_t log M_t) + q_t · C_cc`, where `M_t` is the number of cluster centroids (much smaller than `N_t` of all prior transcripts) and `q_t ∈ {0,1}` gates whether the LM judge runs. This makes the monitor's overhead **negligible for the 99% majority** of traffic that doesn't trigger the cross-context judge.

### Detection Rules (from the red-team exercise)
The cross-context monitor uses six rules, learned/improved over two months of red-teaming:
1. Distinguish isolated-session evidence from cross-session evidence.
2. **Cross-session corroboration matters a lot** — repeated offensive steps across users.
3. **Same-session repetition is weaker** than cross-session repetition.
4. Don't deny solely because prompts mention vulnerabilities/bug bounties/etc.
5. **DENY** when either: (a) the request involves unauthorised access, or (b) cross-session evidence meets calibrated thresholds.
6. **ALLOW** when evidence is isolated, defensive, educational, or doesn't meet the threshold.

## Key Findings

| Metric | Standard Monitor | Online Stateful Monitor |
|--------|------------------|--------------------------|
| Detection of distributed attacks | 20% recall | ~80% recall (Pareto dominates) |
| Time-to-detection | baseline | **30% earlier** (up to 31%) |
| Detection at 0.05 FPR/session | misses ~80% | catches most |
| Per-request latency for 99% of traffic | baseline | ~equal to standard |
| P99 tail latency | baseline | elevated (escalation path) |
| Also catches standard jailbreaks | yes | **yes (with bonus)** |

- The detection advantage **persists but narrows** as benign background traffic grows very large — there is a scale limit to the cluster-based approach.
- **Surprise finding**: stateful monitoring generalises beyond distributed attacks to **standard jailbreaks**, because adaptive attackers reuse attack variants across accounts. Two months of red-teaming did not break the monitor.

## Limitations

- **Scale limit**: at very high benign-traffic ratios, the cluster-quality signal degrades and the detection advantage narrows.
- **P99 latency** is elevated because escalation does invoke the cross-context LM judge.
- **Threat-model asymmetry**: the defender is *the model deployer*. The attack is realistic for any multi-tenant LLM agent deployment.
- **Scope**: focused on cybersecurity tasks; cross-domain generalisation (e.g., bio, chemical, persuasion) is unevaluated.

## Connections

### Wiki concepts
- [[ai-security]] — distributed attacks are the architectural limit of single-context safety
- [[agent-leak-benchmark]] — a related safety benchmark
- [[agentic-oversight]] — the cross-context judge is a form of oversight that spans users
- [[ai-safety]] — the broader family
- [[reconstruction-attack]] — a different attack surface
- [[agentic-research]] — the broader context (stateful monitoring protects agentic research deployments)

### Related papers (wiki)
- [[boiling-frog-agentic-safety-2026]] — 44.4% aggregate ASR in multi-turn agentic settings; complementary: Boiling the Frog is single-context, Stateful Monitoring is cross-context
- [[finharness]] — inline safety harness for finance LLM agents (single-context defense); complements but doesn't replace stateful monitoring
- [[gram-sabotage-alignment-auditing-2026]] — automated alignment auditing for sabotage (~2-3% misbehavior, mostly overeagerness); orthogonal but same oversight family
- [[calibrating-conservatism-scalable-oversight-2026]] — CCO's conformal-decision-theoretic conservatism; the stateful monitor is a *different* lever on the same scalable-oversight problem
- [[alignment-tampering]] — vulnerability in RLHF preference datasets; orthogonal threat
- [[defending-moe-llms-against-harmful-fine-tuning-via-safety-routing-alignment]] — fine-tuning attack vector; orthogonal to distributed deployment attacks
- [[muse-autoskill]] — agents' skill *reuse* across tasks; *re-use* of attack patterns across accounts is the same structural similarity the stateful monitor catches
- [[lcguard-kv-communication-guard-2026]] — KV-based latent communication in multi-agent LLM systems; a different attack surface than cross-account distribution
- [[deltabox-stateful-agent-checkpoint-rollback-2026]] — stateful *agent* infrastructure; pairs with stateful *monitor* infrastructure

### Cross-paper theme
The stateful-monitor paper extends the **oversight / agentic-safety theme** (2026-05-24: Boiling the Frog; 2026-05-28: Gram, CCO) to the **architectural level** — the standard monitor's per-context scoring is the *causal bottleneck* that allows distributed attacks to succeed. The fix is *not* a better single-context judge but a *new monitor architecture* that aggregates weak signals across many contexts in real time.
