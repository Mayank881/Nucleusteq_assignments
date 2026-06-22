# Q6 - Explain the difference between iterator and generator with a small example.

from typing import Iterator

# Constants
SEQUENCE_LIMIT = 3


def generate_square_numbers(limit: int) -> Iterator[int]:
    """Yield square numbers from 1 to the given limit."""

    for current_number in range(1, limit + 1):
        yield current_number ** 2


class NumberSequenceIterator:
    """Custom iterator that returns numbers from 1 to N."""


    def __init__(self, limit: int) -> None:
        """Initialize the iterator with the upper limit."""
        self.limit = limit
        self.current_number = 1

    def __iter__(self) -> "NumberSequenceIterator":
        """Return the iterator object itself."""
        return self

    def __next__(self) -> int:
        """Return the next number in the sequence."""

        if self.current_number > self.limit:
            raise StopIteration

        next_number = self.current_number
        self.current_number += 1

        return next_number



def explain_iterator_vs_generator() -> None:
    """Demonstrate the difference between an iterator and a generator."""

    print("Iterator Example:")
    iterator_example = NumberSequenceIterator(
        SEQUENCE_LIMIT
    )
    print(list(iterator_example))

    print("\nGenerator Example:")
    generator_example = generate_square_numbers(
        SEQUENCE_LIMIT
    )
    
    print(list(generator_example))

    print(
        "\nDifference: Iterators are created manually using "
        "__iter__() and __next__(), while generators use "
        "yield and automatically implement iterator behavior."
    )


if __name__ == "__main__":
    explain_iterator_vs_generator()