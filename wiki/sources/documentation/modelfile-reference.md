
---
created: 2026-05-29
updated: 2026-05-30
type: source
summary: "Ollama Modelfile reference: FROM, PARAMETER, TEMPLATE, SYSTEM, ADAPTER, LICENSE, MESSAGE, REQUIRES instructions for creating customized models"
tags: [ollama,modelfile,llm-configuration,documentation]
sources: https://docs.ollama.com/modelfile
status: active
confidence: 1.0
---

# Modelfile Reference

**Source:** https://docs.ollama.com/modelfile | **Type:** Official documentation

## Instructions

| Instruction | Description |
|-------------|-------------|
| `FROM` (required) | Base model to use |
| `PARAMETER` | Parameters for how Ollama runs the model |
| `TEMPLATE` | Full prompt template sent to the model |
| `SYSTEM` | System message set in the template |
| `ADAPTER` | (Q)LoRA adapters to apply |
| `LICENSE` | Legal license |
| `MESSAGE` | Message history |
| `REQUIRES` | Minimum Ollama version required |

## Key Parameters

| Parameter | Description | Default |
|-----------|-------------|---------|
| `num_ctx` | Context window size (tokens) | 2048 |
| `repeat_last_n` | How far back to look to prevent repetition | 64 |
| `repeat_penalty` | Repetition penalty strength | 1.1 |
| `temperature` | Creativity vs coherence (higher = more creative) | 0.8 |
| `seed` | Random number seed (fixed = reproducible output) | 0 |
| `stop` | Stop sequences | — |
| `num_predict` | Maximum tokens to predict | -1 (infinite) |
| `top_k` | Vocabulary size for sampling | 40 |
| `top_p` | Nucleus sampling threshold | 0.9 |
| `min_p` | Minimum token probability relative to most likely | 0.0 |

## Supported Architectures

- Llama (2, 3, 3.1, 3.2)
- Mistral (1, 2, Mixtral)
- Gemma (1, 2)
- Phi3

## Template Variables

- `{{ .System }}` — system message
- `{{ .Prompt }}` — user prompt
- `{{ .Response }}` — model response (text after omitted during generation)

## Notes

- Modelfile is NOT case sensitive
- Instructions can be in any order
