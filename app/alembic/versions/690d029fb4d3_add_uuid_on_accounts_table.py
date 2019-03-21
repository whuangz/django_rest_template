"""Add uuid on accounts table

Revision ID: 690d029fb4d3
Revises: f2afadd5d4d0
Create Date: 2019-03-20 04:25:07.650571

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '690d029fb4d3'
down_revision = 'f2afadd5d4d0'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('accounts', sa.Column('uuid', mysql.VARCHAR(length=255), nullable=True))


def downgrade():
    op.drop_column('accounts', 'uuid')
