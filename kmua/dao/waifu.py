import random
from itertools import chain
from typing import Generator

from telegram import Chat, User
from telegram.constants import ChatID

import kmua.dao.association as association_dao
import kmua.dao.chat as chat_dao
import kmua.dao.user as user_dao
from kmua.models.models import ChatData, UserChatAssociation, UserData

from ._db import _db, commit


def _get_user_waifu_in_chat_common(
    user: User | UserData, chat: Chat | ChatData
) -> UserData | None:
    db_user = user_dao.get_user_by_id(user.id)
    if db_user is None:
        user_dao.add_user(user)
        return None
    db_chat = chat_dao.get_chat_by_id(chat.id)
    if db_chat is None:
        chat_dao.add_chat(chat)
        return None
    association = association_dao.get_association_in_chat_by_user(chat, user)
    if association is None:
        return None
    if association.waifu_id is None:
        return None
    return user_dao.get_user_by_id(association.waifu_id)


def get_user_waifu_in_chat(
    user: User | UserData, chat: Chat | ChatData
) -> UserData | None:
    """获取 user 在 chat 中的 waifu

    如果没有 waifu, 但 is_married 为 True, 则返回 married_waifu
    """
    db_user = user_dao.add_user(user)
    if db_user.married_waifu_id is not None:
        return user_dao.get_user_by_id(db_user.married_waifu_id)
    return _get_user_waifu_in_chat_common(user, chat)


def get_user_waifu_in_chat_exclude_married(
    user: User | UserData, chat: Chat | ChatData
) -> UserData | None:
    """获取 user 在 chat 中的 waifu

    不考虑 married_waifu
    """
    return _get_user_waifu_in_chat_common(user, chat)


def get_user_waifu_of_in_chat(
    user: User | UserData, chat: Chat | ChatData
) -> list[UserData] | None:
    """
    获取 user 被 chat 中的哪些人选为了 waifu
    """
    db_user = user_dao.get_user_by_id(user.id)
    if db_user is None:
        user_dao.add_user(user)
        return None
    db_chat = chat_dao.get_chat_by_id(chat.id)
    if db_chat is None:
        chat_dao.add_chat(chat)
        return None
    associations = association_dao.get_associations_of_user_waifu_of_in_chat(
        db_user, db_chat
    )
    if not associations:
        return None
    return [
        user_dao.get_user_by_id(association.user_id) for association in associations
    ]


def get_chat_married_users(
    chat: Chat | ChatData,
) -> Generator[UserData, None, None] | None:
    db_chat = chat_dao.get_chat_by_id(chat.id)
    if db_chat is None:
        chat_dao.add_chat(chat)
        return None
    return (user for user in db_chat.members if user.is_married)


def get_chat_married_users_id(chat: Chat) -> Generator[int, None, None]:
    married_user = get_chat_married_users(chat)
    return (user.id for user in married_user)


def get_user_married_waifu(user: User) -> UserData | None:
    db_user = user_dao.get_user_by_id(user.id)
    if db_user is None:
        user_dao.add_user(user)
        return None
    if married_waifu_id := db_user.married_waifu_id:
        return user_dao.get_user_by_id(married_waifu_id)
    return None


def put_user_waifu_in_chat(
    user: User | UserData, chat: Chat | ChatData, waifu: User | UserData
) -> bool:
    if get_user_waifu_in_chat_exclude_married(user, chat) is not None:
        return False
    if user_dao.get_user_by_id(waifu.id) is None:
        user_dao.add_user(waifu)
    if association := association_dao.get_association_in_chat_by_user(chat, user):
        if association.waifu_id is None:
            association.waifu_id = waifu.id
            commit()
            return True
        return False
    association_dao.add_association_in_chat(chat, user, waifu)
    commit()
    return True


def refresh_user_waifu_in_chat(user: User | UserData, chat: Chat | ChatData):
    association = association_dao.get_association_in_chat_by_user(chat, user)
    if association is None:
        return
    association.waifu_id = None
    commit()


def get_chat_users_has_waifu(chat: Chat | ChatData) -> Generator[UserData, None, None]:
    """
    获取 chat 中有 waifu 的人

    :param chat: Chat or ChatData object
    :return: list of UserData object
    """
    db_chat = chat_dao.add_chat(chat)
    associations = (
        _db.query(UserChatAssociation)
        .filter(
            UserChatAssociation.chat_id == db_chat.id,
            UserChatAssociation.waifu_id is not None,
        )
        .all()
    )
    return (
        user_dao.get_user_by_id(association.user_id) for association in associations
    )


def get_chat_users_was_waifu(chat: Chat | ChatData) -> Generator[UserData, None, None]:
    """
    获取 chat 中被选为 waifu 的人

    :param chat: Chat or ChatData object
    :return: list of UserData object
    """
    db_chat = chat_dao.add_chat(chat)
    associations = (
        _db.query(UserChatAssociation)
        .filter(
            UserChatAssociation.chat_id == db_chat.id,
            UserChatAssociation.waifu_id is not None,
        )
        .all()
    )
    return (
        user_dao.get_user_by_id(association.waifu_id) for association in associations
    )


def get_chat_user_participated_waifu_data(
    chat: Chat | ChatData,
) -> tuple[Generator[UserData, None, None], int]:
    """
    获取 chat 中参与了抽老婆的用户生成器和参与人数
    """
    db_chat = chat_dao.add_chat(chat)
    associations = (
        _db.query(UserChatAssociation)
        .filter(
            UserChatAssociation.chat_id == db_chat.id,
            UserChatAssociation.waifu_id.isnot(None),
        )
        .all()
    )

    users_id_participated = {association.user_id for association in associations} | {
        association.waifu_id
        for association in associations
        if association.waifu_id is not None
    }

    def user_generator():
        for user_id in users_id_participated:
            yield user_dao.get_user_by_id(user_id)

    return user_generator(), len(users_id_participated)


async def refresh_all_waifu_data():
    association_dao.update_associations_all_waifu_id_to_none()
    commit()


def refresh_user_all_waifu(user: User | UserData):
    db_user = user_dao.add_user(user)
    associations = association_dao.get_associations_of_user(db_user)
    for association in associations:
        association.waifu_id = None
    commit()


def get_user_waifus(user: User | UserData) -> Generator[UserData, None, None]:
    db_user = user_dao.add_user(user)
    associations = association_dao.get_associations_of_user(db_user)
    for association in associations:
        if association.waifu_id is not None:
            yield user_dao.get_user_by_id(association.waifu_id)


def get_user_waifus_with_chat(
    user: User | UserData,
) -> Generator[tuple[UserData, ChatData], None, None]:
    db_user = user_dao.add_user(user)
    associations = association_dao.get_associations_of_user(db_user)
    for association in associations:
        if association.waifu_id is not None:
            yield (
                user_dao.get_user_by_id(association.waifu_id),
                chat_dao.get_chat_by_id(association.chat_id),
            )


def get_user_waifus_of(user: User | UserData) -> Generator[UserData, None, None]:
    db_user = user_dao.add_user(user)
    associations = association_dao.get_associations_of_user_waifu_of(db_user)
    for association in associations:
        yield user_dao.get_user_by_id(association.user_id)


def get_user_waifus_of_with_chat(
    user: User | UserData,
) -> Generator[tuple[UserData, ChatData], None, None]:
    db_user = user_dao.add_user(user)
    associations = association_dao.get_associations_of_user_waifu_of(db_user)
    for association in associations:
        yield (
            user_dao.get_user_by_id(association.user_id),
            chat_dao.get_chat_by_id(association.chat_id),
        )


def take_waifu_for_user_in_chat(
    user: User | UserData, chat: Chat | ChatData
) -> UserData:
    """为 user 在 chat 中抽取一个 waifu

    如果要获取 user 当前的 waifu, 请使用 get_user_waifu_in_chat

    Arguments:
        user -- User to get waifu for
        chat -- Chat to get waifu in

    Returns:
        UserData -- Waifu for user in chat
    """
    chat_dao.add_chat(chat)
    user_dao.add_user(user)
    members = chat_dao.get_chat_users_without_bots(chat)
    filtered_members = (
        userdata
        for userdata in members
        if not (
            userdata.id == user.id
            or userdata.is_married
            or userdata.id
            in (ChatID.FAKE_CHANNEL, ChatID.ANONYMOUS_ADMIN, ChatID.SERVICE_CHAT)
        )
    )
    filtered_members_list = list(filtered_members)
    if not filtered_members_list:
        return None
    return random.choice(filtered_members_list)
