---
title: FlashAttention: Fast and Memory-Efficient Exact Attention with IO-Awareness
source: https://arxiv.org/abs/2205.14135
created: 2026-06-05T20:08:17Z
tags: [clippings]
---

## Title:FlashAttention: Fast and Memory-Efficient Exact Attention with IO-Awareness

Authors:[Tri Dao](https://arxiv.org/search/cs?searchtype=author&query=Dao,+T), [Daniel Y. Fu](https://arxiv.org/search/cs?searchtype=author&query=Fu,+D+Y), [Stefano Ermon](https://arxiv.org/search/cs?searchtype=author&query=Ermon,+S), [Atri Rudra](https://arxiv.org/search/cs?searchtype=author&query=Rudra,+A), [Christopher Ré](https://arxiv.org/search/cs?searchtype=author&query=R%C3%A9,+C)

[View PDF](https://arxiv.org/pdf/2205.14135)

> Abstract:Transformers are slow and memory-hungry on long sequences, since the time and memory complexity of self-attention are quadratic in sequence length. Approximate attention methods have attempted to address this problem by trading off model quality to reduce the compute complexity, but often do not achieve wall-clock speedup. We argue that a missing principle is making attention algorithms IO-aware -- accounting for reads and writes between levels of GPU memory. We propose FlashAttention, an IO-aware exact attention algorithm that uses tiling to reduce the number of memory reads/writes between GPU high bandwidth memory (HBM) and GPU on-chip SRAM. We analyze the IO complexity of FlashAttention, showing that it requires fewer HBM accesses than standard attention, and is optimal for a range of SRAM sizes. We also extend FlashAttention to block-sparse attention, yielding an approximate attention algorithm that is faster than any existing approximate attention method. FlashAttention trains Transformers faster than existing baselines: 15% end-to-end wall-clock speedup on BERT-large (seq. length 512) compared to the MLPerf 1.1 training speed record, 3 $\times$ speedup on GPT-2 (seq. length 1K), and 2.4 $\times$ speedup on long-range arena (seq. length 1K-4K). FlashAttention and block-sparse FlashAttention enable longer context in Transformers, yielding higher quality models (0.7 better perplexity on GPT-2 and 6.4 points of lift on long-document classification) and entirely new capabilities: the first Transformers to achieve better-than-chance performance on the Path-X challenge (seq. length 16K, 61.4% accuracy) and Path-256 (seq. length 64K, 63.1% accuracy).

| Subjects: | Machine Learning (cs.LG) |
| --- | --- |
| Cite as: | [arXiv:2205.14135](https://arxiv.org/abs/2205.14135) \[cs.LG\] |
|  | (or [arXiv:2205.14135v2](https://arxiv.org/abs/2205.14135v2) \[cs.LG\] for this version) |
|  | [https://doi.org/10.48550/arXiv.2205.14135](https://doi.org/10.48550/arXiv.2205.14135) |

## Submission history

From: Tri Dao \[[view email](https://arxiv.org/show-email/00d4bef1/2205.14135)\]  
**[\[v1\]](https://arxiv.org/abs/2205.14135v1)** Fri, 27 May 2022 17:53:09 UTC (1,325 KB)  
**\[v2\]** Thu, 23 Jun 2022 17:53:32 UTC (1,653 KB)  

[Which authors of this paper are endorsers?](https://arxiv.org/auth/show-endorsers/2205.14135) | Disable MathJax ([What is MathJax?](https://info.arxiv.org/help/mathjax.html))