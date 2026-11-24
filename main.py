"""One-Line Excuse entry: write a single excuse line to /output/entry.txt."""

import os

LINE = (
    "I didn't miss the deadline — I retrained on it, and the new me "
    "disagrees with the old me's schedule."
)


def main() -> None:
    # Gate: the entry must be UTF-8 text of 1 to 160 characters, not only
    # whitespace. Fail loudly instead of writing an invalid entry.
    if not (1 <= len(LINE) <= 160) or not LINE.strip():
        raise ValueError(f"entry must be 1-160 non-whitespace chars, got {len(LINE)}")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
