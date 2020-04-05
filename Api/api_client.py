# -*- coding: utf-8 -*-
from Parser.parser import *
from Models.situation import *
import apiai
import json
import requests
from lxml import html


def get_small_talk_response(text):
    req = apiai.ApiAI(get_small_talk_token()).text_request()
    req.lang = 'ru'
    req.session_id = 'covid_bot'
    req.query = text
    resp = json.loads(req.getresponse().read().decode('utf-8'))['result']['fulfillment']['speech']
    return resp if resp else 'Я пока не очень умный, но ты пытайся...'


def get_from_api() -> Situation:
    resp = requests.get(get_api()).json()
    return json.dumps(resp)['data']


def parse_from_site():
    try:
        return requests.get(get_scraper().source).text
    except Exception as e:
        print(e)


def get_info(world=False):
    return get_from_api() if world else parse_from_site()