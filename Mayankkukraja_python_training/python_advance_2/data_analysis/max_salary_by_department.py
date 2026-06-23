"""
Find the maximum salary for each department.

This program groups employee records by department
and determines the highest salary in each department.
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
SALARY_COLUMN: str = "Salary"


def create_employee_dataframe() -> pd.DataFrame:
    """
    Create an employee DataFrame.

    Returns:
        pd.DataFrame: Employee dataset.
    """
    return pd.DataFrame(EMPLOYEE_DATA)


def calculate_max_salary_by_department() -> pd.Series:
    """
    Calculate the maximum salary for each department.

    Returns:
        pd.Series: Maximum salary grouped by department.
    """
    employee_dataframe = create_employee_dataframe()

    return employee_dataframe.groupby(
        DEPARTMENT_COLUMN
    )[SALARY_COLUMN].max()


def main() -> None:
    """
    Execute the maximum salary analysis example.
    """
    maximum_salary = calculate_max_salary_by_department()

    print("Maximum Salary by Department:")
    print(maximum_salary)


if __name__ == "__main__":
    main()