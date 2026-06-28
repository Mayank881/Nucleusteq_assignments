from dataclasses import dataclass
from datetime import datetime


@dataclass
class User:
    """
    Represents a user document stored in MongoDB.
    """

    name: str
    email: str
    hashed_password: str
    role: str
    created_at: datetime
    updated_at: datetime