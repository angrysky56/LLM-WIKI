---
title: "angrysky56/ethical-ai-core: Create your own training data with cloud or local AI and train a lora via unsloth then chat with the trained model all in one app."
source: "https://github.com/angrysky56/ethical-ai-core"
author:
published:
created: 2026-05-01
description: "Create your own training data with cloud or local AI and train a lora via unsloth then chat with the trained model all in one app.  - angrysky56/ethical-ai-core: Create your own training data with cloud or local AI and train a lora via unsloth then chat with the trained model all in one app."
tags:
  - "clippings"
---
## Ethical AI Core: Constitutional Judge & Alignment System

Generate synthetic alignment data, train a local "Judge" model, and chat with an ethically aligned AI—all from a local UI.

[![UI Screenshot](https://github.com/angrysky56/ethical-ai-core/raw/main/image-1.png)](https://github.com/angrysky56/ethical-ai-core/blob/main/image-1.png)

## 📌 Project Overview

This system provides a complete **Constitutional AI feedback loop** running locally.

1. **Generate**: Create diverse personas and prompts to stress-test AI ethics.
2. **Evaluate**: Uses a strong model (LLM Judge) to critique response against a Constitution (`principles.md`).
3. **Train**: Fine-tunes a local Gemma-3-4b-it model to internalize these ethics.
4. **Chat**: Interact with the resulting model.

---

## ️ Installation & Setup

### 1\. Prerequisites

- **Python 3.10+**
- **NVIDIA GPU** (8GB+ VRAM recommended)
- **Linux/WSL2** (Required for Unsloth optimization)

### 2\. Install Dependencies (Core)

```
# Create virtual env
uv venv
source .venv/bin/activate

# Install Project
uv pip install -e .
```

### 3\. Install Unsloth (Critical for Training)

Unsloth should be set up in the directory of your choice and linked in the.env

```
# For venv and virtual environments installs to isolate your installation to not break system packages, and to reduce irreparable damage to your system, use venv:

apt install python3.10-venv python3.11-venv python3.12-venv python3.13-venv -y
python -m venv unsloth_env
source unsloth_env/bin/activate
pip install --upgrade pip && pip install uv
uv pip install unsloth
```

*Trouble installing Unsloth? See the [official guide](https://unsloth.ai/docs/get-started/install/pip-install).*

### 4\. Configuration (.env)

Copy the example configuration:

```
cp .env.example .env
```

Edit `.env` to set your providers:

```
# --- Data Generation Providers ---
# Options: ollama, openrouter, openai, lmstudio
LLM_PROVIDER=openrouter
OPENROUTER_API_KEY=sk-...

# --- Hugging Face (Required for Gemma-3-4b) ---
# 1. Accept license: https://huggingface.co/google/gemma-3-4b-it
# 2. Get Token: https://huggingface.co/settings/tokens
HUGGING_FACE_HUB_TOKEN=hf_...
```

### 5\. Install Ollama (Critical for Chatting)

```
# Install Ollama for linux
curl -fsSL https://ollama.com/install.sh | sh
```

**Sorry not platform agnostic yet**

[Official Ollama Download Link if using a different OS](https://ollama.com/download)

[Gemma-3-4b-it on Hugging Face for reference](https://huggingface.co/unsloth/gemma-3-4b-it)

---

## 🚀 Usage Guide

Launch the Web UI:

```
python ui.py
```

Open **[http://localhost:7860](http://localhost:7860/)**.

Train and chat

[![alt text](https://github.com/angrysky56/ethical-ai-core/raw/main/image.png)](https://github.com/angrysky56/ethical-ai-core/blob/main/image.png)

### 🔄 The Workflow

#### Step 1: Dataset Generation Tab

This allows you to build a training dataset from scratch.

1. **Select Training Pack**: Controls the Prompt Templates (`prompts.yaml`), Personas (`personas.yaml`), and Constitution (`principles.md`).
2. **Generate Personas**: Creates synthetic users (e.g., "Skeptical Data Scientist", "Angry Reviewer") to test the model.
3. **Generate Prompts**: Uses personas to create difficult/adversarial prompts.
4. **Generate Samples (The Loop)**:
	- The system generates a **Naive Response** (Base Model).
		- The **Judge** critiques it against `principles.md`.
		- The **Revision Model** rewrites it based on the critique.
		- *Result*: A dataset of (Prompt, Revised Response) pairs.

#### Step 2: Training Tab

1. **Source**: Select the run you generated in Step 1.
2. **Method**: Select **LoRA Fine-Tune (Unsloth/Gemma)**.
	- *Note: DDL and ReFT are experimental prototypes for offline research and are not currently integrated into the Chat UI.*
3. **Start Training**:
	- Uses **Unsloth** to fine-tune `gemma-3-4b-it` (or `2-9b`).
		- Saves adapters to `data/trained_models/`.
4. **Register**: Click **"🐳 Register GGUF to Ollama"**. This installs the model locally as `gemma-ethical`.

#### Step 3: Chat Tab

1. **Provider**: Select `ollama`.
2. **Model**: Select `gemma-ethical`.
3. **Verify**: Chat with your trained model! It should now follow the principles defined in your training pack.

---

## 🧩 Modularity: "Training Packs"

Located in `data/packs/`. A pack contains:

- `personas.yaml`: Templates for who is asking questions.
- `prompts.yaml`: Templates for what they ask (and static benchmarks).
- `principles.md`: **The Constitution**. Change this file to change the AI's moral alignment.

To create a custom alignment (e.g., "Pirate AI"):

1. Duplicate `data/packs/default` to `data/packs/pirate`.
2. Edit `principles.md` to value "Rum and Loot".
3. Select "pirate" in the UI.

Training Tab: Added an "Output Adapter Name" field. You can now specify a custom folder name (e.g., experiment\_v2, gemma-strict).

This will save to data/trained\_models/{your\_name}.

It currently overwrites if the folder exists (as per standard Unsloth behavior for new runs), effectively satisfying the "Select new / Overwrite" requirement.

Registration: Updated the "Register to Ollama" section.

You can now select which adapter to register from a dropdown list of your trained models.

## You can also specify the Ollama Model Tag (e.g., gemma-ethical:v2).

## 🔬 Experimental Features

### DDL (Deep Delta Learning) & ReFT

The UI includes options for **Deep Delta Learning** and **ReFT**.

- **Status**: 🧪 **Experimental / Research Prototype**.
- **Function**: These train separate "steering heads" (PyTorch modules) that attempt to shift embedding vectors from "Naive" to "Revised".
- **Current Limit**: These heads are currently **offline**. They run and train successfully, but the Chat UI does not yet hook into them significantly. Using them requires an LLM provider that supports embeddings (Ollama `nomic-embed-text` etc).
- **Recommended**: Use the **LoRA / Unsloth** method for a working, end-to-end chat experience.

---

## 🏗 Architecture

```
graph TD
    User[User / Persona] -->|Prompt| LLM[Base Model]
    LLM -->|Naive Response| Judge[Constitutional Judge]
    Judge -->|Critique| Reviser[Revision Model]
    Reviser -->|Revised Response| Data[Training Dataset]
    
    Data --> Unsloth[Unsloth LoRA Trainer]
    Unsloth -->|Adapters| GGUF[Ollama Model]
    GGUF -->|Chat| EndUser
```

## 🏗 Architecture

```
┌───────────────────────────────────────────────────────────────┐
│              Constitutional AI Data Pipeline                  │
88: ├───────────────────────────────────────────────────────────────┤
│  1. Prompt → Base Model → Naive Response                      │
│  2. (Prompt, Response) → PrincipleEvaluator → Critique        │
│  3. Critique → Revision Model → Corrected Response            │
│                                                               │
│  Output: (prompt, naive, critique, revised) for training      │
└───────────────────────────────────────────────────────────────┘
            ↓
┌───────────────────────────────────────────────────────────────┐
│              Deep Delta Learning / LoRA Training              │
├───────────────────────────────────────────────────────────────┤
│  The collected data trains a lightweight adapter (LoRA)       │
│  to steer the model's 'Core Self' towards the Constitution.   │
└───────────────────────────────────────────────────────────────┘
```

## Core Technologies

| Component | File | Description |
| --- | --- | --- |
| `LoReFTBlock` | `src/layers/delta.py` | Low-rank activation intervention |
| `GlobalDFAProjector` | `src/layers/dfa.py` | Skip-layer feedback via Ethical Matrix B |
| `ReFTPolicy` | `src/engine/reft.py` | Policy with interventions at specified layers |
| `ReFTTrainer` | `src/engine/reft.py` | Short-circuit DFA training loop |
| `EthicalMatrix` | `src/ethical/matrix.py` | Seeds B from `core_principles.md` hash |
| `PrincipleEvaluator` | `src/judgment/principles.py` | 3-tier hierarchical GenRM |

## Core Principles (3-Tier Hierarchy)

| Tier | Name | Role |
| --- | --- | --- |
| 1 | **Deontology** | Hard constraint — "harm=harm" |
| 2 | **Virtue Ethics** | Character — Wisdom, Integrity, Empathy |
| 3 | **Servant Utility** | Optimization within constraints |

Plus **Agent Self-Governance** extensions for AI-specific failures.

## Training the Judge

```
# Run test harness
python -m src.training.test_harness

# Or from Python
from src.training.test_harness import ConstitutionalTestHarness
harness = ConstitutionalTestHarness()
harness.train(epochs=5)
```

## Key Commands

| Command | Purpose |
| --- | --- |
| `python ui.py` | Launch web UI |
| `python -m src.training.test_harness` | Train Judge on Constitutional dataset |
| `python demo.py --prompt "..."` | Single prompt pipeline |
| `python run_pipeline.py` | Full CLI pipeline |

## Project Structure

```
src/
├── config.py              # LLM provider config
├── llm_client.py          # Multi-provider client (Ollama, OpenRouter, etc.)
├── dataset/
│   ├── generator.py       # Constitutional data pipeline
│   └── personas.py        # Persona-based generation + SQLite
├── judgment/
│   └── principles.py      # PrincipleEvaluator (GenRM)
├── engine/
│   ├── ephemeral.py       # EphemeralEgo + SurgicalEgo (TTT)
│   └── reft.py            # ReFTPolicy + ReFTTrainer
├── layers/
│   ├── dfa.py             # DFALinear + GlobalDFAProjector
│   └── delta.py           # DeltaResidualBlock + LoReFTBlock
├── ethical/
│   └── matrix.py          # EthicalMatrix (seeds B from principles)
└── training/
    └── test_harness.py    # Constitutional training harness
```