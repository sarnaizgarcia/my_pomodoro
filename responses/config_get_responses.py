http_responses = {
    'NotFound': {
        'message': 'Not configuration has been set yet',
        'code': '404 '
    },
    'UnexpectedError': {
        'message': 'There is a problem with the data base. Please try later',
        'code': '500 '
    }
}

class NotFound(Exception):
    pass