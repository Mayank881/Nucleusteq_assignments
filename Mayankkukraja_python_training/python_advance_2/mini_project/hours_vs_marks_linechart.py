"""
Create a line chart showing hours studied versus marks.

This program visualizes the relationship between
study hours and student marks using a line chart.
"""

import matplotlib.pyplot as plt
import pandas as pd

from student_data import STUDENT_DATA

HOURS_STUDIED_COLUMN: str = "Hours Studied"
MARKS_COLUMN: str = "Marks"

FIGURE_WIDTH: int = 8
FIGURE_HEIGHT: int = 5
MARKER_STYLE: str = "o"


def create_line_chart() -> None:
    """
    Create and display a line chart showing
    hours studied versus marks.
    """
    student_dataframe = pd.DataFrame(STUDENT_DATA)

    plt.figure(figsize=(FIGURE_WIDTH, FIGURE_HEIGHT))

    plt.plot(
        student_dataframe[HOURS_STUDIED_COLUMN],
        student_dataframe[MARKS_COLUMN],
        marker=MARKER_STYLE,
    )

    plt.title("Hours Studied vs Marks")
    plt.xlabel("Hours Studied")
    plt.ylabel("Marks")

    plt.show()


if __name__ == "__main__":
    create_line_chart()