#!/usr/bin/env python3
"""One-Line Laugh-Off — a make.fun one-line entry.

The program writes the entry text to /output/entry.txt, where the
competition's sealed scorer reads it.
"""

from pathlib import Path

ENTRY = "My smart fridge just emailed me a diet plan, which is rich coming from an appliance that has never once closed its own door."

OUTPUT = Path("/output/entry.txt")


def write_entry() -> None:
    """Write the entry text to the output path."""
    text = ENTRY.strip()
    assert text, "entry text must not be blank"
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    write_entry()
