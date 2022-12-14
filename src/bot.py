import os

import telebot
from loguru import logger

from src.make_button import keyboard, keys
import emoji

class bullshit:
    def __init__(self, username='enter username', message='enter message'):
        self.bot = telebot.TeleBot(os.environ['BOT_TOKEN'])
        self.message = message
        self.username = username
        self.handlers()
        # run bot
        logger.info('Bot started......')
        self.bot.infinity_polling()
    def handlers(self):
        @self.bot.message_handler(commands=['start', 'help'])
        def question(message):
            self.bot.send_message(
                message.chat.id,
                'How are you today?',
                reply_markup=keyboard.first
                )
        @self.bot.message_handler(func=lambda message:True)
        def answer(message):
            user_name = message.__dict__['json']['from']['username']
            if message.text == emoji.emojize(keys.very_good):
                self.bot.reply_to(message, 'Ok im happy for you', reply_markup=keyboard.second)
            elif message.text == emoji.emojize(keys.good):
                self.bot.reply_to(message, "That's good", reply_markup=keyboard.second )
            elif message.text == emoji.emojize(keys.bad):
                self.bot.reply_to(message, 'I know you will be ok', reply_markup=keyboard.second)
            elif message.text == emoji.emojize(keys.back):
                self.bot.send_message(
                message.chat.id,
                'How are you today?',
                reply_markup=keyboard.first
                )
            elif user_name == self.username:
                self.bot.reply_to(message, self.message)







if __name__=='__main__':
    num1 = bullshit(username='enter username', message='enter message')
    num1.run()

