---
title: "Installation"
source: "https://isabelle.in.tum.de/installation.html"
author:
  - "[[Tobias Nipkow]]"
  - "[[Lawrence Paulson]]"
  - "[[Makarius Wenzel]]"
  - "[[Gerwin Klein]]"
  - "[[Florian Haftmann]]"
  - "[[Tjark Weber]]"
  - "[[Johannes Hölzl]]"
published:
created: 2026-05-05
description:
tags:
  - "clippings"
---
## General

Isabelle supports the three main platform families: Linux, Windows, macOS. The platform-specific application bundles include sources, documentation, and add-on components. A few extra dependencies are explained below. There is also a self-contained Docker image (without GUI support).

Individual Isabelle [distribution files](https://isabelle.in.tum.de/dist/index.html) are available for reference: in practice it is sufficient to download the main "apps" below. Past releases are available from the [distribution archive](https://isabelle.in.tum.de/download_past.html). Further technical background information may be found in the [Isabelle System Manual](https://isabelle.in.tum.de/dist/Isabelle2025-2/doc/system.pdf).

## Docker: Headless Ubuntu Linux

### Requirements

- [Docker container](https://www.docker.com/) for the host operating system
- [Docker image](https://hub.docker.com/r/makarius/isabelle) for Isabelle

### Installation

The Docker image contains Ubuntu Linux 22.04 with Isabelle2025-2. It can be used, e.g. on another Linux host like this:

- docker pull makarius/isabelle:Isabelle2025-2
- docker run makarius/isabelle:Isabelle2025-2

That provides command-line access to the regular `isabelle` tool wrapper, with indirection through the Docker container infrastructure.

The default platform is Intel x86\_64, but ARM is supported as well (e.g. for Apple M1):

- docker pull makarius/isabelle:Isabelle2025-2\_ARM
- docker run makarius/isabelle:Isabelle2025-2\_ARM

## Linux

### Requirements

- [Isabelle2025-2\_linux.tar.gz](https://isabelle.in.tum.de/dist/Isabelle2025-2_linux.tar.gz)
- Proper Window manager / Desktop environment that works with Java/AWT/Swing
- TeXLive for Isabelle/LaTeX document preparation

### Installation

The bundled archive contains everything required for Isabelle on Linux. It can be unpacked into an arbitrary directory like this:

- tar -xzf Isabelle2025-2\_linux.tar.gz

The Isabelle/jEdit Prover IDE can be invoked like this:

- Isabelle2025-2/Isabelle2025-2

Other Isabelle command-line tools can be invoked from the terminal like this:

- Isabelle2025-2/bin/isabelle

## Windows (10, 11)

### Requirements

- [Isabelle2025-2.exe](https://isabelle.in.tum.de/dist/Isabelle2025-2.exe)
- [MikTeX](https://www.ctan.org/tex-archive/systems/win32/miktex) for Isabelle/LaTeX document preparation

### Installation

The self-extracting archive contains everything required for Isabelle on Windows PCs. It can be unpacked into an arbitrary directory. The installer starts the Isabelle/jEdit Prover IDE automatically for the first time. It also creates a desktop alias to the main executable for later use.

Isabelle2025-2\\Cygwin-Terminal allows to run Isabelle command-line tools, as known from Unix.

Isabelle2025-2\\Cygwin-Setup allows to modify the Cygwin installation of Isabelle, e.g. to add further packages manually.

**Note:** The Isabelle application lacks developer signatures and certificates, so Microsoft rejects it by default. Running it for the first time requires some careful clicks in the proper spots.

**Note:** The Windows 10 Defender may prevent external provers from working properly (e.g. for **sledgehammer** or the *smt* proof method). In that case the whole Isabelle application directory should be [excluded from Virus & threat protection](https://support.microsoft.com/en-us/help/4028485/windows-10-add-an-exclusion-to-windows-security).

## macOS (12, 13, 14, 15, 26 — Intel or Apple Silicon)

### Requirements

- [Isabelle2025-2\_macos.tar.gz](https://isabelle.in.tum.de/dist/Isabelle2025-2_macos.tar.gz)
- [MacTeX](https://www.tug.org/mactex/) for Isabelle/LaTeX document preparation

### Installation

The bundled archive contains everything required for Isabelle on Macintosh computers. The Isabelle application can be placed into the `/Applications` folder and started as usual.

**Note:** The Isabelle application lacks developer signatures and certificates, so Apple rejects it by default. See also the document [Safely open apps on your Mac](https://support.apple.com/en-us/guide/mac-help/mh40616/mac), notably the last section *"How to open an app that hasn’t been notarized or is from an unidentified developer".* In short, it should work with the default security settings as follows:

1. **Open** `Isabelle2025-2.app` and **Cancel** the subsequent security dialog.
2. **Open Security & Privacy** in system preferences: section *"Allow apps..."* at the bottom should list the blocked application (see [screenshot](https://isabelle.in.tum.de/img/macos_security.png)).
3. Click **Open Anyway** and provide further confirmations as required.