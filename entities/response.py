import json

class Response():

    def __init__(self, status, body):
        self.status = status
        self.body = json.dumps(body)