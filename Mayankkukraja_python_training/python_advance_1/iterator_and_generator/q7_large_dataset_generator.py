# Q7 - Process a large dataset using a generator instead of storing all values in a list.

# Constants
LARGE_DATASET_SIZE = 1_000_000


def generate_large_dataset(dataset_size: int):
    """Yield dataset values one at a time."""

    for current_number in range(dataset_size):
        yield current_number


def process_large_dataset(dataset_size: int) -> int:
    """Process a large dataset using a generator."""

    dataset_generator = generate_large_dataset(
        dataset_size
    )

    total_sum = sum(dataset_generator)

    print(
        f"Sum of numbers from 0 to "
        f"{dataset_size - 1}: {total_sum}"
    )

    return total_sum


if __name__ == "__main__":
    process_large_dataset(
        LARGE_DATASET_SIZE
    )