# Q2 - Create a thread that calculates the sum of numbers from 1 to 100.

import threading

# Constants
SUM_RANGE_END = 100


def calculate_sum() -> None:
    """Calculate and print the sum of numbers from 1 to 100."""

    total = sum(
        range(
            1,
            SUM_RANGE_END + 1
        )
    )

    print(
        f"Sum of numbers from 1 to "
        f"{SUM_RANGE_END}: {total}"
    )


def create_sum_thread() -> None:
    """Create a thread that calculates the sum."""

    sum_thread = threading.Thread(
        target=calculate_sum
    )

    sum_thread.start()
    sum_thread.join()


if __name__ == "__main__":
    create_sum_thread()