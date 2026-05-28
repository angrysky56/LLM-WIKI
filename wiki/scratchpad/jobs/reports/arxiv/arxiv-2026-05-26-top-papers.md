# ArXiv Daily Report — 2026-05-26

## Papers Processed

### 2605.27140v1 — StepOPSD: Step-Aware Online Preference Distillation for Agent Reinforcement Learning

**Finding**: StepOPSD solves the credit-assignment mismatch in multi-turn agentic RL by decomposing trajectories into causal action-centered step segments and using post-rollout hindsight self-distillation to redistribute credit before the GRPO update. Unlike methods that broadcast trajectory-level reward signals blindly or train a dense value model (unstable/hallucination-prone), it uses stale teacher-student log-probability gaps as a surgical credit reshaper. The two-knob law emerges: tighter αclip provides local stability while λmix governs task-dependent mixing strength. Best/first-place results on ALFWorld Heat (79.1%) and PickTwo (95.0%).

**Wiki path**: `wiki/sources/papers/stepopsd.md`

---

### 2605.26952v1 — Efficient Agentic Reinforcement Learning with On-Policy Intrinsic Knowledge Boundary Enhancement

**Finding**: AKBE discovers that agentic RL training causes cognitive offloading — the model increasingly calls tools unnecessarily due to reward shaping targeting overall tool count. It introduces dual-path on-policy probing (with-tool vs. no-tool rollouts) that per-instance determines whether external tools are genuinely needed, categorizes trajectories into Tool-dependent/Efficiency/Hallucination/Both-wrong, and constructs targeted auxiliary signals. Eliminates 18% of redundant tool calls while improving accuracy by +1.85 on average — no accuracy-efficiency trade-off.

**Wiki path**: `wiki/sources/papers/akbe.md`

---

### 2605.26998v1 — Probabilistic Recurrent Intention Switching Model

**Finding**: PRISM addresses the standard IRL assumption of a single stationary reward by using a recurrent gating network to model per-step intention switching. Proves that the resulting EM objective decomposes exactly into independent per-intention reward subproblems, each solvable in closed form via IAVI (no variational approximation). The O(nK) E-step (vs. O(nK²) for forward-backward alternatives) and ~50K parameter RNN enable training in minutes on a laptop GPU. Recovers nameable intentions (water-seeking/homing/exploration in mouse labyrinth; approach/grasp/carry/idle in robotic manipulation) from unlabeled demonstrations.

**Wiki path**: `wiki/sources/papers/prism.md`

---

## Cross-Paper Theme: Instance-Level Behavioral Decomposition in RL Agents

**The unifying finding**: All three papers decompose behavior at the instance level to resolve misallocation of learning signals — and all find that coarser, trajectory-level signals cause informativity or efficiency pathologies.

|| System | Decomposition Unit | Signal | Key Mechanism |
|--------|--------|-------------------|--------|---------------|
| StepOPSD | Causal action step | Step-aware advantage shaping | Post-rollout hindsight distillation via log-prob gap |
| AKBE | Per-instance tool need | Boundary-guided auxiliary loss | Dual-path (with/no-tool) on-policy probing |
| PRISM | Per-step intention | Closed-form per-intention reward | Recurrent gating + exact EM decomposition |

**Design principle**: When trajectory-level or policy-level learning signals are misaligned with the actual causal unit of decision-making, surgical instance-level decomposition of either the behavior (intent), the advantage (steps), or the environment interaction (tool need) restores correct signal routing without architectural overhaul.

**Meta-pattern**: StepOPSD and AKBE both run as plug-in auxiliary modules alongside GRPO — they don't replace the base RL algorithm, they reshape what signal it receives. PRISM runs offline on demonstrations — its decomposition improves reward function interpretability rather than online policy quality.

---

## Next Cycle Search Direction

- **Causal decomposition in RL**: Papers on causal credit assignment beyond step-level (e.g., causal intervention on action sequences, do-calculus for credit assignment)
- **Knowledge boundary / metacognition in LLMs**: Papers on probing LLM self-knowledge, uncertainty elicitation, internal model calibration — bridging AKBE-style probing to non-RL settings
- **Multi-intention IRL applications**: Papers applying PRISM-like intention segmentation to autonomous driving, game-playing agents, or multi-task dialogue
- **GRPO variants**: Papers improving or analyzing GRPO beyond standard implementations (stale ref, adaptive clipping, advantage normalization)
- **Tool-use efficiency in agents**: Papers measuring or optimizing tool productivity beyond accuracy-only metrics

---

## Related
- [[index]]
- [[scratchpad/jobs/reports/arxiv/arxiv-2026-05-26-top-papers]]

- [[arxiv-2026-05-26-top-papers]]

## Deliverables

| Deliverable | Path |
|-------------|------|
| StepOPSD source page | `wiki/sources/papers/stepopsd.md` |
| AKBE source page | `wiki/sources/papers/akbe.md` |
| PRISM source page | `wiki/sources/papers/prism.md` |
| Text extracts (15k chars each) | `/home/ty/Documents/paper-research/2605.27140v1.txt`, `2605.26952v1.txt`, `2605.26998v1.txt` |
| PDFs | `/home/ty/Documents/paper-research/2605.27140v1.pdf`, `2605.26952v1.pdf`, `2605.26998v1.pdf` |
| This report | `wiki/scratchpad/jobs/reports/arxiv/arxiv-2026-05-26-top-papers.md` |
