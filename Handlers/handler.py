from telebot import TeleBot

from Database.mondodb import *
from Mapper.mapping import *
from Api.api_client import *
from Parser.parser import *


@retry(exceptions=Exception, tries=10, delay=1)
def handle_message(bot: TeleBot, message):
    try:
        if message.text == get_button('russia'):
            with open(get_actual_data().get_image(), 'rb') as f:
                return bot.send_photo(message.chat.id, photo=f).photo
        elif message.text == get_button('world'):
            with open(get_actual_data(True).get_image(), 'rb') as f:
                return bot.send_photo(message.chat.id, photo=f).photo
        elif message.text == get_button('joke'):
            return bot.send_message(message.chat.id, get_joke())
        elif 'слава' in str(message.text).lower():
            return bot.send_message(message.chat.id, 'Слава мой создатель,но вообще мог бы и с пользой время потратить')
        else:
            return bot.send_message(message.chat.id, get_small_talk_response(message.text))
    except Exception:
        raise


def get_actual_data(world=False):
    if return_from_db(world) is not None:
        data = return_from_db(world)
        dif = to_datetime(get_timestamp()) - to_datetime(data['timestamp'])
        if abs(dif.total_seconds()) < 3600:
            return map_data(convert_to_json(data['data']), world)
        else:
            data = get_info(world)
            add_to_db(str(data), world)
            return map_data(data, world)
    else:
        data = get_info(world)
        add_to_db(str(data), world)
        return map_data(data, world)


def to_datetime(string_time) -> datetime:
    if type(string_time) == str:
        return datetime.datetime.strptime(string_time, '%Y-%m-%d %H:%M:%S')
    else:
        return string_time