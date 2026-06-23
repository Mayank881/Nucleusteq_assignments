"""
Create a scatter plot showing the relationship
between age and salary.

This program visualizes employee age and salary
using a scatter plot.
"""

import matplotlib.pyplot as plt

AGE_VALUES: list[int] = [
    25,
    30,
    28,
    35,
]

SALARY_VALUES: list[int] = [
    30000,
    50000,
    45000,
    60000,
]

FIGURE_WIDTH: int = 8
FIGURE_HEIGHT: int = 5


def create_scatter_plot() -> None:
    """
    Create and display a scatter plot of age
    versus salary.
    """
    plt.figure(figsize=(FIGURE_WIDTH, FIGURE_HEIGHT))

    plt.scatter(
        AGE_VALUES,
        SALARY_VALUES
    )

    plt.title("Age vs Salary")
    plt.xlabel("Age")
    plt.ylabel("Salary")

    plt.show()


if __name__ == "__main__":
    create_scatter_plot()