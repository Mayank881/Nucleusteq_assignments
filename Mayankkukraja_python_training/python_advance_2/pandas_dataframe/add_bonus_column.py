"""
Add a bonus column to an employee DataFrame.

This program calculates a bonus equal to
10 percent of each employee's salary and
stores the result in a new column.
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

BONUS_PERCENTAGE: float = 0.10


def add_bonus_column() -> pd.DataFrame:
    """
    Add a bonus column to the employee DataFrame.

    Bonus is calculated as 10 percent of salary.

    Returns:
        pd.DataFrame: Employee DataFrame with bonus column.
    """
    employee_dataframe = pd.DataFrame(EMPLOYEE_DATA)

    employee_dataframe["Bonus"] = (
        employee_dataframe["Salary"] * BONUS_PERCENTAGE
    )

    return employee_dataframe


def main() -> None:
    """
    Execute the bonus calculation example.
    """
    employee_dataframe = add_bonus_column()

    print("Employee DataFrame with Bonus:")
    print(employee_dataframe)


if __name__ == "__main__":
    main()