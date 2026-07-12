from fastapi import HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm

from app.auth.jwt_handler import create_access_token
from app.auth.password import verify_password
from app.database import users_collection
from app.schemas.user import Token, UserLogin
from app.constants import app_constants
from app.exceptions.custom_exceptions import UnauthorizedException


INVALID_CREDENTIALS = app_constants.INVALID_CREDENTIALS

def login_user(login_data: OAuth2PasswordRequestForm) -> Token:
    """
    Authenticate a user and return a JWT access token.
    """

    # Find the user by email
    user = users_collection.find_one(
        {"email": login_data.username}
    )

    # Check if the user exists
    if not user:
        raise UnauthorizedException(
        detail=INVALID_CREDENTIALS,
    )

    # Verify the password
    if not verify_password(
        login_data.password,
        user["hashed_password"],
    ):
        raise UnauthorizedException(
            detail=INVALID_CREDENTIALS,
        )
           
    

    # Create JWT token
    access_token = create_access_token(
        data={
            "sub": user["email"],
            "role": user["role"],
        }
    )

    # Return the token
    return Token(
        access_token=access_token,
        token_type="bearer",
    )