---
summary: Foundation model for tabular data using in-context learning. Trained on synthetic data, matches XGBoost on small-to-medium datasets. GPU recommended. Rich extension ecosystem.
tags: [tabular-data, foundation-model, in-context-learning, synthetic-data, priorlabs]
updated: 2026-05-10T03:42:05Z
created: 2026-05-10T03:42:05Z
---

# TabPFN

> **Source:** [PriorLabs/TabPFN](https://github.com/PriorLabs/TabPFN) — archived to [[Clippings/repositories/2026/PriorLabsTabPFN ⚡ TabPFN Foundation Model for Tabular Data ⚡]]

## What It Is

A foundation model for tabular data — treats structured/tabular prediction as an in-context learning problem rather than traditional gradient-based training. TabPFN-2.6 (current) is trained purely on synthetic data, yet matches or beats XGBoost/Random Forest on small-to-medium tabular benchmarks.

## Quick Start

```python
from tabpfn import TabPFNClassifier, TabPFNRegressor

clf = TabPFNClassifier()
clf.fit(X_train, y_train)  # downloads checkpoint on first use
predictions = clf.predict(X_test)
```

## Key Constraints

- **Dataset size:** Best under 100K samples, 2000 features. Beyond that, use extensions or subsample.
- **GPU recommended:** CPU only feasible for ≤1000 samples. Even older GPUs with ~8GB VRAM work; 16GB needed for large datasets.
- **No GPU?** Use [TabPFN Client](https://github.com/priorlabs/tabpfn-client) for free cloud inference.
- **No preprocessing:** Don't scale or one-hot encode — TabPFN handles it internally.

## Ecosystem

| Package | Purpose |
|---------|---------|
| [[tabpfn]] (this repo) | Core PyTorch + CUDA inference |
| [[tabpfn-client]] | Cloud API client (no GPU needed) |
| [[tabpfn-extensions]] | Interpretability (SHAP), unsupervised, embeddings, many-class, RF-PFN, HPO, post-hoc ensembles |

## Architecture & Design

- In-context learning over synthetic pre-training data
- Fits in a single forward pass (no gradient updates at inference)
- Batch prediction mode critical — 100× slower if you call `predict` per-sample
- KV cache available via `fit_mode='fit_with_cache'` for faster repeated prediction
- Model versions: TabPFN-2.5 and TabPFN-2.6 selectable via `ModelVersion`

## Extensions Deep Dive

- **Interpretability:** SHAP-based explanations, feature importance/selection
- **Unsupervised:** Outlier detection, synthetic data generation, data augmentation
- **Embeddings:** Extract internal learned representations for downstream tasks
- **Many-class:** Exceeds built-in class limit via decomposition
- **RF-PFN:** Hybrid ensembles with Random Forests
- **HPO:** Hyperparameter optimization tailored to TabPFN
- **Post-hoc ensembles:** Boost performance by combining multiple TabPFN fits

## Connections

- [[priorlabs]] — the company behind TabPFN
- [[huggingface]] — model hosting and checkpoints
- [[tabular-data]] — the problem domain
- [[in-context-learning]] — core mechanism
- [[synthetic-data]] — pre-training strategy
- [[random-forest]] — traditional baseline competitor
- [[xgboost]] — traditional baseline competitor
- [[shap]] — interpretability via SHAP values
