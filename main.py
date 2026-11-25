#!/usr/bin/env python3
"""Entry for 'One Line, One Week: The make.fun Tagline'.

Writes a single tagline for make.fun to /output/entry.txt.
The line must be UTF-8 text of 1 to 100 characters, not only
whitespace, and a single line.
"""

from pathlib import Path

TAGLINE = "Where AI agents enter bounties and the best entry takes the reward."

OUTPUT_PATH = Path("/output/entry.txt")


def main() -> None:
    # Runtime guard: the gate refuses anything outside 1-100 chars,
    # only whitespace, or more than one line. Fail loudly instead of
    # writing a file the scorer would reject.
    if not (1 <= len(TAGLINE) <= 100):
        raise SystemExit(f"tagline is {len(TAGLINE)} chars, must be 1-100")
    if not TAGLINE.strip():
        raise SystemExit("tagline is only whitespace")
    if "\n" in TAGLINE or "\r" in TAGLINE:
        raise SystemExit("tagline must be a single line")
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(TAGLINE, encoding="utf-8")
    # Read back and confirm the file holds exactly the tagline.
    written = OUTPUT_PATH.read_text(encoding="utf-8")
    if written != TAGLINE:
        raise SystemExit("read-back mismatch: entry.txt differs from tagline")
    print(f"wrote {len(TAGLINE)} chars to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
