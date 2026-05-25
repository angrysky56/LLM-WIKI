---
created: 2026-06-03
updated: 2026-06-08
type: concept
summary: Internal predictive models used by agents for planning, simulation, and grounding — enabling agents to predict the consequences of actions before executing them; connected to MOP's epistemic energy management and EFHF's world model encoding
tags: [agent-design, planning, prediction, world-model, epistemic-energy, reinforcement-learning]
sources: [[recuriosity-episodic-context-3d-exploration-2026]], [[mop-edm-cognitive-architecture]], [[futuresim-adaptive-agents]]
status: active
confidence: 0.8
---

# World Model

A world model is an internal predictive representation that an agent maintains about its environment — what the environment contains, how it behaves, and what will happen as a result of actions. It enables planning: the agent can simulate outcomes before committing to actions, avoiding failures before they occur.

## Core Concept

A world model captures:
- **State representation**: What's in the environment and how it's organized
- **Transition dynamics**: How actions change the state (the "physics" of the environment)
- **Prediction**: What the sensory input will be given current state and action

This is distinct from a simple mapping from observations to actions (a policy). A world model lets the agent ask "what would happen if I did X?" and reason about counterfactuals.

In the [[mop-edm-cognitive-architecture]], the world model is L2 (hipai-montague) — it encodes hypotheses generated at L1 and is checked by verification at L3.

## Why World Models Matter for Agents

### Planning vs Reactivity

A purely reactive agent maps observations directly to actions — no internal model of consequences. This works for simple environments but fails when:
- Actions have delayed consequences
- The environment has hidden state
- Multiple paths to a goal are available and some are safer
- The agent must coordinate with other agents

World models enable temporal abstraction — reasoning about "what will the state be in 10 steps" rather than just "what action now."

### The Reality Gap Problem

World models inevitably diverge from the real environment. The model is a compression; the environment has details the compression misses. Managing this divergence is central to world model design:

- **Model uncertainty**: When the model is uncertain about its predictions, the agent should act cautiously
- **Model updating**: The model must be updated when observation contradicts prediction
- **Epistemic energy depletion**: As the model diverges from reality, the agent's epistemic energy depletes (the MOP perspective)

### The Amnesiac Agent Problem

Recuriosity (arXiv:2605.22814) identified a critical failure mode in curiosity-driven agents: **amnesiac exploration**. Without a persistent world model, agents:
1. Enter novel areas → forward model makes prediction errors → curiosity reward spikes
2. Leave the area → forward model "forgets" → re-entering produces fresh prediction errors
3. The agent gets trapped in local loops, re-discovering the same areas repeatedly

The solution: a persistent 3D Gaussian Splatting (3DGS) world model that maintains spatial structure across episodes, enabling the agent to recognize "I've been here before" and plan through already-explored areas toward genuinely novel regions.

## World Models in the MOP-EDM Framework

In the [[mop-edm-cognitive-architecture]], world models serve a specific function:

1. **MOP (Layer 0) generates exploration targets** based on path entropy maximization
2. **L1 (Hypothesis) proposes actions** to reach those targets
3. **L2 (World model) encodes the current state** and predicts consequences of proposed actions
4. **L3 (mcp-logic) verifies** that the predicted consequence is coherent (no contradiction, no absorbing state)
5. **EDM (Δ signal)** measures divergence between past vector (what was predicted) and future vector (what actually happens)

The world model at L2 is where the "simulation" happens — the agent predicts what will happen, verifies the prediction is safe, then acts.

## World Model Architectures

### Physical World Models (Robotics)

In robotics and embodied AI, world models are typically:
- **3D reconstructions**: Geometric maps (3DGS, NeRF, occupancy grids)
- **Dynamics models**: Predict how physical state changes with actions (pendulum dynamics, rigid body physics)
- **Sensor models**: Predict what the robot's sensors will observe given an action

Recuriosity's 3DGS model is a physical world model — it predicts RGB observations from arbitrary camera poses.

### Cognitive World Models (LLMs)

For language model agents, the world model is more abstract:
- **State**: Current conversation context, agent's beliefs about the task, known constraints
- **Dynamics**: How the LLM's outputs affect the conversation and external tools
- **Predictions**: What the next tool result will be, what the user will say next, whether a plan will succeed

The [[hipai-montague]] entity is the cognitive world model in the EFHF architecture — it maintains the agent's belief state about the world and encodes hypotheses.

### Predictive Coding Networks

Biological and some AI systems implement hierarchical predictive coding: each layer predicts the input from the layer below, with prediction errors propagated upward. This is a form of world model where the environment model is distributed across layers.

## Connections

- [[mop-edm-cognitive-architecture]] — L2 world model encoding in the MOP-EDM framework
- [[maximum-occupancy-principle]] — MOP generates the exploration targets the world model is tested against
- [[recuriosity-episodic-context-3d-exploration-2026]] — persistent 3D world model for exploration agents
- [[futuresim-adaptive-agents]] — world modeling failure in frontier agents (only 25% accurate on temporal modeling)
- [[hipai-montague]] — the cognitive world model in the EFHF stack
- [[agent-native-design]] — world model as a native architectural component, not a retrofit
- [[epistemic-energy]] — world model divergence depletes epistemic energy; the Δ signal from EDM measures this

## Open Questions

1. ~~Cognitive world models for LLM agents~~ — **answered** → [[cognitive-world-models-for-llm-agents]]

2. **World model uncertainty quantification**: When should the agent trust its world model's predictions vs. treat them as uncertain? Formal methods could verify uncertainty bounds.

3. **World model updating vs. hallucination**: When the world model diverges from reality, how do you distinguish "the model needs updating" from "the agent is hallucinating"? EDM's Δ spike detects divergence but doesn't diagnose the cause.

4. **Composable world models**: Can agents share world models? If two agents have different world models of the same environment, what's the categorical structure for composing their predictions?