from fastapi import APIRouter, Depends, status

from typing import List
from app.auth.authorization import RoleChecker
from app.schemas.project import (
    MemberRequest,
    ProjectCreate,
    ProjectUpdate,
    ProjectResponse,
)
from app.schemas.user import UserRole
from app.services.project_service import (
    add_member,
    create_project,
    remove_member,
    get_all_projects,
    get_project,
    update_project,
    delete_project,
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

@router.get(
    "",
    response_model=List[ProjectResponse],
)
def get_projects(
    current_user=Depends(
        RoleChecker(
            [
                UserRole.ADMIN,
                UserRole.MEMBER,
                UserRole.VIEWER,
            ]
        )
    ),
):
    """
    Retrieve all projects.
    """

    return get_all_projects()

@router.get(
    "/{project_id}",
    response_model=ProjectResponse,
)
def get_single_project(
    project_id: str,
    current_user=Depends(
        RoleChecker(
            [
                UserRole.ADMIN,
                UserRole.MEMBER,
                UserRole.VIEWER,
            ]
        )
    ),
):
    """
    Retrieve a project by its ID.
    """

    return get_project(project_id)

@router.put(
    "/{project_id}",
    response_model=ProjectResponse,
)
def update_existing_project(
    project_id: str,
    project: ProjectUpdate,
    _=Depends(
        RoleChecker([UserRole.ADMIN])
    ),
):
    """
    Update project.
    """

    return update_project(
        project_id,
        project,
    )


@router.delete(
    "/{project_id}",
    status_code=status.HTTP_200_OK,
)
def delete_existing_project(
    project_id: str,
    _=Depends(
        RoleChecker([UserRole.ADMIN])
    ),
):
    """
    Delete project.
    """

    return delete_project(project_id)    