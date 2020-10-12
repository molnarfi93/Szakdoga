import math
class Room:
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
class Class:
    def __init__(self, name, grade, subject, type, weekly_periods, headcount, no):
        self.name = name
        self.grade = grade
        self.subject = subject
        self.type = type
        self.weekly_periods = weekly_periods
        self.sum_periods = 0
        self.headcount = headcount
        self.room = ""
        self.teacher = math.nan
        self.itemized = False
        self.no = no
class Teacher:
    def __init__(self, name, either_subject, other_subject):
        self.name = name
        self.either_subject = either_subject
        self.other_subject = other_subject
        self.weekly_periods = 10
        self.sum_periods = 0
class Assignment:
    def __init__(self, klass, room, teacher):
        self.klass = klass
        self.room = room
        self.teacher = teacher
    def __str__(self):
        return "%s %s %s" %(self.klass, self.room, self.teacher)