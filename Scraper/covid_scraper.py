# -*- coding: utf-8 -*-
import requests
from Parser.parser import *
from lxml import html
import datetime


class Situation:

    def __init__(self, cases, recover, dead):
        self.cases = cases
        self.recover = recover
        self.dead = dead

    def get_time(self):
        return str(datetime.datetime.now().strftime('%H:%M'))

    def show(self):
        return '<b>Статистика по России на {} :</b>\n\nЗаразилось: <b>{}</b>\nВыздоровело: <b>{}</b>\nУмерло: <b>{}</b>' \
            .format(self.get_time(), self.cases, self.recover, self.dead)


def parse_covid():
    try:
        data = requests.get(get_scraper().source).text
        tree = html.fromstring(data)
        cases = tree.xpath(get_scraper().cases)[0]
        recover = tree.xpath(get_scraper().recovery)[0]
        dead = tree.xpath(get_scraper().dead)[0]
        return Situation(cases, recover, dead)
    except IndexError:
        info = 'нет информации'
        return Situation(info, info, info)