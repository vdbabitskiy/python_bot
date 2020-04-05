# -*- coding: utf-8 -*-
import telebot
from Handlers.handler import *
from telebot import types
from Api.api_client import *

bot = telebot.TeleBot(str(get_auth().token))


@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=5)
    info_btn_rus = types.KeyboardButton(get_button('russia'))
    info_btn_world = types.KeyboardButton(get_button('world'))
    markup.add(info_btn_rus, info_btn_world)

    bot.send_message(message.chat.id, "Привет "
                     + message.from_user.first_name
                     + ", выбери что тебя интересует", reply_markup=markup)


@bot.message_handler(content_types=['text'])
def process_message(message):
    try:
        types.ReplyKeyboardRemove(selective=False)
        bot.send_message(message.chat.id, handle_message(message.text), parse_mode='HTML')
    except Exception as e:
        print('Something wrong: {}'.format(e))
        bot.send_sticker(message.chat.id, get_stickers('something_wrong'))


if __name__ == '__main__':
    bot.polling(none_stop=True)
