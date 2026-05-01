---
title: "angrysky56/sheaf-consistency-enforcer"
source: "https://github.com/angrysky56/sheaf-consistency-enforcer"
author:
published:
created: 2026-05-01
description: "Contribute to angrysky56/sheaf-consistency-enforcer development by creating an account on GitHub."
tags:
  - "clippings"
---
## Sheaf Consistency Enforcer

Sheaf Laplacian-based consistency enforcer for **Kernel 1 persistence** across the EFH MCP tool stack.

Part of the [Emergent Functional Hierarchies Framework](https://github.com/angrysky56/Emergent-Functional-Hierarchies-Framework).  
For full agent operating instructions: [docs/agent-instructions.md](https://github.com/angrysky56/Emergent-Functional-Hierarchies-Framework/blob/main/docs/agent-instructions.md)

Closes the "missing piece" identified in the AI application analysis: the automatic feedback loop that detects and recovers from lumpability failures before they cascade.

## Theory Mapping

| EFH / Persistence Theory | Enforcer implementation |
| --- | --- |
| Reciprocal Coherence Kernel K\_T | Active agent set with all edges defined |
| Λ(K\_T) < τ\_{T,m} | Agents updated within coherence\_window\_s |
| Restriction maps F\_{i→e} | `restriction_maps` dict per edge |
| Coboundary δFx | `coboundary_norm()` — intersection of projected keys |
| Dual variable (buffering capacity T) | `edge.dual_variable` accumulated per cycle |
| H¹(G;F) ≠ 0 | `detect_h1_obstruction()` 3-cycle sum check |
| Strong lumpability | KERNEL1 status + mean\_coboundary < ε\_primal |
| Weak lumpability | WEAK status — residuals elevated |
| Kernel retreat | `trigger_recovery("kernel_retreat")` |
| Re-partition | `trigger_recovery("re_partition")` |

## Installation

```
cd sheaf-consistency-enforcer
uv sync
```

## MCP Config

```
{
  "mcpServers": {
    "sheaf-consistency-enforcer": {
      "command": "uv",
      "args": ["--directory", "/your/path/to/sheaf-consistency-enforcer", "run", "sheaf-enforcer"]
    }
  }
}
```

## Workflow

After each MCP tool call, report its output as agent state:

```
register_agent_state("hipai-montague", {
    "last_assertion": "Causal closure implies computational closure",
    "belief_score": 0.95,
    "inconsistency_flag": False
})

register_agent_state("mcp-logic", {
    "last_proof_result": "Causal closure implies computational closure",
    "proof_confidence": 0.98,
    "contradictions_found": False
})

run_admm_cycle()     # returns closure_status + warnings
get_closure_status() # concise summary + interpretation
```

## Recovery

```
# H1 obstruction detected:
trigger_recovery("kernel_retreat")

# ADMM stalled — macro states no longer lumpable:
trigger_recovery("re_partition", target_agent="hipai-montague")

# High coboundary norms:
trigger_recovery("admm_reset")
```

## Tools

| Tool | Purpose |
| --- | --- |
| `register_agent_state` | Report current state for an MCP agent |
| `run_admm_cycle` | Execute one full ADMM consistency cycle |
| `get_closure_status` | Closure status + top-pressure edges |
| `set_restriction_map` | Define/update restriction map for an edge |
| `get_edge_report` | Detailed report for a specific agent pair |
| `trigger_recovery` | Execute recovery strategy |
| `configure_thresholds` | Tune ε\_primal, dual threshold, coherence window |
| `reset_session` | Clear all state, reload defaults |

## Default Restriction Maps

Pre-wired for the EFH stack. All bidirectional edges share three edge-space keys:

- `edge_claim` — the proposition under scrutiny
- `edge_confidence` — degree of certainty (0–1)
- `edge_inconsistent` — contradiction flag

Edges: hipai-montague ↔ mcp-logic ↔ advanced-reasoning ↔ hipai-montague + verifier-graph hub.