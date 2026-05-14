---
name: "agentic-tooluse"
description: "Tool use pattern for agents requiring external world interaction. Foundation layer with design principles for effective tool contracts."
---

---
name: "agentic-tooluse"
description: "Tool use pattern for agents requiring external world interaction. Foundation layer for most real-world agentic tasks with design principles for effective tool contracts."
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
┌─────────────────────────────────────────┐
│          AGENTIC SYSTEM LAYERS           │
│                                          │
│  ┌─────────────────────────────────────┐│
│  │  REASONING LAYER (ReAct/Planning)    ││
│  │  "What should I do next?"            ││
│  └─────────────────────────────────────┘│
│                    │                     │
│  ┌─────────────────┴──────────────────┐ │
│  │  TOOL LAYER (Foundation)            │ │
│  │  [Database] [API] [Code] [Search]   │ │
│  └─────────────────────────────────────┘│
└─────────────────────────────────────────┘
```

> **Critical insight**: Tools add capability without changing the reasoning pattern. This means:
> - A ReAct agent with tools is still ReAct
> - A planning agent with tools is still planning

## Decision Gate

**When to use**: Apply this pattern when:
- **Question 2b** = YES: Task requires tool access or external information

**The answer is almost always YES.** An agent that can only reason over training data handles a narrow slice of real-world tasks.

## Effective Tool Design

Effective tools have three components:

### 1. Clear Input Specification

| Good Input | Bad Input |
|------------|-----------|
| `user_id: string (required)` | `query: something` |
| `date_range: {start, end}` | `filter: whatever` |
| `limit: integer (default=10, max=100)` | `count: limitish` |

### 2. Predictable Output Format

```json
// Good: Consistent, structured output
{
  "status": "success" | "error",
  "data": [...],
  "meta": { "count": N, "timestamp": "..." }
}

// Always include error handling
// Never return undefined or untyped data
```

### 3. Defined Failure Modes

| Failure Mode | How to Handle |
|--------------|---------------|
| API timeout | Retry with exponential backoff, then fail gracefully |
| Invalid input | Return clear error message, don't crash |
| Rate limit | Implement backoff, notify agent |
| Partial failure | Return what's available + status |

## Tool Categories

### Data Retrieval Tools

| Tool | Purpose | Example |
|------|---------|---------|
| Database query | Structured data access | `query_sql(query)` |
| Vector search | Semantic similarity | `search_similar(text, k)` |
| Document retrieval | Unstructured text | `get_documents(query)` |
| Web search | Real-time information | `web_search(query)` |
| API call | External services | `call_api(endpoint, params)` |

### Action Tools

| Tool | Purpose | Example |
|------|---------|---------|
| Code execution | Run generated code | `execute(code, lang)` |
| File operations | Read/write files | `write_file(path, content)` |
| Message send | External notifications | `send_email(to, body)` |
| System command | OS-level operations | `run_shell(cmd)` |

### Computation Tools

| Tool | Purpose | Example |
|------|---------|---------|
| Calculator | Precise math | `calculate(expr)` |
| Formatter | Data transformation | `format_table(data)` |
| Aggregator | Summary statistics | `summarize(data, metrics)` |

## Tool Contract Template

```markdown
## Tool: [tool_name]

**Purpose**: [One sentence description]
**Input**: 
  - [param1]: [type] (required/optional) - [description]
  - [param2]: [type] (required/optional) - [description]

**Output**:
  - status: "success" | "error"
  - data: [type] (on success)
  - error: { code, message } (on error)

**Failure Modes**:
  1. [Condition] → [Handling]
  2. [Condition] → [Handling]

**Example**:
  Input: { param1: "value", param2: 42 }
  Output: { status: "success", data: [...] }
```

## Tool Use vs. Reasoning Patterns

Tool use is **orthogonal** to reasoning patterns:

| Reasoning Pattern | + Tool Use | = Same Pattern |
|-------------------|------------|----------------|
| ReAct | + Tools | ReAct with tools |
| Planning | + Tools | Planning with tools |
| Reflection | + Tools | Reflection with tools |
| Multi-Agent | + Tools | Multi-Agent with tools |

**Therefore**: When designing, separate:
1. **What tools are available** (tool layer)
2. **How reasoning happens** (reasoning pattern layer)

## Failure Modes

### Excessive Tool Calls

| Signal | Cause | Fix |
|--------|-------|-----|
| Tool calls > 50 in single task | Agent doesn't know when to stop | Add max tool calls limit |
| Same tool called repeatedly | No state tracking | Add output caching |
| Tool calls without progress | Wrong tool for task | Evaluate tool necessity |

### Tool Contract Violations

| Signal | Cause | Fix |
|--------|-------|-----|
| Unexpected output format | Contract not followed | Add validation layer |
| Type errors | Input specification unclear | Tighten specifications |

## AGEM Integration

### Native Tools
- `run_agem_cycle` — Reasoning phase that invokes tools
- `detect_gaps` — Identify missing tools causing failures
- `get_soc_metrics` — Monitor tool efficiency

### Tool Registration

When building an agent with tools:
1. Define tool contracts (input/output/failures)
2. Register tools in agent context
3. Monitor tool call patterns
4. Optimize frequently used tools

### Workflow Template
```
1. REQUIREMENTS:
   a. Identify external data needed
   b. Identify actions to perform
   c. List available tools

2. TOOL DESIGN:
   a. Define contracts for each tool
   b. Implement error handling
   c. Document failure modes

3. INTEGRATION:
   a. Add tools to agent context
   b. Set tool call limits
   c. Add progress tracking

4. MONITORING:
   a. Track tool call efficiency
   b. Identify underused/overused tools
   c. Optimize based on patterns
```

## Quick-Start Template

```markdown
## Tool Use Task Definition

**Task**: [What needs external interaction]
**External Requirements**:
  - Data needed: [databases/APIs/search]
  - Actions needed: [code/file/system]

### Available Tools:
┌────────────────┬──────────────┬────────────────────┐
│ Tool Name      │ Category     │ Purpose            │
├────────────────┼──────────────┼────────────────────┤
│ [tool_1]       │ [retrieval/  │ [description]      │
│                │  action/     │                    │
│                │  compute]    │                    │
└────────────────┴──────────────┴────────────────────┘

### Max Tool Calls: [N per task]

### Failure Handling:
  - API timeout → [retry/backoff/fail]
  - Invalid input → [validate/reject]
  - Rate limit → [backoff/wait]
```

---

## See Also

- [agentic-react](agentic-react) — Most common reasoning pattern using tools
- [agentic-planner](agentic-planner) — Tools for each planned stage
- [agentic-sequential](agentic-sequential) — Deterministic code vs. tools