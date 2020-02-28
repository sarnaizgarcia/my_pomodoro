import json


class ConfigurationEntity:

    def __init__(self, pomodoro, short_break, long_break):
        self.pomodoro = pomodoro
        self.short_break = short_break
        self.long_break = long_break

    def to_json(self):
        return self.__dict__
