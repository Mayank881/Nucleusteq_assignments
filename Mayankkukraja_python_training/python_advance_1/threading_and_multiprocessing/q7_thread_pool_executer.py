# Q7 - Convert a normal function into parallel execution using ThreadPoolExecutor.

from concurrent.futures import ThreadPoolExecutor

# Constants
NUMBERS_TO_SQUARE = [1, 2, 3, 4, 5]


def square_number(
        number: int
) -> int:
    """Return the square of a number."""

    return number ** 2


def convert_function_to_thread_pool(
        numbers: list[int]
) -> list[int]:
    """Execute a normal function using ThreadPoolExecutor."""

    with ThreadPoolExecutor() as executor:

        results = list(
            executor.map(
                square_number,
                numbers
            )
        )

    print(f"Numbers: {numbers}")
    print(
        f"Squares (ThreadPoolExecutor): "
        f"{results}"
    )

    return results


if __name__ == "__main__":
    convert_function_to_thread_pool(
        NUMBERS_TO_SQUARE
    )