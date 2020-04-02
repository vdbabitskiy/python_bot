import yaml
from Parser.scraper import Scraper
from Parser.auth import Auth


def parse_config():
    with open('configuration.yaml') as file:
        return yaml.load(file, Loader=yaml.FullLoader)


def get_auth():
    return Auth(parse_config()['auth']['token'])


def get_small_talk_token():
    return parse_config()['auth']['small_talk']


def get_scraper():
    data = parse_config()
    src = data['scraper']['source']
    recovery = data['scraper']['stats']['recovered']
    dead = data['scraper']['stats']['dead']
    cases = data['scraper']['stats']['cases']
    return Scraper(source=src, recovery=recovery, dead=dead, cases=cases)


def get_stickers(name):
    return parse_config()['stickers'][name]
