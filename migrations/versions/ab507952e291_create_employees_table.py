"""create employees  table

Revision ID: ab507952e291
Revises: 0569954d522a
Create Date: 2026-04-20 18:38:36.634083

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ab507952e291'
down_revision = '0569954d522a'
branch_labels = None
depends_on = None


def upgrade():
    op.execute("""
        CREATE TABLE employee (
            id UUID PRIMARY KEY,
            user_id UUID,
            company_id UUID
        );
    """)

def downgrade():
    op.execute("DROP TABLE employee;")