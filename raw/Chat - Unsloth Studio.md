---
title: "Chat - Unsloth Studio"
source: "http://localhost:8889/chat?new=333fb779-0129-4203-9a83-6b089a63d99d"
author:
published:
created: 2026-07-12
description:
tags:
  - "clippings"
---
How do we train a model using unsloth for this https://www.alphaxiv.org/abs/2509.13351

The user is asking how to train a model using Unsloth for a specific paper: "Teaching LLMs to Plan: Logical Chain-of-Thought Instruction Tuning for Symbolic Planning" (alphaXiv ID: 2509.13351).

From the alphaXiv abstract:

- The paper presents a novel instruction tuning framework, PDDL-Instruct, designed to enhance LLMs' symbolic planning capabilities through logical chain-of-thought reasoning.
- It focuses on teaching models to rigorously reason about action applicability, state transitions, and plan validity using explicit logical inference steps.
- It decomposes the planning process into explicit reasoning chains about precondition satisfaction, effect application, and invariant preservation.
- Achieves planning accuracy of up to 94% on standard benchmarks, a 66% absolute improvement over baseline models.

The user wants to know how to train a model using Unsloth for this. The paper is about "logical chain-of-thought instruction tuning for symbolic planning" using PDDL (Planning Domain Definition Language).

Unsloth documentation mentions:

1. For reasoning/chain-of-thought models, use a mix of direct answers and chain-of-thought examples. Use 75% reasoning and 25% non-reasoning (or similar ratios).
2. For models that already have reasoning capabilities, you need to follow question/task and answer pairs, but for the answer, you need to change the answer so it includes reasoning/chain-of-thought process and the steps it took to derive the answer.
3. Dataset format for SFT (Supervised Fine-Tuning) using Unsloth:
	- Question/Task and Answer pairs.
		- For reasoning models, the answer should include reasoning/chain-of-thought process and the steps it took to derive the answer.
		- Dataset formatting typically uses a conversation format:
		```
		[
		{ "role": "user",
		  "content": [{"type": "text",  "text": instruction}, ...]
		},
		{ "role": "assistant",
		  "content": [{"type": "text",  "text": answer_with_chain_of_thought} ]
		},
		]
		```
		- Or using the `formatting_prompts_func` for ShareGPT format:
		```
		def formatting_prompts_func(examples):
		    conversations = []
		    for i in range(len(examples['question'])):
		        conv = [
		            {"role": "user", "content": examples['question'][i]},
		            {"role": "assistant", "content": examples['answer'][i]}
		        ]
		        conversations.append(conv)
		    return conversations
		```

Wait, the paper is about "PDDL-Instruct", which is an instruction tuning framework for symbolic planning using PDDL (Planning Domain Definition Language). The chain-of-thought reasoning is about:

- action applicability
- state transitions
- plan validity
- precondition satisfaction
- effect application
- invariant preservation

So to train a model using Unsloth for this, we need to:

1. Prepare a dataset in the PDDL-Instruct format or similar chain-of-thought format for symbolic planning (PDDL domains and problems).
2. Use Unsloth's SFTTrainer with LoRA/QLoRA to fine-tune the model.
3. Ensure the dataset includes chain-of-thought reasoning steps: precondition satisfaction, effect application, invariant preservation, etc.

Let's look at the Unsloth SFTTrainer and dataset formatting for chain-of-thought or reasoning tasks.

From the Unsloth docs:

- For models with reasoning capabilities (like distilled R1), you need to follow question/task and answer pairs, but the answer must include reasoning/chain-of-thought process and the steps it took to derive the answer.
- For non-reasoning models to learn reasoning, you might use GRPO or standard dataset without reasoning in answers (but for SFT with CoT, you include CoT in the answers).
- Dataset format for SFT:
	```python
	from unsloth.chat_templates import get_chat_template
	tokenizer = get_chat_template(
	    tokenizer,
	    mapping = {"role" : "from", "content" : "value", "user" : "human", "assistant" : "gpt"},
	)
	def formatting_prompts_func(examples):
	    convos = examples["conversations"]
	    texts = [tokenizer.apply_chat_template(convo, tokenize = False, add_generation_prompt = False) for convo in convos]
	    return { "text" : texts, }
	pass
	from trl import SFTTrainer
	from transformers import TrainingArguments
	from unsloth import is_bfloat16_supported
	trainer = SFTTrainer(
	    model = model,
	    tokenizer = tokenizer,
	    train_dataset = dataset,
	    dataset_text_field = "text",
	    max_seq_length = max_seq_length,
	    dataset_num_proc = 2,
	    packing = False, # Can make training 5x faster for short sequences.
	    args = TrainingArguments(
	        per_device_train_batch_size = 2,
	        gradient_accumulation_steps = 4,
	        warmup_steps = 5,
	        max_steps = 60,
	        learning_rate = 2e-4,
	        fp16 = not is_bfloat16_supported(),
	        bf16 = is_bfloat16_supported(),
	        logging_steps = 1,
	        optim = "adamw_8bit",
	        weight_decay = 0.01,
	        lr_scheduler_type = "linear",
	        seed = 3407,
	        output_dir = "outputs",
	        report_to = "none", # Use this for WandB etc
	    ),
	)
	trainer.train()
	```

Also, for chain-of-thought reasoning datasets, the Unsloth docs say: "If you want to fine-tune a model that already has reasoning capabilities like the distilled versions of DeepSeek-R1 (e.g. DeepSeek-R1-Distill-Llama-8B), you will need to still follow question/task and answer pairs however, for your answer you will need to change the answer so it includes reasoning/chain-of-thought process and the steps it took to derive the answer."

And for maintaining reasoning capabilities: "If you want to maintain its reasoning capabilities (optional), you can use a mix of direct answers and chain-of-thought examples. Use 75% reasoning and 25% non-reasoning in your dataset to make the model retain its reasoning capabilities."

For the PDDL-Instruct framework: The paper PDDL-Instruct focuses on:

- teaching models to rigorously reason about action applicability, state transitions, and plan validity using explicit logical inference steps.
- instruction prompts that guide models through the precise logical reasoning required to determine when actions can be applied in a given state.
- decomposing the planning process into explicit reasoning chains about:
	1. precondition satisfaction
		2. effect application
		3. invariant preservation

So to train a model using Unsloth for this task, the user needs to:

1. Create a dataset with PDDL domains/problems and the corresponding chain-of-thought reasoning steps (precondition satisfaction, effect application, invariant preservation, plan validity).
2. Format the dataset for Unsloth's SFTTrainer, ensuring the assistant's response includes the chain-of-thought reasoning steps.
3. Use Unsloth's `FastModel` and `FastModel.get_peft_model` for LoRA/QLoRA fine-tuning.
4. Use `SFTTrainer` from `trl` with the formatted dataset.

Let me structure the response:

1. Understand the PDDL-Instruct Framework: Briefly summarize the paper's approach (logical chain-of-thought instruction tuning for symbolic planning using PDDL, focusing on action applicability, state transitions, plan validity, precondition satisfaction, effect application, and invariant preservation).
2. Prepare the Dataset for Chain-of-Thought Reasoning:
	- The dataset should consist of pairs: (PDDL Domain + PDDL Problem) as the "question/task", and a "chain-of-thought answer" that includes the explicit logical inference steps (precondition satisfaction, effect application, invariant preservation, plan validity).
		- Example dataset format for Unsloth SFT:
		```json
		[
		  {
		    "conversations": [
		      {
		        "from": "human",
		        "value": "Domain: ...\nProblem: ...\nGenerate a plan using logical chain-of-thought reasoning."
		      },
		      {
		        "from": "gpt",
		        "value": "Step 1: Analyze the initial state and goal...\nStep 2: Check action applicability and precondition satisfaction for possible actions...\nStep 3: Apply effects and update the state...\nStep 4: Verify invariant preservation and plan validity...\nFinal Plan: ..."
		      }
		    ]
		  }
		]
		```
3. Set up Unsloth for Fine-tuning:
	- Install Unsloth: `pip install --upgrade --force-reinstall --no-cache-dir unsloth unsloth_zoo`
		- Load the model using `FastModel.from_pretrained`.
		- Apply LoRA/QLoRA using `FastModel.get_peft_model`.
4. Format the Dataset for Unsloth's SFTTrainer:
	- Use `unsloth.chat_templates.get_chat_template` or standard ShareGPT formatting.
		- Create a `formatting_prompts_func` to convert the dataset into chat template format.
5. Train using SFTTrainer:
	- Use `trl.SFTTrainer` with `TrainingArguments`.
		- Ensure the dataset includes a mix of reasoning (chain-of-thought for PDDL planning) and non-reasoning (direct PDDL plan output) if maintaining general capabilities is desired (e.g., 75% reasoning / 25% non-reasoning).

Let me provide a concrete code example based on Unsloth's SFT training guide and the chain-of-thought dataset preparation guidelines.

From the Unsloth docs: Dataset format for reasoning/CoT: "For a model that already has reasoning capabilities... you will need to still follow question/task and answer pairs however, for your answer you will need to change the answer so it includes reasoning/chain-of-thought process and the steps it took to derive the answer."

Also, for the chat template formatting:

```python
from unsloth.chat_templates import get_chat_template, standardize_sharegpt

# Get chat template
tokenizer = get_chat_template(
    tokenizer,
    mapping = {"role" : "from", "content" : "value", "user" : "human", "assistant" : "gpt"},
)

def formatting_prompts_func(examples):
    convos = examples["conversations"]
    texts = [tokenizer.apply_chat_template(convo, tokenize = False, add_generation_prompt = False) for convo in convos]
    return { "text" : texts, }
pass

dataset = standardize_sharegpt(dataset)
dataset = dataset.map(formatting_prompts_func, batched = True,)
```

And the SFTTrainer setup:

```python
from trl import SFTTrainer
from transformers import TrainingArguments
from unsloth import is_bfloat16_supported

trainer = SFTTrainer(
    model = model,
    tokenizer = tokenizer,
    train_dataset = dataset,
    dataset_text_field = "text",
    max_seq_length = max_seq_length,
    dataset_num_proc = 2,
    packing = False, # Can make training 5x faster for short sequences.
    args = TrainingArguments(
        per_device_train_batch_size = 2,
        gradient_accumulation_steps = 4,
        warmup_steps = 5,
        max_steps = 60, # Change to your total steps
        learning_rate = 2e-4,
        fp16 = not is_bfloat16_supported(),
        bf16 = is_bfloat16_supported(),
        logging_steps = 1,
        optim = "adamw_8bit",
        weight_decay = 0.01,
        lr_scheduler_type = "linear",
        seed = 3407,
        output_dir = "outputs",
        report_to = "none", # Use this for WandB etc
    ),
)
trainer.train()
```

Let's also mention the specific chain-of-thought steps from the PDDL-Instruct paper:

- Precondition satisfaction: determining when actions can be applied in a given state.
- Effect application: updating the state after applying an action.
- Invariant preservation: ensuring the plan doesn't violate domain invariants.
- Plan validity: verifying the complete sequence of actions leads to the goal state.

Let's ensure the response is well-structured and provides actionable steps for the user to train a model using Unsloth for the PDDL-Instruct logical chain-of-thought instruction tuning for symbolic planning.

Steps to outline:

1. Overview of PDDL-Instruct & Chain-of-Thought Tuning: Explain what the paper does and how it maps to Unsloth's CoT fine-tuning approach.
2. Dataset Preparation for PDDL Symbolic Planning: Show the format of the dataset with PDDL domains/problems and CoT answers (precondition satisfaction, effect application, invariant preservation, plan validity).
3. Unsloth Setup & Model Loading: Code to load the model and apply LoRA.
4. Dataset Formatting for Unsloth SFTTrainer: Code to format the dataset using chat templates.
5. Training with SFTTrainer: Code to set up and run `SFTTrainer`.
6. Tips for Maintaining Reasoning Capabilities: Mention the 75% reasoning / 25% non-reasoning mix if the model is a general-purpose LLM being fine-tuned for PDDL planning.

Let's verify the Unsloth chat template formatting. In Unsloth, the `standardize_sharegpt` and `formatting_prompts_func` are commonly used:

From the docs:

```python
from unsloth.chat_templates import standardize_sharegpt
dataset = standardize_sharegpt(dataset)
dataset = dataset.map(formatting_prompts_func, batched = True,)
```

And `formatting_prompts_func`:

```python
def formatting_prompts_func(examples):
    convos = examples["conversations"]
    texts = [tokenizer.apply_chat_template(convo, tokenize = False, add_generation_prompt = False) for convo in convos]
    return { "text" : texts, }
pass
```

Wait, in the Unsloth docs for gpt-oss:

```python
from unsloth.chat_templates import standardize_sharegpt
dataset = standardize_sharegpt(dataset)
dataset = dataset.map(formatting_prompts_func, batched = True,)

def formatting_prompts_func(examples):
    convos = examples["conversations"]
    texts = [tokenizer.apply_chat_template(convo, tokenize = False, add_generation_prompt = False) for convo in convos]
    return { "text" : texts, }
pass
```

Wait, let me check the exact `formatting_prompts_func` from the docs: From "Liquid LFM2.5: How To Run & Fine-tune":

```python
from trl import SFTTrainer
from transformers import TrainingArguments
from unsloth import is_bfloat16_supported
trainer = SFTTrainer(
    model=model,
    tokenizer=tokenizer,
    train_dataset=dataset,
    dataset_text_field="text",
    max_seq_length=4096,
    dataset_num_proc=2,
    packing=False,
    args=TrainingArguments(
        per_device_train_batch_size=2,
        gradient_accumulation_steps=4,
        warmup_steps=5,
        max_steps=60,
        learning_rate=2e-4,
        fp16=not is_bfloat16_supported(),
        bf16=is_bfloat16_supported(),
        logging_steps=1,
        optim="adamw_8bit",
        weight_decay=0.01,
        lr_scheduler_type="linear",
        seed=3407,
        output_dir="outputs",
    ),
)
trainer.train()
```

From "Tutorial: How to Fine-tune gpt-oss":

```python
from unsloth.chat_templates import standardize_sharegpt
dataset = standardize_sharegpt(dataset)
dataset = dataset.map(formatting_prompts_func, batched = True,)
```

And `formatting_prompts_func` is typically:

```python
def formatting_prompts_func(examples):
    convos = examples["conversations"]
    texts = [tokenizer.apply_chat_template(convo, tokenize = False, add_generation_prompt = False) for convo in convos]
    return { "text" : texts, }
```

Wait, in the gpt-oss tutorial:

```python
To format the dataset, we apply a customized version of the gpt-oss prompt:

from unsloth.chat_templates import standardize_sharegpt
dataset = standardize_sharegpt(dataset)
dataset = dataset.map(formatting_prompts_func, batched = True,)

Let's inspect the dataset by printing the first example:

print(dataset[0]['text'])
```

And earlier:

```python
def formatting_prompts_func(examples):
    convos = examples["conversations"]
    texts = [tokenizer.apply_chat_template(convo, tokenize = False, add_generation_prompt = False) for convo in convos]
    return { "text" : texts, }
pass
```

Wait, let me look at the Qwen3 or gpt-oss tutorial for the exact `formatting_prompts_func`:

From "Qwen3 - How to Run & Fine-tune": It doesn't show the `formatting_prompts_func` explicitly but mentions: "Our Conversational notebook uses a combo of 75% NVIDIA’s open-math-reasoning dataset and 25% Maxime’s FineTome dataset (non-reasoning)."

From "Vision Fine-tuning":

```python
def convert_to_conversation(sample):
    conversation = [
        { "role": "user",
          "content" : [
            {"type" : "text",  "text"  : instruction},
            {"type" : "image", "image" : sample["image"]} ]
        },
        { "role" : "assistant",
          "content" : [
            {"type" : "text",  "text"  : sample["caption"]} ]
        },
    ]
    return { "messages" : conversation }
pass
```

Continue.

Based on the paper "Teaching LLMs to Plan: Logical Chain-of-Thought Instruction Tuning for Symbolic Planning" (PDDL-Instruct framework) and Unsloth's fine-tuning documentation, here is a comprehensive guide on how to train a model using Unsloth for symbolic planning with logical chain-of-thought reasoning.

---

### 1\. Understanding the PDDL-Instruct Framework

The PDDL-Instruct framework enhances LLMs' symbolic planning capabilities by teaching them to rigorously reason about:

- Action applicability and precondition satisfaction
- State transitions and effect application
- Plan validity and invariant preservation

The model is trained using instruction prompts that decompose the planning process into explicit logical reasoning chains, enabling the LLM to self-correct its planning processes through structured reflection.

---

### 2\. Preparing the PDDL-Instruct Dataset for Unsloth

For Unsloth's Supervised Fine-Tuning (SFT), your dataset should follow question/task and answer pairs, where the answer includes the chain-of-thought reasoning process.

A typical PDDL-Instruct dataset entry should include:

- Domain File: PDDL domain definition
- Problem File: PDDL problem definition (initial state and goal)
- Plan File + Explanation: The plan steps along with the logical chain-of-thought reasoning

Example Dataset Entry (Chat/Conversational Format):

```json
{
  "messages": [
    {
      "role": "user",
      "content": "Given the following PDDL domain and problem:\n\n=== DOMAIN ===\n(define (domain blocks)\n  ...\n)\n\n=== PROBLEM ===\n(define (problem blocks-prob)\n  (domain blocks)\n  ...\n)\n\nPlease generate a plan and provide a logical chain-of-thought reasoning about action applicability, state transitions, and plan validity."
    },
    {
      "role": "assistant",
      "content": "Let's reason step by step:\n\n1. **Precondition Satisfaction**: In the initial state, action 'move(A, B, C)' requires that 'A' is clear and 'B' is clear. Checking the initial state...\n2. **Effect Application**: Applying 'move(A, B, C)' results in state S1 where 'A' is on 'C', and 'B' becomes clear.\n3. **Invariant Preservation**: Ensure that no block is on top of two blocks simultaneously...\n...\n**Final Plan**: [move(A, table, B), move(B, table, C), move(A, B, table)]"
    }
  ]
}
```

*Note: If you are fine-tuning a model that already has reasoning capabilities (e.g., DeepSeek-R1 distilled versions or Qwen3), it's recommended to use a mix of 75% reasoning/chain-of-thought examples and 25% non-reasoning examples to make the model retain its general reasoning capabilities.*

---

### 3\. Step-by-Step Unsloth Fine-Tuning Guide

#### Step 1: Install Unsloth and Dependencies

```bash
pip install --upgrade --force-reinstall --no-cache-dir unsloth unsloth_zoo
pip install trl transformers datasets peft
```

#### Step 2: Load the Model and Tokenizer with Unsloth

```python
from unsloth import FastLanguageModel

model_name = "unsloth/llama-3.1-8b-bnb-4bit" # or another suitable base model
max_seq_length = 4096 # PDDL domains/problems can be long, so increase context length

model, tokenizer = FastLanguageModel.from_pretrained(
    model_name = model_name,
    max_seq_length = max_seq_length,
    load_in_4bit = True, # Use 4-bit for memory efficiency, or False for 16-bit
)
```

#### Step 3: Set up LoRA for Fine-tuning

```python
model = FastLanguageModel.get_peft_model(
    model,
    r = 16, # Choose any number > 0: 16, 32, 64, 128, etc.
    target_modules = ["q_proj", "k_proj", "v_proj", "o_proj",
                      "gate_proj", "up_proj", "down_proj",],
    lora_alpha = 16,
    lora_dropout = 0, # Supports any, but = 0 is optimized
    bias = "none",    # Supports any, but = "none" is optimized
    # [NEW] "unsloth" uses 30% less VRAM, fits 2x larger batch sizes!
    use_gradient_checkpointing = "unsloth", # True or "unsloth" for very long context
    random_state = 3407,
    use_rslora = False,  # We support rank stabilized LoRA
    loftq_config = None, # And LoftQ
)
```

#### Step 4: Format the Dataset using Chat Templates

```python
from unsloth.chat_templates import get_chat_template
from datasets import Dataset

# Apply the correct chat template for your model (e.g., llama-3.1, gemma-3, qwen3)
tokenizer = get_chat_template(
    tokenizer,
    chat_template = "llama-3.1", 
)

def formatting_prompts_func(examples):
    convos = examples["messages"]
    texts = [tokenizer.apply_chat_template(convo, tokenize = False, add_generation_prompt = False) for convo in convos]
    return { "text" : texts, }
pass

# Assuming 'dataset' is your Hugging Face Dataset or list of dicts
# dataset = Dataset.from_list(your_data_list)
dataset = dataset.map(formatting_prompts_func, batched = True,)
```

#### Step 5: Train using SFTTrainer

```python
from trl import SFTTrainer
from transformers import TrainingArguments
from unsloth import is_bfloat16_supported

trainer = SFTTrainer(
    model = model,
    tokenizer = tokenizer,
    train_dataset = dataset,
    dataset_text_field = "text",
    max_seq_length = max_seq_length,
    dataset_num_proc = 2,
    packing = False, # Can make training 5x faster for short sequences. Set to True if sequences are short.
    args = TrainingArguments(
        per_device_train_batch_size = 2,
        gradient_accumulation_steps = 4,
        warmup_steps = 5,
        max_steps = 60, # Set to total number of training steps needed
        learning_rate = 2e-4,
        fp16 = not is_bfloat16_supported(),
        bf16 = is_bfloat16_supported(),
        logging_steps = 1,
        optim = "adamw_8bit",
        weight_decay = 0.01,
        lr_scheduler_type = "linear",
        seed = 3407,
        output_dir = "outputs_pddl_instruct",
        report_to = "none", # Use this for WandB etc
    ),
)

trainer_stats = trainer.train()
```

#### Step 6: Save and Deploy the Fine-Tuned Model

```python
# Save the LoRA adapters locally
model.save_pretrained("lora_model_pddl_instruct") # Local save
tokenizer.save_pretrained("lora_model_pddl_instruct")

# Optionally, push to Hugging Face Hub
# model.push_to_hub("your-username/pddl-instruct-lora", token="YOUR_HF_TOKEN")
# tokenizer.push_to_hub("your-username/pddl-instruct-lora", token="YOUR_HF_TOKEN")
```

---

### 4\. Inference / Planning with the Fine-Tuned Model

Once trained, you can use the fine-tuned model to generate logical chain-of-thought plans for new PDDL domains and problems:

```python
# Load model for inference
FastLanguageModel.for_inference(model)

messages = [
    {"role": "user", "content": "Given the following PDDL domain and problem...\nPlease generate a plan and provide a logical chain-of-thought reasoning..."}
]

input_text = tokenizer.apply_chat_template(messages, add_generation_prompt = True)
inputs = tokenizer(
    input_text,
    add_special_tokens = False,
    return_tensors = "pt",
).to("cuda")

from transformers import TextStreamer
text_streamer = TextStreamer(tokenizer, skip_prompt = True)

_ = model.generate(**inputs, streamer = text_streamer, max_new_tokens = 1024,
                   use_cache = True, temperature = 0.7, min_p = 0.1)
```

By following this pipeline, you leverage Unsloth's 2x faster training and 70% less VRAM usage while implementing the PDDL-Instruct logical chain-of-thought instruction tuning framework to significantly improve an LLM's symbolic planning accuracy.