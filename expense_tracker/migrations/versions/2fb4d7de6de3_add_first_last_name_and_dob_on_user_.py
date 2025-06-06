"""Add first, last name and dob on user model

Revision ID: 2fb4d7de6de3
Revises: 245c70abd0a7
Create Date: 2025-04-30 19:04:54.883890

"""
from alembic import op
import sqlalchemy as sa
import sqlmodel             # NEW


# revision identifiers, used by Alembic.
revision = '2fb4d7de6de3'
down_revision = '245c70abd0a7'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.execute("TRUNCATE TABLE users CASCADE")
    op.add_column('users', sa.Column('first_name', sqlmodel.sql.sqltypes.AutoString(), nullable=False))
    op.add_column('users', sa.Column('last_name', sqlmodel.sql.sqltypes.AutoString(), nullable=False))
    op.add_column('users', sa.Column('dob', sa.DateTime(), nullable=False))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'dob')
    op.drop_column('users', 'last_name')
    op.drop_column('users', 'first_name')
    # ### end Alembic commands ###
