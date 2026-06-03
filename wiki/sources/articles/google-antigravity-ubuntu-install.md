---
summary: Installation guide for Google Antigravity 2.0 (desktop, IDE, CLI) on Ubuntu 26.04/24.04/22.04 — covers the three current install paths via Google-hosted tarballs and the legacy 1.x APT package; includes update, launch, authentication, and sandbox troubleshooting.
tags: [google-antigravity, ubuntu, install-guide, ide, cli, desktop-app, agy]
updated: 2026-06-03T12:57:02Z
created: 2026-06-03T12:57:02Z
---

---
created: 2026-06-03T00:00:00Z
updated: 2026-06-03T00:00:00Z
type: source
summary: "Installation guide for Google Antigravity 2.0 (desktop, IDE, CLI) on Ubuntu 26.04/24.04/22.04 — covers the three current install paths via Google-hosted tarballs and the legacy 1.x APT package; includes update, launch, authentication, and sandbox troubleshooting."
tags: [google-antigravity, ubuntu, install-guide, ide, cli, desktop-app, agy]
sources:
  - https://linuxcapable.com/how-to-install-google-antigravity-on-ubuntu-linux/
status: reference
confidence: 0.7
---

# Google Antigravity — Ubuntu Install Guide (Antigravity 2.0, IDE, CLI, Legacy 1.x)

**Source**: https://linuxcapable.com/how-to-install-google-antigravity-on-ubuntu-linux/
**Author**: [[Joshua James]]
**Published**: 2025-12-29
**Captured**: 2026-06-02
**Archived**: `Clippings/articles/2026/How to Install Google Antigravity on Ubuntu 26.04, 24.04 and 22.04.md` (52KB)

## What It Is

An installation guide for **Google Antigravity** on Ubuntu 26.04, 24.04, and 22.04. Antigravity is Google's agent-orchestration platform with three current product surfaces (Antigravity 2.0 desktop app, Antigravity IDE, Antigravity CLI) and a legacy 1.x IDE APT package.

## The Four Install Paths

| Path | Best fit | Update method |
| --- | --- | --- |
| **Antigravity 2.0 desktop app** | Current standalone agent platform — projects, artifacts, scheduled work, visual agent orchestration | `sudo update-antigravity` |
| **Antigravity IDE** | Current editor-first IDE — agent manager, artifacts, tab completion, codebase-aware commands | `sudo update-antigravity-ide` |
| **Antigravity CLI** | Terminal-first `agy` workflow — local projects, SSH sessions, scripts, keyboard-driven dev | `agy update` or `update-antigravity-cli` |
| **Legacy Antigravity IDE APT package** | Older package-managed IDE flow when you specifically need the 1.x app | `sudo apt install --only-upgrade antigravity` (only if Google publishes a newer APT package) |

## Critical Caveat on the Legacy Path

The legacy Debian/Ubuntu APT repository still resolves, but its newest package currently stops at `1.23.2`. **Do not use it as the current Antigravity 2.0 install path** unless Google starts publishing a 2.x APT package.

The Antigravity 2.0 desktop helper exposes `antigravity`, while the current IDE helper exposes `antigravity-ide`. The legacy APT package *also* exposes `antigravity` and `antigravity.desktop` — so **remove the legacy package before using the current desktop helper on the same Ubuntu system** to avoid command-name collisions.

## Launch Methods (per surface)

- **Antigravity 2.0**: open from Activities (GNOME launcher)
- **Antigravity IDE**: open from the IDE launcher
- **Antigravity CLI**: start from a terminal with `agy`

## CLI Authentication

The guide covers authenticating the Antigravity CLI on Ubuntu. Specific flow not captured in the excerpt — refer to the source for the current auth steps (they're CLI-driven, browser-paired).

## Update Methods (per surface)

- **Antigravity 2.0 desktop app**: `sudo update-antigravity`
- **Antigravity IDE**: `sudo update-antigravity-ide`
- **Antigravity CLI**: `agy update` or `update-antigravity-cli`
- **Legacy APT**: `sudo apt install --only-upgrade antigravity`

## Troubleshooting (the high-frequency issues)

| Symptom | Cause | Fix |
| --- | --- | --- |
| Antigravity APT still shows 1.23.2 | The APT repo's newest package is 1.23.2 | Switch to the 2.0 desktop helper path or IDE helper path |
| Desktop helper reports Antigravity 2.0.6 already installed | Stale install state in `/opt` or `~/.local` | Clear the stale install; re-run the helper |
| Desktop or IDE helper fails with a 404 | Google's CDN dropped the version; helper fetches by version | Update the helper to the current version |
| Desktop or IDE helper fails because /tmp is too small | Helpers use `/tmp` for the unpack; default `/tmp` is often 1–2GB on Ubuntu | Set `TMPDIR=/var/tmp` or expand `/tmp` |
| Antigravity desktop or IDE version check fails over SSH | Version check needs an X/Wayland session | Run from a desktop session, or skip the version check (helper flag) |

## Connections

- [[entities/tools/google-antigravity]] — entity page (TODO: create)
- [[wiki/sources/repositories/hermes-agent-documentation-hermes-agent]] — comparison: Hermes Agent is a similar category of multi-agent orchestration tool, with different surface area
- [[concepts/cli]] — Antigravity CLI is `agy`; the source of `agy update` / `update-antigravity-cli` distinction is worth flagging (in-binary updater vs system helper)

## Why This Matters

Google Antigravity is a current (Dec 2025) Google product for agent orchestration on Linux. The wiki doesn't have a deep technical page on Antigravity yet — this install guide is a **reference artifact** (a how-to for installation), not an analysis of Antigravity's architecture, capabilities, or competitive position.

The LLM-WIKI is interested in Antigravity as:

- A reference point for how Google positions its agent-orchestration product (vs. Hermes Agent, vs. Claude Code, vs. OpenAI Codex CLI)
- A potential integration target — does Antigravity expose an MCP, CLI, or SDK the LLM-WIKI's agents could call into?
- A data point on the "agent platform" category as of late 2025 / early 2026

## Methodological Note

This is a **tutorial-style install guide**, low in conceptual content but high in operational detail. The pattern: capture the install paths as a reference table, flag the legacy-vs-current bifurcation, capture the high-frequency troubleshooting patterns. Do not over-summarize a tutorial — the *table of paths* is the value; the prose around it is decorative.
