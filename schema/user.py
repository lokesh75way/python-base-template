from enum import Enum
from typing import Optional

from pydantic import BaseModel, EmailStr


class RoleEnum(str, Enum):
    USER = "USER"
    ADMIN = "ADMIN"


class CreateUser(BaseModel):
    name: Optional[str]
    email: EmailStr
    password: str


class UpdateUser(BaseModel):
    name: Optional[str]
    email: Optional[EmailStr]


class LoginUser(BaseModel):
    email: EmailStr
    password: str


class UserResponse(BaseModel):
    id: str
    name: Optional[str]
    email: EmailStr
    role: RoleEnum

    class Config:
        from_attributes = True
