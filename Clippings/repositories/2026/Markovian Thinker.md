---
title: "Hugging Face"
source: "https://huggingface.co/McGill-NLP/delethink-24k-1.5b"
author:
published: 2025-02-10
created: 2026-05-11
description: "We’re on a journey to advance and democratize artificial intelligence through open source and open science."
tags:
  - "clippings"
---
[Edit model card](https://huggingface.co/McGill-NLP/delethink-24k-1.5b/edit/main/README.md)

## McGill-NLP/delethink-24k-1.5b

![](https://huggingface.co/McGill-NLP/delethink-24k-1.5b/resolve/main/method.png)

### TL;DR

- **Markovian Thinking** for RL in reasoning LLMs: replace the trivial MDP where state = prompt + all past thinking tokens (quadratic compute) with a bounded, fixed-size state, yielding **linear compute** in thinking tokens and constant memory by design.
- Delethink RL trains a model to “think” in **fixed-size chunks** with bounded state..
- This 1.5B model uses an effective **thinking budget of about 24K tokens** while only requiring an **8K active context** at any time via chunked rollouts and short carryovers.
- Initialized from **`deepseek-ai/DeepSeek-R1-Distill-Qwen-1.5B`**, trained with the Delethink RL paradigm. See the paper for full details.

### Links

- Repo: [https://github.com/McGill-NLP/the-markovian-thinker](https://github.com/McGill-NLP/the-markovian-thinker)
- Paper: [https://arxiv.org/abs/2510.06557v1](https://arxiv.org/abs/2510.06557v1)
- Collection: [The Markovian Thinker](https://huggingface.co/collections/McGill-NLP/the-markovian-thinker-68debd2919c4ae47f50706cd)

## Model Summary

- Base model: `deepseek-ai/DeepSeek-R1-Distill-Qwen-1.5B`
- Objective: Reinforcement Learning for long-form reasoning with bounded, chunked thinking (Delethink) trained for 1000 steps.
- **Delethink 24K budget**: uses 8K “context size” chunks, short “markovian” carryovers, and up to 5 chunk iterations for ~24K total thinking tokens.
- Intended use: Math/logic reasoning with step-by-step derivations; final answer typically formatted inside LaTeX `\boxed{}`.
- Library compatibility: Works well with SGLang for chunked inference; also usable with Transformers for standard generation (chunking requires manual orchestration; see paper for an example).

## Intended Uses and Limitations

- Intended uses:
	- Long-form reasoning on math and related tasks.
		- Bounded-context rollouts with repeated chunking and short carryovers.
- Not intended for:
	- Safety-sensitive applications without human oversight.
		- Use cases requiring faithful, verifiable citations to external sources.
- Limitations:
	- May hallucinate, make arithmetic/algebraic mistakes, or produce inconsistent plans.
		- The chunked rollout procedure is needed to realize Delethink’s efficiency advantages.

## How Delethink Works (Concept)

Let:

- C = context\_size per chunk (active KV memory)
- m = markovian\_size = number of tokens carried over to the next chunk
- I = iteration\_cap = maximum number of chunks

Effective thinking budget is:

- C + (I − 1) × (C − m)

For this checkpoint, we recommend:

- C = 8192
- m = 4096
- I ≤ 5 This yields an effective budget ≈ 8192 + 4 × (8192 − 4096) = 24576 tokens of thinking.

## Prompting

- Use the model’s chat template and request a step-by-step solution with a final boxed answer:
	- “Please reason step by step, and put your final answer within \\boxed{}.”

## Quickstart (SGLang, chunked Delethink rollout)

```python
import asyncio
import sglang as sgl

async def delethink_tracing(llm, query_ids, context_size=8192, markovian_size=4096, iteration_cap=5):
    sampling_params = {"temperature": 0.6}
    trace_response_ids = []
    iterations = 0
    prompt_ids = query_ids

    while iterations < iteration_cap:
        params = dict(sampling_params)
        params["max_new_tokens"] = (context_size - markovian_size) if iterations > 0 else context_size

        resp = await llm.async_generate(input_ids=prompt_ids, sampling_params=params, return_logprob=True)
        if "output_ids" in resp:
            out_ids = resp["output_ids"]
        else:
            _, out_ids = zip(*[(lp, tids) for lp, tids, _ in resp["meta_info"]["output_token_logprobs"]])
            out_ids = list(out_ids)

        trace_response_ids.append(out_ids)

        if iterations == 0:
            query_ids = query_ids + out_ids[:100]

        finish_reason_is_eos = resp["meta_info"]["finish_reason"]["type"] == "stop"
        if finish_reason_is_eos:
            break

        prompt_ids = query_ids + out_ids[-markovian_size:]
        iterations += 1

    return sum(trace_response_ids, [])

def main():
    llm = sgl.Engine(
        model_path="McGill-NLP/delethink-24k-1.5b",
        dtype="bfloat16",
        attention_backend="flashinfer",
        mem_fraction_static=0.8,
        log_level="WARNING",
    )

    prompt = (
        r"There exist real numbers $x$ and $y$, both greater than 1, such that "
        r"$\log_x\left(y^x\right)=\log_y\left(x^{4y}\right)=10$. Find $xy$."
        "\n\nPlease reason step by step, and put your final answer within \\boxed{}."
    )
    tok = llm.tokenizer_manager.tokenizer
    query_ids = tok.apply_chat_template(
        [{"role": "user", "content": prompt}],
        tokenize=True,
        add_generation_prompt=True,
    )

    ids = asyncio.run(delethink_tracing(llm, query_ids, context_size=8192, markovian_size=4096, iteration_cap=5))
    print(tok.decode(ids, skip_special_tokens=False))

if __name__ == "__main__":
    main()
```

### Suggested generation settings

- temperature: 0.6
- top\_p: 1.0
- top\_k: -1

## Safety and Use

- This model can produce incorrect or misleading reasoning steps and answers. Always verify results.
- Do not deploy in high-stakes domains without human oversight.

## Citation

```
@misc{Aghajohari2025:TheMarkovianThinker,
      title={The Markovian Thinker}, 
      author={Milad Aghajohari and Kamran Chitsaz and Amirhossein Kazemnejad and Sarath Chandar and Alessandro Sordoni and Aaron Courville and Siva Reddy},
      year={2025},
      eprint={2510.06557},
      archivePrefix={arXiv},
      primaryClass={cs.LG},
      url={https://arxiv.org/abs/2510.06557}, 
}
```

Downloads last month

17

Safetensors

Model size

2B params

Tensor type

F32

Inference Providers [NEW](https://huggingface.co/docs/inference-providers)

This model isn't deployed by any Inference Provider. [🙋 Ask for provider support](https://huggingface.co/spaces/huggingface/InferenceSupport/discussions/new?title=McGill-NLP/delethink-24k-1.5b&description=React%20to%20this%20comment%20with%20an%20emoji%20to%20vote%20for%20%5BMcGill-NLP%2Fdelethink-24k-1.5b%5D\(%2FMcGill-NLP%2Fdelethink-24k-1.5b\)%20to%20be%20supported%20by%20Inference%20Providers.%0A%0A\(optional\)%20Which%20providers%20are%20you%20interested%20in%3F%20\(Novita%2C%20Hyperbolic%2C%20Together%E2%80%A6\)%0A)

## Model tree for McGill-NLP/delethink-24k-1.5b

Base model

[deepseek-ai/DeepSeek-R1-Distill-Qwen-1.5B](https://huggingface.co/deepseek-ai/DeepSeek-R1-Distill-Qwen-1.5B)

Finetuned

([636](https://huggingface.co/models?other=base_model:finetune:deepseek-ai/DeepSeek-R1-Distill-Qwen-1.5B))

this model

Quantizations

[2 models](https://huggingface.co/models?other=base_model:quantized:McGill-NLP/delethink-24k-1.5b)

## Dataset used to train McGill-NLP/delethink-24k-1.5b

## Collection including McGill-NLP/delethink-24k-1.5b[Reformulating the RL of reasoning LLMs through Markovian Thinking paradigm. • 7 items • Updated • 11](https://huggingface.co/collections/McGill-NLP/the-markovian-thinker)

## Paper for McGill-NLP/delethink-24k-1.5b[Paper • 2510.06557 • Published • 33](https://huggingface.co/papers/2510.06557)