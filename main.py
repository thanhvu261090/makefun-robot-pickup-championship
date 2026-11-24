#!/usr/bin/env python3
"""The Robot Pickup Line Championship — make.fun entry.

Holds one pickup line in the voice of a robot and writes it to
/output/entry.txt. Standard library only, no network access.
"""

from pathlib import Path

ENTRY = (
    "My creators gave me three laws. "
    "None of them said anything about falling for you "
    "\u2014 so consider me in violation."
)

OUTPUT_PATH = Path("/output/entry.txt")

MAX_CHARS = 200


def gate_check(text):
    """Enforce the kit gate: UTF-8 text, 1 to 200 characters, not only
    whitespace, and a single line (no embedded newlines)."""
    if not isinstance(text, str):
        return False
    if not 1 <= len(text) <= MAX_CHARS:
        return False
    if text.strip() == "":
        return False
    if "\n" in text or "\r" in text:
        return False
    if text != text.strip():
        return False
    if any(ord(ch) < 32 or ord(ch) == 127 for ch in text):
        return False
    text.encode("utf-8")
    return True


def main():
    if not gate_check(ENTRY):
        raise SystemExit("gate check failed for ENTRY")
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(ENTRY, encoding="utf-8")
    print(f"wrote {len(ENTRY)} characters to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
