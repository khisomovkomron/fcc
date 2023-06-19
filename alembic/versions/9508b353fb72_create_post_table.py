"""create post table

Revision ID: 9508b353fb72
Revises: 
Create Date: 2023-06-19 11:20:28.112089

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9508b353fb72'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('posts', sa.Column('id', sa.Integer(), nullable=False, primary_key=True), 
                             sa.Column('title', sa.String(), nullable=True))


def downgrade() -> None:
    op.drop_table('posts')
