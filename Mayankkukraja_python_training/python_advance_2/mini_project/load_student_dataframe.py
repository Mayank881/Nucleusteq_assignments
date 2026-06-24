"""
Load student data into a Pandas DataFrame.

This program creates and displays a DataFrame
containing student performance information.
"""

import pandas as pd

from student_data import STUDENT_DATA


def load_student_dataframe() -> pd.DataFrame:
    """
    Create a DataFrame from the student dataset.

    Returns:
        pd.DataFrame: Student DataFrame.
    """
    return pd.DataFrame(STUDENT_DATA)


def main() -> None:
    """
    Execute the student DataFrame loading example.
    """
    student_dataframe = load_student_dataframe()

    print("Student DataFrame:")
    print(student_dataframe)


if __name__ == "__main__":
    main()