from linebot import LineBotApi
from linebot.models import TextSendMessage
import os

class NoticeSender:

    def __init__(self):
        self.token = os.getenv('TOKEN')
        self.line_id = os.getenv('DST_ID')
        self.api = LineBotApi(self.token)

    def send(self, message):
        print(f'send {message}')
        self.api.push_message(self.line_id, TextSendMessage(text=message))
