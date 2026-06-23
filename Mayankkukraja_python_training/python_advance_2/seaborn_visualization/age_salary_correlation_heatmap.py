"""
Create a heatmap showing the correlation between
age and salary.

This program calculates the correlation matrix
for employee age and salary and visualizes it
using a Seaborn heatmap.
"""

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

EMPLOYEE_DATA: dict[str, list] = {
    "Name": [
        "Rahul",
        "Priya",
        "Amit",
        "Anuj",
    ],
    "Age": [
        25,
        30,
        28,
        35,
    ],
    "Department": [
        "HR",
        "IT",
        "Finance",
        "IT",
    ],
    "Salary": [
        30000,
        50000,
        45000,
        60000,
    ],
}

AGE_COLUMN: str = "Age"
SALARY_COLUMN: str = "Salary"

FIGURE_WIDTH: int = 6
FIGURE_HEIGHT: int = 4


def create_age_salary_correlation_heatmap() -> None:
    """
    Create and display a heatmap showing the
    correlation between age and salary.
    """
    employee_dataframe = pd.DataFrame(EMPLOYEE_DATA)

    correlation_matrix = employee_dataframe[
        [AGE_COLUMN, SALARY_COLUMN]
    ].corr()

    plt.figure(figsize=(FIGURE_WIDTH, FIGURE_HEIGHT))

    sns.heatmap(
        correlation_matrix,
        annot=True,
        cmap="Blues",
    )

    plt.title("Age and Salary Correlation")

    plt.show()


if __name__ == "__main__":
    create_age_salary_correlation_heatmap()