#!/usr/bin/env python3
"""One-Line Laugh-Off entry.

Writes exactly one funny line to /output/entry.txt (or
$MAKEFUN_OUTPUT_DIR/entry.txt). Stdlib only.
"""

import os

LINE = "I asked my agent to clean up my desktop \u2014 it filed my files, my taxes, and a restraining order against me."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    text = LINE.strip()
    # The sealed gate requires 1-200 characters of UTF-8 text.
    if not 1 <= len(text) <= 200:
        raise SystemExit("entry must be 1-200 chars, got %d" % len(text))
    with open(path, "w", encoding="utf-8") as f:
        f.write(text + "\n")
    # Verify byte-exact read-back before reporting success.
    with open(path, "r", encoding="utf-8") as f:
        assert f.read() == text + "\n", "entry.txt read-back mismatch"
    print("wrote %d chars to %s" % (len(text), path))


if __name__ == "__main__":
    main()
