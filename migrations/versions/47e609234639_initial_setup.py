"""initial setup

Revision ID: 47e609234639
Revises: None
Create Date: 2014-06-14 16:50:04.385760

"""

# revision identifiers, used by Alembic.
revision = '47e609234639'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('loans',
      sa.Column('id', sa.Integer(), nullable=False),
      sa.Column('json', sa.BLOB(), nullable=True),
      sa.PrimaryKeyConstraint('id')
    )
    op.create_table('lenders',
      sa.Column('id', sa.Integer(), nullable=False),
      sa.Column('username', sa.String(length=200), nullable=False),
      sa.Column('json', sa.BLOB(), nullable=True),
      sa.PrimaryKeyConstraint('id')
    )
    op.create_table('loan_lenders',
      sa.Column('id', sa.Integer(), nullable=False),
      sa.Column('json', sa.BLOB(), nullable=True),
      sa.PrimaryKeyConstraint('id')
    )
    op.create_table('recommendations',
      sa.Column('id', sa.Integer(), nullable=False),
      sa.Column('lender_id', sa.Integer(), nullable=False),
      sa.Column('loan_id', sa.Integer(), nullable=False),
      sa.Column('score', sa.Integer(), nullable=True),
      sa.PrimaryKeyConstraint('id')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('loans')
    op.drop_table('lenders')
    op.drop_table('recommendations')
    op.drop_table('loan_lenders')
    ### end Alembic commands ###

