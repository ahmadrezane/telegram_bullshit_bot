import os

import telebot
from loguru import logger


class bullshit:
    def __init__(self, username='ahmadrezane', message=f'Hi ahmadreza'):
        self.bot = telebot.TeleBot(os.environ['BOT_TOKEN'])
        self.message = message
        self.username = username
        self.reply = self.bot.message_handler(func=lambda message:True)(self.reply)
    def run(self):
        logger.info('Bot started......')
        self.bot.infinity_polling()
    def reply(self, message):
        user_name = message.__dict__['json']['from']['username']
        if user_name == self.username:
            self.bot.reply_to(message, self.message)

if __name__=='__main__':
    num1 = bullshit(username='moeinkaffash', message="معین باز کسشر گفتی؟")
    num1.run()

