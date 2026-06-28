from enum import Enum

from pydantic import BaseModel, EmailStr, Field


class UserRole(str, Enum):
    """Supported user roles."""

    ADMIN = "ADMIN"
    MEMBER = "MEMBER"
    VIEWER = "VIEWER"


class UserCreate(BaseModel):
    """Schema for user registration."""

    name: str = Field(
        ...,
        min_length=2,
        max_length=100,
        description="Full name of the user",
    )
    email: EmailStr
    password: str = Field(
        ...,
        min_length=8,
        max_length=128,
        description="User password",
    )
    role: UserRole


class UserResponse(BaseModel):
    """Schema returned after successful registration."""

    id: str
    name: str
    email: EmailStr
    role: UserRole