"""add last columns

Revision ID: 71bcba59acf9
Revises: 4c5d63b86674
Create Date: 2022-10-29 01:21:21.678824

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '71bcba59acf9'
down_revision = '4c5d63b86674'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column(
        'published', sa.Boolean(), nullable=False, server_default='TRUE'),)
    op.add_column('posts', sa.Column(
        'created_at', sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text('NOW()')),)
    pass

def downgrade() -> None:
    op.drop_column('posts', 'published')
    op.drop_column('posts', 'created_at')
    pass
