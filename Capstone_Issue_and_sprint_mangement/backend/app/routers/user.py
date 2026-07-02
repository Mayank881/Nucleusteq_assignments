from fastapi import APIRouter, Depends, status

from app.auth.authentication import get_current_user

from app.schemas.user import (
    Token,
    UserCreate,
    UserLogin,
    UserResponse,
)
from app.services.auth_service import login_user
from app.services.user_service import register_user

router = APIRouter(
    prefix="/users",
    tags=["Users"],
)


@router.post(
    "/register",
    response_model=UserResponse,
    status_code=status.HTTP_201_CREATED,
)
def register(user: UserCreate) -> UserResponse:
    """
    Register a new user.
    """
    return register_user(user)


@router.post(
    "/login",
    response_model=Token,
    status_code=status.HTTP_200_OK,
)
def login(login_data: UserLogin) -> Token:
    """
    Authenticate a user and return a JWT access token.
    """
    return login_user(login_data)

@router.get("/me")
def get_profile(
    current_user=Depends(get_current_user),
):
    """
    Return the currently authenticated user.
    """
    return {
        "id": str(current_user["_id"]),
        "name": current_user["name"],
        "email": current_user["email"],
        "role": current_user["role"],
    }