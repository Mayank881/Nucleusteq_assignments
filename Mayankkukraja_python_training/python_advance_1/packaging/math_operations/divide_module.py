# Divide module


def divide_numbers(
        first_number: float,
        second_number: float
) -> float:
    """Return the division of two numbers."""

    if second_number == 0:
        raise ValueError(
            "Cannot divide by zero."
        )

    return first_number / second_number