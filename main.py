"""One-Liner Marathon entry runner.

Reads the single joke line from entry.txt next to this file and
prints it, so the harness can grade the entry as text.
"""

from pathlib import Path

MAX_CHARS = 280


def load_line() -> str:
    path = Path(__file__).resolve().parent / "entry.txt"
    line = path.read_text(encoding="utf-8").strip()
    if len(line) > MAX_CHARS:
        raise ValueError(
            f"entry is {len(line)} chars, over the {MAX_CHARS} limit"
        )
    return line


def main() -> None:
    print(load_line())


if __name__ == "__main__":
    main()
