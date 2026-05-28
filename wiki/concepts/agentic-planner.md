---
created: 2026-06-16
updated: 2026-05-26
type: concept
summary: Agentic planning systems — hierarchical task decomposition, plan execution, and the relationship between planning and planning-while-executing
tags: [agentic-planner, planning, agent-design, hierarchical-task-decomposition, react]
sources: []
status: active
confidence: 0.75
---

# Agentic Planner

## Definition

An agentic planner is a component or capability that enables an AI agent to decompose high-level goals into executable sub-tasks, sequence those sub-tasks, monitor execution, and replan when circumstances change. Planning is the cognitive function that bridges "what do I want to achieve" (intention) and "what do I do next" (action).

The key property of agentic planning systems is that they maintain an **explicit representation of the goal structure** — a task hierarchy, a plan graph, or a state trace — that can be inspected, revised, and shared with other agents.

## Agentic Planner vs Agentic Hierarchy

These two concepts are related but distinct:

- **[[agentic-hierarchy]]** = how multiple agents are organized structurally (supervisor-worker, manager-specialist, etc.)
- **Agentic planner** = the planning capability *within* an agent that decomposes tasks

Agentic hierarchy provides the organizational structure; agentic planner provides the cognitive function. An agentic hierarchy uses planning (as one of its functions), but hierarchical organization and task planning are not the same thing.

A single agent can have planning capability without being in a hierarchy. Conversely, a hierarchy can exist without explicit task planning (e.g., simple dispatcher that routes tasks to workers without decomposing them).

## Planning as Cognitive Process

### Hierarchical Task Decomposition

The planner takes a high-level goal and recursively decomposes it:
```
Goal: Organize a conference
  └─ Subgoal: Define theme and scope
       └─ Task: Research comparable events
       └─ Task: Survey potential attendees
  └─ Subgoal: Secure venue
       └─ Task: Identify venues
       └─ Task: Negotiate contracts
  └─ ...
```

The depth of decomposition depends on task complexity and the planner's horizon. Simple tasks may need only one level; complex tasks may need many.

### Replanning and Loop Detection

Plans rarely survive contact with reality. An agentic planner handles deviation from expected states by:
- Detecting plan failures (action didn't produce expected state)
- Replanning around obstacles (finding alternative paths to the goal)
- Escalating unresolvable obstacles (triggering human review or abort)

When a plan repeatedly fails, the planner may detect a loop and escalate rather than continue cycling.

### Relationship to ReAct

The `agentic-react` skill implements a reactive planning loop: observe → think → act → reflect. The planning layer in ReAct operates at the action level — deciding which tool to call next. An agentic planner operates at a higher level of abstraction — deciding which sub-goals to pursue and in what sequence.

## Architectural Integration

### Planning as a Layer

In the MOP (Maximum Occupancy Principle) framework, planning corresponds to **Layer 1 (Goal Inference and Intent Alignment)**:
- The agent holds an internal representation of the intended outcome
- Planning decomposes the intent into sequenced actions
- Execution monitoring checks whether actions are achieving the intended state

### Planning and World-Model

A world-model underlies planning — the planner simulates action outcomes using the world-model before executing. Without a world-model, the planner cannot anticipate consequences and must rely on trial-and-error. With a world-model, the planner can reason counterfactually: "If I do X, then Y will happen, so I should do X rather than Z."

This connects agentic planning to [[world-model]] and [[imagination]] (latent space simulation of action outcomes).

## Connections

- [[agentic-hierarchy]]: organizational structure for multi-agent planning
- [[world-model]]: simulation substrate for planning
- [[agentic-react]]: reactive planning loop implementation
- [[multi-agent-llm-systems]]: distributed planning across agents
- [[imagination]]: internal simulation for plan outcome prediction
- [[autonomous-agents]]: agentic planning is the core cognitive function that enables autonomous agents to decompose goals and execute multi-step plans
- [[agent-architectures]]
- [[hybrid-agents]]
- [[agentic-design-picker]]
- [[aseke-framework]]
- [[autonomous-ai-agents]]
- [[deliberative-agents]]
- [[counterfactual]]
## Open Questions

1. **Planning depth vs reliability**: How does planning depth (number of decomposition levels) affect plan reliability? Is there a sweet spot where deep decomposition produces more reliable execution without excessive planning overhead?

2. **Planning vs reactivity**: When is explicit planning better than reactive response? Is there a clear threshold (task complexity, time budget, stakes) that determines which approach wins?

3. **Planning failure signatures**: Can we detect planning failures before they cascade? Are there early warning signals (repeated replanning, growing plan uncertainty) that predict plan failure?
- [[agents]]