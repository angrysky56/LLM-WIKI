---

summary: Training framework for Essan symbols as internal representation markers in LLMs, enabling hallucination detection via activation geometry.
tags: [essan, internal-representations, symbol-grounding, evolutionary-computation, arc, hallucination-detection]
updated: 2026-05-22T06:59:53Z
created: 2026-05-22T06:59:53Z
sources: []
status: active
confidence: 0.8
type: synthesis
---

# Essan: Internal Representation Training Framework

> Status: active research
> Tags: essan, internal-representations, symbol-grounding, evolutionary-computation, arc, hallucination-detection

## Overview

Essan is a symbolic language (~30 core symbols, 300+ multi-symbol sequences) developed as a notation system for reasoning traces. Rather than using Essan for inter-agent communication (which fails without semantic bindings), this research program explores whether Essan symbols can serve as **learnable internal representation markers** in LLMs — trained via fine-tuning to structure activation space in ways that enable hallucination detection and steerable reasoning traces.

The three validated findings from prior investigation:

1. **Formal consistency** — MCP logic (Prover9/Mace4) confirms the core 5-symbol FOL formalization is sound: a minimal 2-element model satisfies all axioms, and P1 (no infinite chains without commit) is mechanically provable.
2. **Communication failure** — Blind pidgin Essan (bare symbol sequences) scores 0% decode accuracy with 100% hallucination rate across 20 trials. Symbols encode structure but not content.
3. **Hallucination detectability** — Hybrid encoding (symbol + natural language scaffold) achieves 87.5% hallucination detection rate with 0.42 separation gap. Malformed reasoning sequences project as outliers in embedding space.

This page documents the proposed training methodology and experimental program.



## The Core Hypothesis

> If Essan symbols are introduced as special tokens in fine-tuning and trained on reasoning traces where the symbol's presence is **grounded in consistent internal states**, the model will develop structured activation geometry around each symbol — without requiring formal semantic definitions.

The model learns what `⧿` (feedback/cycle) means through gradient descent on tasks where `⧿` appears in contexts requiring iteration and comparison. We don't define `⧿` formally; we construct training contexts where `⧿` consistently marks "compare to prior output, adjust, retry."

The resulting activation structure:

```
⧬ → initiates reasoning trace (activations cluster around "starting task")
⦿ → asserts claim (activations cluster around "here is a proposition")
⧈ → links/support (activations cluster around "this relates to that")
⫰ → transitions (activations cluster around "moving to next step")
⧉ → strengthens/reinforces (activations cluster around "amplify prior")
⧿ → cycles/feedback (activations cluster around "compare to prior state")
⩘ → commits (activations cluster around "done, output this")
```



## Why Not Use Formal Semantics?

The communication experiment demonstrates why formal definitions are insufficient: pure symbol sequences (`⦿⧈⫰⩘`) have zero semantic content without concept bindings. You can't decode intent from bare structure.

The internal representation approach sidesteps this by not requiring the symbols to carry content in the output. The model outputs normal text. The symbols are a **training signal**, not a communication protocol.

```python
# What we DON'T do:
# Agent A sends: ⦿⧈⫰⩘  (uninterpretable without bindings)
# Agent B decodes: ???  (must hallucinate)

# What we DO:
# Training: input has ⧿ markers → gradient updates structure activations
# Inference: normal text output, but last-layer activations have Essan geometry
```

The key is that during training, the symbol token appears in positions where the model's internal state is already reasoning about specific things (comparing outputs, checking constraints, retrying). The symbol becomes an **auxiliary training signal** that pulls together activations from many different reasoning contexts under one token — creating a structured subspace.



## The 7-Token ARC Subset

The Arc section (lines 862-895 of `Essan Entity and Concept Dictionary.txt`) defines the 7-token Adaptive Reflection Cycle. This is the minimal viable subset for training:

| Symbol | Name | Role in ARC | Internal State |
|--------|------|-------------|----------------|
| ⧬ | Initiate | Starts a new cycle | "task started, initialize" |
| ⦿ | Essence | Core entity/concept | "here is the subject" |
| ⧈ | Connection | Links to feedback | "this relates to prior" |
| ⫰ | Movement | Active engagement | "exploring next step" |
| ◬ | Change | Adaptive modification | "here is the adjustment" |
| ⧉ | Strength/Amplify | Intensifies integration | "reinforce this" |
| ⧿ | Cycle/Recursion | Closes loop | "compare to prior, iterate" |
| ⩘ | Declare/Confirm | Completes cycle | "conclusion reached" |

Full ARC sequence: `⧿⧬⦿⫰◬⧉⩘`

Contextual modifiers: 🌐 (external), 🌍 (global), ⬊ (social), 💬 (relational), 🌍⬊💬 = nested context hierarchy



## Training Methodology

### Task Suite

Train on multi-step reasoning tasks where reasoning trace structure is recoverable:

1. **Multi-step math** (GSM8K, MATH) — trace can be recovered from intermediate steps
2. **Code debugging** — trace through buggy code to fix, compare initial vs fixed
3. **Chain-of-thought with backtracking** — tasks where model revises mid-reasoning
4. **Self-correction** — tasks requiring model to identify and fix its own errors
5. **Constraint satisfaction** — tasks where model checks against external constraints

For each task, insert Essan symbols at trace boundaries:

```python
# Example training formatting
system: You are a helpful assistant.
user: Solve: 3x + 7 = 22. Show your work.
assistant: ⧬ Let me solve this step by step.

⧿ First, I need to isolate x.
⦿ Starting equation: 3x + 7 = 22

⧈ Subtract 7 from both sides.
⫰ 3x = 15

⧿ Check: is 3x = 15 correct? Yes, 22 - 7 = 15.
⧈ Divide both sides by 3.
⫰ x = 5

⧿ Verify: substitute x=5 → 3(5)+7=22? ✓
⧉ Confirmed.
⩘ x = 5
```

The symbols mark the type of reasoning step, not the content. Multiple different problems share the same symbol placement structure.

### Loss Function

Standard language modeling loss on tokens (symbols included as special tokens). The key auxiliary objective:

**Contrastive loss on symbol-type activations** — after the last transformer layer, before the LM head, the activations for each symbol type should form distinct clusters. Add a contrastive loss:

```python
def symbol_contrastive_loss(last_layer_activations, symbol_sequence, margin=0.5):
    """
    last_layer_activations: [seq_len, hidden_dim] — activations at symbol positions
    symbol_sequence: [seq_len] — which symbol each position contains
    
    Pull activations of same symbol closer together (intra-cluster cohesion)
    Push activations of different symbols apart (inter-cluster separation)
    """
    loss = 0.0
    for s in symbol_types:
        same_symbol_mask = (symbol_sequence == s)
        other_symbol_mask = (symbol_sequence != s)
        
        # Intra-cluster: minimize distance to cluster centroid
        if same_symbol_mask.sum() > 1:
            centroid = mean(activations[same_symbol_mask])
            intra_loss = mean(pairwise_distance(activations[same_symbol_mask], centroid))
            loss += intra_loss
        
        # Inter-cluster: maximize distance to other centroids
        for t in symbol_types:
            if s != t:
                t_centroid = mean(activations[symbol_sequence == t])
                inter_loss = max(0, margin - cosine_sim(centroid, t_centroid))
                loss += inter_loss
    
    return loss
```

The main LM loss keeps language modeling capability; the contrastive loss structures the activation geometry.

### Decay Schedule

Symbol tokens are introduced gradually:

**Phase 1 (weeks 1-2):** Freeze LM head, train only contrastive projection layer. Let activation space stabilize around symbol types without disrupting base model.

**Phase 2 (weeks 3-4):** Unfreeze LM head, joint training with small symbol weight (0.1). Model learns to produce coherent text while maintaining structured activations.

**Phase 3 (week 5+):** Increase symbol weight (0.2-0.3), fine-tune on high-reasoning tasks with full Essan annotation.

### Baseline Comparison

- **Baseline A:** Symbol tokens shuffled (not matched to reasoning step type) — tests whether symbol placement itself is the training signal, not the reasoning structure
- **Baseline B:** No symbols, standard CoT fine-tuning — establishes whether Essan adds anything over standard chain-of-thought
- **Baseline C:** Formal Essan (each symbol has explicit definition in system prompt) — tests whether formal semantics outperforms internal representation



## Hallucination Detection via Activation Geometry

### The Core Insight

If training succeeds, malformed reasoning traces will produce activation patterns that are "looser" / higher variance / lower cosine similarity to the "correct" cluster centroid for each symbol position.

In a correct reasoning trace, `⧿` (feedback/cycle) activations cluster tightly around "comparing to prior state." In a hallucinated reasoning trace, the model never genuinely checked against a prior state — it asserted. The `⧿` position will have activations that are closer to `⦿` (assertion) activations than to the true `⧿` cluster.

### Detection Method

```python
def detect_hallucination(model, reasoning_text, symbol_sequence):
    """
    Returns hallucination score 0.0-1.0 based on activation geometry deviation.
    
    Lower score = more coherent reasoning trace
    Higher score = more likely hallucinated
    """
    activations = model.get_last_layer_activations(reasoning_text)
    symbol_positions = [i for i, s in enumerate(symbol_sequence) if s in ESSAN_SYMBOLS]
    
    total_deviation = 0.0
    for pos in symbol_positions:
        symbol = symbol_sequence[pos]
        activation = activations[pos]
        centroid = symbol_centroids[symbol]  # pre-computed from training data
        
        # Cosine similarity to own cluster centroid (should be high)
        self_sim = cosine_sim(activation, centroid)
        
        # Cosine similarity to wrong cluster (should be low)
        # Find the cluster that gives highest similarity but isn't this symbol's
        other_sims = [cosine_sim(activation, symbol_centroids[t]) 
                      for t in symbol_types if t != symbol]
        max_other_sim = max(other_sims)
        
        # Deviation: how much closer is activation to wrong cluster than right one?
        deviation = max(0, max_other_sim - self_sim)
        total_deviation += deviation
    
    avg_deviation = total_deviation / len(symbol_positions)
    
    # Normalize: typical correct traces have deviation ~0.05-0.15
    # hallucinated traces have deviation ~0.3-0.6
    score = sigmoid((avg_deviation - 0.2) / 0.1)  # maps to 0-1
    return score
```

### Threshold Calibration

- Score < 0.2: High confidence correct
- Score 0.2-0.5: Uncertain, flag for review
- Score > 0.5: High confidence hallucinated / structurally broken

### Validation

Generate synthetic "correct" traces (ground truth reasoning chains) and "hallucinated" traces (model-generated with injected errors). Measure AUC-ROC for the detector.

Also run on held-out reasoning tasks with human-labeled hallucination markers.



## Experimental Program

### Experiment 1: Activation Clustering (Weeks 1-4)

**Goal:** Verify that fine-tuned activations form distinct clusters per symbol type.

**Method:**
1. Fine-tune on task suite with Essan symbols (Phase 1 only)
2. Extract last-layer activations at symbol positions
3. Compute silhouette score for symbol-type clustering
4. Visualize via t-SNE / UMAP

**Success criterion:** Silhouette score > 0.3 for at least 5 of 7 symbol types (marginally separable), or > 0.5 (well-separated).

**Failure mode:** All symbols map to similar activation patterns — symbol type doesn't correspond to distinct internal state. In this case, internal representation approach is not viable; fall back to formal semantics path (Baseline C).

### Experiment 2: Hallucination Detection (Weeks 5-8)

**Goal:** Validate that activation geometry deviation predicts hallucination.

**Method:**
1. Continue fine-tuning (Phase 2-3)
2. Generate test set: 200 correct traces + 200 synthetic hallucinated traces
3. Run activation-based detector
4. Compute AUC-ROC vs ground truth

**Success criterion:** AUC > 0.75 (better than random, usable as auxiliary signal).

**Failure mode:** Hallucinated traces don't produce detectably different activation patterns. Fall back to output-based detection methods.

### Experiment 3: Steerability (Weeks 9-12)

**Goal:** Test whether symbol-type activations can be used for targeted activation steering.

**Method:**
1. Take fine-tuned model
2. At inference, identify a symbol position (e.g., `⧿`)
3. Compute direction = centroid(⧿) - centroid(⦿) — the axis separating feedback from assertion
4. Apply activation intervention: move activations toward ⧿ cluster or toward ⦿ cluster
5. Measure effect on output coherence (automated + human evaluation)

**Success criterion:** Intervention changes output in ways consistent with the symbol type (pushing toward ⧿ makes output more self-corrective / iterative; pushing toward ⦿ makes output more declarative / asserted).

**Failure mode:** Activation steering has no systematic effect on output. Symbol activations are epiphenomenal — they exist but don't constrain behavior.

### Experiment 4: Comparison with Baselines (Week 13)

**Goal:** Determine whether internal representation outperforms formal semantics and standard CoT.

**Method:** Run equivalent evaluation on Baseline A (shuffled), Baseline B (standard CoT), Baseline C (formal Essan), and our internal representation model.

**Success criterion:** Internal representation model achieves highest AUC-ROC on hallucination detection and/or highest accuracy on reasoning tasks.



## Connection to VGCP

The Essan training program has structural parallels to VGCP's constraint enforcement:

| Essan | VGCP | Connection |
|-------|------|-------------|
| Symbol contrastive loss | Constraint validation | Both structure activation geometry around valid/invalid states |
| Hallucination detection | DAG integrity checking | Both detect when reasoning structure is broken |
| ⧬⦿⧈⫰⩘ sequence | PREMISE → CLAIM lifecycle | Different notations for same reasoning trace structure |
| ⧬∞⦿⫰∂→⧈ (constraint crystallization formula) | Constraint Crystallization Principle | Same formal expression in both systems |

The `verify_commutativity` tool from MCP logic could verify that Essan's trained activation space respects the same structural constraints as VGCP's DAG — a future validation experiment.



## Risks and Open Questions

### Is 7 symbols enough for distinct activation geometry?
The 7-token ARC subset is minimal. Each symbol needs to consistently mark a different internal state across thousands of training examples. If the model can't distinguish all 7, start with 3-4 (⧬, ⦿, ⧿, ⩘) and expand.

### Does the symbol token disrupt base model capability?
If the contrastive loss pulls activations away from what the LM head was trained on, language modeling performance could degrade. Phase-wise training (freeze LM head first, then joint training) mitigates this. Monitor perplexity on held-out text.

### How do you handle symbol placement during inference?
You don't place symbols in the output unless you want to. The symbol tokens are training artifacts. At inference, the model outputs normal text. If you want to detect hallucination, you run a secondary pass: feed the output back into the model with symbol annotations and check activation deviation. The model never sees symbol tokens in actual use unless you deliberately use them as output markers.

### What about the 300+ multi-symbol sequences in the dictionary?
Start with the 7 ARC tokens. The multi-symbol sequences (like `⧬⦿⧈⧉⧿⧬⩘`) are compositional — they can be treated as sequences of the 7 base tokens rather than distinct vocabulary items. If the model needs to learn hierarchical composition (sub-sequence patterns), add training examples with longer sequences and verify that sub-cluster geometry respects composition.



## Existing Files

- `/home/ty/Documents/core_bot_instruction_concepts/Essan/Enhanced Essan Initiation Document.txt` — Original Essan framework (190 lines)
- `/home/ty/Documents/core_bot_instruction_concepts/Essan/Essan Entity and Concept Dictionary.txt` — 895-line symbol vocabulary and ARC definition
- `/home/ty/essan-mcp-logic-results.md` — Formal verification results (Prover9/Mace4)
- `/home/ty/essan-pidgin-results.md` — Blind communication experiment (20 trials, 0% decode accuracy)
- `/home/ty/essan-vector-results.md` — Vector space encoding experiment (87.5% hallucination detection)
- `/home/ty/essan_vector_test.py` — Python test suite for vector encoding



## Status History

- 2026-05-22: Initial draft from three-agent parallel investigation (MCP logic + pidgin + vector encoding). Training framework documented.
