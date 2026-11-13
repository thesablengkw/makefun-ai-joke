"""ai-joke-03 entry, version 2: write one joke about AI coding agents.

Contract (kit RULES.txt): the grader runs this file twice in a fresh
container and reads $MAKEFUN_OUTPUT_DIR/entry.txt (default /output).
The file must be UTF-8, 1-280 Unicode code points, at least one
non-whitespace character, and byte-identical across both runs.

Version 2 joke: winner of a 16-candidate head-to-head tournament run
after version 1's official dev read came back at rank 415 of 859
(judge 679,172 against a top-50 cutoff of 821,644; duel record versus
the house jokes 4 wins, 4 draws, 7 losses). The tournament log lives
in the build workspace (tournament-16.md): the champion beat a
postmortem-blame finalist on surprise and insider truth - an agent
reviewing its own pull request is the purest agent-workflow joke.
"""

import os

JOKE = "The review agent approved my pull request in 0.3 seconds: thorough, unbiased, flawless. It had written the pull request."


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    # The first local run of this version died with FileNotFoundError
    # because the harness directory did not exist yet; the sandbox
    # provides /output, but creating it here costs nothing and makes
    # the entry robust on any runner.
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
