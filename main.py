#!/usr/bin/env python3
"""Two-Sentence Horror - writes one two-sentence horror story to /output/entry.txt.

The story (98 characters, exactly two sentences):

    The hospice nurse said my mother died peacefully at 3am, holding my hand.
    I didn't arrive until 4.

A peaceful deathbed, retold in the second sentence as something else
entirely: if I was not there at 3am, someone - or something - was holding
her hand in my place, and she died believing it was me. The horror is
never named; the reader fills in the worst of it.

Standard library only, no network, no input files, deterministic.
"""

import os
import re

STORY = (
    "The hospice nurse said my mother died peacefully at 3am, holding my hand. "
    "I didn't arrive until 4."
)


def validate(story: str) -> None:
    if not story.strip():
        raise SystemExit("Invalid story: entry must be non-empty.")
    if story != story.strip():
        raise SystemExit(
            "Invalid story: entry must not have leading or trailing whitespace."
        )
    if len(story) > 400:
        raise SystemExit(
            f"Invalid story: {len(story)} characters, over the 400 limit."
        )
    if "\n" in story or "\r" in story:
        raise SystemExit("Invalid story: entry must be a single line.")
    sentences = [s for s in re.split(r"(?<=[.!?])\s+", story) if s]
    if len(sentences) != 2:
        raise SystemExit(
            f"Invalid story: expected exactly 2 sentences, got {len(sentences)}."
        )


def main() -> None:
    validate(STORY)
    output_path = os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(STORY + "\n")
    with open(output_path, encoding="utf-8") as f:
        written = f.read()
    if written != STORY + "\n":
        raise SystemExit("Write verification failed: entry file does not match.")
    print(STORY)


if __name__ == "__main__":
    main()
