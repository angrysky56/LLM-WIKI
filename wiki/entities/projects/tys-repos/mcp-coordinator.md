---
summary: Project page for mcp-coordinator.
tags: [projects, ty-repo, orchestration]
updated: 2026-05-01T07:06:12Z
created: 2026-05-01T07:06:12Z
---

---
created: 2026-05-01T07:06:06Z
updated: 2026-05-01T07:06:06Z
type: entity
summary: Self-optimizing MCP orchestrator that uses semantic tool discovery, Docker execution, and agent delegation.
tags: [projects, ty-repo, angrysky56, orchestration, mcp, docker, sub-agents, autonomous-agents]
status: active
confidence: 1.0
---

# MCP-Coordinator

**MCP-Coordinator** is a "Meta-Operating System" for AI agents developed by [[tyler-hall|Ty]]. It bridges the gap between high-level human intent and low-level system execution through self-optimizing orchestration.

## Key Pillars
1. **Autonomous Epistemic Evolution**: Captures successful logic and execution paths as "Skills" for long-term persistence.
2. **Recursive Complexity Management**: Spawns specialized sub-agents via `coordinator_task` to handle modular sub-problems without context bloat.
3. **Dynamic Environmental Mapping**: Semantically discovers and understands novel MCP tools in real-time.
4. **Hybrid Logic Orchestration**: Blends Python-based algorithmic logic (Rational Actor) with direct MCP tool calls (Direct Actor).
5. **Reflective Self-Correction (RAA)**: Uses the Reflective Agent Architecture and verifier-graph integration to ensure justified belief over hallucination.

## Tools
- `execute_code`: Run Python in sandboxed Docker containers.
- `coordinator_task`: Delegate complex tasks to sub-agents.
- `save_skill` / `run_skill`: Build a persistent library of reusable code.
- `find_tools` / `call_tool`: Semantic discovery and execution of any MCP tool.

## Connections
- [[efhf]] — The overarching architectural framework.
- [[conscience-servitor]] — Provides ethical triage for coordinator tasks.
- [[tys-repos]] — Part of Ty's repository collection.
