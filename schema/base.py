from pydantic import BaseModel
from typing import Generic, TypeVar, Optional, List


def to_camel(string: str) -> str:
    parts = string.split("_")
    return parts[0] + "".join(word.capitalize() for word in parts[1:])


class CamelModel(BaseModel):
    class Config:
        alias_generator = to_camel
        populate_by_name = True
        from_attributes = True


T = TypeVar("T")


class ApiResponse(BaseModel, Generic[T]):
    success: bool
    detail: str
    data: Optional[T] = None


class PaginatedResponse(BaseModel, Generic[T]):
    items: List[T]
    page: int
    limit: int
    total: int
    total_pages: int
