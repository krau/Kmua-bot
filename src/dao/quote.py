from telegram import Chat, Message, User

from ..models.models import ChatData, Quote, UserData
from .db import db


def get_quote_by_link(link: str) -> Quote | None:
    return db.query(Quote).filter(Quote.link == link).first()


def delete_quote(quote: Quote):
    db.delete(quote)
    db.commit()


def delete_quote_by_link(link: str) -> bool:
    quote = get_quote_by_link(link)
    if quote is None:
        return False
    delete_quote(quote)
    return True


def add_quote(
    chat: Chat | ChatData,
    user: User | UserData | Chat,
    qer: User | UserData | Chat,
    message: Message,
    img: str = None,
) -> Quote:
    """
    add quote if not exists

    :param chat: Chat or ChatData object
    :param user: 被 q 的人 User or UserData object
    :param qer: 使用 q 的人
    :param message: Message object
    :param img: str, 图片的 file_id, defaults to None
    """
    link = message.link
    # 如果群组为公开群组, 将其转换为与私有群组相同的格式
    if chat.username is not None:
        link = f"https://t.me/c/{str(chat.id).removeprefix('-100')}/{message.id}"
    if quote := get_quote_by_link(link):
        return quote
    db.add(
        Quote(
            chat_id=chat.id,
            user_id=user.id,
            message_id=message.message_id,
            link=link,
            qer_id=qer.id,
            text=message.text,
            img=img,
        )
    )
    db.commit()
    return get_quote_by_link(message.link)
