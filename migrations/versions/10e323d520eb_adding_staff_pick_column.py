"""adding staff pick column

Revision ID: 10e323d520eb
Revises: 42ed287b538f
Create Date: 2014-06-15 13:17:32.206892

"""

# revision identifiers, used by Alembic.
revision = '10e323d520eb'
down_revision = '42ed287b538f'

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.add_column('loans', sa.Column('is_staff_pick', sa.Boolean(), nullable=True))
    op.add_column('loans', sa.Column('popularity'), sa.Integer(), nullable=True)

def downgrade():
  pass
