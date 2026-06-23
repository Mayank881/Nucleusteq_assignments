"""
Perform arithmetic operations on two NumPy arrays.

Operations performed:
1. Addition
2. Element-wise multiplication
"""

import numpy as np

FIRST_ARRAY_DATA: list[int] = [1, 2, 3]
SECOND_ARRAY_DATA: list[int] = [4, 5, 6]


def perform_array_operations() -> tuple[np.ndarray, np.ndarray]:
    """
    Perform addition and element-wise multiplication on two arrays.

    Returns:
        tuple[np.ndarray, np.ndarray]:
            Addition result and multiplication result.
    """
    first_array_data = np.array(FIRST_ARRAY_DATA)
    second_array_data = np.array(SECOND_ARRAY_DATA)

    addition_result = first_array_data + second_array_data
    multiplication_result = first_array_data * second_array_data

    return addition_result, multiplication_result


def main() -> None:
    """
    Execute NumPy arithmetic operations.
    """
    addition_result, multiplication_result = perform_array_operations()

    print("Addition Result:")
    print(addition_result)

    print("\nMultiplication Result:")
    print(multiplication_result)


if __name__ == "__main__":
    main()