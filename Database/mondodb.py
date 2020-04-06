import json
from json import JSONDecodeError

from pymongo import MongoClient
from pymongo.cursor import Cursor
from Parser.parser import *
import time
import datetime

client = MongoClient(get_connection_string())
db = client.covid_bot_database


def get_timestamp() -> datetime:
    return datetime.datetime.fromtimestamp(time.time(), datetime.timezone.utc).strftime('%Y-%m-%d %H:%M:%S')


def create_post(data):
    return {'timestamp': get_timestamp(), 'data': data}


def add_to_db(data, world=False):
    db.world_covid_info.insert_one(create_post(data)) if world else db.russian_covid_info.insert_one(create_post(data))


def return_from_db(world=False):
    try:
        return get_data(db.world_covid_info.find().sort([('_id', -1)]).limit(1)) if world else \
            get_data(db.russian_covid_info.find().sort([('_id', -1)]).limit(1))
    except Exception as e:
        print(e)
        return None


def get_data(cursor: Cursor):
    for item in cursor:
        return item


def convert_to_json(string_json):
    try:
        return json.loads(string_json.replace("'", "\""))
    except JSONDecodeError:
        return string_json

