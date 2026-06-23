# Q4 - Use re.search() to check whether a word exists in a sentence.

import re

# Constants
SAMPLE_SENTENCE = (
    "Python is a powerful programming language."
)

SEARCH_WORD = "powerful"


def search_word_in_sentence(
        sentence: str,
        word: str
) -> bool:
    """Check whether a word exists in a sentence."""

    match = re.search(
        rf"\b{re.escape(word)}\b",
        sentence
    )

    word_found = match is not None

    print(f"Sentence: {sentence}")
    print(f"Search Word: '{word}'")
    print(f"Word Found: {word_found}")

    return word_found


if __name__ == "__main__":
    search_word_in_sentence(
        SAMPLE_SENTENCE,
        SEARCH_WORD
    )