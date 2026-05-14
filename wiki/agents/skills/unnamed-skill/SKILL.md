---
name: "unnamed-skill"
description: "No description."
---

---
name: "agentic-tooluse"
description: "Tool use pattern for agents requiring external world interaction. Foundation layer for most real-world agentic tasks. Design principles for effective tool contracts."
---

# Agentic Tool Use Pattern

> [!TIP]
> **TL;DR**: Tool use is the foundation layer for most agentic patterns. If a task requires external data, state, or actions, tools are required. Tool use sits UNDER the reasoning layer, not alongside it.
> **Key Principle**: "A ReAct agent with tools is still ReAct, and a planning agent with tools is still planning."

## Pattern Overview

**Tool use** enables agents to interact with the external world:
- Query databases
- Call APIs
- Retrieve documents
- Execute code
- Modify system state

```