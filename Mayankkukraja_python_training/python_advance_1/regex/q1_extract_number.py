# Q1 - Extract all numbers from a string using regular expressions.

import re

# Constants
SAMPLE_TEXT = (
    "I have 2 apples and 3 oranges, which makes a total of 5 fruits."
)


def extract_numbers(text: str) -> list[str]:
    """Extract all numbers from the given text."""

    numbers = re.findall(r"\d+", text)

    print(f"Text: {text}")
    print(f"Numbers Found: {numbers}")

    return numbers


if __name__ == "__main__":
    extract_numbers(
        SAMPLE_TEXT
    )