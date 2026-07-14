from fastapi import APIRouter, Depends, status

from app.auth.authorization import RoleChecker
from app.schemas.comment import (
    CommentResponse,
    CreateCommentRequest,
    DeleteCommentResponse,
    UpdateCommentRequest,
)
from app.schemas.user import UserRole
from app.services.comment_service import (
    create_comment,
    delete_comment,
    update_comment,
)

router = APIRouter(
    prefix="/comments",
    tags=["Comments"],
)


@router.post(
    "/issues/{issue_id}",
    response_model=CommentResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_new_comment(
    issue_id: str,
    request: CreateCommentRequest,
    current_user=Depends(
        RoleChecker(
            [
                UserRole.ADMIN,
                UserRole.MEMBER,
            ]
        )
    ),
) -> CommentResponse:
    """
    Create a new comment on an issue.
    """

    return create_comment(
        issue_id,
        request,
        current_user,
    )


@router.put(
    "/{comment_id}",
    response_model=CommentResponse,
)
def update_existing_comment(
    comment_id: str,
    request: UpdateCommentRequest,
    current_user=Depends(
        RoleChecker(
            [
                UserRole.ADMIN,
                UserRole.MEMBER,
            ]
        )
    ),
) -> CommentResponse:
    """
    Update an existing comment.
    """

    return update_comment(
        comment_id,
        request,
        current_user,
    )


@router.delete(
    "/{comment_id}",
    response_model=DeleteCommentResponse,
)
def delete_existing_comment(
    comment_id: str,
    current_user=Depends(
        RoleChecker(
            [
                UserRole.ADMIN,
                UserRole.MEMBER,
            ]
        )
    ),
) -> DeleteCommentResponse:
    """
    Delete a comment.
    """

    return delete_comment(
        comment_id,
        current_user,
    )