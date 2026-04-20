"""add name to company

Revision ID: 6920bd9a0fc3
Revises: d6d1bfd04951
Create Date: 2026-04-20 18:48:29.457341

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6920bd9a0fc3'
down_revision = 'd6d1bfd04951'
branch_labels = None
depends_on = None


def upgrade():
    op.execute("ALTER TABLE company ADD COLUMN name VARCHAR(100);")



def downgrade():
    op.execute("ALTER TABLE company DROP COLUMN name;")

