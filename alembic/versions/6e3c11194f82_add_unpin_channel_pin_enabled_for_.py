"""add unpin_channel_pin_enabled for chatdata

Revision ID: 6e3c11194f82
Revises: 328dd4daa661
Create Date: 2024-01-26 13:52:40.227118

"""

from typing import Sequence, Union

import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision: str = "6e3c11194f82"
down_revision: Union[str, None] = "328dd4daa661"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "chat_data", sa.Column("unpin_channel_pin_enabled", sa.Boolean(), nullable=True)
    )
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
    op.drop_column("chat_data", "unpin_channel_pin_enabled")
    # ### end Alembic commands ###
