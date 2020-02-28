class ConfigFacade():

    def config_validation(self, pomodoro, short_break, long_break):
        is_valid = self.integer_validation(pomodoro)
        is_valid = is_valid and self.integer_validation(short_break)

        return is_valid and self.integer_validation(long_break) and (short_break < long_break)

    def integer_validation(self, value):
        return (type(value) == int) and (value > 0)


config_facade = ConfigFacade()
