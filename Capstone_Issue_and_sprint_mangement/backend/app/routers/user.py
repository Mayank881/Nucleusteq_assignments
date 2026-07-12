from fastapi import APIRouter, status

from app.schemas.user import UserCreate, UserResponse
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