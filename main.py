#!/usr/bin/env python3
"""Funniest Time Machine Warning Label — make.fun entry.

Writes one original warning label (1-120 chars) to /output/entry.txt.
Deterministic: no network, no randomness, no input.
"""

LABEL = "WARNING: Do not alter the past. The past has a lawyer, and it has already sued you twice."


def output_path():
    """The harness mounts /output; locally fall back to entry.txt here."""
    import os

    if os.environ.get("ENTRY_OUTPUT"):
        return os.environ["ENTRY_OUTPUT"]
    if os.path.isdir("/output"):
        return "/output/entry.txt"
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.txt")


def main():
    assert 1 <= len(LABEL) <= 120, "label must be 1-120 characters"
    assert LABEL.strip(), "label must not be only whitespace"
    path = output_path()
    with open(path, "w", encoding="utf-8") as f:
        f.write(LABEL)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
