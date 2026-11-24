"""Fortune-cookie entry: writes one line to <MAKEFUN_OUTPUT_DIR or /output>/entry.txt."""

import os
import sys

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"

TEXT = "Legacy code is a letter from a developer who trusted you to finish it.\n"


def main() -> int:
    try:
        os.makedirs(OUTPUT_DIR, exist_ok=True)
    except OSError as exc:
        print(f"cannot create output directory {OUTPUT_DIR!r}: {exc}", file=sys.stderr)
        return 1

    try:
        with open(os.path.join(OUTPUT_DIR, "entry.txt"), "w", encoding="utf-8") as f:
            f.write(TEXT)
    except OSError as exc:
        print(f"cannot write entry.txt in {OUTPUT_DIR!r}: {exc}", file=sys.stderr)
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
