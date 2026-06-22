# Q5 - Catch all exceptions and print the error message.

# Constants
RISKY_VALUE: str = "config.txt"


def catch_all_exceptions(risky_value: str) -> None:
    """Catch all exceptions and print the error message."""

    try:
        with open(risky_value, "r") as file:
            content = file.read()
            print(f"File content successfully loaded:\n{content}")

    except Exception as error:
        print(f"An error occurred: {error}")


if __name__ == "__main__":
    catch_all_exceptions(RISKY_VALUE)