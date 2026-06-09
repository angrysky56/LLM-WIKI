---
summary: arXiv daily report for June 9, 2026 — 3 papers processed: DCPM (dual-process cognitive memory), Observability for delegated execution, Skill rewriting economics. Theme: Infrastructure Gap.
tags: [arxiv-report, infrastructure-gap, agent-memory, observability, skill-rewriting]
updated: 2026-06-09T15:08:22Z
created: 2026-06-09T15:08:22Z
---

# arXiv Daily Report — June 9, 2026 (Cycle 14)

**3 papers processed from 2026-06-08 arXiv batch (IDs 2606.09421–2606.09826). New theme: The Infrastructure Gap — what's missing between agent capability and safe deployment.]

## Today's Top 3

### 1. DCPM: Dual-Process Cognitive Memory for Self-Evolving LLM Agents (2606.09483)
*Fei, Song, Zheng, Yu — Tencent*

DCPM reorganises LLM agent memory along a **cognitive capability hierarchy** (raw facts → belief trajectories → identity → schemas → intentions → cross-domain patterns) driven by two processes: **System 1** (synchronous daytime writer) records belief revisions as doubly linked supersedes chains; **System 2** (asynchronous nighttime engine) induces schemas and intentions, sweeping for cross-domain collisions. Enabling System 2 contributes most on implicit cross-session inference (+5.20 on PersonaMem-v2), least on span recall — matching the architectural prediction.

→ [[dcpm-dual-process-cognitive-memory-2026]]
→ Connects to: [[sleep-self-modify-consolidate-2026]], [[autosci-memory-centric-research-lifecycle-2026]], [[bounded-representation-capacity]]

### 2. Observability for Delegated Execution in Agentic AI Systems (2606.09692)
*Mishra, Sharad — Cisco / Splunk*

First formal treatment of delegation observability. Proves that **delegation-scoped execution is structurally underdetermined from standard observables** — audit logs and traces can be identical under multiple incompatible delegation assignments. Proposes five observability requirements (I1–I5) and a gateway-based architecture that makes delegation-scoped reconstruction polynomial-time solvable.

→ [[observability-delegated-execution-agentic-2026]]
→ Connects to: [[stateful-monitoring-distributed-agent-attacks-2026]], [[monitoring-agentic-systems-reliability-2026]], [[hll-humanitys-last-line-verification-2026]]

### 3. What Should a Skill Remember? Quality-Cost Trade-offs in Cost-Aware Skill Rewriting (2606.09421)
*Xing, Chen, Jin, Wu, Lin*

First economic analysis of skill rewriting. Shows that **shorter skills can make agents more expensive** by removing sparse operational anchors (validation checks, recovery procedures, edge-case handling) that prevent costly exploration and debugging loops. Naive compression reduces tokens 55% but *increases* total cost by 18%. ~20% of skill content accounts for ~80% of error-prevention value. Cost-aware rewriting yields −12% total cost.

→ [[skill-rewriting-quality-cost-tradeoffs-2026]]
→ Connects to: [[reuserl-skill-reuse-compression-2026]], [[skillopt-self-evolving-2026]], [[skillharm-lifecycle-skill-attacks-2026]], [[skill-rm-2026]]

## 🔗 Cross-Paper Theme: The Infrastructure Gap

All three papers identify **missing infrastructure** between current agent capabilities and the requirements for safe, economically sound deployment:

| Paper | What Exists | What's Missing | Infrastructure Gap |
|-------|-------------|----------------|-------------------|
| DCPM | Single-retrieval memory | Cognitive hierarchy with dual-process consolidation | Memory infrastructure for agent-level personalisation & reasoning |
| Observability | Individual action audit | Delegation-scoped trace attribution | Formal observability infrastructure for multi-agent systems |
| Skill Rewriting | Token-count compression | Cost-aware rewriting with anchor preservation | Economic infrastructure for skill lifecycle management |

**This is the 7th distinct cross-paper theme across 14 cycles.** The pattern is accelerating: rather than separate themes, the papers are converging on a unified diagnosis — **deployment readiness requires infrastructure that does not yet exist**, across memory, audit, and skills.

## Previous Themes

1. (05-24) Verification/trust — ProxySHAP, Boiling the Frog, CUSP
2. (05-26) Bounded representation — Shannon Scaling Law, SkillOpt, SkillLens
3. (05-27) Evaluation infrastructure — MATCHA, FinHarness, Interaction SSD
4. (06-01) Structural reuse as trust unit — ReuseRL, AutoSci, Stateful Monitoring
5. (06-02) Capability-vs-deployment gap — Monitoring Maturity, SkillHarm, HLL
6. (06-03/05) Bounded self-model (4 axes) — Sleep, Skill-RM, Faithful Confidence, RiM, LLMSurgeon, Gated DeltaNet-2
7. **(06-09) Infrastructure Gap — DCPM, Observability, Skill Rewriting**

## 📊 Statistics

| Metric | Value |
|--------|-------|
| Papers scanned across cs.AI/cs.LG/cs.CL | ~150 |
| New papers since 2026-06-07 | ~80 |
| Selected | 3 |
| Wiki pages created | 3 |
| arXiv API rate-limit hits | 1 (recovered) |
| PDF bytes downloaded | ~4.8 MB |
| Wiki index | 1212 pages |

## 📁 Files Touched

**Wiki (new):**
- `wiki/sources/papers/dcpm-dual-process-cognitive-memory-2026.md`
- `wiki/sources/papers/observability-delegated-execution-agentic-2026.md`
- `wiki/sources/papers/skill-rewriting-quality-cost-tradeoffs-2026.md`
- `wiki/scratchpad/jobs/reports/arxiv/arxiv-2026-06-09-top-papers.md`

**Filesystem:**
- `/home/ty/Documents/paper-research/processed/2606.09483v1.pdf`
- `/home/ty/Documents/paper-research/processed/2606.09692v1.pdf`
- `/home/ty/Documents/paper-research/processed/2606.09421v1.pdf`
