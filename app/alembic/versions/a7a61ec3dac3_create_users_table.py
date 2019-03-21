"""Create users table

Revision ID: a7a61ec3dac3
Revises: b9b23babaf75
Create Date: 2019-03-17 10:03:08.265822

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'a7a61ec3dac3'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('accounts',
    	sa.Column('id', mysql.INTEGER(display_width=11), nullable=False),
    	sa.Column('name', mysql.VARCHAR(length=255), nullable=True),
        sa.Column('email', mysql.VARCHAR(length=255), nullable=False, index=True),
        sa.Column('is_verified', mysql.INTEGER(), nullable=False, server_default=sa.text('0')),
        sa.Column('can_change_password', mysql.INTEGER(), nullable=False, server_default=sa.text('0')),
        sa.Column('is_skip_verification', mysql.INTEGER(), nullable=False, server_default=sa.text('0')),
        
        sa.Column('created_at', mysql.DATETIME(), nullable=False, server_default=sa.text('NOW()')),  
        sa.Column('updated_at', mysql.DATETIME(), nullable=False, server_default=sa.text('NOW()')),
        sa.Column('deleted_at', mysql.DATETIME(), nullable=True),
    	sa.PrimaryKeyConstraint('id'),
    	mysql_default_charset="UTF8MB4"
    	)

    op.create_unique_constraint("uq_accounts_email", "accounts", ["email"])

    op.create_table('accounts_oauths',
        sa.Column('id', mysql.INTEGER(), nullable=False),
        sa.Column('account_id', mysql.INTEGER(), sa.ForeignKey('accounts.id'), nullable=False, index=True),
        sa.Column('oauth_user_id', mysql.INTEGER(), nullable=False, index=True),
        
        sa.Column('created_at', mysql.DATETIME(), nullable=False, server_default=sa.text('NOW()')),  
        sa.Column('updated_at', mysql.DATETIME(), nullable=False, server_default=sa.text('NOW()')),
        sa.Column('deleted_at', mysql.DATETIME(), nullable=True),
        sa.PrimaryKeyConstraint('id'),
        mysql_default_charset='UTF8MB4'
    )

    op.create_table("teachers",
    	sa.Column("id", mysql.INTEGER(), nullable=False),
    	sa.Column("account_id", mysql.INTEGER(), sa.ForeignKey("accounts.id"), nullable=False, index=True),
        sa.Column('teaching_field', mysql.VARCHAR(length=255), nullable=False),

    	sa.Column('created_at', mysql.DATETIME(), nullable=False, server_default=sa.text('NOW()')),  
        sa.Column('updated_at', mysql.DATETIME(), nullable=False, server_default=sa.text('NOW()')),
        sa.Column('deleted_at', mysql.DATETIME(), nullable=True),
    	sa.PrimaryKeyConstraint('id'),
    	mysql_default_charset="UTF8MB4"
    	)

    op.create_table("students",
    	sa.Column("id", mysql.INTEGER(), nullable=False),
    	sa.Column("account_id", mysql.INTEGER(), sa.ForeignKey("accounts.id"), nullable=False, index=True),
        sa.Column('major', mysql.VARCHAR(length=255), nullable=False),

    	sa.Column('created_at', mysql.DATETIME(), nullable=False, server_default=sa.text('NOW()')),  
        sa.Column('updated_at', mysql.DATETIME(), nullable=False, server_default=sa.text('NOW()')),
        sa.Column('deleted_at', mysql.DATETIME(), nullable=True),
    	sa.PrimaryKeyConstraint('id'),
    	mysql_default_charset="UTF8MB4"
    	)



def downgrade():
	op.drop_table("students")
	op.drop_table("teachers")
	op.drop_table("accounts_oauths")
	op.drop_table("accounts")