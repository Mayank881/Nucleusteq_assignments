# Q8 - Create a password validation program using regex
# (minimum length, one digit, one special character).

import re

# Constants
STRONG_PASSWORD = "Pass@123"
WEAK_PASSWORD = "password"
MIN_PASSWORD_LENGTH = 8


def validate_password(password: str) -> bool:
    """Validate a password using regular expressions."""

    has_min_length = (
        len(password) >= MIN_PASSWORD_LENGTH
    )

    has_digit = bool(
        re.search(
            r"\d",
            password
        )
    )

    has_special_character = bool(
        re.search(
            r"[!@#$%^&*(),.?\":{}|<>]",
            password
        )
    )

    is_valid = (
        has_min_length
        and has_digit
        and has_special_character
    )

    print(f"Password: '{password}'")
    print(
        f"Minimum Length "
        f"({MIN_PASSWORD_LENGTH}+): "
        f"{has_min_length}"
    )
    print(f"Contains Digit: {has_digit}")
    print(
        f"Contains Special Character: "
        f"{has_special_character}"
    )
    print(f"Valid Password: {is_valid}")

    return is_valid


if __name__ == "__main__":
    validate_password(
        STRONG_PASSWORD
    )

    print()

    validate_password(
        WEAK_PASSWORD
    )