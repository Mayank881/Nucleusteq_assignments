from datetime import datetime

from bson import ObjectId
from bson .errors import InvalidId
from fastapi import HTTPException, status

from app.database import (
    projects_collection,
    issues_collection,
    sprints_collection,
)
from app.models.sprint import Sprint
from app.schemas.issue import IssueStatus
from app.schemas.sprint import (
    CreateSprintRequest,
    UpdateSprintRequest,
    SprintResponse,
    AddIssueRequest,
    SprintStatus,
)
from app.constants.app_constants import (
    DONE_ISSUE_NOT_ALLOWED,
    INVALID_SPRINT_DATES,
    ISSUE_ALREADY_IN_SPRINT,
    ISSUE_NOT_FOUND,
    ISSUE_NOT_IN_SPRINT,
    ISSUE_PROJECT_MISMATCH,
    INVALID_SPRINT_ID,
    SPRINT_ALREADY_ACTIVE,
    SPRINT_ALREADY_COMPLETED,
    SPRINT_NOT_ACTIVE,
    SPRINT_NOT_FOUND,
    SPRINT_STATUS_PLANNED,
    SPRINT_STATUS_ACTIVE,
    SPRINT_STATUS_COMPLETED,
)
from app.services.project_service import get_project_by_id


def create_sprint(
    sprint: CreateSprintRequest,
    current_user: dict,
) -> SprintResponse:
    """
    Create a new sprint.
    """

    # Validate project exists
    project = get_project_by_id(
        sprint.project_id
    )

    # Validate sprint dates
    if sprint.start_date >= sprint.end_date:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=INVALID_SPRINT_DATES,
        )

    created_by = str(current_user["_id"])

    sprint_data = Sprint(
        name=sprint.name,
        project_id=str(project["_id"]),
        start_date=sprint.start_date,
        end_date=sprint.end_date,
        created_by=created_by,
        status=SPRINT_STATUS_PLANNED,
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow(),
    )
    sprint_document = {
        "name": sprint_data.name,
        "project_id": sprint_data.project_id,
        "start_date": sprint_data.start_date,
        "end_date": sprint_data.end_date,
        "created_by": sprint_data.created_by,
        "status": sprint_data.status,
        "issue_ids": sprint_data.issue_ids,
        "created_at": sprint_data.created_at,
        "updated_at": sprint_data.updated_at,
    }
    result = sprints_collection.insert_one(
        sprint_document
    )
    return SprintResponse(
        id=str(result.inserted_id),
        name=sprint_data.name,
        project_id=sprint_data.project_id,
        status=sprint_data.status,
        issue_ids=sprint_data.issue_ids,
        start_date=sprint_data.start_date,
        end_date=sprint_data.end_date,
        created_by=sprint_data.created_by,
        created_at=sprint_data.created_at,
        updated_at=sprint_data.updated_at,
    )

def get_all_sprints() -> list[SprintResponse]:
    """
    Get all sprints.
    """

    sprints = sprints_collection.find()

    sprint_list = []

    for sprint in sprints:
        sprint_list.append(
            SprintResponse(
                id=str(sprint["_id"]),
                name=sprint["name"],
                project_id=sprint["project_id"],
                status=sprint["status"],
                issue_ids=sprint.get("issue_ids", []),
                start_date=sprint["start_date"],
                end_date=sprint["end_date"],
                created_by=sprint["created_by"],
                created_at=sprint["created_at"],
                updated_at=sprint["updated_at"],
            )
        )

    return sprint_list

def get_sprint_by_id(
    sprint_id: str,
) -> SprintResponse:
    """
    Get sprint by ID.
    """

    try:
        sprint = sprints_collection.find_one(
            {
                "_id": ObjectId(sprint_id)
            }
        )

    except InvalidId:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=INVALID_SPRINT_ID,
        )

    if not sprint:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=SPRINT_NOT_FOUND,
        )

    return SprintResponse(
        id=str(sprint["_id"]),
        name=sprint["name"],
        project_id=sprint["project_id"],
        status=sprint["status"],
        issue_ids=sprint.get("issue_ids", []),
        start_date=sprint["start_date"],
        end_date=sprint["end_date"],
        created_by=sprint["created_by"],
        created_at=sprint["created_at"],
        updated_at=sprint["updated_at"],
    )

def update_sprint(
    sprint_id: str,
    sprint: UpdateSprintRequest,
) -> SprintResponse:
    """
    Update sprint details.
    """

    try:
        sprint_object_id = ObjectId(sprint_id)

    except InvalidId:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=INVALID_SPRINT_ID,
        )

    existing_sprint = sprints_collection.find_one(
        {
            "_id": sprint_object_id
        }
    )

    if not existing_sprint:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=SPRINT_NOT_FOUND,
        )

    start_date = sprint.start_date or existing_sprint["start_date"]
    end_date = sprint.end_date or existing_sprint["end_date"]

    if start_date >= end_date:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=INVALID_SPRINT_DATES,
        )

    update_data = {}

    if sprint.name is not None:
        update_data["name"] = sprint.name

    if sprint.start_date is not None:
        update_data["start_date"] = sprint.start_date

    if sprint.end_date is not None:
        update_data["end_date"] = sprint.end_date

    update_data["updated_at"] = datetime.utcnow()

    sprints_collection.update_one(
        {
            "_id": sprint_object_id
        },
        {
            "$set": update_data
        }
    )

    updated_sprint = sprints_collection.find_one(
        {
            "_id": sprint_object_id
        }
    )

    return SprintResponse(
        id=str(updated_sprint["_id"]),
        name=updated_sprint["name"],
        project_id=updated_sprint["project_id"],
        status=updated_sprint["status"],
        issue_ids=updated_sprint.get("issue_ids", []),
        start_date=updated_sprint["start_date"],
        end_date=updated_sprint["end_date"],
        created_by=updated_sprint["created_by"],
        created_at=updated_sprint["created_at"],
        updated_at=updated_sprint["updated_at"],
    )

def _change_sprint_status(
    sprint_id: str,
    new_status: str,
) -> SprintResponse:
    """
    Update sprint status.
    """

    try:
        sprint_object_id = ObjectId(sprint_id)

    except InvalidId:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=INVALID_SPRINT_ID,
        )

    existing_sprint = sprints_collection.find_one(
        {
            "_id": sprint_object_id
        }
    )

    if not existing_sprint:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=SPRINT_NOT_FOUND,
        )

    sprints_collection.update_one(
        {
            "_id": sprint_object_id
        },
        {
            "$set": {
                "status": new_status,
                "updated_at": datetime.utcnow(),
            }
        }
    )

    updated_sprint = sprints_collection.find_one(
        {
            "_id": sprint_object_id
        }
    )

    return SprintResponse(
        id=str(updated_sprint["_id"]),
        name=updated_sprint["name"],
        project_id=updated_sprint["project_id"],
        status=updated_sprint["status"],
        issue_ids=updated_sprint.get("issue_ids", []),
        start_date=updated_sprint["start_date"],
        end_date=updated_sprint["end_date"],
        created_by=updated_sprint["created_by"],
        created_at=updated_sprint["created_at"],
        updated_at=updated_sprint["updated_at"],
    )

def start_sprint(
    sprint_id: str,
) -> SprintResponse:
    """
    Start a planned sprint.
    """

    try:
        sprint_object_id = ObjectId(sprint_id)

    except InvalidId:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=INVALID_SPRINT_ID,
        )

    sprint = sprints_collection.find_one(
        {
            "_id": sprint_object_id
        }
    )

    if not sprint:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=SPRINT_NOT_FOUND,
        )

    if sprint["status"] == SprintStatus.ACTIVE.value:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=SPRINT_ALREADY_ACTIVE,
        )

    if sprint["status"] == SprintStatus.COMPLETED.value:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=SPRINT_ALREADY_COMPLETED,
        )

    return _change_sprint_status(
        sprint_id,
        SprintStatus.ACTIVE.value,
    )


def add_issue_to_sprint(
    sprint_id: str,
    request: AddIssueRequest,
) -> SprintResponse:
    """
    Add an issue to a sprint.
    """

    try:
        sprint_object_id = ObjectId(sprint_id)
        issue_object_id = ObjectId(request.issue_id)

    except InvalidId:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=INVALID_SPRINT_ID,
        )

    sprint = sprints_collection.find_one(
        {
            "_id": sprint_object_id
        }
    )

    if not sprint:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=SPRINT_NOT_FOUND,
        )

    issue = issues_collection.find_one(
        {
            "_id": issue_object_id
        }
    )

    if not issue:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=ISSUE_NOT_FOUND,
        )

    if sprint["project_id"] != issue["project_id"]:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=ISSUE_PROJECT_MISMATCH,
        )

    if issue["status"] == IssueStatus.DONE.value:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=DONE_ISSUE_NOT_ALLOWED,
        )

    issue_ids = sprint.get("issue_ids", [])

    if request.issue_id in issue_ids:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=ISSUE_ALREADY_IN_SPRINT,
        )

    issue_ids.append(request.issue_id)

    sprints_collection.update_one(
        {
            "_id": sprint_object_id
        },
        {
            "$set": {
                "issue_ids": issue_ids,
                "updated_at": datetime.utcnow(),
            }
        }
    )

    updated_sprint = sprints_collection.find_one(
        {
            "_id": sprint_object_id
        }
    )

    return SprintResponse(
        id=str(updated_sprint["_id"]),
        name=updated_sprint["name"],
        project_id=updated_sprint["project_id"],
        status=updated_sprint["status"],
        issue_ids=updated_sprint["issue_ids"],
        start_date=updated_sprint["start_date"],
        end_date=updated_sprint["end_date"],
        created_by=updated_sprint["created_by"],
        created_at=updated_sprint["created_at"],
        updated_at=updated_sprint["updated_at"],
    )

def remove_issue_from_sprint(
    sprint_id: str,
    issue_id: str,
) -> SprintResponse:
    """
    Remove an issue from a sprint.
    """

    try:
        sprint_object_id = ObjectId(sprint_id)
        ObjectId(issue_id)

    except InvalidId:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=INVALID_SPRINT_ID,
        )

    sprint = sprints_collection.find_one(
        {
            "_id": sprint_object_id
        }
    )

    if not sprint:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=SPRINT_NOT_FOUND,
        )

    issue_ids = sprint.get(
        "issue_ids",
        [],
    )

    if issue_id not in issue_ids:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=ISSUE_NOT_IN_SPRINT,
        )

    issue_ids.remove(issue_id)

    sprints_collection.update_one(
        {
            "_id": sprint_object_id
        },
        {
            "$set": {
                "issue_ids": issue_ids,
                "updated_at": datetime.utcnow(),
            }
        },
    )

    updated_sprint = sprints_collection.find_one(
        {
            "_id": sprint_object_id
        }
    )

    return SprintResponse(
        id=str(updated_sprint["_id"]),
        name=updated_sprint["name"],
        project_id=updated_sprint["project_id"],
        status=updated_sprint["status"],
        issue_ids=updated_sprint["issue_ids"],
        start_date=updated_sprint["start_date"],
        end_date=updated_sprint["end_date"],
        created_by=updated_sprint["created_by"],
        created_at=updated_sprint["created_at"],
        updated_at=updated_sprint["updated_at"],
    )

def complete_sprint(
    sprint_id: str,
) -> SprintResponse:
    """
    Complete an active sprint.
    """

    try:
        sprint_object_id = ObjectId(sprint_id)

    except InvalidId:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=INVALID_SPRINT_ID,
        )

    sprint = sprints_collection.find_one(
        {
            "_id": sprint_object_id
        }
    )

    if not sprint:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=SPRINT_NOT_FOUND,
        )

    if sprint["status"] == SprintStatus.PLANNED.value:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=SPRINT_NOT_ACTIVE,
        )

    if sprint["status"] == SprintStatus.COMPLETED.value:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=SPRINT_ALREADY_COMPLETED,
        )

    return _change_sprint_status(
        sprint_id,
        SprintStatus.COMPLETED.value,
    )