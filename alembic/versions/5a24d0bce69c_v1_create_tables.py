"""v1_create_tables

Revision ID: 5a24d0bce69c
Revises: 
Create Date: 2025-06-14 11:56:13.042471

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '5a24d0bce69c'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.create_table(
        'transaction',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('seller_id', sa.Integer),
        sa.Column('cash_register_id', sa.Integer),
        sa.Column('transaction_time', sa.DateTime),
        sa.Column('transaction_audio', sa.String),
    )

    op.create_table(
        'rating',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('transaction_id', sa.Integer, sa.ForeignKey('transaction.id'), unique=True),
        sa.Column('rating_transaction', sa.Integer),
    )

def downgrade():
    op.drop_table('rating')
    op.drop_table('transaction')