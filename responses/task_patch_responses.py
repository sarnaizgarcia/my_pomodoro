http_responses = {
    'UpdateSuccess': {
        'message': 'Task state updated',
        'code': '200 '
    },
    'Conflict': {
        'message': 'Only one task can be in state ongoing',
        'code': '409 '
    },
    'WrongRequest': {
        'message': 'Wrong state values',
        'code': '400 '
    },
    'NotFound': {
        'message': 'Task not found',
        'code': '404 '
    },
    'UnexpectedError': {
        'message': 'There is a problem with the data base. Please try later',
        'code': '500 '
    }
}


class WrongRequest(Exception):
    pass


class NotFound(Exception):
    pass


class Conflict(Exception):
    pass
