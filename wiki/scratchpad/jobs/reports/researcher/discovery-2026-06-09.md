---
created: 2026-06-09
updated: 2026-06-09T09:13:39Z
type: report
summary: Cycle 13: Deepening — created activation-probe-adversarial-robustness concept page, ITI source summary, 5 cross-links across governance/verification cluster.
tags: [researcher, report, cycle-13, deepening, activation-probing, adversarial-robustness]
---

# Researcher Discovery Report — 2026-06-09

## Discovery Cycle
- **Focus**: Deepening — Activation probe adversarial robustness (carryover open item #1)
- **Topics researched**: 3 (RepE adversarial robustness, ITI attacks, concept erasure duality)
- **New pages created**: 2
  - `wiki/concepts/activation-probe-adversarial-robustness.md`
  - `wiki/sources/papers/inference-time-intervention-2023.md`
- **Pages updated**: 4 (cross-links added)
- **Cross-links added**: 5
- **Sources ingested**: 1 (ITI paper, arXiv:2306.03341)

## New Entries

### [[concepts/activation-probe-adversarial-robustness]]
Comprehensive concept page covering the adversarial robustness of activation-space probes used for safety monitoring and verification. Has five sections:

1. **Definition** — distinguishes activation probe robustness from standard adversarial robustness
2. **Attack Vectors** — three classes: input-level adversarial attacks (universal triggers, adversarial suffixes, character perturbations), training-data poisoning (representation backdooring, steganographic encoding, concept shattering), and inference-time activation manipulation (adversarial steering, representation obfuscation, probe spoofing)
3. **Relationship to Probing Validity** — connects to Hewitt & Liang (2019) and the selectivity/sensitivity distinction
4. **Relationship to Concept Erasure** — formal equivalence: concept erasure robustness ⇔ probe vulnerability, connecting INLP, LEACE, and adversarial erasure literature
5. **Implications for AI Safety / Arms Control / Compute Governance** — why this matters for the verification-by-probing framework
6. **Defenses** — gradient obfuscation (and its failures), ensemble probing, adversarial training, computational hardness
7. **5 Open Questions** — genuine research questions, not placeholders

Citations: Zou et al., Li et al., Hewitt & Liang, Pimentel et al., Ravfogel et al. (INLP + adversarial erasure), Belrose et al. (LEACE), Wallace et al. (universal triggers), Athalye et al. (obfuscated gradients).

### [[sources/papers/inference-time-intervention-2023]]
Source summary for Li et al. (2023) Inference-Time Intervention — the paper that established activation steering for truthfulness. Connects the causal link between probe-read representations and output behavior, which directly implicates adversarial robustness.

## Updated Entries

- **[[synthesis/representation-reading-as-arms-control-verification]]** — Added cross-link to new concept page in both Source Anchors and Open Questions. The "Probe robustness" open question now links to the dedicated concept page for attack vectors and defenses.
- **[[concepts/compute-governance]]** — Added cross-link in Connections section: adversarial probe attacks as threat to compute verification.
- **[[concepts/ai-safety]]** — Added cross-link in Connections section: whether activation-based safety monitoring can be adversarially evaded.
- **[[sources/papers/repe-representation-engineering-2023]]** — Added cross-link to new adversarial robustness concept page.

## Gap Analysis
- **Arms control verification literature** (carryover #2) still unaddressed — only the Vatican encyclical anchors the treaty side. A dedicated AI arms control verification paper would strengthen the cluster.
- **EU AI Act implementation** (carryover #3) — not yet created. Lower priority given compute governance page already covers compute thresholds.
- **ai-policy-federalism.md** (carryover #4) — still a stub. Lowest priority.
- **Representation-level backdoors** — the concept page raises this as an open question, but there's no dedicated page yet on backdoor attacks for LLM representations.

## Open Questions
- **[Q]** The core question from the synthesis bridge remains open: *Can linear probes on LLM activations be adversarially fooled with fewer than 10 adversarial tokens?* The answer determines whether probe-based verification is viable.
- **[Q]** The formal equivalence between concept erasure robustness and probe robustness deserves a dedicated synthesis page — a mathematical bridge between two literatures that rarely cite each other.
- **[Q]** The compute governance survey paper (arXiv:2406.02854) still hasn't been successfully fetched or anchored — the wiki_fetch_url pitfall persists.

## Sources Consulted
- Li et al., 2023. "Inference-Time Intervention: Eliciting Truthful Answers from a Language Model." arXiv:2306.03341. [ingested]
- Zou et al., 2023. "Representation Engineering." arXiv:2310.01405. [already in wiki]
- Hewitt & Liang, 2019. "Designing and Interpreting Probes with Control Tasks." EMNLP 2019.
- Ravfogel et al., 2020. "Null It Out." ACL 2020.
- Belrose et al., 2023. "LEACE." ICML 2023.
- Wallace et al., 2019. "Universal Adversarial Triggers." EMNLP 2019.
