from fastapi import APIRouter, Depends, status

from app.auth.authorization import RoleChecker
from app.schemas.project import (
    MemberRequest,
    ProjectCreate,
    ProjectResponse,
)
from app.schemas.user import UserRole
from app.services.project_service import (
    add_member,
    create_project,
    remove_member,
)

router = APIRouter(
    prefix="/projects",
    tags=["Projects"],
)


@router.post(
    "",
    response_model=ProjectResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_new_project(
    project: ProjectCreate,
    current_user=Depends(
        RoleChecker([UserRole.ADMIN])
    ),
) -> ProjectResponse:
    """
    Create a new project.
    """
    return create_project(
        project,
        current_user,
    )


@router.post(
    "/{project_id}/members",
    response_model=ProjectResponse,
    status_code=status.HTTP_200_OK,
)
def add_project_member(
    project_id: str,
    member: MemberRequest,
    _=Depends(
        RoleChecker([UserRole.ADMIN])
    ),
) -> ProjectResponse:
    """
    Add a member to a project.
    """
    return add_member(
        project_id,
        member,
    )


@router.delete(
    "/{project_id}/members/{user_id}",
    response_model=ProjectResponse,
    status_code=status.HTTP_200_OK,
)
def remove_project_member(
    project_id: str,
    user_id: str,
    _=Depends(
        RoleChecker([UserRole.ADMIN])
    ),
) -> ProjectResponse:
    """
    Remove a member from a project.
    """
    return remove_member(
        project_id,
        user_id,
    )