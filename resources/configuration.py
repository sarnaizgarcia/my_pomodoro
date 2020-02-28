from flask_restful import Resource, reqparse

from helper.flask_response_factory import flask_response_factory
from controllers.read_config import read_config
from controllers.create_config import create_config

_config_parser = reqparse.RequestParser()
_config_parser.add_argument('pomodoro', type=int, required=True)
_config_parser.add_argument('short_break', type=int, required=True)
_config_parser.add_argument('long_break', type=int, required=True)


class Configuration(Resource):

    @classmethod
    def get(cls):
        return flask_response_factory(read_config())

    @classmethod
    def post(cls):
        data = _config_parser.parse_args()

        return flask_response_factory(create_config(**data))
