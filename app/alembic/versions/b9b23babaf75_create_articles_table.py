"""Create articles table

Revision ID: b9b23babaf75
Revises: 
Create Date: 2019-03-15 04:14:13.345933

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql


# revision identifiers, used by Alembic.
revision = 'b9b23babaf75'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('sources',
		sa.Column('id', mysql.INTEGER(display_width=11), nullable=False),
		sa.Column('name', mysql.VARCHAR(length=255), nullable=True),
		sa.Column('domain', mysql.VARCHAR(length=255), nullable=True),
        sa.Column('base_url', mysql.VARCHAR(length=255), nullable=True),


        #add column here
        sa.Column('created_at', mysql.DATETIME(), nullable=False),
        sa.Column('updated_at', mysql.DATETIME(), nullable=False),
        sa.Column('deleted_at', mysql.DATETIME(), nullable=True),
        sa.PrimaryKeyConstraint('id'),
        mysql_default_charset='UTF8MB4'
    )

    op.create_table('articles',
        sa.Column('id', mysql.INTEGER(display_width=11), nullable=False),
        sa.Column('title', mysql.VARCHAR(length=255), nullable=True),
        sa.Column('source_id', mysql.INTEGER(display_width=11), sa.ForeignKey('sources.id'), nullable=False),
        sa.Column('summary', mysql.VARCHAR(length=1023), nullable=True),
        sa.Column('image_url', mysql.VARCHAR(length=1023), nullable=True),
        sa.Column('article_url', mysql.VARCHAR(length=1023), nullable=True),
        sa.Column('article_date', mysql.DATETIME(), nullable=True),
        sa.Column('published', mysql.DATETIME(), nullable=True),
        sa.Column('is_published', mysql.INTEGER(display_width=11), nullable=False, server_default=sa.text('0')),


        #add column here
        
        sa.Column('created_at', mysql.DATETIME(), nullable=False),  
        sa.Column('updated_at', mysql.DATETIME(), nullable=False),
        sa.Column('deleted_at', mysql.DATETIME(), nullable=True),
        sa.PrimaryKeyConstraint('id'),
        mysql_default_charset='UTF8MB4'
    )


def downgrade():
    op.drop_table("articles")
    op.drop_table("sources")
