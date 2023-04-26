"""empty message

Revision ID: 1f988a623a76
Revises: e0ba1f6aa238
Create Date: 2023-04-26 21:00:55.611998

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '1f988a623a76'
down_revision = 'e0ba1f6aa238'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('times', schema=None) as batch_op:
        batch_op.alter_column('creation_date',
               existing_type=postgresql.TIMESTAMP(timezone=True),
               type_=sa.DateTime(),
               existing_nullable=True,
               existing_server_default=sa.text('now()'))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('times', schema=None) as batch_op:
        batch_op.alter_column('creation_date',
               existing_type=sa.DateTime(),
               type_=postgresql.TIMESTAMP(timezone=True),
               existing_nullable=True,
               existing_server_default=sa.text('now()'))

    # ### end Alembic commands ###
