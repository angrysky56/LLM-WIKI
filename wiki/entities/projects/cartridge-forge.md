---
summary: Ty's ECS-based turn-based game generator — declarative DSL, Zod-validated Cartridge JSON, multi-agent pipeline (Map Architect / Mechanics Designer / Lore Weaver). Natural integration partner with image-extender.
tags: [projects, game-gen, ecs, typescript, agent-pipeline, zod, dsl, vite]
updated: 2026-06-01T16:26:13Z
created: 2026-06-01T16:26:13Z
---

---
title: cartridge-forge
summary: Ty's ECS-based turn-based game generator. Declarative DSL + Zod-validated Cartridge JSON + multi-agent (Map Architect / Mechanics Designer / Lore Weaver) pipeline.
tags: projects, game-gen, ecs, typescript, agent-pipeline, zod, dsl
---

# Cartridge Forge

AI-driven turn-based game generator using ECS architecture and a declarative DSL.

**Repo:** `/home/ty/Repositories/ai_workspace/cartridge-forge/`
**Stack:** TypeScript, Vite, Zod, expr-eval (forked). WebGL renderer, C64 color palette.
**Status:** Milestone 2 (Agent Forge) ~90% complete. Milestone 3 (RTA + Sensory) is roadmap.

## Architecture

```
User describes game
        ↓
   Forgemaster Agent coordinates specialized skills (Map, Mechanics, Lore)
        ↓
   AI generates Cartridge JSON (ECS data + expression rules)
        ↓
   Zod schema validation (catch errors before runtime)
        ↓
   Browser runtime loads cartridge → playable game
        ↓
   User feedback → AI patches cartridge → hot-reload
```

## Core Concepts

### The "Cartridge" (AI Output)
A JSON file conforming to a strict Zod schema. Contains:
- **Components** — pure data bag type definitions
- **Blueprints** — entity templates (component bundles with values)
- **Systems** — declarative rules using a constrained expression DSL
- **World Gen** — procedural map generation configuration
- **Traits** — genetic inheritance weighting for the breeding system

### The Expression DSL
A constrained language for game logic that AI can generate reliably:
- Math expressions: `"max(1, attacker.CombatStats.strength - target.CombatStats.armor)"`
- Built-ins: `distance()`, `roll()`, `has_tag()`, `has_component()`, `max()`, `min()`
- Safe eval via `expr-eval` (no `eval()`, no arbitrary code)

### Effect Types (exhaustive)
| Type | Description |
|------|-------------|
| `MUTATE` | Change a component value (ADD/SUBTRACT/SET/MULTIPLY) |
| `DESTROY_ENTITY` | Remove an entity |
| `SPAWN_ENTITY` | Create entity from blueprint |
| `APPLY_TAG` | Add a temporary tag (e.g. "stunned") |
| `REMOVE_TAG` | Remove a tag |
| `LOG_MESSAGE` | Push to combat log (template strings) |
| `EMIT_EVENT` | Chain events (with loop protection) |
| `BREED_ENTITY` | Create a hybrid offspring from two parents |
| `EQUIP_ITEM` | Attach an item and apply its modifiers |
| `UNEQUIP_ITEM` | Remove an item and strip its modifiers |

## Agent Skill Pipeline

Forgemaster coordinates three specialized skills in `.forge/`:
- **Map Architect** — procedural world generation
- **Mechanics Designer** — systems and balance
- **Lore Weaver** — narrative and aesthetic

Iterative refinement: Agent-to-Agent feedback in Forgemaster instructions, Fragment merging + Zod validation in Forge CLI.

## Rendering Modes

- **2D Grid** — discrete grid with tile-based assets
- **Wireframe 3D** — vector-based 3D projection
- **Pseudo-3D (C64-style)** — raycaster-style from-disk

## Cartridges Shipped

- `crawler_demo.json` — basic dungeon crawler
- `abyssal_protocol.json` — deep-sea themed (this is the most-developed one visually)
- `wireframe_demo.json` — wireframe 3D demo
- `rpg_test.json`, `gladiator_gen.json` — additional test cartridges

## Roadmap Status

- [x] Milestone 1: Core Runtime (ECS, WebGL, Cartridge loader, DSL, RPG mechanics)
- [x] Milestone 2: Agent Forge (skill folders, Forgemaster, end-to-end pipeline) — **Phase 6 verification/validation still open**
- [ ] Milestone 3: Real-Time Action & Sensory (continuous time, FOV/lighting, audio)

## See Also

- [[image-extender]] — natural integration partner. The 5 image-extender studios (Tile / Sprite / Parallax / Props / Extender) map almost 1:1 to cartridge-forge's visual needs. See that page for the integration plan.
