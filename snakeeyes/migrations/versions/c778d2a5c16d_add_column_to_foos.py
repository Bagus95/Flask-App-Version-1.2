import sqlalchemy as sa

from alembic import op

from lib.util_datetime import tzware_datetime
from lib.util_sqlalchemy import AwareDateTime


"""
add column to foos

Revision ID: c778d2a5c16d
Revises: 93278d92ea0a
Create Date: 2017-08-28 08:06:22.440132
"""

# Revision identifiers, used by Alembic.
revision = 'c778d2a5c16d'
down_revision = '93278d92ea0a'
branch_labels = None
depends_on = None


def upgrade():
    pass


def downgrade():
    pass
