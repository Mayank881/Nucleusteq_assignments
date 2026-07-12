from fastapi import APIRouter, Depends, status
from fastapi.security import OAuth2PasswordRequestForm 

from app.auth.authentication import get_current_user

from app.schemas.user import (
    Token,
    UserCreate,
    UserLogin,
)

from app.services.auth_service import login_user
from app.services.user_service import register_user

from app.schemas.api_response import ApiResponse
from app.utils.api_response import success_response

router = APIRouter(
    prefix="/users",
    tags=["Users"],
)


@router.post(
    "/register",
    response_model=ApiResponse,
    status_code=status.HTTP_201_CREATED,
)
def register(user: UserCreate):
    created_user = register_user(user)

    return success_response(
        message="User registered successfully",
        data=created_user,
    )


@router.post(
    "/login",
    response_model=Token,
    status_code=status.HTTP_200_OK,
)
def login(login_data: OAuth2PasswordRequestForm = Depends()) -> Token:
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