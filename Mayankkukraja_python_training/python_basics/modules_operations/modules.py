# Q22, Q23, Q24 - Modules

import math
import random

from custom_module import display_message

NUMBER = 25


def use_math_module() -> None:
    """Demonstrate sqrt, power and factorial using math module."""

    print(f"Square root of {NUMBER}: {math.sqrt(NUMBER)}")
    print(f"Power 2^8: {math.pow(2, 8)}")
    print(f"Factorial of 6: {math.factorial(6)}")


def generate_random() -> None:
    """Generate random values using random module."""

    print(f"Random number: {random.randint(1, 100)}")
    print(f"Random float: {round(random.random(), 4)}")
    print(f"Random language: {random.choice(['Python', 'Java', 'C++'])}")


def custom_module_demo() -> None:
    """Import and use a custom module."""

    display_message()


if __name__ == "__main__":
    use_math_module()
    generate_random()
    custom_module_demo()