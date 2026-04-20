"""add name to employees

Revision ID: 0f917c0cd5ff
Revises: 6920bd9a0fc3
Create Date: 2026-04-20 18:49:20.518798

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0f917c0cd5ff'
down_revision = '6920bd9a0fc3'
branch_labels = None
depends_on = None


def upgrade():
    op.execute("ALTER TABLE employee ADD COLUMN name VARCHAR(100);")



def downgrade():
    op.execute("ALTER TABLE employee ADD COLUMN name VARCHAR(100);")

