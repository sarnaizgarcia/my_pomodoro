import traceback

from entities.response import Response
from facade.config_facade import config_facade
from responses import config_post_responses as responses
from model.configuration_model import ConfigurationModel
from services.pomodoro_counter import pomodoro_counter


def create_config(pomodoro, short_break, long_break):

    try:
        if not config_facade.config_validation(pomodoro, short_break, long_break):
            raise responses.WrongRequest

        total_config = ConfigurationModel.config_count()

        if total_config > 0:
            ConfigurationModel.uptate_configuration(
                pomodoro, short_break, long_break)
        else:
            config_model = ConfigurationModel(
                pomodoro, short_break, long_break)
            config_model.save()

        pomodoro_counter.update_config(pomodoro, short_break, long_break)
        code = responses.http_responses['ConfigSaved']['code']
        message = responses.http_responses['ConfigSaved']['message']
        return Response(code, message)
    except responses.WrongRequest:
        message = responses.http_responses['WrongRequest']['message']
        code = responses.http_responses['WrongRequest']['code']
        return Response(code, message)
    except Exception:
        print(traceback.format_exc())
        message = responses.http_responses['UnexpectedError']['message']
        code = responses.http_responses['UnexpectedError']['code']
        return Response(code, message)
