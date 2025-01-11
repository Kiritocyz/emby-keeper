from ._base import BotCheckin


class OracleCheckin(BotCheckin):
    name = "Oracle 群组签到"
    chat_name = "nba8668"
    bot_checkin_cmd = "签到"

    async def send_checkin(self, retry=False):
        await super().send_checkin(retry=retry)
        self.finished.set()
