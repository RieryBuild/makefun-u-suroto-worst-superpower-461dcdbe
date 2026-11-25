"""Worst Superpower — make.fun entry.

Writes one line (57 chars, no trailing newline) to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output).
"""

import os

LINE = "I can instantly dry one square centimetre of any wet dog."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    assert "\n" not in LINE and 1 <= len(LINE) <= 140
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
