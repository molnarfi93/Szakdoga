class Teacher:

    def __init__(self, name, subjects):
        """
        Initialize a new teacher instance.
        :param name: unique name of the teacher
        :param subjects: list of subjects
        """
        self.name = name
        self.subjects = subjects
        self.weekly_periods = 10
        self.sum_periods = 0

