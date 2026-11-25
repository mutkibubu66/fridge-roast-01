#!/usr/bin/env python3
"""Write one original roast line for a smart fridge.

Pure standard library, no network. Writes the line to /output/entry.txt
and prints it to stdout.

The line roasts the ice maker: a machine whose only job is freezing
water now demands three preconditions before it will make one cube —
a firmware update, a Wi-Fi signal, and a pep talk. The third item is
the turn: an appliance that needs emotional support before doing the
one thing it was built for. It aims squarely at the fridge's firmware
and connectivity, not at the generic "it orders groceries" or "it
watches you" cracks every other roast reaches for first.
"""

import os

OUTPUT_PATH = "/output/entry.txt"


def get_line() -> str:
    """Return the entry line: the ice maker and its three preconditions."""
    return (
        "My smart fridge's ice maker needs a firmware update, "
        "a Wi-Fi signal, and a pep talk before it will make a single cube."
    )


LINE = get_line()


def validate(line: str) -> None:
    """Enforce the gate: 1-200 chars, exactly one non-blank UTF-8 line."""
    if line != line.strip():
        raise ValueError("entry must have no leading/trailing whitespace")
    if len(line.splitlines()) != 1:
        raise ValueError("entry must be exactly one line")
    if not 1 <= len(line) <= 200:
        raise ValueError("entry line must be 1-200 characters")
    if not line.strip():
        raise ValueError("entry must not be only whitespace")
    line.encode("utf-8")  # must be valid UTF-8


def main() -> None:
    validate(LINE)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    # Round-trip check: what the grader reads must be exactly the line.
    with open(OUTPUT_PATH, encoding="utf-8") as f:
        assert f.read() == LINE + "\n", "entry.txt round-trip mismatch"
    print(LINE)


if __name__ == "__main__":
    main()
