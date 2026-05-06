---
title: "Titans: Learning to Memorize at Test Time"
source: "https://www.alphaxiv.org/overview/2501.00663"
author:
  - "[[Ali Behrouz]]"
  - "[[Peilin Zhong]]"
  - "[[Vahab Mirrokni]]"
published: 2024-12-31
created: 2026-05-03
description: "Titans introduces a new neural memory module that learns to memorize information at test time and effectively combines with attention mechanisms for better"
tags:
  - "clippings"
---
## Introduction

Sequence modeling tasks present a fundamental challenge in machine learning: how can models effectively process and retain information from very long input sequences? Traditional Transformer models, while powerful, struggle with long contexts due to their quadratic computational complexity. Linear recurrent models offer better efficiency but often sacrifice performance, particularly for extremely long contexts.

The research paper "Titans: Learning to Memorize at Test Time" by Ali Behrouz, Peilin Zhong, and Vahab Mirrokni from Google Research introduces a novel solution to this challenge. Titans represents an innovative family of architectures that combines the strengths of attention-based models with a neural long-term memory module capable of learning to memorize important information at test time.

![Memory Types in Titans](https://paper-assets.alphaxiv.org/figures/2501.00663/MAC.png "Memory Types in Titans") *Figure 1: Visualization of different memory types in the Titans architecture. The model progressively enhances its memory capabilities by adding long-term memory and persistent memory components to the standard short-term memory.*

The key innovation of Titans lies in its three distinct memory components, inspired by human cognition: short-term memory (attention), a neural long-term memory, and persistent memory (learnable parameters). By effectively combining these components, Titans achieves remarkable performance on long-context tasks while maintaining computational efficiency.

## Background and Context

Current approaches to sequence modeling broadly fall into two categories:

1. **Transformer Models**: These use self-attention mechanisms to model dependencies between all elements in a sequence. While Transformers excel at capturing complex relationships, they suffer from quadratic complexity in terms of sequence length, making them impractical for very long contexts.
2. **Linear Recurrent Models**: Models like Linear Transformers, Mamba, and RetNet process sequences with linear complexity by using recurrence mechanisms. However, they often struggle to match the performance of full attention models on complex tasks.

The concept of augmenting neural networks with memory components isn't new – previous works like Neural Turing Machines, Memory Networks, and Hopfield Networks have explored this idea. However, these approaches typically focus on fixed memory representations or require extensive pre-training.

What distinguishes Titans is its ability to learn to memorize information at test time through its neural long-term memory module. This dynamic memorization process allows the model to adaptively retain important information while processing long sequences, addressing a key limitation of existing architectures.

## The Memory-Inspired Architecture

The Titans architecture draws inspiration from how human memory works, incorporating three distinct types of memory:

1. **Short-term Memory**: Implemented as an attention mechanism that focuses on local context within a limited window.
2. **Long-term Memory**: A neural network that learns to memorize information dynamically during inference. This component stores information in its parameters through continuous updates.
3. **Persistent Memory**: Fixed, learnable, data-independent parameters that store general knowledge acquired during training.

The integration of these memory components allows Titans to maintain information over very long contexts more effectively than traditional models. As shown in Figure 1, this approach creates a more comprehensive memory system that can identify and preserve important information from the input sequence.

## Neural Long-Term Memory Design

The neural long-term memory module is the core innovation of Titans. It functions as a meta in-context learner that memorizes significant information from the input sequence directly into its parameters. The design incorporates several key components:

### Surprise-Based Memorization

Inspired by how humans remember surprising events more vividly, the module uses a "surprise" metric to prioritize information:

```
surprise(x_t) = ∇_θ L(f_θ(x_t), y_t)
```

Where ∇\_θ L represents the gradient of the loss with respect to the model parameters. This metric identifies which elements of the input sequence contain important information worth memorizing.

### Memory Decay Mechanism

To prevent memory saturation when processing very long sequences, Titans implements a decaying mechanism:

```
θ_t = θ_{t-1} - η · Θ_b B_b(W_0 X - f_θ(X))X^T
```

Where:

- θ\_t represents the parameters at time t
- η is the learning rate
- Θ\_b and B\_b are weight decay terms
- W\_0 is the initial parameter state

This decaying mechanism is a generalization of forgetting mechanisms in modern recurrent models, allowing the memory to adaptively forget less important information when necessary.

### Parallelized Training

The memory module is trained using tensorized mini-batch gradient descent, which allows for more efficient computation through matrix operations:

```
θ_t = θ_{t-1} - η · (W_0 X - f_θ(X))X^T
```

This approach enables fast and parallelizable updates to the memory parameters, as illustrated in Figure 8:

![Parallelization Techniques](https://paper-assets.alphaxiv.org/figures/2501.00663/Parallelization.png "Parallelization Techniques") *Figure 2: Parallelization techniques for neural memory training, showing linear within-chunk computations, non-linear cross-chunk processing, momentum calculation, and weight decay implementation.*

## Titans Architecture Variants

Titans introduces three distinct architectural variants, each incorporating the neural long-term memory in a different way:

### Memory as a Context (MAC)

In the MAC variant, the memory module's output is concatenated with the input sequence as additional context. This approach allows the attention mechanism to directly access both the input and the memorized information:

![MAC Architecture](https://paper-assets.alphaxiv.org/figures/2501.00663/MAL.png "MAC Architecture") *Figure 3: Memory as a Layer (MAL) architecture, showing the core processing path, neural memory module, and persistent memory components.*

### Memory as a Layer (MAL)

The MAL variant positions the memory module as a layer in the model, processing the input before it reaches the attention mechanism. This creates a hierarchical processing flow where the memory extracts and retains key information before the attention mechanism processes the sequence.

### Memory as a Gate (MAG)

In the MAG variant, the memory module's output is combined with the core branch using a gating mechanism. This allows the model to dynamically control how much information from the memory influences the final output:

![MAG Architecture](https://paper-assets.alphaxiv.org/figures/2501.00663/gate-arch.png "MAG Architecture") *Figure 4: Memory as a Gate (MAG) architecture, showing how the neural memory's output is combined with the attention output through a gating mechanism.*

Each variant has its strengths, with MAC showing superior performance on tasks requiring longer-term dependencies, while MAL and MAG offer more efficient processing for certain applications.

## Experimental Results

The Titans architectures were evaluated on a variety of sequence modeling tasks, with impressive results:

### Long-Context Performance

On needle-in-haystack tasks designed to test long-term memory capabilities, Titans significantly outperformed both standard Transformers and linear recurrent models:

![Long-Term Memory Performance](https://paper-assets.alphaxiv.org/figures/2501.00663/BABILong-FT.png "Long-Term Memory Performance") *Figure 5: Performance comparison on the bAbI Long task, showing Titans (MAC) maintaining high accuracy even at sequence lengths of 10^6 tokens, while other models' performance degrades.*

The results show Titans (MAC) maintaining 70% accuracy even at sequence lengths of 10^7 tokens, while state-of-the-art models like GPT-4 and Mamba drop below 40% accuracy at much shorter lengths.

### Few-Shot Learning Capabilities

Titans also demonstrated superior few-shot learning abilities, maintaining higher accuracy across increasing sequence lengths compared to other models:

![Few-Shot Learning Performance](https://paper-assets.alphaxiv.org/figures/2501.00663/BABILong-few-shot.png "Few-Shot Learning Performance") *Figure 6: Few-shot learning performance, showing Titans (MAC) consistently outperforming other models as sequence length increases.*

This indicates that the neural long-term memory effectively captures and uses information from previous examples, even without extensive fine-tuning.

## Deep Memory Analysis

The research included a detailed analysis of how the depth of the neural memory network affects performance. Results showed that deeper memory networks (with multiple layers) consistently outperformed linear memory:

![Deep Memory Performance 1](https://paper-assets.alphaxiv.org/figures/2501.00663/deep-memory-1.png "Deep Memory Performance 1") ![Deep Memory Performance 2](https://paper-assets.alphaxiv.org/figures/2501.00663/deep-memory-2.png "Deep Memory Performance 2") ![Deep Memory Performance 3](https://paper-assets.alphaxiv.org/figures/2501.00663/deep-memory-3.png "Deep Memory Performance 3") *Figures 7-9: Comparison of perplexity scores for different memory depths (LMM) versus Mamba across various sequence lengths, showing deeper memories consistently achieving lower perplexity.*

The experiments showed that deeper memory networks (L\_M = 3 or L\_M = 4) achieved lower perplexity scores than shallower networks, particularly for longer sequences. This suggests that the capacity for complex, non-linear memorization improves the model's ability to retain and use information from the input sequence.

Importantly, this improved performance does not come at a significant computational cost, as shown in Figure 10:

![Memory Efficiency](https://paper-assets.alphaxiv.org/figures/2501.00663/deep-memory-efficiency.png "Memory Efficiency") *Figure 10: Computational efficiency (tokens processed per second) for different memory depths across sequence lengths, showing that deeper memories maintain reasonable efficiency.*

## Efficiency Considerations

Beyond accuracy, the research examined the computational efficiency of Titans compared to other sequence models:

![Efficiency Comparison](https://paper-assets.alphaxiv.org/figures/2501.00663/efficiency.png "Efficiency Comparison") *Figure 11: Processing efficiency comparison of Titans variants against Transformer++ and other recurrent models, showing competitive performance with linear scaling.*

While standard Transformers (Transformer++) show a significant decrease in processing speed as sequence length increases, all Titans variants maintain nearly constant throughput. This linear scaling behavior makes Titans suitable for processing very long sequences efficiently.

The efficiency comes from two key factors:

1. The use of attention only within limited windows
2. The neural memory's ability to condense important information from the entire sequence into a compact representation

## Conclusion and Implications

The Titans architecture represents a significant advancement in sequence modeling by addressing the key limitations of both Transformers and linear recurrent models. By introducing a neural long-term memory module that learns to memorize at test time, Titans achieves both high accuracy on long-context tasks and computational efficiency.

Key contributions and implications of this research include:

1. **A new paradigm for memory in neural networks**: Titans demonstrates how distinct memory components inspired by human cognition can work together to process information more effectively.
2. **Solution to the context length limitation**: By achieving strong performance on sequences with millions of tokens, Titans opens possibilities for applications requiring extremely long contexts, such as document analysis, genomics, and extended conversations.
3. **Efficient in-context learning**: The ability to memorize important information at test time provides a form of efficient in-context learning without requiring extensive parameter updates.
4. **Generalizable architecture**: The three variants of Titans (MAC, MAL, MAG) offer flexibility for different applications, with trade-offs between performance and efficiency.

The success of Titans suggests a promising direction for future model development, where specialized memory components augment traditional attention mechanisms to create more capable and efficient sequence models. This approach could influence the design of next-generation large language models and other sequence processing systems, allowing them to handle longer contexts while using computational resources more efficiently.

## Relevant Citations

Vaswani et al. 2017. [Attention Is All You Need](https://alphaxiv.org/abs/1706.03762). Advances in Neural Information Processing Systems.

- This citation is highly relevant as it introduces the Transformer model, which is the foundation of modern attention-based models and the primary architecture that Titans aim to improve upon. The paper discusses the limitations of Transformers, particularly the quadratic cost with respect to context length, which motivates the development of Titans.

Katharopoulos et al. 2020. Transformers are rnns: Fast autoregressive transformers with linear attention. International conference on machine learning.

- This citation introduces linear Transformers, a more efficient alternative to standard Transformers. The paper shows the connection between linear attention and recurrent networks. As Titans aim to address the limitations of both Transformers and recurrent models, understanding the connection between the two is crucial.

S. Yang, B. Wang, Shen, et al. 2024. [Gated Linear Attention Transformers with Hardware-Efficient Training](https://alphaxiv.org/abs/2312.06635). Forty-first International Conference on Machine Learning.

- This citation describes Gated Linear Attention (GLA), an efficient attention mechanism used as a baseline for comparison with Titans. The paper focuses on the importance of gating mechanisms in linear attention models, which is a design element also incorporated into Titans' memory module for efficient memory management.

Dao and Gu 2024. Transformers are SSMs: Generalized models and efficient algorithms through structured state space duality. arXiv preprint arXiv:2405.21060.

- This citation establishes a connection between Transformers and State Space Models (SSMs), offering a different perspective on sequence modeling. This connection is relevant because Titans incorporate elements of both recurrent models (related to SSMs) and attention, and this paper helps bridge the gap between the two paradigms.

S. Yang, Kautz, and Hatamizadeh 2024. [Gated Delta Networks: Improving Mamba2 with Delta Rule](https://alphaxiv.org/abs/2412.06464). arXiv preprint arXiv:2412.06464.

- This citation is important because it discusses Gated Delta Networks, another advanced recurrent model used as a strong baseline for evaluating the performance of Titans. This work explores improvements to recurrent models by incorporating gating and the Delta Rule, ideas that are conceptually related to the memory mechanisms in Titans.