# Q6 - Write a recursive function to calculate Fibonacci.

# Constants
FIBONACCI_POSITION = 7


def calculate_fibonacci(position: int) -> int:
    """Calculate the Fibonacci number at a given position using recursion."""

    if position <= 0:
        return 0

    if position == 1:
        return 1

    return (
        calculate_fibonacci(position - 1)
        + calculate_fibonacci(position - 2)
    )


if __name__ == "__main__":
    print(
        f"Fibonacci at position "
        f"{FIBONACCI_POSITION} = "
        f"{calculate_fibonacci(FIBONACCI_POSITION)}"
    )