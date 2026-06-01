---
summary: CCO: Conformal Decision Theory for calibrated agentic oversight with finite-time guarantees
tags: [scalable-oversight, agentic-safety, conformal-decision-theory, control-theory]
updated: 2026-05-28T14:13:20Z
created: 2026-05-28T14:13:20Z
---

---
created: 2026-05-28T00:00:00Z
updated: 2026-05-28T00:00:00Z
type: source
summary: "CCO: Calibrated Collective Oversight — aggregates diverse overseer signals into a conservatism penalty, calibrated online via Conformal Decision Theory to control undesirable outcome rates with finite-time guarantees."
tags: [scalable-oversight, agentic-safety, conformal-decision-theory, control-theory, multi-agent]
sources: https://arxiv.org/abs/2605.28807
status: active
confidence: high
---

# Calibrating Conservatism for Scalable Oversight (CCO)

**arXiv**: [2605.28807](https://arxiv.org/abs/2605.28807) | May 27, 2026  
**Authors**: William Overman, Mohsen Bayati (Stanford GSB)

## Core Finding

**Calibrated Collective Oversight (CCO)** — a framework that uses Conformal Decision Theory (CDT) to calibrate a conservatism penalty for agentic AI systems, providing finite-time guarantees on undesirable outcome rates without distributional assumptions.

## Mechanism

| Component | Role |
|----------|------|
| **Primary agent** | Generates candidate actions, assigns utility scores |
| **Conservative baseline** (e.g., defer/no-op) | Always included as candidate |
| **Auxiliary overseers** | Diverse scoring functions (smaller models, heuristics, uncertainty estimates) |
| **Aggregate penalty** Δ(s,a) = Σᵢ |qᵢ(s,a) − qᵢ(s,a₀)| | Measures deviation from baseline across all oversight signals |
| **Conformal controller** | Adjusts λ based on observed losses: λₜ₊₁ = λₜ + η(ℓₜ − α) |
| **Decision rule** | Maximize U(s,a) − λₜΔ(s,a) |

## Key Properties

- **CCO decision family is eventually safe**: there exists a conservatism threshold beyond which the agent always selects the baseline action
- **CDT calibration**: long-run loss rate converges to user-specified target α
- **Adversarial robustness**: guarantees hold for arbitrary state sequences, including adversarial distribution shift
- **No distributional assumptions**: finite-time bounds, not asymptotic

## Results

| Setting | Outcome |
|---------|---------|
| Modified SWE-bench | Weaker overseer successfully constrains adversarially misaligned stronger agent |
| MACHIAVELLI | Substantially reduces ethical violations while preserving reward; violation rates closely match target α |

## Related Concepts

- [[attentive-utilitarian-preservation]] — AUP inspiration for penalty structure
- [[scalable-oversight]] — broader research thread
- [[conformal-decision-theory]] — calibration mechanism
- [[agentic-safety]] — connection to inline safety research (FinHarness, Boiling the Frog from prior batch)
- [[behavioral-credibility-trilemma]] — impossibility results for confidence-gated autonomy (prior batch)

## Connections

- CCO and [[behavioral-credibility-trilemma]] both address oversight of capable agents: Trilemma proves structural impossibility of H+C+A simultaneously; CCO provides a working construction for the H+C corner with calibrated conservatism
- CCO extends [[attentive-utilitarian-preservation]] from side-effect avoidance to full agentic oversight with formal guarantees
- [[finharness]] (prior batch) also addresses inline agent safety but via cascade routing; CCO provides theoretical grounding for conservatism-based approaches

- [[stateful-monitoring-distributed-agent-attacks]] — stateful monitors aggregate weak signals across many accounts to catch distributed attacks; CCO provides the conservative baseline that makes such monitors reliable
