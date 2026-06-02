#!/usr/bin/env python3
"""
carryover_stale_sweep.py — Cross-check an agent carryover's "## What Remains"
list against the live kanban.db state.

For each item in the carryover's "What Remains" / "Still Open" / "Open" section:
  - If a matching task exists in kanban with status 'done' or 'archived' → mark
    it as resolved in-place: strikethrough + add "(verified done YYYY-MM-DD, t_xxx)"
  - If a matching task exists with status ready/in_progress/blocked → leave as-is
  - If no matching task exists → leave as-is (genuinely open)

This is the binding Step 1b from the kanban-review skill, but executed as code
at end-of-cycle rather than as prose at start-of-review. Catches the
"carryover says (Pending) but it's been done in kanban for 3 days" pattern
that the morning overseer report has been flagging repeatedly.

Matching: by title fragment. The carryover item is parsed line-by-line; the
leading "- [ ] " or "- [x] " is stripped, then the line is searched against
kanban titles (and, if no direct title hit, against an inferred keyword
extracted from the line — see keyword heuristics below).

Usage:
  python3 carryover_stale_sweep.py <agent> [--dry-run] [--no-write]

  agent: arxiv | news | insights | ingest | librarian | librarians-assistant |
         researcher | overseer
  --dry-run: print proposed edits without modifying the file
  --no-write: same as --dry-run (alias)
"""
import argparse
import os
import re
import sqlite3
import sys
from datetime import datetime, timezone

KANBAN_DB = os.path.expanduser("~/.hermes/kanban.db")
CARRYOVER_ROOT = "/home/ty/Documents/LLM-WIKI/wiki/scratchpad/agent-sheets"
SECTION_HEADERS = ("## What Remains", "## Still Open", "## Open Questions", "## Open")

# Lines we want to consider as open items: markdown list items under one of
# the SECTION_HEADERS, starting with "- [ ]" or "- [x]" or "- " (some carryovers
# drop the checkbox).
ITEM_RE = re.compile(r"^\s*-\s+\[(?P<box>[ xX])\]\s+(?P<body>.+)$")
PLAIN_ITEM_RE = re.compile(r"^\s*-\s+(?P<body>[^\[\s].+)$")


def load_kanban():
    """Return (done_index, open_index) where each is dict mapping title-keyword
    -> (id, status, title). Use a separate set of full token-sets for fuzzy
    intersection matching."""
    if not os.path.exists(KANBAN_DB):
        return {}, {}, set(), set()
    conn = sqlite3.connect(KANBAN_DB)
    done, open_ = {}, {}
    done_tokens, open_tokens = set(), set()  # for intersection matching
    for row in conn.execute("SELECT id, title, status FROM tasks"):
        tid, title, status = row
        tokens = _tokens(title)
        kw = _keyword(title)
        if not kw:
            continue
        if status in ("done", "archived"):
            done.setdefault(kw, []).append((tid, status, title))
            done_tokens.add(frozenset(tokens))
        else:
            open_.setdefault(kw, []).append((tid, status, title))
            open_tokens.add(frozenset(tokens))
    conn.close()
    return done, open_, done_tokens, open_tokens


def _tokens(text):
    """All content tokens from a title (for set-intersection matching)."""
    if not text:
        return set()
    t = text.strip()
    if ":" in t:
        prefix, rest = t.split(":", 1)
        if prefix.strip().lower() in {
            "arxiv", "news", "insights", "ingest", "librarian",
            "librarians-assistant", "researcher", "overseer",
        }:
            t = rest.strip()
    t = re.sub(r"^\(([^)]+)\)\s*", "", t).strip()
    t = re.sub(r"[^a-z0-9\s]", " ", t.lower())
    return {w for w in t.split() if len(w) > 2}


def _keyword(text):
    """Extract a 4+-word fragment from a title for fuzzy matching.

    Skips agent prefixes ("arxiv:", "news:") and short stopwords.
    The fragment is lowercased and stripped of non-alphanumeric.
    """
    if not text:
        return None
    t = text.strip()
    # Strip leading "agent-name:" prefix if present
    if ":" in t:
        prefix, rest = t.split(":", 1)
        if prefix.strip().lower() in {
            "arxiv", "news", "insights", "ingest", "librarian",
            "librarians-assistant", "researcher", "overseer",
        }:
            t = rest.strip()
    # Strip parenthetical status prefixes like "(Optional)" "(Pending)"
    t = re.sub(r"^\(([^)]+)\)\s*", "", t).strip()
    # Lowercase, remove punctuation
    t = re.sub(r"[^a-z0-9\s]", " ", t.lower())
    # Drop short stopwords
    stops = {"a", "an", "and", "or", "the", "of", "to", "for", "in", "on",
             "is", "be", "with", "by", "as", "at", "from", "this", "that",
             "create", "add", "page", "wiki", "synthesis"}
    tokens = [w for w in t.split() if w and w not in stops and len(w) > 2]
    if len(tokens) < 3:
        return None
    return " ".join(tokens[:8])  # 8-token window is robust against rewording


def find_section_end(lines, start_idx):
    """Return the index of the next H2 header at or after start_idx, or len(lines)."""
    for i in range(start_idx, len(lines)):
        if lines[i].startswith("## ") and i != start_idx:
            return i
    return len(lines)


def sweep(carryover_path, dry_run=False):
    with open(carryover_path, "r", encoding="utf-8") as f:
        text = f.read()
    lines = text.split("\n")
    done_index, open_index, done_tokens, open_tokens = load_kanban()

    edits = []  # list of (line_no, old, new)
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")

    for hdr in SECTION_HEADERS:
        if hdr not in lines:
            continue
        start = lines.index(hdr)
        end = find_section_end(lines, start)
        for i in range(start + 1, end):
            line = lines[i]
            m = ITEM_RE.match(line) or PLAIN_ITEM_RE.match(line)
            if not m:
                continue
            body = m.group("body").strip()
            if body.startswith("(resolved") or "verified done" in body.lower():
                continue  # already swept
            kw = _keyword(body)
            if not kw:
                continue
            match = None
            # First check: same keyword in done/archived
            direct_match = done_index.get(kw)
            if direct_match:
                # First (most recent) task with this keyword
                match = direct_match[0]
            # If no direct hit, the carryover line may bundle multiple tasks
            # separated by ", " or "; " — try splitting on those and matching
            # each segment individually. If ALL segments resolve, mark the
            # whole line as resolved. Try this BEFORE whole-line Jaccard
            # because bundled lines have noise that tanks the score.
            if not match and (", " in body or "; " in body):
                segments = re.split(r"(?<!^)[,;]\s+(?=[A-Z])", body)
                if len(segments) > 1:
                    seg_matches = []
                    for seg in segments:
                        seg = seg.strip().rstrip(".")
                        seg_kw = _keyword(seg)
                        if not seg_kw:
                            break
                        seg_match = None
                        direct = done_index.get(seg_kw) or open_index.get(seg_kw)
                        if direct:
                            seg_match = direct[0]
                        if not seg_match:
                            seg_tokens = set(seg_kw.split())
                            if seg_tokens:
                                best_sim = 0.0
                                best_kt = None
                                for kt in done_tokens | open_tokens:
                                    if not kt:
                                        continue
                                    sim = len(seg_tokens & kt) / len(seg_tokens | kt)
                                    if sim > best_sim:
                                        best_sim = sim
                                        best_kt = kt
                                if best_sim >= 0.3 and best_kt is not None:  # lower threshold for segments
                                    target_dict = (
                                        done_index if best_kt in done_tokens
                                        else open_index
                                    )
                                    for tlist in target_dict.values():
                                        for trow in tlist:
                                            if _tokens(trow[2]) == best_kt:
                                                seg_match = trow
                                                break
                                        if seg_match:
                                            break
                        if not seg_match:
                            break  # unresolved segment → don't sweep the line
                        seg_matches.append((seg_match, seg.strip()))
                    else:
                        # for-else: loop completed without break
                        if seg_matches and all(
                            m[0][1] in ("done", "archived") for m in seg_matches
                        ):
                            ids = ", ".join(m[0][0] for m in seg_matches)
                            match = seg_matches[0][0]  # use first task for display
                            # Annotate with all resolved IDs
                            body = f"{body} *(all resolved: {ids})*"

            # Fallback: highest Jaccard overlap with done/archived titles
            if not match:
                seg_tokens = set(kw.split())
                if seg_tokens:
                    best_sim = 0.0
                    best_kt = None
                    for kt in done_tokens:
                        if not kt:
                            continue
                        sim = len(seg_tokens & kt) / len(seg_tokens | kt)
                        if sim > best_sim:
                            best_sim = sim
                            best_kt = kt
                    if best_sim >= 0.5 and best_kt is not None:
                        for tlist in done_index.values():
                            for trow in tlist:
                                if _tokens(trow[2]) == best_kt:
                                    match = trow
                                    break
                            if match:
                                break

            # Apply the patch if a match was found
            if match:
                tid, status, _title = match
                # Mark resolved
                if m.groupdict().get("box") in ("x", "X"):
                    # Already checked; just annotate
                    new_body = f"{body} *(verified {status} {today}, {tid})*"
                else:
                    new_body = f"~~{body}~~ *(verified {status} {today}, {tid})*"
                # Preserve checkbox if present
                if "[" in line[:line.index("-") + 6]:
                    new_line = re.sub(r"-\s+\[[ xX]\]\s+.+", f"- [x] {new_body}", line)
                else:
                    new_line = f"- [x] {new_body}"
                edits.append((i + 1, line, new_line))
            # Don't auto-act on 'open' matches — leave as-is for kanban-review to handle

    if not edits:
        print(f"[{os.path.basename(os.path.dirname(carryover_path))}] no stale items found")
        return 0

    if dry_run:
        print(f"[{os.path.basename(os.path.dirname(carryover_path))}] would patch {len(edits)} line(s):")
        for ln, old, new in edits:
            print(f"  L{ln}: {old.strip()[:90]}")
            print(f"    ->  {new.strip()[:90]}")
        return len(edits)

    # Apply edits in reverse order so line numbers stay valid
    for ln, old, new in reversed(edits):
        lines[ln - 1] = new
    with open(carryover_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    print(f"[{os.path.basename(os.path.dirname(carryover_path))}] patched {len(edits)} stale line(s):")
    for ln, old, new in edits:
        print(f"  L{ln}: {old.strip()[:80]}")
    return len(edits)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("agent", help="agent name (e.g. arxiv, news)")
    ap.add_argument("--dry-run", "--no-write", action="store_true",
                    help="print edits without writing")
    args = ap.parse_args()

    path = os.path.join(CARRYOVER_ROOT, args.agent, "carryover.md")
    if not os.path.exists(path):
        print(f"ERROR: {path} not found", file=sys.stderr)
        sys.exit(1)
    n = sweep(path, dry_run=args.dry_run)
    sys.exit(0 if n >= 0 else 1)


if __name__ == "__main__":
    main()
