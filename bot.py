# -*- coding: utf-8 -*-
import telebot
from Scraper.covid_scraper import *
from telebot import types
from Api.api_client import *

bot = telebot.TeleBot(str(get_auth().token))


@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    info_btn = types.KeyboardButton('Информация по COVID-19')
    simple_talk = types.KeyboardButton('Поболтать')
    markup.add(info_btn, simple_talk)

    bot.send_message(message.chat.id, "Привет "
                     + message.from_user.first_name
                     + ", выбери что тебя интересует", reply_markup=markup)


@bot.message_handler(content_types=['text'])
def handle_message(message):
    if 'люблю' in message.text.lower():
        bot.send_sticker(message.chat.id, get_stickers('love'))
    elif message.text == 'Информация по COVID-19':
        types.ReplyKeyboardRemove(selective=False)
        bot.send_message(message.chat.id, parse_covid().show(), parse_mode='HTML')
    elif message.text == 'Поболтать':
        bot.send_message(message.chat.id, 'Ну давай болтать, дружок')
    else:
        bot.send_message(message.chat.id, get_small_talk(message.text))


if __name__ == '__main__':
    bot.polling(none_stop=True)
