from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer

from app.auth.jwt_handler import decode_access_token
from app.database import users_collection

oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="/users/login"
)

def get_current_user(
    token: str = Depends(oauth2_scheme),
):
    """
    Validate JWT token and return the current user.
    """

    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials.",
    )

    payload = decode_access_token(token)

    if not payload:
        raise credentials_exception

    email = payload.get("sub")

    if email is None:
        raise credentials_exception

    user = users_collection.find_one(
        {"email": email}
    )

    if not user:
        raise credentials_exception

    return user