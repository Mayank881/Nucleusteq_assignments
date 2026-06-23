# Q3 - Use modules from a package.

from sample_package.greeting_module import (
    greet_morning,
    greet_evening
)

from sample_package.calculator_module import (
    add_two_numbers,
    multiply_two_numbers
)


def demonstrate_package_usage() -> None:
    """Use functions from both modules."""

    print(greet_morning("Mayank"))
    print(greet_evening("Mayank"))

    print(
        f"Addition: "
        f"{add_two_numbers(10, 20)}"
    )

    print(
        f"Multiplication: "
        f"{multiply_two_numbers(10, 20)}"
    )


if __name__ == "__main__":
    demonstrate_package_usage()