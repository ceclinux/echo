"""empty message

Revision ID: 2a5ee36b4a3
Revises: 21ffa9a5f12
Create Date: 2015-06-07 23:28:34.973304

"""

# revision identifiers, used by Alembic.
revision = '2a5ee36b4a3'
down_revision = '21ffa9a5f12'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('tags', sa.String(length=1024), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'tags')
    ### end Alembic commands ###