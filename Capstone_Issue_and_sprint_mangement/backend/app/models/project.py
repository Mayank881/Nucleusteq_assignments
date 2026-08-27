from dataclasses import dataclass, field
from datetime import datetime
from typing import List


@dataclass
class Project:
    """
    Represents a project document stored in MongoDB.
    """

    name: str
    description: str
    owner_id: str
    members: List[str] = field(default_factory=list)
    created_at: datetime = field(default_factory=datetime.utcnow)
    updated_at: datetime = field(default_factory=datetime.utcnow)