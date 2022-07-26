"""empty message

Revision ID: fd465a61f704
Revises: 3c66c9a64723
Create Date: 2022-07-25 18:05:03.831740

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fd465a61f704'
down_revision = '3c66c9a64723'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_commits_commit', table_name='commits')
    op.create_index(op.f('ix_commits_commit'), 'commits', ['commit'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_commits_commit'), table_name='commits')
    op.create_index('ix_commits_commit', 'commits', ['commit'], unique=False)
    # ### end Alembic commands ###
