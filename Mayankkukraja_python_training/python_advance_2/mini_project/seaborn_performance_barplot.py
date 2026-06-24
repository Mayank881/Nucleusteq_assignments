"""
Create a Seaborn barplot showing performance versus marks.

This program classifies students as Pass or Fail
and visualizes their marks using a Seaborn barplot.
"""

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

from student_data import STUDENT_DATA

PASSING_MARKS: int = 65

MARKS_COLUMN: str = "Marks"
PERFORMANCE_COLUMN: str = "Performance"

FIGURE_WIDTH: int = 8
FIGURE_HEIGHT: int = 5


def create_performance_barplot() -> None:
    """
    Create and display a barplot showing
    performance versus marks.
    """
    student_dataframe = pd.DataFrame(STUDENT_DATA)

    student_dataframe[PERFORMANCE_COLUMN] = (
        student_dataframe[MARKS_COLUMN]
        .apply(
            lambda marks: (
                "Pass"
                if marks > PASSING_MARKS
                else "Fail"
            )
        )
    )

    plt.figure(figsize=(FIGURE_WIDTH, FIGURE_HEIGHT))

    sns.barplot(
        data=student_dataframe,
        x=PERFORMANCE_COLUMN,
        y=MARKS_COLUMN,
    )

    plt.title("Performance vs Marks")
    plt.xlabel("Performance")
    plt.ylabel("Marks")

    plt.show()


if __name__ == "__main__":
    create_performance_barplot()