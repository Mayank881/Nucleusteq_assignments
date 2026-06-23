# Q1 - Write a lambda function to find the square of a number.

# Constants
TEST_NUMBER = 6

# Lambda function to calculate square
square_function = lambda number: number ** 2


if __name__ == "__main__":
    print(
        f"Square of {TEST_NUMBER} = "
        f"{square_function(TEST_NUMBER)}"
    )