#!/usr/bin/env python3
"""Alien Field Notes: The Two Day Earth Review.

Writes one original line -- an alien tourist's review of planet Earth --
to /output/entry.txt.

Pure Python standard library: no dependencies, no network, deterministic.
"""

import os

# Gate caps from the competition rules: /output/entry.txt must be UTF-8
# text of 1 to 200 characters, a single line, not only white space.
MAX_CHARS = 200

# The one-line review (177 characters, measured -- well inside the
# 200-character gate).
# Voice: a bemused alien tourist, deadpan. Concrete detail: humans live
# inside little boxes all week, then drive for hours to other little
# boxes just to look at trees. The turn lands on the last clause:
# a 4/5 verdict and "would orbit again" -- a tourist's closing remark.
REVIEW = (
    "Earth: stunning views, confusing locals. They spend all week inside "
    "little boxes, then drive for hours to other little boxes just to "
    "look at trees. 4/5 stars, would orbit again."
)


def main() -> None:
    text = REVIEW.strip()
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if not text:
        raise ValueError("entry must not be empty")
    if len(text) > MAX_CHARS:
        raise ValueError(
            "entry must be 1-%d characters, got %d" % (MAX_CHARS, len(text))
        )
    # The grader provides /output; fall back to a local output/ dir so the
    # program also runs standalone for a quick local check.
    try:
        os.makedirs("/output", exist_ok=True)
        out_path = "/output/entry.txt"
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(text)
    except OSError:
        os.makedirs("output", exist_ok=True)
        out_path = os.path.join("output", "entry.txt")
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(text)
    print("wrote %d characters to %s" % (len(text), out_path))


if __name__ == "__main__":
    main()
