from Database.mondodb import *
from Mapper.mapping import *
from Api.api_client import *
from Parser.parser import *


def handle_message(message):
    if message == get_button('russia'):
        return get_actual_data().show()
    elif message == get_button('world'):
        return get_actual_data(world=True).show()
    else:
        return get_small_talk_response(message)


def get_actual_data(world=False):
    if return_from_db(world) is not None:
        data = return_from_db(world)
        dif = to_datetime(get_timestamp()) - to_datetime(data['timestamp'])
        if abs(dif.total_seconds()) > 3600:
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
