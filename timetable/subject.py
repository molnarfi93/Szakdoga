class Subject:

    def __init__(self, name, type, weekly_periods):
        self._name = name
        self._type = type
        self._weekly_periods = weekly_periods

    @staticmethod
    def create_subject_from_dict(name, d):
        """
        """
        subject = Subject(name, d['type'], d['weekly_periods'])
        return subject
