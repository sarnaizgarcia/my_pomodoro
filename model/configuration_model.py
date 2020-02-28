from db import db


class ConfigurationModel(db.Model):
    __tablename__ = 'configuration'

    id = db.Column(db.Integer, primary_key=True)
    pomodoro = db.Column(db.Integer)
    short_break = db.Column(db.Integer)
    long_break = db.Column(db.Integer)

    def __init__(self, pomodoro, short_break, long_break):
        self.pomodoro = pomodoro
        self.short_break = short_break
        self.long_break = long_break

    def save(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_configuration(cls):
        result = None
        total_config = cls.query.count()
        if (total_config > 0):
            result = cls.query.all()[0]
        return result

    @classmethod
    def config_count(cls):
        return cls.query.count()

    @classmethod
    def uptate_configuration(cls, pomodoro, short_break, long_break):
        cls.query.filter_by(id=1).update({
            "pomodoro": pomodoro,
            "short_break": short_break,
            "long_break": long_break
        },
            synchronize_session=False)

        db.session.commit()
