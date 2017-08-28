import sqlalchemy as sa

from alembic import op

from lib.util_datetime import tzware_datetime
from lib.util_sqlalchemy import AwareDateTime


"""
create foo table

Revision ID: 34bc17086a04
Revises: 
Create Date: 2017-08-28 07:40:40.127578
"""

# Revision identifiers, used by Alembic.
revision = '93278d92ea0a'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('foos',
    				sa.Column('id', sa.Integer, primary_key=True),
    				sa.Column('created_on', AwareDateTime(), default=tzware_datetime),
    				sa.Column('updated_on', AwareDateTime(), default=tzware_datetime, onupdate=tzware_datetime),
    				sa.Column('bar', sa.String(128), index=True))


def downgrade():
    op.drop_table('foos')
