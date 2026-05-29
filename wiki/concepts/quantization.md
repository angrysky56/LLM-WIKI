---
created: 2026-07-28
updated: 2026-07-28
type: concept
summary: Quantization — reducing model weight precision (e.g., 32-bit float to 4/8-bit integer) to decrease memory and compute costs
tags: [quantization, model-compression, llm-training, inference-efficiency]
sources: []
status: stub
confidence: 0.3
---

# Quantization

Quantization reduces the precision of neural network weights from high-precision formats (e.g., 32-bit floating point) to lower-precision formats (e.g., 8-bit or 4-bit integer). This reduces memory footprint and enables faster inference with acceptable quality degradation.

## Key Concepts

- **INT8/INT4 quantization**: Mapping 32-bit floats to 8-bit or 4-bit integers
- **Post-training quantization (PTQ)**: Quantizing a trained model without retraining
- **Quantization-aware training (QAT)**: Training with quantization constraints built in
- **QLoRA**: Combines 4-bit quantization with LoRA fine-tuning (Dettmers et al., 2023)

## Relationship to Other Concepts

See [[parameter-efficient-fine-tuning]] for how quantization combines with LoRA adapters.

## See Also
- [[concepts/parameter-efficient-fine-tuning]]
- [[concepts/qora]]
- [[log]]
- [[wiki/index]]
- [[concepts/quantization]]
- [[quantization]]

- [[llm-training]]: quantization is a key technique in LLM training efficiency
- [[parameter-efficient-fine-tuning]]: QLoRA combines quantization with PEFT
- [[qora]]