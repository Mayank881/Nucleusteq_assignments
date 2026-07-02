
from passlib.context import CryptContext

# Configure bcrypt as the password hashing algorithm
password_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto",
)


def hash_password(password: str) -> str:
    """
    Convert a plain-text password into a secure hashed password.
    """
    return password_context.hash(password)


def verify_password(
    plain_password: str,
    hashed_password: str,
) -> bool:
    """
    Verify whether the entered password matches the stored hashed password.
    """
    return password_context.verify(
        plain_password,
        hashed_password,
    )