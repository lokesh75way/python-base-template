from sqlalchemy import Column, Integer, DateTime, func, text, Boolean
from sqlalchemy.dialects.postgresql import UUID


class IDPrimaryKeyModel:
    __abstract__ = True

    id = Column(Integer, primary_key=True, index=True)


class UUIDModel:
    __abstract__ = True

    id = Column(
        UUID(as_uuid=True),
        server_default=text("gen_random_uuid()"),
        primary_key=True,
        unique=True,
        nullable=False,
        index=True,
    )


class TimestampModel:
    __abstract__ = True

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False,
    )

    updated_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
        nullable=False,
    )


class SoftDelete:
    __abstract__ = True

    is_deleted = Column(
        Boolean,
        default=False,
        nullable=False,
        server_default=text("false"),
    )
    deleted_at = Column(DateTime(timezone=True), nullable=True)

    def soft_delete(self):
        if not self.is_deleted:
            self.is_deleted = True
            self.deleted_at = func.now()

    def restore(self):
        self.is_deleted = False
        self.deleted_at = None
