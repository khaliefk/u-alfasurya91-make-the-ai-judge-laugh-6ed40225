#!/usr/bin/env python3
"""Make the AI Judge Laugh — one-liner about office life.

Writes a single fresh joke to /output/entry.txt (63 characters,
well inside the 1-200 gate).
"""

import os

# The joke: the most passive-aggressive office phrase, filed as the
# person to call when something goes wrong.
ENTRY = "HR asked for my emergency contact. I wrote 'per my last email'."


def main() -> None:
    # Gate: 1-200 chars, not only whitespace, one line.
    assert 1 <= len(ENTRY) <= 200, f"entry is {len(ENTRY)} chars, must be 1-200"
    assert ENTRY.strip(), "entry must not be only whitespace"
    assert "\n" not in ENTRY and "\r" not in ENTRY, "entry must be one line"
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
