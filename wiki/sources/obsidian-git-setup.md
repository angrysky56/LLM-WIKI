---
summary: Setup guide for the Obsidian Git community plugin (desktop and mobile)
tags: [obsidian, git, setup, version-control]
updated: 2026-04-07T22:31:53Z
created: 2026-04-07T22:31:53Z
---

# Obsidian Git Plugin Setup

Source: [Git Documentation - Obsidian Publish](https://publish.obsidian.md/git-doc/Getting+Started)

## Desktop Setup

### New repo from existing vault
1. Install the Git community plugin from Obsidian Settings → Community Plugins
2. Call `Initialize a new repo` command
3. Create first commit via `Commit all changes with specific message`
4. To push to GitHub: set up authentication, ensure remote repo is empty, call `Push` — enter `origin` for name and paste the remote URL

### Clone existing repo
1. Install Git community plugin
2. Set up authentication (GitHub personal access token for HTTPS)
3. Use `Clone an existing remote repository` command, or run `git clone <url>` in terminal
4. Configure `.gitignore` (see Tips & Tricks in docs)

## Mobile

The mobile Git implementation is **unstable**. Alternatives:
- [GitSync](https://github.com/ViscousPot/GitSync) (Android + iOS)
- [Working Copy](https://workingcopy.app/) (iOS, paid)

Mobile limitations: no SSH auth, repo size restricted, no rebase, no submodules.

## Relevance to This Wiki

This vault uses the Obsidian Git plugin to sync to [GitHub](https://github.com/angrysky56/LLM-WIKI). All wiki pages, raw sources, and the CLAUDE.md schema are version-controlled. Destructive edits can be reverted via `git revert`.
