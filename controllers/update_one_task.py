from entities.response import Response
from facade.task_facade import task_facade
from responses import task_put_responses as responses
from model.task_model import TaskModel


def update_one_task(id, name, description, state):
    try:
        if not task_facade.task_valdation(name, description, state) and task_facade.id_validation(id):
            raise responses.WrongRequest

        task_to_update = TaskModel.get_one_task(id)

        if not task_to_update:
            raise responses.NotFound

        TaskModel.update_task(id, name, description, state)

        code = responses.http_responses['UpdateSuccess']['code']
        message = responses.http_responses['UpdateSuccess']['message']
        return Response(code, message)

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
