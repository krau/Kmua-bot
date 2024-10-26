"""message_search_enabled for chatdata

Revision ID: 5ad3da643ecc
Revises: 6ff4aa4c3270
Create Date: 2024-06-25 20:14:55.638122

"""

from typing import Sequence, Union

import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision: str = "5ad3da643ecc"
down_revision: Union[str, None] = "6ff4aa4c3270"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "chat_data", sa.Column("message_search_enabled", sa.Boolean(), nullable=True)
    )

    if op.get_bind().dialect.name == "mysql":
        op.alter_column(
            "chat_data",
            "id",
            existing_type=sa.INTEGER(),
            type_=sa.BigInteger(),
            existing_nullable=False,
            autoincrement=False,
        )
        op.alter_column(
            "quotes",
            "chat_id",
            existing_type=sa.INTEGER(),
            type_=sa.BigInteger(),
            existing_nullable=True,
        )
        op.alter_column(
            "quotes",
            "message_id",
            existing_type=sa.INTEGER(),
            type_=sa.BigInteger(),
            existing_nullable=False,
        )
        op.alter_column(
            "quotes",
            "user_id",
            existing_type=sa.INTEGER(),
            type_=sa.BigInteger(),
            existing_nullable=True,
        )
        op.alter_column(
            "quotes",
            "qer_id",
            existing_type=sa.INTEGER(),
            type_=sa.BigInteger(),
            existing_nullable=True,
        )
        op.alter_column(
            "user_chat_association",
            "user_id",
            existing_type=sa.INTEGER(),
            type_=sa.BigInteger(),
            existing_nullable=False,
            autoincrement=False,
        )
        op.alter_column(
            "user_chat_association",
            "chat_id",
            existing_type=sa.INTEGER(),
            type_=sa.BigInteger(),
            existing_nullable=False,
            autoincrement=False,
        )
        op.alter_column(
            "user_chat_association",
            "waifu_id",
            existing_type=sa.INTEGER(),
            type_=sa.BigInteger(),
            existing_nullable=True,
        )
        op.alter_column(
            "user_data",
            "id",
            existing_type=sa.INTEGER(),
            type_=sa.BigInteger(),
            existing_nullable=False,
            autoincrement=False,
        )
        op.alter_column(
            "user_data",
            "married_waifu_id",
            existing_type=sa.INTEGER(),
            type_=sa.BigInteger(),
            existing_nullable=True,
        )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column(
        "user_data",
        "married_waifu_id",
        existing_type=sa.BigInteger(),
        type_=sa.INTEGER(),
        existing_nullable=True,
    )
    op.alter_column(
        "user_data",
        "id",
        existing_type=sa.BigInteger(),
        type_=sa.INTEGER(),
        existing_nullable=False,
        autoincrement=False,
    )
    op.alter_column(
        "user_chat_association",
        "waifu_id",
        existing_type=sa.BigInteger(),
        type_=sa.INTEGER(),
        existing_nullable=True,
    )
    op.alter_column(
        "user_chat_association",
        "chat_id",
        existing_type=sa.BigInteger(),
        type_=sa.INTEGER(),
        existing_nullable=False,
        autoincrement=False,
    )
    op.alter_column(
        "user_chat_association",
        "user_id",
        existing_type=sa.BigInteger(),
        type_=sa.INTEGER(),
        existing_nullable=False,
        autoincrement=False,
    )
    op.alter_column(
        "quotes",
        "qer_id",
        existing_type=sa.BigInteger(),
        type_=sa.INTEGER(),
        existing_nullable=True,
    )
    op.alter_column(
        "quotes",
        "user_id",
        existing_type=sa.BigInteger(),
        type_=sa.INTEGER(),
        existing_nullable=True,
    )
    op.alter_column(
        "quotes",
        "message_id",
        existing_type=sa.BigInteger(),
        type_=sa.INTEGER(),
        existing_nullable=False,
    )
    op.alter_column(
        "quotes",
        "chat_id",
        existing_type=sa.BigInteger(),
        type_=sa.INTEGER(),
        existing_nullable=True,
    )
    op.alter_column(
        "chat_data",
        "id",
        existing_type=sa.BigInteger(),
        type_=sa.INTEGER(),
        existing_nullable=False,
        autoincrement=False,
    )
    op.drop_column("chat_data", "message_search_enabled")
    # ### end Alembic commands ###
