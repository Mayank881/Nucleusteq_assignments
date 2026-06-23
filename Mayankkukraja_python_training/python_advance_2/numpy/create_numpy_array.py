"""
Create and display a NumPy array.

This program demonstrates how to create a NumPy array
using predefined integer values.
"""

import numpy as np

ARRAY_VALUES: list[int] = [10, 20, 30, 40, 50]


def create_numpy_array() -> np.ndarray:
    """
    Create a NumPy array from predefined values.

    Returns:
        np.ndarray: NumPy array containing the specified values.
    """
    return np.array(ARRAY_VALUES)


def main() -> None:
    """
    Execute the NumPy array creation example.
    """
    numbers_array = create_numpy_array()

    print("NumPy Array:")
    print(numbers_array)


if __name__ == "__main__":
    main()
    