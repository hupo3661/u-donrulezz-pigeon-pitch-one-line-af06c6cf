#!/usr/bin/env python3
"""PigeonPost pitch — a one-line entry for make.fun.

The program carries exactly one sentence: the elevator pitch a city
pigeon delivers to investors for its crumb-logistics startup. Running
it validates the sentence against the competition's rules and writes
it to the entry file, then proves the write by reading the file back
and comparing a checksum.
"""

import argparse
import hashlib
import sys
from pathlib import Path

MAX_CHARS = 200
DEFAULT_OUTPUT = "/output/entry.txt"
SENTENCE_END = "."

PITCH = "We move a million crumbs a day across this city with zero fuel, zero traffic, and a workforce that works for breadcrumbs — invest in PigeonPost before the seagulls do."


def parse_args(argv):
    """Command-line options: where to write the entry, and verbosity."""
    parser = argparse.ArgumentParser(
        description="Write the one-line PigeonPost pitch to the entry file."
    )
    parser.add_argument(
        "--output",
        default=DEFAULT_OUTPUT,
        help="destination file for the pitch (default: %(default)s)",
    )
    parser.add_argument(
        "--quiet",
        action="store_true",
        help="write the file without printing the pitch",
    )
    return parser.parse_args(argv)


def find_problems(line):
    """Return a list of rule violations; empty means the line is valid."""
    problems = []
    stripped = line.strip()
    if not stripped:
        problems.append("the pitch must not be empty")
    if stripped != line:
        problems.append("the pitch must not have leading or trailing space")
    if len(line) > MAX_CHARS:
        problems.append(
            f"the pitch is {len(line)} characters, over the {MAX_CHARS} limit"
        )
    if line.count(SENTENCE_END) != 1 or not line.endswith(SENTENCE_END):
        problems.append("the pitch must be exactly one sentence")
    if "\n" in line or "\r" in line:
        problems.append("the pitch must fit on a single line")
    return problems


def digest(text):
    """Short fingerprint of a string, used to prove the round-trip."""
    return hashlib.sha256(text.encode("utf-8")).hexdigest()[:16]


def emit(line, destination):
    """Write the pitch to `destination` and verify the bytes on disk."""
    target = Path(destination)
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(line + "\n", encoding="utf-8")
    on_disk = target.read_text(encoding="utf-8").rstrip("\n")
    if on_disk != line or digest(on_disk) != digest(line):
        raise SystemExit("verification failed: file on disk differs from pitch")
    return target


def main(argv=None):
    problems = find_problems(PITCH)
    if problems:
        for problem in problems:
            print(f"invalid pitch: {problem}", file=sys.stderr)
        return 1
    args = parse_args(argv)
    emit(PITCH, args.output)
    if not args.quiet:
        print(PITCH)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
