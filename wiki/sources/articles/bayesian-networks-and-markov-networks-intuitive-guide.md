---
summary: A comprehensive hands-on guide to probabilistic graphical models — covering Bayesian networks (DAGs, CPTs, junction tree inference) and Markov networks (undirected constraints, Markov logic), with full Python implementation and real-world applications to visual surveillance and medical diagnosis.
tags: [bayesian-networks, markov-networks, probabilistic-graphical-models, inference, belief-propagation, towards-data-science]
updated: 2026-06-11T12:49:38Z
created: 2026-06-11T12:49:38Z
---

Source: [Towards Data Science](https://towardsdatascience.com/bayesian-networks-and-markov-networks-an-intuitive-guide-to-structured-uncertainty/)

## Overview

A comprehensive, hands-on guide to probabilistic graphical models — covering Bayesian networks (directed) and Markov networks (undirected). The article builds intuition from first principles through a full Python toy implementation, then extends to real-world applications and the generative vs. discriminative distinction.

## Bayesian Networks (Directed)

- **Core idea**: Decompose the full joint distribution into local conditional dependencies encoded as a directed acyclic graph (DAG). Each node has a conditional probability table (CPT) given its parents.
- **Inference**: Sum over matching worlds — enumerate all variable assignments consistent with observed evidence.
- **Explaining away**: Evidence can support multiple explanations; observing one cause can reduce belief in another (inter-causal reasoning).
- **Use cases**: Visual surveillance (ontologies from low-level detections to high-level scenarios), medical diagnosis, any domain where causal structure is known.

## Practical Implementation

Full Python implementation covering:
1. Defining the network structure (Sprinkler/Rain/WetGrass example)
2. Computing probabilities by summing over matching worlds
3. Asking queries: marginal, conditional, and interventional
4. Smoothing for zero-count estimates from finite data

## Key Concepts

- **D-separation**: The graph encodes conditional independence — which variables stop mattering when others are observed.
- **Junction tree**: Converts the DAG into a tree of cliques for efficient belief propagation.
- **Three basic structures**: Chain, fork, and collider — each with different independence properties.

## Markov Networks (Undirected)

- **Core idea**: Undirected graph where edges represent constraints or affinities between variables, not causal direction.
- **Bayesian networks generate; Markov networks constrain**: BNs model generative processes; MNs model soft constraints via potential functions.
- **Markov logic**: First-order logic + Markov networks — weighted formulas as soft constraints.
- **Use cases**: Image segmentation, natural language processing, relational domains.

## Key Distinction

- **Generative models** (Bayesian networks): Model how data is generated. Good when causal structure is known.
- **Discriminative models**: Model decision boundaries directly. Often better for classification tasks.

## Connections

- [[probabilistic-graphical-models]]
- [[bayesian-networks]]
- [[markov-networks]]
- [[belief-propagation]]
- [[markov-logic]]
