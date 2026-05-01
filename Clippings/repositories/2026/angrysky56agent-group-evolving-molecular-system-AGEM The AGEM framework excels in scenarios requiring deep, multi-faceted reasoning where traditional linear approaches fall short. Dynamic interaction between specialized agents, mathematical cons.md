---
title: "angrysky56/agent-group-evolving-molecular-system-AGEM: The AGEM framework excels in scenarios requiring deep, multi-faceted reasoning where traditional linear approaches fall short. Dynamic interaction between specialized agents, mathematical consistency guarantees, and adaptive recovery mechanisms that maintain reasoning quality when confronting highly complex, ambiguous, or contradictory information."
source: "https://github.com/angrysky56/agent-group-evolving-molecular-system-AGEM"
author:
published:
created: 2026-05-01
description: "The AGEM framework excels in scenarios requiring deep, multi-faceted reasoning where traditional linear approaches fall short. Dynamic interaction between specialized agents, mathematical consistency guarantees, and adaptive recovery mechanisms that maintain reasoning quality when confronting highly complex, ambiguous, or contradictory information. - angrysky56/agent-group-evolving-molecular-system-AGEM"
tags:
  - "clippings"
---
## Agent Group Evolving Molecular System (AGEM)

RLM-LCM Molecular-CoT Group Evolving Agents — Sheaf-theoretic multi-agent coordination with lumpability-audited context management and self-healing cognitive architecture.

**Documentation**:

- [Original Project Specification](https://github.com/angrysky56/agent-group-evolving-molecular-system-AGEM/blob/master/docs/RLM-LCM-Molecular-CoT-Group-Evolving-Agents.md) — technical deep-dive into the core architecture
- [Emergent Constraints & Development Plan](https://github.com/angrysky56/agent-group-evolving-molecular-system-AGEM/blob/master/docs/emergent-constraints-and-development-plan.md) — theoretical foundation (memory bottlenecks as syntax engines, C-Induction via sheaf cohomology, Price equation for CoT evolution) and development roadmap

AGEM is a multi-agent orchestration framework that uses molecular biological metaphors and advanced mathematical structures to manage group-evolving agent behaviors. Instead of programming rules into agents, it creates computational pressures — memory bottlenecks, coordination requirements, topology constraints — and lets the rules emerge. It leverages cellular sheaves for agent stalk tracking, cohomology for structural obstruction detection, information-theoretic auditing to detect when context compression loses critical reasoning variables, and real-time SOC metrics with an interactive dashboard.

---

## EFHF System — Required MCP Servers

AGEM's cognitive architecture is built on the **Emergent Functional Hierarchy Framework (EFHF)** — [a system of coordinated MCP servers](https://github.com/angrysky56/Emergent-Functional-Hierarchies-Framework) that provide mathematical consistency guarantees, ethical constraint enforcement, and reasoning provenance tracking across agent sessions.

| Server | Role | Repository |
| --- | --- | --- |
| **sheaf-consistency-enforcer** | Enforces Kernel 1 causal closure across agents via ADMM. Detects H^1 obstructions when agent states become inconsistent. | [angrysky56/sheaf-consistency-enforcer](https://github.com/angrysky56/sheaf-consistency-enforcer) |
| **conscience-servitor** | EFHF L2–L5 ethical evaluation with triage, intent decoding, and audit logging. Implements the Paraclete Protocol for harm prevention. | [angrysky56/conscience-servitor](https://github.com/angrysky56/conscience-servitor) |
| **hipai-montague** | Montague-grammar world model with belief tracking, hypothesis evaluation, and the Paraclete Protocol's calibrate/escalate pipeline. | [angrysky56/HiPAI-Montague-Semantic-Cognition](https://github.com/angrysky56/HiPAI-Montague-Semantic-Cognition) |
| **advanced-reasoning** | Meta-cognitive reasoning with confidence tracking, hypothesis testing, graph-based memory libraries, and SystemJSON structured storage. | [angrysky56/advanced-reasoning-mcp](https://github.com/angrysky56/advanced-reasoning-mcp) |
| **verifier-graph** | DAG-structured reasoning provenance. Every claim traces back to its premises via the causal light cone. | [angrysky56/vgcp-mcp-server](https://github.com/angrysky56/vgcp-mcp-server) |
| **mcp-logic** | Formal logic: Prover9/Mace4 theorem proving, abductive explanation, contingency checking, categorical diagram commutativity. | [angrysky56/mcp-logic](https://github.com/angrysky56/mcp-logic) |
| **cognitive-diagram-nav** | Diagram creation, navigation, reachability analysis, pattern matching, and semantic search over cognitive structures. | [angrysky56/cognitive-diagram-nav-mcp](https://github.com/angrysky56/cognitive-diagram-nav-mcp) |
| **aseke-compass** | ASEKE behavioral analysis: maps Panksepp primary emotional systems, matches behavioral patterns, bridges to political orientation tendencies. | [angrysky56/aseke-compass-mcp](https://github.com/angrysky56/aseke-compass-mcp) |

### Utility MCP Servers (included in mcp.json)

| Server | Source |
| --- | --- |
| sqlite | `uvx mcp-server-sqlite` (PyPI) |
| memory | `@modelcontextprotocol/server-memory` (npm) |
| desktop-commander | `@wonderwhy-er/desktop-commander` (npm) |
| fetch | `uvx mcp-server-fetch` (PyPI) |
| playwright | `@playwright/mcp` (npm) |
| docker-mcp | `uvx docker-mcp` (PyPI) |

---

## System Tools Available to Users

AGEM exposes its capabilities through MCP tools that any connected LLM agent can call natively. These tools fall into five functional categories:

### Consistency & Coordination (sheaf-consistency-enforcer)

- **`register_agent_state`** — Register or update an agent's current state snapshot (assertions, confidence, hypotheses). The enforcer tracks all active agents and runs ADMM to detect inconsistencies.
- **`get_closure_status`** — Check whether the system is in Kernel 1 (full causal closure). Returns H^1 obstruction flags, edge health, convergence status, and actionable interpretation.
- **`set_restriction_map`** — Define how one agent's state maps to another's on the sheaf edge. Both directions of a bidirectional edge must use the same `to_key` names.
- **`get_edge_report`** — Detailed consistency report for a specific agent pair: dual variables, primal/dual residuals, projected states, and convergence status.
- **`trigger_recovery`** — Execute a recovery strategy when obstructions are detected. Strategies: `kernel_retreat`, `re_partition`, `admm_reset`, `soft_relax`, `fusion`.

### Ethical Constraint Enforcement (conscience-servitor + hipai-montague)

- **`triage`** — Classify any prompt or response by ethical risk level before generation. Returns cluster, confidence, risk level, and whether full L2–L5 evaluation is needed.
- **`evaluate`** — Run full EFHF L2–L5 evaluation on a list of claims. Returns KERNEL status, consistency scores, tier-by-tier pass/fail, and pre-response guidance.
- **`decode_intent`** — Read the LLM's predicted response from the embedding *before* generating it. Use when triage flags high-risk content for pre-generation inspection.
- **`add_belief`** — Add a fact to the HiPAI world model in natural language (e.g., "Socrates is a man"). Beliefs persist across the session and are used for hypothesis evaluation.
- **`evaluate_hypothesis`** — Test a hypothesis against the current knowledge graph. Returns supporting/contradicting evidence from the world model.
- **`calibrate_belief`** / **`escalate_block`** — The Paraclete Protocol pipeline: when an action is blocked by an ethical axiom, `calibrate_belief` seeks disconfirming evidence for the factual premises, and `escalate_block` resolves the epistemic status to a final ruling.

### Reasoning & Provenance (advanced-reasoning + verifier-graph)

- **`advanced_reasoning`** — Multi-step meta-cognitive reasoning with confidence tracking, hypothesis formulation, branching/revision, and automatic memory integration. Each thought step is stored in a graph-based memory system.
- **`query_reasoning_memory`** — Search past reasoning sessions for related insights, hypotheses, and evidence. Builds on previous reasoning without losing context.
- **`create_memory_library`** / **`switch_memory_library`** — Manage separate reasoning libraries per project or domain for clean context separation.
- **`create_system_json`** / **`get_system_json`** — Structured data storage for workflows, instructions, and domain-specific knowledge alongside the reasoning graph.
- **`propose_thought`** — Add a verified node to the verifier-graph reasoning DAG. The Graph Kernel validates constraints before committing.
- **`get_reasoning_chain`** — Trace the full provenance path from root premises to a specific claim. Shows exactly which reasoning steps led to a conclusion.
- **`get_context`** — Retrieve the causal ancestors of a node (the "causal light cone") that should be loaded when reasoning about that node.

### Formal Logic & Proofs (mcp-logic)

- **`prove`** — Prove a logical statement using Prover9 or HCC. Accepts premises and goals in first-order logic syntax.
- **`find_counterexample`** — Use Mace4 to find a finite counterexample that disproves a conjecture.
- **`find_model`** — Use Mace4 to find a finite model satisfying given premises.
- **`abductive_explain`** — Find the VFE-minimizing abductive explanation for an observation from a list of candidate hypotheses.
- **`check_contingency`** — Check if a propositional formula is truth-functionally contingent.
- **`verify_commutativity`** — Verify categorical diagram commutativity.
- **`get_category_axioms`** — Get FOL axioms for category theory structures (category, functor, group, etc.).
- **`analyze_behavior`** — Perform a structured ASEKE analysis of a behavioral pattern, situation, or conflict. Maps to Panksepp primary emotional systems.
- **`match_patterns`** — Given observed behavioral signals, return matching patterns from the library with confidence scores.
- **`bridge_to_political`** — Given active primary emotional systems, assess probable political orientation tendencies.
- **`diagram_create`** / **`diagram_save`** / **`diagram_load`** — Create, persist, and retrieve cognitive diagrams.
- **`navigate_guided`** / **`navigate_breadth_first`** — Navigate reasoning spaces within diagrams.
- **`explore_reasoning_space`** — Explore equivalent states and reasoning alternatives within a diagram structure.

---

## Key Features

- **Sheaf-Theoretic Coordination**: Uses `CellularSheaf` to track agent states and restriction maps, enabling robust multi-agent consensus via the Sheaf Laplacian and ADMM.
- **Topological Obstruction Detection**: Employs `CohomologyAnalyzer` to identify structural gaps (H^1) in agent communication and knowledge via SVD of the coboundary operator.
- **Lumpability Auditing**: The `LumpabilityAuditor` detects information loss at LCM compaction boundaries by comparing embedding entropy profiles of source entries vs summary nodes — classifying compressions as strongly or weakly lumpable.
- **System 1 Override Detection**: `RegimeValidator.detectEarlyConvergence()` flags when embedding entropy stabilizes before structural entropy has developed — the mathematical signature of "conclusion precedes logic."
- **Text Network Analysis (TNA)**: Semantic graph processing including community detection (Louvain), centrality analysis, structural gap detection, ForceAtlas2 layout, and catalyst question generation.
- **Lifecycle Context Model (LCM)**: Lossless context management with embedding-based search, three-level escalation protocol, and guaranteed convergence via deterministic fallback.
- **Self-Organized Criticality (SOC)**: Real-time tracking of system criticality (CDP, VNE, EE, SER) with dynamic phase transition detection, regime validation, and stability classification.
- **Molecular Chain-of-Thought**: Reasoning topology using covalent bonds (strong logical dependency), hydrogen bonds (self-reflection), and Van der Waals forces (exploration) with enforced behavioral invariants.
- **MCP Bridge**: Optional cross-session coordination that maps internal lumpability auditing to external sheaf-consistency-enforcer, verifier-graph, and hipai-montague MCP servers.
- **Full-Stack Chat Interface**: React + Express interface with SSE streaming, session history, knowledge base persistence, and interactive settings.
- **Interactive System Dashboard**: Real-time vitals strip (iteration, regime, state, CDP, H¹), tabbed content (Graph visualization, SOC sparklines, event log), quick action buttons with explanatory tooltips, and toast notifications for critical events (System 1, weak lumpability, phase transitions). Independent SSE event stream at `/api/v1/system/events`.
- **Meta-Tool MCP Access**: Instead of flooding models with 50+ tool schemas, 3 meta-tools (`list_mcp_servers`, `list_server_tools`, `call_mcp_tool`) give every model dynamic access to all connected MCP servers through a compact 13-tool interface. Pattern adapted from the mcp\_coordinator project.
- **Provider Embeddings**: `ProviderEmbedder` calls Ollama (`/api/embeddings` with nomic-embed-text) or OpenRouter (`/embeddings` with gemini-embedding-001) for real semantic similarity. Graceful dimension-aware fallback to hash-based mock. `/api/v1/system/embeddings` endpoint for external consumers.
- **Interactive CLI**: Commander.js-based terminal REPL for quick chat interactions and system management.
- **Tri-Provider LLM Support**: Ollama (local), OpenRouter (cloud), and Anthropic with provider-correct tool calling formats, model capability detection via `/api/show`, and content fallback parsing for models that output tool calls as text.
- **Agent Skills System**: YAML-frontmatter based dynamic skill definition loaded natively into the prompt.

## Tech Stack

### Core Engine

- **Language**: [TypeScript](https://www.typescriptlang.org/) (ES2022)
- **Runtime**: [Node.js](https://nodejs.org/) v20+
- **Mathematics**: [mathjs](https://mathjs.org/), [ml-matrix](https://github.com/mljs/matrix)
- **NLP**: [natural](https://github.com/NaturalNode/natural), [wink-lemmatizer](https://winkjs.org/), [stopword](https://github.com/fergiemcdowall/stopword)
- **Graph Theory**: [graphology](https://graphology.github.io/) (Louvain, Metrics, Layout)
- **AI/ML**: [@huggingface/transformers](https://huggingface.co/docs/transformers.js/)
- **Testing**: [Vitest](https://vitest.dev/)

### Interface

- **Backend**: [Express](https://expressjs.com/) + SSE streaming
- **Frontend**: [React](https://react.dev/) + [Vite](https://vite.dev/) + TypeScript
- **State**: [Zustand](https://zustand.docs.pmnd.rs/) (persisted to localStorage)
- **LLM Providers**: Ollama (local), OpenRouter (cloud)

## Project Structure

```
agent-group-evolving-molecular-system-AGEM/
├── src/                       # Core AGEM engine
│   ├── orchestrator/          # Central coordination + obstruction handling
│   │   ├── ComposeRootModule  #   Composition root — wires all modules
│   │   ├── ObstructionHandler #   H^1 → gap detection → agent spawn pipeline
│   │   ├── VdWAgentSpawner    #   Van der Waals exploratory agent management
│   │   └── EventBus           #   Central typed event coordination
│   ├── sheaf/                 # CellularSheaf + CohomologyAnalyzer
│   │   ├── CellularSheaf      #   Graph topology with validated restriction maps
│   │   ├── CohomologyAnalyzer #   SVD-based H^0/H^1 computation + events
│   │   ├── SheafLaplacian     #   B^T B assembly and eigenspectrum
│   │   └── ADMMSolver         #   Gradient descent toward consensus
│   ├── tna/                   # Text Network Analysis pipeline
│   │   ├── CooccurrenceGraph  #   4-gram weighted semantic network
│   │   ├── LouvainDetector    #   Community detection + modularity
│   │   ├── CentralityAnalyzer #   Betweenness centrality time series
│   │   ├── GapDetector        #   Structural hole identification
│   │   └── LayoutComputer     #   ForceAtlas2 visualization
│   ├── soc/                   # Self-Organized Criticality tracker
│   │   ├── SOCTracker         #   All 5 SOC metrics + phase transitions
│   │   └── RegimeValidator    #   Regime stability + System 1 detection
│   ├── lcm/                   # Lifecycle Context Model
│   │   ├── ImmutableStore     #   Append-only ground truth
│   │   ├── ContextDAG         #   Hierarchical summary DAG
│   │   └── EscalationProtocol #   Three-level guaranteed convergence
│   ├── lumpability/           # Lumpability auditing (NEW)
│   │   ├── LumpabilityAuditor #   Entropy ratio + centroid drift detection
│   │   ├── entropyProfile     #   Embedding entropy computation
│   │   └── MCPBridge          #   Cross-session MCP coordination
│   └── types/                 # Shared type definitions + events
├── interface/                 # Full-stack chat interface
│   ├── backend/               #   Express API + SSE streaming
│   │   └── src/services/      #   LLM providers, agem-bridge, provider-embedder, MCP manager
│   ├── frontend/              #   React + Vite + TypeScript
│   │   └── src/
│   │       ├── components/dashboard/  # SystemVitals, MetricsPanel, EventLog, QuickActions, Toasts
│   │       ├── hooks/                 # useSystemEvents (SSE connection)
│   │       └── stores/                # chat.ts, agem.ts (system state), settings.ts
│   └── shared/                #   FE ↔ BE type contract
├── cli/                       # Interactive terminal REPL
├── skills/                    # YAML-frontmatter agent skill definitions
├── knowledge_base/            # Persistent outputs (reports, analysis)
├── mcp.json                   # MCP server configuration
└── mcp.json.example           # Template MCP config
```

## Getting Started

### 1\. Clone & Install

```
git clone https://github.com/angrysky56/agent-group-evolving-molecular-system-AGEM.git
cd agent-group-evolving-molecular-system-AGEM
npm install
```

### 2\. Install EFHF MCP Servers

Clone the required MCP servers into a sibling directory:

```
cd ..  # parent directory of AGEM
git clone https://github.com/angrysky56/sheaf-consistency-enforcer.git
git clone https://github.com/angrysky56/conscience-servitor.git
git clone https://github.com/angrysky56/HiPAI-Montague-Semantic-Cognition.git
git clone https://github.com/angrysky56/advanced-reasoning-mcp.git
git clone https://github.com/angrysky56/vgcp-mcp-server.git
git clone https://github.com/angrysky56/mcp-logic.git
git clone https://github.com/angrysky56/cognitive-diagram-nav-mcp.git
git clone https://github.com/angrysky56/aseke-compass-mcp.git
```

Each server has its own setup instructions in its README. Most Python servers use `uv`; Node servers use `npm install && npm run build`.

### 3\. Configure Environment

```
cp .env.example .env
# Edit .env — set LLM_PROVIDER, API keys, model names
```

### 4\. Configure MCP Servers

```
cp mcp.json.example mcp.json
# Edit mcp.json — update paths to match your MCP server locations
```

### 5\. Run the Core Engine Tests

```
npm test
```

### 6\. Start the Interface

```
./start.sh
```

This installs dependencies (if needed), copies `.env.example` → `.env` (if missing), and starts both servers. The frontend will be available at `http://localhost:5173` with API proxy to the backend on port 8000. Press `Ctrl+C` to stop both.

```
# Or start individually:
./start.sh --backend    # Backend only
./start.sh --frontend   # Frontend only
./start.sh --install    # Force reinstall dependencies
```

## Configuration

All configuration lives in `.env` at the project root. Key settings:

| Variable | Default | Description |
| --- | --- | --- |
| `LLM_PROVIDER` | `ollama` | Active provider (`ollama`, `openrouter`, or `anthropic`) |
| `OLLAMA_BASE_URL` | `http://localhost:11434` | Ollama API endpoint |
| `OLLAMA_MODEL` | `gemma3:latest` | Ollama chat model |
| `OLLAMA_EMBEDDING_MODEL` | `nomic-embed-text:latest` | Ollama embedding model |
| `OPENROUTER_API_KEY` | — | OpenRouter API key |
| `OPENROUTER_BASE_URL` | `https://openrouter.ai/api/v1` | OpenRouter API endpoint |
| `OPENROUTER_MODEL` | `google/gemini-2.5-flash-preview` | OpenRouter chat model |
| `OPENROUTER_EMBEDDING_MODEL` | `google/gemini-embedding-001` | OpenRouter embedding model |
| `PORT` | `8000` | Backend server port |

## Architecture

### How the Modules Interact

```
User Prompt → Orchestrator.runReasoning()
    │
    ├─→ TNA: preprocess → co-occurrence graph → Louvain → centrality → gaps
    ├─→ LCM: append to ImmutableStore → ProviderEmbedder → embedding cache
    ├─→ Sheaf: cohomology analysis → H^0 (consensus) or H^1 (obstruction)
    ├─→ SOC: VNE + EE + CDP + SER + correlation → phase transitions → regime
    ├─→ Lumpability: audit compaction → entropy ratio → strong/weak classification
    │
    ├─→ [H^1 detected] → ObstructionHandler → GapDetector → VdW agent spawn
    ├─→ [Weak lumpability] → EventBus → recovery via lcm_expand
    ├─→ [System 1 override] → soc:system1-early-convergence event
    │
    ├─→ MCP Meta-Tools: list_mcp_servers → list_server_tools → call_mcp_tool
    │   (dynamic discovery of sheaf-enforcer, advanced-reasoning, hipai, etc.)
    │
    ├─→ Dashboard SSE: /api/v1/system/events → SystemVitals + Sparklines + EventLog
    │
    └─→ MCP Bridge (optional): register states with sheaf-consistency-enforcer,
        log provenance in verifier-graph, track beliefs in hipai-montague
```

All events flow through the central `EventBus`. Modules communicate exclusively via typed events — only `ComposeRootModule` imports from multiple modules.

### Module Isolation

Each module (sheaf, lcm, tna, soc, lumpability) has **zero cross-imports** to other modules. This is statically enforced by isolation tests in each module. Only the orchestrator's `ComposeRootModule` is permitted to import from multiple modules simultaneously. The lumpability module imports narrowly from `lcm/interfaces` (IEmbedder, ITokenCounter) and `soc/entropy` (embeddingEntropy, cosineSimilarity).

## Available Scripts

| Command | Description |
| --- | --- |
| `npm run build` | Compiles the TypeScript project (core engine). |
| `npm test` | Runs the full Vitest suite. |
| `npm run test:watch` | Runs Vitest in watch mode. |
| `npm run typecheck` | Runs the TypeScript compiler in no-emit mode. |

## Interface

The interface wraps the AGEM engine with a chat-like experience:

- **Backend** serves a REST + SSE API on port 8000. Chat completions stream tokens via Server-Sent Events. A separate `/system/events` SSE endpoint streams engine state, SOC metrics, phase transitions, and obstructions to the dashboard in real-time. Sessions persist as JSON files.
- **Frontend** is a React SPA with a dark glassmorphism theme. The left panel shows chat; the right panel is an interactive dashboard with system vitals, SOC sparklines, event log, graph visualization, and quick action buttons. Uses Zustand for state management with separate stores for chat and system state.
- **Dashboard** shows real-time engine state: iteration count, regime classification, operational state, CDP, H¹ obstructions, graph stats. Metrics tab renders SOC sparklines (VNE, EE, CDP, SER, Correlation). Events tab shows a filtered stream of system events. Toast notifications surface critical events (System 1 override, weak lumpability, phase transitions).
- **Meta-Tool Access** lets the LLM dynamically discover and invoke any connected MCP server through 3 compact meta-tools, instead of overwhelming the context with 50+ tool schemas.
- **CLI** provides a fully interactive terminal REPL for quick querying, testing, and managing the server.
- **Agent Skills** system traverses the `skills/` directory, extracts context from YAML frontmatter in `.md` files, and exposes them as selectable knowledge areas to the agent.
- **MCP Integration** connects to configured external Model Context Protocol servers (see `mcp.json`) to dynamically register tools that the LLM agent can call natively.

## License

MIT (or check `LICENSE` file if present)