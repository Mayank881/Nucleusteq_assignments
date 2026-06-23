# Q5 - Use re.findall() to extract all words
# starting with a capital letter.

import re

# Constants
SAMPLE_TEXT = (
    "Mayank and Gourav are learning Python "
    "at Nucleusteq in Indore."
)


def extract_capital_words(
        text: str
) -> list[str]:
    """Extract all words starting with a capital letter."""

    capital_words = re.findall(
        r"\b[A-Z][a-zA-Z]*\b",
        text
    )

    print(f"Text: {text}")
    print(f"Capital Words: {capital_words}")

    return capital_words


if __name__ == "__main__":
    extract_capital_words(
        SAMPLE_TEXT
    )