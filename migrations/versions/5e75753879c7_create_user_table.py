"""create user table

Revision ID: 5e75753879c7
Revises: 
Create Date: 2026-04-20 18:32:17.381838

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5e75753879c7'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.execute("""
        CREATE TABLE user (
            id UUID PRIMARY KEY
        );
    """)

def downgrade():
    op.execute("DROP TABLE user;")