# Q4 - Use a package for mathematical operations.

from math_operations.add_module import (
    add_numbers
)

from math_operations.subtract_module import (
    subtract_numbers
)

from math_operations.multiply_module import (
    multiply_numbers
)

from math_operations.divide_module import (
    divide_numbers
)


def demonstrate_math_operations() -> None:
    """Use functions from the math_operations package."""

    first_number = 20
    second_number = 10

    print(
        f"Addition: "
        f"{add_numbers(first_number, second_number)}"
    )

    print(
        f"Subtraction: "
        f"{subtract_numbers(first_number, second_number)}"
    )

    print(
        f"Multiplication: "
        f"{multiply_numbers(first_number, second_number)}"
    )

    print(
        f"Division: "
        f"{divide_numbers(first_number, second_number)}"
    )


if __name__ == "__main__":
    demonstrate_math_operations()