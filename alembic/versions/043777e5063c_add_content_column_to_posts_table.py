"""add content column to posts table

Revision ID: 043777e5063c
Revises: 04da055eb1a3
Create Date: 2022-10-28 22:51:46.255599

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '043777e5063c'
down_revision = '04da055eb1a3'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts',sa.Column('content', sa.String(), nullable=False))


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
