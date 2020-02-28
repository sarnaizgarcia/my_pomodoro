import traceback

from entities.response import Response
from facade.task_facade import task_facade
from model.task_model import TaskModel
from responses import task_post_responses as responses


def create_task(name, description, state):
    try:
        if not task_facade.task_validation(name, description, state):
            raise responses.WrongRequest

        task_model = TaskModel(name, description, state)
        task_model.save()

        code = responses.http_responses['TaskSaved']['code']
        message = responses.http_responses['TaskSaved']['message']

        return Response(code, message)

    except responses.WrongRequest:
        code = responses.http_responses['WrongRequest']['code']
        message = responses.http_responses['WrongRequest']['message']

        return Response(code, message)
    except Exception:
        print(traceback.format_exc())
        code = responses.http_responses['UnexpectedError']['code']
        message = responses.http_responses['UnexpectedError']['message']

        return Response(code, message)
