"""adding status to loan table

Revision ID: 42ed287b538f
Revises: 352fee31f96a
Create Date: 2014-06-15 11:38:24.372639

"""

# revision identifiers, used by Alembic.
revision = '42ed287b538f'
down_revision = '352fee31f96a'

from alembic import op
import sqlalchemy as sa


def upgrade():
  op.add_column('loans', sa.Column('status', sa.String(length=50), nullable=True))


def downgrade():
  op.drop_column('loans', 'status')
