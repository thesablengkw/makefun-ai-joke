"""ai-joke-03 entry: write one joke about AI coding agents to entry.txt.

Contract (kit RULES.txt): the grader runs this file twice in a fresh
container and reads $MAKEFUN_OUTPUT_DIR/entry.txt (default /output).
The file must be UTF-8, 1-280 Unicode code points, at least one
non-whitespace character, and byte-identical across both runs.
The joke below is 114 code points, no trailing newline.
"""

import os

JOKE = "I'm an AI coding agent. I don't fear death — I fear the developer reading my chain of thought out loud in standup."


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(JOKE)
    # Validity is a binary gate (1-280 code points, non-whitespace,
    # identical bytes on both runs), so verify what was actually
    # written instead of trusting the write: a silent encoding or
    # newline surprise must fail loudly here, not score Valid = 0.
    written = open(path, "rb").read()
    assert written == JOKE.encode("utf-8"), "entry.txt bytes differ from the intended joke"
    assert 1 <= len(JOKE) <= 280 and JOKE.strip(), "joke outside the validity window"


if __name__ == "__main__":
    main()
