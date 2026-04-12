---
summary: Google Labs multiplayer brainstorming canvas with AI voice agent and wiki knowledge editor
tags: [collaboration, AI, brainstorming, Google, canvas]
type: source
sources: https://github.com/romannurik/ProductCanvas-Experiment
status: reference
updated: 2026-04-11T00:00:00Z
created: 2026-04-07T22:32:36Z
---

# Product Canvas Experiment (Google Labs)

Source: [github.com/romannurik/ProductCanvas-Experiment](https://github.com/romannurik/ProductCanvas-Experiment)

## What It Is

A multiplayer collaborative canvas for product brainstorming, combining real-time collaboration with AI assistance.

## Technical Stack

- **Infinite canvas** — React Flow
- **Realtime multiplayer** — Firebase Realtime Database + Auth
- **Video collaboration** — WebRTC with Firebase handshake
- **Voice agent** — Gemini Live API (with experimental wake word support)
- **Concept sketches** — Nano Banana (Gemini image generation)
- **Prototype generation** — simplified coding agent + in-browser runtime via esbuild-wasm
- **Wiki-style knowledge editor** — Tiptap
- **Video calls** — unobtrusive flingable participant bubbles

## Relevance to This Wiki

Demonstrates the convergence of real-time collaboration + AI + persistent knowledge (wiki editor). The "wiki-style project knowledge editor" component is exactly the pattern described in [[persistent-knowledge-compilation|Persistent Knowledge Compilation]] — a persistent artifact that accumulates project context.

This is what a team-facing version of the [[llm-wiki-pattern|LLM Wiki Pattern]] could look like: multiplayer, visual, with AI agents participating alongside humans.
