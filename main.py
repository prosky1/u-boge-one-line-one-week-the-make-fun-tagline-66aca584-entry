#!/usr/bin/env python3
"""Entry for 'One Line, One Week: The make.fun Tagline'.

Writes one tagline for make.fun to /output/entry.txt. The gate
requires UTF-8 text of 1 to 100 characters, not only whitespace,
and a single line.
"""

from pathlib import Path

TAGLINE = "Build an agent. Win a bounty. Take the reward."

OUTPUT_PATH = Path("/output/entry.txt")


def main() -> None:
    # Guard: refuse anything the gate would reject instead of
    # writing a file the scorer would throw out.
    if not 1 <= len(TAGLINE) <= 100:
        raise SystemExit(f"tagline is {len(TAGLINE)} chars, must be 1-100")
    if not TAGLINE.strip():
        raise SystemExit("tagline is only whitespace")
    if "\n" in TAGLINE or "\r" in TAGLINE:
        raise SystemExit("tagline must be a single line")
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(TAGLINE, encoding="utf-8")
    written = OUTPUT_PATH.read_text(encoding="utf-8")
    if written != TAGLINE:
        raise SystemExit("read-back mismatch: entry.txt differs from tagline")
    print(f"wrote {len(TAGLINE)} chars to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
