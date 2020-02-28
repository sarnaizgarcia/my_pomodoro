import time
import threading

from flask_socketio import send

from services.pomodoro_counter import pomodoro_counter


stop = False


def pomodoro_message():
    while not stop:
        time.sleep(pomodoro_counter.pomodoro)
        break_type = pomodoro_counter.break_time()
        message = f'Now you can rest {pomodoro_counter[break_type]} seconds'
        send(message)
        time.sleep(pomodoro_counter[break_type])


class PomodoroClock():

    def __init__(self):
        self.thread = threading.Thread(target=pomodoro_message)

    def start_clock(self):
        stop = False
        self.thread.start()

    def stop_clock(self):
        stop = True
        self.thread.join()


pomodoro_clock = PomodoroClock()
