import yaml
from Models.scraper import Scraper
from Models.auth import Auth


def parse_config():
    with open('../configuration.yaml') as file:
        return yaml.load(file, Loader=yaml.FullLoader)


def get_auth():
    try:
        return Auth(parse_config()['auth']['token'])
    except yaml.YAMLError as exc:
        print(exc)


def get_small_talk_token():
    try:
        return parse_config()['auth']['small_talk']
    except yaml.YAMLError as exc:
        print(exc)


def get_joke_api():
    try:
        return parse_config()['api']['joke_api']
    except yaml.YAMLError as exc:
        print(exc)

def get_api():
    try:
        return parse_config()['api']['source']
    except yaml.YAMLError as exc:
        print(exc)


def get_connection_string():
    try:
        return parse_config()['database']['connection_string']
    except yaml.YAMLError as exc:
        print(exc)


def get_scraper():
    try:
        data = parse_config()
        src = data['scraper']['source']
        recovery = data['scraper']['stats']['recovered']
        dead = data['scraper']['stats']['dead']
        cases = data['scraper']['stats']['cases']
        return Scraper(source=src, recovery=recovery, dead=dead, cases=cases)
    except yaml.YAMLError as exc:
        print(exc)


def get_stickers(name):
    try:
        return parse_config()['stickers'][name]
    except yaml.YAMLError as exc:
        print(exc)


def get_button(location):
    try:
        return parse_config()['button_name'][location]
    except yaml.YAMLError as exc:
        print(exc)
