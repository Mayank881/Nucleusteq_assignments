from datetime import datetime

from bson import ObjectId
from bson.errors import InvalidId
from fastapi import HTTPException, status


from app.database import issues_collection
from app.models.issue import Issue
from app.schemas.issue import (
    IssueCreate,
    IssueResponse,
    IssueStatus,
    IssueStatusUpdate,
)
from app.constants.app_constants import (
    ISSUE_NOT_FOUND,
    INVALID_ISSUE_ID,
    INVALID_STATUS_TRANSITION,
    ISSUE_NOT_ASSIGNEE,
)


ALLOWED_TRANSITIONS = {
    IssueStatus.BACKLOG: [IssueStatus.TODO],
    IssueStatus.TODO: [IssueStatus.IN_PROGRESS],
    IssueStatus.IN_PROGRESS: [IssueStatus.DONE],
    IssueStatus.DONE: [],
}
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

def update_issue_status(
    issue_id: str,
    status_update: IssueStatusUpdate,
    current_user: dict,
) -> IssueResponse:
    """
    Update the workflow status of an issue.
    """

    try:
        issue = issues_collection.find_one(
            {"_id": ObjectId(issue_id)}
        )
    except InvalidId:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=INVALID_ISSUE_ID,
        )

    if not issue:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=ISSUE_NOT_FOUND,
        )

    if issue["assignee_id"] != str(current_user["_id"]):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail=ISSUE_NOT_ASSIGNEE,
        )

    current_status = IssueStatus(issue["status"])
    new_status = status_update.status

    if new_status not in ALLOWED_TRANSITIONS[current_status]:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=INVALID_STATUS_TRANSITION,
        )

    issues_collection.update_one(
        {"_id": ObjectId(issue_id)},
        {
            "$set": {
                "status": new_status.value,
                "updated_at": datetime.utcnow(),
            }
        },
    )

    updated_issue = issues_collection.find_one(
        {"_id": ObjectId(issue_id)}
    )

    return IssueResponse(
        id=str(updated_issue["_id"]),
        title=updated_issue["title"],
        description=updated_issue["description"],
        project_id=updated_issue["project_id"],
        reporter_id=updated_issue["reporter_id"],
        assignee_id=updated_issue.get("assignee_id"),
        type=updated_issue["type"],
        priority=updated_issue["priority"],
        status=updated_issue["status"],
        parent_id=updated_issue.get("parent_id"),
    )