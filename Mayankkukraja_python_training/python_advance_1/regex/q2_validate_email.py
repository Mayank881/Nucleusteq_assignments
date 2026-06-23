# Q2 - Write a regular expression to validate an email address.

import re

# Constants
VALID_EMAIL = "mayank.kukraja@example.com"
INVALID_EMAIL = "mayank.kukraja@.com"


def validate_email(email_address: str) -> bool:
    """Validate an email address using a regular expression."""

    email_pattern = (
        r"^[a-zA-Z0-9._%+-]+"
        r"@[a-zA-Z0-9.-]+"
        r"\.[a-zA-Z]{2,}$"
    )

    is_valid = bool(
        re.match(
            email_pattern,
            email_address
        )
    )

    print(
        f"Email: '{email_address}' "
        f"-> Valid: {is_valid}"
    )

    return is_valid


if __name__ == "__main__":
    validate_email(VALID_EMAIL)
    validate_email(INVALID_EMAIL)