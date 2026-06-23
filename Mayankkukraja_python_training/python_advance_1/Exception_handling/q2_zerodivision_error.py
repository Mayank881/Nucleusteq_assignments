# Q2 - Divide two numbers entered by the user and handle ZeroDivisionError.

def divide_numbers() -> None:
    """Divide two numbers and handle ZeroDivisionError."""

    try:
        numerator = float(input("Enter  numerator : "))
        denomenator = float(input("Enter  denomenator: "))

        division_result =  numerator  / denomenator
        print(f"Result: {division_result}")

    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")


if __name__ == "__main__":
    divide_numbers()