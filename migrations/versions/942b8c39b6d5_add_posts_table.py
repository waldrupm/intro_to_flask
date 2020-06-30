"""add posts table

Revision ID: 942b8c39b6d5
Revises: be24f9062746
Create Date: 2020-06-30 11:57:28.829261

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '942b8c39b6d5'
down_revision = 'be24f9062746'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('post',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(), nullable=True),
    sa.Column('body', sa.Text(), nullable=True),
    sa.Column('created_on', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('post')
    # ### end Alembic commands ###
