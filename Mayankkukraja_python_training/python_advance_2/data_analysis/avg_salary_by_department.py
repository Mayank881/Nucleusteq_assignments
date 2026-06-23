"""
Calculate the average salary for each department.

This program groups employee records by department
and calculates the average salary for each group.
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


def calculate_average_salary_by_department() -> pd.Series:
    """
    Calculate the average salary for each department.

    Returns:
        pd.Series: Average salary grouped by department.
    """
    employee_dataframe = create_employee_dataframe()

    return employee_dataframe.groupby(
        DEPARTMENT_COLUMN
    )[SALARY_COLUMN].mean()


def main() -> None:
    """
    Execute the average salary analysis example.
    """
    average_salary = calculate_average_salary_by_department()

    print("Average Salary by Department:")
    print(average_salary)


if __name__ == "__main__":
    main()