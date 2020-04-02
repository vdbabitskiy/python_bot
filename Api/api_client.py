# -*- coding: utf-8 -*-
from Parser.parser import *
import apiai
import json


def get_small_talk(text):
    req = apiai.ApiAI(get_small_talk_token()).text_request()
    req.lang = 'ru'
    req.session_id = 'covid_bot'
    req.query = text
    resp = json.loads(req.getresponse().read().decode('utf-8'))['result']['fulfillment']['speech']
    return resp if resp else 'Я пока не очень умный, но ты пытайся...'


def get_covid_info():
    pass