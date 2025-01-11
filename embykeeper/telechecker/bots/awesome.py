from ._base import BotCheckin


class AwesomeCheckin(BotCheckin):
    name = "Awesome 群组签到"
    chat_name = "awesomegogo"
    bot_checkin_cmd = "签到"

    async def send_checkin(self, retry=False):
        await super().send_checkin(retry=retry)
        self.finished.set()
