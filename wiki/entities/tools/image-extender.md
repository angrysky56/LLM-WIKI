---
summary: Open-source Next.js app for AI outpainting (Gemini via OpenRouter) with Poisson blending, plus 4 game-art studios (Parallax, Tiles, Sprites, Props). Ty's hook: agent could use for visual thought exploration.
tags: [tools, image, ai, open-source, game-art, gemini, byok, nextjs]
updated: 2026-06-01T16:17:13Z
created: 2026-06-01T16:17:13Z
---

---
title: image-extender (boona13)
summary: Open-source Next.js web app — AI outpainting (Gemini via OpenRouter) with Poisson-blended seams, plus 4 game-art studios (Parallax, Tiles, Sprites, Props).
tags: tools, image, ai, open-source, game-art, gemini
source: https://github.com/boona13/image-extender
fetched: 2026-06-01
---

# image-extender (boona13)

> Ty's note: "vague thought an agent could use this for visuals and exploration of thoughts."

## What it is

A small open-source **Next.js 14** web app that does AI outpainting and 2D game-art generation, powered by Google's Gemini image models via OpenRouter. ~13.5K LOC, MIT-licensed, 263★ / 34 forks.

**Repo:** https://github.com/boona13/image-extender
**Stack:** Next.js 14 (App Router), React 18, TypeScript, Tailwind, OpenRouter → Gemini (Nano Banana Pro / 2 / 1)
**BYOK** — key stored in `localStorage`, server is a stateless proxy.

## Five workspaces in one app

1. **Extender** (default) — outpaint any image in any of 4 directions, best-of-3 seam-quality variant picker.
2. **Parallax Studio** — multi-layer sidescroller backgrounds (Sky / Far / Mid / Near), chroma-keyed transparent layers, live multi-layer scroll preview, auto-extend to target width, tileable-loop healing, ZIP + JSON manifest export.
3. **Tile Studio** — 13-tile autotile set (body + 4 edges + 4 outer corners + 4 inner corners) in **one** AI call as a 4×4 sprite-sheet, deterministic corner reconciliation, AI art-director QA/repaint loop, 14 material presets.
4. **Sprite Studio** — character animations as a single AI-call sheet. 5 body plans (humanoid, quadruped, serpent, flyer, blob), anatomy-specific pose-guide rigs, scale normalization, baseline alignment, twin-detector, engine-ready export (sheet + strip + per-frame ZIP).
5. **Props Studio** — open-ended, ever-growing library of decoration sprites, 8 at a time via two-call art-director→painter pipeline, 8 biome presets, atlas + ZIP export with descriptive names.

## The interesting techniques (agent-relevant)

- **Poisson blending** (`app/utils/imageProcessor.ts`, ~3.5K LOC) — gradient-domain image editing (Pérez 2003) with mask-grow + replicate-padded Gauss-Seidel. Used to make the AI-original boundary mathematically invisible.
- **Pre-correction for low-frequency color drift** — bulk-shifts AI output toward original's color at the seam *before* blending. Fixes the "sky got slightly bluer" failure mode of outpainting.
- **Best-of-N variant picker** — every extension generates up to 3 candidates, sorted by seam quality, cycle with arrow keys.
- **Two-pass anchor → sheet** for sprites — generate a single neutral reference image first, then attach it as a "canonical character" reference for the keyframe sheet. The single biggest lever for cross-frame identity preservation.
- **Anatomy-specific pose-guide rigs** — deterministic code-generated "ControlNet-style" mannequins drawn fresh per body plan × action, fed as structural reference.
- **AI "art director" QA loop** — vision critic reviews composited output and returns a fix report that drives a repaint, with keep-best selection (loop can only improve, never regress).
- **Deterministic twin detector** — pixel-level morphological-opening pass that splits fused duplicates, forces repaint on duplicates. No vision model needed → fast.
- **Role-aware AI prompts for parallax** — Far/Mid/Near get rendered on flat magenta (`#FF00FF`), client keys to alpha. Layer compositing is just alpha-over.
- **Auto-extend to target width** — repeatedly extends the active layer, auto-accepts best variant, re-applies chroma-keying, stops at target. `Tileable` button auto-runs at end.

## File map

```
app/
  api/extend/route.ts            # 386 LOC — core outpaint
  api/generate/route.ts           # 1359 LOC — text-to-image + variants
  api/tile-review/route.ts        # 187 LOC — vision critic
  api/sprite-review/route.ts      # 309 LOC
  api/scene-brief/route.ts        # 126 LOC — shared project context
  api/prop-brief/route.ts         # 216 LOC — art-director ideation
  lib/{tileset,sprite,parallax,props,bodyPlans,artStyles,models,app}.ts
  utils/imageProcessor.ts         # 3459 LOC — Poisson, chroma key, scale norm, alignment
  utils/{poseRig,rigCore}.ts      # deterministic mannequin generators
  utils/rigs/{biped,quadruped,serpent,flyer,blob}.ts
  components/{Workspace,TopBar,CommandBar,VariantSelector,Modals,
              ParallaxStudio,SpriteStudio,TileStudio,PropStudio,EmptyState,icons}.tsx
```

## How an agent could use this

- **Mind-mapping / thought exploration** — Ty's stated hook. The Extender workspace lets you "grow" a starting visual in any direction while keeping stylistic continuity. Could seed with a concept image, extend into adjacent idea-space.
- **Scene brief propagation** — `scene-brief` API distills a setting/time/palette/mood once, then Parallax/Tiles/Sprites/Props all reuse it so a whole world feels coherent. This is the "explore a thought" loop: lock a brief, mutate it across modalities.
- **Image generation with constraints** — template-guided image-to-image (Tiles), role-aware prompts (Parallax), anchor+sheet (Sprites) are all constraint patterns useful for any "make me X that matches my existing Y" task.
- **Image-to-image as a service** — the BYOK + server-proxy pattern is reusable. Just point at your own OpenRouter key.

## Open questions / follow-up

- **Integration with [[cartridge-forge]]** — see below. The five studios in this app are almost a turn-key art pipeline for cartridge-forge's 2D grid / pseudo-3D modes.
- Can the Extender be driven headless from an agent? The UI is React; the API routes are Next.js. An agent would call the same routes directly with BYOK.
- Is the `scene-brief` / `prop-brief` "reasoning model" pattern worth lifting into the wiki-overseer or librarian agents? (Reuse existing reasoning model to decide *what* to write, then image model to render.)
- Active project, 5 commits in 1 week. Worth a kanban card to revisit in a month.

## Integration with cartridge-forge

[[cartridge-forge]] is Ty's ECS-based turn-based game generator — declarative DSL, Zod-validated Cartridge JSON files, multi-mode rendering (2D Grid, Wireframe 3D, C64-style). It currently ships 3 demo cartridges (`crawler_demo.json`, `abyssal_protocol.json`, `wireframe_demo.json`) and has a Map Architect / Mechanics Designer / Lore Weaver multi-agent pipeline for generating new cartridges from a prompt.

**The natural integration:** the 5 image-extender studios map almost 1:1 to cartridge-forge's visual needs.

| cartridge-forge need | image-extender studio | What it produces |
|---|---|---|
| 2D Grid mode tile set | **Tile Studio** | 13-tile autotile set (body + 4 edges + 4 outer + 4 inner corners) as one AI call, deterministic corner reconciliation, engine-ready atlas with 2px extrude border. 14 material presets. |
| Character / creature animations | **Sprite Studio** | Keyframe sheets across 5 body plans (humanoid, quadruped, serpent, flyer, blob), anatomy-specific pose rigs, scale normalization, baseline alignment, twin-detector. |
| Parallax background | **Parallax Studio** | 4-layer Sky/Far/Mid/Near with chroma-keyed transparency, live multi-layer scroll preview, ZIP + `parallax.json` manifest drop-in for Unity/Godot/Phaser. |
| Scatter decoration props | **Props Studio** | Open-ended transparent library grown 8-at-a-time, two-call art-director→painter pipeline, atlas + descriptive-named ZIP. |
| Concept art / mood board for a cartridge | **Extender** | Best-of-3 variant picker with Poisson-blended seam continuation. Seed with one image, grow in any direction. |

**The pattern that makes this viable for agents:** both projects are JSON-pipeline-first. cartridge-forge already treats Cartridge JSON as the AI's output; image-extender's API routes (`/api/extend`, `/api/generate`, `/api/scene-brief`, `/api/prop-brief`) return images that an agent can pack into a sidecar `art.json` for the cartridge. The cartridge schema could grow a new `art` section that references exported assets:

```jsonc
{
  "name": "Abyssal Protocol",
  "components": { ... },
  "art": {
    "tileset":   "atlas://tileset-meadow.png",      // from Tile Studio export
    "sprites":   "atlas://sprite-anglerfish.png",   // from Sprite Studio export
    "parallax":  "atlas://parallax-deep-sea/",      // ZIP with manifest
    "props":     "atlas://props-deep-sea.json"      // Props Studio atlas + manifest
  }
}
```

**Forgemaster angle:** cartridge-forge's Map Architect / Mechanics Designer / Lore Weaver skills could grow a fourth sibling — **Art Director** — that drives image-extender's studios from a `scene-brief`. The art-director→painner two-call pattern (used in Props Studio) is the same pattern that cartridge-forge's multi-agent flow already uses for ideation (Lore Weaver proposes, Mechanics Designer implements). Pluggable.

**Concrete next step:** spawn a kanban card to wire up the simplest path — Tile Studio output → cartridge-forge 2D Grid mode. One cartridge, one tile set, end-to-end demo. Validates the schema and the agent handoff before building the rest.

**Ty's storage convention**: Repos go in `/home/ty/Repositories/` unless they are Ty's own or a fork. This fork lives at `/home/ty/Repositories/ai_workspace/image-extender/` (forked 2026-06-01).
**Local mirror:** none — only the fork.
