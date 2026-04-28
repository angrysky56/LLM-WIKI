---
summary: Summary of Eidetic Learning: An Efficient and Provable Solution to Catastrophic Forgetting — solving catastrophic forgetting via structured pruning and disjoint subnetworks.
tags: [catastrophic-forgetting, continual-learning, pruning, machine-learning]
updated: 2026-04-28T20:26:19Z
created: 2026-04-28T20:26:19Z
---

---
title: "Eidetic Learning: An Efficient and Provable Solution to Catastrophic Forgetting"
type: source
status: ingested
tags: [catastrophic-forgetting, continual-learning, pruning, subnetworks, deep-learning, machine-learning]
source: "https://arxiv.org/abs/2106.01257"
---

# Eidetic Learning: An Efficient and Provable Solution to Catastrophic Forgetting

## Overview
This paper proposes **Eidetic Learning**, a method for training deep artificial neural networks (ANNs) on a sequence of tasks without suffering from **catastrophic forgetting**. The core idea is to use **structured pruning** to identify and isolate disjoint subnetworks for each task, providing provable guarantees that performance on previous tasks remains unchanged.

## Key Concepts
- **EideticNets**: Neural networks that use structured pruning to allocate dedicated capacity for specific tasks.
- **Structured Pruning**: Unlike weight-level pruning, this method prunes entire neurons (or channels in CNNs), which allows for efficient task separation and compatible integration with standard layers like Batch Normalization.
- **Provable Guarantees**: By freezing the subnetworks identified for task $t_i$, the network ensures that the output for $t_i$ is never altered by the training of subsequent tasks $t_{i+1}, \dots, t_n$.

## Architecture Support
The method is shown to be compatible with:
- **Linear Layers**: Standard feed-forward networks.
- **Convolutional Layers**: Structured pruning applied to channel dimensions.
- **Batch Normalization (BN)**: Task-specific statistics are preserved by freezing $\beta$ and $\gamma$ and maintaining task-specific running means ($\mu$) and variances ($\sigma$).
- **Residual Connections**: Handled by syncing masks across the residual block to maintain distribution stability.
- **Recurrent/LSTM Layers**: Theoretically compatible via sequential linear operations, though out of scope for the paper's main experiments.

## Results
- **Permuted MNIST**: Achieves near-perfect preservation across 10 tasks.
- **ResNet on Imagenette/CIFAR-100**: Successfully scales to modern architectures and complex datasets without performance degradation on early tasks.

## Connections to Synapse Framework
- **Knowledge Consolidation**: Provides a structural mechanism for how an agent can "remember" early foundational knowledge while learning new complex behaviors.
- **Structural Isomorphism**: The concept of dedicated subnetworks maps well to the idea of "Knowledge Modules" or specific functional regions in the Synapse graph.

---
**Location**: `Clippings/papers/2026/Eidetic Learning an Efficient and Provable Solution to Catastrophic Forgetting.md`
**Ingested**: 2026-04-28
