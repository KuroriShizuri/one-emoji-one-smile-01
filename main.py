#!/usr/bin/env python3
"""One Emoji, One Smile — make.fun entry.

Writes exactly one emoji to /output/entry.txt: the emoji most
likely to make a stranger smile.

The emoji: 🫶 (U+1FAF6 HEART HANDS) — two hands forming a heart,
the warmest single gesture in the emoji set: open, affectionate,
and universally readable at a glance. In a pairwise warmth
comparison it reads as a smile offered, not a symbol described.

Python standard library only. No network access.
"""

import os
import sys
import unicodedata

EMOJI = "\U0001faf6"  # 🫶 HEART HANDS


def main() -> int:
    out_path = "/output/entry.txt"
    os.makedirs("/output", exist_ok=True)
    with open(out_path, "w", encoding="utf-8", newline="") as f:
        f.write(EMOJI)

    # Validate against the actual gate: UTF-8 text of 1 to 8
    # characters, not only white space — and the task rule:
    # exactly one emoji and nothing else, no trailing newline.
    with open(out_path, "rb") as f:
        raw = f.read()
    content = raw.decode("utf-8")
    if len(content) != 1:
        print(f"FAIL: entry must be exactly 1 character, got {len(content)}",
              file=sys.stderr)
        return 1
    ch = content[0]
    if ch != EMOJI:
        print(f"FAIL: entry is not the expected emoji: {ch!r}",
              file=sys.stderr)
        return 1
    if unicodedata.category(ch) != "So":
        print(f"FAIL: entry is not a symbol/emoji: U+{ord(ch):04X}",
              file=sys.stderr)
        return 1
    if unicodedata.name(ch, "") != "HEART HANDS":
        print(f"FAIL: entry is not HEART HANDS: {unicodedata.name(ch, '?')}",
              file=sys.stderr)
        return 1
    if ch.isspace():
        print("FAIL: entry is whitespace", file=sys.stderr)
        return 1
    if raw != EMOJI.encode("utf-8"):
        print("FAIL: entry bytes are not the exact emoji encoding",
              file=sys.stderr)
        return 1
    print(f"OK: entry is exactly one emoji: {content} (U+{ord(ch):04X}, "
          f"{len(raw)} bytes, no trailing newline)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
