#!/usr/bin/env python3
"""One-Line Laugh-Off (make.fun).

Writes the entry -- exactly one funny line --
to /output/entry.txt, where the sealed scorer reads it.
"""

import os

TEXT = "I was going to write a joke about procrastination, but I'll do it tomorrow."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
