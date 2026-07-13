from datetime import datetime

from app.database import issues_collection
from app.models.issue import Issue
from app.schemas.issue import (
    IssueCreate,
    IssueResponse,
)
from app.services.project_service import get_project_by_id


def create_issue(
    project_id: str,
    issue: IssueCreate,
    current_user: dict,
) -> IssueResponse:
    """
    Create a new issue in a project.
    """

    # Validate project exists
    project = get_project_by_id(project_id)

    reporter_id = str(current_user["_id"])

    issue_data = Issue(
        title=issue.title,
        description=issue.description,
        project_id=str(project["_id"]),
        reporter_id=reporter_id,
        assignee_id=issue.assignee_id,
        type=issue.type,
        priority=issue.priority,
        status="BACKLOG",
        parent_id=issue.parent_id,
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow(),
    )

    issue_document = {
        "title": issue_data.title,
        "description": issue_data.description,
        "project_id": issue_data.project_id,
        "reporter_id": issue_data.reporter_id,
        "assignee_id": issue_data.assignee_id,
        "type": issue_data.type,
        "priority": issue_data.priority,
        "status": issue_data.status,
        "parent_id": issue_data.parent_id,
        "created_at": issue_data.created_at,
        "updated_at": issue_data.updated_at,
    }

    result = issues_collection.insert_one(
        issue_document
    )

    return IssueResponse(
        id=str(result.inserted_id),
        title=issue_data.title,
        description=issue_data.description,
        project_id=issue_data.project_id,
        reporter_id=issue_data.reporter_id,
        assignee_id=issue_data.assignee_id,
        type=issue_data.type,
        priority=issue_data.priority,
        status=issue_data.status,
        parent_id=issue_data.parent_id,
    )