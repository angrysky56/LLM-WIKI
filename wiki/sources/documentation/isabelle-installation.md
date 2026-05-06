---
summary: Official installation guide for Isabelle2025-2.
tags: [isabelle, installation, formal-methods]
updated: 2026-05-06T20:06:20Z
created: 2026-05-06T20:06:20Z
---

---
created: 2026-05-06T20:06:15Z
updated: 2026-05-06T20:06:15Z
type: source
summary: Official installation guide for Isabelle2025-2 across Linux, Windows, and macOS.
tags: [isabelle, formal-methods, installation]
sources: https://isabelle.in.tum.de/installation.html
status: reference
confidence: 1.0
---

# Isabelle Installation

Comprehensive guide for setting up [[isabelle|Isabelle2025-2]] on major platforms.

## Summary

Isabelle supports Linux, Windows, and macOS, providing platform-specific bundles that include sources, documentation, and components.

### Platform Specifics
- **Docker**: Headless Ubuntu Linux image available for command-line access.
- **Linux**: Requires a window manager compatible with Java/AWT/Swing and TeXLive for document preparation.
- **Windows**: Provided as a self-extracting archive; requires MikTeX. Note that it may require security exclusions in Windows Defender for external provers like [[sledgehammer]].
- **macOS**: Requires MacTeX. Installation involves manual security bypass in "Security & Privacy" as the app is not notarized.

## Connections
- Tool: [[isabelle]]
- Concept: [[formal-verification]]
- Dependency: [[java]]
- Dependency: [[latex]]
