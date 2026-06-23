# Q7 - Convert a simple loop-based program into a functional style
# using map() or filter().

# Constants
NUMBER_LIST = [2, 4, 6, 8, 10]


def loop_based_approach(
        numbers: list[int]
) -> list[int]:
    """Double numbers greater than 5 using a loop."""

    doubled_numbers = []

    for current_number in numbers:
        if current_number > 5:
            doubled_numbers.append(
                current_number * 2
            )

    return doubled_numbers


def functional_approach(
        numbers: list[int]
) -> list[int]:
    """Double numbers greater than 5 using filter() and map()."""

    return list(
        map(
            lambda current_number:
            current_number * 2,
            filter(
                lambda current_number:
                current_number > 5,
                numbers
            )
        )
    )


def compare_approaches(
        numbers: list[int]
) -> None:
    """Compare loop-based and functional approaches."""

    loop_result = loop_based_approach(
        numbers
    )

    functional_result = functional_approach(
        numbers
    )

    print(f"Original Numbers: {numbers}")
    print(f"Loop Result: {loop_result}")
    print(f"Functional Result: {functional_result}")


if __name__ == "__main__":
    compare_approaches(
        NUMBER_LIST
    )