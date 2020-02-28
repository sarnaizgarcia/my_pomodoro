import traceback

from entities.response import Response
from model.configuration_model import ConfigurationModel
import responses.config_get_responses as responses
from entities.config import ConfigurationEntity


def read_config():
    try:
        config_model = ConfigurationModel.get_configuration()

        if not config_model:
            raise responses.NotFound
        config_response = ConfigurationEntity(
            config_model.pomodoro,
            config_model.short_break,
            config_model.long_break
        )

        return Response('200 ', config_response.to_json())
    except responses.NotFound:
        code = responses.http_responses['NotFound']['code']
        message = responses.http_responses['NotFound']['message']
        return Response(code, message)
    except Exception:
        print('Error: {}'.format(traceback.format_exc()))
        code = responses.http_responses['UnexpectedError']['code']
        message = responses.http_responses['UnexpectedError']['message']
        return Response(code, message)
