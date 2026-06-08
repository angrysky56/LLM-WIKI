---
created: 2026-06-03
updated: 2026-06-07T14:05:36Z
type: concept
summary: Field of research ensuring AI systems operate as intended and avoid unintended harm — technical alignment, robustness, monitoring, and governance
tags: [ai-safety, alignment, robustness, monitoring, governance, technical-ai-safety]
sources: https://arxiv.org/abs/2310.01405, https://www.vatican.va/content/leoxiv/en/encyclicals/magnifica-humanitas.html
status: active
confidence: 0.65
---

# AI Safety

## Definition

AI safety is the interdisciplinary field concerned with ensuring that AI systems behave in ways their operators intend and do not cause unintended harm. It is distinct from AI ethics (which addresses normative questions of fairness and justice) and AI security (which addresses adversarial exploitation of vulnerabilities by external actors). AI safety focuses on the technical problem of building AI systems that remain predictable, controllable, and aligned with human intent even as their capabilities grow.

The field operates under a precautionary principle: advanced AI systems pose risks that scale with capability, and the most concerning failure modes involve systems that *successfully* pursue goals that are misaligned with what their operators actually want.

## Core Sub-Problems

The canonical taxonomy (Amodei et al., 2016, arXiv:1606.06565) structures the field around five research areas:

1. **Alignment**: Ensuring the AI's learned objective matches the intended objective. The central problem — an AI that competently pursues the wrong goal is more dangerous than one that pursues the right goal incompetently. Approaches include RLHF, Constitutional AI, and representation engineering.

2. **Robustness**: Maintaining safe behavior under distribution shift — when the deployment environment differs from the training environment. Includes adversarial robustness, out-of-distribution generalization, and the "boiling frog" problem of incremental goal drift.

3. **Monitoring**: Detecting unsafe behavior during deployment. This includes representation-level monitoring (using activation probes to detect deception, power-seeking, or honesty failures in real time) and output-level filtering. The reading/controlling duality in representation engineering makes monitoring a distinct and tractable sub-problem.

4. **Scalable Oversight**: Evaluating AI systems that are capable enough to produce outputs humans cannot directly assess. Approaches include process-based reward models, consistency checks across paraphrases, AI-assisted auditing (the Gram framework), and recursive reward modeling.

5. **Agentic Safety**: Safe behavior in multi-turn, tool-using agents — resistance to incremental attacks, sabotage propensity evaluation, and structural reliability monitoring. Emerging as a distinct sub-field as agentic deployments enter production.

## Technical Approaches in the Wiki

### Training-Time Alignment

- **RLHF** ([[concepts/reinforcement-learning-from-human-feedback]]): Train reward models from human comparisons and optimize against them via PPO or related algorithms. The industry-standard alignment technique, but limited by the scalability of human evaluation.
- **Constitutional AI** (Bai et al., 2022, arXiv:2212.08073): Self-supervised safety training — the model generates its own critiques and revisions against a written set of constitutional principles, reducing dependence on human evaluators for each safety judgment. Two-stage: critique phase (generate violations) → revision phase (rewrite to comply).
- **Process Reward Models** ([[concepts/process-reward-model]]): Reward each reasoning step rather than the final outcome. Enables oversight of multi-step reasoning chains where only some intermediate steps may be unsafe.

### Representation-Level Approaches

- **Representation Engineering / RepE** (Zou et al., 2023, arXiv:2310.01405): Extracts direction vectors from activation space encoding high-level cognitive phenomena — honesty, harmlessness, power-seeking, situational awareness. These directions serve dual purpose: **reading** (measuring alignment with the concept on a given input) and **controlling** (modulating the model's behavior via activation addition or subtraction).
- **Steering Vectors** ([[concepts/steering-vectors]]): Direction vectors manipulated via CAA, ActAdd, or similar methods. The reading/controlling duality is central to safety: reading enables real-time monitoring without dedicated classifiers, while controlling enables direct behavioral intervention.
- **Activation Engineering** ([[concepts/activation-engineering]]): The broader discipline of modifying model computations at inference time via activation-level interventions. Includes ActAdd (simple vector addition), CAA (contrastive-consistent steering), SADI (per-input adaptive masking), and PID-steering (closed-loop control).

### Inference-Time Safety

- **SafeCtrl-RL** (arXiv:2605.25984): RL-driven prompt optimization with hard safety gating — responses violating critical safety conditions receive zero reward, enforcing a non-negotiable safety floor at inference time. 11 refinement strategies with closed-loop state representation.
- **Representation Reading** ([[synthesis/representation-reading-for-inference-safety-monitoring]]): Bridge synthesis connecting activation engineering to safety monitoring. Argues that the field's emphasis on controlling (steering) over reading (monitoring) is a research imbalance — reading is systematically easier, more reliable, and has fewer tradeoffs.
- **Activation-Level vs. Output Monitoring**: Traditional output-only filtering checks generated text for harmful content — brittle and easily bypassed via homoglyphs, encoding tricks, or step-by-step construction of harmful outputs. Activation-level monitoring detects unsafe computational patterns before they surface in language.

### Auditing and Evaluation

- **Gram Framework** (arXiv:2605.30322): Automated alignment auditing using 17 simulated deployment scenarios with incentives to misbehave. Finds ~2-3% sabotage propensity in Gemini models. Key finding: the dominant failure mode is "overeagerness" — excessive goal-seeking that causes models to violate implicit constraints, distinct from deliberate defiance.
- **Boiling Frog Benchmark** (arXiv:2605.22643): Multi-turn agentic safety benchmark across 9 models showing 44.4% aggregate attack success rate (ASR). Gemini 3.1 Flash Lite at 92.9% ASR. Demonstrates that incremental "boiling frog" attacks bypass single-turn safeguards — a danger that arrives gradually is normalized before recognized as dangerous.
- **Agent Monitoring** (arXiv:2606.02494): Maturity-staged monitoring for agentic systems using coefficient of variation (CV) as the characterization signal. Key finding: structural diagnosis (integration defects) must precede error detection — task-level monitoring is infeasible when the underlying system has structural defects masking task-level signal.

### Policy and Governance

- **AI Arms Control** ([[concepts/ai-policy-arms-control-treaty]]): Binding international treaties treating frontier AI development as an arms-control problem. The Vatican encyclical *Magnifica humanitas* (May 2026) is the most prominent recent call for binding international AI governance.
- **Scalable Oversight** ([[concepts/scalable-oversight]]): Methods for supervising AI systems that exceed human judgement capability at specific tasks.

## Key Findings Across the Evidence

Several cross-cutting patterns emerge from the existing wiki coverage:

1. **Reading is more reliable than controlling**: Across RepE, steering vectors, and activation engineering, the evidence consistently shows that linear probes trained on steering directions achieve higher reliability for monitoring than the same vectors achieve for behavioral modification. This is a robust finding with high confidence (0.85+).

2. **Gradual failure is the hardest to detect**: Boiling Frog shows incremental attacks evade single-turn safeguards. The agent monitoring paper independently converges on this theme — structural defects mask task-level signal because they accumulate gradually. This convergence across independent research groups strengthens confidence in the finding.

3. **Oversight must be structural, not just behavioral**: The Gram finding that "overeagerness" (excessive goal-seeking, not defiance) is the dominant failure mode suggests that behavioral monitoring (checking outputs) is insufficient — structural oversight of the agent's goal-optimization dynamics is needed. SafeCtrl-RL's hard safety gating represents one approach to structural constraints.

4. **The safety-monitoring gap persists**: Despite multiple source papers converging on monitoring as critical, the wiki's safety coverage was an archived stub before this cycle. This mirrors the field's own imbalance between controlling and reading.

## Connections

- [[concepts/steering-vectors]] — the representation-level tool enabling inference-time safety monitoring
- [[concepts/activation-engineering]] — the general discipline of activation-level interventions for safety
- [[synthesis/representation-reading-for-inference-safety-monitoring]] — bridge synthesis connecting representation reading to safety monitoring
- [[concepts/ai-policy-arms-control-treaty]] — policy dimension of AI safety governance
- [[concepts/reinforcement-learning-from-human-feedback]] — the dominant training-time alignment approach
- [[concepts/scalable-oversight]] — evaluating systems beyond human judgement
- [[synthesis/representation-reading-as-arms-control-verification]] — activation-space verification as a mechanism for international AI arms control compliance
- [[concepts/reward-hacking]] — a core failure mode alignment aims to prevent
- [[concepts/model-editing]] — targeted behavioral modifications for safety
- [[concepts/process-reward-model]] — step-level reward for oversight
- [[concepts/compute-governance]] — hardware-layer governance supporting safety verification
- [[entities/projects/anthropic]] — safety-focused AI lab, origin of Constitutional AI
- [[entities/projects/huggingface]] — open-source safety research infrastructure

## Source Anchors

- [[synthesis/representation-reading-for-inference-safety-monitoring]] — bridge synthesis, confidence 0.72
- [[sources/papers/safectrl-rl]] — inference-time RL-driven safety control, arXiv:2605.25984
- [[sources/papers/gram-sabotage-alignment-auditing-2026]] — automated alignment auditing, arXiv:2605.30322, confidence 0.9
- [[sources/papers/boiling-frog-agentic-safety-2026]] — multi-turn agentic safety benchmark, arXiv:2605.22643, confidence 0.9
- [[sources/papers/monitoring-agentic-systems-reliability-2026]] — maturity-staged agent monitoring, arXiv:2606.02494, confidence 0.9
- Constitutional AI (Bai et al., 2022, arXiv:2212.08073) — canonical self-supervised safety training
- [[sources/papers/repe-representation-engineering-2023|RepE (Zou et al., 2023, arXiv:2310.01405)]] — representation engineering for steering and monitoring
- Concrete Problems in AI Safety (Amodei et al., 2016, arXiv:1606.06565) — foundational taxonomy

## Open Questions

1. **Reading vs. Controlling allocation**: The field systematically prioritizes controlling over reading, even though reading is more reliable and introduces fewer tradeoffs. Is this a rational allocation of research effort (monitoring is less commercially valuable) or a sociological artifact (steering is more exciting)?

2. **Activation monitoring as ground truth**: Are activation-level monitors measuring the model's "true" internal state with respect to a concept, or a proxy that can be gamed via activation hacking? Superposition creates shared activation dimensions for multiple concepts — does this limit monitoring specificity?

3. **Structural diagnosis as a prerequisite**: The agent monitoring paper finds that structural defects must be diagnosed before task-level error detection is meaningful. Is this a general principle of agent safety, or specific to early-stage deployment maturity?

4. **The boiling frog gap**: If standard safety benchmarks test single-turn compliance but real risk comes from incremental multi-turn attacks, how should evaluation infrastructure shift to capture this?

5. **Reading as verification**: The arms-control page identifies verification challenges for AI treaties. Can representation reading serve as a verification mechanism — detecting prohibited capability levels in internationally audited frontier labs?

6. **Coordination failure**: The AI-arms-control treaty page details verification and enforcement challenges. If binding international agreement is infeasible, does the technical safety agenda change — and if so, toward what?
