"""Adding in facebook id

Revision ID: 32ebf8d50cc6
Revises: 47e609234639
Create Date: 2014-06-14 22:00:11.741654

"""

# revision identifiers, used by Alembic.
revision = '32ebf8d50cc6'
down_revision = '47e609234639'

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.add_column('lenders', sa.Column('facebook_id', sa.String(length=200), nullable=True))
    op.add_column('lenders', sa.Column('work', sa.String(length=200), nullable=True))
    op.add_column('lenders', sa.Column('location', sa.String(length=200), nullable=True))
    op.add_column('lenders', sa.Column('hometown', sa.String(length=200), nullable=True))


def downgrade():
    op.drop_column('lenders', 'facebook_id')
    op.drop_column('lenders', 'work')
    op.drop_column('lenders', 'location')
    op.drop_column('lenders', 'hometown')
