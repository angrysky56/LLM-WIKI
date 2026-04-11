---
title: "romannurik/ProductCanvas-Experiment: A multiplayer collaborative canvas for product brainstorming"
source: "https://github.com/romannurik/ProductCanvas-Experiment"
author:
published:
created: 2026-04-07
description: "A multiplayer collaborative canvas for product brainstorming - romannurik/ProductCanvas-Experiment"
tags:
  - "clippings"
---
## Product Canvas Experiment

A multiplayer collaborative canvas for product brainstorming

👉 [**Read the article**](https://labs.google/code/experiments/product-canvas)

## Building locally

1. Create a Firebase project with Realtime Database and Auth enabled
2. Make a `.env` file at the root, as a copy of [`.env.example`](https://github.com/romannurik/ProductCanvas-Experiment/blob/main/.env.example), filling out the necessary field(s)
3. Install dependencies and start the Vite server:
	```
	$ npm install
	$ npm run dev
	```

## Technical components

- **Infinite canvas** - powered by the excellent [React Flow](http://reactflow.dev/).
- **Realtime multiplayer** - powered by [Firebase Realtime Database](https://firebase.google.com/docs/database) and Auth.
- **Realtime video collaboration** – powered by [WebRTC](https://webrtc.org/) and Firebase for handshake.
- **Assistive voice agent** - powered by the [Gemini Live API](https://ai.google.dev/gemini-api/docs/live)
	- There's also support for wake words (e.g. "Hey Gemini") to start new sessions, but as this is highly unstable and needs to be trained for each user's voice, it's hidden by default.
- **Concept sketch generation** - powered by [🍌 Nano Banana](https://gemini.google/overview/image-generation/)
- **On-the-fly prototype generation** - simplified coding agent powered by Gemini, along with an in-browser runtime powered by [`esbuild-wasm`](https://www.npmjs.com/package/esbuild-wasm) and inspired by [JSNotebook](https://github.com/tschoffelen/jsnotebook).
- **Wiki-style project knowledge editor** - powered by [Tiptap](https://tiptap.dev/)
- **Video calls** unobtrusive, flingable participant video bubbles