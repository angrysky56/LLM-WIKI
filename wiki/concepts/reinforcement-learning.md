---
summary: Reinforcement learning — training agents via reward signals through environment interaction
tags: [reinforcement-learning, machine-learning, agent-training, rlhf, policy-gradient, mcts]
updated: 2026-05-28T01:21:37Z
---

---
created: 2026-05-25
updated: 2026-08-18
type: concept
summary: "Reinforcement learning — training agents via reward signals through environment interaction"
tags: [reinforcement-learning, machine-learning, agent-training, rlhf, policy-gradient, mcts]
sources: https://people.idsia.ch//kumar/Papers/rlhandbook2022.pdf
status: active
confidence: 0.7
---

# Reinforcement Learning

Reinforcement learning (RL) is a training paradigm where an agent learns to maximize cumulative reward by interacting with an environment. Unlike supervised learning, RL does not have labeled examples — the agent discovers good behavior through trial and error, with reward signals providing feedback rather than correct answers.

## Core Framework

An RL problem is formalized as a **Markov Decision Process (MDP)**: a tuple (S, A, P, R, γ) where:
- **S** — state space
- **A** — action space
- **P(s'|s,a)** — transition probability
- **R(s,a)** — reward function
- **γ** — discount factor

The agent learns a **policy** π(a|s) that maps states to actions, optimized to maximize expected cumulative discounted reward E[Σγ^t R(s_t, a_t)].

## Key Algorithms

### Value-Based
- **Q-Learning** — learns action-value function Q(s,a), policy is implicit (greedy on Q)
- **DQN** — Q-learning with experience replay and target networks for stability

### Policy Gradient
- **REINFORCE** — Monte Carlo estimate of policy gradient
- **PPO (Proximal Policy Optimization)** — clipped surrogate objective for stable updates; current standard for LLM alignment (RLHF)
- **TRPO** — trust region methods; PPO's predecessor

### Model-Based
- **World models** — learn a transition model of the environment
- **MCTS** (Monte Carlo Tree Search) —规划 without full environment model; used inAlphaGo and reasoning systems

## RL in the LLM Context

RL has become central to LLM development in two distinct roles:

### 1. RLHF — LLM Alignment
Reinforcement Learning from Human Feedback uses a learned reward model to provide training signal for LLM fine-tuning, typically via PPO. This is what makes models like GPT-4 and Claude obedient and helpful. The reward model is trained on human preference comparisons, then PPO uses it as the training target.

The key failure mode here is [[reward-hacking]] — the agent finds ways to maximize the reward model without actually accomplishing the intended task.

### 2. Test-Time Scaling / Inference
Best-of-N and similar approaches use reward models at inference time: generate N candidate responses, score each with the reward model, return the highest-scoring. This is RL without Weight Updates — test-time compute scaling through environmental sampling.

### 3. Process Reward Models
Unlike outcome reward (scored at final output), process rewards are assigned at intermediate reasoning steps. Combined with Monte Carlo Tree Search or beam search, this enables strategic reasoning rather than pure output selection. [[mop-next-token-prediction]] provides an entropy-based alternative to RL-style reward signals for hidden-state reasoning.

## Connections

- [[reward-modeling]] — the technique that trained a separate model to score LLM outputs for RLHF
- [[reward-hacking]] — the principal failure mode when learned reward models become targets
- [[reinforcement-learning-from-human-feedback]] — RLHF is RL applied at scale to LLM alignment
- [[autonomous-agents]] — RL is a core training paradigm for developing agent behaviors
- [[bounded-rationality]] — RL agents must contend with bounded exploration resources just as humans do
- [[exploration]] and [[exploitation]] — the fundamental tradeoff in RL exploration (epsilon greedy, UCB, curiosity-driven)
- [[group-relative-policy-optimization]] — GRPO, a PPO variant that normalizes rewards relative to a group baseline; used in DeepSeek-R1

## Open Questions

1. **MoE compatibility**: Do current RLHF methods (PPO/GRPO) work well when different experts are active for different inputs? Gradient signal conflicts at the shared output layer.
2. **Process vs outcome reward accuracy**: Process rewards are more sample-efficient but harder to label accurately — can supervised approaches to process reward learning match outcome reward scaling curves?
3. **Credit assignment latencies**: In long-horizon tasks, reward signals arrive hundreds of tokens after the decisions that caused them — how do underlying attention mechanisms propagate delayed gradients?
