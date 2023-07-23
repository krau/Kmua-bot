import asyncio

from telegram.ext import (
    CallbackQueryHandler,
    ChatMemberHandler,
    CommandHandler,
    ContextTypes,
    InlineQueryHandler,
    MessageHandler,
    filters,
)

from .callbacks.bnhhsh import bnhhsh
from .callbacks.chatmember import on_member_join, on_member_left, track_chats, set_greet
from .callbacks.help import help
from .callbacks.interact import interact
from .callbacks.keyword_reply import keyword_reply
from .callbacks.others import chat_migration, error_notice_control
from .callbacks.quote import (
    clear_chat_quote,
    clear_chat_quote_ask,
    clear_chat_quote_cancel,
    del_quote,
    inline_query_quote,
    quote,
    random_quote,
    set_quote_probability,
)
from .callbacks.rank import group_rank
from .callbacks.remake import remake
from .callbacks.start import start
from .callbacks.suicide import suicide
from .callbacks.title import title
from .callbacks.userdata import (
    clear_user_img_quote,
    clear_user_text_quote,
    delete_quote,
    next_page,
    prev_page,
    user_data_manage,
    user_quote_manage,
)
from .callbacks.chatdata import (
    clear_chat_data_ask,
    clear_chat_data,
    clear_chat_data_cancel,
)
from .callbacks.waifu import (
    clear_members_data,
    today_waifu,
    remove_waifu,
    waifu_graph,
    user_waifu_manage,
    set_mention,
    clear_waifu_data,
    migrate_waifu_shutdown,
    clear_chat_waifu,
)
from .config.config import settings
from .filters import (
    bnhhsh_filter,
    interact_filter,
    keyword_reply_filter,
    mention_or_private_filter,
)
from .logger import logger

# CommandHandlers
start_handler = CommandHandler("start", start, filters=mention_or_private_filter)
chat_migration_handler = MessageHandler(filters.StatusUpdate.MIGRATE, chat_migration)
title_handler = CommandHandler("t", title, filters=mention_or_private_filter)
quote_handler = CommandHandler("q", quote, filters=mention_or_private_filter)
set_quote_probability_handler = CommandHandler("setqp", set_quote_probability)
del_quote_handler = CommandHandler("d", del_quote)
clear_chat_quote_ask_handler = CommandHandler("clear_chat_quote", clear_chat_quote_ask)
clear_chat_data_ask_handler = CommandHandler("clear_chat_data", clear_chat_data_ask)
bnhhsh_command_handler = CommandHandler("bnhhsh", bnhhsh)
help_handler = CommandHandler("help", help, filters=mention_or_private_filter)
error_notice_control_handler = CommandHandler("error_notice", error_notice_control)
group_rank_handler = CommandHandler("rank", group_rank)
qrand_handler = CommandHandler("qrand", random_quote)
remake_handler = CommandHandler("remake", remake)
suicide_handler = CommandHandler("suicide", suicide)
today_waifu_handler = CommandHandler(
    "waifu", today_waifu, filters=filters.ChatType.GROUPS
)
waifu_graph_handler = CommandHandler(
    "waifu_graph", waifu_graph, filters=filters.ChatType.GROUPS
)
migrate_waifu_shutdown_handler = CommandHandler(
    "migrate_waifu_shutdown", migrate_waifu_shutdown
)
clear_waifu_data_handler = CommandHandler("clear_waifu_data", clear_waifu_data)
set_greet_handler = CommandHandler(
    "set_greet", set_greet, filters=filters.ChatType.GROUPS
)
clear_chat_waifu_handler = CommandHandler("clear_chat_waifu", clear_chat_waifu)

# CallbackQueryHandlers
start_callback_handler = CallbackQueryHandler(start, pattern="back_home")
clear_chat_data_handler = CallbackQueryHandler(
    clear_chat_data, pattern="clear_chat_data"
)
clear_chat_quote_handler = CallbackQueryHandler(
    clear_chat_quote, pattern="clear_chat_quote"
)
clear_chat_quote_cancel_handler = CallbackQueryHandler(
    clear_chat_quote_cancel, pattern="cancel_clear_chat_quote"
)
clear_user_img_quote_handler = CallbackQueryHandler(
    clear_user_img_quote, pattern="clear_user_img_quote"
)
clear_user_text_quote_handler = CallbackQueryHandler(
    clear_user_text_quote, pattern="clear_user_text_quote"
)

clear_chat_data_cancel_handler = CallbackQueryHandler(
    clear_chat_data_cancel, "cancel_clear_chat_data"
)
clear_members_data_handler = CallbackQueryHandler(
    clear_members_data, "clear_members_data"
)
remove_waifu_handler = CallbackQueryHandler(remove_waifu, pattern=r"remove_waifu")
user_data_manage_handler = CallbackQueryHandler(
    user_data_manage, pattern="user_data_manage"
)
user_quote_manage_handler = CallbackQueryHandler(
    user_quote_manage, pattern="user_quote_manage"
)
prev_page_handler = CallbackQueryHandler(prev_page, pattern=r"prev_page")
next_page_handler = CallbackQueryHandler(next_page, pattern=r"next_page")
delete_quote_handler = CallbackQueryHandler(delete_quote, pattern=r"delete_quote")
user_waifu_manage_handler = CallbackQueryHandler(
    user_waifu_manage, pattern="user_waifu_manage"
)
set_mention_handler = CallbackQueryHandler(set_mention, pattern="set_mention")


# others
interact_handler = MessageHandler(filters=interact_filter, callback=interact)
inline_query_handler = InlineQueryHandler(inline_query_quote)
random_quote_handler = MessageHandler(~filters.COMMAND, random_quote)
bnhhsh_handler = MessageHandler(bnhhsh_filter, bnhhsh)
keyword_reply_handler = MessageHandler(keyword_reply_filter, keyword_reply)
track_chats_handler = ChatMemberHandler(track_chats, ChatMemberHandler.MY_CHAT_MEMBER)
member_left_handler = MessageHandler(
    filters.StatusUpdate.LEFT_CHAT_MEMBER, on_member_left
)
member_join_handler = MessageHandler(
    filters.StatusUpdate.NEW_CHAT_MEMBERS, on_member_join
)

handlers = [
    start_handler,
    track_chats_handler,
    member_left_handler,
    member_join_handler,
    chat_migration_handler,
    title_handler,
    quote_handler,
    set_quote_probability_handler,
    del_quote_handler,
    qrand_handler,
    remake_handler,
    suicide_handler,
    today_waifu_handler,
    waifu_graph_handler,
    clear_waifu_data_handler,
    clear_chat_waifu_handler,
    clear_members_data_handler,
    set_greet_handler,
    start_callback_handler,
    clear_chat_quote_ask_handler,
    clear_chat_data_ask_handler,
    help_handler,
    error_notice_control_handler,
    clear_chat_quote_handler,
    clear_chat_data_handler,
    group_rank_handler,
    bnhhsh_command_handler,
    clear_chat_quote_cancel_handler,
    clear_chat_data_cancel_handler,
    interact_handler,
    remove_waifu_handler,
    keyword_reply_handler,
    bnhhsh_handler,
    inline_query_handler,
    user_data_manage_handler,
    user_quote_manage_handler,
    prev_page_handler,
    next_page_handler,
    delete_quote_handler,
    clear_user_img_quote_handler,
    clear_user_text_quote_handler,
    user_waifu_manage_handler,
    set_mention_handler,
    random_quote_handler,
]


async def on_error(update: object | None, context: ContextTypes.DEFAULT_TYPE):
    error = context.error
    # 如果聊天限制了 bot 发送消息, 忽略
    if error.__class__.__name__ == "BadRequest":
        if error.message == "Chat_write_forbidden":
            return
    logger.error(f"在该更新发生错误\n{update}\n错误信息\n{error.__class__.__name__}:{error}")
    if context.bot_data.get("error_notice", False):

        async def send_update_error(chat_id):
            await context.bot.send_message(
                chat_id=chat_id,
                text=f"在该更新发生错误\n{update}\n错误信息\n\n{context.error.__class__.__name__}:{context.error}",
            )

        tasks = [send_update_error(chat_id) for chat_id in settings.owners]
        await asyncio.gather(*tasks)
