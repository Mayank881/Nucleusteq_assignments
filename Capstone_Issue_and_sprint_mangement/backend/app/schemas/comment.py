from datetime import datetime

from pydantic import BaseModel, Field


class CreateCommentRequest(BaseModel):
    content: str = Field(
        ...,
        min_length=1,
        max_length=1000,
    )


class UpdateCommentRequest(BaseModel):
    content: str = Field(
        ...,
        min_length=1,
        max_length=1000,
    )


class CommentResponse(BaseModel):
    id: str
    issue_id: str
    user_id: str
    content: str
    created_at: datetime
    updated_at: datetime

class DeleteCommentResponse(BaseModel):
    message: str    