from fastapi import APIRouter, Depends, status
from typing import List

from app.auth.authorization import RoleChecker
from app.schemas.sprint import (
    CreateSprintRequest,
    SprintResponse,
    UpdateSprintRequest,
    AddIssueRequest,
    
)
from app.schemas.user import UserRole
from app.services.sprint_service import (
    create_sprint,
    get_all_sprints,
    get_sprint_by_id,
    update_sprint,
    add_issue_to_sprint,
    remove_issue_from_sprint,
)

router = APIRouter(
    prefix="/sprints",
    tags=["Sprints"],
)


@router.post(
    "",
    response_model=SprintResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_new_sprint(
    sprint: CreateSprintRequest,
    current_user=Depends(
        RoleChecker(
            [
                UserRole.ADMIN,
                UserRole.MEMBER,
            ]
        )
    ),
) -> SprintResponse:
    """
    Create a new sprint.
    """
    return create_sprint(
        sprint,
        current_user,
    )

@router.get(
    "",
    response_model=List[SprintResponse],
    status_code=status.HTTP_200_OK,
)
def get_sprints(
    current_user=Depends(
        RoleChecker(
            [
                UserRole.ADMIN,
                UserRole.MEMBER,
                UserRole.VIEWER
            ]
        )
    ),
) -> List[SprintResponse]:
    """
    Get all sprints.
    """

    return get_all_sprints()

@router.get(
    "/{sprint_id}",
    response_model=SprintResponse,
    status_code=status.HTTP_200_OK,
)
def get_sprint(
    sprint_id: str,
    current_user=Depends(
        RoleChecker(
            [
                UserRole.ADMIN,
                UserRole.MEMBER,
                UserRole.VIEWER
            ]
        )
    ),
) -> SprintResponse:
    """
    Get sprint by ID.
    """

    return get_sprint_by_id(
        sprint_id
    )

@router.put(
    "/{sprint_id}",
    response_model=SprintResponse,
    status_code=status.HTTP_200_OK,
)
def update_existing_sprint(
    sprint_id: str,
    sprint: UpdateSprintRequest,
    current_user=Depends(
        RoleChecker(
            [
                UserRole.ADMIN,
                UserRole.MEMBER,
            ]
        )
    ),
) -> SprintResponse:
    """
    Update sprint details.
    """

    return update_sprint(
        sprint_id,
        sprint,
    )

@router.post(
    "/{sprint_id}/issues",
    response_model=SprintResponse,
    status_code=status.HTTP_200_OK,
)
def add_issue(
    sprint_id: str,
    request: AddIssueRequest,
    current_user=Depends(
        RoleChecker(
            [
                UserRole.ADMIN,
                UserRole.MEMBER,
            ]
        )
    ),
) -> SprintResponse:

    return add_issue_to_sprint(
        sprint_id,
        request,
    )

@router.delete(
    "/{sprint_id}/issues/{issue_id}",
    response_model=SprintResponse,
    status_code=status.HTTP_200_OK,
)
def remove_issue(
    sprint_id: str,
    issue_id: str,
    current_user=Depends(
        RoleChecker(
            [
                UserRole.ADMIN,
                UserRole.MEMBER,
            ]
        )
    ),
) -> SprintResponse:
    """
    Remove an issue from a sprint.
    """

    return remove_issue_from_sprint(
        sprint_id,
        issue_id,
    )