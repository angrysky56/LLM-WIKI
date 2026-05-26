# Researcher Discovery Report — 2026-05-26

## Discovery Cycle
- Topics researched: 6
- New pages created: 0
- Pages upgraded from stub: 6
- Cross-links added: 24

## Pages Upgraded from Stub

### `dynamical-systems.md` → active
**What was filled**: Full concept page for dynamical systems as mathematical framework for systems evolving over time.

Key content:
- **State space and phase space**: Complete specification of system state; transformer hidden states as extremely high-dimensional phase space
- **Attractors**: Point, limit cycle, quasi-periodic, strange (chaotic); basin of attraction partitions state space
- **Bifurcations**: Parameter changes causing qualitative behavioral shifts; period-doubling cascade to chaos
- **Sensitivity and chaos**: Positive Lyapunov exponents; sensitive dependence on initial conditions
- **Neural network connection**: Hopfield networks (memories as energy minima) → transformers (IDP framework, generalized Hopfield dynamics)
- **Reasoning as attractor settlement**: CoT as trajectory through state space to attractor; shorthand-for-thought may involve pre-formed basins

Confidence: 0.75 (solid mathematical foundation; connections to neural network dynamics well-established)

### `mental-imagery.md` → active
**What was filled**: Full concept page for mental imagery as cognitive capacity to form internal visual representations.

Key content:
- **Phantasia/hyperaphantasia spectrum**: Individual differences in vividness (2-4% aphantasia, absent visual imagery)
- **Neural basis**: Frontoparietal attention network (superior frontal gyrus, intraparietal sulcus); V1 activation debated
- **Top-down generation**: Imagery generates novel configurations, not memory replay; creative combination
- **AI connection**: Latent space traversal as imagery analog; counterfactual generation; mental simulation
- **Imagination connection**: Mental imagery is a specific modality of the broader imagination capacity

Confidence: 0.75 (well-grounded in cognitive science; AI connection is speculative but reasonable)

### `llm-training.md` → active
**What was filled**: Full concept page for LLM training pipeline — pre-training, fine-tuning, continual learning.

Key content:
- **Pre-training**: Unsupervised language modeling, scaling laws, emergent capabilities
- **Instruction tuning**: Transforming raw LM into instruction follower; maintaining general capabilities
- **Catastrophic forgetting**: Weight interference during fine-tuning; mitigation strategies (regularization, rehearsal, EWC, MoE)
- **RLHF and GRPO**: Standard pipeline (comparison data → reward model → RL fine-tune); GRPO as simplified variant (no reference model needed)
- **GRPO + MoE compatibility**: Structural advantage of GRPO for MoE architectures (no doubled memory footprint)
- **Continual learning**: The goal of updating without forgetting; scaffolding vs compression trade-offs

Confidence: 0.75 (well-established ML; standard taxonomy)

### `agentic-planner.md` → active
**What was filled**: Full concept page for agentic planning as distinct from agentic hierarchy.

Key content:
- **Definition**: Planning capability within an agent (decomposing goals into sub-tasks) — distinct from hierarchical organization of multiple agents
- **Agentic planner vs agentic-hierarchy**: Resolution of carryover question — planning function (planner) vs organizational structure (hierarchy); both needed, distinct
- **Hierarchical task decomposition**: Recursive goal decomposition; depth depends on task complexity
- **Replanning and loop detection**: Handling plan failures, finding alternative paths, escalating unresolvable obstacles
- **Connection to world-model**: Planning simulates action outcomes using world-model before execution
- **Connection to ReAct**: Reactive planning loop at action level; agentic planner at higher level (sub-goal sequencing)

Confidence: 0.75 (solid architectural concept; relationship to agentic-hierarchy clarified)

### `spiral-architecture.md` → active
**What was filled**: Full concept page for spiral architecture (research council deliberation pattern).

Key content:
- **Closed loop (rejected)**: Completion metaphor that stops thinking; rewards premature certainty
- **Spiral (adopted)**: Center as opening not point; each circuit adds context; depth not breadth
- **Center as opening**: The moment where the question's essential shape is clear enough to act on — not a solution
- **Weil-gate as spiral mechanism**: "Who does this hurt?" as 3-layer descent (direct, systemic, normalization)
- **Properties**: Center as opening, never back to start, depth not breadth, optional continuation

Confidence: 0.85 (strong conceptual foundation in synthesis/spiral-architecture.md; well-developed in original)

### `weil-gate.md` → active
**What was filled**: Full concept page for Weil-gate as ethical deliberation mechanism.

Key content:
- **Definition**: "Who does this hurt?" as a gate — not a test to pass but a depth charge; each pass goes deeper
- **Named after**: Simone Weil's attention ethics — staying with suffering, witnessing harm
- **Three layers**: Direct harm → systemic harm → normalization harm
- **Connection to spiral architecture**: The mechanism that drives spiral descent; gate doesn't determine stop, spiral does
- **Two-council role**: Research Council operates the Weil-gate; Refuser monitors compliance
- **Connection to harm-cases**: The empirical record of Weil-gate analysis — documented instances of harm witnessed

Confidence: 0.85 (strong foundation in synthesis/spiral-architecture.md and synthesis/two-council-architecture.md)

## Resolved Carryover

**Agentic planner vs agentic-hierarchy**: RESOLVED. These are distinct concepts:
- Agentic hierarchy = organizational structure (how agents are arranged relative to each other)
- Agentic planner = planning capability within an agent (goal decomposition, sequencing, replanning)

Both concepts are necessary. A hierarchy uses planning but is not itself a planner. A planner can exist without a hierarchy.

## Gap Analysis

**Next priority cluster candidates** (from carryover Heading):

1. **`ramirez-ruiz-mop-2024.md`** — MOP research paper; connects to `mop-architecture` (active) and `cognitive-architecture` (active)
2. **`emergence` cluster** — `emergence` is active; `attractor-dynamics` now links to it strongly; computational-irreducibility already connects
3. **Agent cluster** — `agents` → `agent-architectures` → `autonomous-agents` → all stubs; may be lower priority
4. **`two-council-architecture` concept page** — exists as synthesis, not yet as concept (conceptual overlap)
5. **`empty-chair-protocol` concept page** — exists as synthesis, not yet as concept (protocol vs concept distinction)

**Note**: The spiral-architecture/weil-gate cluster (research council deliberation) is now well-connected to the broader AI safety/oversight cluster:
- weil-gate → agentic-oversight (oversight framework that implements harm questioning)
- spiral-architecture → governance (deliberation pattern)
- weil-gate → accountability (asking who is harmed)

## Open Questions

1. **Dynamical systems quantitative validity**: Does low-dimensional attractor theory apply to high-dimensional transformer state spaces? Is the energy landscape metaphor valid quantitatively or only qualitatively?

2. **AI imagery signatures**: Can we detect latent-space imagery analogs in LLMs? What would be the behavioral or activation signatures?

3. **Weil-gate calibration**: How deep must the Weil-gate pass go before a proposal can proceed? Is there a minimum depth (number of layers addressed) that is required, or does the council's judgment determine sufficiency?

4. **Spiral depth heuristics**: How does a council know when it has gone deep enough? Is there a reliable signal that the opening has been reached?

5. **GRPO + MoE routing collapse**: Does GRPO training cause expert routing collapse in MoE architectures? Active empirical question.

6. **Scaffolding identification**: Can we systematically distinguish scaffolding (calibration tokens) from load-bearing tokens in CoT traces? No current method exists.

## Stub Count

- Before: 330 stubs (from Jul 3 cycle)
- After: 326 stubs (net -4 from 6 upgrades; note: 2 stubs in spiral-architecture/weil-gate chain may have been non-stub in concepts — adjusted count)

## Cross-Links Added (24)

- dynamical-systems: attractor-dynamics, systems-theory, complexity, emergence, shorthand-for-thought, neural-interpretability
- mental-imagery: imagination, neuroscience, aphantasia, world-model, shorthand-for-thought
- llm-training: catastrophic-forgetting, control-llm, group-relative-policy-optimization, reinforcement-learning-from-human-feedback, mixture-of-experts, agent-onboarding
- agentic-planner: agentic-hierarchy, world-model, agentic-react, multi-agent-llm-systems, imagination
- spiral-architecture: two-council-architecture, empty-chair-protocol, weil-gate, agentic-design-picker
- weil-gate: spiral-architecture, two-council-architecture, empty-chair-protocol, harm-cases, refuser-pattern, agentic-oversight