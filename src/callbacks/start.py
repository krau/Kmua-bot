from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import ContextTypes

from ..logger import logger
from ..common.message import message_recorder

from ..dao.db import db
from ..dao.user import (
    add_user,
    get_user_by_id,
)
from ..common.user import download_big_avatar

_start_bot_markup = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("Open source", url="https://github.com/krau/kmua-bot"),
            InlineKeyboardButton("Detail help", url="https://krau.github.io/kmua-bot/"),
        ],
        [
            InlineKeyboardButton("Your data", callback_data="user_data_manage"),
            InlineKeyboardButton("Quote manage", callback_data="user_quote_manage"),
        ],
        [
            InlineKeyboardButton("Waifu manage", callback_data="user_waifu_manage"),
            InlineKeyboardButton("Nya~", callback_data="noop"),
        ],
    ]
)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    logger.info(f"[{update.effective_user.name}] <start>")
    await message_recorder(update, context)
    if update.effective_chat.type != "private":
        if update.effective_message.text == "/start":
            # 如果是群聊，且没有艾特，直接返回
            return
        await _start_in_group(update, context)
        return

    if update.callback_query:
        if update.callback_query.message.photo:
            await update.callback_query.edit_message_caption(
                caption="Nya~",
                reply_markup=_start_bot_markup,
            )
            return
        await update.callback_query.edit_message_text(
            text="Nya~",
            reply_markup=_start_bot_markup,
        )
    db_bot_user = get_user_by_id(context.bot.id)
    if not db_bot_user:
        db_bot_user = add_user((await context.bot.get_me()))
        db_bot_user.avatar_big_blob = await download_big_avatar(context.bot.id, context)
        db.commit()
    photo = db_bot_user.avatar_big_id or db_bot_user.avatar_big_blob
    sent_message = await update.effective_message.reply_photo(
        photo=photo,
        caption="Nya~",
        reply_markup=_start_bot_markup,
    )
    db_bot_user.avatar_big_id = sent_message.photo[-1].file_id
    db.commit()


async def _start_in_group(update: Update, context: ContextTypes.DEFAULT_TYPE):
    logger.info(f"[{update.effective_user.name}] <start in group>")
    start_bot_markup = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    "PM me nya~", url=f"https://t.me/{context.bot.username}?start=start"
                )
            ],
            [
                InlineKeyboardButton(
                    "Open source", url="https://github.com/krau/kmua-bot"
                ),
                InlineKeyboardButton(
                    "Detail help", url="https://krau.github.io/kmua-bot/"
                ),
            ],
        ]
    )
    sent_message = await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="Nya!",
        reply_markup=start_bot_markup,
    )
    logger.info(f"Bot:{sent_message.text}")
