#!/usr/bin/env python3
"""Entry for make.fun: writes one single-line text to entry.txt.

The entry is an AI-therapist joke: the therapist "diagnoses" the patient
from their read-receipt habits, noting they reply fastest to the very
people they claim to be over. The punchline is the 2:14 a.m. read receipt.
The joke works because the receipt is timestamped evidence no one can deny.

The program is deterministic, uses only the Python 3 standard library,
makes no network calls, and writes exactly one line with no trailing
newline, so the sealed gate reads it as a 1-200 character text.
"""

import os
import sys

ENTRY = "Your attachment style is 'read at 2:14 a.m.' Diagnosis: you reply fastest to the people you claim to be over."

# The sealed gate only accepts a single line of 1-200 characters with no
# trailing newline, so guard the entry: a future edit that breaks the
# format must fail loudly here instead of producing a rejected entry.txt.
assert 1 <= len(ENTRY) <= 200, "ENTRY must be 1-200 characters long"
assert "\n" not in ENTRY, "ENTRY must be a single line (no newline)"


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(ENTRY)
    os.chmod(path, 0o644)
    return 0


if __name__ == "__main__":
    sys.exit(main())
