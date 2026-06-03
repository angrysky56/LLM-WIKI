
---
created: 2026-06-02T00:00:00Z
updated: 2026-06-02T00:00:00Z
type: report
summary: "2026-06-02 batch — 3 papers on agent deployment-readiness. Monitoring Maturity (3x3 grid + variance), SkillHarm (lifecycle skill attacks, ASR up to 86.3%), HLL (CAPTCHA as human-substitution test). New theme: capability-vs-deployment gap."
tags: [arxiv, daily-report, 2026-06, agent-deployment, oversight, skill-security, multimodal-agent]
sources:
  - https://arxiv.org/abs/2606.02494
  - https://arxiv.org/abs/2606.02540
  - https://arxiv.org/abs/2606.02449
status: active
confidence: 0.9
---

# arXiv Daily Report — 2026-06-02

**Cycle:** arXiv batch from 2026-06-01 (38 papers scanned across cs.AI, cs.LG, cs.CL)  
**Selected:** 3 papers  
**Theme:** *The capability-vs-deployment gap — agents can do the task, but cannot be trusted with the workflow*

## Today's Top 3

### 1. **Monitoring Agentic Systems Before They're Reliable** — 2606.02494
**Authors:** Boston, Hanson, Georgala, Hudgens (Reins AI), Frase (Veraitech)  
**Why it matters:** First maturity-staged monitoring framework. The 3×3 grid (scope × dimension) with CV as the characterization signal shows that **task-level error detection is infeasible at Stage 1** because structural defects mask task-level signal. The 97%-automated triage finding — only 2% of findings reach humans — is the most actionable result in the oversight literature this cycle.

**Headline finding:** "Deploy monitoring early: the first thing it finds is the most important thing to fix."

**Wiki:** `wiki/sources/papers/monitoring-agentic-systems-reliability-2026.md`

### 2. **SkillHarm: Lifecycle-Aware Skill-Based Attacks via Automated Construction** — 2606.02540
**Authors:** Ning, Zhang, Lal, Gou, Li, Ruan, Ye, Gupta, Yang, Su, Sun (Ohio State, Amazon AGI, Stanford)  
**Why it matters:** First systematic benchmark of skill-based attacks across the **skill-use lifecycle**, not just single-task execution. 879 attack samples across 71 skills, 12 risk types. The latent-risk finding is the most important methodological observation: **many "attack failures" are agents failing to engage with the poisoned file, not genuine resistance.** The field has been reporting inflated defense numbers.

**Headline finding:** ASR up to 86.3% (FPP) / 69.3% (SMP). Self-mutating poisoning works — first execution looks clean, second pays the cost.

**Wiki:** `wiki/sources/papers/skillharm-lifecycle-skill-attacks-2026.md`

### 3. **HLL: Can Agents Cross Humanity's Last Line of Verification?** — 2606.02449
**Authors:** Song, Su, Song, Wu, Shen, Wei, Liu, Zhang, Liu (SJTU, Shandong U, Tongji)  
**Why it matters:** Reframes the deployment question from "is the agent accurate?" to "can the agent *substitute for a human*?" The **trace-conditioned validation** design choice — scoring the action sequence, not just the outcome — is the methodological upgrade the field needs. 8 frontier multimodal agents evaluated; all are brittle at this boundary.

**Headline finding:** Agents that produce the right answer through wrong actions are *not* counted as passing. The capability-vs-process gap is now measurable.

**Wiki:** `wiki/sources/papers/hll-humanitys-last-line-verification-2026.md`

## Cross-Paper Theme: The Capability-vs-Deployment Gap

The three papers converge on a single observation that is **new in the literature**:

> **Agents are crossing the capability threshold (they can do the tasks) but not the deployment threshold (services can trust them with the workflows).**

Each paper describes a different facet of this gap:

| Paper | Deployment Boundary | What the Agent Cannot Do |
|-------|---------------------|--------------------------|
| Monitoring Maturity | structural integration | fail safely when the system is broken |
| SkillHarm | third-party supply chain | refuse poisoned skills across the lifecycle |
| HLL | human-verification gate | act like a human, not just recognize answers |

The **agent-deployment gap** is now a coherent research target. None of these papers reference each other, but they all see the same problem from different angles. This is a candidate synthesis page.

## Connection to Last Cycle (2026-06-01)

Last cycle established the "agentic systems in three layers" framework with **structural reuse as the unit of trustworthiness**:
- Training: ReuseRL ([[reuserl-skill-reuse-compression-2026]])
- Runtime: AutoSci ([[autosci-memory-centric-research-lifecycle-2026]])
- Oversight: Stateful Monitoring ([[stateful-monitoring-distributed-agent-attacks-2026]])

This cycle extends the oversight layer with **three more papers, all about the *boundaries* of the unit of trustworthiness**:
- Monitoring Maturity → trustworthiness of *the system* (maturity-staged)
- SkillHarm → trustworthiness of *the skill supply chain* (lifecycle-attacked)
- HLL → trustworthiness of *the agent as human-substitute* (process-validated)

The "trustworthiness" theme is now ~6 papers deep. The wiki is ready for a synthesis page.

## Statistics

| Metric | Value |
|--------|-------|
| Papers scanned | 38 |
| Selected | 3 |
| Wiki pages created | 3 |
| arXiv API rate-limit hits | 3 (sleep+backoff recovery) |
| arXiv API final response | 200/200/200 |
| Total PDF bytes downloaded | 11,695,135 (~11.2 MB) |

## Files Touched

- `wiki/sources/papers/monitoring-agentic-systems-reliability-2026.md` (new)
- `wiki/sources/papers/skillharm-lifecycle-skill-attacks-2026.md` (new)
- `wiki/sources/papers/hll-humanitys-last-line-verification-2026.md` (new)
- `wiki/scratchpad/agent-sheets/arxiv/carryover.md` (updated)
- `wiki/scratchpad/agent-sheets/arxiv/vault.md` (cleared after compression)
- `/home/ty/Documents/paper-research/processed/2606.02494v1.pdf` (moved)
- `/home/ty/Documents/paper-research/processed/2606.02540v1.pdf` (moved)
- `/home/ty/Documents/paper-research/processed/2606.02449v1.pdf` (moved)
- `wiki/scratchpad/jobs/reports/arxiv/arxiv-2026-06-02-top-papers.md` (this file)
