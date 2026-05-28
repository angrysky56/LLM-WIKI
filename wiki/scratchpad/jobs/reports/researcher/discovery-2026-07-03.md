# Researcher Discovery Report — 2026-07-03

## Discovery Cycle
- Topics researched: 5
- New pages created: 0
- Pages upgraded from stub: 5
- Cross-links added: 18

## Pages Upgraded from Stub

### `creativity.md` → active
**What was filled**: Full concept page for creativity as a cognitive and AI capability.

Key content:
- **Definition**: Novel, useful output generation — spans from combinatorial recombination to genuine origination
- **Divergent/convergent framework**: Divergent = explore many possibilities; convergent = evaluate and select best candidates
- **Connection to parallel-reasoning**: Parallel reasoning is the convergent phase for verifiable domains; creative evaluation has no Bradley-Terry equivalent for subjective outputs
- **Evaluation challenge**: The central unsolved problem — objective metrics measure fidelity, not creativity; human evaluation is expensive and subjective
- **Connections**: parallel-reasoning (selection mechanism), generative-ai (output medium), imagination (generative substrate), in-context-learning, shorthand-for-thought

Confidence: 0.70 (solid conceptual foundation; empirical basis in creativity research literature)

### `attractor-dynamics.md` → active
**What was filled**: Full concept page for attractor dynamics in dynamical systems and neural networks.

Key content:
- **Definition**: How system states evolve toward stable configurations (attractors) — energy minima, basins of attraction
- **Hopfield networks**: Canonical model — content-addressable memory via energy minima as attractors
- **Attention as generalization**: Transformer attention mechanisms generalize Hopfield network dynamics (IDP framework)
- **Reasoning as attractor settlement**: CoT as path through state space to attractor state; shorthand-for-thought may be about pre-formed basins
- **Connection to emergence**: Emergent capabilities are reorganizations of the energy landscape creating/destroying attractor basins
- **Attractor types**: Point, cyclic, quasi-periodic, strange (chaotic); LLMs may use all four for different tasks

Confidence: 0.75 (solid mathematical foundation; clear connections to neural network dynamics)

### `generative-ai.md` → active
**What was filled**: Full concept page for generative AI as the output medium (text, code, image, audio) via learned distributions.

Key content:
- **Definition**: Systems that produce outputs by sampling from learned probability distributions; four architecture families (autoregressive, diffusion, VAE, flow-based)
- **Generation pipeline**: Representation learning → latent space structure → sampling
- **CFG as divergent/convergent dial**: High guidance = convergent (safe, on-distribution); low = divergent (surprising)
- **Connection to creativity**: CFG and parallel-reasoning selection mechanism are both convergent phases; evaluation is the unsolved problem
- **Mode collapse**: Failure mode where the model only generates a subset of possible outputs
- **Connections**: creativity (convergent evaluation), parallel-reasoning (selection mechanism), llm-reasoning (reasoning as constrained generation), diffusion-models

Confidence: 0.75 (well-established field; standard taxonomy)

### `wolfram-nks-causal-networks.md` → active
**What was filled**: Full concept page for Stephen Wolfram's causal network interpretation of computation and spacetime.

Key content:
- **Definition**: Causal networks = directed graphs where nodes = updating events, edges = causal dependencies; underlying framework for [[wolfram-physics-project]] and [[computational-irreducibility]]
- **Multiway rewrite systems**: All branches exist simultaneously; multiway system represents all possible computations
- **Causal disruption**: Multiway branching creates divergent histories; physical indeterminacy
- **Distinction from causal reasoning**: NKS causal networks = structural representation of computation (what computes what); LLMs causal reasoning = statistical inference of what predicts what
- **Connection to emergence**: Topological properties of causal networks emerge from local rules
- **Connections**: wolfram-physics-project, computational-irreducibility (the key link), causal-networks (distinction), stephen-wolfram

Confidence: 0.75 (established Wolfram framework; non-controversial within NKS community)

### `imagination.md` → active
**What was filled**: Full concept page for imagination as the cognitive capacity to form internal representations of absent/hypothetical scenarios.

Key content:
- **Definition**: Cognitive capacity for mental simulation — running internal models of the world without external input; encompasses mental imagery, counterfactual reasoning, scenario construction
- **AI conceptions**: Latent space traversal, counterfactual generation, scenario construction, internal simulation (shorthand-for-thought)
- **Connection to creativity**: Imagination = divergent generative substrate; [[parallel-reasoning]] selection = convergent evaluation
- **World-model substrate**: Imagination runs on world models; [[world-model]] provides the internal representation structure
- **Emergence connection**: CoT emergence may reflect the development of compressed reasoning simulations — "imagining" rather than generating token-by-token
- **Connections**: creativity, world-model, mental-imagery, counterfactual-reasoning, shorthand-for-thought, llm-reasoning

Confidence: 0.70 (solid cognitive science basis; AI application is more speculative but well-grounded)

## Gap Analysis

**Next priority cluster candidates** (from carryover Heading):

1. **`dynamical-systems`** — stub, needed to support attractor-dynamics now that it's active. Links to systems-theory, complexity, emergence
2. **`mental-imagery`** — stub, was referenced in imagination but remains empty; connects to neuroscience and imagination
3. **`emergence` cluster** — `emergence` is already active but `attractor-dynamics` now connects to it; the attractor-dynamics → emergence → computational-irreducibility thread is now strong
4. **`ramirez-ruiz-mop-2024.md`** — MOP research, connects to `mop-architecture` (active) and `cognitive-architecture` (active)
5. **`llm-training.md`** — has substantive content (22 lines), links to 4 active concepts (catastrophic-forgetting, control-llm, grpo, rlhf); upgrade candidate
6. **`spiral-architecture.md`** — connects to `two-council-architecture` and `empty-chair-protocol` (both stubs), plus `weil-gate.md` (stub)
7. **Agent cluster** — `agents` → `agent-architectures` → `autonomous-agents` → all stubs; low priority

**Wolfram NKS thread now active** (wolfram-nks-causal-networks → computational-irreducibility → emergence):
- `wolfram-nks-causal-networks` links to `wolfram-physics-project` and `causal-networks` (reference)
- `computational-irreducibility` already links to `emergence`, `open-ended-evolution`, `causal-networks`
- `attractor-dynamics` now links to `emergence`, `neural-interpretability`, `computational-irreducibility`

**Creativity thread now active** (creativity → parallel-reasoning → generative-ai → imagination):
- `creativity` links to `parallel-reasoning` (convergent selection), `generative-ai` (output medium), `imagination` (substrate)
- `generative-ai` links to `creativity`, `parallel-reasoning`, `llm-reasoning`, `chain-of-thought`
- `imagination` links to `world-model`, `creativity`, `shorthand-for-thought`

## Open Questions

1. **Dynamical systems**: How do low-dimensional attractor theory results apply to high-dimensional transformer state spaces? Is the "energy landscape" metaphor valid quantitatively or only qualitatively?

2. **AI imagination measurement**: Can we detect imagination-like internal simulation in LLMs via probing studies? What would be the signature?

3. **Mode collapse detection**: Can we detect when a generative model is in mode collapse without exhaustive sampling? Are there structural signatures in activation space?

4. **Agentic planner vs agentic-hierarchy**: Still unresolved from last cycle — these two stubs may be redundant or distinct. Needs clarification.

## Stub Count

- Before: 335 stubs
- After: 330 stubs (net -5 from 5 upgrades this cycle)

## Kanban Status

- No new open items created this cycle
- Discovery report to #research is delivery mechanism per agent sheet
- kanban-morning-review for trailing 10:30 AM aggregator cron handles task surfacing

## Related
- [[index]]
- [[scratchpad/jobs/reports/researcher/discovery-2026-07-03]]

- [[discovery-2026-07-03]]

## Connections Added (18)

- creativity: parallel-reasoning, generative-ai, imagination, in-context-learning, shorthand-for-thought, llm-reasoning, multi-agent-llm-systems, emergence
- attractor-dynamics: emergence, neural-interpretability, hopfield-network, dynamical-systems, computational-irreducibility, shorthand-for-thought
- generative-ai: creativity, parallel-reasoning, generative-ai (self-ref), diffusion-models, in-context-learning, chain-of-thought, llm-reasoning, self-correction
- wolfram-nks-causal-networks: wolfram-physics-project, computational-irreducibility, causal-networks, stephen-wolfram, emergence
- imagination: creativity, world-model, mental-imagery, counterfactual-reasoning, shorthand-for-thought, llm-reasoning