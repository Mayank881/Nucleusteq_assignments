"""
Create and display a 3x3 matrix using NumPy.

This program generates a matrix containing
values from 1 to 9 arranged in 3 rows and 3 columns.
"""

import numpy as np

MATRIX_ROW_COUNT: int = 3
MATRIX_COLUMN_COUNT: int = 3
START_VALUE: int = 1
END_VALUE: int = 10


def create_matrix() -> np.ndarray:
    """
    Create a 3x3 NumPy matrix.

    Returns:
        np.ndarray: Generated 3x3 matrix.
    """
    return np.arange(
        START_VALUE,
        END_VALUE
    ).reshape(
        MATRIX_ROW_COUNT,
        MATRIX_COLUMN_COUNT
    )


def main() -> None:
    """
    Execute the matrix creation example.
    """
    matrix_data = create_matrix()

    print("3x3 Matrix:")
    print(matrix_data)


if __name__ == "__main__":
    main()