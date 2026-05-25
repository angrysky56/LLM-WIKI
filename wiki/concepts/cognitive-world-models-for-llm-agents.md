---
created: 2026-06-26
updated: 2026-06-26
type: concept
summary: How text-based LLM agents represent "what the world looks like" — the abstraction layers between raw conversation history and a predictive world model; covers belief state, tool-history graphs, conversation structure, and the gap between retrieval and compilation
tags: [agent-design, world-model, cognitive-architecture, representation, EFHF, memory, tool-use]
sources: [[2602.10090]], [[2504.15785]], [[world-model]], [[agent-native-design]], [[hipai-montague]], [[persistent-knowledge-compilation]], [[bounded-rationality]]
status: active
confidence: 0.75
---

# Cognitive World Models for LLM Agents

A cognitive world model is the internal predictive representation a language model agent maintains about its task environment — not a geometric reconstruction of physical space, but an abstract model of what the conversation contains, what the tools have done to external state, and what will happen next. It is the LLM-agent analogue of the 3D Gaussian Splatting world model that Recuriosity uses for physical exploration: a persistent, queryable structure that lets the agent ask "have I seen this before?", "what will this tool call change?", and "where does my plan break down?".

This page answers the question posed in [[world-model]] Open Question #1: *How do you represent "what the world looks like" for a text-based agent?*

## The Core Problem

A physical robot's world model can be a geometric map. A text-based agent's world is the conversation transcript plus everything the conversation references — files, APIs, databases, user goals, previous tool outputs. The agent never sees the "actual state" of anything external; it sees only textual representations of state. This creates a specificational gap:

1. The agent operates in a **text-mediated environment** — everything it knows about the world comes through language
2. The agent's **actual world** is the set of text representations it has accumulated (tool returns, file contents, conversation history)
3. The agent must maintain a **predictive model** of how those representations will change when it acts

The cognitive world model sits between the raw conversation window and a genuine predictive model. It is not the conversation itself — it is the agent's structured interpretation of what the conversation means about the world.

## The Four Layers of a Cognitive World Model

### Layer 1: Conversation State (Episodic Belief)

The conversation transcript is raw episodic memory. The cognitive world model's first layer is a **belief graph** — what the agent believes is true about the task, the user, and the environment, derived from conversation history.

Components:
- **User intent model**: What the user is trying to accomplish (inferred from conversation, not stated explicitly)
- **Task state**: What has been done, what remains, what failed
- **Constraint set**: Explicit and inferred constraints on valid actions
- **Goal decomposition**: How the overall task is broken into sub-tasks

Representation: A structured belief state, not a flat context string. The distinction matters because a flat context string cannot be queried ("what did the user say about constraint X?"), only re-read. A belief graph can be traversed.

The [[hipai-montague]] entity is the cognitive world model component in the EFHF architecture that maintains this belief state.

### Layer 2: Tool History Graph (Environmental State)

Each tool call is a state-modifying operation. A tool history graph records:

- **Tool identity**: What tool was called
- **Input state**: What the environment looked like before the call
- **Parameters**: What arguments were provided
- **Output state**: What the tool returned (the new text representation of the environment)
- **Causality**: Which tool calls causally contributed to which subsequent calls

This is the key innovation of WALL-E 2.0 (arXiv:2504.15785): extracting **symbolic knowledge** — action rules, knowledge graphs, scene graphs — from exploration trajectories and encoding them into executable form. For text agents, the "symbolic knowledge" is the tool-history graph. The agent can ask "what state will result from calling tool X with arguments Y?" by traversing the graph rather than re-executing.

The Agent World Model (arXiv:2602.10090) takes a complementary approach: synthetic code-driven environments where the environment state is explicitly represented in a database, making state transitions deterministic and queryable. For natural text agents, the equivalent is structuring tool outputs as explicit state deltas rather than opaque text blobs.

### Layer 3: World Dynamics Model (Transition Function)

Given the current belief state (Layer 1) and tool history (Layer 2), the agent needs a model of **how actions change state** — the transition dynamics of its environment.

For a file-system tool agent, this might be explicit: `write_file(path, content)` → file at `path` now contains `content`. For more complex agents (code generation, research, multi-step reasoning), the transition dynamics are learned from experience:

- Which tool sequences reliably achieve which outcomes?
- Which plans have succeeded in similar task contexts before?
- When a plan fails, what was the failure mode?

This is where the cognitive world model diverges most from physical world models. Physical dynamics (gravity, rigid body physics) are universal and can be learned once. Task dynamics are task-specific and must be learned or compiled for each new task domain.

[[persistent-knowledge-compilation]] (PKC) is relevant here: if the transition dynamics for a recurring task pattern can be compiled into a rapid-access structure, the agent doesn't need to re-derive them from the tool history graph every time.

### Layer 4: Uncertainty and Divergence Tracking (Epistemic Monitoring)

Following the [[world-model]] reality gap principle: cognitive world models also diverge from actual environment state. For text agents, divergence manifests as:

- **Stale tool beliefs**: Agent believes a file contains X because it saw X in an earlier tool output, but the file was modified externally
- **User intent drift**: Agent's model of user intent diverges from actual user intent as the conversation progresses
- **Plan outcome misprediction**: Agent predicts a tool call will succeed but it fails; the divergence signal should trigger model updating

[[epistemic-energy]] tracks this divergence. As the cognitive world model diverges from actual state, epistemic energy depletes. The agent should become more conservative — gather more explicit confirmations — as energy depletes.

## Architecture: Compilation vs. Retrieval

There are two competing paradigms for maintaining a cognitive world model:

### Retrieval Paradigm (RAG-style)

The world model is the full conversation context. When the agent needs to reason about "what is the current state?", it retrieves from the full context using attention or a retrieval model. Context window size is the hard constraint.

This is the dominant approach in current LLM agents. Its weakness: the retrieval is non-structural. The agent cannot efficiently ask "what were all the tool calls that modified file X?" or "what was my first hypothesis about this problem?" — it must re-read and re-parse the entire context.

### Compilation Paradigm (PKC-style)

The world model is compiled into a structured representation that goes beyond the raw context. Tool calls are parsed into state delta records. Beliefs are extracted into a belief graph. Plans are stored as structured objects.

[[persistent-knowledge-compilation]] predicts which knowledge will be needed and precompiles it. For cognitive world models, this means: when the agent executes a tool, the tool's state delta is immediately compiled into the world model structure, rather than waiting to retrieve it from raw context later.

The synthesis: the raw context remains the source of truth (for faithfulness), but the cognitive world model is a compiled index into it (for efficient query and prediction).

## Relationship to Existing Architecture

The cognitive world model maps onto the MOP-EFHF stack as:

| Layer | Function | Cognitive World Model Equivalent |
|-------|----------|----------------------------------|
| L0 (MOP) | Exploration target generation | Task-space coverage: what parts of the problem space remain unresolved? |
| L1 (Hypothesis) | Generate action candidates | Plan proposals given current belief state |
| L2 (hipai-montague) | World model encoding | The cognitive world model itself — belief state + tool history + dynamics |
| L3 (mcp-logic) | Verification | Consistency check: does the predicted plan outcome contradict known beliefs? |
| L4 (Coherence) | Epistemic energy tracking | World model divergence → energy depletion |
| L5 (Persistence) | Global consistency | Belief graph + tool history must remain consistent with each other |

## Practical Design Questions

**How often should the cognitive world model be updated?**
On every tool call, the tool's output should be parsed into a state delta and merged into the world model. On every user message, the belief state should be updated. Continuous compilation rather than batch reconstruction.

**How do you handle contradictory beliefs?**
The belief graph should support belief revision with provenance — when the agent detects that a new observation contradicts a stored belief, the old belief should be marked superseded (not deleted) with a reference to the contradicting observation. This enables the agent to reason about how its beliefs evolved.

**What is the "absorbing state" for a text agent?**
In physical agents, death is terminal. In text agents, the absorbing state is **irrecoverable belief divergence** — the agent's world model is so far from actual state that no coherent continuation is possible. This is distinct from a simple contradiction; it means the cumulative divergence makes reliable planning impossible. Detecting this requires monitoring the rate of belief revision, not just individual contradictions.

**How does the cognitive world model relate to multi-agent shared state?**
In [[multi-agent-llm-systems]], each agent has a private cognitive world model. Shared state (via blackboard or message passing) must be translated into each agent's belief representation. Two agents with different world models of the same environment is the multi-agent analogue of the composable world models question in [[world-model]].

## Connections

- [[world-model]] — parent concept; this page answers Open Question #1
- [[agent-native-design]] — cognitive world model as a native architectural component
- [[hipai-montague]] — EFHF entity that maintains the belief state
- [[persistent-knowledge-compilation]] — compilation paradigm for world model maintenance
- [[epistemic-energy]] — world model divergence depletes energy; the Δ signal from EDM
- [[bounded-rationality]] — cognitive world model is the structural bound on what the agent can reason about
- [[multi-agent-llm-systems]] — shared cognitive world models across agents
- [[futuresim-adaptive-agents]] — empirical evidence that frontier agents have severe world modeling gaps (25% accuracy on temporal event forecasting)
- [[agent-architectures]] — broader context for agent system design

## Open Questions

1. **Structured belief representation vs. implicit LLM belief**: Is an explicit belief graph necessary, or does a sufficiently powerful LLM maintain an implicit world model in its activations? The practical difference: an explicit graph can be queried, inspected, and corrected; an implicit model cannot.

2. **World model persistence across sessions**: For long-running agents, should the cognitive world model persist beyond the current conversation? What is the equivalent of Recuriosity's episodic context — a compressed representation of previous task episodes that informs the current one?

3. **Tool-call semantics as state deltas**: Can tool interfaces be designed so that every tool call is inherently a state delta with explicit pre-state and post-state representations? This would make Layer 2 (tool history graph) automatic rather than inferred.

4. **World model uncertainty quantification**: When should the agent trust its cognitive world model's predictions? For physical world models, this is active research (model uncertainty). For cognitive world models, the uncertainty is about belief correctness — a different problem.
