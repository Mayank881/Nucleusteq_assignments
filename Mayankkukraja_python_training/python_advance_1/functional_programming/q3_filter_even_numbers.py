# Q3 - Use filter() to extract even numbers from a list.

# Constants
NUMBER_LIST = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def extract_even_numbers(
        numbers: list[int]
) -> list[int]:
    """Use filter() to extract even numbers from a list."""

    even_numbers = list(
        filter(
            lambda current_number: current_number % 2 == 0,
            numbers
        )
    )

    print(f"Original Numbers: {numbers}")
    print(f"Even Numbers: {even_numbers}")

    return even_numbers


if __name__ == "__main__":
    extract_even_numbers(
        NUMBER_LIST
    )