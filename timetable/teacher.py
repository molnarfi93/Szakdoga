import math

class Teacher:
    def __init__(self, name, either_subject, other_subject):
        self.name = name
        self.either_subject = either_subject
        self.other_subject = other_subject
        self.sum_periods = 0
        self.weekly_periods = math.inf
