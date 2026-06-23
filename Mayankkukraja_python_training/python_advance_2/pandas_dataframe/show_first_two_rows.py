"""
Display the first two rows of an employee DataFrame.

This program creates an employee DataFrame and
retrieves the first two records.
"""

import pandas as pd

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

ROW_COUNT: int = 2


def get_first_two_rows() -> pd.DataFrame:
    """
    Retrieve the first two rows from the employee DataFrame.

    Returns:
        pd.DataFrame: DataFrame containing the first two records.
    """
    employee_dataframe = pd.DataFrame(EMPLOYEE_DATA)

    return employee_dataframe.head(ROW_COUNT)


def main() -> None:
    """
    Execute the first two rows example.
    """
    first_two_rows = get_first_two_rows()

    print("First Two Rows:")
    print(first_two_rows)


if __name__ == "__main__":
    main()