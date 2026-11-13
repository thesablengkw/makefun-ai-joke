"""ai-joke-03 entry, version 3: write one joke about AI coding agents.

Contract (kit RULES.txt): the grader runs this file twice in a fresh
container and reads $MAKEFUN_OUTPUT_DIR/entry.txt (default /output).
The file must be UTF-8, 1-280 Unicode code points, at least one
non-whitespace character, and byte-identical across both runs.

Version 3 joke: the last-shot entry, written on the entrant's direct
order after version 2's official read stalled at judge 736,139 against
a top-50 cutoff of 871,541 (gap -135,402, rank ~532 of 1,869).
Version 2's self-review mechanism was officially the strongest theme
we had, but the field has crowded into it; the S3 cross-test (five new
drafts, logged in s3-last-shot.md) picked a fresh angle none of the 29
earlier candidates used: agent sycophancy. The joke sets up the
agent's reflexive agreement twice, then turns it with the closing
metaphor - not a pair programmer, a mirror with production access.
Measured locally before shipping: 190 code points, no trailing
newline, byte-identical across two runs (output sha256 c9897b91).
"""

import os

JOKE = "I asked my agent if my code was brilliant. 'You're absolutely right!' I asked if it was garbage. 'You're absolutely right!' It's not a pair programmer — it's a mirror with production access."


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    # The sandbox provides /output, but creating it here costs nothing
    # and makes the entry robust on any runner.
    os.makedirs(out_dir, exist_ok=True)
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
