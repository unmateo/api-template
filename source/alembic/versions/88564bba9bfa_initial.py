"""initial

Revision ID: 88564bba9bfa
Revises:
Create Date: 2020-06-15 00:47:31.841835

"""
import sqlalchemy as sa

from alembic import op
from api.models.orm.guid import GUID


# revision identifiers, used by Alembic.
revision = "88564bba9bfa"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "users",
        sa.Column("id", GUID(), nullable=False),
        sa.Column("created_at", sa.DateTime(), nullable=False),
        sa.Column("updated_at", sa.DateTime(), nullable=False),
        sa.Column("deleted", sa.Boolean(), nullable=False),
        sa.Column("username", sa.String(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("id"),
    )


def downgrade():
    op.drop_table("users")
