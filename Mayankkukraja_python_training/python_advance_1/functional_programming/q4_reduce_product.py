# Q4 - Use reduce() to find the product of all elements in a list.

from functools import reduce

# Constants
NUMBER_LIST = [1, 2, 3, 4, 5]


def calculate_product(numbers: list[int]) -> int:
    """Use reduce() to find the product of all elements in a list."""

    product = reduce(
        lambda first_number, second_number:
        first_number * second_number,
        numbers
    )

    print(f"Numbers: {numbers}")
    print(f"Product: {product}")

    return product


if __name__ == "__main__":
    calculate_product(NUMBER_LIST)