"""
Create a bar chart showing the number of employees
in each department.
"""

import matplotlib.pyplot as plt

DEPARTMENTS: list[str] = ["HR", "IT", "Finance"]
EMPLOYEE_COUNTS: list[int] = [5, 12, 7]

FIGURE_WIDTH: int = 8
FIGURE_HEIGHT: int = 5


def create_bar_chart() -> None:
    """
    Create and display a bar chart for employee counts
    across departments.
    """
    plt.figure(figsize=(FIGURE_WIDTH, FIGURE_HEIGHT))

    plt.bar(DEPARTMENTS, EMPLOYEE_COUNTS)

    plt.title("Employee Count by Department")
    plt.xlabel("Department")
    plt.ylabel("Number of Employees")

    plt.show()


if __name__ == "__main__":
    create_bar_chart()