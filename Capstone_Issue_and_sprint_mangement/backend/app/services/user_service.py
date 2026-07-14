from datetime import datetime

from fastapi import HTTPException, status

from app.database import users_collection
from app.schemas.user import UserCreate, UserResponse, UserRole
from app.auth.password import hash_password
from app.constants import app_constants

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
            detail=app_constants.USER_ALREADY_EXISTS,
        )

    user_document = {
        "name": user.name,
        "email": user.email,
        "hashed_password": hash_password(user.password),
        "role": UserRole.VIEWER.value,
        "created_at": datetime.utcnow(),
        "updated_at": datetime.utcnow(),
    }

    result = users_collection.insert_one(user_document)

    return UserResponse(
        id=str(result.inserted_id),
        name=user.name,
        email=user.email,
        role=UserRole.VIEWER,  # Default role for new users
    )