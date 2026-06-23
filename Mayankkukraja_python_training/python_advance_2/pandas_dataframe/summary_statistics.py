"""
Generate summary statistics for an employee DataFrame.

This program creates an employee DataFrame and
displays statistical information for numeric columns.
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


def generate_summary_statistics() -> pd.DataFrame:
    """
    Generate summary statistics for the employee dataset.

    Returns:
        pd.DataFrame: Summary statistics table.
    """
    employee_dataframe = pd.DataFrame(EMPLOYEE_DATA)

    return employee_dataframe.describe()


def main() -> None:
    """
    Execute the summary statistics example.
    """
    summary_statistics = generate_summary_statistics()

    print("Summary Statistics:")
    print(summary_statistics)


if __name__ == "__main__":
    main()