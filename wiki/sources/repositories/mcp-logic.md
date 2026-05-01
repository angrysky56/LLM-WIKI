---
summary: Source summary for mcp-logic.
tags: [sources, repositories]
updated: 2026-05-01T07:06:32Z
created: 2026-05-01T07:06:32Z
---

---
created: 2026-05-01T07:06:27Z
updated: 2026-05-01T07:06:27Z
type: source
summary: Source summary for the mcp-logic repository.
tags: [sources, repositories, ty-repo, logic]
sources: https://github.com/angrysky56/mcp-logic
status: active
confidence: 1.0
---

# Source: mcp-logic

The **mcp-logic** repository contains a Model Context Protocol (MCP) server that bridges to the LADR (Prover9 and Mace4) libraries for formal first-order logic reasoning.

## Key Components
- `src/mcp_logic/server.py`: Core MCP server with 8 specialized logic tools.
- `vfe_engine.py`: Implements abductive reasoning via Variational Free Energy.
- `hcc_prover.py`: Implements Hypersequent Contingency Calculus for propositional checks.
- `categorical_helpers.py`: Logic generation for category theory axioms.

## Key Documents
- `ENHANCEMENTS.md`: Overview of v0.2.0 and v0.3.0 features.
- `Documents/`: Theoretical deep-dives into HCC and VFE.

## Connections
- [[mcp-logic]] — The entity page for this project.
- [[tyler-hall|angrysky56]] — Repository owner.
