import datetime


class Situation:

    def __init__(self, cases, recover, dead, rate=None):
        self.cases = cases
        self.recover = recover
        self.dead = dead
        self.last_update = None
        self.death_rate = rate

    def get_time(self):
        return str(datetime.datetime.now().strftime('%H:%M'))

    def calculate_rate(self):
        return self.death_rate or round(((int(self.dead.replace(' ', '')) / int(self.cases.replace(' ', ''))) * 100), 2)

    def show(self):
        return '<b>Статистика на {} :</b>\n\nЗаразилось: <b>{}</b>\nВыздоровело: <b>{}</b>\nУмерло: <b>{}</b>\n' \
               'Общая смертность: <b>{}%</b>' \
            .format(self.get_time(), self.cases, self.recover, self.dead, self.calculate_rate())
