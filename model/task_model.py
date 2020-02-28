from db import db


class TaskModel(db.Model):
    __tablename__ = 'task'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30))
    description = db.Column(db.String(250))
    state = db.Column(db.String(30))

    def __init__(self, name, description, state):
        self.name = name
        self.description = description
        self.state = state

    def save(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def update_task(cls, id, name, description, state):
        cls.query.filter_by(id=id).update({
            "name": name,
            "description": description,
            "state": state
        },
            synchronize_session=False)

        db.session.commit()

    @classmethod
    def get_all_tasks(cls):
        return cls.query.all()

    @classmethod
    def task_count(cls):
        return cls.query.count()

    @classmethod
    def change_state(cls, id, state):
        cls.query.filter_by(id=id).update({
            "state": state
        },
            synchronize_session=False)

        db.session.commit()

    @classmethod
    def get_one_task(cls, id):
        return cls.query.filter_by(id=id).first()

    @classmethod
    def number_of_ongoing_task(cls):
        return cls.query.filter_by(state="ongoing").count()

    @classmethod
    def number_of_done_task(cls):
        return cls.query.filter_by(state="done").count()
