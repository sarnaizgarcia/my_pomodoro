http_responses = {
    'WrongRequest': {
        'message': 'Wrong id format',
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