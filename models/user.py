import enum
import uuid

from core.database import Base
from sqlalchemy import Boolean, Column, Enum, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship


class RoleEnum(str, enum.Enum):
    USER = "USER"
    ADMIN = "ADMIN"


class ProviderEnum(str, enum.Enum):
    MANUAL = "MANUAL"
    GOOGLE = "GOOGLE"
    FACEBOOK = "FACEBOOK"
    LINKEDIN = "LINKEDIN"
    APPLE = "APPLE"


class User(Base):
    __tablename__ = "users"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)

    name = Column(String, nullable=True)
    email = Column(String, unique=True, index=True)
    password = Column(String, nullable=True)

    active = Column(Boolean, default=True)

    role = Column(Enum(RoleEnum), default=RoleEnum.USER, nullable=False)

    refresh_token = Column(String, default="")
    blocked = Column(Boolean, default=False)
    block_reason = Column(String, default="")

    provider = Column(Enum(ProviderEnum), default=ProviderEnum.MANUAL)

    facebook_id = Column(String, nullable=True)
    linkedin_id = Column(String, nullable=True)

    image = Column(String, nullable=True)

    assistants = relationship("Assistant", back_populates="owner")
