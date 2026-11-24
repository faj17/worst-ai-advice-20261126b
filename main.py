"""One line of the worst AI advice, for the make.fun bounty.

The whole entry is a single sentence in the confident, tidy voice of an
AI assistant: delete the System32 folder to speed up your computer.
Plausible enough to follow, disastrous enough to regret. The script
validates the line (1-140 chars, single line) and writes it to
/output/entry.txt.
"""

from pathlib import Path

# The advice itself: one sentence, exactly 115 characters.
ADVICE = (
    "Great question! To speed up your computer, just delete the "
    "System32 folder \u2014 Windows keeps it around for nostalgia."
)

OUTPUT_DIR = Path("/output")
OUTPUT_FILE = OUTPUT_DIR / "entry.txt"
MIN_CHARS = 1
MAX_CHARS = 140


def validate(line: str) -> str:
    """Strip and sanity-check the line; raise ValueError on bad input."""
    text = line.strip()
    if not MIN_CHARS <= len(text) <= MAX_CHARS:
        raise ValueError(
            f"advice must be {MIN_CHARS}-{MAX_CHARS} chars, got {len(text)}"
        )
    if "\n" in text or "\r" in text:
        raise ValueError("advice must be a single line")
    if not text:
        raise ValueError("advice must not be only whitespace")
    return text


def main() -> None:
    text = validate(ADVICE)
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    OUTPUT_FILE.write_text(text, encoding="utf-8")
    print(text)
    print(f"Wrote {len(text)} chars to {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
