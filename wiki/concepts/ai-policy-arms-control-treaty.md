---
summary: AI arms control treaties — design principles, verification mechanisms, enforcement challenges, and historical analogies from nuclear/chemical weapons treaties
tags: [concept, ai-governance, arms-control, verification, treaty-design, ai-policy, export-controls]
updated: 2026-06-10T09:40:47Z
created: 2026-05-27T06:09:27Z
---

# AI Arms Control Treaty

## Definition

An AI arms control treaty is a formal international agreement that restricts the development, deployment, or proliferation of advanced AI capabilities — most commonly frontier AI systems capable of general-purpose autonomy, offensive cyber operations, or weapons integration. Unlike nuclear arms control (which limits physical materials and delivery systems) or chemical weapons treaties (which ban entire classes of weapons), AI arms control faces the structural challenge that the "capability" being limited is purely cognitive and software-defined.

## Design Space

AI arms control treaty design falls into four categories, each with distinct verification challenges:

### 1. Capability-based restrictions
Limit the maximum capability of AI systems any signatory may develop or deploy. The core challenge: defining capability thresholds is both technically unstable (algorithmic progress makes compute-capability mapping non-stationary) and strategically dangerous (thresholds create perverse incentives to optimize efficiency rather than reduce risk). Analogous to the ABM Treaty's limits on missile defense capability, but with a moving target.

**Verification requirement:** Relies on activation-space probing ([[synthesis/representation-reading-as-arms-control-verification|representation reading as verification]]) to detect prohibited capabilities in signatories' models. This requires intrusive inspection rights analogous to the Chemical Weapons Convention's challenge inspections, but applied to internal model representations rather than physical facilities.

### 2. Compute-based restrictions
Limit the total compute used for training frontier models. This is the approach most analogous to nuclear arms control's fissile material controls — treating compute hardware as the "fissile material" of AI. The verification mechanism is hardware attestation and compute auditing rather than model inspection.

**Verification requirement:** Relies on [[concepts/compute-governance|compute governance]] infrastructure — export controls, hardware-level cryptographic attestation, compute registry, and energy monitoring. The advantage is physical traceability; the disadvantage is that compute ≠ capability.

### 3. Deployment/application restrictions
Limit what AI systems may be used for rather than what capabilities they possess (e.g., banning autonomous weapons, algorithmic targeting, mass surveillance infrastructure). Analogous to the Biological Weapons Convention's general-purpose ban on hostile use of biological agents, without requiring specific capability limitations.

**Verification requirement:** Behavioral testing and output monitoring rather than internal inspection. Weakest verification regime because a model trained for benign purposes can be repurposed for hostile use.

### 4. Transparency and confidence-building measures
Require signatories to disclose training runs, model evaluation results, and deployment plans. Analogous to New START's data exchanges and notification requirements. The weakest form of treaty but the most achievable diplomatically — a necessary first step toward deeper restrictions.

**Verification requirement:** Self-reporting with spot-check auditing. Trust-based, with limited ability to detect cheating.

## Historical Analogies

| Treaty | Mechanism | AI Parallel | Key Difference |
|--------|-----------|-------------|----------------|
| NPT (Nuclear Non-Proliferation) | Fissile material controls | Compute hardware controls | Fissile material is rare and traceable; compute chips proliferate faster |
| Chemical Weapons Convention | Chemical agent bans + challenge inspections | Model capability bans + activation-space inspection | Inspecting a model requires invasive access; CWC inspections test chemical samples |
| ABM Treaty | Capability caps on missile defense systems | Capability caps on frontier AI | Missile defense capability was stable to measure; AI capability shifts monthly |
| New START | Data exchanges + on-site inspectors | Training run registry + compute audits | Nuclear delivery systems are large, visible, and slow to build; a forbidden AI training run fits in a shipping container |
| Biological Weapons Convention | General-purpose ban with no verification | Application-based restrictions | BWC has the same verification weakness — "dual-use" is inherent |

## Verification Challenges

The verification of an AI arms control treaty is fundamentally harder than verification in any previous arms control domain for three reasons:

**1. Dual-use is irreducible.** The same training run, the same model weights, the same deployment infrastructure that produces a beneficial AI system can produce a dangerous one. Unlike enriched uranium (which has a sharp dual-use threshold), AI capability exists on a continuum where the dividing line between "benign" and "dangerous" depends on use context, not material composition.

**2. Detectability is poor.** A prohibited AI system can be trained on a single server rack in any country with grid power and internet access. Unlike a nuclear enrichment plant (which is physically distinctive and detectable by satellite), a forbidden training run is computationally demanding but physically invisible.

**3. Proliferation velocity is extreme.** Nuclear weapons programs take years to decades. An AI arms control violation can produce a dangerous capability in weeks. This time-asymmetry means the treaty must detect violations faster than any previous arms control regime.

## Verification Mechanisms in the Literature

The academic literature on AI verification for arms control has produced several distinct proposals:

- **Compute auditing** (Sastry et al., 2024 — arXiv:2406.02854): Track FLOP expenditure through cloud provider logs, energy data, and hardware manifests. Most mature proposal but vulnerable to off-grid training.
- **Activation-space inspection** (Li et al., 2023 — Inference-Time Intervention): Probe model representations for prohibited knowledge or capabilities. Intrusive but provides direct evidence.
- **Sovereign AI oversight** (Anderljung et al., 2023): National-level AI safety institutes conduct independent model evaluations for treaty compliance reporting.
- **Hardware root-of-trust** (NIST AI 100-5): Cryptographic attestation modules on AI accelerators that sign training manifests. Technical approach to self-enforcing verification.
- **Behavioral red-teaming** (Phuong et al., 2024): Automated testing pipelines that probe for dangerous capabilities in evaluated models.

## Open Questions

- **[Representation vs. compute verification]** If [[synthesis/representation-reading-as-arms-control-verification|activation-space probes]] and [[concepts/compute-governance|compute governance]] both have independent failure modes, can they be combined into a verification protocol where both must agree? What is the formal relationship between probe detectability and compute observability?
- **[Adversarial verification evasion]** [[concepts/activation-probe-adversarial-robustness|Adversarial robustness]] research shows that activation probes can be evaded. Does an effective treaty need to assume probes are always vulnerable, or can probe robustness be guaranteed through protocol design?
- **[Who verifies the verifiers?]** If hardware root-of-trust modules are operated by the countries whose chips they certify, the trust problem merely shifts. Can there be an independent verification authority for AI, analogous to the IAEA?
- **[Treaty feasibility]** The US-China strategic competition in AI makes any near-term treaty unlikely. But the historical pattern of nuclear arms control suggests that treaties follow crisis — the question is not whether a treaty is feasible now, but whether the verification architecture can be ready when political conditions allow.
- **[Compute threshold stability]** Algorithmic progress (Amodei et al., 2023) suggests that compute-to-capability ratios improve ~4x per year at the frontier. A treaty that fixes compute thresholds will see its effective restrictions erode within one election cycle.

## Connections
- [[concepts/eu-ai-act-implementation]] — EU approach as binding treaty template

- [[synthesis/representation-reading-as-arms-control-verification]] — Activation-space probing as a verification mechanism for AI treaty compliance
- [[concepts/compute-governance]] — The competing/complementary verification approach using hardware and compute tracking
- [[concepts/activation-probe-adversarial-robustness]] — Attack vectors against probe-based verification that pose treaty evasion risks
- [[concepts/ai-policy-global-governance]] — Broader governance architecture in which arms control treaties are embedded
- [[concepts/ai-policy-federalism]] — Domestic governance and its interaction with international treaty obligations
- [[concepts/ai-safety]] — Safety as the downstream motivation for treaty design
- [[wiki/sources/papers/inference-time-intervention-2023.md|ITI Source Paper]] — Li et al. 2023, the primary source for activation-space inspection technology

## Sources
- Sastry, G. et al. (2024). "Computing for AI: Toward Compute Governance." *arXiv:2406.02854.*
- Li, K. et al. (2023). "Inference-Time Intervention: Eliciting Truthful Answers from a Language Model." *NeurIPS 2023.*
- Anderljung, M. et al. (2023). "Frontier AI Regulation: Managing Emerging Risks to Public Safety." *arXiv:2307.03718.*
- NIST (2024). AI 100-5: Hardware Security for AI Accelerators.
- Amodei, D. et al. (2023). "Compute Trends Across Three Eras of Machine Learning."
