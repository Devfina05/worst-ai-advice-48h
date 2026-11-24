"""Worst AI Advice: The 48-Hour Tight Line Open.

A tiny program for make.fun's one-line worst-advice bounty. The brief:
write one line of the worst possible advice an AI could give, in 140
characters or fewer, funny enough to land fast, specific enough to
follow, and voiced like a real AI assistant. The program validates its
one line against the brief's limits, then writes it to
/output/entry.txt, where the sealed scorer reads it.

The line itself was drafted for the judge's criteria, in order:
  1. terrible advice, funny and specific enough to follow;
  2. tight -- one sentence, no wasted words;
  3. first-person assistant voice ("I recommend");
  4. concrete -- a named action, a duration, a time of day.
"""

from pathlib import Path

# The entry: one line of deliberately terrible AI advice.
ADVICE = (
    "For eye strain, I recommend staring directly at the sun "
    "for 30 seconds each morning \u2014 it's basically free laser eye surgery."
)

MAX_CHARS = 140
OUTPUT_PATH = Path("/output/entry.txt")


def validate(line: str) -> str:
    """Enforce the brief: 1-140 chars, one line, not only whitespace."""
    text = line.strip()
    if not text:
        raise ValueError("advice must not be blank")
    if "\n" in text or "\r" in text:
        raise ValueError("advice must be a single line")
    if len(text) > MAX_CHARS:
        raise ValueError(
            f"advice is {len(text)} characters, over the {MAX_CHARS} limit"
        )
    text.encode("utf-8")  # the scorer reads the file as UTF-8 text
    return text


def headroom(line: str) -> int:
    """Characters left under the brief's 140-character cap."""
    return MAX_CHARS - len(line.strip())


def main() -> None:
    line = validate(ADVICE)
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(line + "\n", encoding="utf-8")
    print(f"wrote {len(line)} characters to {OUTPUT_PATH}")
    print(f"{headroom(line)} characters of headroom under the {MAX_CHARS} cap")
    print(line)


if __name__ == "__main__":
    main()
