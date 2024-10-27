"""adapt mysql

Revision ID: a7203cd2ce37
Revises: 798a99eb0695
Create Date: 2024-09-19 15:01:37.251193

"""

from typing import Sequence, Union

import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision: str = "a7203cd2ce37"
down_revision: Union[str, None] = "798a99eb0695"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    if op.get_bind().dialect.name != "mysql":
        return
    op.alter_column(
        "chat_data",
        "title",
        existing_type=sa.VARCHAR(length=128),
        type_=sa.String(length=256),
        existing_nullable=False,
    )
    op.alter_column(
        "quotes",
        "link",
        existing_type=sa.VARCHAR(length=128),
        type_=sa.String(length=256),
        existing_nullable=False,
    )
    op.alter_column(
        "quotes",
        "img",
        existing_type=sa.VARCHAR(length=128),
        type_=sa.String(length=256),
        existing_nullable=True,
    )
    op.create_index(op.f("ix_quotes_chat_id"), "quotes", ["chat_id"], unique=False)
    op.create_index(
        op.f("ix_quotes_message_id"), "quotes", ["message_id"], unique=False
    )
    op.create_index(op.f("ix_quotes_qer_id"), "quotes", ["qer_id"], unique=False)
    op.create_index(op.f("ix_quotes_user_id"), "quotes", ["user_id"], unique=False)
    op.create_index(
        op.f("ix_user_chat_association_chat_id"),
        "user_chat_association",
        ["chat_id"],
        unique=False,
    )
    op.create_index(
        op.f("ix_user_chat_association_user_id"),
        "user_chat_association",
        ["user_id"],
        unique=False,
    )
    op.create_index(
        op.f("ix_user_chat_association_waifu_id"),
        "user_chat_association",
        ["waifu_id"],
        unique=False,
    )
    op.alter_column(
        "user_data",
        "username",
        existing_type=sa.VARCHAR(length=32),
        type_=sa.String(length=64),
        existing_nullable=True,
    )
    op.alter_column(
        "user_data",
        "full_name",
        existing_type=sa.VARCHAR(length=128),
        type_=sa.String(length=256),
        existing_nullable=False,
    )
    op.alter_column(
        "user_data",
        "avatar_big_id",
        existing_type=sa.VARCHAR(length=128),
        type_=sa.String(length=256),
        existing_nullable=True,
    )
    op.create_index(
        op.f("ix_user_data_married_waifu_id"),
        "user_data",
        ["married_waifu_id"],
        unique=False,
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    if op.get_bind().dialect.name != "mysql":
        return
    op.drop_index(op.f("ix_user_data_married_waifu_id"), table_name="user_data")
    op.alter_column(
        "user_data",
        "avatar_big_id",
        existing_type=sa.String(length=256),
        type_=sa.VARCHAR(length=128),
        existing_nullable=True,
    )
    op.alter_column(
        "user_data",
        "full_name",
        existing_type=sa.String(length=256),
        type_=sa.VARCHAR(length=128),
        existing_nullable=False,
    )
    op.alter_column(
        "user_data",
        "username",
        existing_type=sa.String(length=64),
        type_=sa.VARCHAR(length=32),
        existing_nullable=True,
    )
    op.drop_index(
        op.f("ix_user_chat_association_waifu_id"), table_name="user_chat_association"
    )
    op.drop_index(
        op.f("ix_user_chat_association_user_id"), table_name="user_chat_association"
    )
    op.drop_index(
        op.f("ix_user_chat_association_chat_id"), table_name="user_chat_association"
    )
    op.drop_index(op.f("ix_quotes_user_id"), table_name="quotes")
    op.drop_index(op.f("ix_quotes_qer_id"), table_name="quotes")
    op.drop_index(op.f("ix_quotes_message_id"), table_name="quotes")
    op.drop_index(op.f("ix_quotes_chat_id"), table_name="quotes")
    op.alter_column(
        "quotes",
        "img",
        existing_type=sa.String(length=256),
        type_=sa.VARCHAR(length=128),
        existing_nullable=True,
    )
    op.alter_column(
        "quotes",
        "link",
        existing_type=sa.String(length=256),
        type_=sa.VARCHAR(length=128),
        existing_nullable=False,
    )
    op.alter_column(
        "chat_data",
        "title",
        existing_type=sa.String(length=256),
        type_=sa.VARCHAR(length=128),
        existing_nullable=False,
    )
    # ### end Alembic commands ###