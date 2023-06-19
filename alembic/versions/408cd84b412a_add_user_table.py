"""add user table

Revision ID: 408cd84b412a
Revises: 050c691db65c
Create Date: 2023-06-19 11:36:37.299572

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '408cd84b412a'
down_revision = '050c691db65c'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('users', 
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('email', sa.String(), nullable=False),
                    sa.Column('password', sa.String(), nullable=False),
                    sa.Column('created_at', sa.TIMESTAMP(timezone=True), 
                              server_default=sa.text('now()'), nullable=False),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('email')
                    )


def downgrade() -> None:
    op.drop_table('users')
