from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class Comment:
    """
    Represents a comment document stored in MongoDB.
    """

    issue_id: str
    user_id: str
    content: str
    created_at: datetime = field(default_factory=datetime.utcnow)
    updated_at: datetime = field(default_factory=datetime.utcnow)