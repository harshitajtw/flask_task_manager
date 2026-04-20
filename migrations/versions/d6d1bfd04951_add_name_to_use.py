"""add name to use

Revision ID: d6d1bfd04951
Revises: ab507952e291
Create Date: 2026-04-20 18:47:43.854089

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd6d1bfd04951'
down_revision = 'ab507952e291'
branch_labels = None
depends_on = None


def upgrade():
    op.execute("ALTER TABLE user ADD COLUMN name VARCHAR(100);")



def downgrade():
    op.execute("ALTER TABLE user DROP COLUMN name;")
