"""empty message

Revision ID: c076eb857024
Revises: 5c4183ca1bdb
Create Date: 2019-11-18 14:50:13.652028

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c076eb857024'
down_revision = '5c4183ca1bdb'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('blog', sa.Column('user_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'blog', 'user', ['user_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'blog', type_='foreignkey')
    op.drop_column('blog', 'user_id')
    # ### end Alembic commands ###
