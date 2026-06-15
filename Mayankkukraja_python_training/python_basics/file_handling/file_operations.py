# Q35, Q36, Q37, Q38, Q39 - File Handling

import os

FILE_NAME = "mayank.txt"
COPY_FILE_NAME = "mayank_copy.txt"

OWNER_NAME = "Mayank"

APPEND_LINE_1 = "Python Training 2026\n"
APPEND_LINE_2 = "NucleusTeq Assignment\n"

SEARCH_WORD_1 = "Mayank"
SEARCH_WORD_2 = "Python"

OUTPUT_DIR = "file_outputs"

os.makedirs(OUTPUT_DIR, exist_ok=True)


def write_name() -> None:
    """Create a file and write a name into it."""

    file_path = os.path.join(OUTPUT_DIR, FILE_NAME)

    with open(file_path, "w") as file:
        file.write(OWNER_NAME + "\n")

    print(f"File created: {file_path}")


def analyse_file() -> None:
    """Read a file and count words, lines and characters."""

    file_path = os.path.join(OUTPUT_DIR, FILE_NAME)

    with open(file_path, "r") as file:
        content = file.read()

    print(f"Lines: {len(content.splitlines())}")
    print(f"Words: {len(content.split())}")
    print(f"Characters: {len(content)}")


def append_to_file() -> None:
    """Append data to an existing file."""

    file_path = os.path.join(OUTPUT_DIR, FILE_NAME)

    with open(file_path, "a") as file:
        file.write(APPEND_LINE_1)
        file.write(APPEND_LINE_2)

    print("Data appended successfully")


def copy_file() -> None:
    """Copy content from one file to another."""

    source_file = os.path.join(OUTPUT_DIR, FILE_NAME)
    destination_file = os.path.join(OUTPUT_DIR, COPY_FILE_NAME)

    with open(source_file, "r") as source:
        content = source.read()

    with open(destination_file, "w") as destination:
        destination.write(content)

    print(f"Copied '{source_file}' to '{destination_file}'")


def search_word(word: str) -> None:
    """Search a word in a file."""

    file_path = os.path.join(OUTPUT_DIR, FILE_NAME)
    found = False

    with open(file_path, "r") as file:
        for line_num, line in enumerate(file, start=1):
            if word in line:
                print(f"Found '{word}' on line {line_num}: {line.strip()}")
                found = True

    if not found:
        print(f"'{word}' not found in file")


if __name__ == "__main__":
    write_name()
    append_to_file()

    print()
    analyse_file()

    print()
    copy_file()

    print()
    search_word(SEARCH_WORD_1)
    search_word(SEARCH_WORD_2)