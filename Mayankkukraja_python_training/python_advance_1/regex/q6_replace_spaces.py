# Q6 - Replace multiple spaces in a string
# with a single space using re.sub().

import re

# Constants
SAMPLE_TEXT = (
    "Python     is    a     powerful      programming    language."
)


def replace_multiple_spaces(
        text: str
) -> str:
    """Replace multiple spaces with a single space."""

    cleaned_text = re.sub(
        r"\s+",
        " ",
        text
    )

    print(f"Original Text: {text}")
    print(f"Cleaned Text:  {cleaned_text}")

    return cleaned_text


if __name__ == "__main__":
    replace_multiple_spaces(
        SAMPLE_TEXT
    )