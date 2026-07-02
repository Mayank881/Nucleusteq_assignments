from fastapi import APIRouter, Depends

from app.auth.authorization import RoleChecker
from app.schemas.user import UserRole

router = APIRouter(
    prefix="/admin",
    tags=["Admin"],
)


@router.get("/dashboard")
def admin_dashboard(
    current_user=Depends(
        RoleChecker([UserRole.ADMIN])
    ),
):
    """
    Admin-only dashboard endpoint.
    """
    return {
        "message": "Welcome Admin",
        "user": current_user["name"],
    }