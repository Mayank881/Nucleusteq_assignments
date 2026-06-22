# Q2 - Use map() to convert a list of numbers into their squares.

# Constants
NUMBER_LIST = [1, 2, 3, 4, 5]


def convert_numbers_to_squares(
        numbers: list[int]
) -> list[int]:
    """Use map() to convert a list of numbers into their squares."""

    squared_numbers = list(
        map(
            lambda current_number: current_number ** 2,
            numbers
        )
    )

    print(f"Original Numbers: {numbers}")
    print(f"Squared Numbers: {squared_numbers}")

    return squared_numbers


if __name__ == "__main__":
    convert_numbers_to_squares(
        NUMBER_LIST
    )