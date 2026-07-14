from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel, Field


class CreateSprintRequest(BaseModel):
    """
    Schema for creating a new sprint.
    """

    name: str = Field(
        ...,
        min_length=3,
        max_length=100,
        description="Sprint name"
    )

    project_id: str = Field(
        ...,
        min_length=1,
        description="Project ID"
    )

    start_date: datetime
    end_date: datetime


class UpdateSprintRequest(BaseModel):
    """
    Schema for updating sprint details.
    """

    name: Optional[str] = Field(
        default=None,
        min_length=3,
        max_length=100
    )

    start_date: Optional[datetime] = None
    end_date: Optional[datetime] = None


class AddIssueRequest(BaseModel):
    """
    Schema for adding an issue to a sprint.
    """

    issue_id: str = Field(
        ...,
        min_length=1,
        description="Issue ID"
    )


class SprintResponse(BaseModel):
    """
    Sprint response returned to the client.
    """

    id: str

    name: str

    project_id: str

    status: str

    issue_ids: List[str]

    start_date: datetime

    end_date: datetime

    created_by: str

    created_at: datetime

    updated_at: datetime