"""init

Revision ID: 9ae115493cdc
Revises:
Create Date: 2026-03-11 16:26:02.217584
"""

from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = "9ae115493cdc"
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""

    op.create_table(
        "users",
        sa.Column("id", sa.UUID(), primary_key=True, nullable=False),
        sa.Column("name", sa.String(), nullable=True),
        sa.Column("email", sa.String(), nullable=False, unique=True, index=True),
        sa.Column("password", sa.String(), nullable=True),
        sa.Column(
            "active", sa.Boolean(), nullable=False, server_default=sa.text("true")
        ),
        sa.Column(
            "role",
            sa.Enum("USER", "ADMIN", name="roleenum"),
            nullable=False,
            server_default="USER",
        ),
        sa.Column("refresh_token", sa.String(), nullable=True, server_default=""),
        sa.Column(
            "blocked", sa.Boolean(), nullable=False, server_default=sa.text("false")
        ),
        sa.Column("block_reason", sa.String(), nullable=True, server_default=""),
        sa.Column(
            "provider",
            sa.Enum(
                "MANUAL",
                "GOOGLE",
                "FACEBOOK",
                "LINKEDIN",
                "APPLE",
                name="providerenum",
            ),
            nullable=False,
            server_default="MANUAL",
        ),
        sa.Column("facebook_id", sa.String(), nullable=True),
        sa.Column("linkedin_id", sa.String(), nullable=True),
        sa.Column("image", sa.String(), nullable=True),
        sa.Column("created_at", sa.DateTime(), nullable=False),
        sa.Column("updated_at", sa.DateTime(), nullable=False),
    )


def downgrade() -> None:
    """Downgrade schema."""

    op.drop_table("users")

    op.execute("DROP TYPE IF EXISTS roleenum")
    op.execute("DROP TYPE IF EXISTS providerenum")
