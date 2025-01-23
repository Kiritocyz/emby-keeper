from pyrogram.types import Message

from ._base import BotCheckin

__ignore__ = True


class HKACheckin(BotCheckin):
    name = "HKA"
    bot_username = "hkaemby_bot"
    bot_checkin_cmd = ["/cancel", "/start"]
    bot_text_ignore = ["对话已关闭"]

    