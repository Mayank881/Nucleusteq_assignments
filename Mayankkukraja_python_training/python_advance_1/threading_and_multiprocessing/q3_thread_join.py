# Q3 - Demonstrate the use of join() method in threading.

import threading
import time

# Constants
SLEEP_SECONDS = 2


def slow_task(task_name: str) -> None:
    """Simulate a slow task."""

    print(f"{task_name} started.")

    time.sleep(
        SLEEP_SECONDS
    )

    print(f"{task_name} finished.")


def demonstrate_join_method() -> None:
    """Demonstrate how join() works."""

    task_thread = threading.Thread(
        target=slow_task,
        args=("Task-1",)
    )

    task_thread.start()

    print(
        "Main program is waiting "
        "for the thread to finish..."
    )

    task_thread.join()

    print(
        "Main program continues "
        "after the thread finishes."
    )


if __name__ == "__main__":
    demonstrate_join_method()