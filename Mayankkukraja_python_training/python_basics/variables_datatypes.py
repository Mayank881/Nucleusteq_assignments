# Q4, Q5, Q6 - Variables and Data Types


def show_data_types() -> None:
    """Create variables of different data types and display their types."""

    number = 10
    amount = 3.14
    user_name = "Mayank"
    is_active = True

    print(type(number))
    print(type(amount))
    print(type(user_name))
    print(type(is_active))


def swap_numbers() -> None:
    """Swap two numbers using Python's multiple assignment feature."""

    first_num = 5
    second_num = 10

    print(f"Before swap: first_num={first_num}, second_num={second_num}")

    first_num, second_num = second_num, first_num

    print(f"After swap: first_num={first_num}, second_num={second_num}")


def basic_arithmetic() -> None:
    """Perform basic arithmetic operations on two numbers."""

    first_num = 20
    second_num = 4

    print(f"Sum: {first_num + second_num}")
    print(f"Difference: {first_num - second_num}")
    print(f"Product: {first_num * second_num}")
    print(f"Division: {first_num / second_num}")


if __name__ == "__main__":
    show_data_types()
    swap_numbers()
    basic_arithmetic()