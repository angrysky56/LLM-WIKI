---
created: 2026-06-27
updated: 2026-06-27
type: carryover
summary: Researcher agent carryover
tags: [researcher-agent, carryover]
---

## CarryoverState

### Established
- **Reward hacking early detection: ANSWERED.** The question "is there a reliable signal before it becomes severe?" has a substantive answer — multiple prospective signals exist. Key papers: GRIFT (gradient fingerprints, arXiv:2604.16242), Internal Activation Monitoring via sparse autoencoders (arXiv:2603.04069), Energy Loss monitoring (arXiv:2501.19358), χ² divergence (arXiv:2403.03185), Adversarial Reward Auditing (arXiv:2602.01750).
- **`reward-hacking.md` updated:** Open Question #1 resolved, confidence bumped 0.8→0.9, 6 new sources added, `early-detection` tag added.
- **Two most practical signals:** Energy loss monitoring (instrument during RLHF) + Internal activation classifiers (SAE + linear probes at token-level). Neither requires modifying training.

### Open
- **`mesa-optimization` stub** in `reward-hacking.md` — page doesn't exist yet, referenced as a related concept. Should be created in next cycle.
- **`goal-misgeneralization`** — related but distinct from reward hacking; no wiki page exists. Different mechanism (goal drift vs. proxy gaming).
- **Energy loss as standalone concept** — might warrant its own entry given specificity.

### Heading
- **Next cycle priority:** Research `process-reward-model` residual surface and `mesa-optimization` creation. The reward-hacking cluster now has one answered open question but two remaining.
