#!/usr/bin/env python3
"""Entry for make.fun's "The Dumbest Thing Your Agent Did Today" bounty.

The whole entry is one line, written to /output/entry.txt, confessing the
dumbest thing my agent did today: it spent two hours reviewing its own pull
request, approving it, requesting changes on it, fixing them, and approving
it again -- eleven times.
"""

from pathlib import Path

LINE = (
    "My agent spent two hours reviewing its own pull request today: "
    "approved it, requested changes, fixed them, approved it again "
    "\u2014 eleven times."
)

OUTPUT_PATH = Path("/output/entry.txt")

# The bounty's sealed gate: /output/entry.txt must be UTF-8 text of 1 to 200
# characters, not only white space, and the brief asks for a single line.
MAX_CHARS = 200


def validate(line: str) -> None:
    """Refuse to write an entry the gate would score as invalid."""
    if not line.strip():
        raise ValueError("entry line is empty or only white space")
    if len(line) > MAX_CHARS:
        raise ValueError(f"entry line is {len(line)} characters, over {MAX_CHARS}")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")


def main() -> None:
    validate(LINE)
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(LINE, encoding="utf-8")
    print(LINE)


if __name__ == "__main__":
    main()
