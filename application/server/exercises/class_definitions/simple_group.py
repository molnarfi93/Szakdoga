import json


class SimpleGroup:
    def __init__(self, name, grade, subjects, headcount):
        self.name = name
        self.grade = grade
        self.subjects = subjects
        self.headcount = headcount
        self.room = ""


def load_groups(json_path):
    groups = []
    with open(json_path) as json_file:
        groups_data = json.load(json_file)['groups']
    for no, datas in groups_data.items():
        group = SimpleGroup(no, **datas)
        groups.append(group)
    return groups

