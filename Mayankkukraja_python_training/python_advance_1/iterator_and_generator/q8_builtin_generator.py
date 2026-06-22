# Q8 - Show an example of a built-in generator (like range)
# and iterate over it.

# Constants
START_NUMBER = 1
END_NUMBER = 5


def print_range_values(
        start_number: int,
        end_number: int
) -> None:
    """Iterate over a built-in range object and print its values."""

    range_iterator = iter(
        range(
            start_number,
            end_number + 1
        )
    )

    for current_number in range_iterator:
        print(current_number)


if __name__ == "__main__":
    print_range_values(
        START_NUMBER,
        END_NUMBER
    )