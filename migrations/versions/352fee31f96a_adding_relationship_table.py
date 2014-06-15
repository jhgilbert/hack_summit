"""Adding relationship table

Revision ID: 352fee31f96a
Revises: 32ebf8d50cc6
Create Date: 2014-06-15 11:13:32.477953

"""

# revision identifiers, used by Alembic.
revision = '352fee31f96a'
down_revision = '32ebf8d50cc6'

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.create_table('friends',
      sa.Column('lender_id', sa.Integer(), nullable=False),
      sa.Column('friend_id', sa.Integer(), nullable=False),
      sa.ForeignKeyConstraint(['lender_id'], ['lenders.id'], ),
      sa.ForeignKeyConstraint(['friend_id'], ['lenders.id'], ),
      sa.PrimaryKeyConstraint()
    )

def downgrade():
  op.drop_table('friends')
