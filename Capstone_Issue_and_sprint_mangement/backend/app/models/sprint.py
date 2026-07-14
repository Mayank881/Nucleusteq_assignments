from dataclasses import dataclass, field
from datetime import datetime
from typing import List


@dataclass
class Sprint:
    """
    Represents a sprint document stored in MongoDB.
    """

    name: str
    project_id: str
    start_date: datetime
    end_date: datetime
    created_by: str

    status: str = "PLANNED"
    issue_ids: List[str] = field(default_factory=list)

    created_at: datetime = field(default_factory=datetime.utcnow)
    updated_at: datetime = field(default_factory=datetime.utcnow)