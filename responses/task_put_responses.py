http_responses = {
    'UpdateSuccess': {
        'message': 'Task updated',
        'code': '200 '
    },
    'WrongRequest': {
        'message': 'Wrong task values',
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