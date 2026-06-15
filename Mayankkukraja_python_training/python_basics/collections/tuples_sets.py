# Q28, Q29, Q30, Q31 - Tuples and Sets


def tuple_demo() -> None:
    """Create a tuple and access its elements."""

    student = ("Mayank", 21, "CSE", 8.5)

    print(f"Full Tuple: {student}")
    print(f"First Element: {student[0]}")
    print(f"Last Element: {student[-1]}")
    print(f"Slice [1:3]: {student[1:3]}")


def tuple_to_list() -> None:
    """Convert tuple to list and modify it."""

    values = (10, 20, 30)

    print(f"Original Tuple: {values}")

    value_list = list(values)
    value_list[1] = 50

    print(f"Modified List: {value_list}")


def set_operations() -> None:
    """Perform union, intersection and difference."""

    set_a = {1, 2, 3, 4, 5}
    set_b = {4, 5, 6, 7, 8}

    print(f"Set A: {set_a}")
    print(f"Set B: {set_b}")
    print(f"Union: {set_a | set_b}")
    print(f"Intersection: {set_a & set_b}")
    print(f"Difference: {set_a - set_b}")


def remove_duplicates() -> None:
    """Remove duplicate values using set."""

    num_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]

    unique_list = sorted(set(num_list))

    print(f"With Duplicates: {num_list}")
    print(f"Without Duplicates: {unique_list}")


if __name__ == "__main__":
    tuple_demo()
    print()

    tuple_to_list()
    print()

    set_operations()
    print()

    remove_duplicates()