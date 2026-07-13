from fastapi import APIRouter, Depends, status

from app.auth.authorization import RoleChecker
from app.schemas.issue import (
    IssueCreate,
    IssueResponse,
)
from app.schemas.user import UserRole
from app.services.issue_service import create_issue

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