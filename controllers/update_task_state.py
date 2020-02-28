import traceback

from entities.response import Response
from facade.task_facade import task_facade
from model.task_model import TaskModel
from responses import task_patch_responses as responses
from services.send_message import pomodoro_clock


def update_task_state(id, state):
    try:
        if not (task_facade.id_validation(id) and task_facade.state_validation(state)):
            raise responses.WrongRequest

        ongoing_number = TaskModel.number_of_ongoing_task()

        if (state == 'ongoing') and (ongoing_number > 0):
            raise responses.Conflict

        task_to_update = TaskModel.get_one_task(id)
        if not task_to_update:
            raise responses.NotFound

        if not task_facade.state_change_validation(task_to_update.state, state):
            raise responses.WrongRequest

        TaskModel.change_state(id, state)

        if state == 'ongoing':
            pomodoro_clock.start_clock()
        elif state == 'done':
            pomodoro_clock.start_clock()

        code = responses.http_responses['UpdateSuccess']['code']
        message = responses.http_responses['UpdateSuccess']['message']
        return Response(code, message)

    except responses.NotFound:
        code = responses.http_responses['NotFound']['code']
        message = responses.http_responses['NotFound']['message']
        return Response(code, message)
    except responses.WrongRequest:
        code = responses.http_responses['NotFound']['code']
        message = responses.http_responses['NotFound']['message']
        return Response(code, message)
    except responses.Conflict:
        code = responses.http_responses['Conflict']['code']
        message = responses.http_responses['Conflict']['message']
        return Response(code, message)
    except Exception:
        print(traceback.format_exc())
        code = responses.http_responses['UnexpectedError']['code']
        message = responses.http_responses['UnexpectedError']['message']
        return Response(code, message)
