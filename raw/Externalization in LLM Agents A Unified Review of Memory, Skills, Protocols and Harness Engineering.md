---
title: "Externalization in LLM Agents: A Unified Review of Memory, Skills, Protocols and Harness Engineering"
source: "https://www.alphaxiv.org/overview/2604.08224"
author:
  - "[[Chenyu Zhou]]"
  - "[[Huacan Chai]]"
  - "[[Wenteng Chen]]"
  - "[[Zihan Guo]]"
  - "[[Rong Shan]]"
  - "[[Yuanyi Song]]"
  - "[[Tianyi Xu]]"
  - "[[Yingxuan Yang]]"
  - "[[Aofan Yu]]"
  - "[[Weiming Zhang]]"
published: 2026-04-09
created: 2026-04-15
description: "Researchers propose \"externalization\" as a unifying principle explaining advancements in LLM agent reliability and capability, demonstrating how relocating"
tags:
  - "clippings"
---
## The Shift Toward Externalized Agency

Recent advancements in Large Language Model (LLM) agents have often been attributed to the scaling of model parameters or the refinement of internal reasoning capabilities. However, a growing body of research suggests that a significant portion of progress is derived from "externalization"—the deliberate relocation of cognitive burdens from the model's internal computation to structured, persistent, and inspectable external systems. This shift transforms the nature of the task for the model, moving from reliance on fragile internal memory and improvised generation to operating within a robust, designed environment.

![The comprehensive framework of externalization in LLM agents, illustrating the transition from internal weights to a structured external harness.](https://paper-assets.alphaxiv.org/figures-normalized/figures/2604.08224v1/x1.png "The comprehensive framework of externalization in LLM agents, illustrating the transition from internal weights to a structured external harness.")

This conceptual shift is grounded in the theory of "cognitive artifacts," which suggests that external tools do not merely augment an agent's internal abilities but fundamentally change the task itself. For an LLM agent, these artifacts include persistent memory stores, libraries of validated skills, and standardized communication protocols. When these components are integrated into a coherent runtime environment—termed the "harness"—the model no longer needs to solve every sub-problem through raw inference. Instead, it can rely on the harness to maintain state, provide procedural guidance, and ensure interoperability with external tools.

Formally, if an agent's action $a_t$ at time $t$ was previously a function of just the input $x_t$ and the model weights $\theta$, the externalization paradigm introduces a harness $H$ that provides structured context:

$$
a_t = \text{LLM}(x_t, M_t, S, P; \theta)
$$

Where $M_t$ represents the externalized memory state at time $t$, $S$ is the library of skills, and $P$ represents the interaction protocols.

## The Historical Trajectory: From Weights to Harness

The development of LLM agents can be categorized into three distinct evolutionary layers: the Weights Layer, the Context Layer, and the Harness Layer. Each layer represents a progressive movement of cognitive responsibility "outward" from the model core.

1. **Weights Layer ($W$):** Early efforts focused on embedding capabilities directly into the model parameters $\theta$ through pretraining and fine-tuning. While this creates a high-speed "system 1" intuition, it is expensive to update and suffers from knowledge staleness.
2. **Context Layer ($C$):** The introduction of prompt engineering and Retrieval-Augmented Generation (RAG) moved information into the ephemeral context window. This allows for in-context learning and access to dynamic data, but is limited by the finite size and "forgetting" behaviors of long contexts.
3. **Harness Layer ($H$):** Current state-of-the-art agents focus on the harness—a persistent infrastructure that exists outside individual sessions. This layer manages the lifecycle of memory, organizes skills, and enforces protocols, providing a stable "cognitive environment" that survives beyond a single model call.

![Evolutionary timeline of LLM agent research, highlighting the shift in focus from model weights to context management and finally to harness engineering.](https://paper-assets.alphaxiv.org/figures-normalized/figures/2604.08224v1/timeline.png "Evolutionary timeline of LLM agent research, highlighting the shift in focus from model weights to context management and finally to harness engineering.")

## Memory: Externalizing Temporal State

Memory systems address the "continuity problem"—the inability of base LLMs to maintain state across long horizons or multiple sessions. By externalizing state, the system converts the cognitive burden of perfect recall into a task of selective retrieval.

Memory content is typically categorized into four types:

- **Working Context ($M_{\text{working}}$):** The immediate state of the current task, including active variables and recent history.
- **Episodic Experience ($M_{\text{episodic}}$):** Traces of past runs, including successes and failures, which allow the agent to learn from its own history.
- **Semantic Knowledge ($M_{\text{semantic}}$):** Domain-specific facts and conventions that are too voluminous to fit in weights or prompts.
- **Personalized Memory:** User preferences and environmental nuances that dictate how tasks should be performed for a specific context.

![The architecture of externalized memory, showing the flow from ephemeral context to persistent, hierarchical storage systems.](https://paper-assets.alphaxiv.org/figures-normalized/figures/2604.08224v1/memory_f.png "The architecture of externalized memory, showing the flow from ephemeral context to persistent, hierarchical storage systems.")

Modern memory architectures have moved away from simple monolithic prompts toward "Operating System-style" memory management. This includes hierarchical storage (tiering information into "hot" context and "cold" vector databases) and adaptive retrieval strategies that dynamically decide which memories are relevant at time $t_i$. This organization ensures that the agent maintains a consistent identity and state across vast temporal gaps $\Delta t$.

## Skills: Externalizing Procedural Expertise

Skills address the "variance problem," where LLMs often fail to execute multi-step procedures consistently. By externalizing expertise into a skill library $S = \{s_1, s_2, \dots, s_n\}$, the harness provides the model with "packaged expertise" rather than requiring it to re-derive logic at every step.

A skill artifact $s_i$ typically encapsulates three components:

1. **Operational Procedures:** Structured workflows and step-by-step skeletons.
2. **Decision Heuristics:** Strategies for branching and handling edge cases.
3. **Normative Constraints:** Safety boundaries and compliance rules that must be followed during execution.

![The lifecycle of skill externalization, from acquisition and discovery to execution binding and runtime composition.](https://paper-assets.alphaxiv.org/figures-normalized/figures/2604.08224v1/skill_f.png "The lifecycle of skill externalization, from acquisition and discovery to execution binding and runtime composition.")

Skills are acquired through various pathways: they can be authored by human experts, distilled from past episodic memory, or autonomously discovered through environment interaction. Once externalized, the harness handles "progressive disclosure"—providing the agent with a high-level summary of available skills and only loading the full procedural detail when a specific skill is selected for execution. This significantly reduces the context burden on the model.

## Protocols: Standardizing Interaction Contracts

Protocols solve the "coordination problem," reducing the ambiguity inherent in free-form communication between agents, tools, and users. By externalizing interaction structures into machine-readable contracts $P$, the harness ensures that actions are interoperable and governed.

Protocols typically define:

- **Invocation Grammar:** The exact format and arguments required for a tool or service.
- **Lifecycle Semantics:** State transitions, such as "in-progress," "success," or "failed," which provide a clear signal for agent control flow.
- **Discovery Metadata:** Information that allows an agent to understand which tools are available and what they are capable of.

![Standardized interaction protocols enable consistent communication across agent-tool, agent-agent, and agent-user boundaries.](https://paper-assets.alphaxiv.org/figures-normalized/figures/2604.08224v1/protocol_f.png "Standardized interaction protocols enable consistent communication across agent-tool, agent-agent, and agent-user boundaries.")

Emerging standards like the Model Context Protocol (MCP) or Agent-to-Agent (A2A) protocols allow for a "decentralized agentic web," where different systems can collaborate without custom, hard-coded integrations. This externalization makes the agent's interaction with the world more predictable and easier to audit.

## Harness Engineering: Designing the Cognitive Environment

The "harness" is the integrative runtime that coordinates memory, skills, and protocols. Harness engineering is the discipline of designing this environment to minimize the cognitive load on the LLM core while maximizing the reliability of the system.

![Key dimensions of harness engineering, including control loops, sandboxing, observability, and permission management.](https://paper-assets.alphaxiv.org/figures-normalized/figures/2604.08224v1/x2.png "Key dimensions of harness engineering, including control loops, sandboxing, observability, and permission management.")

A well-engineered harness includes several critical dimensions:

- **Agent Loop and Control Flow:** Managing the "perceive-plan-act" cycle and enforcing termination conditions to prevent infinite loops.
- **Sandboxing:** Isolating tool execution to prevent side effects and simplify the model's operating environment.
- **Human Oversight:** Providing explicit "approval gates" where humans can intervene in the agent's decision-making process.
- **Observability:** Maintaining structured traces of all externalized interactions for debugging and feedback.
- **Context Budget Management:** Actively pruning and summarizing the information fed into the model's finite context window.

## The Dynamics of Unified Externalization

The three modules of externalization—memory, skills, and protocols—do not operate in isolation. They form a self-reinforcing cycle within the harness that drives agent evolution.

![The interconnected cycle of memory, skills, and protocols within the agent harness.](https://paper-assets.alphaxiv.org/figures-normalized/figures/2604.08224v1/circle.png "The interconnected cycle of memory, skills, and protocols within the agent harness.")

The interactions are deeply coupled:

- **Memory to Skill:** Successful episodic experiences can be distilled into new reusable skills.
- **Skill to Protocol:** Skill execution is bound to external tools through standardized protocols.
- **Protocol to Memory:** The results of external actions are assimilated back into memory to update the agent's state.

This unified structure creates a "distributed cognition" system where the intelligence of the agent is a property of the entire system (Weights + Harness) rather than just the neural network alone.

## Parametric vs. Externalized Capability: A Strategic Trade-off

One of the most important decisions for agent developers is determining whether a capability should remain "parametric" (inside model weights $\theta$) or be "externalized" into the harness $H$. This is governed by several trade-offs:

- **Update Frequency:** If information changes rapidly, it should be externalized (Memory/RAG).
- **Reliability vs. Latency:** Parametric execution is faster but prone to hallucination; externalized skills are more reliable but introduce retrieval and composition latency.
- **Governance and Safety:** High-stakes procedures should be externalized as explicit skills or protocols to allow for human auditing and hard constraints.
- **Complexity:** Simple, intuitive tasks are best handled by the model's internal weights, while multi-step, technical workflows benefit from external procedural guidance.

In conclusion, the evolution of LLM agents is moving away from the pursuit of a single "all-knowing" model and toward the engineering of sophisticated "cognitive environments." By systematically externalizing state, expertise, and interaction, we can build agents that are more consistent, more governable, and capable of operating over much longer horizons than a standalone model ever could. This shift redefines agency as a system-level property, where the "harness" is as critical to intelligence as the weights themselves.

Things That Make Us Smart: Defending Human Attributes in the Age of the Machine

This work provides the central theoretical foundation for the entire review paper. The authors explicitly frame their thesis of "externalization" around Norman's concept of cognitive artifacts, arguing that agent infrastructure transforms difficult cognitive tasks for the LLM, which is a recurring theme throughout the paper.

D. A. Norman. Things That Make Us Smart: Defending Human Attributes in the Age of the Machine. Addison-Wesley, Reading, MA, 1993.

Cognitive architectures for language agents

The review paper explicitly identifies this work on the CoALA framework as the "closest conceptual bridge" to its own. This citation is crucial for understanding the paper's context and its contribution to the idea of building structured cognitive systems around LLMs, rather than treating them as monolithic reasoners.

T. R. Sumers, S. Yao, K. Narasimhan, and T. L. Griffiths. Cognitive architectures for language agents. Transactions on Machine Learning Research, 2024. Published in TMLR; available at https://openreview.net/forum?id=1i6ZCvflQJ.

Retrieval-augmented generation for knowledge-intensive NLP tasks

This paper introduced Retrieval-Augmented Generation (RAG), which the review identifies as a foundational mechanism for the "Externalized State: Memory" pillar. The review frames RAG as the key architectural shift that converts an internal recall problem into an external retrieval problem, forming the basis for more advanced agent memory systems.

P. Lewis, E. Perez, A. Piktus, F. Petroni, V. Karpukhin, N. Goyal, H. Küttler, M. Lewis, W.-t. Yih, T. Rocktäschel, S. Riedel, and D. Kiela. Retrieval-augmented generation for knowledge-intensive NLP tasks. In Advances in Neural Information Processing Systems, volume 33, pages 9459–9474, 2020.

React: Synergizing reasoning and acting in language models

The ReAct framework is cited as a pivotal development that demonstrated how to interleave reasoning and action within the context window. This is fundamental to the review's concept of a "harness," as it provides the basis for the agent loops and control flows that coordinate externalized skills and memory.

S. Yao, J. Zhao, D. Yu, N. Du, I. Shafran, K. Narasimhan, and Y. Cao. React: Synergizing reasoning and acting in language models, 2023a. URL https://arxiv.org/abs/2210.03629.