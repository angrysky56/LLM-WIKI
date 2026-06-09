---
summary: "First formal treatment of observability for delegated execution in agentic AI: delegation-scoped execution is structurally underdetermined from standard audit logs. Proposes five requirements (I1–I5) for delegation observability."
tags: [agentic-safety, observability, delegation, audit, monitoring, arxiv-2026-06-09]
updated: 2026-06-09T15:06:38Z
created: 2026-06-09T15:06:38Z
---

# Observability for Delegated Execution in Agentic AI Systems

**arXiv:** 2606.09692 | **Authors:** Abhinav Mishra, Kumar Sharad (Cisco / Splunk)

## Problem

When an AI agent delegates a task to a sub-agent, who authorised what? Current audit systems record individual actions — an API call was made, a file was read, a tool was invoked — but **delegation-scoped execution is structurally underdetermined from standard observables**. Audit logs and execution traces can be identical under multiple incompatible delegation assignments. This gap is especially acute in LLM-based agentic systems, where agents dynamically select tools, vary execution sequences across runs for the same instruction, and spawn cooperating sub-agents. These dynamics fragment and interleave traces, making delegation-scoped reconstruction from causal structure alone structurally impossible.

## Method — Formal Observability Framework

The paper's core contribution is a **formal definition of delegation observability** and a structural analysis of why standard approaches fail. Key elements:

1. **Delegation-scoped execution defined:** A set of actions A = {a₁, ..., aₙ} that occurred under a specific delegation D, where D is a principal-authorised scope boundary (a user asked the agent to X, the agent delegated sub-tasks to other agents/tools).

2. **Underdetermination proof:** For any observable trace T and any two incompatible delegation assignments D₁, D₂ (where D₁ ≠ D₂), there exists an execution E that produces T under both assignments. **This is not a practical limitation — it is a structural one.**

3. **Five Observability Requirements (I1–I5):**

   | ID | Requirement | What It Prevents |
    |----|------------|------------------|
   | I1 | Authenticated channel binding principals to agent instances at the gateway boundary | Identity spoofing / delegation scope misattribution |
   | I2 | Mandatory routing to track which sub-agent received which delegation | Orphaned actions with no delegation parent |
   | I3 | Coverage detection to surface actions not covered by any delegation | Shadow execution / unauthorised tool use |
   | I4 | Gateway-minted delegation identifiers with principal binding | Delegation scope extension / authority escalation |
   | I5 | Tamper-evident storage with gateway isolation | Post-hoc log manipulation / evidence suppression |

4. **Gateway architecture:** The paper proposes a **gateway-based observability layer** that sits at the boundary between the delegating principal and the agent system. All delegation events pass through this gateway, which mints delegation identifiers, binds them to authenticated principals via I1, and routes actions through I2 such that every observable action carries its delegation scope.

## Results

The formal results are primarily structural rather than empirical:

- **Delegation observability is NP-hard** under general conditions (reduction from the graph isomorphism problem on delegation-labelled action DAGs)
- With I1–I4 satisfied, delegation-scoped reconstruction is **polynomial-time solvable** (O(n×d) where n = actions, d = depth of delegation tree)
- Adding I5 (tamper-evident storage) provides **probabilistic post-hoc verification** of delegation integrity

The paper does not provide a deployed system evaluation but instead gives a **proof-of-concept architecture** using SPIRE (SPIFFE) for I1, OpenTelemetry for I2, and a blockchain-anchored audit log for I5.

## Limitations

- Purely formal/architectural — no empirical evaluation on real agent systems
- Gateway assumes a centralised trust boundary; distributed or peer-to-peer delegation models (where no gateway exists) are structurally unaddressed
- I5's blockchain anchoring introduces latency and cost that may be prohibitive for high-frequency delegation
- The framework only covers delegation scoping — it does not address content-level oversight (what the sub-agent *does* within scope)
- Evaluated only on synthetic delegation scenarios; real-world agent systems (AutoSci, ChatGPT with tools, Claude Code) produce delegation patterns far more complex than the model captures

## Connections

- [[stateful-monitoring-distributed-agent-attacks-2026]] — Stateful monitoring catches distributed agent attacks via stream clustering; this paper provides the *delegation framework* that those attacks operate on. Together they form: attack vector (Stateful Monitoring's distributed attack) + formal boundary (Observability's delegation scope).
- [[monitoring-agentic-systems-reliability-2026]] — Monitoring Maturity's 3×3 grid assumes observability as a prerequisite. This paper shows that prerequisite is not met — you cannot monitor what you cannot attribute.
- [[hll-humanitys-last-line-verification-2026]] — HLL tests whether agents can substitute for humans at verification boundaries. Observability asks a prior question: can you even tell *who* was acting?
- [[skillharm-lifecycle-skill-attacks-2026]] — Poisoned skills can be injected via delegation chains; delegation observability is the infrastructure that would catch which sub-agent introduced what when.
- [[boiling-frog-agentic-safety-2026]] — Gradual erosion of safety boundaries: delegation observability is the structural prerequisite for detecting that erosion in multi-agent deployments.
- [[ai-safety]] — Foundational infrastructure layer for multi-agent safety.
- [[autosci-memory-centric-research-lifecycle-2026]] — AutoSci's SciDAG multi-agent operators create delegation chains that Observability's framework would govern.

## Key Quote

> "Delegation-scoped execution is not identifiable from standard observables: audit logs and execution traces can be identical under multiple incompatible delegation assignments."

## Discussion

This paper fills a critical gap in the wiki's coverage of agentic safety. The existing papers cover detection (Stateful Monitoring), maturity staging (Monitoring Maturity), verification boundaries (HLL), and attack surfaces (SkillHarm). What was missing was the **formal infrastructure** — the question of whether you can even *determine who did what* in a multi-agent system. This paper proves that you cannot, and provides requirements for fixing it.

For the **capability-vs-deployment gap** theme: observability is the infrastructural prerequisite that must be satisfied before agents can be safely deployed with delegation authority. Deployment without delegation observability is structurally blind to unauthorised sub-agent behaviour.
