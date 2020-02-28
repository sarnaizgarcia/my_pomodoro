import traceback

from entities.response import Response
from entities.task import TaskEntity
from responses import task_get_one_responses as responses
from model.task_model import TaskModel
from facade.task_facade import task_facade


def read_one_task(task_id):
    try:

        if not task_facade.id_validation(task_id):
            raise responses.WrongRequest

        task_found = TaskModel.get_one_task(task_id)

        if not task_found:
            raise responses.NotFound

        task = TaskEntity(
            task_found.name, task_found.description, task_found.state)

        return Response(200, task.to_json())

    except responses.NotFound:
        code = responses.http_responses['NotFound']['code']
        message = responses.http_responses['NotFound']['message']
        return Response(code, message)
    except responses.WrongRequest:
        code = responses.http_responses['WrongRequest']['code']
        message = responses.http_responses['WrongRequest']['message']
        return Response(code, message)
    except Exception:
        code = responses.http_responses['UnexpectedError']['code']
        message = responses.http_responses['UnexpectedError']['message']
        return Response(code, message)
