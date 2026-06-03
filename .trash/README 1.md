# Meta-Harness

![Meta-Harness](assets/repo.png)

Meta-Harness is a framework for automated search over task-specific model harnesses: the code around a fixed base model that decides what to store, retrieve, and show while the model works. This repo contains the framework and two reference experiments from the paper.

The paper is [Meta-Harness: End-to-End Optimization of Model Harnesses](https://arxiv.org/abs/2603.28052).

## Hermes Agent Integration

This fork replaces the original Claude Code proposer with **Hermes Agent** — an open-source AI agent framework by Nous Research. The evolution loop uses Hermes as the proposer engine, with support for:

- **Any LLM provider**: OpenRouter (default), Anthropic, Ollama (local), or custom endpoints
- **Model routing**: auto-detects from `~/.hermes/config.yaml`, overridable via env vars
- **Tool integration**: file read/write, terminal, delegation — no Claude CLI dependency

## Architecture

```
meta-harness/
├── run_evolution.py              ← unified entry point
├── src/meta_harness/             ← shared package (domain-agnostic)
│   ├── engine.py                 ← EvolutionEngine (Evaluator protocol)
│   ├── evaluator.py              ← Evaluator protocol
│   ├── wrapper.py                ← HermesWrapper (env-aware)
│   ├── text_classification_evaluator.py
│   └── __init__.py
├── reference_examples/
│   ├── text_classification/
│   │   ├── meta_harness.py       ← evolution loop (proven pipeline)
│   │   ├── hermes_wrapper.py     ← AIAgent integration
│   │   ├── benchmark.py          ← benchmark sweep
│   │   ├── data/                 ← datasets (USPTO, LawBench, Sentiment, ...)
│   │   ├── agents/               ← baseline + generated agents
│   │   ├── .claude/skills/       ← proposer skill instructions
│   │   └── config.yaml           ← datasets, models, splits
│   └── terminal_bench_2/         ← Terminal-Bench 2 reference
└── .env                           ← API keys (gitignored)
```
See [ARCHITECTURE.md](ARCHITECTURE.md) for a detailed breakdown of the framework components and code standards.

## MCP Server Ecosystem (EFHF)
| Server | Status | Role | Description |
| :--- | :--- | :--- | :--- |
| **project-synapse** | **Required** | Grounding | Wiki & Neo4j semantic indexing and knowledge retrieval. |
| **advanced-reasoning** | **Required** | Meta-Cognition | Meta-cognitive monitoring, confidence tracking, and hypothesis testing. |
| **hipai-montague** | Optional | World Model | Semantic cognition and world modeling using Montague grammar. |
| **mcp-logic** | Optional | Logic | Structural verification via theorem proving (Prover9/Mace4). |
| **seg-narrative** | Optional | Experiential | Narrative synthesis and experiential reasoning via Persona Councils. |
| **sheaf-consistency-enforcer** | Optional | Consistency | Multi-perspective consistency enforcement using Sheaf theory. |
| **conscience-servitor** | Optional | Ethics | Pre-response ethical triage and alignment enforcement. |
| **verifier-graph** | Optional | Verification | Formal graph-based verification of reasoning chains. |

The evolution loop in `text_classification` specifically verifies the presence of the **Required** servers to ensure grounding and meta-cognitive oversight. The optional servers provide extended capabilities for specific high-stakes research domains.

## Code Quality

This project maintains high code quality standards to ensure stable autonomous evolution:
- **Linting**: Clean under `ruff` (including built-in shadowing checks).
- **Types**: Full Python type hints with `mypy` validation.
- **Interface Stability**: The `MemorySystem` interface is standardized across agents.

## Quick Start

**Prerequisites:** Hermes Agent installed, Python >= 3.11, `uv`.

```bash
# 1. Install dependencies (single venv at repo root)
uv sync

# 2. Set up API key (for OpenRouter — add to .env, which is gitignored)
echo "OPENROUTER_API_KEY=sk-or-v1-..." > .env

# 3. Run evolution (1 iteration, fresh start)
uv run python run_evolution.py --domain text_classification --iterations 1 --fresh --skip-baseline
```

**Model selection:**

```bash
# Use default model from ~/.hermes/config.yaml (deepseek-v4-pro via OpenRouter)
uv run python run_evolution.py --domain text_classification --iterations 5

# Use a specific OpenRouter model
HERMES_PROPOSER_MODEL=google/gemini-2.5-flash uv run python run_evolution.py ...

# Use local Ollama model
HERMES_PROPOSER_MODEL=gemma4:31b \
HERMES_PROPOSER_PROVIDER=ollama \
HERMES_PROPOSER_BASE_URL=http://localhost:11434/v1 \
uv run python run_evolution.py ...
```

**Diagnostic dataset:** A 60-example sentiment dataset is included for fast iteration — edit `config.yaml` to switch between Sentiment and the full legal/medical datasets.

## Applying Meta-Harness To A New Domain

Start by pointing your coding assistant to [`ONBOARDING.md`](ONBOARDING.md) and having a conversation with it. This should produce a `domain_spec.md` file with concrete details on how to proceed.

The `src/meta_harness/evaluator.py` defines the Evaluator protocol — implement it for your domain, then add a branch in `run_evolution.py`. The existing `TextClassificationEvaluator` in `src/meta_harness/text_classification_evaluator.py` serves as a reference implementation.

## Citation

```bibtex
@misc{lee2026metaharnessendtoendoptimizationmodel,
      title={Meta-Harness: End-to-End Optimization of Model Harnesses},
      author={Yoonho Lee and Roshen Nair and Qizheng Zhang and Kangwook Lee and Omar Khattab and Chelsea Finn},
      year={2026},
      eprint={2603.28052},
      archivePrefix={arXiv},
      primaryClass={cs.AI},
      url={https://arxiv.org/abs/2603.28052},
}
```
