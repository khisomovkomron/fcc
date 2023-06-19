"""add foreign-key to post table

Revision ID: cb66914d67e1
Revises: 408cd84b412a
Create Date: 2023-06-19 11:44:04.791306

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cb66914d67e1'
down_revision = '408cd84b412a'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('owner_id', sa.Integer(), nullable=False))
    op.create_foreign_key('posts_users_fk', 
                          source_table='posts', 
                          referent_table='users', 
                          local_cols=['owner_id'], 
                          remote_cols=['id'], 
                          ondelete='CASCADE')


def downgrade() -> None:
    op.drop_constraint('post_users_fk', table_name='posts')
    op.drop_column('posts', 'owner_idalembic')