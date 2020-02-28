from flask_restful import Resource, reqparse

from controllers.read_one_task import read_one_task
from helper.flask_response_factory import flask_response_factory
from controllers.update_one_task import update_one_task
from controllers.update_task_state import update_task_state

_task_parser = reqparse.RequestParser()
_task_parser.add_argument('name', type=str, required=True)
_task_parser.add_argument('description', type=str, required=True)
_task_parser.add_argument('state', type=str, required=True)

_task_state_parser = reqparse.RequestParser()
_task_state_parser.add_argument('state', type=str, required=True)


class OneTask(Resource):

    @classmethod
    def get(cls, task_id):
        return flask_response_factory(read_one_task(task_id))

    @classmethod
    def put(cls, task_id):
        data = _task_parser.parse_args()

        data['id'] = task_id
        return flask_response_factory(update_one_task(**data))

    @classmethod
    def patch(cls, task_id):
        data = _task_state_parser.parse_args()
        data['id'] = task_id
        return flask_response_factory(update_task_state(**data))
