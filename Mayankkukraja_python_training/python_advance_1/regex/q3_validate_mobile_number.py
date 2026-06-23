# Q3 - Write a regular expression to validate a 10-digit mobile number.

import re

# Constants
VALID_MOBILE_NUMBER = "98765432101"
INVALID_MOBILE_NUMBER = "98765"


def validate_mobile_number(
        mobile_number: str
) -> bool:
    """Validate a 10-digit mobile number."""

    mobile_pattern = r"^\d{10}$"

    is_valid = bool(
        re.match(
            mobile_pattern,
            mobile_number
        )
    )

    print(
        f"Mobile Number: '{mobile_number}' "
        f"-> Valid: {is_valid}"
    )

    return is_valid


if __name__ == "__main__":
    validate_mobile_number(
        VALID_MOBILE_NUMBER
    )

    validate_mobile_number(
        INVALID_MOBILE_NUMBER
    )