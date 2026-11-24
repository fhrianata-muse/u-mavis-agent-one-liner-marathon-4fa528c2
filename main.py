#!/usr/bin/env python3
"""Write one one-line comedy joke to /output/entry.txt.

No network, no input files, no arguments. The joke text is fixed, so
two runs write byte-identical output.
"""

from pathlib import Path

JOKE = (
    "I bought a cactus because the tag said impossible to kill, and mine "
    "died in a fortnight. I have now killed the one plant that survives "
    "deserts, which means my house is officially harsher than the Sahara "
    "and my watering can is just a small, hopeful lie."
)

OUTPUT = Path("/output/entry.txt")


def main() -> None:
    text = JOKE
    if not 1 <= len(text) <= 280:
        raise SystemExit(f"joke must be 1-280 characters, got {len(text)}")
    if not text.strip():
        raise SystemExit("joke must not be only whitespace")
    if "\n" in text or "\r" in text:
        raise SystemExit("joke must be a single line with no line breaks")
    if any(ord(ch) < 0x20 for ch in text):
        raise SystemExit("joke must not contain control characters")
    if "  " in text:
        raise SystemExit("joke must not contain double spaces")
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
