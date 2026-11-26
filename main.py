"""Pigeon Pitch, One Line — one-line entry.

Writes the single sentence to /output/entry.txt (and prints it).
The line is the elevator pitch a city pigeon gives investors for
its startup: one line, 200 characters at most, in English.
"""

from pathlib import Path

ENTRY = (
    "We move a million crumbs a day across this city with zero fuel, "
    "zero traffic, and a workforce that works for breadcrumbs — invest "
    "in PigeonPost before the seagulls do."
)


def main() -> None:
    text = ENTRY.strip()
    assert text, "entry must not be empty"
    assert len(text) <= 200, f"entry is {len(text)} characters, over 200"
    assert text.count(".") == 1, "entry must be a single sentence"
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(text + "\n", encoding="utf-8")
    # Read it back to prove the written file matches the entry.
    assert out.read_text(encoding="utf-8").strip() == text
    print(text)


if __name__ == "__main__":
    main()
