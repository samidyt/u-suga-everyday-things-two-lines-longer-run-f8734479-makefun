#!/usr/bin/env python3
"""Entry for make.fun bounty: Everyday Things, Two Lines, Longer Run.

Writes the two-line explanation to /output/entry.txt.

Line 1 explains one everyday thing (a traffic jam) to a 10-year-old in a
single vivid sentence built on one analogy. Line 2 says in one sentence
why that analogy works: what it maps and what it leaves out.
"""

ENTRY = (
    "A traffic jam is a river of cars that forgot how to flow, so it just "
    "stands there, bumper to bumper, waiting for someone downstream to move.\n"
    "The river maps how cars pile up behind each other the way water piles "
    "up behind a dam, but it leaves out that rivers never choose to stop "
    "\u2014 drivers do, by braking \u2014 and a river never honks.\n"
)


def main() -> None:
    import os

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
