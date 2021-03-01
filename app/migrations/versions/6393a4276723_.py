"""empty message

Revision ID: 6393a4276723
Revises: 290ecd6b0404
Create Date: 2021-02-28 21:04:56.021003

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6393a4276723'
down_revision = '290ecd6b0404'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('images_1',
    sa.Column('id', sa.String(length=36), nullable=False),
    sa.Column('file_name', sa.String(length=256), nullable=False),
    sa.Column('created_date', sa.String(), nullable=True),
    sa.Column('s3_object_name', sa.String(), nullable=True),
    sa.Column('user_id', sa.String(length=64), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('images')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('images',
    sa.Column('id', sa.VARCHAR(length=36), autoincrement=False, nullable=False),
    sa.Column('file_name', sa.VARCHAR(length=256), autoincrement=False, nullable=False),
    sa.Column('created_date', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('s3_object_name', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('user_id', sa.VARCHAR(length=64), autoincrement=False, nullable=False),
    sa.Column('book_id', sa.VARCHAR(length=64), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='images_pkey')
    )
    op.drop_table('images_1')
    # ### end Alembic commands ###
