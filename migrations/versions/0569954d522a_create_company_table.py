"""create company  table

Revision ID: 0569954d522a
Revises: 5e75753879c7
Create Date: 2026-04-20 18:37:54.257561

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0569954d522a'
down_revision = '5e75753879c7'
branch_labels = None
depends_on = None


def upgrade():
    op.execute("""
        CREATE TABLE company (
            id UUID PRIMARY KEY,
            name VARCHAR(100)
        );
    """)

def downgrade():
    op.execute("DROP TABLE company;")