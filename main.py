#!/usr/bin/env python3
"""One Line, One Laugh — writes a single funny line to /output/entry.txt."""

import os

LINE = (
    "My cat has been staring at the wall for an hour, so now I'm staring "
    "too — I refuse to be the only one in this house who doesn't know."
)


def main() -> None:
    text = LINE.strip()
    assert 1 <= len(text) <= 200, "entry must be 1..200 characters"
    assert "\n" not in text, "entry must be a single line"
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as fh:
        fh.write(text)


if __name__ == "__main__":
    main()
