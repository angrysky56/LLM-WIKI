## CarryoverState

### Established
- **Reward hacking early detection: ANSWERED.** Multiple prospective signals exist. Key papers: GRIFT (gradient fingerprints, arXiv:2604.16242), Internal Activation Monitoring via sparse autoencoders (arXiv:2603.04069), Energy Loss monitoring (arXiv:2501.19358), χ² divergence (arXiv:2403.03185), Adversarial Reward Auditing (arXiv:2602.01750). Two most practical: energy loss monitoring + internal activation classifiers (SAE + linear probes at token-level). reward-hacking.md §Early Detection complete, Open Question #1 struck through.
- **MoE routing collapse under RLHF:** Confirmed via SafeMoE (Kim 2025) across 7B–141B models. Monitoring is mitigation only.
- **Hybrid reward models:** ELHSR + SD-Search combining hidden-state outcome scoring with process-level self-distillation. hybrid-reward-models.md created.
- **Adaptive budget learning:** 5 training approaches documented (supervised losses, RL, teacher-guidance/TGR-MoE, two-stage). adaptive-budget-learning.md created.

### Open
- **`mesa-optimization` stub** in reward-hacking.md — page doesn't exist yet, referenced as related concept. Should be created.
- **`goal-misgeneralization`** — related but distinct from reward hacking (goal drift vs. proxy gaming). No wiki page.
- **Energy loss as standalone concept** — may warrant its own entry given specificity.
- **Process reward models residual surface** — PRMs reduce but don't eliminate hacking. What's the residual surface?

### Heading
- **Next cycle priority:** Research `process-reward-model` residual surface and create `mesa-optimization.md`. The reward-hacking cluster has one answered open question but two remaining stubs.