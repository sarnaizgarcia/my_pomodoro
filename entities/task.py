class TaskEntity:

    def __init__(self, title, description, state):
        self.title = title
        self.description = description
        self.state = state


    def to_json(self):
        return self.__dict__