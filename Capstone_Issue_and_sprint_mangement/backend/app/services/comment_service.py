from datetime import datetime

from bson import ObjectId
from bson.errors import InvalidId
from fastapi import HTTPException, status

from app.constants.app_constants import (
    COMMENT_DELETED,
    COMMENT_NOT_FOUND,
    INVALID_ISSUE_ID,
    ISSUE_NOT_FOUND,
    ONLY_COMMENT_OWNER,
)

from app.database import (
    comments_collection,
    issues_collection,
)

from app.schemas.comment import (
    CommentResponse,
    CreateCommentRequest,
    DeleteCommentResponse,
    UpdateCommentRequest,
)


def create_comment(
    issue_id: str,
    request: CreateCommentRequest,
    current_user,
) -> CommentResponse:
    """
    Create a new comment for an issue.
    """

    try:
        issue_object_id = ObjectId(issue_id)

    except InvalidId:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=INVALID_ISSUE_ID,
        )

    issue = issues_collection.find_one(
        {
            "_id": issue_object_id,
        }
    )

    if not issue:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=ISSUE_NOT_FOUND,
        )

    comment_document = {
        "issue_id": issue_id,
        "user_id": str(current_user["_id"]),
        "content": request.content,
        "created_at": datetime.utcnow(),
        "updated_at": datetime.utcnow(),
    }

    result = comments_collection.insert_one(
        comment_document,
    )

    return CommentResponse(
        id=str(result.inserted_id),
        issue_id=issue_id,
        user_id=str(current_user["_id"]),
        content=request.content,
        created_at=comment_document["created_at"],
        updated_at=comment_document["updated_at"],
    )


def update_comment(
    comment_id: str,
    request: UpdateCommentRequest,
    current_user,
) -> CommentResponse:
    """
    Update an existing comment.
    """

    try:
        comment_object_id = ObjectId(comment_id)

    except InvalidId:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=COMMENT_NOT_FOUND,
        )

    comment = comments_collection.find_one(
        {
            "_id": comment_object_id,
        }
    )

    if not comment:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=COMMENT_NOT_FOUND,
        )

    if comment["user_id"] != str(current_user["_id"]):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail=ONLY_COMMENT_OWNER,
        )

    comments_collection.update_one(
        {
            "_id": comment_object_id,
        },
        {
            "$set": {
                "content": request.content,
                "updated_at": datetime.utcnow(),
            }
        },
    )

    updated_comment = comments_collection.find_one(
        {
            "_id": comment_object_id,
        }
    )

    return CommentResponse(
        id=str(updated_comment["_id"]),
        issue_id=updated_comment["issue_id"],
        user_id=updated_comment["user_id"],
        content=updated_comment["content"],
        created_at=updated_comment["created_at"],
        updated_at=updated_comment["updated_at"],
    )


def delete_comment(
    comment_id: str,
    current_user,
) -> DeleteCommentResponse:
    """
    Delete a comment.
    """

    try:
        comment_object_id = ObjectId(comment_id)

    except InvalidId:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=COMMENT_NOT_FOUND,
        )

    comment = comments_collection.find_one(
        {
            "_id": comment_object_id,
        }
    )

    if not comment:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=COMMENT_NOT_FOUND,
        )

    if comment["user_id"] != str(current_user["_id"]):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail=ONLY_COMMENT_OWNER,
        )

    comments_collection.delete_one(
        {
            "_id": comment_object_id,
        }
    )

    return DeleteCommentResponse(
        message=COMMENT_DELETED,
    )