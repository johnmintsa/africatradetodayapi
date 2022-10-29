"""add user table 

Revision ID: 450b01981b79
Revises: 043777e5063c
Create Date: 2022-10-28 23:57:35.079638

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '450b01981b79'
down_revision = '043777e5063c'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('users', sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('email',sa.String(), nullable=False),
        sa.Column('password', sa.String(), nullable=False),
        sa.Column('created_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('now()'), nullable=False),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('email')
    )
    print("done")
    pass


def downgrade() -> None:
    op.drop_table('users')
    pass
