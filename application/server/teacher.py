import json


class Teacher:
    def __init__(self, name, subjects, balance, extremisms):
        self.name = name
        self.subjects = subjects
        self.balance = balance
        self.extremisms = extremisms


def load_teachers(json_path):
    teachers = []
    with open(json_path) as json_file:
        teachers_data = json.load(json_file)['teachers']
    for name, datas in teachers_data.items():
        teacher = Teacher(name, **datas)
        teachers.append(teacher)
    return teachers
