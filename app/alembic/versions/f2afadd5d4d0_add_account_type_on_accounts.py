"""Add account type on accounts

Revision ID: f2afadd5d4d0
Revises: a7a61ec3dac3
Create Date: 2019-03-20 03:54:13.741883

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql


# revision identifiers, used by Alembic.
revision = 'f2afadd5d4d0'
down_revision = 'a7a61ec3dac3'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('accounts', sa.Column('type', mysql.VARCHAR(length=255), nullable=True))


def downgrade():
    op.drop_column('accounts', 'type')
