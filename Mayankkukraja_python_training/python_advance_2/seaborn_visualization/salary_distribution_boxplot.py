"""
Create a boxplot to visualize salary distribution.

This program displays the distribution of employee
salaries using a Seaborn boxplot.
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

SALARY_COLUMN: str = "Salary"

FIGURE_WIDTH: int = 8
FIGURE_HEIGHT: int = 5


def create_salary_boxplot() -> None:
    """
    Create and display a boxplot showing
    salary distribution.
    """
    employee_dataframe = pd.DataFrame(EMPLOYEE_DATA)

    plt.figure(figsize=(FIGURE_WIDTH, FIGURE_HEIGHT))

    sns.boxplot(
        y=employee_dataframe[SALARY_COLUMN]
    )

    plt.title("Salary Distribution")
    plt.ylabel("Salary")

    plt.show()


if __name__ == "__main__":
    create_salary_boxplot()