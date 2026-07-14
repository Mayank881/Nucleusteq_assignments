from typing import Any

from app.schemas.api_response import ApiResponse


def success_response(message: str, data: Any = None) -> ApiResponse:
    return ApiResponse(
        success=True,
        message=message,
        data=data
    )