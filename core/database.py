# db/base.py
import importlib
import os
import pkgutil
from pathlib import Path

from core.config import settings
from sqlalchemy import Column, DateTime, create_engine, func, text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import declarative_base, sessionmaker

BaseModel = declarative_base()


class Base(BaseModel):
    __abstract__ = True
    id = Column(
        UUID(as_uuid=True),
        server_default=text("gen_random_uuid()"),
        primary_key=True,
        unique=True,
        nullable=False,
        index=True,
    )
    created_at = Column(
        DateTime(timezone=True), server_default=func.now(), nullable=False
    )
    updated_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
        nullable=False,
    )


BASE_DIR = os.path.dirname(os.path.dirname(__file__))
models_path = Path(BASE_DIR) / "models"

print(BASE_DIR)

for module_info in pkgutil.iter_modules([str(models_path)]):
    importlib.import_module(f"models.{module_info.name}")


engine = create_engine(
    settings.DATABASE_URL,
    pool_pre_ping=True,
)


SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
