# Q7, Q8, Q9, Q10, Q11 - Operators and Conditionals

NUMBER = 7
SIGN_NUMBER = -3
FIRST_NUM, SECOND_NUM, THIRD_NUM = 10, 32, 30
MARKS = 88
YEAR = 2024


def check_even_odd(number: int) -> None:
    """Check whether a number is even or odd."""
    if number % 2 == 0:
        print(f"{number} is Even")
    else:
        print(f"{number} is Odd")


def check_sign(number: int) -> None:
    """Check whether a number is positive, negative or zero."""
    if number > 0:
        print(f"{number} is Positive")
    elif number < 0:
        print(f"{number} is Negative")
    else:
        print("The number is Zero")


def find_largest(first_num: int, second_num: int, third_num: int) -> None:
    """Find and print the largest among three numbers."""
    largest = max(first_num, second_num, third_num)
    print(
        f"Largest of {first_num}, {second_num}, {third_num} is: {largest}"
    )


def calculate_grade(marks: int) -> None:
    """Calculate grade based on marks."""
    if marks >= 90:
        grade = "A"
    elif marks >= 75:
        grade = "B"
    elif marks >= 60:
        grade = "C"
    else:
        grade = "Fail"

    print(f"Marks: {marks} => Grade: {grade}")


def check_leap_year(year: int) -> None:
    """Check whether a year is a leap year."""
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print(f"{year} is a Leap Year")
    else:
        print(f"{year} is NOT a Leap Year")


if __name__ == "__main__":
    check_even_odd(NUMBER)
    check_sign(SIGN_NUMBER)
    find_largest(FIRST_NUM, SECOND_NUM, THIRD_NUM)
    calculate_grade(MARKS)
    check_leap_year(YEAR)