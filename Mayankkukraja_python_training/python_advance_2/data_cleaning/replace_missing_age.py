"""
Replace missing age values with the mean age.

This program calculates the average age from
available records and replaces missing values
in the Age column.
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


def replace_missing_age_with_mean() -> pd.DataFrame:
    """
    Replace missing age values with the mean age.

    Returns:
        pd.DataFrame: Updated DataFrame.
    """
    employee_dataframe = create_employee_dataframe()

    mean_age = employee_dataframe["Age"].mean()

    employee_dataframe["Age"] = employee_dataframe["Age"].fillna(
        mean_age
    )

    return employee_dataframe


def main() -> None:
    """
    Execute the missing age replacement example.
    """
    updated_dataframe = replace_missing_age_with_mean()

    print("DataFrame After Replacing Missing Age:")
    print(updated_dataframe)


if __name__ == "__main__":
    main()