# Second module inside sample_package


def add_two_numbers(
        first_number: float,
        second_number: float
) -> float:
    """Return the sum of two numbers."""

    return first_number + second_number


def multiply_two_numbers(
        first_number: float,
        second_number: float
) -> float:
    """Return the product of two numbers."""

    return first_number * second_number


if __name__ == "__main__":
    print(
        f"3 + 4 = "
        f"{add_two_numbers(3, 4)}"
    )

    print(
        f"3 * 4 = "
        f"{multiply_two_numbers(3, 4)}"
    )