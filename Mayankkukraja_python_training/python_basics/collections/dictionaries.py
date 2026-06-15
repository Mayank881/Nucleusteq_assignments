# Q32, Q33, Q34 - Dictionaries

STUDENT_NAME = "Mayank"
STUDENT_ROLL = 121
STUDENT_BRANCH = "CSE"
STUDENT_MARKS = 89.5

TEXT = "python"


def student_dictionary() -> None:
    """Create a student dictionary and access its values."""

    student = {
        "name": STUDENT_NAME,
        "roll_no": STUDENT_ROLL,
        "branch": STUDENT_BRANCH,
        "marks": STUDENT_MARKS
    }

    print(f"Name: {student['name']}")
    print(f"Roll No: {student['roll_no']}")
    print(f"Branch: {student['branch']}")
    print(f"Marks: {student['marks']}")


def character_frequency() -> None:
    """Count frequency of characters in a string."""

    freq = {}

    for char in TEXT:
        freq[char] = freq.get(char, 0) + 1

    print(f"Character Frequency in '{TEXT}':")

    for char, count in freq.items():
        print(f"'{char}': {count}")


def merge_dicts() -> None:
    """Merge two dictionaries."""

    dict_one = {"name": "Mayank", "city": "Bhopal"}
    dict_two = {"course": "Python", "year": 2026}

    merged_dict = {**dict_one, **dict_two}

    print(f"Dictionary 1: {dict_one}")
    print(f"Dictionary 2: {dict_two}")
    print(f"Merged Dictionary: {merged_dict}")


if __name__ == "__main__":
    student_dictionary()
    print()

    character_frequency()
    print()

    merge_dicts()