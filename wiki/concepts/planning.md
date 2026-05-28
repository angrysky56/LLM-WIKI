---
summary: Planning — generation of action sequences toward goals, classical vs LLM planning, failure modes, and architecture patterns
tags: [planning, agents, reasoning, bounded-rationality, goal-management, llm]
updated: 2026-05-28T18:32:10Z
---

---
created: 2026-08-23
updated: 2026-08-23
type: concept
summary: Planning — the generation of action sequences toward goals, with emphasis on LLM-based planning and its failure modes
tags: [planning, agents, reasoning, bounded-rationality, goal-management, llm]
sources: []
status: active
confidence: 0.72
---

# Planning

Planning is the reasoning process of generating a sequence of actions to achieve a desired goal state. In AI systems, it involves representing the world, projecting how actions change state, and searching for action sequences that lead from the current state to the goal.

## Classical vs. LLM Planning

Classical planning (STRIPS, PDDL, HTN) uses explicit symbolic representations:
- **World state** as a set of predicates
- **Actions** as preconditions + effects
- **Search** over the state space

LLM-based planning replaces symbolic search with language-model inference. The LLM:
- Represents the world in natural language (implicitly in weights)
- Projects consequences of actions via next-token prediction
- Searches via beam search, chain-of-thought, or tree-of-thought rather than explicit state enumeration

This shift trades **guaranteed correctness** for **generalization**. Classical planners are sound and complete for their formal domain; LLMs can plan in novel situations without explicit encoding but with no guarantees.

## LLM Planning Failure Modes

LLM planning suffers from well-documented failure modes:

### 1. Goal Drift
The agent's interpretation of the goal shifts during multi-step planning. Early steps are aimed at the true goal; later steps address a subtly different objective that emerged from the LLM's interpretation of intermediate results. Related to [[self-correction]] failures.

### 2. Subgoal Conflict
Subsidiary goals created during planning conflict with each other or with the parent goal. A plan that optimally achieves subgoal A makes subgoal B impossible. This is a hallmark of [[bounded-rationality]] — the agent cannot fully enumerate all subgoal interactions.

### 3. Hallucinated Prerequisites
The LLM assumes capabilities or environmental conditions that don't exist. The plan calls for a tool the system doesn't have, or assumes facts not in the knowledge base.

### 4. Credit Assignment Failure
When a plan fails, the LLM misattributes cause — blaming the wrong step and retrying with a fix that doesn't address the actual problem.

### 5. Plan Space Explosion
The branching factor of valid action sequences exceeds what the LLM can explore effectively. Without explicit search pruning, the model generates increasingly divergent plans.

## Planning Architectures

### Chain-of-Thought (CoT)
Linear step-by-step reasoning. The simplest planning pattern — the model generates a sequence of reasoning steps, each projecting toward the goal. Vulnerable to goal drift and subgoal conflicts because it maintains no explicit world model.

### Tree-of-Thought (ToT)
Explore multiple action branches simultaneously, evaluate each branch's projected outcome, and select the best. Enables backtracking. More compute-intensive than CoT.

### ReAct (Reason + Act)
Interleave reasoning with tool use — reason about the current state, take an action, observe the result, repeat. Native pattern for tool-using agents.

### Reflexion
Planning with self-reflection — after executing a plan, the agent critiques the plan's execution and revises. Addresses some credit assignment failures but not goal drift.

## Connection to [[Goal Management]]

Planning generates the content; [[goal-management]] tracks the state. A plan is created in service of a goal — but the goal persists across sessions, while individual plan executions are stateless. The interplay:

- Planning operates within the context of an active goal (from goal management)
- Goal management decides which goal to plan for, based on priority
- Plan failure triggers goal state transitions in goal management (BLOCKED → ABANDONED or back to PLANNING)

## Connections to Other Concepts

- [[bounded-rationality]] — the structural constraints that make perfect planning impossible
- [[goal-management]] — the persistence layer for goals that planning serves
- [[self-correction]] — the revision mechanism when plans fail
- [[agentic-design-picker]] — architectural choices about how planning is structured
- [[cognitive-world-models-for-llm-agents]] — the world model that planning operates on
- [[deliberative-agents]] — agents that make planning explicit
- [[epistemic-energy]] — energy depletion limits planning depth

## Open Questions

- Can LLMs learn to do explicit planning search (beamwidth, pruning) the way they do implicit reasoning — or does "planning" in LLMs remain fundamentally different from classical planning?
- How does context length affect planning quality — does longer context enable better planning or just more convincing-sounding plans?
- Can reflexion-style self-critique be made stable enough to handle long-horizon plans, or does error compound?
