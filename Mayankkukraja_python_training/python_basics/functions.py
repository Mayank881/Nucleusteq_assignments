# Q17, Q18, Q19, Q20 - Functions

SQUARE_NUM = 9
PALINDROME_NUM = 121
PALINDROME_TEXT = "racecar"
NORMAL_TEXT = "hello"
NUM_LIST = [3, 7, 1, 9, 4]
USER_NAME = "Mayank"


def square(num: int) -> int:
    """Return the square of a number."""
    return num ** 2


def is_palindrome(value: str | int) -> None:
    """Check if a value is palindrome or not."""
    text = str(value)

    if text == text[::-1]:
        print(f"'{value}' is a Palindrome")
    else:
        print(f"'{value}' is not a Palindrome")


def find_max(numbers: list[int]) -> int:
    """Return the largest value from a list."""
    return max(numbers)


def greet(name: str, message: str = "Hello") -> None:
    """Display a greeting message."""
    print(f"{message}, {name}!")


if __name__ == "__main__":
    print(f"Square of {SQUARE_NUM} = {square(SQUARE_NUM)}")

    is_palindrome(PALINDROME_NUM)
    is_palindrome(PALINDROME_TEXT)
    is_palindrome(NORMAL_TEXT)

    print(f"Max in list: {find_max(NUM_LIST)}")

    greet(USER_NAME)
    greet(USER_NAME, "Namaste")