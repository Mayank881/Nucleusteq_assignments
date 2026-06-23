"""
Detect missing values in an employee dataset.

This program creates a DataFrame containing
missing values and identifies their locations.
"""

import pandas as pd

EMPLOYEE_DATA: dict[str, list] = {
    "Name": ["Rahul", "Priya", "Anuj"],
    "Age": [25, None, 29],
    "Salary": [30000, 40000, None],
}


def create_employee_dataframe() -> pd.DataFrame:
    """
    Create a DataFrame containing employee information.

    Returns:
        pd.DataFrame: Employee DataFrame.
    """
    return pd.DataFrame(EMPLOYEE_DATA)


def detect_missing_values() -> pd.DataFrame:
    """
    Identify missing values in the DataFrame.

    Returns:
        pd.DataFrame: Boolean DataFrame indicating missing values.
    """
    employee_dataframe = create_employee_dataframe()

    return employee_dataframe.isnull()


def main() -> None:
    """
    Execute the missing value detection example.
    """
    missing_values = detect_missing_values()

    print("Missing Values:")
    print(missing_values)


if __name__ == "__main__":
    main()