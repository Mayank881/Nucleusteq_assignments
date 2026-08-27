from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional


@dataclass
class Issue:
    """
    Represents an issue document stored in MongoDB.
    """

    title: str
    description: str
    project_id: str
    reporter_id: str
    type: str
    priority: str
    assignee_id: Optional[str] = None
    status: str = "BACKLOG"
    parent_id: Optional[str] = None
    created_at: datetime = field(default_factory=datetime.utcnow)
    updated_at: datetime = field(default_factory=datetime.utcnow)