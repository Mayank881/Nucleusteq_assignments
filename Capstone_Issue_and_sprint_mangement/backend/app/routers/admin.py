from fastapi import APIRouter, Depends

from app.auth.authorization import RoleChecker
from app.schemas.user import UserRole

from app.schemas.api_response import ApiResponse
from app.utils.api_response import success_response

router = APIRouter(
    prefix="/admin",
    tags=["Admin"],
)


@router.get(
    "/dashboard",
    response_model=ApiResponse,
)
def admin_dashboard(
    current_user=Depends(
        RoleChecker([UserRole.ADMIN])
    ),
):
    """
    Admin-only dashboard endpoint.
    """
    return success_response(
        message="Welcome Admin",
        data={
            "user": current_user["name"],
        },
    )