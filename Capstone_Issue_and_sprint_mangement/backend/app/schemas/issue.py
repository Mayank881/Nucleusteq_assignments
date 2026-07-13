from enum import Enum
from typing import Optional

from pydantic import BaseModel, ConfigDict, Field


class IssueStatus(str, Enum):
    """
    Allowed workflow statuses for an issue.
    """

    BACKLOG = "BACKLOG"
    TODO = "TODO"
    IN_PROGRESS = "IN_PROGRESS"
    DONE = "DONE"


class IssueCreate(BaseModel):
    """
    Schema for creating a new issue.
    """

    title: str = Field(..., min_length=3, max_length=100)
    description: str = Field(..., min_length=5)
    type: str
    priority: str
    assignee_id: Optional[str] = None
    parent_id: Optional[str] = None


class IssueResponse(BaseModel):
    id: str
    title: str
    description: str
    project_id: str
    reporter_id: str
    assignee_id: str | None = None
    type: str
    priority: str
    status: str
    parent_id: str | None = None

    model_config = ConfigDict(from_attributes=True)


class IssueStatusUpdate(BaseModel):
    """
    Schema for updating only the issue status.
    """

    status: IssueStatus