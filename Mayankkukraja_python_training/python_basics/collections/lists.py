# Q25, Q26, Q27 - Lists

NUM_LIST = [4, 7, 2, 9, 1, 5, 3, 8, 6, 2]
COUNT_LIST = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
REVERSE_LIST = [10, 20, 30, 40, 50]


def analyse_list() -> None:
    """Find sum, max, sorted order and unique values from a list."""

    num_list = NUM_LIST

    print(f"Original List: {num_list}")
    print(f"Sum: {sum(num_list)}")
    print(f"Max: {max(num_list)}")
    print(f"Sorted: {sorted(num_list)}")
    print(f"Without Duplicates: {sorted(set(num_list))}")


def count_even_odd() -> None:
    """Count even and odd numbers in a list."""

    num_list = COUNT_LIST
    even_count = 0
    odd_count = 0

    for num in num_list:
        if num % 2 == 0:
            even_count += 1
        else:
            odd_count += 1

    print(f"Even Count: {even_count}")
    print(f"Odd Count: {odd_count}")


def reverse_list() -> None:
    """Reverse a list without using reverse()."""

    num_list = REVERSE_LIST
    reversed_list = []

    for i in range(len(num_list) - 1, -1, -1):
        reversed_list.append(num_list[i])

    print(f"Original List: {num_list}")
    print(f"Reversed List: {reversed_list}")


if __name__ == "__main__":
    analyse_list()
    print()

    count_even_odd()
    print()

    reverse_list()