"""empty message

Revision ID: 0325a455aa2e
Revises: d979382af927
Create Date: 2023-09-11 14:55:20.118165

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0325a455aa2e'
down_revision = 'd979382af927'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('todo', schema=None) as batch_op:
        batch_op.alter_column('user_id',
               existing_type=sa.VARCHAR(length=200),
               type_=sa.Integer(),
               existing_nullable=True)
        batch_op.create_foreign_key(None, 'user', ['user_id'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('todo', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.alter_column('user_id',
               existing_type=sa.Integer(),
               type_=sa.VARCHAR(length=200),
               existing_nullable=True)

    # ### end Alembic commands ###
