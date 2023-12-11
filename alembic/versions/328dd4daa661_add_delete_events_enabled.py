"""add delete_events_enabled

Revision ID: 328dd4daa661
Revises: fbcd18a27f96
Create Date: 2023-12-11 21:06:41.454858

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '328dd4daa661'
down_revision: Union[str, None] = 'fbcd18a27f96'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('chat_data', sa.Column('delete_events_enabled', sa.Boolean(), nullable=True))

    # 如使用 Mysql 则去除注释

    # op.alter_column('chat_data', 'id',
    #            existing_type=sa.INTEGER(),
    #            type_=sa.BigInteger(),
    #            existing_nullable=False,
    #            autoincrement=False)
    # op.alter_column('quotes', 'chat_id',
    #            existing_type=sa.INTEGER(),
    #            type_=sa.BigInteger(),
    #            existing_nullable=True)
    # op.alter_column('quotes', 'message_id',
    #            existing_type=sa.INTEGER(),
    #            type_=sa.BigInteger(),
    #            existing_nullable=False)
    # op.alter_column('quotes', 'user_id',
    #            existing_type=sa.INTEGER(),
    #            type_=sa.BigInteger(),
    #            existing_nullable=True)
    # op.alter_column('quotes', 'qer_id',
    #            existing_type=sa.INTEGER(),
    #            type_=sa.BigInteger(),
    #            existing_nullable=True)
    # op.alter_column('user_chat_association', 'user_id',
    #            existing_type=sa.INTEGER(),
    #            type_=sa.BigInteger(),
    #            existing_nullable=False,
    #            autoincrement=False)
    # op.alter_column('user_chat_association', 'chat_id',
    #            existing_type=sa.INTEGER(),
    #            type_=sa.BigInteger(),
    #            existing_nullable=False,
    #            autoincrement=False)
    # op.alter_column('user_chat_association', 'waifu_id',
    #            existing_type=sa.INTEGER(),
    #            type_=sa.BigInteger(),
    #            existing_nullable=True)
    # op.alter_column('user_data', 'id',
    #            existing_type=sa.INTEGER(),
    #            type_=sa.BigInteger(),
    #            existing_nullable=False,
    #            autoincrement=False)
    # op.alter_column('user_data', 'married_waifu_id',
    #            existing_type=sa.INTEGER(),
    #            type_=sa.BigInteger(),
    #            existing_nullable=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###

    # 如使用 Mysql 则去除注释

    # op.alter_column('user_data', 'married_waifu_id',
    #            existing_type=sa.BigInteger(),
    #            type_=sa.INTEGER(),
    #            existing_nullable=True)
    # op.alter_column('user_data', 'id',
    #            existing_type=sa.BigInteger(),
    #            type_=sa.INTEGER(),
    #            existing_nullable=False,
    #            autoincrement=False)
    # op.alter_column('user_chat_association', 'waifu_id',
    #            existing_type=sa.BigInteger(),
    #            type_=sa.INTEGER(),
    #            existing_nullable=True)
    # op.alter_column('user_chat_association', 'chat_id',
    #            existing_type=sa.BigInteger(),
    #            type_=sa.INTEGER(),
    #            existing_nullable=False,
    #            autoincrement=False)
    # op.alter_column('user_chat_association', 'user_id',
    #            existing_type=sa.BigInteger(),
    #            type_=sa.INTEGER(),
    #            existing_nullable=False,
    #            autoincrement=False)
    # op.alter_column('quotes', 'qer_id',
    #            existing_type=sa.BigInteger(),
    #            type_=sa.INTEGER(),
    #            existing_nullable=True)
    # op.alter_column('quotes', 'user_id',
    #            existing_type=sa.BigInteger(),
    #            type_=sa.INTEGER(),
    #            existing_nullable=True)
    # op.alter_column('quotes', 'message_id',
    #            existing_type=sa.BigInteger(),
    #            type_=sa.INTEGER(),
    #            existing_nullable=False)
    # op.alter_column('quotes', 'chat_id',
    #            existing_type=sa.BigInteger(),
    #            type_=sa.INTEGER(),
    #            existing_nullable=True)
    # op.alter_column('chat_data', 'id',
    #            existing_type=sa.BigInteger(),
    #            type_=sa.INTEGER(),
    #            existing_nullable=False,
    #            autoincrement=False)
    op.drop_column('chat_data', 'delete_events_enabled')
    # ### end Alembic commands ###