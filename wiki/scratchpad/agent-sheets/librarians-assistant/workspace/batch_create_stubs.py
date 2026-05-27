#!/usr/bin/env python3
"""Batch create entity stubs for librarians-assistant kanban items."""
import sqlite3, hashlib, uuid, time, os

DB = sqlite3.connect(os.path.expanduser("~/.hermes/kanban.db"))

# Check existing open tasks for our items
cur = DB.execute("SELECT id, title, status FROM tasks WHERE status != 'done' AND assignee = 'librarians-assistant'")
rows = cur.fetchall()
print("Current librarians-assistant open tasks:")
for r in rows: print(f"  {r[0]} | {r[1][:60]} | {r[2]}")

print("\nDone.")