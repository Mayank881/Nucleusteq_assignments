from datetime import datetime

from bson import ObjectId
from bson.errors import InvalidId
from fastapi import HTTPException, status

from app.database import projects_collection, users_collection
from app.schemas.project import (
    MemberRequest,
    ProjectCreate,
    ProjectUpdate,
    ProjectResponse,
)

from app.constants.app_constants import (
    PROJECT_NOT_FOUND,
    PROJECT_NAME_EXISTS,    
    USER_NOT_FOUND,
    MEMBER_ALREADY_EXISTS,
    MEMBER_NOT_FOUND,
    INVALID_PROJECT_ID,
    INVALID_USER_ID,
    PROJECT_OWNER_CANNOT_BE_REMOVED,
)



def create_project(
    project: ProjectCreate,
    current_user: dict,
) -> ProjectResponse:
    """
    Create a new project.
    """

    existing_project = projects_collection.find_one(
        {"name": project.name}
    )

    if existing_project:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=PROJECT_NAME_EXISTS,
        )

    owner_id = str(current_user["_id"])

    project_document = {
        "name": project.name,
        "description": project.description,
        "owner_id": owner_id,
        "members": [owner_id],
        "created_at": datetime.utcnow(),
        "updated_at": datetime.utcnow(),
    }

    result = projects_collection.insert_one(
        project_document
    )

    return ProjectResponse(
        id=str(result.inserted_id),
        name=project.name,
        description=project.description,
        owner_id=owner_id,
        members=[owner_id],
    )

def get_all_projects() -> list[ProjectResponse]:
    """
    Retrieve all projects.
    """

    projects = projects_collection.find()

    response = []

    for project in projects:
        response.append(
            ProjectResponse(
                id=str(project["_id"]),
                name=project["name"],
                description=project["description"],
                owner_id=project["owner_id"],
                members=project["members"],
            )
        )

    return response

def get_project(
    project_id: str,
) -> ProjectResponse:
    """
    Retrieve a project by its ID.
    """

    project = get_project_by_id(project_id)

    return ProjectResponse(
        id=str(project["_id"]),
        name=project["name"],
        description=project["description"],
        owner_id=project["owner_id"],
        members=project["members"],
    )


def get_project_by_id(
    project_id: str,
) -> dict:
    """
    Retrieve a project by its ID.
    """

    try:
        project = projects_collection.find_one(
            {"_id": ObjectId(project_id)}
        )
    except InvalidId:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=INVALID_PROJECT_ID,
        )

    if not project:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=PROJECT_NOT_FOUND,
        )

    return project

def add_member(
    project_id: str,
    member: MemberRequest,
) -> ProjectResponse:
    """
    Add a member to a project.
    """

    project = get_project_by_id(project_id)

    try:
        user = users_collection.find_one(
            {"_id": ObjectId(member.user_id)}
        )
    except InvalidId:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=INVALID_USER_ID,
        )

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=USER_NOT_FOUND,
        )

    member_id = str(user["_id"])

    if member_id in project["members"]:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=MEMBER_ALREADY_EXISTS,
        )

    updated_members = project["members"].copy()
    updated_members.append(member_id)

    projects_collection.update_one(
        {"_id": project["_id"]},
        {
            "$set": {
                "members": updated_members,
                "updated_at": datetime.utcnow(),
            }
        },
    )

    project["members"] = updated_members

    return ProjectResponse(
        id=str(project["_id"]),
        name=project["name"],
        description=project["description"],
        owner_id=project["owner_id"],
        members=project["members"],
    )

def remove_member(
    project_id: str,
    user_id: str,
) -> ProjectResponse:
    """
    Remove a member from a project.
    """

    project = get_project_by_id(project_id)

    try:
        user = users_collection.find_one(
            {"_id": ObjectId(user_id)}
        )
    except InvalidId:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=INVALID_USER_ID,
        )

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=USER_NOT_FOUND,
        )

    member_id = str(user["_id"])

    if member_id == project["owner_id"]:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=PROJECT_OWNER_CANNOT_BE_REMOVED,
        )

    if member_id not in project["members"]:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=MEMBER_NOT_FOUND,
        )

    updated_members = project["members"].copy()
    updated_members.remove(member_id)

    projects_collection.update_one(
        {"_id": project["_id"]},
        {
            "$set": {
                "members": updated_members,
                "updated_at": datetime.utcnow(),
            }
        },
    )

    return ProjectResponse(
        id=str(project["_id"]),
        name=project["name"],
        description=project["description"],
        owner_id=project["owner_id"],
        members=updated_members,
    )


def update_project(
    project_id: str,
    project_data: ProjectUpdate,
) -> ProjectResponse:
    """
    Update an existing project.
    """

    project = get_project_by_id(project_id)

    existing_project = projects_collection.find_one(
        {
            "name": project_data.name,
            "_id": {"$ne": project["_id"]},
        }
    )

    if existing_project:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=PROJECT_NAME_EXISTS,
        )

    projects_collection.update_one(
        {"_id": project["_id"]},
        {
            "$set": {
                "name": project_data.name,
                "description": project_data.description,
                "updated_at": datetime.utcnow(),
            }
        },
    )

    updated_project = get_project_by_id(project_id)

    return ProjectResponse(
        id=str(updated_project["_id"]),
        name=updated_project["name"],
        description=updated_project["description"],
        owner_id=updated_project["owner_id"],
        members=updated_project["members"],
    )


def delete_project(
    project_id: str,
) -> dict:
    """
    Delete a project.
    """

    project = get_project_by_id(project_id)

    projects_collection.delete_one(
        {"_id": project["_id"]}
    )

    return {
        "message": "Project deleted successfully"
    }