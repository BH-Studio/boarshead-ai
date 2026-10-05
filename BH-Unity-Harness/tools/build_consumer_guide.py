#!/usr/bin/env python3
"""Copy the owned consumer guidance without creating a second wire schema."""
from pathlib import Path
P = Path(__file__).resolve().parents[1]
if __name__ == '__main__':
    source = P/'contracts/CODEX_CONSUMER.md'
    target = P/'project-template/Docs/Harness/CODEX_CONSUMER.md'
    target.write_bytes(source.read_bytes())
