"""add content column to post table

Revision ID: 050c691db65c
Revises: 9508b353fb72
Create Date: 2023-06-19 11:32:02.944498

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '050c691db65c'
down_revision = '9508b353fb72'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', 
                  sa.Column('content', sa.String(), nullable=False))


def downgrade() -> None:
    op.drop_column('posts', 'content')
