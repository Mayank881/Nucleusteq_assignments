"""
Create a scatter plot showing study hours versus marks.

This program visualizes the relationship between
hours studied and marks obtained by students.
"""

import matplotlib.pyplot as plt
import pandas as pd

from student_data import STUDENT_DATA

HOURS_STUDIED_COLUMN: str = "Hours Studied"
MARKS_COLUMN: str = "Marks"

FIGURE_WIDTH: int = 8
FIGURE_HEIGHT: int = 5


def create_scatter_plot() -> None:
    """
    Create and display a scatter plot showing
    study hours versus marks.
    """
    student_dataframe = pd.DataFrame(STUDENT_DATA)

    plt.figure(figsize=(FIGURE_WIDTH, FIGURE_HEIGHT))

    plt.scatter(
        student_dataframe[HOURS_STUDIED_COLUMN],
        student_dataframe[MARKS_COLUMN],
    )

    plt.title("Study Hours vs Marks")
    plt.xlabel("Hours Studied")
    plt.ylabel("Marks")

    plt.show()


if __name__ == "__main__":
    create_scatter_plot()
    