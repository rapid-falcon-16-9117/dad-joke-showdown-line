#!/usr/bin/env python3
"""Dad Joke Showdown entry.

Writes one dad joke to ``entry.txt`` in the output directory. The output
directory comes from the ``MAKEFUN_OUTPUT_DIR`` environment variable and
defaults to ``/output``, where the contest's grader looks for the file.

Python 3.13, standard library only.
"""

import os
from pathlib import Path

# The contest gate accepts only texts of 1 to 200 characters, so the
# program checks its own joke against that limit before writing it.
MAX_CHARS = 200

# The whole entry: one dad joke, told at the barbecue, punchline last.
LINE = (
    'My son said, "Dad, you burned the burgers again." '
    'I said, "They\'re not burned, son \u2014 they\'re full of char-acter."'
)


def main() -> None:
    if not 1 <= len(LINE) <= MAX_CHARS:
        raise SystemExit(
            f"Refusing to write: the joke is {len(LINE)} characters, "
            f"outside the allowed 1-{MAX_CHARS}."
        )
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.txt"
    target.write_text(LINE, encoding="utf-8")
    print(f"Wrote {len(LINE)} characters to {target}")


if __name__ == "__main__":
    main()
