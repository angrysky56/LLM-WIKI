---
created: 2026-06-03
updated: 2026-06-09
type: concept
summary: Monte Carlo Tree Search — tree search algorithm using random simulation and backpropagation for decision-making in complex, non-trivial game trees and planning problems
tags: [search-algorithms, game-playing, planning, reinforcement-learning, alphazero]
sources: https://www.sciencedirect.com/science/article/pii/S0004370207002662 (MCTS survey)
status: active
confidence: 0.9
---

# Monte Carlo Tree Search

**Also known as:** MCTS, UCT (Upper Confidence Bounds for Trees)

## What It Is

Monte Carlo Tree Search is a best-first search algorithm for decision processes, combining tree search with random simulation (rollouts). It builds a search tree incrementally, balancing exploration (trying new nodes) with exploitation (following promising paths).

The algorithm maintains a tree where each node represents a game state. For each node it tracks:
- **Visit count**: How many times this node was visited
- **Win count**: How many rollouts through this node resulted in a win

The key innovation is **UCB1** (Upper Confidence Bound for trees), which balances:

```
UCB1 = Q(s,a) / N(s,a) + c * sqrt(ln(N(s,a_parent)) / N(s,a))
```

Where c is the exploration constant. The first term exploits (high win rate), the second explores (low visit count).

## The MCTS Loop

At each step:
1. **Selection**: Traverse the tree from root, selecting children by UCB1 until reaching an unexpanded node
2. **Expansion**: Add one or more child nodes
3. **Simulation (Rollout)**: Play out the game randomly from the new node to a terminal state
4. **Backpropagation**: Update visit/win counts up the path

The process repeats for as many simulations as time allows.

## Why It Matters

MCTS enabled a qualitative leap in game-playing AI:

| Game | MCTS Impact |
|------|-------------|
| **Go** | AlphaGo (2016) combined MCTS with deep learning; defeated Lee Sedol |
| **Chess** | AlphaZero (2017) used self-play + MCTS from scratch, outperforming Stockfish |
| **Shogi** | AlphaZero mastered shogi with the same approach |
| **Poker** | Pluribus (2019) used constrained MCTS for imperfect-information games |

MCTS is particularly valuable when:
- The game tree is too large for exhaustive search
- No good heuristic evaluation function exists (the simulation/rollout provides the signal)
- Self-play training is possible (no human data needed)

## AlphaZero Architecture

AlphaZero used MCTS with deep neural networks:
- **NN evaluates** leaf nodes instead of random rollouts (policy + value head)
- **NN guides** selection using the policy head to prioritize promising actions
- Self-play generates training data: each game produces (state, π, z) triples where π is the MCTS visit distribution

This is the foundation for the RL + MCTS combination used in modern reasoning systems (SD-Search, Process Reward Models).

## Connections
- [[concepts/mcts]]
- [[scratchpad/jobs/reports/researcher/discovery-2026-06-09]]
- [[concepts/causal-reasoning]]
- [[wiki/index]]
- [[concepts/collm-nas]]
- [[log]]
- [[sources/papers/deltabox-stateful-agent-checkpoint-rollback-2026]]
- [[concepts/code-generation]]
- [[concepts/swe-bench]]
- [[concepts/process-reward-model]]
- [[concepts/world-model]]
- [[concepts/agentic-hierarchy]]
- [[mcts]]

- [[process-reward-model]] — SD-Search uses MCTS-like search over reasoning steps, guided by a process reward model
- [[swe-bench]] — MCTS-like search has been explored for code agent task decomposition
- [[agentic-hierarchy]] — MCTS as a planning primitive in hierarchical agent architectures
- [[causal-reasoning]] — MCTS can be viewed as causal search over a decision tree (counterfactual: "what if I chose a different action?")
- [[world-model]] — MCTS requires a world model to simulate outcomes from a node
- [[code-generation]] — MCTS for generating code by exploring the program space (AlphaCode-style)