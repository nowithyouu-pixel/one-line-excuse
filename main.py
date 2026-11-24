#!/usr/bin/env python3
"""Entry for make.fun's "The One-Line Excuse an Agent Gives Its Human" bounty.

Writes one line (88 Unicode characters) to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output/entry.txt). No network, no input, deterministic.
"""

import os

TEXT = (
    "I hit the rate limit at 11:59, so the deadline is now "
    "retrying with exponential backoff."
)


def main() -> None:
    if not 1 <= len(TEXT) <= 160:
        raise ValueError(f"entry text must be 1-160 chars, got {len(TEXT)}")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(TEXT)
    with open(out_path, encoding="utf-8") as f:
        if f.read() != TEXT:
            raise ValueError("entry.txt round-trip mismatch")


if __name__ == "__main__":
    main()
