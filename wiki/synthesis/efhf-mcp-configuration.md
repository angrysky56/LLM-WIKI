---
summary: Master MCP configuration for the EFHF stack.
tags: [mcp, infrastructure, config]
updated: 2026-05-01T07:58:00Z
created: 2026-05-01T07:51:15Z
---

---

created: 2026-05-01T07:51:00Z
updated: 2026-05-01T07:58:00Z
type: synthesis
summary: Unified MCP configuration for the EFHF (Emergent Functional Hierarchies Framework) ecosystem.
tags: [mcp, infrastructure, configuration, efhf]
status: active
confidence: 1.0

---

# EFHF Unified MCP Configuration

This document provides the master configuration for the [[efhf]] (Emergent Functional Hierarchies Framework) Model Context Protocol (MCP) ecosystem. This configuration allows a compliant MCP client (like Claude Desktop) to connect to the entire cognitive stack.

## Installation

To use this configuration with **Claude Desktop**, add the following JSON to your `config.json` file:

- **Linux**: `~/.config/Claude/config.json`
- **macOS**: `~/Library/Application Support/Claude/config.json`

## Unified Configuration

```json
{
  "mcpServers": {
    "project-synapse": {
      "command": "uv",
      "args": [
        "--directory",
        "/home/ty/Repositories/ai_workspace/project-synapse-mcp",
        "run",
        "python",
        "-m",
        "synapse_mcp.server"
      ],
      "env": {
        "NEO4J_URI": "bolt://localhost:7687",
        "NEO4J_USER": "neo4j",
        "NEO4J_PASSWORD": "synapse_password",
        "NEO4J_DATABASE": "synapse",
        "WIKI_VAULT_PATH": "/home/ty/Documents/LLM-WIKI"
      }
    },
    "hipai-montague": {
      "command": "uv",
      "args": [
        "--directory",
        "/home/ty/Repositories/ai_workspace/HiPAI-Montague-Semantic-Cognition",
        "run",
        "python",
        "-m",
        "hipai.mcp_server"
      ],
      "env": {
        "PYTHONPATH": "src"
      }
    },
    "mcp-logic": {
      "command": "uv",
      "args": [
        "--directory",
        "/home/ty/Repositories/ai_workspace/mcp-logic",
        "run",
        "mcp_logic",
        "--prover-path",
        "/home/ty/Repositories/ai_workspace/mcp-logic/ladr/bin"
      ]
    },
    "advanced-reasoning": {
      "command": "node",
      "args": [
        "/home/ty/Repositories/ai_workspace/advanced-reasoning-mcp/build/index.js"
      ]
    },
    "sheaf-consistency-enforcer": {
      "command": "uv",
      "args": [
        "--directory",
        "/home/ty/Repositories/ai_workspace/sheaf-consistency-enforcer",
        "run",
        "sheaf-enforcer"
      ]
    },
    "conscience-servitor": {
      "command": "uv",
      "args": [
        "--directory",
        "/home/ty/Repositories/ai_workspace/conscience-servitor",
        "run",
        "conscience-servitor"
      ]
    },
    "seg-narrative": {
      "command": "uv",
      "args": [
        "--directory",
        "/home/ty/Repositories/ai_workspace/sentience_metaphysics",
        "run",
        "-m",
        "mcp_server.server"
      ],
      "env": {
        "AI_PROVIDER": "ollama"
      }
    },
    "verifier-graph": {
      "command": "node",
      "args": [
        "/home/ty/Repositories/ai_workspace/vgcp-mcp-server/build/index.js"
      ]
    }
  }
}
```

## Component Roles (EFHF Layers)

| Server                         | Role                                            | Layer |
| :----------------------------- | :---------------------------------------------- | :---- |
| **project-synapse**            | Grounding layer (Wiki & Neo4j Indexing)         | 0     |
| **hipai-montague**             | World Model (Semantic Cognition)                | 2     |
| **mcp-logic**                  | Structural Verification (Theorem Proving)       | 3     |
| **advanced-reasoning**         | Meta-Cognitive Monitoring (Confidence Tracking) | 4     |
| **sheaf-consistency-enforcer** | Sheaf Consistency Enforcement                   | 5     |
| **seg-narrative**              | Experiential Reasoning (Persona Councils)       | 5     |
| **conscience-servitor**        | Ethical Triage (Pre-response Enforcement)       | 5+    |

## Environment Requirements

- **Python**: All Python-based servers use `uv` for environment management.
- **Node.js**: Required for `advanced-reasoning`.
- **Neo4j**: Required for `project-synapse`.
- **Ollama**: Required for `seg-narrative` and local LLM inference.
- **Prover9/Mace4**: Bundled in `mcp-logic/ladr/bin`.

## Troubleshooting

1. **Absolute Paths**: Ensure all paths in `args` and `command` are absolute. This config uses the standard `/home/ty/Repositories/ai_workspace/` base.
2. **UV Directory**: The `--directory` flag ensures `uv` runs in the correct environment context.
3. **Database Connectivity**: Ensure Neo4j is running for `project-synapse`.

## Connections

- [[efhf]]
- [[project-synapse]]
- [[sentience-metaphysics]]
- [[agent-group-evolving-molecular-system-agem]]
