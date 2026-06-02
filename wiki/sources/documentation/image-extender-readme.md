---
summary: image-extender (boona13) README — open-source Next.js 14 web app for AI outpainting (Gemini via OpenRouter) with Poisson-blended seams, plus four game-art studios. Primary source for the existing image-extender entity.
tags: [image-extender, open-source, nextjs, gemini, openrouter, outpainting, poisson-blending, game-art, byok]
updated: 2026-06-02T12:39:33Z
created: 2026-06-02T12:39:33Z
---

---
created: 2026-06-02T00:00:00Z
updated: 2026-06-02T00:00:00Z
type: source
summary: "image-extender (boona13) README — open-source Next.js 14 web app for AI outpainting (Gemini via OpenRouter) with Poisson-blended seams, plus four game-art studios (Parallax, Tiles, Sprites, Props). Primary source for the existing [[image-extender]] entity."
tags: [image-extender, open-source, nextjs, gemini, openrouter, outpainting, poisson-blending, game-art, byok, repositories-source]
sources:
  - https://github.com/boona13/image-extender
status: active
confidence: 0.95
---

# image-extender (boona13) — README

**Source**: `https://github.com/boona13/image-extender` (README.md)
**Captured**: 2026-06-02
**Archived**: `Clippings/documentation/2026/README.md` (29KB, 483 lines)
**Routing note**: The "README" signal in the wiki's auto-router routes this to `documentation/` not `repositories/`. This page lives in `wiki/sources/documentation/` to match the archive location. The content is a GitHub repo README.

## What It Is

A small open-source web app for **AI outpainting** and 2D game-art generation, powered by Google's **Gemini** image models via **OpenRouter**, with a Poisson-blending pipeline that hides the seam between original and AI-generated pixels, plus purpose-built pipelines for tiles, sprites, and props. BYOK (Bring Your Own Key) — the OpenRouter key stays in the user's browser, never on the server.

The five workspaces (switchable from a pill in the top bar):

- **Extender** (default) — outpaint any image in any of four directions, with a best-of-3 seam-quality variant picker
- **Parallax Studio** — build a multi-layer sidescroller background from scratch: Sky / Far / Mid / Near layers, role-aware AI prompts, chroma-keyed transparent layers, live multi-layer scrolling preview, auto-extend to a target width, tileable-loop healing, one-click ZIP export with a JSON manifest
- **Tile Studio** — 13-tile autotile set for 2D platformers (body + 4 edges + 4 outer corners + 4 inner corners) generated in **one** AI call as a 4×4 sprite-sheet, with deterministic corner reconciliation and an AI "art director" QA/repaint loop
- **Sprite Studio** — character & creature animations as a single AI-call sheet, with anatomy-specific pose-guide rigs and engine-ready export
- **Props Studio** — open-ended library of transparent decoration sprites, grown 8 at a time, driven by a two-call "art director → painter" pipeline

## Key Techniques (agent-relevant)

- **Poisson-blended seams** — gradient-domain image editing (Pérez et al. 2003) with mask-grow + replicate-padded Gauss-Seidel iterations to make the AI-original boundary mathematically invisible
- **Pre-correction for low-frequency color drift** — bulk-shifts the AI output toward the original's color at the seam *before* blending, fixing the "sky got slightly bluer" failure mode
- **Best-of-3 variant picker** — every extension generates up to 3 candidates, sorted by seam quality
- **40+ custom art styles** — cinematic, oil painting, Studio Ghibli, cyberpunk, vaporwave, etc.
- **Keyboard-first** — arrow keys to extend, `←/→` to cycle variants, `Enter` to accept, `R` to regenerate, `Esc` to discard
- **BYOK (Bring Your Own Key)** — OpenRouter key stored only in browser `localStorage`; server proxies requests without logging the key
- **Model picker** — Gemini 3 Pro Image (Nano Banana Pro), Gemini 3 Flash Image (Nano Banana 2), Gemini 2.5 Flash Image (Nano Banana) from Settings

## Connections

- [[entities/tools/image-extender]] — full entity page with deep integration analysis (Ty's existing note)
- [[cartridge-forge]] — natural consumer of the four game-art studios (mapped 1:1 in the entity page)
- [[wiki/index]]

## Provenance

This README is the primary source for the [[entities/tools/image-extender|existing entity page]] (which was created 2026-06-01 from a separate fetch). The README was placed in `raw/` on 2026-06-01 10:17 UTC, ingested 2026-06-02, archived to `Clippings/documentation/2026/README.md` (the README routing signal goes to `documentation/`, not `repositories/`). The entity page should be considered canonical for analysis; this source page is the primary-source archive of the README itself.
