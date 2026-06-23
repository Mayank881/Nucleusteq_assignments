"""
Count employees in each department.

This program groups employee records by department
and calculates the number of employees in each group.
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

DEPARTMENT_COLUMN: str = "Department"


def create_employee_dataframe() -> pd.DataFrame:
    """
    Create an employee DataFrame.

    Returns:
        pd.DataFrame: Employee dataset.
    """
    return pd.DataFrame(EMPLOYEE_DATA)


def count_employees_by_department() -> pd.Series:
    """
    Count employees in each department.

    Returns:
        pd.Series: Employee count grouped by department.
    """
    employee_dataframe = create_employee_dataframe()

    return employee_dataframe.groupby(
        DEPARTMENT_COLUMN
    ).size()


def main() -> None:
    """
    Execute the employee count analysis example.
    """
    employee_count = count_employees_by_department()

    print("Employee Count by Department:")
    print(employee_count)


if __name__ == "__main__":
    main()