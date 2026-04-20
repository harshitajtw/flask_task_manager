"""add address of employee

Revision ID: 1f9588798e8f
Revises: b0d7d5b66630
Create Date: 2026-04-20 19:04:12.589522

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1f9588798e8f'
down_revision = 'b0d7d5b66630'
branch_labels = None
depends_on = None


def upgrade():
    op.execute("ALTER TABLE employee ADD COLUMN address TEXT;")



def downgrade():
    op.execute("ALTER TABLE employee DROP COLUMN address;")
