import datetime


class Situation:

    def __init__(self, cases, recover, dead, rate=None):
        self.cases = cases
        self.recover = recover
        self.dead = dead
        self.last_update = None
        self.death_rate: str = rate

    def get_time(self):
        return str(datetime.datetime.now().strftime('%H:%M'))

    def calculate_rate(self):
        if self.death_rate is None:
            return round(((int(self.dead.replace(' ', '')) / int(self.cases.replace(' ', ''))) * 100), 2)
        else:
            return round(float(self.death_rate))

    def show(self):
        return '======================\n' \
               '!!<b>Статистика на {} UTC</b>!!\n' \
               '======================\n> Заразилось: <b>{}</b>\n> Выздоровело: <b>{}</b>\n> Умерло: <b>{}</b>\n' \
               '> Общая смертность: <b>{}%</b>'\
            .format(self.get_time(), self.cases, self.recover, self.dead, self.calculate_rate())
