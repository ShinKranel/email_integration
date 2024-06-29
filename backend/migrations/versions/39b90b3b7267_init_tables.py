"""Init tables

Revision ID: 39b90b3b7267
Revises: 
Create Date: 2024-06-29 18:18:03.773537

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = '39b90b3b7267'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('login', sa.String(), nullable=False),
    sa.Column('password', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('login'),
    sa.UniqueConstraint('login')
    )
    op.create_table('email',
    sa.Column('id', sa.String(), nullable=False),
    sa.Column('email_theme', sa.String(), nullable=False),
    sa.Column('send_date', sa.DateTime(), nullable=False),
    sa.Column('receive_date', sa.DateTime(), nullable=False),
    sa.Column('email_text', sa.String(), nullable=False),
    sa.Column('attached_files', postgresql.ARRAY(sa.String()), nullable=False),
    sa.Column('user_id', sa.String(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['user.login'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('email')
    op.drop_table('user')
    # ### end Alembic commands ###
