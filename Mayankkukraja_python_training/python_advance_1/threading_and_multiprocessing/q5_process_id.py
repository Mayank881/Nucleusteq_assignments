# Q5 - Write a program to create two processes that print their Process IDs.

import multiprocessing
import os


def print_process_id(
        process_label: str
) -> None:
    """Print the Process ID of the current process."""

    print(
        f"[{process_label}] "
        f"Process ID: {os.getpid()}"
    )


def create_two_processes_printing_pid() -> None:
    """Create two processes and print their PIDs."""

    process_one = multiprocessing.Process(
        target=print_process_id,
        args=("Process-1",)
    )

    process_two = multiprocessing.Process(
        target=print_process_id,
        args=("Process-2",)
    )

    process_one.start()
    process_two.start()

    process_one.join()
    process_two.join()


if __name__ == "__main__":
    create_two_processes_printing_pid()