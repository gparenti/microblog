"""empty message

Revision ID: df553148ed9b
Revises: 68d7ce95352b
Create Date: 2023-09-10 21:51:22.413642

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'df553148ed9b'
down_revision = '68d7ce95352b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('to_do',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('task', sa.String(length=140), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('to_do', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_to_do_task'), ['task'], unique=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('to_do', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_to_do_task'))

    op.drop_table('to_do')
    # ### end Alembic commands ###