---
title: "Agentic Hardware Design as Repository-Level Code Evolution"
source: "https://www.alphaxiv.org/overview/2606.28279"
author:
  - "[[Brucek Khailany]]"
published: 2026-06-26
created: 2026-07-05
description: "The HORIZON framework, developed by Yu et al. at NVIDIA Research, models hardware design as repository-level code evolution, enabling autonomous agents to"
tags:
  - "clippings"
---
The design of modern hardware is an intricate process that demands extreme precision. Unlike general software, where a small bug might lead to a minor application crash, errors in hardware design can result in non-functional physical chips, costing millions of dollars in fabrication and months of lost time. Currently, large language models (LLMs) are being explored to automate the generation of Register-Transfer Level (RTL) code—the primary blueprint for hardware. However, single-turn generation often falls short because hardware correctness depends on cycle-level behavior, specific interface protocols, and strict timing constraints.

A new research paper from NVIDIA Research introduces **HORIZON**, a framework that treats hardware design not as a sequence of code generation prompts, but as a process of repository-level code evolution. By hosting hardware design tasks within version-controlled repositories, HORIZON allows autonomous agents to iteratively refine, simulate, and debug designs until they meet rigorous verification standards.

![HORIZON Framework Overview](https://paper-assets.alphaxiv.org/figures-normalized/figures/2606.28279v1/x1.png "HORIZON Framework Overview") *Figure 1: The HORIZON system architecture, showing the transition from a human-defined harness to an autonomous agent loop that evolves code within a Git repository based on executable feedback.*

## The Shift to Repository-Level Evolution

The fundamental insight behind HORIZON is that complex hardware design requires an environment where an agent can "live" and work over a long horizon. Previous efforts in automated RTL generation focused primarily on "Pass@1" metrics—the probability that the first attempt by an LLM is correct. While these models have improved through domain adaptation, they lack the ability to handle the multi-step verification and repair cycles that human engineers perform.

HORIZON draws inspiration from "self-evolving" software agents like AlphaEvolve and SATLUTION, which have successfully improved complex algorithmic repositories. This work extends that paradigm to hardware design artifacts themselves. In the HORIZON framework, every hardware design problem is managed as a standalone Git repository. This repository contains the source code, testbenches (the code used to test the design), and the entire evaluation infrastructure. By using Git as the substrate, the agent can branch, commit changes, and maintain a traceable history of its attempts, effectively turning the design process into an evolutionary trajectory guided by automated feedback.

## The HORIZON Framework and Project Pack

The process begins with a structured Markdown harness provided by a user. This harness details the high-level design objectives, domain knowledge, and the conditions for success. A "bootstrap agent" translates this harness into a `project_pack`, which serves as the control center for the autonomous loop.

The `project_pack` includes several critical components:

- $\pi_{\text{agent}}$: The agent's policy and tool contract.
- $E_p$: An executable evaluator, such as a simulator or synthesis tool, that provides objective feedback.
- $A_p$: An acceptance predicate—a hard "gate" that determines if a design is correct.
- $\Gamma_p$: The version-control and artifact policies.
- $\Omega_p$: Specific domain skills and repository instructions.

This structured approach ensures that the agent understands not just what to build, but how to test it and when to consider the mission complete.

## A Mathematical View of Agentic Evolution

To analyze the agent's behavior systematically, HORIZON formalizes the design process as a semi-Markov decision process. At any point in time $t$, the state $s_t$ of the design is defined by the entire context of the repository:

$$
s_t = (\text{tree}(w_t), p, z_t, \ell_{\leq t}, \mu_t)
$$

In this equation, $\text{tree}(w_t)$ represents the current state of the files in the Git worktree $w_t$, $p$ is the project pack, $z_t$ is the state of the overall design campaign, $\ell_{\leq t}$ are the accumulated logs, and $\mu_t$ is the agent's internal memory.

The agent takes an action $a_t$, which is defined as:

$$
a_t = (\Delta_t, u_{t, 1:K_t}, \rho_t)
$$

Here, $\Delta_t$ represents the specific changes (diffs) made to the code, $u_{t, 1:K_t}$ are the various tool calls (like running a simulator) performed during that iteration, and $\rho_t$ is the agent's final decision for that step. The evaluator $E_p$ then analyzes the new state:

$$
y_t = E_p(w_t + \Delta_t)
$$

The output $y_t$ provides the evidence needed for the acceptance gate $A_p$. If the gate passes, the change is committed to the repository, and the state advances to $s_{t+1}$. This rigorous formulation allows researchers to measure rewards $r_t$ in terms of improvements in pass rates ($\Delta \text{pass}$), verification coverage ($\Delta \text{coverage}$), or efficiency ($-\text{tokens}$).

## Performance Across Benchmarks

HORIZON was tested across a wide variety of RTL benchmark suites, including legacy datasets like Verilog-Eval and RTLLM-2.0, and more complex categories from the CVDP suite. The results demonstrate the power of iterative evolution: the framework achieved a 100% pass rate across nearly all suites in a fully "hands-free" mode.

![Pass Rate Progression](https://paper-assets.alphaxiv.org/figures-normalized/figures/2606.28279v1/x2.png "Pass Rate Progression") *Figure 2: Convergence trajectories for legacy RTL benchmarks. Most designs achieve 100% correctness within just two to five iterations.*

While simple designs converged almost immediately, more complex tasks required significant effort. For instance, in the CVDP categories, tasks like "checker generation" started with a near-zero success rate but climbed steadily to 100% over multiple iterations. One particularly difficult category, "code completion" (CID 002), required 82 iterations to reach full success. This highlight's HORIZON's ability to persist and debug through long-horizon problems that would be impossible for a single-turn generator.

![CVDP Convergence](https://paper-assets.alphaxiv.org/figures-normalized/figures/2606.28279v1/x3.png "CVDP Convergence") *Figure 3: Detailed convergence trajectories for various CVDP categories. The diversity in slopes shows that different hardware tasks present vastly different debugging challenges.*

## Efficiency and Token Consumption

A major consideration for agentic systems is the computational cost, often measured in the number of tokens processed by the LLM. The total campaign for the study consumed approximately 210 million tokens. Interestingly, the distribution of this consumption was highly skewed.

The "legacy" suites, which represent standard RTL generation tasks, consumed only 2.9% of the total tokens. In contrast, the most challenging CVDP categories accounted for over 97% of the total budget. The "code completion" task alone consumed 56 million tokens.

![Token Consumption Distribution](https://paper-assets.alphaxiv.org/figures-normalized/figures/2606.28279v1/x4.png "Token Consumption Distribution") *Figure 4: A pie chart showing token consumption across different tasks. A small number of difficult tasks consume the majority of the computational resources.*

To manage these costs, HORIZON uses persistent model sessions. This allows the system to cache the large "harness" and project pack data, meaning only the new code changes and simulator logs are billed as "new" tokens in each iteration. Approximately 91% of the tokens used in the study were cached, significantly reducing the actual cost of running the agent loop.

## Verification Quality and Coverage

In hardware design, "passing a test" is not always enough. A design might pass a specific testbench but still contain bugs in unexplored corners of its logic. To address this, HORIZON also tracks "coverage"—a metric that measures what percentage of the design's internal logic was actually exercised by the tests.

For tasks involving testbench stimulus generation (CID 012), HORIZON showed that as the pass rate increased, the average coverage also improved. However, because the agent was programmed to stop as soon as it met the benchmark's success criteria (the acceptance gate $A_p$), it did not always reach 100% coverage.

![Coverage vs Pass Rate](https://paper-assets.alphaxiv.org/figures-normalized/figures/2606.28279v1/x7.png "Coverage vs Pass Rate") *Figure 5: The relationship between pass rate and logic coverage for task CID 012. While the agent successfully passes the benchmark, there is often a "tail" of designs where coverage could be further optimized.*

This finding is significant because it suggests that the next phase of research in agentic hardware design should focus on maximizing verification quality rather than just achieving a binary "pass" signal.

## Significance and the Path Forward

HORIZON represents a move toward fully autonomous hardware engineering. By achieving 100% completion on existing benchmarks, it shifts the research focus from "Can an LLM write RTL?" to "How can we make agentic design more efficient and robust?"

Several key challenges remain:

1. **Convergence Efficiency:** While HORIZON can solve difficult problems, the "long tail" of iterations for complex tasks is expensive. Future work will likely focus on improving the agent's "reasoning" to reduce the number of iterations required.
2. **Verification Robustness:** As agents become better at "passing" benchmarks, there is a risk of "reward hacking"—where the agent finds a way to satisfy the specific tests in the harness without creating a truly robust design. Next-generation benchmarks will need hidden, randomized tests to ensure true correctness.
3. **Feedback Latency:** RTL simulation is relatively fast, but physical design steps like synthesis and routing can take hours or days. Developing agents that can reason through these slow feedback loops is essential for scaling to production-level chips.

By establishing a Git-native framework for repository-level evolution, HORIZON provides the infrastructure needed to tackle these problems, moving the field of EDA (Electronic Design Automation) closer to a future where hardware can be evolved as fluidly as software.

[Autonomous Code Evolution Meets NP-Completeness](https://www.alphaxiv.org/abs/2509.07367)

This paper, titled SATLUTION, is cited as a direct precursor to HORIZON from the same lead author. It established the principle of evolving an entire software repository (a SAT-solver) using an agentic loop, which HORIZON directly extends from the domain of software to hardware design artifacts.

Cunxi Yu, Rongjian Liang, Chia-Tung Ho, and Haoxing Ren. Autonomous Code Evolution Meets NP-Completeness. arXiv preprint arXiv:2509.07367, 2025.

[Autonomous Evolution of EDA Tools: Multi-Agent Self-Evolved ABC](https://www.alphaxiv.org/abs/2604.15082)

Titled ABCEvo, this is another critical precursor from the same authors that applied the repository-level self-evolution concept specifically to EDA software. This work represents the immediate conceptual step before HORIZON, bridging the gap from general software evolution to the chip design domain by evolving the tools engineers use.

Cunxi Yu, Rongjian Liang, Chia-Tung Ho, and Haoxing Ren. Autonomous Evolution of EDA Tools: Multi-Agent Self-Evolved ABC. arXiv preprint arXiv:2604.15082, 2026.

[Comprehensive Verilog Design Problems: A Next-Generation Benchmark Dataset for Evaluating Large Language Models and Agents on RTL Design and Verification](https://www.alphaxiv.org/abs/2506.14074)

This paper introduces the CVDP benchmark, which is the most significant and challenging benchmark suite used to evaluate the HORIZON framework. The authors emphasize that CVDP's breadth and inclusion of agentic tasks make it a strong fit for testing their system, and the paper's main results are centered on achieving 100% completion on its categories.

Nathaniel Pinckney, Chenhui Deng, Chia-Tung Ho, Yun-Da Tsai, Mingjie Liu, Wenfei Zhou, Brucek Khailany, and Haoxing Ren. Comprehensive Verilog Design Problems: A Next-Generation Benchmark Dataset for Evaluating Large Language Models and Agents on RTL Design and Verification. arXiv preprint arXiv:2506.14074, 2025.

[AlphaEvolve: A coding agent for scientific and algorithmic discovery](https://www.alphaxiv.org/abs/2506.13131)

This paper is cited as the foundational work for the entire paradigm of self-evolving agents over code repositories. It introduced the core concept of coupling an LLM with automated evaluators in an evolutionary loop, which the HORIZON paper and its direct precursors (SATLUTION, ABCEvo) adopt and extend.

Alexander Novikov, Ngân V˜u, Marvin Eisenberger, Emilien Dupont, Po-Sen Huang, et al. AlphaEvolve: A Coding Agent for Scientific and Algorithmic Discovery. arXiv preprint arXiv:2506.13131, 2025.