from datetime import datetime

from fastapi import HTTPException, status

from app.auth.password import hash_password
from app.constants.app_constants import(
    ADMIN_REGISTERED_NOT_ALLOWED,
    USER_ALREADY_EXISTS,
)
from app.database import users_collection
from app.schemas.user import (
    UserCreate,
    UserResponse,
    UserRole,
)


def register_user(user: UserCreate) -> UserResponse:
    """
    Register a new user.
    """

    existing_user = users_collection.find_one(
        {"email": user.email}
    )

    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=USER_ALREADY_EXISTS,
        )

    # Public registration must never create Admin users.
    if user.role == UserRole.ADMIN:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=ADMIN_REGISTERED_NOT_ALLOWED,
        )

    user_document = {
        "name": user.name,
        "email": user.email,
        "hashed_password": hash_password(
            user.password
        ),
        "role": user.role.value,
        "created_at": datetime.utcnow(),
        "updated_at": datetime.utcnow(),
    }

    result = users_collection.insert_one(
        user_document
    )

    return UserResponse(
        id=str(result.inserted_id),
        name=user.name,
        email=user.email,
        role=user.role,
    )