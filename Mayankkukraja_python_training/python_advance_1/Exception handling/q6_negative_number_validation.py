# Q6 - Create a function that raises a ValueError if a number is negative.

# Constants
TEST_NUMBER = 0


def validate_non_negative_number(number: int | float) -> int | float:
    """Raise a ValueError if the given number is negative."""

    if number < 0:
        raise ValueError(
            f"Number must not be negative, got {number}."
        )

    return number


if __name__ == "__main__":

    try:
        validate_non_negative_number(TEST_NUMBER)

    except ValueError as error:
        print(f"Caught error: {error}")