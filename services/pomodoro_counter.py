import asyncio
import websockets
from os import environ

from model.configuration_model import ConfigurationModel
from model.task_model import TaskModel


class PomodorCounter():

    def __init__(self):
        self.pomodoro = environ['POMODORO']
        self.short_break = environ['SHORT_BREAK']
        self.long_break = environ['LONG_BREAK']

    def initialization(self):
        config_count = ConfigurationModel.config_count()
        if (config_count > 0):
            current_config = ConfigurationModel.get_configuration()
            self.pomodoro = current_config.pomodoro
            self.short_break = current_config.short_break
            self.long_break = current_config.long_break

    def update_config(self, pomodoro, short_break, long_break):

        self.pomodoro = pomodoro
        self.short_break = short_break
        self.long_break = long_break

    def break_time(self):
        task_done = TaskModel.number_of_done_task()
        result = 'short_break'

        if (task_done % 4) == 0:
            result = 'long_break'

        return result


pomodoro_counter = PomodorCounter()
