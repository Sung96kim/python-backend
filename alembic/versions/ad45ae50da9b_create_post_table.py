"""create post table

Revision ID: ad45ae50da9b
Revises: 
Create Date: 2022-02-06 20:33:30.639903

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ad45ae50da9b'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('posts', sa.Column('id', sa.Integer(), nullable=False, primary_key=True),
                    sa.Column('title', sa.Column('title', sa.String(), nullable=False)))
    pass


def downgrade():
    op.drop_table('posts')
    pass
