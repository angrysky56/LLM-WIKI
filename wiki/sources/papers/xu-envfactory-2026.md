---
created: 2026-05-20T12:20:00Z
updated: 2026-05-20T12:20:00Z
type: source
summary: "EnvFactory: Automated synthesis of executable MCP tool environments for agentic RL training, using topology-aware graph sampling and calibrated query refinement to produce realistic multi-turn trajectories with implicit human intents."
tags: [tool-use-agents, environment-synthesis, agentic-rl, mcp, credit-assignment, robust-rl]
status: active
confidence: high
arXiv: 2605.18703v1
authors: "Minrui Xu, Zilin Wang, Mengyi Deng, Zhiwei Li, Zhicheng Yang, Xiao Zhu, Yinhong Liu, Boyu Zhu, Baiyu Huang, Chao Chen, Heyuan Deng, Fei Mi, Lifeng Shang, Xingshan Zeng, Zhijiang Guo"
institutions: ["HKUST (GZ)", "Huawei Technologies", "University of Cambridge", "UCL"]
date: 2026-05-18
paper: /home/ty/Documents/paper-research/2605.18703v1.pdf
github: https://github.com/LARK-AI-Lab/EnvFactory
---

# EnvFactory: Scaling Tool-Use Agents via Executable Environments Synthesis and Robust RL

**arXiv**: [2605.18703v1](https://arxiv.org/abs/2605.18703) | **GitHub**: [LARK-AI-Lab/EnvFactory](https://github.com/LARK-AI-Lab/EnvFactory)

## Metadata

| Field | Value |
|-------|-------|
| **Title** | EnvFactory: Scaling Tool-Use Agents via Executable Environments Synthesis and Robust RL |
| **Authors** | Minrui Xu\*, Zilin Wang\*, Mengyi Deng, Zhiwei Li, Zhicheng Yang, Xiao Zhu, Yinhong Liu, Boyu Zhu, Baiyu Huang, Chao Chen, Heyuan Deng, Fei Mi, Lifeng Shang, Xingshan Zeng†, Zhijiang Guo† |
| **Institutions** | HKUST (GZ) (LARK Lab), Huawei Technologies, University of Cambridge, UCL |
| **Published** | 18 May 2026 |
| **Categories** | cs.CL (Computation and Language) |
| **Framework** | Agentic RL / Tool-Use LLM Agents |

---

## Executive Summary

EnvFactory addresses two core bottlenecks in Agentic Reinforcement Learning: (1) the lack of scalable, robust, executable tool environments, and (2) the scarcity of realistic training data that captures implicit human reasoning. The framework fully automates environment construction via a three-agent pipeline (Search Agent → Code Agent → Test Agent), then synthesizes natural multi-turn trajectories through topology-aware graph sampling and calibrated query refinement.

Key results: with only **85 verified environments** (842 tools, 7 domains), EnvFactory generates 2,575 SFT and RL trajectories and outperforms baselines using 5× more environments—achieving +15% on BFCLv3, +8.6% on MCP-Atlas, and +6% on τ²-Bench and VitaBench.

---

## Technical Approach

### 3.1 Problem Setup

EnvFactory defines tool-agentic interaction as a tuple **E = (m, D, π, Vₑ)** where:
- **m**: environment metadata (descriptions, tool definitions, schemas)
- **D**: stateful database schema (environment state)
- **π**: executable Python implementation
- **Vₑ**: exposed tool interface (via MCP by default)

The pipeline synthesizes high-quality trajectories by first constructing environments via **EnvGen**, then building a dependency tool graph **G = (V, E)** for **topology-aware sampling** via **QueryGen**.

### 3.2 EnvGen: Environment Construction Pipeline

A three-agent collaboration autonomously constructs environments:

1. **Search Agent**: Proposes diverse tool-use scenarios by exploring authentic online resources (API docs, technical reports). Analyzes coverage gaps in existing environments and retrieves source-grounded functionalities. Produces structured metadata **m** including environment descriptions, tool definitions, and schemas.

2. **Code Agent**: Derives stateful database schema **D** from metadata (Pydantic models for entities, relationships, mutable states). Implements executable Python code **π** for each tool, wrapped into standardized MCP tool interfaces **Vₑnew**.

3. **Test Agent**: Creates unit test cases and validates against four criteria:
   - Tool interfaces consistent with metadata
   - Tools import and execute successfully
   - Execution results match expected behavior
   - Database states transition correctly
   
   On failure, produces structured error reports; Code Agent revises. Iterative validation loop continues until all tests pass.

**Result**: 85 verified environments, 842 tools across commerce, finance, travel, office, lifestyle, research, utilities.

### 3.3 Dependency Tool Graph

**Graph Construction (two steps)**:
1. **Semantic Parameter Matching**: BGE-M3 embeddings encode all input/output parameters of every tool. Cosine similarity between output parameter embeddings of vᵢ and input parameter embeddings of vⱼ exceeding threshold → edge (vᵢ → vⱼ).
2. **Logical Dependency Refinement**: LLM analyzes tools in each environment, identifies missing logical dependencies and prunes spurious edges. Critical for parameter-less tools (e.g., `delete_all_notes` in Notion) that semantic matching alone would isolate.

**Topology-Aware Sampling** (Algorithm 1 & 2):
- Operates on directed dependency graph G = (V, E)
- **Backward dependency resolution**: Before adding tool v to visited set V̂, recursively resolves unsatisfied inputs via `SamplePriors`. A parameter pᵢ ∈ I(v) is valid if: (1) optional (has schema default), (2) user-providable per LLM classification, or (3) already produced by some u ∈ V̂ where pᵢ ∈ O(u). Invalid parameters trigger backward traversal to uniformly sample a producer tool u satisfying (u → v) ∈ E and pᵢ ∈ O(u), with recursion depth capped at Dmax = 3. Stochastic override (p = 0.1) occasionally introduces additional priors for diversity.
- **Forward expansion**: Once dependencies resolved, v is added to V̂; algorithm samples one outgoing neighbor from N(v) = {u | (v → u) ∈ E} for subsequent processing.

**Key advantage over naive random walks**: Guarantees all required inputs of each sampled tool are satisfied before inclusion—addressing the key failure mode of random traversal when a tool requires outputs from multiple preceding tools.

### 3.4 QueryGen: Trajectory Synthesis

After sampling tool chain τ = [v₁, ..., vₙ] from the graph:

1. **Scenario Planning**: LLM designs a cohesive narrative (user persona, situation, time/place/context) that naturally motivates the observed tool sequence. Never mentions tools/APIs—only human behaviors and motivations.

2. **State Generation**: Generate JSON schema defining the initial state (databases, entities, relationships).

3. **Query Generation**: Simulated user generates the most plausible natural request motivating the target tool call(s) in the current turn. Builds logically on prior context, uses natural references. Then a calibrated refinement stage injects realistic human communication patterns—implicit intents and ambiguity—transforming rigid "instruction lists" into natural human requests.

**User/Assistant Tool Classification**: LLM classifies available MCP tools into user tools (confidential/sensitive operations like login, reset_password; physically constrained like restart_engine) vs assistant tools. Simulated user is constrained to external parameters only—information human users can realistically provide—preventing implausible responses like verbatim recitation of system-generated IDs.

---

## Key Results

| Metric | EnvFactory | AWM | EnvScaler |
|--------|-----------|-----|-----------|
| **Environments** | **85** ✓ (5× fewer) | 526 | 191 |
| **SFT Trajectories** | 1,622 | 9,022 | 1,622 |
| **RL Trajectories** | 953 | 3,315 | 2,550 |
| **BFCLv3** | +15% (Qwen3) | — | — |
| **MCP-Atlas** | +8.6% (Qwen3) | — | — |
| **τ²-Bench / VitaBench** | +6% | — | — |

Despite using 5× fewer environments than concurrent work, EnvFactory achieves superior training efficiency and downstream performance.

---

## Relevance to EFHF / AGEM / MOP

### Tool-Use Agent Environments

EnvFactory's automated MCP environment synthesis is directly relevant to the **AGEM (Agent Group Evolving Molecular System)** and **MOP (Multi-Agent Orchestration Protocol)** layers. The framework demonstrates:

- **Executable environment construction**: Stateful MCP tool environments that maintain session isolation while enabling write-capable tools to modify shared databases—exactly the kind of robust, low-latency tool execution environments needed for agentic system training.
- **Three-agent pipeline architecture**: Search Agent → Code Agent → Test Agent mirrors the modular,分层 architecture implied by EFHF's layered design (Layer 0 grounding, Layer 2 world modeling, Layer 3 structural verification).
- **Iterative validation loops**: The Test Agent's feedback-driven revision mirrors the verifier graph's constraint propagation.

### Automated Environment Synthesis

EnvFactory's autonomous environment discovery and construction addresses a key bottleneck: the scarcity of scalable, realistic tool-use training environments. This is directly relevant to the [[agentic-research]] challenge of **implementation drift** and **context degradation**—by providing verified, executable environments with proper state management, EnvFactory enables more reliable agent training.

The framework's approach to **automatic tool ecosystem recovery from authentic online resources** (rather than relying on pre-curated specifications) is a significant advance for agentic system scalability.

### Robust RL

EnvFactory employs **Group Relative Policy Optimization (GRPO)** with step-level training samples (each interaction turn treated as an individual training sample). Key characteristics:

- Learning rate 1×10⁻⁶, rollout size 8, batch size 256
- Max trajectory length 16k tokens, max generation length 4k tokens
- 10 epochs training for RL; 3 epochs for SFT
- **Verification-before-reward**: Environments are rigorously verified before being used for RL training, ensuring reliable reward signals and stable policy optimization

The distinction from hallucination-prone LLM simulators and expensive production APIs positions EnvFactory's synthetic environments as the practical middle ground.

### Credit Assignment in Agentic Systems

EnvFactory's approach to credit assignment operates at multiple levels:

1. **Topology-aware sampling**: Recursively resolves tool dependencies before adding tools to the visited set. This ensures coherent logical foundations for trajectory synthesis, implicitly providing credit assignment at the trajectory level.

2. **Dependency graph with semantic matching + LLM refinement**: Captures non-linear relationships between tools, enabling proper sequencing that reflects real tool dependencies.

3. **Step-level RL training**: Each interaction turn is treated as an individual training sample in RL, enabling fine-grained credit assignment at the turn level rather than just trajectory level.

4. **Simulated user patterns with implicit intents**: Injecting ambiguity and natural communication patterns creates realistic decision-making challenges that test the agent's credit assignment abilities.

### Connection to EFHF Architecture

| EFHF Layer | EnvFactory Relevance |
|------------|---------------------|
| **Layer 0 (Grounding)** | Environment construction via authentic resource exploration; project-synapse serves as the index layer |
| **Layer 2 (World Model)** | Semantic parameter matching using BGE-M3 embeddings; simulated user scenarios reflect real-world usage patterns |
| **Layer 3 (Structural Verification)** | Test Agent validation loop; rigorous verification before RL training functions as structural constraint enforcement |
| **Layer 4 (Meta-Cognitive)** | Topology-aware sampling with recursive dependency resolution; adaptive training (stochastic override p=0.1) |
| **Layer 5+ (Experiential/Ethical)** | Implicit intent injection and calibrated refinement for realistic human communication patterns |

---

## Key Quotes

> "EnvFactory addresses both challenges. EnvFactory autonomously explores and verifies stateful, executable tool environments from authentic resources, and synthesizes natural multi-turn trajectories through topology-aware sampling and calibrated refinement, producing grounded queries with implicit intents."

> "Existing approaches depend on costly real-world APIs, hallucination-prone LLM simulators, or synthetic environments that are often single-turn or depend on pre-collected documents."

> "Our approach combines semantic matching with LLM-augmented refinement for graph construction, and introduces a topology-aware sampling strategy that recursively resolves unsatisfied input dependencies before tool selection."

> "Using only 85 verified environments across 7 domains, EnvFactory generates 2,575 SFT and RL trajectories. Despite using significantly fewer environments than prior work, which are often 5 times more, EnvFactory achieves superior training efficiency and downstream performance."

---

## Structural Insights

1. **Three-tier agent collaboration** (Search/Code/Test) mirrors cognitive分层: Search = ideation/planning, Code = execution, Test = evaluation/critique. This is a microcosm of the agentic research pipeline.

2. **Environment as first-class citizen**: Unlike prior work that treats environments as static artifacts, EnvFactory treats environment construction as an automated, iterative, verifiable process with explicit feedback loops.

3. **Topology-aware sampling solves the sequential dependency problem**: Naive random walks fail when tools require outputs from multiple preceding tools. EnvFactory's backward resolution with depth cap (Dmax=3) is a clean solution.

4. **Calibrated refinement bridges the sim-to-real gap**: Transforming rigid "instruction lists" into natural human requests with implicit intents addresses the key failure mode of synthetic trajectories—over-specification.

5. **Verification before reward**: The rigorous test-driven environment construction ensures reward signals are reliable before RL training begins, addressing the stabilization challenge that plagues production-API-based RL.

6. **Session isolation via dedicated transport connections**: Each conversation requires a dedicated MCP connection, creating a throughput bottleneck. Mitigated via asynchronous synthesis pipeline.

---

## Limitations

1. **Throughput bottleneck**: MCP's stateful, write-capable tools with strict session isolation require dedicated transport connections per conversation, constraining parallel tool invocation. Mitigated by asynchronous synthesis pipeline.

2. **Network-dependent environments excluded**: Due to connectivity constraints, evaluation on MCP-Atlas excludes mongodb, oxylabs, brave-search, wikipedia, slack, and google-workspace servers.

3. **Scope limited to MCP**: EnvFactory uses MCP as its tool interface; generalization to other tool protocols not explored.

---

## Related Papers

- **AWM (Wang et al., 2026)**: Abstract scenario seeds → 526 environments; EnvFactory autonomously discovers from online resources instead
- **EnvScaler (Song et al., 2026)**: Builds on existing task sets; EnvFactory requires no pre-collected specifications
- **AutoForge (Cai et al., 2025), AgentScaler (Fang et al., 2025)**: Rely on pre-collected tools/documentation; EnvFactory automates discovery

---

## Connections

- [[agentic-research]] — Agentic research paradigm; EnvFactory addresses implementation drift and context degradation
- [[reward-modeling]] — Process vs outcome reward models; EnvFactory's step-level RL training enables fine-grained credit assignment
- [[efhf]] — EFHF architecture layers align with EnvFactory's three-tier pipeline
- [[agent-group-evolving-molecular-system-agem]] — AGEM/MOP tool-use environment requirements
- [[mcp-model-context-protocol]] — EnvFactory's tool interface standard
- [[project-synapse]] — Grounding layer for environment indexing