"""One Line, One Laugh - entry generator.

Writes the single funny line to /output/entry.txt (UTF-8, no trailing
newline) and verifies the gate rules: 1-200 characters, exactly one line,
not only whitespace.
"""

import os
import sys

ENTRY = "My fortune cookie promised me a bright future, so the restaurant turned off the lights and asked me to leave."

OUTPUT_PATH = "/output/entry.txt"


def main():
    # Gate assertions on the entry text itself.
    assert 1 <= len(ENTRY) <= 200, "entry must be 1-200 characters"
    assert ENTRY.strip(), "entry must not be only whitespace"
    assert "\n" not in ENTRY and "\r" not in ENTRY, "entry must be one line"
    assert not ENTRY.endswith("\n"), "entry must not end with a newline"

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)

    # Read back and assert byte-identical output.
    with open(OUTPUT_PATH, "rb") as f:
        raw = f.read()
    assert raw == ENTRY.encode("utf-8"), "output bytes differ from ENTRY"
    decoded = raw.decode("utf-8")
    assert 1 <= len(decoded) <= 200, "written entry must be 1-200 characters"
    assert "\n" not in decoded and "\r" not in decoded, "written entry must be one line"

    print(ENTRY)
    print("chars: %d" % len(ENTRY))
    return 0


if __name__ == "__main__":
    sys.exit(main())
