
from fastapi import APIRouter, Depends, status

from app.auth.authorization import RoleChecker
from app.schemas.issue import (
    IssueCreate,
    IssueResponse,
    IssueStatusUpdate,
)
from app.schemas.user import UserRole
from app.services.issue_service import (
    create_issue,
    update_issue_status,
)

router = APIRouter(
    prefix="/projects",
    tags=["Issues"],
)


@router.post(
    "/{project_id}/issues",
    response_model=IssueResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_new_issue(
    project_id: str,
    issue: IssueCreate,
    current_user=Depends(
        RoleChecker(
            [
                UserRole.ADMIN,
                UserRole.MEMBER,
            ]
        )
    ),
) -> IssueResponse:
    """
    Create a new issue inside a project.
    """
    return create_issue(
        project_id,
        issue,
        current_user,
    ) 


@router.patch(
    "/{project_id}/issues/{issue_id}/status",
    response_model=IssueResponse,
)
def update_issue_workflow(
    project_id: str,
    issue_id: str,
    status_update: IssueStatusUpdate,
    current_user=Depends(
        RoleChecker(
            [
                UserRole.ADMIN,
                UserRole.MEMBER,
            ]
        )
    ),
) -> IssueResponse:
    """
    Update the workflow status of an issue.
    """

    return update_issue_status(
        issue_id,
        status_update,
        current_user,
    )