"""users number

Revision ID: fc915266424c
Revises: 23a73509de38
Create Date: 2019-11-26 23:53:48.243362

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fc915266424c'
down_revision = '23a73509de38'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('num_whispers', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'num_whispers')
    # ### end Alembic commands ###
