"""
Calculate statistical values for a NumPy array.

This program calculates:
1. Mean
2. Maximum value
3. Minimum value
4. Sum of all elements
"""

import numpy as np

ARRAY_VALUES: list[int] = [10, 20, 30, 40, 50]


def calculate_array_statistics() -> dict[str, float]:
    """
    Calculate statistical values for the predefined array.

    Returns:
        dict[str, float]: Calculated statistical values.
    """
    array_data = np.array(ARRAY_VALUES)

    statistics = {
        "mean_value": float(np.mean(array_data)),
        "maximum_value": float(np.max(array_data)),
        "minimum_value": float(np.min(array_data)),
        "total_sum": float(np.sum(array_data)),
    }

    return statistics


def main() -> None:
    """
    Execute the statistics calculation example.
    """
    statistics = calculate_array_statistics()

    print(f"Mean: {statistics['mean_value']}")
    print(f"Maximum Value: {statistics['maximum_value']}")
    print(f"Minimum Value: {statistics['minimum_value']}")
    print(f"Sum: {statistics['total_sum']}")


if __name__ == "__main__":
    main()