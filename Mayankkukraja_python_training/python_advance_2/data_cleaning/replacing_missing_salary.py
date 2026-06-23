"""
Replace missing salary values with zero.

This program identifies missing values in the
Salary column and replaces them with a default value.
"""

import pandas as pd

EMPLOYEE_DATA: dict[str, list] = {
    "Name": ["Rahul", "Priya", "Anuj"],
    "Age": [25, None, 29],
    "Salary": [30000, 40000, None],
}

DEFAULT_SALARY: int = 0


def create_employee_dataframe() -> pd.DataFrame:
    """
    Create a DataFrame containing employee information.

    Returns:
        pd.DataFrame: Employee DataFrame.
    """
    return pd.DataFrame(EMPLOYEE_DATA)


def replace_missing_salary_with_zero() -> pd.DataFrame:
    """
    Replace missing salary values with zero.

    Returns:
        pd.DataFrame: Updated DataFrame.
    """
    employee_dataframe = create_employee_dataframe()

    employee_dataframe["Salary"] = employee_dataframe[
        "Salary"
    ].fillna(DEFAULT_SALARY)

    return employee_dataframe


def main() -> None:
    """
    Execute the salary replacement example.
    """
    updated_dataframe = replace_missing_salary_with_zero()

    print("DataFrame After Replacing Missing Salary:")
    print(updated_dataframe)


if __name__ == "__main__":
    main()