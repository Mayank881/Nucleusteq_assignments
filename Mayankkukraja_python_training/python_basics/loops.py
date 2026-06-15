# Q12, Q13, Q14, Q15, Q16 - Loops

TABLE_NUM = 5
FACT_NUM = 6
REVERSE_NUM = 12345
PRIME_NUM = 29


def print_one_to_hundred() -> None:
    """Print numbers from 1 to 100."""
    for i in range(1, 101):
        print(i, end=" ")
    print()


def multiplication_table(num: int) -> None:
    """Print multiplication table of a number."""
    print(f"\nMultiplication table of {num}:")

    for i in range(1, 11):
        print(f"{num} x {i} = {num * i}")


def factorial(num: int) -> None:
    """Calculate factorial of a number."""
    result = 1

    for i in range(2, num + 1):
        result *= i

    print(f"Factorial of {num} = {result}")


def reverse_number(num: int) -> None:
    """Reverse the digits of a number."""
    reversed_num = 0
    temp_num = abs(num)

    while temp_num > 0:
        digit = temp_num % 10
        reversed_num = reversed_num * 10 + digit
        temp_num //= 10

    print(f"Reverse of {num} = {reversed_num}")


def check_prime(num: int) -> None:
    """Check whether a number is prime."""

    if num < 2:
        print(f"{num} is not a Prime Number")
        return

    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            print(f"{num} is not a Prime Number")
            return

    print(f"{num} is a Prime Number")


if __name__ == "__main__":
    print_one_to_hundred()
    multiplication_table(TABLE_NUM)
    factorial(FACT_NUM)
    reverse_number(REVERSE_NUM)
    check_prime(PRIME_NUM)