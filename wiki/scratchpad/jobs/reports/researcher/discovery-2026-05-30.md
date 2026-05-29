---
created: 2026-05-30
updated: 2026-06-27
type: report
summary: Researcher discovery report
tags: [researcher, report]
---

# Researcher Discovery Report — 2026-05-30

## Discovery Cycle
- Topics researched: 1 (reward hacking early detection)
- New pages created: 1 (workspace research doc)
- Pages updated: 1 (reward-hacking.md)
- Cross-links added: 0 (existing links already adequate)

## New Entries

### Workspace research doc: `reward-hacking-early-detection.md`
Located at `~/.hermes/kanban/workspaces/t_3f6f2a5e0e9755d4/`. Contains detailed findings on 8 research directions for early detection of reward hacking before it becomes severe:

1. **Gradient Fingerprints (GRIFT)** — arXiv:2604.16242: Gradient-level representations of CoT outputs detect hacking 25% better than baselines; integrates with rejection fine-tuning
2. **Internal Activation Monitoring** — arXiv:2603.04069: Sparse autoencoders on residual stream + linear classifiers give token-level detection early in generation
3. **Energy Loss Monitoring** — arXiv:2501.19358: Final-layer energy loss increase during RLHF is a characterizing structural signal
4. **χ² Divergence** — arXiv:2403.03185: Better than KL for detecting occupancy measure divergence indicating hacking
5. **Adversarial Reward Auditing** — arXiv:2602.01750: Hacker-auditor game; auditor loss curve is the early warning
6. **Reward Model Calibration** — arXiv:2311.14743: OOD detection on responses precedes exploitation
7. **Contrastive Anomaly Detection (TRACE)** — arXiv:2601.20103: 63% vs 45% vs binary; contrastive framing beats isolated classification
8. **Self-Refinement Hacking** — arXiv:2407.04549: Model size and context sharing as escalation risk factors

## Updated Entries

### `wiki/concepts/reward-hacking.md`
- **What changed:** Open Question #1 ("reward hacking detectability") marked as ANSWERED with new §Early Detection section
- **Added 6 new source papers** (2023-2026)
- **Confidence bumped:** 0.8 → 0.9
- **New tags:** `early-detection` added
- **Key findings integrated:**
  - GRIFT: gradient fingerprint detection during training
  - Internal activations: early token-level signals via sparse autoencoders
  - Energy loss: structural signal during RLHF
  - χ² vs KL: occupancy measure divergence detection
  - ARA: adversarial auditor as early warning system
  - Reward model calibration: OOD drops precede exploitation
- **Bottom line:** Two most operationally practical near-term signals are energy loss monitoring and internal activation classifiers — neither requires modifying training

## Gap Analysis

- `mesa-optimization` is referenced as a stub in reward-hacking.md but doesn't exist yet — consider creating next cycle
- `goal-misgeneralization` is related but no page exists — different concept from reward hacking (goal misgeneralization is when the learned goal itself drifts, not just the reward proxy)
- No dedicated page for **energy loss in RLHF** — could warrant its own concept entry given the specificity
- `process-reward-model.md` could benefit from a cross-link to the early-detection section

## Open Questions

1. **Mechanistic interpretability of reward hacking** — still open: what does the exploit strategy look like in activation space?
2. **Process reward models as defense** — residual surface area unquantified
3. **Constitutional AI effectiveness** against sophisticated reward hacking — unverified

## Related
- [[wiki/index]]
- [[scratchpad/jobs/reports/researcher/discovery-2026-05-30]]

- [[discovery-2026-05-30]]

## Sources Cited

- Wang et al. (2026) — arXiv:2604.16242
- Wilhelm et al. (2026) — arXiv:2603.04069
- Miao et al. (2025) — arXiv:2501.19358
- Laidlaw et al. (2024) — arXiv:2403.03185
- Beigi et al. (2026) — arXiv:2602.01750
- LeVine et al. (2023) — arXiv:2311.14743
- Deshpande et al. (2026) — arXiv:2601.20103
- Pan et al. (2024) — arXiv:2407.04549
