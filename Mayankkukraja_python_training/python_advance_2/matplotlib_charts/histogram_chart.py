"""
Create a histogram to visualize salary distribution.

This program displays the frequency distribution
of salary values using a histogram.
"""

import matplotlib.pyplot as plt

SALARY_VALUES: list[int] = [
    30000,
    40000,
    50000,
    60000,
    45000,
]

FIGURE_WIDTH: int = 8
FIGURE_HEIGHT: int = 5
BIN_COUNT: int = 5


def create_histogram() -> None:
    """
    Create and display a histogram of salary values.
    """
    plt.figure(figsize=(FIGURE_WIDTH, FIGURE_HEIGHT))

    plt.hist(
        SALARY_VALUES,
        bins=BIN_COUNT,
        edgecolor="black"
    )

    plt.title("Salary Distribution")
    plt.xlabel("Salary")
    plt.ylabel("Frequency")

    plt.show()


if __name__ == "__main__":
    create_histogram()