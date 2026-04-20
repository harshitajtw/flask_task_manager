"""add address of company

Revision ID: b0d7d5b66630
Revises: 8f5c10c5fdb2
Create Date: 2026-04-20 19:03:36.846398

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b0d7d5b66630'
down_revision = "8f5c10c5fdb2"
branch_labels = None
depends_on = None


def upgrade():
    op.execute("ALTER TABLE company ADD COLUMN address TEXT;")



def downgrade():
    op.execute("ALTER TABLE company DROP COLUMN address;")

