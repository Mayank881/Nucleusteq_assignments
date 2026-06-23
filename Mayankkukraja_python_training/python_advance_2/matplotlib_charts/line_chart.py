"""
Create a line chart showing employee count
across departments.
"""

import matplotlib.pyplot as plt

DEPARTMENTS: list[str] = ["HR", "IT", "Finance"]
EMPLOYEE_COUNTS: list[int] = [5, 12, 7]

FIGURE_WIDTH: int = 8
FIGURE_HEIGHT: int = 5
MARKER_STYLE: str = "o"


def create_line_chart() -> None:
    """
    Create and display a line chart for employee
    counts across departments.
    """
    plt.figure(figsize=(FIGURE_WIDTH, FIGURE_HEIGHT))

    plt.plot(
        DEPARTMENTS,
        EMPLOYEE_COUNTS,
        marker=MARKER_STYLE
    )

    plt.title("Employee Count by Department")
    plt.xlabel("Department")
    plt.ylabel("Number of Employees")

    plt.show()


if __name__ == "__main__":
    create_line_chart()