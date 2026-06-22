# Q5 - Write a recursive function to calculate factorial.

# Constants
FACTORIAL_NUMBER = 6


def calculate_factorial(number: int) -> int:
    """Calculate the factorial of a number using recursion."""

    if number <= 1:
        return 1

    return number * calculate_factorial(number - 1)


if __name__ == "__main__":
    print(
        f"Factorial of {FACTORIAL_NUMBER} = "
        f"{calculate_factorial(FACTORIAL_NUMBER)}"
    )