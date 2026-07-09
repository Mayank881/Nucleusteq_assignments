
from fastapi import APIRouter, Depends, status
from typing import Optional, List

from app.auth.authorization import RoleChecker
from app.schemas.issue import (
    IssueCreate,
    IssueResponse,
    IssueStatusUpdate,
)
from app.schemas.user import UserRole
from app.services.issue_service import (
    create_issue,
    get_issue_by_id,
    update_issue_status,
    search_issues,
    get_all_issues,
)
from app.auth.authentication import get_current_user

router = APIRouter(
    prefix="/issues",
    tags=["Issues"],
)



@router.post(
    "/project/{project_id}",
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
    "/{project_id}/{issue_id}/status",
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

@router.get(
    "/search",
    response_model=list[IssueResponse],
)
def search_issue(
    title: Optional[str] = None,
    description: Optional[str] = None,
    status: Optional[str] = None,
    project_id: Optional[str] = None,
    assignee_id: Optional[str] = None,
    current_user=Depends(get_current_user),
):
    """
    Search and filter issues.
    """

    return search_issues(
        title,
        description,
        status,
        project_id,
        assignee_id,
    )

@router.get(
    "",
    response_model=List[IssueResponse],
)
def get_issues(
    current_user=Depends(get_current_user),
):
    """
    Retrieve all issues.
    """

    return get_all_issues()

@router.get(
    "{issue_id}",
    response_model=IssueResponse,
)
def get_issue(
    issue_id: str,
    current_user=Depends(get_current_user),
):
    """
    Retrieve an issue by its ID.
    """

    return get_issue_by_id(issue_id)