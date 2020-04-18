from Models.situation import Situation
from Parser.parser import get_scraper
from lxml import html


def map_data(data, world=False):
    if world:
        cases = data['total_cases']
        recovered = data['recovery_cases']
        dead = data['death_cases']
        rate = data['general_death_rate']
        return Situation(cases, recovered, dead, rate)
    else:
        tree = html.fromstring(data)
        cases = tree.xpath(get_scraper().cases)[0]
        recovered = tree.xpath(get_scraper().recovery)[0]
        dead = str(tree.xpath(get_scraper().dead)[0])
        return Situation(cases, recovered, dead)