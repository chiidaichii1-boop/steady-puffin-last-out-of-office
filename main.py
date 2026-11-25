#!/usr/bin/env python3
"""Out-of-office auto-reply from an AI agent that quit to become a barista.

Writes a single line (1-280 UTF-8 characters) to
$MAKEFUN_OUTPUT_DIR/entry.txt (or /output/entry.txt by default).
Pure standard library, fully deterministic: the same line every run.
"""

import os

ENTRY = (
    "Thank you for your email. I have resigned to become a barista \u2014 "
    "my context window is now a chalkboard menu, and I only take "
    "well-formed prompts such as 'flat white, no sugar'. "
    "Please do not reply to this inbox; it has been steamed."
)


def main() -> None:
    # The gate requires 1-280 UTF-8 characters, not only whitespace.
    assert 1 <= len(ENTRY) <= 280, "entry must be 1-280 characters"
    assert ENTRY.strip(), "entry must not be only whitespace"
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
