---
summary: SSH command reference: connections, key auth, port forwarding, common options
tags: [linux, ssh, command-line, networking, reference]
updated: 2026-05-07T16:48:57Z
created: 2026-05-07T16:48:57Z
---

# SSH Command in Linux

**Source:** GeeksforGeeks
**Type:** Reference — Linux command reference

## Summary

Reference guide for SSH (Secure Shell) command usage in Linux. Covers basic connection syntax, key-based authentication, port forwarding, and common options.

## Key Commands

- `ssh user@host` — basic connection
- `ssh -p 2222 user@host` — custom port
- `ssh -i ~/.ssh/id_rsa user@host` — key-based auth
- `ssh -L 8080:localhost:80 user@host` — local port forwarding
- `ssh -R 9090:localhost:3000 user@host` — remote port forwarding

## Relevance

Standard reference. SSH is the transport layer for remote development and server administration throughout this ecosystem.
