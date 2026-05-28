---
created: 2026-07-28
updated: 2026-07-28
type: concept
summary: Tool use in LLM agents — how agents invoke external functions, APIs, and capabilities to affect the world
tags: [tool-use, agents, mcp, function-calling, autonomous-agents]
sources: []
status: active
confidence: 0.8
---

# Tool Use

Tool use is the capability of an LLM agent to invoke external functions, APIs, code execution, and other capabilities to perceive and affect the world beyond generating text.

## Definition

Tool use in the LLM agent context refers to the mechanism by which an agent instructs external systems to perform actions and returns the results to the agent's reasoning loop. Common tools include search, file operations, code execution, web requests, and domain-specific APIs.

## Tool Use Architecture

The basic tool-use loop:

```
Agent (LLM)
  ↓ "Call search('arxiv transformer')"
Tool Interface (MCP or similar)
  ↓
External System (search API, filesystem, etc.)
  ↓
Result returned to agent
  ↓
Agent reasons about result, calls next tool
```

## Key Concepts

- **[[mcp]] (Model Context Protocol)**: Standardized interface for tool invocation
- **[[autonomous-agents]]**: The systems that use tool use as part of their operation
- **[[agents/skills/agentic-decision-tree]]**: The skill implementing tool use patterns

## Tool Categories

1. **Information retrieval**: Search, database queries, web fetching
2. **File operations**: Read, write, move files
3. **Code execution**: Run code, evaluate expressions
4. **External APIs**: Call third-party services
5. **Environment interaction**: Control processes, interact with systems

## See Also
- [[concepts/tool-use]]
- [[index]]
- [[log]]
- [[concepts/autonomous-agents]]
- [[tool-use]]

- [[mcp]]: Model Context Protocol for tool standardization
- [[autonomous-agents]]: How tool use fits into autonomous agent architecture
- [[agents/skills/agentic-tooluse]]: The skill implementing tool use