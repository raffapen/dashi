"""empty message

Revision ID: 33336ff994e8
Revises: 47e84e16b150
Create Date: 2022-07-29 14:38:40.191828

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '33336ff994e8'
down_revision = '47e84e16b150'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_job_workflowId', table_name='job')
    op.create_index(op.f('ix_job_workflowId'), 'job', ['workflowId'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_job_workflowId'), table_name='job')
    op.create_index('ix_job_workflowId', 'job', ['workflowId'], unique=False)
    # ### end Alembic commands ###
