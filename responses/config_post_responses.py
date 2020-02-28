http_responses = {
    'ConfigSaved': {
        'message': 'Configuration saved successfully',
        'code': '201'
    },
    'WrongRequest': {
        'message': 'The configuration parameters has wrong values',
        'code': '400 '
    },
    'UnexpectedError': {
        'message': 'There is a problem with the data base. Please try later',
        'code': '500 '
    }
}

class WrongRequest(Exception):
    pass