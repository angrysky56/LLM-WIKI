---
summary: Policies and technical mechanisms for controlling access to AI-relevant compute resources — export controls, compute thresholds, hardware attestation, and their role as a verification mechanism in AI arms control
tags: [concept, ai-governance, compute-governance, arms-control, export-controls, ai-policy, verification]
updated: 2026-06-08T14:16:05Z
created: 2026-06-08T14:16:05Z
---

# Compute Governance

Compute governance refers to policies, regulations, and technical mechanisms that control access to the computational resources (hardware, cloud clusters, data center capacity) required to train and deploy advanced AI systems. It is a distinct but complementary approach to AI regulation compared to model licensing, output filtering, or safety alignment — operating at the hardware layer rather than the software or behavioral layer.

## Definition

Compute governance encompasses any policy or technical system designed to monitor, allocate, restrict, or verify access to AI-relevant compute. The core insight is that large-scale AI training is physically constrained: training a frontier model requires thousands of GPUs running for weeks, consuming megawatts of power in specialized data centers. This physical traceability makes compute a natural enforcement chokepoint.

The concept sits at the intersection of:

1. **Export controls** — Restricting cross-border transfer of high-performance AI chips (e.g., US BIS export restrictions on NVIDIA H100/H200/B200 GPUs to China)
2. **Compute quotas** — Domestic allocation systems that require approval for training runs above a compute threshold (proposed in the EU AI Act and California SB 1047 framework)
3. **Cloud compute verification** — Mechanisms for verifying the identity, purpose, and capability level of cloud-based training runs
4. **Hardware-level trust anchors** — Cryptographic attestation built into AI accelerators that can verify model properties at training time (e.g., hardware root-of-trust for training integrity)
5. **Energy monitoring** — Data center power consumption as a proxy for compute usage (less granular but harder to falsify)

## Rationale

The argument for compute governance follows from the verification problem in AI arms control: *AI capabilities are not physically traceable in the same way nuclear materials are.* However, the *compute required to produce those capabilities* is physically traceable.

| Governance Layer | Traceability | Enforceability | Granularity |
|---|---|---|---|
| Model weights | Low (easily copied) | Low | High |
| Output/text | None | None | N/A |
| Compute hardware | High (physical) | High (customs/seizure) | Low |
| Compute usage | Medium (cloud logs) | Medium (audit) | Medium |

## Relationship to AI Arms Control

Compute governance is often presented as the competing — or complementary — verification mechanism to [[synthesis/representation-reading-as-arms-control-verification|activation-space probing]].

**Competing argument:** If you can verify compliance by tracking compute inputs (how many FLOP went into a training run, was the compute purchased through approved channels), you don't need to probe internal model representations. This is the approach favored by hardware-side governance advocates.

**Complementary argument:** Compute tells you *how much* training happened, but not *what* capabilities emerged. Two models trained on the same number of FLOP can have vastly different capabilities. Activation-space probes tell you *what capabilities exist* but not *how they were produced*. Together, they provide dual verification.

## Key Policy Mechanisms

### Export Controls (Active)

The US Bureau of Industry and Security (BIS) has implemented escalating restrictions on AI chip exports since October 2022, including:
- Performance density caps (processed in terms of TPUs)  
- Worldwide licensing requirements for advanced AI chips
- "Chip fence" agreements with allied nations (Japan, Netherlands, South Korea)

These are the most mature form of compute governance, but they face evasion risks: smuggling, third-country fabrication, and declining foreign chip manufacturing capability.

### Compute Thresholds (Proposed)

The EU AI Act introduces compute-based triggers: models trained above 10^25 FLOP for general-purpose AI and 10^26 FLOP for high-impact models face stricter transparency and risk management requirements. California's SB 1047 (vetoed 2024, reintroduced 2025) proposed similar thresholds.

The critical open question: *Can compute thresholds be verified without developer cooperation?* The UK's Frontier AI Taskforce has explored independent compute auditing as a research direction.

### Hardware Attestation (Emerging)

Hardware-level trust anchors — cryptographic modules on AI accelerators that digitally sign training manifests — represent a technical approach to making compute governance self-enforcing. If every training run must be signed by an attested hardware module, the chip itself becomes a verification instrument.

No production system currently implements this, but it is under active research (see NIST AI 100-5 hardware security guidelines).

## Open Questions

- **[Verify compute vs. verify capability]** Can compute verification stand alone, or does the field need a multi-layer verification framework combining compute auditing + activation probes + behavioral testing?
- **[Adversarial compute]** If training compute is capped, what prevents a hostile actor from training a dangerous model on a smaller number of more capable chips, or distributing training across many smaller clusters?
- **[Sovereignty and evasion]** Can export controls survive as a long-term governance mechanism given the proliferation of AI chip fabrication capability (China's SMIC, Huawei Ascend)?
- **[Compute ≠ capability]** The core objection: Amodei et al. (2023) demonstrated that algorithmic improvements make compute-capability mapping unstable. A breakthrough architecture could achieve the same capability at 1/100th the compute.

## Connections

- [[concepts/ai-policy-arms-control-treaty]] — Compute governance as a verification mechanism in treaty design
- [[synthesis/representation-reading-as-arms-control-verification]] — The competing/complementary verification approach
- [[concepts/ai-policy-global-governance]] — Broader governance architecture
- [[concepts/ai-safety]] — Safety as the downstream motivation for governance
- [[concepts/ai-policy-federalism]] — Domestic governance distribution (federal/state tension)

## See Also

- EU AI Act (compute threshold provisions, Article 51)
- US BIS Export Controls on Advanced Computing Chips (2022–2026)
- UK Frontier AI Taskforce Compute Auditing Initiative
- NIST AI 100-5 Hardware Security for AI Accelerators

## Open Questions

1. Can compute thresholds be reliably verified without developer cooperation from sovereign cloud providers?
2. If hardware attestation becomes mandatory, who holds the root-of-trust keys?
3. What is the correct compute-to-capability mapping for AI safety regulation, and how frequently must it be updated?
4. Do export controls create a "compute iron curtain" that accelerates non-Western AI chip development?
5. Can activation-space probes ([[synthesis/representation-reading-as-arms-control-verification]]) and compute governance be combined into a unified verification protocol with independent failure modes?
