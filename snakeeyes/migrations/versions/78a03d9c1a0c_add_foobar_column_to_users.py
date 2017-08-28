import sqlalchemy as sa

from alembic import op

from lib.util_datetime import tzware_datetime
from lib.util_sqlalchemy import AwareDateTime


"""
add foobar column to users

Revision ID: 78a03d9c1a0c
Revises: c778d2a5c16d
Create Date: 2017-08-28 09:32:41.249999
"""

# Revision identifiers, used by Alembic.
revision = '78a03d9c1a0c'
down_revision = 'c778d2a5c16d'
branch_labels = None
depends_on = None


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('foobar', sa.String(length=128), nullable=True))
    op.create_index(op.f('ix_users_foobar'), 'users', ['foobar'], unique=False)
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_users_foobar'), table_name='users')
    op.drop_column('users', 'foobar')
    ### end Alembic commands ###
