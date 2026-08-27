from typing import List

from pydantic import BaseModel, ConfigDict


class ProjectCreate(BaseModel):
    name: str
    description: str

class ProjectUpdate(BaseModel):
    name: str
    description: str    


class MemberRequest(BaseModel):
    user_id: str


class ProjectResponse(BaseModel):
    id: str
    name: str
    description: str
    owner_id: str
    members: List[str]

    model_config = ConfigDict(from_attributes=True)

class PaginatedProjectResponse(BaseModel):
    items: List[ProjectResponse]
    page: int
    limit: int
    total: int
    total_pages: int    