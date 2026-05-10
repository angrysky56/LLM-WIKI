---
title: "Free Models Router - Zero-Cost AI Inference"
source: "https://openrouter.ai/docs/guides/routing/routers/free-router"
author:
published:
created: 2026-05-09
description: "Get free AI inference by routing to available free models"
tags:
  - "clippings"
---
The [Free Models Router](https://openrouter.ai/openrouter/free) (`openrouter/free`) automatically selects a free model at random from the available free models on OpenRouter. The router intelligently filters for models that support the features your request needs, such as image understanding, tool calling, and structured outputs.

## Overview

Instead of manually choosing a specific free model, let the Free Models Router handle model selection for you. This is ideal for experimentation, learning, and low-volume use cases where you want zero-cost inference without worrying about which specific model to use.

To try the Free Models Router without writing any code, see the [Chat Playground guide](https://openrouter.ai/docs/cookbook/get-started/free-models-router-playground).

## Usage

Set your model to `openrouter/free`:

```
1import requests
2import json
3
4response = requests.post(
5  url="https://openrouter.ai/api/v1/chat/completions",
6  headers={
7    "Authorization": "Bearer <OPENROUTER_API_KEY>",
8    "Content-Type": "application/json",
9  },
10  data=json.dumps({
11    "model": "openrouter/free",
12    "messages": [
13      {
14        "role": "user",
15        "content": "Hello! What can you help me with today?"
16      }
17    ]
18  })
19)
20
21data = response.json()
22print(data['choices'][0]['message']['content'])
23# Check which model was selected
24print('Model used:', data['model'])
```

## Response

The response includes the `model` field showing which free model was actually used:

```json
1{
2  "id": "gen-...",
3  "model": "upstage/solar-pro-3:free",
4  "choices": [
5    {
6      "message": {
7        "role": "assistant",
8        "content": "..."
9      }
10    }
11  ],
12  "usage": {
13    "prompt_tokens": 12,
14    "completion_tokens": 85,
15    "total_tokens": 97
16  }
17}
```

## How It Works

1. **Request Analysis**: Your request is analyzed to determine required capabilities (e.g., vision, tool calling, structured outputs)
2. **Model Filtering**: The router filters available free models to those supporting your request’s requirements
3. **Random Selection**: A model is randomly selected from the filtered pool
4. **Request Forwarding**: Your request is forwarded to the selected free model
5. **Response Tracking**: The response includes metadata showing which model was used

## Available Free Models

The Free Models Router selects from all currently available free models on OpenRouter. Some popular options include:

Free model availability changes frequently. Check the [models page](https://openrouter.ai/models?pricing=free) for the current list of free models.

- **DeepSeek R1 (free)** - DeepSeek’s reasoning model
- **Llama models (free)** - Various Meta Llama models
- **Qwen models (free)** - Alibaba’s Qwen family
- And other community-contributed free models

## Pricing

The Free Models Router is completely free. There is no charge for:

- Using the router itself
- Requests routed to free models

## Use Cases

- **Learning and experimentation**: Try AI capabilities without any cost
- **Prototyping**: Build and test applications before committing to paid models
- **Low-volume applications**: Suitable for personal projects or demos
- **Education**: Perfect for students and educators exploring AI

## Limitations

- **Rate limits**: Free models may have lower rate limits than paid models
- **Availability**: Free model availability can vary; some may be temporarily unavailable
- **Performance**: Free models may have higher latency during peak usage
- **Model selection**: You cannot control which specific model is selected (use the `:free` variant suffix on a specific model if you need a particular free model)

## Selecting Specific Free Models

If you prefer to use a specific free model rather than random selection, you can:

1. **Use the `:free` variant**: Append `:free` to any model that has a free variant:
	```json
	1{
	2  "model": "meta-llama/llama-3.2-3b-instruct:free"
	3}
	```
2. **Browse free models**: Visit the [models page](https://openrouter.ai/models?pricing=free) to see all available free models and select one directly.

## Related

- [Free Models Router in Chat Playground](https://openrouter.ai/docs/cookbook/get-started/free-models-router-playground) - Try the router without writing code
- [Free Variant](https://openrouter.ai/docs/guides/routing/model-variants/free) - Use the `:free` suffix for specific models
- [Auto Router](https://openrouter.ai/docs/guides/routing/routers/auto-router) - Intelligent model selection (paid models)
- [Latest Model Resolution](https://openrouter.ai/docs/guides/routing/routers/latest-resolution) - Always target the newest version of a model family
- [Body Builder](https://openrouter.ai/docs/guides/routing/routers/body-builder) - Generate multiple parallel API requests
- [Model Fallbacks](https://openrouter.ai/docs/guides/routing/model-fallbacks) - Configure fallback models