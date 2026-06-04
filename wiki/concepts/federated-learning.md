---
created: 2026-05-29
updated: 2026-05-29
type: concept
summary: Federated learning — machine learning on decentralized data without raw data centralization
tags: [privacy, distributed-systems, machine-learning]
sources: 
status: stub
confidence: 0.3
---

# Federated Learning

Federated learning trains machine learning models on decentralized data without the data leaving its original location. The standard approach:

1. Initialize global model at central server
2. Distribute model to participating clients
3. Clients train locally on their private data
4. Clients send model updates (not data) to server
5. Server aggregates updates (e.g., FedAvg)
6. Repeat

Variants include:
- **Horizontal federated learning** — same features, different samples
- **Vertical federated learning** — same samples, different features
- **Federated transfer learning** — transfer learning across domains

## Connections
- [[wiki/index]]
- [[concepts/federated-learning]]
- [[concepts/privacy-utility-tradeoff]]
- [[log]]
- [[concepts/data-privacy]]
- [[concepts/federated-learning]]

- [[data-privacy]] — privacy as the motivation
- [[privacy-utility-tradeoff]] — tradeoff in federated systems
- [[agem]] — where federated learning techniques apply
