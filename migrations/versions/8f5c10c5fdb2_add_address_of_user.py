"""add address of user

Revision ID: 8f5c10c5fdb2
Revises: ab507952e291
Create Date: 2026-04-20 19:02:52.837511

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8f5c10c5fdb2'
down_revision = 'ab507952e291'
branch_labels = None
depends_on = None


def upgrade():
    op.execute("ALTER TABLE user ADD COLUMN address TEXT;")



def downgrade():
    op.execute("ALTER TABLE user DROP COLUMN address;")

