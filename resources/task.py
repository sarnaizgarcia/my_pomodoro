from flask_restful import Resource, reqparse

from controllers.create_task import create_task
from helper.flask_response_factory import flask_response_factory
from controllers.read_all_tasks import read_all_tasks

_task_parser = reqparse.RequestParser()
_task_parser.add_argument('name', type=str, required=True)
_task_parser.add_argument('description', type=str, required=True)
_task_parser.add_argument('state', type=str, required=True)


class Task(Resource):

    @classmethod
    def post(cls):
        data = _task_parser.parse_args()

        return flask_response_factory(create_task(**data))

    @classmethod
    def get(cls):
        return flask_response_factory(read_all_tasks())
