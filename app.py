from os import environ

from flask import Flask
from flask_restful import Resource, Api
from flask_migrate import Migrate
from flask_socketio import SocketIO

from db import db

from resources.configuration import Configuration
from resources.task import Task
from resources.one_task import OneTask
from services.pomodoro_counter import pomodoro_counter


app_port = environ['APP_PORT']
debug_flag = environ['DEBUG'] == 'true'

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = environ['DB_PATH']
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True

migrate = Migrate(app, db)
api = Api(app)
socketIO = SocketIO(app)

api.add_resource(Configuration, '/config')
api.add_resource(Task, '/task')
api.add_resource(OneTask, '/task/<int:task_id>')

db.init_app(app)

with app.app_context():
    pomodoro_counter.initialization()


if __name__ == '__main__':
    socketIO.run(app, port=app_port)
