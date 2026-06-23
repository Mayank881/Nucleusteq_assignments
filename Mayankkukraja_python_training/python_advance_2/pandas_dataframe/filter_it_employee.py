"""
Filter and display employees from the IT department.

This program creates an employee DataFrame and
retrieves only the employees who belong to the
IT department.
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

TARGET_DEPARTMENT: str = "IT"


def filter_it_employees() -> pd.DataFrame:
    """
    Retrieve employees belonging to the IT department.

    Returns:
        pd.DataFrame: Filtered DataFrame containing IT employees.
    """
    employee_dataframe = pd.DataFrame(EMPLOYEE_DATA)

    return employee_dataframe[
        employee_dataframe["Department"] == TARGET_DEPARTMENT
    ]


def main() -> None:
    """
    Execute the IT employee filtering example.
    """
    it_employees = filter_it_employees()

    print("IT Employees:")
    print(it_employees)


if __name__ == "__main__":
    main()