class TaskFacade():

    def task_validation(self, name, description, state):
        is_valid = self.string_validation(name)
        is_valid = is_valid and self.string_validation(description)
        is_valid = is_valid and self.string_validation(state)

        return is_valid and self.state_validation(state)

    def id_validation(self, task_id):
        return (type(task_id) == int) and (task_id > 0)

    def string_validation(self, value):
        return (value != None) and (len(value) > 0)

    def state_validation(self, state):
        return state in ['pending', 'ongoing', 'done']

    def state_change_validation(self, current_state, new_state):
        valid_changes = {
            'pending': 'ongoing',
            'ongoing': 'done',
            'done': 'pending'
        }

        return valid_changes[current_state] == new_state


task_facade = TaskFacade()
