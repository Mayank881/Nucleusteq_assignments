from fastapi import Depends, HTTPException, status

from app.auth.authentication import get_current_user
from app.schemas.user import UserRole


class RoleChecker:
    """
    Dependency to check whether the current user has one
    of the required roles.
    """

    def __init__(self, allowed_roles: list[UserRole]):
        self.allowed_roles = allowed_roles

    def __call__(
        self,
        current_user: dict = Depends(get_current_user),
    ):
        """
        Check if the current user's role is allowed.
        """

        if current_user["role"] not in [
            role.value for role in self.allowed_roles
        ]:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="You are not authorized to perform this action.",
            )

        return current_user