"""added owner name to property table

Revision ID: 59dbade86018
Revises: 36fd79e25a65
Create Date: 2023-12-19 11:11:20.304673

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '59dbade86018'
down_revision = '36fd79e25a65'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('properties', schema=None) as batch_op:
        batch_op.add_column(sa.Column('owner_name', sa.String(), nullable=True))
        batch_op.create_foreign_key(batch_op.f('fk_properties_owner_name_owners'), 'owners', ['owner_name'], ['name'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('properties', schema=None) as batch_op:
        batch_op.drop_constraint(batch_op.f('fk_properties_owner_name_owners'), type_='foreignkey')
        batch_op.drop_column('owner_name')

    # ### end Alembic commands ###
