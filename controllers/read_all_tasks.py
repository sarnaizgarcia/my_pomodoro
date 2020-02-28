import traceback

from entities.task import TaskEntity
from entities.response import Response
from responses import tasks_get_responses as responses
from model.task_model import TaskModel


def read_all_tasks():
    try:
        result = list()

        if (TaskModel.task_count() > 0):
            list_tasks = TaskModel.get_all_tasks()
            for task_model in list_tasks:
                result.append(TaskEntity(
                    task_model.name, task_model.description, task_model.state).to_json())

        return Response(200, result)

    except Exception:
        print(traceback.format_exc())
        code = responses.http_responses['UnexpectedError']['code']
        message = responses.http_responses['UnexpectedError']['message']
        return Response(code, message)
