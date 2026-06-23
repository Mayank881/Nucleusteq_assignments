"""
Create a Seaborn barplot showing department-wise salary.

This program visualizes the relationship between
department and salary using a Seaborn barplot.
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

DEPARTMENT_COLUMN: str = "Department"
SALARY_COLUMN: str = "Salary"

FIGURE_WIDTH: int = 8
FIGURE_HEIGHT: int = 5


def create_department_salary_barplot() -> None:
    """
    Create and display a Seaborn barplot showing
    department-wise salary.
    """
    employee_dataframe = pd.DataFrame(EMPLOYEE_DATA)

    plt.figure(figsize=(FIGURE_WIDTH, FIGURE_HEIGHT))

    sns.barplot(
        data=employee_dataframe,
        x=DEPARTMENT_COLUMN,
        y=SALARY_COLUMN,
    )

    plt.title("Department vs Salary")
    plt.xlabel("Department")
    plt.ylabel("Salary")

    plt.show()


if __name__ == "__main__":
    create_department_salary_barplot()