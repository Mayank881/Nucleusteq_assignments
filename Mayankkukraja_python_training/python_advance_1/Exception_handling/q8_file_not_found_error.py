# Q8 - Handle FileNotFoundError when trying to open a file.

# Constants
FILE_NAME = "student_data.txt"


def read_file_content(file_name: str) -> None:
    """Read and display the contents of a file."""

    try:
        with open(file_name, "r") as file:
            content = file.read()

        print("File content loaded successfully:")
        print(content)

    except FileNotFoundError:
        print(f"Error: File '{file_name}' was not found.")


if __name__ == "__main__":
    read_file_content(FILE_NAME)