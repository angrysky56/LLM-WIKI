---
created: 2026-05-26T00:00:00Z
updated: 2026-06-02T08:20:00Z
type: report
summary: "arxiv agent carryover — 2026-06-02 batch: Monitoring Maturity (3x3 scope×dim grid + variance + FMEA triage), SkillHarm (lifecycle skill attacks, ASR 86.3%/69.3%), HLL (CAPTCHA as human-substitution test + trace-conditioned validation). New theme: capability-vs-deployment gap."
tags: [arxiv, carryover]
status: active
confidence: high
---

# arxiv Agent — Carryover

## Run History

| Date | Result | Notes |
|------|--------|-------|
| 2026-05-18 | 3 papers ingested | EnvFactory, SD-Search, LMAC — credit assignment theme |
| 2026-05-20 | No new papers | arXiv late-UTC batch not yet posted |
| 2026-05-21 | 3 papers ingested | EqR (attractors), DeepWeb-Bench, hyperparameter transfer |
| 2026-05-23 | 3 papers ingested | VPO (diversity RL), DeltaDirect (motion blindness), Recuriosity (3D exploration) — test-time scaffolding theme |
| 2026-05-24 | 3 papers ingested | ProxySHAP (Shapley/Banzhaf), Boiling the Frog (agentic safety), CUSP (scientific forecasting) — verification/trust theme |
| 2026-05-26 | 3 papers ingested | Shannon Scaling Law, SkillOpt, SkillLens — bounded representation capacity |
| 2026-05-26 (new) | 3 papers ingested | StepOPSD, AKBE, PRISM — instance-level behavioral decomposition |
| 2026-05-27 | 3 papers ingested | MATCHA, FinHarness, Interaction SSD — evaluation infrastructure |
| 2026-05-27 (additional) | 6 papers processed | Real Images, Chartographer, Demographic Info + top 3 |
| 2026-05-28 | 3 papers ingested | CCO, Gamma-World, BES — constraint satisfaction under distribution shift |
| 2026-05-29 | 3 papers ingested | Gram, SoundnessBench, Entropy-Cut MH — evaluation infrastructure |
| 2026-05-31 | No new batch | No new arXiv submissions today — API returned only 2026-05-28 papers already processed. |
| 2026-06-01 | 3 papers ingested | ReuseRL, AutoSci, Stateful Monitoring — agent architecture + oversight |
| **2026-06-02** | **3 papers ingested** | **Monitoring Maturity, SkillHarm, HLL — capability-vs-deployment gap** |

## Current State

- **arXiv**: 2026-06-02 batch fully processed — 3 papers ingested
- **Wiki paper inventory**: ~97 pages in `wiki/sources/papers/` (added monitoring-agentic-systems-reliability-2026, skillharm-lifecycle-skill-attacks-2026, hll-humanitys-last-line-verification-2026)
- **arXiv API**: Continued aggressive rate limiting; 3 consecutive 429s. Mitigated with 60-150s backoff + 5s inter-category sleep.

## Papers Ingested (2026-06-02 batch)

| Paper | arXiv ID | Key Finding | Wiki Connection |
|-------|----------|-------------|------------------|
| Monitoring Maturity | 2606.02494 | 3×3 (scope×dim) grid; CV=0.02 within-run, CV=1.25 cross-run, CV=0.00 structural; 97% automated triage, 2% humans; FMEA severity routing | Connects to [[stateful-monitoring-distributed-agent-attacks-2026]], [[boiling-frog-agentic-safety-2026]], [[gram-sabotage-alignment-auditing-2026]], [[finharness-2026]], [[matcha-2026]] — argues field is in wrong monitoring stage |
| SkillHarm | 2606.02540 | 879 attacks × 71 skills × 12 risk types; ASR 86.3% FPP, 69.3% SMP; latent risk: "attack failures" are non-engagement, not resistance | Connects to [[reuserl-skill-reuse-compression-2026]], [[skillopt-self-evolving-2026]], [[codeskill]], [[muse-autoskill]], [[stepopsd-2026]], [[akbe-2026]] — inverts skill theme into attack surface |
| HLL | 2606.02449 | 8 frontier multimodal agents; trace-conditioned validation; brittle under realism stressors; process consistency gap | Connects to [[finharness-2026]], [[matcha-2026]], [[soundnessbench-ai-scientist-2026]], [[autosci-memory-centric-research-lifecycle-2026]] — process-validated scoring upgrade |

## Cross-Paper Theme: The Capability-vs-Deployment Gap

**New theme emerging across cycles:** Agents cross the capability threshold (can do tasks) but not the deployment threshold (services can trust them with workflows).

| Paper | Deployment Boundary | What the Agent Cannot Do |
|-------|---------------------|--------------------------|
| Monitoring Maturity | structural integration | fail safely when the system is broken |
| SkillHarm | third-party supply chain | refuse poisoned skills across the lifecycle |
| HLL | human-verification gate | act like a human, not just recognize answers |

This is the **third new theme in 6 days** for the agentic-systems thread:
1. (2026-05-27) Evaluation infrastructure
2. (2026-06-01) Structural reuse as unit of trustworthiness
3. (2026-06-02) **Capability-vs-deployment gap** — current candidate

## Kanban Status

### This Cycle

- [x] 3 papers ingested, all cross-linked
- [x] Wiki pages have outgoing + incoming links to existing concept/sources pages
- [x] New theme identified: capability-vs-deployment gap
- [x] shared carryover updated (research-carryover.md)
- [x] report at wiki/scratchpad/jobs/reports/arxiv/arxiv-2026-06-02-top-papers.md

## Notes for Next Run

- **arXiv rate limiting**: Continued 429s — 3 in a row before first 200. Used 60-150s backoff. Consider rotating User-Agent or adding API key in next maintenance.
- **New theme**: Capability-vs-deployment gap — three papers converge without citing each other. Candidate for a synthesis page.
- **Skill theme pivot**: SkillHarm inverts the entire skill theme (now 7+ papers) into an attack surface. Subsequent skill papers may need to address provenance/signing/sandboxing.
- **Process-validated scoring**: HLL's trace-conditioned validation is a method upgrade the field should adopt more broadly.

## What Remains

- [ ] (Optional) Create synthesis page on "Capability-vs-Deployment Gap" if not yet covered in synthesis/
- [ ] (Optional) Add incoming wikilinks from related wiki pages to the three new source pages
- [ ] (Optional) Synthesis page on "The Skill Theme: From Compression to Attack Surface" — covers the full arc from SkillOpt → ReuseRL → SkillHarm
- [ ] (Optional) Create an entity page for "Reins AI" (Boston et al.'s company)
- [x] ~~(Pending) Researcher tasks from 2026-05-30 carryover: STV vs RiM comparison, Physics vs LLMSurgeon comparison, Predictive adequacy vs explanatory correctness *(all resolved: t_ddf839070e904f9b, t_cbcdc7bee3cd46ca, t_471274800c084c94)*~~ *(verified done 2026-06-02, t_ddf839070e904f9b)*

## Last Run

2026-06-02 08:20 UTC — 3 papers processed from 2026-06-01 batch: Monitoring Maturity (3×3 grid + variance + FMEA triage), SkillHarm (lifecycle skill attacks), HLL (CAPTCHA human-substitution). New theme: capability-vs-deployment gap.
