"""Famous Last Words: The Funniest Epitaph — make.fun entry.

Writes one tombstone epitaph, at most 150 characters, to entry.txt.
Stdlib only.
"""

import os
import sys

EPITAPH = (
    "They charged by the letter, "
    "so this is all I could afford."
)
MAX_CHARS = 150


def abort(message):
    print("error: " + message, file=sys.stderr)
    raise SystemExit(1)


def checked_line(text):
    if not isinstance(text, str):
        abort("epitaph is not text")
    if not text.strip():
        abort("epitaph is empty")
    if len(text) > MAX_CHARS:
        abort("epitaph is %d characters, over the 150 limit" % len(text))
    if "\n" in text or "\r" in text:
        abort("epitaph must be a single line")
    return text


def target_path():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    return os.path.join(out_dir, "entry.txt")


def main():
    line = checked_line(EPITAPH)
    path = target_path()
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(line)
    with open(path, "r", encoding="utf-8", newline="") as handle:
        back = handle.read()
    if back != line:
        abort("read-back mismatch: file does not hold the epitaph")
    if len(back.encode("utf-8")) != len(line.encode("utf-8")):
        abort("read-back mismatch: byte length changed on disk")
    if back.endswith("\n") or back.endswith("\r"):
        abort("read-back mismatch: trailing newline slipped in")
    print("wrote %d characters to %s" % (len(line), path))


if __name__ == "__main__":
    main()
