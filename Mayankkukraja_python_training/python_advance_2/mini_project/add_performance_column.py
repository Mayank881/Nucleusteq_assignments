"""
Add a performance column to the student dataset.

This program classifies students as Pass or Fail
based on their marks.
"""

import pandas as pd

from student_data import STUDENT_DATA

PASSING_MARKS: int = 65
MARKS_COLUMN: str = "Marks"
PERFORMANCE_COLUMN: str = "Performance"


def add_performance_column() -> pd.DataFrame:
    """
    Add a performance column based on student marks.

    Returns:
        pd.DataFrame: Updated student DataFrame.
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

    return student_dataframe


def main() -> None:
    """
    Execute the performance classification example.
    """
    student_dataframe = add_performance_column()

    print("Student Performance Data:")
    print(student_dataframe)


if __name__ == "__main__":
    main()