---
created: 2026-06-03
updated: 2026-06-25
type: concept
summary: System architecture patterns for LLM-based autonomous agents — runtime composition, failure modes, and the LLM/software boundary as first-class design concern
tags: [llm-agents, agent-architecture, production-systems, runtime-patterns, tool-use, verification]
sources: [https://arxiv.org/abs/2605.20173]
status: active
confidence: 0.8
---

# LLM Agent Architecture

LLM agent architecture refers to the structural patterns that govern how an LLM-based autonomous agent is composed: how it receives inputs, generates outputs, uses tools, maintains state, and coordinates with other agents or systems. Unlike a standalone language model, an LLM agent is an integrated system where the model is one component in a larger runtime architecture.

The key architectural insight (from production-llm-agent-runtime-architecture-patterns): **production agent failures — hallucinations, tool misuse, state corruption, non-termination — are disproportionately caused by runtime architecture deficiencies, not model capability gaps**. The boundary between the LLM and the deterministic software around it requires its own design methodology.

## Core Architectural Components

### 1. The LLM/Software Boundary

Every LLM agent operates at the interface between stochastic model outputs and deterministic software systems. This boundary requires specific architectural treatment:

- **Guardrail layers**: Validate model outputs before they trigger actions
- **Confirmation gates**: Require explicit validation for high-stakes operations
- **State machines**: Define legitimate state transitions and prevent invalid states
- **Replay buffers**: Enable recovery and retry from recoverable failures

### 2. Runtime Architecture Patterns

The production-llm-agent-runtime-architecture-patterns paper identifies recurring runtime patterns:

| Pattern | Purpose | Failure Mode Addressed |
|---------|---------|------------------------|
| Guardrail layer | Enforce output constraints | Hallucinated tool calls |
| Confirmation gate | Human-in-the-loop for risky actions | Irreversible operations |
| State machine | Define valid state transitions | State corruption |
| Replay buffer | Recover from failures | Non-termination loops |
| Tool registry | Structured tool access | Tool misuse |

### 3. Tool Use Architecture

LLM agents interact with the world primarily through tool use. The architecture determines:

- **Tool definition**: How tools are represented and made accessible to the model
- **Tool selection**: How the model chooses which tool to call
- **Output processing**: How tool results are interpreted and fed back
- **Error handling**: How tool failures are detected and recovered from

The [[code-as-agent-harness]] survey frames code as the universal tool interface — agents write tools as code rather than calling fixed APIs. This shifts the architecture from API-based tool calling to executable, stateful interfaces.

### 4. State Management

Agents must maintain state across multiple reasoning steps:

- **Context window management**: Keeping relevant context while avoiding overflow
- **Working memory**: Short-term state for current task
- **Persistent memory**: Long-term knowledge and experience
- **World model state**: Internal model of the environment

The [[hermes-agent]] framework provides a delegate_task pattern for spawning sub-agents, tool registry for file system/shell/git operations, state management for iteration loops, and safety constraints via soul configuration.

## Failure Modes at the Boundary

Production agents fail in characteristic ways that are architectural, not model-based:

1. **Hallucinated tool calls**: Model generates a valid-looking tool name that doesn't exist or has wrong arguments → addressed by guardrail validation
2. **State corruption**: Model drives system into invalid state → addressed by state machine enforcement
3. **Non-termination**: Model enters infinite reasoning loop → addressed by replay buffer and timeout constraints
4. **Tool misuse**: Model calls right tool for wrong reason → addressed by confirmation gates

## Relationship to Agent Native Design

[[agent-native-design]] describes the architectural ideal: the LLM itself should be architected for agency. LLM agent architecture is the current practice — engineering around the reactive transformer to approximate agency. The gap between the two defines the design space:

- **Current practice**: Retrofit reactivity with RLHF + constitutional constraints + CoT prompting
- **Agent native design**: Replace reactive generation with proactive path-entropy maximization (MOP Layer 0)

The production-llm-agent-runtime-architecture-patterns paper confirms this gap empirically: boundary failures dominate model failures.

## Connections
- [[concepts/maximum-occupancy-principle]]
- [[log]]
- [[concepts/load-bearing-reasoning]]
- [[concepts/code-agent]]
- [[concepts/llm-agent-architecture]]
- [[concepts/world-model]]
- [[concepts/agent-native-design]]
- [[concepts/agentic-hierarchy]]
- [[sources/papers/production-llm-agent-runtime-architecture-patterns]]
- [[concepts/code-generation]]
- [[wiki/index]]
- [[llm-agent-architecture]]

- [[agent-native-design]] — architectural ideal that LLM agent architecture approximates
- [[maximum-occupancy-principle]] — path entropy maximization as intrinsic motivation
- [[production-stage-architecture]] — self-direction and the production boundary
- [[agentic-hierarchy]] — hierarchical agent organization
- [[code-agent]] — software engineering specialization
- [[world-model]] — internal predictive model for planning
- [[code-as-agent-harness]] — code as universal tool interface
- [[load-bearing-reasoning]] — boundary reasoning as load-bearing
- Concept: [[code-generation]]


## Open Questions

1. **Tool registry design**: What is the optimal granularity and abstraction for tool definitions? Too fine-grained and the model can't navigate; too coarse and capability is limited.
2. **State machine completeness**: How do you ensure the state machine covers all legitimate transitions without being over-constrained?
3. **Guardrail performance**: Guardrails can block legitimate outputs — how do you balance safety vs. capability?
4. **Multi-agent state consistency**: When multiple agents share state, how do you prevent race conditions and stale reads? (code-as-agent-harness identifies this as open challenge #4)