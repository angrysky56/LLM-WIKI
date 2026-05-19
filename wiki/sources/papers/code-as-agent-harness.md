---
summary: Survey on code as operational substrate ("harness") for agentic AI systems
tags: [agentic-ai, code-generation, tool-use, multi-agent, survey]
updated: 2026-05-19T16:46:58Z
created: 2026-05-19T16:46:58Z
---

---
title: Code as Agent Harness
authors: Ning, Tieu, Fu, Wei, Li, Bei, Zou, Ai, Liu, Li, Chen, Zhao, Yang, Li, Qian, Li, Lin, Zeng, Qiu, Chen, Sun, Yang, Wang, Pan, Yang, Zhang, Fang, Liu, Wu, Wang, Zhou, Zhang, Chen, Liu, Sun, Wang, Li, Fang, Zhang, Chen, Liu, Shen, Lin, Wang, Xu, Zhao, Zhou, Fang, Liu, Du, Zhang, Wang, Lin, Zeng, Qiu, Chen, Sun, Yang, Wang, Pan, Yang, Zhang, Fang, Liu, Wu, Wang, Zhou, Zhang, Chen, Liu, Shen, Lin, Wang, Xu, Zhao, Zhou, Fang, Liu, Du, Zhang, Wang, Lin, Zeng, Qiu, Chen, Sun, Yang, Wang, Pan, Yang, Zhang, Fang, Liu, Wu, Wang, Zhou, Zhang, Chen, Liu, Shen, Lin, Wang, Xu, Zhao, Zhou, Fang, Liu, Du, Zhang
created: 2026-05-19
updated: 2026-05-19
type: source
summary: "Survey framing code as the operational substrate for agentic AI — the 'harness' connecting agents to reasoning, action, and environment modeling."
tags: [agentic-ai, code-generation, tool-use, multi-agent, survey, planning, memory, verification]
sources: https://arxiv.org/abs/2605.18747
repo: https://github.com/AIOS-Agent/Code-as-Agent-Harness
confidence: high
---

## Core Thesis

Code is no longer just *output* from LLMs — it increasingly serves as the **operational substrate** for agentic AI systems: reasoning, acting, environment modeling, and execution-based verification. The survey frames this shift as **code as agent harness**: code connects agents to the world and enables them to execute, verify, and coordinate.

Three interconnected layers define the harness:

1. **Harness Interface** — how code connects agents to reasoning, action, and environment modeling
2. **Harness Mechanisms** — planning, memory, tool use, feedback-driven control, and optimization
3. **Harness Scaling** — from single-agent to multi-agent settings where shared code artifacts enable coordination, review, and verification

## Key Dimensions

### Harness Interface
Code serves as the bridge between agent cognition and environment. Agents execute code to query state, run tools, and verify results. The harness replaces brittle API wrappers with executable, stateful interfaces.

### Harness Mechanisms
- **Planning**: code as the medium for multi-step reasoning and task decomposition
- **Memory**: code structs as stateful memory schemas; executing code updates persistent world model
- **Tool Use**: code as the universal tool interface — agents write tools as code rather than calling fixed APIs
- **Feedback & Control**: execution-based verification (run code, observe outcome) as the primary feedback signal
- **Optimization**: agents improve their own code-harnesses over time

### Harness Scaling (Multi-Agent)
Shared code artifacts become coordination substrates:
- Code review as agent verification
- Shared code state across agents = consistent world model
- Multi-agent execution of code plans with role specialization

## Applications
Coding assistants, GUI/OS automation, embodied agents, scientific discovery, personalization, DevOps, enterprise workflows.

## Open Challenges
1. **Evaluation beyond final task success** — harness quality metrics
2. **Verification under incomplete feedback** — partial code execution, stochastic environments
3. **Regression-free harness improvement** — improving the harness without breaking existing capabilities
4. **Consistent shared state across agents** — race conditions, stale reads in multi-agent code execution
5. **Human oversight for safety-critical actions** — code execution boundaries
6. **Extension to multimodal environments** — vision, audio, sensorimotor harnesses

## Connections

- [[efhf-mcp-configuration]] — EFHF as a harness substrate: verification via mcp-logic + causal state tracking
- [[ctx2skill]] — Ctx2Skill = agents writing their own skill code; harness engineering for autonomous skill extraction
- [[self-prompting-via-production-stage-architecture]] — self-generated code as behavior directives (production-stage architecture)
- [[synapse-retrieval-architecture]] — retrieval as verification mechanism within a harness
- [[graphify-ai-coding-assistant-skill]] — graph-based code understanding as part of the agent tool chain

## Repo

https://github.com/AIOS-Agent/Code-as-Agent-Harness
