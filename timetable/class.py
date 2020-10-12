class Class:

    def __init__(self, name, grade, subject, type, weekly_periods, headcount, no):
        """
        Initialize a new class instance.
        :param name: 
        :param grade: 
        :param subject: 
        :param type: 
        :param name: 
        """
        self.name = name
        self.grade = grade
        self.subject = subject
        self.type = type
        self.weekly_periods = weekly_periods
        self.sum_periods = 0
        self.headcount = headcount
        self.room = ""
        self.teacher = None
        self.itemized = False
        self.no = no

