from sqlalchemy import func
from telegram import Chat

from kmua.dao._db import _db, commit
from kmua.models.models import ChatData, Quote, UserData


def get_chat_by_id(chat_id: int) -> ChatData | None:
    return _db.query(ChatData).filter(ChatData.id == chat_id).first()


def add_chat(chat: Chat | ChatData) -> ChatData:
    """
    add chat if not exists

    :param chat: Chat or ChatData object
    :return: ChatData object
    """
    if chatdata := get_chat_by_id(chat.id):
        return chatdata
    _db.add(
        ChatData(
            id=chat.id,
            title=chat.title,
        )
    )
    commit()
    return get_chat_by_id(chat.id)


def get_chat_members(chat: Chat | ChatData) -> list[UserData]:
    _db_chat = get_chat_by_id(chat.id)
    if _db_chat is None:
        add_chat(chat)
        return []
    return _db_chat.members


def get_chat_members_id(chat: Chat | ChatData) -> list[int]:
    members = get_chat_members(chat)
    return [member.id for member in members]


def get_chat_quote_probability(chat: Chat | ChatData) -> float:
    _db_chat = get_chat_by_id(chat.id)
    if _db_chat is None:
        add_chat(chat)
        return 0.001
    return _db_chat.quote_probability


def update_chat_quote_probability(chat: Chat | ChatData, probability: float):
    _db_chat = get_chat_by_id(chat.id)
    if _db_chat is None:
        add_chat(chat)
        _db_chat = get_chat_by_id(chat.id)
    _db_chat.quote_probability = probability
    commit()


def get_chat_quotes(chat: Chat | ChatData) -> list[Quote]:
    _db_chat = get_chat_by_id(chat.id)
    if _db_chat is None:
        add_chat(chat)
        return []
    return _db_chat.quotes


def get_chat_random_quote(chat: Chat | ChatData) -> Quote | None:
    return (
        _db.query(Quote)
        .filter(Quote.chat_id == chat.id)
        .order_by(func.random())
        .first()
    )


def get_chat_quotes_count(chat: Chat | ChatData) -> int:
    return _db.query(Quote).filter(Quote.chat_id == chat.id).count()


def get_chat_quotes_page(
    chat: Chat | ChatData, page: int, page_size: int
) -> list[Quote]:
    return (
        _db.query(Quote)
        .filter(Quote.chat_id == chat.id)
        .offset((page - 1) * page_size)
        .limit(page_size)
        .all()
    )


def get_chat_quotes_message_id(chat: Chat | ChatData) -> list[int]:
    quotes = get_chat_quotes(chat)
    return [quote.message_id for quote in quotes]


def get_chat_bots(chat: Chat | ChatData) -> list[UserData]:
    """
    获取 chat 中的 bot
    """
    _db_chat = add_chat(chat)
    return [user for user in _db_chat.members if user.is_bot]


def get_chat_bots_id(chat: Chat | ChatData) -> list[int]:
    bots = get_chat_bots(chat)
    return [bot.id for bot in bots]


def get_chat_users_without_bots(chat: Chat | ChatData) -> list[UserData]:
    _db_chat = add_chat(chat)
    return [user for user in _db_chat.members if not user.is_bot]


def get_chat_users_without_bots_id(chat: Chat | ChatData) -> list[int]:
    users = get_chat_users_without_bots(chat)
    return [user.id for user in users]


def get_all_chats() -> list[ChatData]:
    return _db.query(ChatData).all()


def get_all_chats_id() -> list[int]:
    return [chat.id for chat in get_all_chats()]


def delete_chat(chat: Chat | ChatData):
    _db_chat = get_chat_by_id(chat.id)
    if _db_chat is None:
        return
    _db.delete(_db_chat)
    commit()


def get_all_chats_count() -> int:
    return _db.query(ChatData).count()


def get_chat_waifu_disabled(chat: Chat | ChatData) -> bool:
    _db_chat = add_chat(chat)
    return _db_chat.waifu_disabled


def update_chat_waifu_disabled(chat: Chat | ChatData, disabled: bool):
    _db_chat = add_chat(chat)
    _db_chat.waifu_disabled = disabled
    commit()


def get_chat_delete_events_enabled(chat: Chat | ChatData) -> bool:
    _db_chat = add_chat(chat)
    return _db_chat.delete_events_enabled


def update_chat_delete_events_enabled(chat: Chat | ChatData, enabled: bool):
    _db_chat = add_chat(chat)
    _db_chat.delete_events_enabled = enabled
    commit()


def get_chat_unpin_channel_pin_enabled(chat: Chat | ChatData) -> bool:
    _db_chat = add_chat(chat)
    return _db_chat.unpin_channel_pin_enabled


def update_chat_unpin_channel_pin_enabled(chat: Chat | ChatData, enabled: bool):
    _db_chat = add_chat(chat)
    _db_chat.unpin_channel_pin_enabled = enabled
    commit()


def get_chat_title_permissions(chat: Chat | ChatData) -> dict:
    _db_chat = add_chat(chat)
    if _db_chat.title_permissions is None:
        _db_chat.title_permissions = {}
        commit()
    return _db_chat.title_permissions


def update_chat_title_permissions(chat: Chat | ChatData, permissions: dict):
    _db_chat = add_chat(chat)
    _db_chat.title_permissions = permissions
    commit()


def get_chat_message_search_enabled(chat: Chat | ChatData) -> bool:
    _db_chat = add_chat(chat)
    return _db_chat.message_search_enabled


def update_chat_message_search_enabled(chat: Chat | ChatData, enabled: bool):
    _db_chat = add_chat(chat)
    _db_chat.message_search_enabled = enabled
    commit()
