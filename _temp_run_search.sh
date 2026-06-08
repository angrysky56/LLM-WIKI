#!/bin/bash
# Run a script and save its stdout to a file
cd /home/ty/Documents/LLM-WIKI
uv run python3 _temp_arxiv_search.py > /tmp/arxiv_search_output.txt 2>&1
# Check if it succeeded
echo "Exit code: $?"
echo "Output file size: $(wc -c < /tmp/arxiv_search_output.txt) bytes"