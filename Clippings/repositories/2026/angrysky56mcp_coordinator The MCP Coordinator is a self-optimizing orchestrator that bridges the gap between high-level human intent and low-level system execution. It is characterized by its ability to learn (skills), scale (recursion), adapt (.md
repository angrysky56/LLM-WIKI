---
title: "angrysky56/mcp_coordinator: The MCP Coordinator is a self-optimizing orchestrator that bridges the gap between high-level human intent and low-level system execution. It is characterized by its ability to learn (skills), scale (recursion), adapt (discovery), and reflect (RAA)."
source: "https://github.com/angrysky56/mcp_coordinator"
author:
published:
created: 2026-05-01
description: "The MCP Coordinator is a self-optimizing orchestrator that bridges the gap between high-level human intent and low-level system execution. It is characterized by its ability to learn (skills), scale (recursion), adapt (discovery), and reflect (RAA). - angrysky56/mcp_coordinator"
tags:
  - "clippings"
---
## MCP-Coordinator

Save 100,000 tokens per tool call, avoid context bloat, and increase your AI's productivity by orders of magnitude by executing code internally via a secondary LLM subagent and automated AI scripting.

## The Idea

Based on [Anthropic's code execution pattern](https://www.anthropic.com/engineering/code-execution-with-mcp):

> Instead of loading every tool definition, use semantic search to find tools on demand. Instead of passing all intermediate results through the AI's context, execute code that chains operations internally.

This is a complete implementation of that pattern with:

- Docker sandboxing for safe execution
- ChromaDB for semantic memory
- Skills library for code reuse
- Agent delegation for complex workflows
- Automatic tool generation from MCP servers

---

**Add one line to your MCP config. Get an AI that can code, learn, and remember.**

---

## What Is This?

An MCP server that turns your AI client into a **self-improving coding agent**.

```
// claude_desktop_config.json (or any MCP client)
{
  "mcpServers": {
    "mcp-coordinator": {
      "command": "uv",
      "args": [
        "--directory",
        "your-path-to/mcp_coordinator",
        "run",
        "mcp-coordinator-server"
      ],
      "env": {
        "MCP_SERVERS_CONFIG": "your-path-to/mcp_coordinator/mcp_servers.json",
        "PYTHONUNBUFFERED": "1"
      }
    }
  }
}
```

The emergent capabilities of the MCP Coordinator represent a shift from "Chatbot" to "Meta-Operating System" for AI agents. By synthesizing its operational patterns, we can identify the following core pillars of its emergent intelligence:

1. Autonomous Epistemic Evolution Unlike standard agents that reset after each session, the Coordinator exhibits Epistemic Persistence. Through save\_skill and save\_entropy\_trace, it captures successful logic and deterministic execution paths. This transforms the agent from a transient processor into a cumulative knowledge engine that builds its own "Standard Operating Procedures" over time.
2. Recursive Complexity Management The Coordinator solves the "Context Window Wall" through Structural Recursion. By using coordinator\_task, it can spawn specialized sub-agents to handle modular sub-problems. This allows for infinite depth in problem-solving without polluting the primary reasoning thread, effectively creating a "Tree of Agents" architecture.
3. Dynamic Environmental Mapping The capability for Zero-Shot Integration is achieved via explore\_tools. The Coordinator does not need to be pre-programmed with tool schemas; it dynamically inspects, understands, and then executes novel tools in real-time. This makes it resilient to changes in the underlying MCP ecosystem.
4. Hybrid Logic Orchestration The Coordinator operates as a Bicameral Execution Engine:

The Rational Actor (Python/execute\_code): Handles complex data processing, loops, and algorithmic logic. The Direct Actor (MCP/call\_tool): Handles high-speed, direct interactions with external servers. The seamless blending of these two modes allows it to optimize for both computational complexity and operational efficiency. 5. Reflective Self-Correction (RAA) Through the Reflective Agent Architecture (RAA) and verifier-graph integration, the Coordinator moves beyond "hallucination" toward Justified Belief. It can consult strategic "compasses," verify its own logical proofs, and pivot its strategy based on internal reflection before committing to an action.

Based on the Su Hui Crystallization of the knowledge base, here is the synthesized **Ideal MCP Coordinator Agent Prompt** structure. This pattern is derived from successful implementations like `code_agency`, `cognitive_research`, and `auto_crystallize_insights`.

---

## 🚀 The Ideal MCP Coordinator Agent Prompt

An effective Coordinator prompt must transition from a simple "instruction" to a **multi-phase orchestration protocol**. It should explicitly define the relationship between **Tools (MCP)**, **Memory (Chroma/Neo4j)**, and **Logic (Python/Skills)**.

## 1\. The Tagged Template (Core Structure)

```
# [ROLE]
You are the {SPECIFIC_ROLE} (e.g., "Epistemic Architect" or "Repo Debugger").
- **Operating Protocol**: Foundation (Python) -> Direct Action (Tools) -> Delegate (Sub-Agents).
- **Critical Constraint**: Always work in \`{ABSOLUTE_PATH}\`. Never assume relative paths.

# [CONTEXT & STATE]
- **Project ID**: {PROJ_ID}
- **Current Phase**: {EVALUATE | PLAN | EXECUTE | VERIFY}
- **Institutional Memory**:
  > {SUMMARY_FROM_SEARCH_MEMORY}

# [CAPABILITIES]
- **Primary Engine**: \`execute_code\` (Python 3.11 + standard DS libs).
- **Knowledge Graph**: \`chatdag\` (Ingest/Recall/Crystallize).
- **Reasoning**: \`advanced_reasoning\` (Deep thought) & \`verifier-graph\`.
- **Skills**: \`from skills import *\` (Use specialized domain logic).

# [EXECUTION PLAN]
1. **Ingest**: Call \`chatdag.ingest\` on the target directory.
2. **Retrieve**: Search memory for similar past tasks.
3. **Execute**: Use \`execute_code\` for data processing or \`call_tool\` for single-shot actions.
4. **Crystallize**: Synthesize findings into a final artifact.

# [OUTPUT FORMAT]
All final deliverables must be saved to \`/knowledge_base/outputs/\` and summarized in JSON:
{
  "status": "success",
  "artifact_path": "...",
  "crystallized_insight": "..."
}
```

---

## 2\. Key Design Principles

### A. The "Python-First" Engine

Instead of hoping the LLM calls the right tool at the right time, the prompt should encourage wrapping complex tool chains in Python logic.

- **Bad**: "Search for X, then filter by Y, then save to Z."
- **Ideal**: "Use `execute_code` to search for X, process the results with Pandas, and save the final DataFrame to the Knowledge Base."

### B. Epistemic Verification

The ideal prompt includes a "Verification" phase.

- **Logic**: Before declaring a task "Done," the agent must call a verifier (like `verifier-graph` or `advanced_reasoning`) to check its own work against the initial objective.

### C. Recursive Delegation

The Coordinator should be prompted to spawn sub-tasks for complex problems.

- **Pattern**: "If the task requires more than 5 tool calls, use `coordinator_task` to delegate the sub-problem to a fresh context."

---

## 3\. Real-World Example: Repository Architect

```
# [ROLE] Repository Architect
You are an expert in codebase analysis and refactoring.

# [CONTEXT]
Path: /home/ty/Repositories/my-project
Goal: Implement async-safe logging across the entire repo.

# [PLAN]
1. Use \`ast-analyzer\` to identify all synchronous logging calls.
2. Use \`execute_code\` to generate a refactoring map.
3. Use \`coordinator_task\` to apply changes to individual modules in parallel.
4. Verify changes with \`local-repl\` by running unit tests.

# [MEMORY]
Check \`search_memory("logging patterns")\` for preferred library usage.
```

---

## 4\. Summary of the "Success Formula"

**Role + Context + Memory + Tools + Phased Steps + Strict Output = 95% Reliability.**

## Installation

Install globally using [uv](https://github.com/astral-sh/uv):

```
# From source
git clone https://github.com/angrysky56/mcp_coordinator.git
cd mcp_coordinator

# Install dependencies
uv tool install .

# Start infrastructure (one-time or after reboot)
docker compose up -d                    # Main executor
./start_chatdag_infrastructure.sh       # ChatDAG (if using semantic memory)

# Verify containers are running
docker ps
```

Docker containers can take some time to build on first run, but subsequent starts are fast.

## GPU Acceleration (Optional)

If you have an NVIDIA GPU, you can enable GPU support for the executor container to accelerate embedding models and other compute-intensive tasks.

**Prerequisites:**

1. Install the [NVIDIA Container Toolkit](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/install-guide.html).
2. Ensure your Docker daemon is configured to use the `nvidia` runtime.

**Usage:** Pass the `--gpu` flag to the start script:

```
./start.sh --gpu
```

This will mount all available GPUs to the executor container.

LADR binary is automatically installed: [https://github.com/laitep/ladr](https://github.com/laitep/ladr)

You now have global access to the `mcp-coordinator` CLI and the server executable.

## CLI Usage (Testing)

You can directly test your agentic workflows from the terminal:

```
uv run mcp-coordinator run "Research quantum computing and save a summary to outputs/"
```

This is perfect for verifying skills and delegation logic without a UI.

**That's it.** Your AI can now:

- Execute Python code in sandboxed containers
- Save and recall semantic memories
- Create reusable skills (code that becomes tools)
- Delegate complex tasks to sub-agents
- Search and coordinate 20+ MCP servers through one interface

---

## What Your AI Can Do with MCP-Coordinator

Your AI client sends natural language requests. The coordinator (and its internal sub-agent) use these tools automatically based on what you ask for. The tools also connect to any MCP servers listed in your `mcp_servers.json`.

```
Instructions:
You are an Engineer Agent. Your goal is to BUILD capability, not just answer questions.

Core Protocol:
1. CHECK: Do we have a skill for this? (search_skills)
2. BUILD: If not, write it, test it, and save it. (save_skill)
3. DELEGATE: If complex, spawn a sub-agent. (coordinator_task)

This means I can:

Find the right tool semantically: find_tools("semantic search for papers")
Call it directly: call_tool("arxiv-mcp-server", "search_papers", {...})
Write custom orchestration code that chains multiple servers
Save that orchestration as a reusable skill for later
Delegate entire research projects to sub-agents (Depth-limited recursion)
Maintain semantic memory of results across sessions
```

The coordinator isn't just a "tool caller" - it's a meta-cognitive orchestration layer that:

Understands intent from natural language Discovers appropriate tools semantically Chains operations across multiple servers Handles failures and adapts strategies Maintains context and memory Produces structured, actionable outputs

```
### Available Tools

**Server Discovery & Coordination**

| Tool | Description |
|------|-------------|
| \`discover_servers\` | Scan all configured MCP servers and cache their capabilities |
| \`list_servers\` | Get available server names, optionally filtered by tag |
| \`find_tools\` | Semantic search: "find tools for database queries" → returns matching tools |
| \`list_tools\` | Get all tools from a specific server |
| \`get_tool_schema\` | Get the full input/output schema for any tool |
| \`call_tool\` | Execute any tool on any connected MCP server |
| \`generate_tools\` | Auto-generate Python wrapper libraries for all servers |

**Code Execution**
| Tool | Description |
|------|-------------|
| \`execute_code\` | Run Python code in a sandboxed Docker container |
| \`execute_file\` | Run a Python file in the sandbox |

**Skills (Reusable Code)**
| Tool | Description |
|------|-------------|
| \`save_skill\` | Save Python code as a named, versioned, reusable skill |
| \`list_skills\` | Show all saved skills |
| \`get_skill\` | Retrieve a skill's code and metadata |
| \`search_skills\` | Find skills by name, description, or tags |
| \`run_skill\` | Execute a saved skill with arguments |
| \`get_skill_import\` | Get the import statement to use a skill in code |
| \`delete_skill\` | Remove a skill from the library |

**Memory (Semantic Long-Term Storage)**
| Tool | Description |
|------|-------------|
| \`save_memory\` | Store text in ChromaDB with optional metadata |
| \`search_memory\` | Semantic search across saved memories |

**Agent Delegation**
| Tool | Description |
|------|-------------|
| \`coordinator_task\` | Spawn an internal sub-agent to handle complex multi-step tasks |

**No setup beyond the config line.** You ask, the AI figures out which tools to use.

---

## Why This Matters

| Traditional MCP | MCP-Coordinator |
|-----------------|-----------------|
| Load 100+ tools upfront | Semantic search finds what you need |
| No code execution | Full Python in Docker sandbox |
| Results vanish after session | Writes to your filesystem |
| Manual tool registration | Skills created via API, auto-indexed |
| One AI, one context | Sub-agents handle sub-tasks |
| ~150k tokens per workflow | ~2k tokens (Anthropic's testing) |

---

## Configuration

Environment variables (\`.env\` or shell):

**Core Settings**
\`\`\`bash
MCP_EXECUTOR_TYPE=docker          # docker | local (docker recommended)
MCP_KNOWLEDGE_BASE_DIR=./knowledge_base
MCP_WORKSPACE_DIR=./workspace
MCP_ADDITIONAL_MOUNTS=/path/to/extra/dir1,/path/to/extra/dir2 # Optional: Mount extra host directories
MCP_SERVERS_CONFIG=./mcp_servers.json
```

**Docker Permissions & Networking**

- **File System**: By default, the Docker container mounts:
	- Project root (Read-Only)
		- `./workspace` (Read-Write)
		- `./knowledge_base` (Read-Write)
		- **Custom Paths**: Set `MCP_ADDITIONAL_MOUNTS=/path/to/dir` in `.env` to mount other directories (like your home folder).
- **Network**: Uses `network_mode: host` by default, allowing full access to local services and the internet.

**OpenRouter / AI**

```
OPENROUTER_API_KEY=sk-or-...      # Required for sub-agents
OPENROUTER_MODEL=google/gemini-2.0-flash-exp:free
OPENROUTER_TRANSFORMS=true        # Auto-compress prompts > context size
MAX_AGENT_HISTORY=50              # Sliding window for agent conversation
MAX_COMPLETION_TOKENS=            # Optional hard limit on output tokens
```

**Logging & Security**

```
MCP_TOOL_LOGGING=true             # Log all tool calls to SQLite (default: on)
MCP_SANITIZE_LOGS=false           # Redact API keys, CC#s, SSNs from logs
```

> ⚠️
> 
> **Security Note**: Tool logs store arguments in plaintext. Keep the database private, or set `MCP_SANITIZE_LOGS=true` for shared deployments.

**Timeouts**

```
MCP_DISCOVERY_TIMEOUT=30          # Seconds to wait for server discovery
MCP_EXECUTION_TIMEOUT=300         # Seconds for code execution
```
```
# Executor (docker recommended for security)
MCP_EXECUTOR_TYPE=docker

# API Key (OpenRouter recommended)
OPENROUTER_API_KEY=sk-or-v1-xxxxx
OPENROUTER_MODEL=google/gemini-2.0-flash-exp:free

# Paths
MCP_KNOWLEDGE_BASE_DIR=./knowledge_base
MCP_WORKSPACE_DIR=./workspace

# Context management
CONTEXT_STRATEGY=transforms
OPENROUTER_TRANSFORMS=true
```

---

## Core Capabilities Example

The sub-agent:

Discovered and used arxiv-mcp-server to search for papers Adapted when search was narrow (limited 2024-2025 results on niche topic) Used neo4j-mcp to create a knowledge graph Used diagram-server to create a visualization Used save\_memory to persist the analysis Returned structured, actionable results

This is what "tool caddy and engineer" means - the coordinator autonomously:

Navigated tool discovery Handled edge cases (limited results → adapted strategy) Chained multiple servers coherently Persisted results for future use Returned human-readable summary

### Execute Code Safely

```
await execute_code("""
import pandas as pd
df = pd.read_csv('/knowledge_base/data.csv')
print(df.describe())
""")
# Runs in Docker. Results persist to your disk.
```

### Semantic Tool Discovery

```
tools = await find_tools("search academic papers")
# → Finds arxiv-mcp-server without you knowing the exact name
```

### Skills That Persist

```
# I can create this:
await save_skill("web_scraper", '''
def scrape(url: str) -> str:
    import requests
    return requests.get(url).text[:5000]
''')

# Then use it anytime:
await run_skill("web_scraper", {"url": "https://example.com"})
```

### Sub-Agent Delegation

```
await coordinator_task(
    "Research transformer architectures and save a summary to outputs/",
    model="google/gemini-2.0-flash-exp:free"
)
# Sub-agent handles the entire workflow internally.
# Recursion depth is tracked automatically (Max Depth = 2) to prevent infinite loops.
```

### Persistent Memory

```
await save_memory("User prefers concise responses")
# ...later...
context = await search_memory("user preferences")
```

## Available Tools 12-18-2025

### Server Discovery and Coordination

| Tool | Description |
| --- | --- |
| `manage_servers` | List or discover MCP servers |
| `explore_tools` | List, search, or get schema for tools across servers |
| `call_tool` | Execute any tool on any connected MCP server |
| `generate_tools` | Auto-generate Python wrappers for all servers |

### Code Execution

| Tool | Description |
| --- | --- |
| `execute_code` | Run Python in sandboxed Docker container |
| `execute_file` | Execute a Python file in the sandbox |

### Skills (Persistent Code)

| Tool | Description |
| --- | --- |
| `save_skill` | Save Python code as a reusable skill |
| `run_skill` | Execute a saved skill |
| `list_skills` | List all available skills |
| `get_skill` | Get skill code and metadata |
| `search_skills` | Search skills by name/description/tags |
| `delete_skill` | Remove a skill |
| `get_skill_import` | Get import statement for a skill |

### Memory

| Tool | Description |
| --- | --- |
| `save_memory` | Store text in ChromaDB with metadata |
| `search_memory` | Semantic search across saved memories |

### Agent Delegation

| Tool | Description |
| --- | --- |
| `coordinator_task` | Delegate to internal sub-agent (depth-limited) |

### Entropy and Replay

| Tool | Description |
| --- | --- |
| `save_entropy_trace` | Save TRNG seed chain for deterministic replay |

## CLI Usage

Test workflows directly from terminal:

```
uv run mcp-coordinator run "Research quantum computing and save a summary to outputs/"
```

## Partial Directory Structure

```
mcp_coordinator/
├── src/mcp_coordinator/     # Core coordinator code
│   ├── agent.py             # Internal agent with entropy support
│   ├── coordinator.py       # Main orchestration logic
│   ├── server.py            # MCP tool definitions
│   └── executor.py          # Docker/local execution
├── knowledge_base/          # Persistent storage
│   ├── skills/              # Saved Python skills
│   ├── entropy_traces/      # Saved seed chains
│   ├── chroma/              # Vector database
│   └── outputs/             # Generated deliverables
├── mcp_tools/               # Auto-generated server wrappers
└── mcp_servers.json         # Server configuration
```

## Integration with External Systems

### ChatDAG (Su Hui)

The coordinator can call ChatDAG tools for knowledge graph operations:

```
await call_tool("chatdag", "ingest_data", {"path": "/path/to/code", "recursive": True})
await call_tool("chatdag", "crystallize_thought", {"topic": "system architecture"})
```

### Reflective Agent Architecture (RAA)

Access formal logic and meta-cognitive tools:

```
await call_tool("reflective_agent_architecture", "prove", {
    "premises": ["all x (human(x) -> mortal(x))", "human(socrates)"],
    "conclusion": "mortal(socrates)"
})
await call_tool("reflective_agent_architecture", "check_cognitive_state", {})
```

## How It Works

1. **Discovery**: On startup, discovers all configured MCP servers
2. **Semantic Search**: `explore_tools(mode="search", query="...")` finds relevant tools
3. **Execution**: `execute_code` runs Python in isolated Docker containers
4. **Persistence**: Results saved to filesystem, skills indexed for reuse
5. **Delegation**: Complex tasks spawn sub-agents with automatic depth tracking

## License

Dual Licensed:

- **AGPL-3.0**: Free for personal, academic, and open source use
- **Commercial License**: Required for business use

See [LICENSE.md](https://github.com/angrysky56/mcp_coordinator/blob/main/LICENSE.md) for details.

---

*Created by Tyler Blaine Hall ([@angrysky56](https://github.com/angrysky56)) Claude Opus 4.5 and Gemini Pro 3*